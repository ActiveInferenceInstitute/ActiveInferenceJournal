# Pipeline & provenance

This repository is **generated and maintained** by the
[Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities) engine.
The journal holds the *content*; Journal-Utilities holds the *code* that produces it.

## End to end

```
YouTube (@ActiveInference)
  └─ scripts/download_channel.py   enumerate (videos+streams+shorts) → channel manifest
        ├─ transcripts (yt-dlp captions, cookie-free)
        └─ local Whisper (mlx-whisper) for caption-less videos
  └─ scripts/refactor_journal.py   → this repo's per-item v2 schema, namespaced layout,
                                      audio split to the `audio` branch
  └─ scripts/enrich_metadata.py    → Coda/session/manifest enrichment of metadata.json
  └─ scripts/generate_journal_indexes.py
                                   → INDEX.json/INDEX.md derived from metadata.json
  └─ scripts/repair_split_transcripts.py
                                   → session IDs/headings in merged transcript artifacts
  └─ scripts/translate_subtitles.py / translate_subtitles_openrouter.py
                                   → 11-language subtitle translation under translations/
  └─ scripts/validate_journal.py   → read-only release/integrity gate
```

## Completeness & idempotency contract

- **All channel videos:** every non-duplicate video on the Institute channel is a part
  in exactly one canonical item. Records marked with `duplicate_of` are deliberate
  secondary copies and are excluded from missing/duplicate coverage counts. Coverage
  is reconciled against the channel manifest (`Journal-Utilities/data/output/channel_videos.json`);
  the target is `missing == 0`.
- **Idempotent:** re-running the generators only adds genuinely-missing videos/parts and
  rebuilds derived files (`metadata.json`, `transcript.txt`, indexes). Multi-part items
  merge all parts (never last-write-wins); `generate_journal_indexes.py --check` fails
  if either derived index is stale. `repair_split_transcripts.py --check` likewise
  detects stale merged session transcript artifacts.
- **Zero data loss on refactor:** `refactor_journal.py --build` stages out-of-place and
  reconciles `total source files == captured + intentional drops` before any in-place apply.

## Maintenance sequence

Run these commands from the Journal-Utilities checkout. Enrichment is dry-run by
default; only the explicit `--apply` command writes canonical metadata.

```bash
cd ../Journal-Utilities
uv run python scripts/enrich_metadata.py --journal ../ActiveInferenceJournal
uv run python scripts/enrich_metadata.py --journal ../ActiveInferenceJournal --apply
uv run python scripts/repair_split_transcripts.py \
  --journal ../ActiveInferenceJournal --utilities .
uv run python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal
uv run python run.py journal-check
```

`journal-check` is read-only. It verifies metadata/path consistency, derived
indexes, duplicate targets and canonical ID uniqueness, transcript JSON shape,
manifest coverage, URL-only enrichment fields, and the rule that `main` contains
neither audio nor credentials. Use `--strict-manifest` after fresh enumeration
when canonical IDs absent from the manifest must fail rather than warn.

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
