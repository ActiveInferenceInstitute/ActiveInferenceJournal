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

The coverage target is that every non-duplicate video in the supplied channel
manifest belongs to exactly one canonical item. Validation uses the pinned
Journal-Utilities manifest; it does not enumerate the live channel or establish
current hosted CI status. Billing-lock failures were recorded on 2026-11-12
(see [`TO-DO.md`](TO-DO.md)); those dated receipts do not establish today's hosted
availability or results. The repository is **generated**: the per-item `metadata.json` core
keys, `transcript.*`, `captions/`, `translations/`, `INDEX.json`/`INDEX.md` and the
item/series `README.md` files are produced by
[Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal_Utilities) and
hand edits to them are overwritten on the next run. There is **no build step**: the
gate is [`./run.sh`](run.sh) (the arms CI runs), and the static-site build and the
channel ingest run from a Journal-Utilities checkout (see
[Operations](docs/OPERATIONS.md)).

- **Works offline:** cloning, browsing, grepping and editing the hand-editable files
  (see [`CONTRIBUTING.md`](CONTRIBUTING.md)).
- **Uses pinned Journal-Utilities:** index/transcript validation executes a fresh
  exact-commit snapshot. A sibling working tree is not required as executable
  source; the static-site workflow uses its separately pinned producer checkout.
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
both indexed video records and unique video IDs. Coverage is assessed against the
supplied manifest, not guaranteed against the live channel. Indexed videos without
a more specific series live under `Other/`.

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

Browsing requires nothing to install or build. Validation runs from this checkout;
cold Journal-Utilities acquisition and GNN provisioning can require network and
an appropriate runtime. Run Journal-Utilities directly when changing the generator
(enrichment is dry-run unless `--apply` is passed):

```bash
./run.sh all                     # lint, docs, identity, full, gnn; stop at first failure
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

Transcripts and metadata are produced from Institute YouTube content by
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
