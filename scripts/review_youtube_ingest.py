#!/usr/bin/env python3
"""Prepare a public channel worklist for the Journal-Utilities scaffold preview."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path


CHANNEL_ID = "UCbPq2w41ZaJSWtpCq4BE6Dg"
VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{11}")
PUBLIC_STATE = {
    "privacy_status": "public",
    "upload_status": "processed",
    "broadcast_status": "none",
    "publication_state": "published",
}


def index_video_ids(index: object) -> set[str]:
    items = index.get("items") if isinstance(index, dict) else None
    if not isinstance(items, list) or not items:
        raise ValueError("INDEX.json must contain a nonempty items list")
    video_ids: set[str] = set()
    for position, item in enumerate(items, 1):
        parts = item.get("parts") if isinstance(item, dict) else None
        if not isinstance(parts, list) or any(
            not isinstance(video_id, str) or VIDEO_ID.fullmatch(video_id) is None
            for video_id in parts
        ):
            raise ValueError(f"INDEX.json item {position} has invalid video IDs")
        video_ids.update(parts)
    if not video_ids:
        raise ValueError("INDEX.json contains no video IDs")
    return video_ids


def timestamp(value: object, field: str) -> str:
    if isinstance(value, str):
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            pass
        else:
            if parsed.utcoffset() is not None:
                return value
    raise ValueError(f"{field} must be an ISO 8601 timestamp with an offset")


def public_entry(entry: object, position: int) -> dict:
    label = f"worklist row {position}"
    if not isinstance(entry, dict):
        raise ValueError(f"{label} must be an object")
    if entry.get("is_scheduled") is not False or any(
        entry.get(field) != value for field, value in PUBLIC_STATE.items()
    ):
        raise ValueError(f"{label} must be a completed public video")
    video_id = entry.get("video_id")
    if not isinstance(video_id, str) or VIDEO_ID.fullmatch(video_id) is None:
        raise ValueError(f"{label} has an invalid video ID")
    title = entry.get("title")
    if not isinstance(title, str) or not title.strip():
        raise ValueError(f"{label} has no title")
    duration = entry.get("duration_seconds")
    if duration is not None and (type(duration) is not int or duration < 0):
        raise ValueError(f"{label} has an invalid duration")
    published_at = entry.get("published_at", "")
    if published_at != "":
        published_at = timestamp(published_at, f"{label} published_at")
    return {
        "video_id": video_id,
        "title": title,
        "published_at": published_at,
        "duration_seconds": duration,
        **PUBLIC_STATE,
        "description": "",
        "published_date": published_at[:10],
        "is_scheduled": False,
        "url": f"https://www.youtube.com/watch?v={video_id}",
    }


def review_worklist(worklist: object, indexed: set[str]) -> dict:
    if not isinstance(worklist, dict) or worklist.get("channel_id") != CHANNEL_ID:
        raise ValueError("worklist must identify the Institute YouTube channel")
    generated_at = timestamp(worklist.get("generated_at"), "worklist generated_at")
    rows = worklist.get("new_videos")
    if not isinstance(rows, list):
        raise ValueError("worklist new_videos must be a list")
    count = worklist.get("new_video_count")
    channel_count = worklist.get("channel_video_count")
    if type(count) is not int or count != len(rows):
        raise ValueError("worklist new_video_count differs from the row count")
    if type(channel_count) is not int or channel_count < count:
        raise ValueError("worklist channel_video_count must cover its rows")

    seen: set[str] = set()
    new_videos: list[dict] = []
    for position, row in enumerate(rows, 1):
        video = public_entry(row, position)
        video_id = video["video_id"]
        if video_id in seen:
            raise ValueError(f"worklist row {position} duplicates a video ID")
        seen.add(video_id)
        if video_id not in indexed:
            new_videos.append(video)
    return {
        "channel_id": CHANNEL_ID,
        "generated_at": generated_at,
        "index_video_count": len(indexed),
        "channel_video_count": channel_count,
        "new_video_count": len(new_videos),
        "new_videos": new_videos,
    }


def write_atomically(output: Path, report: dict) -> None:
    if output.is_symlink():
        raise ValueError("output must be a regular file path")
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=output.parent, delete=False
        ) as stream:
            temporary = Path(stream.name)
            json.dump(report, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
        os.replace(temporary, output)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--journal", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--worklist", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)

    index_path = args.journal / "INDEX.json"
    try:
        if args.output.resolve() in {args.worklist.resolve(), index_path.resolve()}:
            raise ValueError("output must be separate from the worklist and INDEX.json")
        indexed = index_video_ids(json.loads(index_path.read_text(encoding="utf-8")))
        report = review_worklist(json.loads(args.worklist.read_text(encoding="utf-8")), indexed)
        write_atomically(args.output, report)
    except (OSError, ValueError) as exc:
        print(f"Cannot review YouTube ingest: {exc}", file=sys.stderr)
        return 1
    print(f"Reviewed {report['new_video_count']} new public videos against {len(indexed)} indexed IDs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
