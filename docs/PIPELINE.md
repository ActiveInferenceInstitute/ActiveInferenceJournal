# Pipeline & provenance

This repository is **generated and maintained** by the
[Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities) engine.
The journal holds the *content*; Journal-Utilities holds the *code* that produces it.

## End to end

```
YouTube (@ActiveInference)
  └─ scripts/download_channel.py   enumerate (videos+streams+shorts) → 729 videos
        ├─ transcripts (yt-dlp captions, cookie-free)
        └─ local Whisper (mlx-whisper) for caption-less videos
  └─ scripts/refactor_journal.py   → this repo's per-item v2 schema, namespaced layout,
                                      INDEX.json/INDEX.md, audio split to the `audio` branch
```

## Completeness & idempotency contract

- **All channel videos:** every video on the Institute channel is a part in exactly one
  item. Coverage is reconciled against the channel manifest
  (`Journal-Utilities/data/output/channel_videos.json`); the target is `missing == 0`.
- **Idempotent:** re-running the generators only adds genuinely-missing videos/parts and
  rebuilds derived files (`metadata.json`, `transcript.txt`, indexes). Multi-part items
  merge all parts (never last-write-wins).
- **Zero data loss on refactor:** `refactor_journal.py --build` stages out-of-place and
  reconciles `total source files == captured + intentional drops` before any in-place apply.

## Metadata

`metadata.json` per item carries `series`, `item`, `source`, `channel`, and `parts[]`
with `video_id`, `url`, `title`, `duration`, `upload_date`. Titles/durations come from the
channel manifest; `upload_date` is enriched where available.

## Audio

Audio is kept off `main`. The `audio` branch mirrors `main` and adds
`<item>/audio/<name>.64k.m4a` (re-encoded to 64 kbps via ffmpeg).

## Security note

Never commit credentials. A `cookies.txt` once leaked Google session cookies into the
Journal-Utilities public repo; that history was purged and the downloader now runs
cookie-free. See Journal-Utilities `CLAUDE.md`.
