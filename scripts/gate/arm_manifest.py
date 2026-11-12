"""Manifest staleness and channel/INDEX reconciliation (handoff E13).

This is the step that used to live inline in journal-integrity.yml. It reports;
it does not fail, because the scheduled manifest refresh does not exist yet and
a stale manifest would block every pull request.
"""

from __future__ import annotations

import argparse
import collections
import datetime
import json
import sys
from pathlib import Path

from common import ROOT, log

FRESHNESS_DAYS = 7


def reconcile(manifest_path: Path, index_path: Path) -> list[str]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    enumerated = datetime.datetime.fromisoformat(manifest["enumerated_at"])
    age = (datetime.datetime.now(datetime.timezone.utc) - enumerated).days
    listed = [video["id"] for video in manifest["videos"]]
    ids = set(listed)
    duplicated = sorted(v for v, count in collections.Counter(listed).items() if count > 1)

    index = json.loads(index_path.read_text(encoding="utf-8"))
    indexed: set[str] = set()
    for item in index.get("items", []):
        for part in item.get("parts", []):
            indexed.add(part if isinstance(part, str) else part.get("video_id"))

    missing = sorted(ids - indexed)
    extra = sorted(indexed - ids)
    print(
        f"manifest: enumerated_at={manifest['enumerated_at']} age_days={age} "
        f"declared={manifest.get('total_videos')} listed={len(listed)} "
        f"unique={len(ids)} duplicate_ids={len(duplicated)}"
    )
    print(
        f"INDEX: count={index.get('count')} unique_videos={index.get('unique_videos')} "
        f"part_ids={len(indexed)}"
    )
    print(
        f"reconciliation: manifest-not-in-INDEX={len(missing)} "
        f"INDEX-not-in-manifest={len(extra)}"
    )
    for video in missing[:20]:
        print(f"  manifest-only: {video}")
    for video in extra[:20]:
        print(f"  index-only: {video}")

    warnings: list[str] = []
    if age > FRESHNESS_DAYS:
        warnings.append(
            f"channel_videos.json is {age} days old (enumerated_at "
            f"{manifest['enumerated_at']}) - exceeds the {FRESHNESS_DAYS}-day "
            "freshness budget (E13); refresh via the scheduled enumeration"
        )
    if duplicated:
        warnings.append(f"manifest contains {len(duplicated)} duplicate video ids: {duplicated[:5]}")
    return warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--index", type=Path, default=ROOT / "INDEX.json")
    parser.add_argument("--strict", action="store_true", help="fail on a stale manifest")
    args = parser.parse_args(argv)

    warnings = reconcile(args.manifest, args.index)
    for message in warnings:
        print(f"::warning::{message}")
    if args.strict and warnings:
        return 1
    log(f"manifest: reconciliation complete ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
