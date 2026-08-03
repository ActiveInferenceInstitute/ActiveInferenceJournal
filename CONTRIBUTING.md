# Contributing to ActiveInferenceJournal

ActiveInferenceJournal is a public, source-namespaced **data repository**: transcripts,
metadata, captions, translations, and curated materials from the
[Active Inference Institute](https://www.youtube.com/@ActiveInference) video library.
All content is licensed [CC BY 4.0](LICENSE). Read
[`README.md`](README.md), [`AGENTS.md`](AGENTS.md), and [`docs/README.md`](docs/README.md)
before contributing.

## What lives here vs. in Journal-Utilities

This repo holds the *content*. The *code* that generates and validates it lives in the
separate [Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities)
repository.

- **Hand-editable here:** `docs/` (schema, organization, pipeline), root and structural
  `README.md`/`AGENTS.md`, curated `assets/` content, `metadata.json` `sessions[]`
  (journal-owned; the enrichment script seeds but never overwrites it),
  `metadata.json` `parts[].speakers` (human speaker identifications), and
  `private_videos.json`.
- **Generated — change the generator instead:** per-item `metadata.json` core keys,
  `transcript.txt`/`transcript.json`, `captions/`, `translations/`, `INDEX.json`,
  `INDEX.md`, and the series/item `README.md` files. Hand edits to generated files are
  overwritten on the next generator run (see `AGENTS.md`).

## Rules

- **No audio on `main`.** Audio lives on the `audio` branch only (`<item>/audio/*.64k.m4a`).
  Never commit `*.m4a`/audio to `main`.
- **No credentials.** Never commit cookies, tokens, or keys. See the security note in
  [`docs/PIPELINE.md`](docs/PIPELINE.md).
- **Coverage invariant:** every non-duplicate channel video is a part in exactly one
  canonical item; `duplicate_of` records are deliberate secondary copies and are
  excluded from coverage reconciliation. Target: `missing == 0` against the channel
  manifest.
- **`metadata.json` is the single source of truth** per item — see
  [`docs/SCHEMA.md`](docs/SCHEMA.md).

## Validation

The CI workflow (`.github/workflows/journal-integrity.yml`) runs on every push and pull
request and is the release gate:

1. `generate_journal_indexes.py --journal . --check` — derived indexes must not be stale.
2. `repair_split_transcripts.py --journal . --utilities .journal-utilities --check` —
   merged session transcript artifacts must not be stale.
3. `validate_journal.py --journal . --manifest …/channel_videos.json` — read-only
   integrity gate (metadata/path consistency, transcript shape, manifest coverage,
   no audio or credentials on `main`).

To validate locally, run from a Journal-Utilities checkout:

```bash
uv run python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal --check
uv run python scripts/repair_split_transcripts.py \
  --journal ../ActiveInferenceJournal --utilities .
uv run python run.py journal-check
```

## Citation

If you use this repository in published work, cite it via the Zenodo DOI in
[`CITATION.cff`](CITATION.cff) (also shown as the badge in `README.md`).
