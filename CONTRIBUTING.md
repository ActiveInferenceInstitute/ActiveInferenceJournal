# Contributing to ActiveInferenceJournal

ActiveInferenceJournal is a public, source-namespaced **data repository**: transcripts,
metadata, captions, translations, and curated materials from the
[Active Inference Institute](https://www.youtube.com/@ActiveInference) video library.
All content is licensed [CC BY 4.0](LICENSE). Read
[`README.md`](README.md), [`AGENTS.md`](AGENTS.md), and [`docs/README.md`](docs/README.md)
before contributing.

## What lives here vs. in Journal-Utilities

This repo holds the *content*. The *code* that generates and validates it lives in the
separate [Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal_Utilities)
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

Run the gate from the repository root. Each arm is what CI runs; the workflows
call `./run.sh`, they do not carry a second copy of any command.

```bash
./run.sh lint    # workflow action pins, pin-file schemas, shipped JSON
./run.sh docs    # relative links, anchors, docs index coverage, documented pins
./run.sh identity # record identity grammar and the publishing contract digest
./run.sh fast    # derived indexes are not stale (pinned Journal-Utilities)
./run.sh full    # split transcripts, integrity gate, manifest reconciliation
./run.sh gnn     # pinned GNN conformance
./run.sh all     # everything a pull request must pass
```

`lint` and `docs` run offline in seconds; `fast`/`full` use the Journal-Utilities
revision pinned in `.github/journal-utilities-pin.json` (an explicit
`--utilities PATH` is accepted only when it sits on that pin). What each arm
actually proves, plus the current job layout, is in
[`docs/OPERATIONS.md`](docs/OPERATIONS.md).

## Citation

If you use this repository in published work, cite it via the Zenodo DOI in
[`CITATION.cff`](CITATION.cff) (also shown as the badge in `README.md`).
