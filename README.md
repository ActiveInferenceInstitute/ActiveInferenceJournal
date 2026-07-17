# ActiveInferenceJournal

Content of the Active Inference Journal — transcripts, metadata, captions, translations,
and curated materials from the [Active Inference Institute](https://www.youtube.com/@ActiveInference)
video library.

<a href="https://zenodo.org/badge/latestdoi/562916661"><img src="https://zenodo.org/badge/562916661.svg" alt="DOI"></a>

Learn more: https://www.activeinference.org/research/journal ·
Tooling: https://github.com/ActiveInferenceInstitute/Journal-Utilities

## Layout

Content is **source-namespaced** so other channels and non-video sources can live
alongside, e.g. `data/video/<other-channel>/…` or `data/<other-type>/<source>/…`:

```
data/video/activeinferenceinstitute/<Series>/<item>/
  metadata.json     # canonical: series, item, parts[{video_id, url, title, duration, upload_date}]
  transcript.txt    # clean text (part-tagged when multi-part)
  transcript.json   # timestamped segments (where available)
  captions/         # original-language .srt
  translations/     # translated .srt (per language)
  assets/           # images, html, prose, appendices, bibliography, …
  README.md         # human nav: titles, links, contents
docs/               # technical documentation (SCHEMA.md, …)
INDEX.json          # machine entry point: every item, its videos, paths
INDEX.md            # human index, grouped by series
```

Current item and video totals are generated in [`INDEX.json`](INDEX.json).
Deliberate duplicate records are marked with `duplicate_of`; the index reports
both indexed video records and unique video IDs. Every Institute channel video
is represented (uncategorized videos live under `Other/`).

## Branches

- **`main`** — everything above, **without audio** (lightweight to clone).
- **`audio`** — `main` + `<item>/audio/<name>.64k.m4a` (audio re-encoded to 64 kbps).
  `git checkout audio` to get the media.

## Provenance

Transcripts and metadata are pulled completely and idempotently from the Institute
YouTube channel (captions, or local Whisper where captions are absent) by
[Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities)
(`scripts/refactor_journal.py`, `scripts/download_channel.py`). See [`docs/SCHEMA.md`](docs/SCHEMA.md).
