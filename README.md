# ActiveInferenceJournal

Content of the Active Inference Journal — transcripts, metadata, captions, translations,
and curated materials from the [Active Inference Institute](https://www.youtube.com/@ActiveInference)
video library.

<a href="https://zenodo.org/badge/latestdoi/562916661"><img src="https://zenodo.org/badge/562916661.svg" alt="DOI"></a>
[![Journal integrity](https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal/actions/workflows/journal-integrity.yml/badge.svg)](https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal/actions/workflows/journal-integrity.yml)

Learn more: https://activeinference.institute/learning/ ·
Site: https://activeinferenceinstitute.github.io/ActiveInferenceJournal/ ·
Tooling: https://github.com/ActiveInferenceInstitute/Journal_Utilities

## Contents

- [Status](#status)
- [Layout](#layout)
- [Branches](#branches)
- [Using this repository](#using-this-repository)
- [Documentation](#documentation)
- [Provenance](#provenance)
- [InstituteOS sidecar](#instituteos-sidecar)

## Status

The content on `main` is **complete and current** against the Institute channel: every
non-duplicate channel video is a part in exactly one item, and the read-only integrity
gate passes in CI. The repository is **generated**: the per-item `metadata.json` core
keys, `transcript.*`, `captions/`, `translations/`, `INDEX.json`/`INDEX.md` and the
item/series `README.md` files are produced by
[Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal_Utilities) and
hand edits to them are overwritten on the next run. There is **no build step**: the
gate is [`./run.sh`](run.sh) (the arms CI runs), and the static-site build and the
channel ingest run from a Journal-Utilities checkout (see
[Operations](docs/OPERATIONS.md)).

- **Works offline:** cloning, browsing, grepping and editing the hand-editable files
  (see [`CONTRIBUTING.md`](CONTRIBUTING.md)).
- **Needs the sibling Journal-Utilities checkout:** index/transcript validation and the
  static-site build.
- **Needs network:** the weekly ingest workflow (YouTube enumeration via `yt-dlp`).
- **Not on `main`:** audio — check out the `audio` branch for the 64 kbps media.

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

## Using this repository

Clone it (add `--depth 1` for a lightweight copy):

```bash
git clone https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal.git
git clone --branch audio https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal.git  # with media
```

Browse or consume the content offline: start from [`INDEX.json`](INDEX.json) (machine)
or [`INDEX.md`](INDEX.md) (human), then read each item's `metadata.json` and
`transcript.txt`. The static reader site is published at
https://activeinferenceinstitute.github.io/ActiveInferenceJournal/.

There is nothing to install or build here. To **regenerate or validate** the repository,
run the gate from this checkout (`./run.sh` brings up the pinned Journal-Utilities
revision by itself), or run the Journal-Utilities scripts directly from that checkout
when you are changing the generator (enrichment is dry-run unless `--apply` is passed):

```bash
./run.sh all                     # lint, docs, full, gnn — the same commands CI runs
```

```bash
cd ../Journal-Utilities
uv run python scripts/enrich_metadata.py --journal ../ActiveInferenceJournal --apply
uv run python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal
uv run python run.py journal-check   # read-only integrity gate
```

See [Operations](docs/OPERATIONS.md) for every arm, workflow and pin.

## Documentation

- Technical docs index (schema, organization, pipeline, operations): [`docs/`](docs/README.md).
- Flat index of every long-lived doc: [`docs/documentation-index.md`](docs/documentation-index.md).
- Gate arms and measured timings: [`docs/OPERATIONS.md`](docs/OPERATIONS.md) and [`docs/_generated/gate-timings.md`](docs/_generated/gate-timings.md).
- Contribution guide (what to edit vs. generated): [`CONTRIBUTING.md`](CONTRIBUTING.md).
- Security rules (credentials, audio): [`SECURITY.md`](SECURITY.md).
- Scoped improvement list and open items: [`TO-DO.md`](TO-DO.md).
- Citation (Zenodo DOI): [`CITATION.cff`](CITATION.cff).
- Agent conventions: [`AGENTS.md`](AGENTS.md).

## Provenance

Transcripts and metadata are pulled completely and idempotently from the Institute
YouTube channel by
[Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal_Utilities).
Most transcripts are WhisperX-diarized: `transcript.json` holds the immutable raw
segments (`SPEAKER_NN`), human speaker identifications are recorded in
`metadata.json` `parts[].speakers`, and `transcript.txt` is regenerated from the
two (`Journal-Utilities/scripts/apply_speaker_names.py`). Items without diarization yet carry
YouTube-caption text; original captions always remain under `captions/`.
Private/unlisted videos are not transcribed. See [`docs/SCHEMA.md`](docs/SCHEMA.md)
("Transcripts — raw vs derived").

## InstituteOS sidecar

This repository carries a committed [`.aii/`](.aii/README.md) sidecar with curated
InstituteOS metadata (`aii-sidecar/v1`): category, maturity, ecosystem relations,
key artifacts, provenance, and portable tasks. It is read by
[InstituteOS](https://github.com/ActiveInferenceInstitute/InstituteOS) tooling and
does not affect the project's build or runtime.
