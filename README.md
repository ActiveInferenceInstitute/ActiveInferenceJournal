# ActiveInferenceJournal

Content of the Active Inference Journal — transcripts, metadata, captions, translations,
and curated materials from the [Active Inference Institute](https://www.youtube.com/@ActiveInference)
video library.

<a href="https://zenodo.org/badge/latestdoi/562916661"><img src="https://zenodo.org/badge/562916661.svg" alt="DOI"></a>
[![Journal integrity](https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal/actions/workflows/journal-integrity.yml/badge.svg)](https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal/actions/workflows/journal-integrity.yml)

Learn more: https://activeinference.institute/learning/ ·
Tooling: https://github.com/ActiveInferenceInstitute/Journal-Utilities

## Layout

Content is **source-namespaced** so other channels and non-video sources can live
alongside, e.g. `data/video/<other-channel>/…` or `data/<other-type>/<source>/…`:

```
data/video/activeinferenceinstitute/<Series>/<item>/
  metadata.json     # canonical: series, item, parts[{video_id, url, title, duration, upload_date, speakers}]
  transcript.txt    # derived speaker-labeled text (part-tagged when multi-part)
  transcript.json   # raw diarized segments — immutable, SPEAKER_NN labels (where available)
  captions/         # original-language .srt (+ youtube_captions.txt where captions predate diarization)
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

## Documentation

- Technical docs (schema, organization, pipeline): [`docs/`](docs/README.md).
- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md).
- Citation (Zenodo DOI): [`CITATION.cff`](CITATION.cff).
- Agent conventions: [`AGENTS.md`](AGENTS.md).

## Provenance

Transcripts and metadata are pulled completely and idempotently from the Institute
YouTube channel by
[Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities).
Most transcripts are WhisperX-diarized: `transcript.json` holds the immutable raw
segments (`SPEAKER_NN`), human speaker identifications are recorded in
`metadata.json` `parts[].speakers`, and `transcript.txt` is regenerated from the
two (`Journal-Utilities/scripts/apply_speaker_names.py`). Items without diarization yet carry
YouTube-caption text; original captions always remain under `captions/`.
Private/unlisted videos are not transcribed. See [`docs/SCHEMA.md`](docs/SCHEMA.md)
("Transcripts — raw vs derived").
