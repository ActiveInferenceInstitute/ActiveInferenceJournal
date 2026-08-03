# Agent guide — ActiveInferenceJournal

A source-namespaced **data repository**: transcripts, metadata, captions, translations, and
curated materials from the Active Inference Institute video library. Read
[`README.md`](README.md) and [`docs/`](docs/README.md) first.

## Entry points

- **Machine:** [`INDEX.json`](INDEX.json) — every item, its videos, and paths. Start here.
- **Human:** [`INDEX.md`](INDEX.md), [`README.md`](README.md).
- **Content:** [`data/video/activeinferenceinstitute/`](data/video/activeinferenceinstitute/).
- **Schema/docs:** [`docs/`](docs/README.md) (`SCHEMA.md`, `ORGANIZATION.md`, `PIPELINE.md`).
- **Open work:** [`TO-DO.md`](TO-DO.md) — scoped improvement list (docs pass 2026-08-02).

## Rules for agents

- This repo is **generated** by
  [Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities)
  (`scripts/refactor_journal.py`, `scripts/download_channel.py`). Prefer changing the
  generator over hand-editing derived files (`metadata.json`, `transcript.txt`,
  `INDEX.*`); hand edits are overwritten on the next run.
- **Per-item schema is fixed** — see [`docs/SCHEMA.md`](docs/SCHEMA.md). Keep `metadata.json`
  the single source of truth per item.
- **Audio is off `main`** — it lives on the `audio` branch only. Never commit `*.m4a`/audio
  to `main`.
- **Never commit credentials** (cookies, tokens). See the security note in `docs/PIPELINE.md`.
- Completeness invariant: every non-duplicate channel video is a part in exactly one
  canonical item; records with `duplicate_of` are deliberate secondary copies and are
  excluded from coverage reconciliation. Reconcile to `missing == 0` against the
  channel manifest.
- Generator entry points: `Journal-Utilities/scripts/enrich_metadata.py` updates the
  canonical metadata, and `Journal-Utilities/scripts/generate_journal_indexes.py`
  regenerates `INDEX.json` and `INDEX.md`; `Journal-Utilities/scripts/repair_split_transcripts.py`
  repairs merged session transcript identities when split sources are available;
  `Journal-Utilities/scripts/validate_journal.py` is the final read-only integrity gate.

## Layout

`data/<type>/<source>/<Series>/<item>/` + `docs/` + top-level `INDEX.*`. See
[`docs/ORGANIZATION.md`](docs/ORGANIZATION.md).
