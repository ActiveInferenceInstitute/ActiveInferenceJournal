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
import sys
from dataclasses import dataclass
from pathlib import Path

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

    flag = _require(block, "transcript_flag", f"{path}: x-identity")
    if not isinstance(flag, dict):
        raise IdentityError(f"{path}: x-identity.transcript_flag must be an object")

    components = _require(block, "derived_prefix_components", f"{path}: x-identity")
    if not isinstance(components, int) or components < 1:
        raise IdentityError(f"{path}: derived_prefix_components must be a positive integer")

    return Spec(
        path=path,
        document=document,
        patterns=patterns,
        leaf_key=str(_require(block, "leaf_key", f"{path}: x-identity")),
        ancestor_key=str(_require(block, "ancestor_key", f"{path}: x-identity")),
        duplicate_key=str(_require(block, "duplicate_key", f"{path}: x-identity")),
        index_file=str(_require(block, "index_file", f"{path}: x-identity")),
        derived_prefix_components=components,
        transcript_flag=flag,
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
        candidate = root / location / name if location else root / name
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
        path = schema.path if name == schema.path.name else resolve_artifact(root, name)
        if path is None:
            failures.append(
                f"{contract.name}: records {name}, which is not one file under "
                f"{root} at {', '.join(location or '.' for location in ARTIFACT_LOCATIONS)}"
            )
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
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
        digest = hashlib.sha256(copy.read_bytes()).hexdigest()
    except FileNotFoundError:
        return f"{copy}: no such file"
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
    """Enforce the identity grammar over one corpus; return failures and counts."""
    failures: list[str] = []
    counts = {"records": 0, "parts": 0, "duplicates": 0}
    index_path = root / spec.index_file
    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"missing {spec.index_file} under {root}"], counts
    except json.JSONDecodeError as exc:
        return [f"{spec.index_file} is not valid JSON: {exc}"], counts

    records = index.get("items") if isinstance(index, dict) else None
    if not isinstance(records, list):
        return [f"{spec.index_file}: `items` must be a list"], counts

    known_paths = {
        str(item.get("path", "")) for item in records if isinstance(item, dict)
    }
    seen: set[str] = set()
    for position, record in enumerate(records):
        if not isinstance(record, dict):
            failures.append(f"{spec.index_file}: items[{position}] is not an object")
            continue
        relative = str(record.get("path", ""))
        if not relative:
            failures.append(f"{spec.index_file}: items[{position}] has no path")
            continue
        if relative in seen:
            failures.append(f"{spec.index_file}: duplicate record path {relative}")
            continue
        seen.add(relative)
        record_dir = root / relative
        metadata_path = record_dir / "metadata.json"
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            failures.append(f"{relative}: no metadata.json")
            continue
        except json.JSONDecodeError as exc:
            failures.append(f"{relative}: metadata.json is not valid JSON: {exc}")
            continue
        if not isinstance(metadata, dict):
            failures.append(f"{relative}: metadata.json must hold an object")
            continue

        counts["records"] += 1
        leaf = metadata.get(spec.leaf_key)
        if leaf != record_dir.name:
            failures.append(
                f"{relative}: {spec.leaf_key} is {leaf!r}, but the directory is "
                f"{record_dir.name!r}; the item id must name its own directory"
            )
        ancestors = {parent.name for parent in record_dir.parents if parent.name}
        series = metadata.get(spec.ancestor_key)
        if series not in ancestors:
            failures.append(
                f"{relative}: {spec.ancestor_key} is {series!r}, which names no "
                "directory above the item"
            )

        parts = metadata.get("parts")
        if not isinstance(parts, list):
            failures.append(f"{relative}: `parts` must be a list")
            continue
        for position, part in enumerate(parts):
            if not isinstance(part, dict):
                failures.append(f"{relative}: parts[{position}] is not an object")
                continue
            video_id = part.get("video_id")
            counts["parts"] += 1
            if not isinstance(video_id, str) or not spec.patterns["video_id"].match(video_id):
                failures.append(
                    f"{relative}: parts[{position}].video_id is {video_id!r}, which is "
                    "not an 11-character YouTube id"
                )

        duplicate = metadata.get(spec.duplicate_key)
        if duplicate is not None:
            counts["duplicates"] += 1
            if not isinstance(duplicate, str):
                failures.append(f"{relative}: {spec.duplicate_key} must be a string")
            else:
                prefix = "/".join(relative.split("/")[: spec.derived_prefix_components])
                target = f"{prefix}/{duplicate}"
                if target not in known_paths:
                    failures.append(
                        f"{relative}: {spec.duplicate_key} {duplicate!r} resolves to "
                        f"{target}, which is not a record path"
                    )
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
