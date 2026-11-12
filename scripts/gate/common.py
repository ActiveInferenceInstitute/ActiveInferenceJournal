"""Shared helpers for the ActiveInferenceJournal gate arms.

The gate is deliberately stdlib-only: every arm runs on the plain ``python3``
already present on a GitHub runner and on a developer machine, so local runs and
CI runs are the same code with no environment to install.
"""

from __future__ import annotations

import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

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


def _hash_object(clone: Path, revision: str) -> bool:
    return git(["cat-file", "-e", f"{revision}^{{commit}}"], cwd=clone).returncode == 0


def _local_clone() -> Path | None:
    override = os.environ.get("GATE_JU_CLONE")
    if override:
        return Path(override).expanduser().resolve()
    sibling = ROOT.parent / "Journal_Utilities"
    if (sibling / ".git").exists():
        return sibling
    return None


def _extract_archive(clone: Path, revision: str, destination: Path) -> None:
    archive = subprocess.run(
        ["git", "-C", str(clone), "archive", revision],
        capture_output=True,
        check=True,
    )
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as tar:
        tar.extractall(destination, filter="data")


def _clone_at_pin(repository: str, revision: str, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.setdefault("GIT_TERMINAL_PROMPT", "0")
    for args in (
        ["init", "--quiet"],
        ["remote", "add", "origin", f"https://github.com/{repository}.git"],
        ["fetch", "--quiet", "--depth", "1", "origin", revision],
        ["checkout", "--quiet", "--detach", "FETCH_HEAD"],
    ):
        completed = subprocess.run(["git", *args], cwd=str(destination), env=env)
        if completed.returncode != 0:
            raise GateError(
                f"cannot materialize {repository}@{revision[:12]} into {destination}"
            )


def journal_utilities(override: str | None = None) -> Path:
    """Return a Journal-Utilities tree at the pinned revision.

    An explicit ``--utilities`` path is trusted but checked: a Git tree must sit
    at the pinned commit, and an exported tree must carry the materialization
    stamp written below. Anything else is refused, because running the gate
    against an unpinned engine silently changes what the result means.
    """
    pin = read_pin(JU_PIN)
    repository = pin.get("repository", "")
    revision = pin.get("revision", "")
    if not repository or not revision:
        raise GateError(f"{JU_PIN.relative_to(ROOT)} lacks repository/revision")

    if override:
        path = Path(override).expanduser().resolve()
        if not (path / "scripts" / "validate_journal.py").exists():
            raise GateError(f"{path} is not a Journal-Utilities checkout")
        if (path / ".git").exists():
            head = git(["rev-parse", "HEAD"], cwd=path).stdout.strip()
            if head != revision:
                raise GateError(
                    f"{path} is at {head[:12]}, but {JU_PIN.relative_to(ROOT)} pins "
                    f"{revision[:12]}; check out the pin or update the pin file"
                )
        else:
            stamp = path / ".gate-pin"
            if not stamp.exists() or stamp.read_text(encoding="utf-8").strip() != revision:
                raise GateError(
                    f"{path} carries no .gate-pin stamp for {revision[:12]}; "
                    "run the gate without --utilities to materialize the pin"
                )
        log(f"journal-utilities: {path} @ {revision[:12]}")
        return path

    destination = cache_dir() / f"ju-{revision[:12]}"
    stamp = destination / ".gate-pin"
    if stamp.exists() and stamp.read_text(encoding="utf-8").strip() == revision:
        log(f"journal-utilities: cached {destination}")
        return destination

    if destination.exists():
        shutil.rmtree(destination)

    clone = _local_clone()
    if clone is not None and _hash_object(clone, revision):
        log(f"journal-utilities: exporting {revision[:12]} from {clone}")
        _extract_archive(clone, revision, destination)
    else:
        log(f"journal-utilities: fetching {repository}@{revision[:12]}")
        _clone_at_pin(repository, revision, destination)

    stamp.write_text(revision + "\n", encoding="utf-8")
    return destination


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
