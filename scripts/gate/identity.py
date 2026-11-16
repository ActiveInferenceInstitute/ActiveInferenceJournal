"""Record identity for the publishing group: one schema, one grammar.

``docs/workflows/record-identity.schema.json`` is the only copy of the identity
grammar (namespaces, patterns, the record path rule). This module enforces its
``x-identity`` block; nothing here restates a pattern, so editing the schema
changes behaviour instead of creating a second source of truth.

The group contract, ``docs/workflows/publishing.md``, records the schema's
sha256. A member repository does not re-implement any of this: copy this module
and the schema, record their digest in the contract copy, and run
``--verify-copy`` before every release. The check fails as soon as the member's
copy and the digest the contract records disagree, which is the whole point of
the drift test.

Stdlib only, so the same bytes run on a GitHub runner and on a laptop.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import sys
from dataclasses import dataclass
from pathlib import Path, PureWindowsPath

SCHEMA_VERSION = "record-identity/v1"
# A pinned copy is any artifact kind a member can carry, not just a schema: the
# contract pins the Python modules too, and a `.json`-only parser would make
# those entries unverifiable.
ARTIFACT_SUFFIXES = ("json", "py", "mjs", "sh", "md", "ts")
DIGEST_LINE = re.compile(
    r"^\s*([\w.+@-]+\.(?:" + "|".join(ARTIFACT_SUFFIXES) + r"))\s{2,}([0-9a-f]{64})\s*$"
)
# Where a recorded name may live, relative to the repository root. A fixed list
# keeps resolution deterministic: no directory walk, no ambiguity by accident.
ARTIFACT_LOCATIONS = ("scripts/gate", "docs/workflows", ".github", "")


class IdentityError(Exception):
    """A contract or corpus problem with a reviewer-facing message."""


@dataclass(frozen=True)
class Spec:
    """The compiled ``x-identity`` block of the canonical schema."""

    path: Path
    document: dict
    patterns: dict[str, re.Pattern[str]]
    leaf_key: str
    ancestor_key: str
    duplicate_key: str
    index_file: str
    derived_prefix_components: int
    transcript_flag: dict
    index_record_keys: tuple[str, ...]

    def digest(self) -> str:
        return hashlib.sha256(self.path.read_bytes()).hexdigest()

    def relative(self, root: Path) -> str:
        try:
            return self.path.relative_to(root).as_posix()
        except ValueError:
            return str(self.path)


def _require(mapping: dict, key: str, where: str) -> object:
    if key not in mapping:
        raise IdentityError(f"{where} lacks `{key}`")
    return mapping[key]


def _relative_path(value: object, where: str) -> Path:
    """Admit one unambiguous, corpus-relative POSIX path before filesystem access."""
    if (
        not isinstance(value, str)
        or not value
        or "\0" in value
        or "\\" in value
        or PureWindowsPath(value).drive
        or any(part in {"", ".", ".."} for part in value.split("/"))
    ):
        raise IdentityError(f"{where}: expected a relative path without traversal")
    return Path(value)


def _contained_path(root: Path, value: object, where: str) -> Path:
    relative = _relative_path(value, where)
    try:
        resolved = (root / relative).resolve()
    except (OSError, RuntimeError, ValueError) as exc:
        raise IdentityError(f"{where}: cannot resolve path: {exc}") from None
    if not resolved.is_relative_to(root):
        raise IdentityError(f"{where}: path escapes the corpus")
    return resolved


def _read_json(path: Path) -> object:
    if not stat.S_ISREG(path.stat().st_mode):
        raise IdentityError("expected a regular JSON file")
    return json.loads(path.read_text(encoding="utf-8"))

def load_schema(path: Path) -> Spec:
    """Parse and compile the canonical schema, refusing an incomplete contract."""
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise IdentityError(f"missing identity schema {path}") from None
    except json.JSONDecodeError as exc:
        raise IdentityError(f"{path} is not valid JSON: {exc}") from None
    if not isinstance(document, dict):
        raise IdentityError(f"{path} must hold a JSON object")

    version = document.get("schema_version")
    if version != SCHEMA_VERSION:
        raise IdentityError(
            f"{path}: schema_version is {version!r}, expected {SCHEMA_VERSION!r}"
        )
    block = _require(document, "x-identity", f"{path}")
    if not isinstance(block, dict):
        raise IdentityError(f"{path}: x-identity must be an object")

    raw_patterns = _require(block, "patterns", f"{path}: x-identity")
    patterns: dict[str, re.Pattern[str]] = {}
    if not isinstance(raw_patterns, dict):
        raise IdentityError(f"{path}: x-identity.patterns must be an object")
    for name, pattern in raw_patterns.items():
        if not isinstance(pattern, str):
            raise IdentityError(f"{path}: pattern `{name}` must be a string")
        try:
            patterns[name] = re.compile(pattern)
        except re.error as exc:
            raise IdentityError(f"{path}: pattern `{name}` is invalid: {exc}") from None
    for required in ("video_id", "session_id"):
        if required not in patterns:
            raise IdentityError(f"{path}: x-identity.patterns lacks `{required}`")
    if "video_id" not in patterns["session_id"].groupindex:
        raise IdentityError(f"{path}: session_id pattern must capture `video_id`")

    flag = _require(block, "transcript_flag", f"{path}: x-identity")
    if not isinstance(flag, dict):
        raise IdentityError(f"{path}: x-identity.transcript_flag must be an object")
    for key in ("key", "artifact"):
        value = _require(flag, key, f"{path}: x-identity.transcript_flag")
        if not isinstance(value, str) or not value:
            raise IdentityError(f"{path}: transcript_flag.{key} must be a nonempty string")
    _relative_path(flag["artifact"], f"{path}: transcript_flag.artifact")

    keys: dict[str, str] = {}
    for key in ("leaf_key", "ancestor_key", "duplicate_key", "index_file"):
        value = _require(block, key, f"{path}: x-identity")
        if not isinstance(value, str) or not value:
            raise IdentityError(f"{path}: x-identity.{key} must be a nonempty string")
        keys[key] = value
    _relative_path(keys["index_file"], f"{path}: x-identity.index_file")
    index_keys = _require(block, "index_record_keys", f"{path}: x-identity")
    expected_keys = {
        "path", keys["leaf_key"], keys["ancestor_key"], "parts",
        flag["key"], keys["duplicate_key"],
    }
    if (
        not isinstance(index_keys, list)
        or not all(isinstance(key, str) for key in index_keys)
        or len(index_keys) != len(expected_keys)
        or set(index_keys) != expected_keys
    ):
        raise IdentityError(
            f"{path}: index_record_keys must name {', '.join(sorted(expected_keys))}"
        )

    components = _require(block, "derived_prefix_components", f"{path}: x-identity")
    if type(components) is not int or components < 1:
        raise IdentityError(f"{path}: derived_prefix_components must be a positive integer")

    return Spec(
        path=path,
        document=document,
        patterns=patterns,
        leaf_key=keys["leaf_key"],
        ancestor_key=keys["ancestor_key"],
        duplicate_key=keys["duplicate_key"],
        index_file=keys["index_file"],
        derived_prefix_components=components,
        transcript_flag=flag,
        index_record_keys=tuple(index_keys),
    )


def recorded_digests(contract: Path) -> dict[str, str]:
    """Read ``<file>  <sha256>`` lines; the contract's digest table in one format."""
    try:
        text = contract.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise IdentityError(f"missing contract {contract}") from None
    recorded: dict[str, str] = {}
    for line in text.splitlines():
        match = DIGEST_LINE.match(line)
        if match:
            recorded[match.group(1)] = match.group(2)
    return recorded


def repository_root(contract: Path) -> Path:
    """The checkout a contract belongs to: nearest ancestor holding `.git`."""
    for parent in contract.resolve().parents:
        if (parent / ".git").exists():
            return parent
    return contract.resolve().parents[2]


def resolve_artifact(root: Path, name: str) -> Path | None:
    """Find the file a recorded digest names, or None when it is not unique."""
    matches: list[Path] = []
    for location in ARTIFACT_LOCATIONS:
        relative = f"{location}/{name}" if location else name
        _contained_path(root.resolve(), relative, f"artifact {name}")
        candidate = root / relative
        if candidate.is_file():
            matches.append(candidate)
    return matches[0] if len(matches) == 1 else None


def check_contract(contract: Path, schema: Spec) -> list[str]:
    """Every recorded digest must match its file; the schema must be recorded."""
    failures: list[str] = []
    recorded = recorded_digests(contract)
    if not recorded:
        failures.append(
            f"{contract.name}: no `name  sha256` digest block; members cannot verify a copy"
        )
        return failures
    root = repository_root(contract)
    for name, expected in sorted(recorded.items()):
        try:
            if name == schema.path.name:
                relative = schema.path.absolute().relative_to(root).as_posix()
                path = _contained_path(root, relative, f"artifact {name}")
            else:
                path = resolve_artifact(root, name)
            if path is None:
                failures.append(
                    f"{contract.name}: records {name}, which is not one file under "
                    f"{root} at {', '.join(location or '.' for location in ARTIFACT_LOCATIONS)}"
                )
                continue
            if not stat.S_ISREG(path.stat().st_mode):
                raise IdentityError(f"artifact {name}: expected a regular file")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
        except (IdentityError, OSError, ValueError) as exc:
            failures.append(f"{contract.name}: cannot read artifact {name}: {exc}")
            continue
        if digest != expected:
            failures.append(
                f"{contract.name}: records {name} as {expected[:12]}, "
                f"but the file is {digest[:12]}; update the digest with the edit"
            )
    if schema.path.name not in recorded:
        failures.append(f"{contract.name}: records no digest for {schema.path.name}")
    return failures


def verify_copy(copy: Path, contract: Path) -> str | None:
    """Return a failure message when a member's artifact copy diverges."""
    try:
        if not stat.S_ISREG(copy.stat().st_mode):
            return f"{copy}: expected a regular file"
        digest = hashlib.sha256(copy.read_bytes()).hexdigest()
    except FileNotFoundError:
        return f"{copy}: no such file"
    except OSError as exc:
        return f"{copy}: cannot read artifact: {exc}"
    recorded = recorded_digests(contract)
    expected = recorded.get(copy.name)
    if expected is None:
        return f"{contract}: records no digest for {copy.name}"
    if expected != digest:
        return (
            f"{copy}: copy is {digest[:12]}, contract records {expected[:12]}; "
            "the copy drifted from the canonical artifact"
        )
    return None


def check_corpus(root: Path, spec: Spec) -> tuple[list[str], dict[str, int]]:
    """Check contained record identities, not the producer's raw transcript layer."""
    failures: list[str] = []
    counts = {"records": 0, "parts": 0, "duplicates": 0}
    try:
        root = root.resolve(strict=True)
        if not root.is_dir():
            raise IdentityError("corpus root must be a directory")
        index_path = _contained_path(root, spec.index_file, "index_file")
        index = _read_json(index_path)
    except (IdentityError, OSError, RuntimeError, ValueError) as exc:
        return [f"{spec.index_file}: {exc}"], counts

    records = index.get("items") if isinstance(index, dict) else None
    if not isinstance(records, list):
        return [f"{spec.index_file}: `items` must be a list"], counts

    # Admit every record path before any metadata read or duplicate resolution.
    admitted: list[tuple[dict, str]] = []
    known_paths: set[str] = set()
    for position, record in enumerate(records):
        where = f"{spec.index_file}: items[{position}]"
        if not isinstance(record, dict):
            failures.append(f"{where} is not an object")
            continue
        relative = record.get("path")
        try:
            record_dir = _contained_path(root, relative, f"{where}.path")
            if not record_dir.is_dir():
                raise IdentityError(f"{where}: record path is not a directory")
        except (IdentityError, OSError) as exc:
            failures.append(str(exc))
            continue
        if relative in known_paths:
            failures.append(f"{spec.index_file}: duplicate record path {relative}")
            continue
        known_paths.add(relative)
        admitted.append((record, relative))

    for record, relative in admitted:
        try:
            metadata_path = _contained_path(
                root, f"{relative}/metadata.json", f"{relative}: metadata.json"
            )
            metadata = _read_json(metadata_path)
        except (IdentityError, OSError, ValueError) as exc:
            failures.append(f"{relative}: metadata.json: {exc}")
            continue
        if not isinstance(metadata, dict):
            failures.append(f"{relative}: metadata.json must hold an object")
            continue

        counts["records"] += 1
        for key in spec.index_record_keys:
            if key != spec.duplicate_key and key not in record:
                failures.append(f"{relative}: INDEX record lacks `{key}`")

        # Use the admitted logical path, never parents of the host's corpus root.
        path = Path(relative)
        leaf = metadata.get(spec.leaf_key)
        if leaf != path.name:
            failures.append(
                f"{relative}: {spec.leaf_key} is {leaf!r}, but the directory is "
                f"{path.name!r}; the item id must name its own directory"
            )
        series = metadata.get(spec.ancestor_key)
        if not isinstance(series, str) or series not in path.parts[:-1]:
            failures.append(
                f"{relative}: {spec.ancestor_key} is {series!r}, which names no "
                "directory above the item inside the corpus"
            )
        for key in (spec.leaf_key, spec.ancestor_key):
            if record.get(key) != metadata.get(key):
                failures.append(f"{relative}: INDEX `{key}` disagrees with metadata.json")

        parts = metadata.get("parts")
        video_ids: list[object] = []
        valid_video_ids: set[str] = set()
        if not isinstance(parts, list):
            failures.append(f"{relative}: `parts` must be a list")
        else:
            for position, part in enumerate(parts):
                if not isinstance(part, dict):
                    failures.append(f"{relative}: parts[{position}] is not an object")
                    continue
                video_id = part.get("video_id")
                video_ids.append(video_id)
                counts["parts"] += 1
                if (
                    not isinstance(video_id, str)
                    or not spec.patterns["video_id"].fullmatch(video_id)
                ):
                    failures.append(
                        f"{relative}: parts[{position}].video_id is {video_id!r}, which is "
                        "not an 11-character YouTube id"
                    )
                else:
                    valid_video_ids.add(video_id)
        if not isinstance(record.get("parts"), list) or record["parts"] != video_ids:
            failures.append(f"{relative}: INDEX `parts` disagrees with metadata video IDs")

        flag_key = spec.transcript_flag["key"]
        artifact = spec.transcript_flag["artifact"]
        try:
            transcript = _contained_path(root, f"{relative}/{artifact}", f"{relative}: {artifact}")
            try:
                mode = transcript.stat().st_mode
            except FileNotFoundError:
                has_transcript = False
            else:
                if not stat.S_ISREG(mode):
                    raise IdentityError(f"{artifact} must be a regular file")
                has_transcript = True
            if type(record.get(flag_key)) is not bool or record[flag_key] != has_transcript:
                failures.append(
                    f"{relative}: INDEX `{flag_key}` must be {has_transcript} "
                    f"to match {artifact}"
                )
        except (IdentityError, OSError) as exc:
            failures.append(f"{relative}: {artifact}: {exc}")

        sessions = metadata.get("sessions", [])
        if not isinstance(sessions, list):
            failures.append(f"{relative}: `sessions` must be a list")
        else:
            for position, session in enumerate(sessions):
                where = f"{relative}: sessions[{position}].session_name"
                name = session.get("session_name") if isinstance(session, dict) else None
                match = spec.patterns["session_id"].fullmatch(name) if isinstance(name, str) else None
                if match is None:
                    failures.append(f"{where} is {name!r}, which does not match session_id")
                elif match.group("video_id") not in valid_video_ids:
                    failures.append(f"{where} {name!r} does not belong to a record part")
                # sessions[].video_id can name a separate per-talk upload, not this part.

        duplicate_key = spec.duplicate_key
        if (
            (duplicate_key in record) != (duplicate_key in metadata)
            or record.get(duplicate_key) != metadata.get(duplicate_key)
        ):
            failures.append(f"{relative}: INDEX `{duplicate_key}` disagrees with metadata.json")
        if duplicate_key in metadata:
            counts["duplicates"] += 1
            duplicate = metadata[duplicate_key]
            try:
                suffix = _relative_path(duplicate, f"{relative}: {duplicate_key}")
                prefix = Path(*path.parts[: spec.derived_prefix_components])
                target = (prefix / suffix).as_posix()
                _contained_path(root, target, f"{relative}: {duplicate_key}")
                if target not in known_paths:
                    failures.append(
                        f"{relative}: {duplicate_key} {duplicate!r} resolves to "
                        f"{target}, which is not a record path"
                    )
            except IdentityError as exc:
                failures.append(str(exc))
    return failures, counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", default="docs/workflows/record-identity.schema.json")
    parser.add_argument("--contract", default="docs/workflows/publishing.md")
    parser.add_argument("--corpus", help="corpus root holding INDEX.json (default: none)")
    parser.add_argument("--verify-copy", metavar="PATH", help="check a member's schema copy")
    parser.add_argument("--digest", action="store_true", help="print the schema sha256")
    args = parser.parse_args(argv)

    schema_path = Path(args.schema)
    try:
        spec = load_schema(schema_path)
    except IdentityError as exc:
        print(f"identity: {exc}", file=sys.stderr)
        return 1

    if args.digest:
        print(f"{schema_path.name}  {spec.digest()}")
        return 0

    if args.verify_copy:
        problem = verify_copy(Path(args.verify_copy), Path(args.contract))
        if problem:
            print(f"identity: {problem}", file=sys.stderr)
            return 1
        print(f"identity: {args.verify_copy} matches {Path(args.contract).name}")
        return 0

    failures = check_contract(Path(args.contract), spec)
    counts: dict[str, int] = {}
    if args.corpus:
        corpus_failures, counts = check_corpus(Path(args.corpus), spec)
        failures += corpus_failures
    for message in failures:
        print(f"identity: FAIL {message}", file=sys.stderr)
    if failures:
        return 1
    suffix = "".join(f", {value} {name}" for name, value in counts.items())
    print(f"identity: ok ({schema_path.name}{suffix})")
    return 0


if __name__ == "__main__":
    sys.exit(main())