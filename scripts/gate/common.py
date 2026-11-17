"""Shared helpers for the ActiveInferenceJournal gate arms.

The gate is deliberately stdlib-only: every arm runs on the plain ``python3``
already present on a GitHub runner and on a developer machine, so local runs and
CI runs are the same code with no environment to install.
"""

from __future__ import annotations

import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]

JU_PIN = ROOT / ".github" / "journal-utilities-pin.json"
GNN_PIN = ROOT / ".github" / "gnn-pin.json"

# Python ranges are read from the pinned GNN package's metadata at install time;
# this is the range its ``requires-python`` declares, quoted so the failure is
# actionable instead of a bare pip error.
GNN_PYTHON_RANGE = ">=3.11,<3.15"


class GateError(SystemExit):
    """A gate failure with a reviewer-facing message."""

    def __init__(self, message: str, code: int = 1) -> None:
        super().__init__(f"gate: {message}")
        self.code = code


@dataclass
class Step:
    label: str
    command: str
    seconds: float


def log(message: str) -> None:
    print(f"gate: {message}", flush=True)


def read_pin(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise GateError(f"missing pin file {path.relative_to(ROOT)}") from None
    except json.JSONDecodeError as exc:
        raise GateError(f"{path.relative_to(ROOT)} is not valid JSON: {exc}") from None
    if not isinstance(data, dict):
        raise GateError(f"{path.relative_to(ROOT)} must hold a JSON object")
    return data


def cache_dir() -> Path:
    base = os.environ.get("GATE_CACHE")
    root = Path(base) if base else Path(tempfile.gettempdir()) / "aij-gate"
    root.mkdir(parents=True, exist_ok=True)
    return root


def run(label: str, command: list[str], cwd: Path | None = None) -> Step:
    """Run one command, echo its output, and fail the gate if it exits nonzero."""
    started = time.perf_counter()
    print(f"\n$ {' '.join(command)}", flush=True)
    completed = subprocess.run(command, cwd=str(cwd or ROOT))
    seconds = time.perf_counter() - started
    print(f"gate: {label} -> exit {completed.returncode} in {seconds:.2f}s", flush=True)
    if completed.returncode != 0:
        raise GateError(f"{label} failed (exit {completed.returncode})")
    return Step(label=label, command=" ".join(command), seconds=seconds)


def git(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd or ROOT),
        capture_output=True,
        text=True,
    )


def _object_git(
    args: list[str], source: Path, *, input: bytes | None = None, network: bool = False
) -> subprocess.CompletedProcess:
    """Read literal objects without replacement refs, lazy fetches or caller Git env."""
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(
        GIT_CONFIG_GLOBAL=os.devnull,
        GIT_CONFIG_NOSYSTEM="1",
        GIT_TERMINAL_PROMPT="0",
        GIT_NO_REPLACE_OBJECTS="1",
        GIT_NO_LAZY_FETCH="1",
        GIT_OPTIONAL_LOCKS="0",
        GIT_ALLOW_PROTOCOL="https" if network else "",
    )
    return subprocess.run(
        ["git", "-c", "core.fsmonitor=false", "-c", f"core.hooksPath={os.devnull}", *args],
        cwd=source,
        env=env,
        input=input,
        capture_output=True,
    )


def _hash_object(clone: Path, revision: str) -> bool:
    # Do not inherit an enclosing repository when passed an exported subdirectory.
    if not (clone / ".git").exists() and not (
        (clone / "HEAD").is_file() and (clone / "objects").is_dir()
    ):
        return False
    result = _object_git(["cat-file", "-t", revision], clone)
    return result.returncode == 0 and result.stdout.strip() == b"commit"


def _local_clone() -> Path | None:
    override = os.environ.get("GATE_JU_CLONE")
    if override:
        return Path(override).expanduser().resolve()
    sibling = ROOT.parent / "Journal_Utilities"
    if (sibling / ".git").exists():
        return sibling
    return None


def _extract_tree(source: Path, revision: str, destination: Path) -> None:
    """Materialize every committed blob, not archive/checkout-transformed bytes."""
    listed = _object_git(["ls-tree", "-rz", "--full-tree", revision], source)
    if listed.returncode:
        raise GateError(f"cannot read the committed tree {revision} from {source}")
    entries: list[tuple[bytes, bytes, Path]] = []
    for record in listed.stdout.split(b"\0"):
        if not record:
            continue
        metadata, name = record.split(b"\t", 1)
        mode, kind, oid = metadata.split()
        relative = PurePosixPath(os.fsdecode(name))
        if (
            relative.is_absolute()
            or any(part in {"", ".", ".."} or part.lower() == ".git" for part in os.fsdecode(name).split("/"))
            or kind != b"blob"
            or mode not in {b"100644", b"100755", b"120000"}
        ):
            raise GateError(f"cannot bind committed entry {os.fsdecode(name)!r} ({mode.decode()})")
        entries.append((mode, oid, destination / relative))

    objects = _object_git(
        ["cat-file", "--batch"], source,
        input=b"".join(oid + b"\n" for _, oid, _ in entries),
    )
    if objects.returncode:
        raise GateError(f"cannot read all blobs for {revision} from {source}")
    stream = io.BytesIO(objects.stdout)
    links: list[tuple[Path, str]] = []
    for mode, oid, target in entries:
        header = stream.readline().split()
        if len(header) != 3 or header[:2] != [oid, b"blob"]:
            raise GateError(f"missing exact blob {oid.decode()} for {target.relative_to(destination)}")
        size = int(header[2])
        body = stream.read(size)
        if len(body) != size or stream.read(1) != b"\n":
            raise GateError(f"incomplete blob {oid.decode()}")
        parent = destination
        for part in target.relative_to(destination).parts[:-1]:
            child = parent / part
            if child.exists() and part not in os.listdir(parent):
                raise GateError(f"committed directory names collide at {child.relative_to(destination)}")
            child.mkdir(exist_ok=True)
            parent = child
        if target.exists() or target.is_symlink():
            raise GateError(f"committed paths collide at {target.relative_to(destination)}")
        if mode == b"120000":
            links.append((target, os.fsdecode(body)))
        else:
            target.write_bytes(body)
            target.chmod(0o755 if mode == b"100755" else 0o644)
    for target, link in links:
        if os.path.isabs(link):
            raise GateError(f"committed symlink escapes the snapshot: {target.relative_to(destination)}")
        target.symlink_to(link)
    for target, _ in links:
        try:
            target.resolve().relative_to(destination.resolve())
        except (ValueError, RuntimeError):
            raise GateError(f"committed symlink escapes or cycles: {target.relative_to(destination)}") from None


def _clone_at_pin(repository: str, revision: str, destination: Path) -> None:
    """Fetch into a newly owned bare object store; never check out or reset a caller."""
    for args in (
        ["init", "--bare", "--quiet"],
        ["fetch", "--quiet", "--depth", "1", "--no-tags", f"https://github.com/{repository}.git", revision],
    ):
        completed = _object_git(args, destination, network=True)
        if completed.returncode != 0:
            raise GateError(f"cannot acquire {repository}@{revision} into {destination}")
    if not _hash_object(destination, revision):
        raise GateError(f"acquisition did not provide exact commit {revision}")


def _producer_source(repository: str, revision: str, override: str | None) -> Path:
    if override is not None:
        source = Path(override).expanduser().resolve()
        if not override.strip() or not _hash_object(source, revision):
            raise GateError(
                f"{source} does not provide exact Git commit {revision}; "
                "a mutable .gate-pin export is not an object source"
            )
        return source

    local = _local_clone()
    if local is not None:
        if _hash_object(local, revision):
            return local
        if os.environ.get("GATE_JU_CLONE"):
            raise GateError(f"GATE_JU_CLONE {local} does not provide exact Git commit {revision}")

    cache = cache_dir()
    # Old caches may supply objects, but neither their stamp nor their worktree is trusted.
    candidates = [cache / f"ju-{revision[:12]}", *sorted(cache.glob(f"ju-objects-{revision}-*"))]
    for candidate in candidates:
        if _hash_object(candidate, revision):
            return candidate

    source = Path(tempfile.mkdtemp(prefix=f"ju-objects-{revision}-", dir=cache))
    try:
        log(f"journal-utilities: fetching {repository}@{revision}")
        _clone_at_pin(repository, revision, source)
    except BaseException:
        shutil.rmtree(source)
        raise
    return source


@contextmanager
def journal_utilities(override: str | None = None) -> Iterator[Path]:
    """Yield an owned exact-commit snapshot, valid only inside the ``with`` block.

    Explicit sources must already contain the pinned commit; their HEAD, index,
    dirty files and stamps are irrelevant and untouched. Without an explicit
    source, local objects or object caches are preferred before a cold fetch.
    Snapshots are never reused and are removed on success or failure.
    """
    pin = read_pin(JU_PIN)
    repository = pin.get("repository")
    revision = pin.get("revision")
    if repository != "ActiveInferenceInstitute/Journal_Utilities" or not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise GateError(f"{JU_PIN.relative_to(ROOT)} needs the Journal-Utilities repository and a full commit id")
    source = _producer_source(repository, revision, override)
    with tempfile.TemporaryDirectory(prefix=f"ju-snapshot-{revision[:12]}-", dir=cache_dir()) as tmp:
        tree = Path(tmp)
        try:
            _extract_tree(source, revision, tree)
        except (OSError, ValueError) as exc:
            raise GateError(f"cannot materialize exact producer snapshot: {exc}") from None
        if not (tree / "scripts" / "validate_journal.py").is_file():
            raise GateError(f"{revision} has no Journal-Utilities validator")
        log(f"journal-utilities: snapshot {tree} @ {revision} from {source}")
        yield tree


def find_python(candidates: list[str]) -> str:
    for candidate in candidates:
        if not candidate:
            continue
        resolved = shutil.which(candidate) if os.sep not in candidate else candidate
        if resolved and Path(resolved).exists():
            return resolved
    raise GateError(
        "no Python interpreter in " + GNN_PYTHON_RANGE + " found; the pinned GNN "
        "package declares that range. Set GATE_PYTHON, or install one with "
        "`uv python install 3.12`."
    )


def tracked_markdown() -> list[Path]:
    """Every tracked Markdown file; falls back to a walk outside a Git tree."""
    listed = git(["ls-files", "-z", "--", "*.md"])
    if listed.returncode == 0 and listed.stdout:
        return [ROOT / name for name in listed.stdout.split("\0") if name]
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


if __name__ == "__main__":  # pragma: no cover - debugging helper
    print(json.dumps({"root": str(ROOT), "python": sys.version}))
