# ActiveInferenceJournal

Content of the Active Inference Journal — transcripts, metadata, captions, translations,
and curated materials from the [Active Inference Institute](https://www.youtube.com/@ActiveInference)
video library.

<a href="https://zenodo.org/badge/latestdoi/562916661"><img src="https://zenodo.org/badge/562916661.svg" alt="DOI"></a>

Learn more: https://www.activeinference.org/research/journal ·
Tooling: https://github.com/ActiveInferenceInstitute/Journal-Utilities

## Layout (v2 schema)

The journal is organized by **series** → **item**, with a uniform, agent- and
program-navigable structure per item:

```
<Series>/<Series>_<NNN[.E]>/
  metadata.json     # canonical record: series, item, parts[{video_id, url, title}]
  transcript.txt    # clean text (part-tagged when multi-part)
  transcript.json   # timestamped segments
  captions/         # original-language .srt
  translations/     # translated .srt (per language)
  assets/           # images, html, prose, appendices, bibliography, …
  README.md         # human nav: titles, links, contents
```

- **`INDEX.json`** (repo root) — machine entry point: every item, its videos, and paths.
- **`INDEX.md`** — human index, grouped by series.
- **`SCHEMA.md`** — the full schema spec.

468 items · 615 videos · 18 series.

## Branches

- **`main`** — everything above, **without audio** (lightweight to clone).
- **`audio`** — `main` + `<item>/audio/<name>.64k.m4a` (audio re-encoded to 64 kbps).
  `git checkout audio` to get the media.

## Provenance

Transcripts are pulled from the Institute YouTube channel (captions, or local Whisper
where captions are absent) by [Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities);
`scripts/refactor_journal.py` produced this v2 layout with verified zero data loss.
