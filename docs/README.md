# docs — ActiveInferenceJournal technical documentation

Technical documentation for the ActiveInferenceJournal data repository. The journal is a
source-namespaced corpus of transcripts, metadata, captions, translations, and curated
materials from the Active Inference Institute video library.

## Contents

| Doc | What it covers |
| --- | --- |
| [`SCHEMA.md`](SCHEMA.md) | Canonical per-item schema (`metadata.json`, `transcript.*`, `captions/`, `translations/`, `assets/`) and the `INDEX.json` contract. |
| [`ORGANIZATION.md`](ORGANIZATION.md) | The top-level namespace (`data/video/<source>/`, `data/<type>/<source>/`), how series and items are organized, and how to add other channels / non-video sources. |
| [`PIPELINE.md`](PIPELINE.md) | How content is produced and kept complete + idempotent — the collaboration with the [Journal_Utilities](https://github.com/ActiveInferenceInstitute/Journal_Utilities) engine. |
| [`OPERATIONS.md`](OPERATIONS.md) | The gate (`./run.sh` arms), the CI workflows (integrity, GNN conformance, Pages deploy, weekly ingest), pins, dependency updates, local validation, and the branch model. |
| [`m4-site-spec.md`](m4-site-spec.md) | Spec for the M4 static per-item pages + `sitemap.xml`/`robots.txt`, implemented by the Journal-Utilities builder. |
| [`translation-migration-map.md`](translation-migration-map.md) | Item-by-item map of the legacy `Translations/` → `translations/<video_id>.<bcp47>.srt` migration; status: executed (part 2 + pass 2b), 423 files remain in `Translations/`. |
| [`volunteer-transcript-tasks.md`](volunteer-transcript-tasks.md) | Volunteer triage list (I16): the 423 remaining translation files and the 600-file conflicts backlog, by item. |
| [`good-first-issues-draft.md`](good-first-issues-draft.md) | Ready-to-file `good-first-issue` drafts for the highest-value volunteer batches. |
| [`misfiling-findings.md`](misfiling-findings.md) | Captions/translations misfiling dispositions (Textbook Cohort 2 Meeting 20 SRT; 2021 Symposium `Translations/` robotics duplicates). |
| [`AGENTS.md`](AGENTS.md) | Conventions for AI agents and programs operating on this repo. |
| [`documentation-index.md`](documentation-index.md) | Flat index of every long-lived document here and at the repo root. |
| [`_generated/`](_generated/README.md) | Generated facts: gate arm timings and their producers. Never hand-edited. |

## Quick orientation

- **Gate:** `./run.sh` — `lint`, `docs`, `fast`, `full`, `gnn`; every arm is also
  the command CI runs. See [`OPERATIONS.md`](OPERATIONS.md#gate-arms).
- **Machine entry point:** [`../INDEX.json`](../INDEX.json) — every item, its videos, and paths.
- **Human entry point:** [`../INDEX.md`](../INDEX.md) and the repo [`../README.md`](../README.md).
- **Content root:** [`../data/video/activeinferenceinstitute/`](../data/video/activeinferenceinstitute/).
- **Repo-level guides:** [`../CONTRIBUTING.md`](../CONTRIBUTING.md) (what to edit vs.
  generated), [`../SECURITY.md`](../SECURITY.md) (credentials/audio rules),
  [`../CITATION.cff`](../CITATION.cff) (Zenodo citation), [`../TO-DO.md`](../TO-DO.md)
  (scoped improvement list).
- **Tooling (separate repo):**
  [Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal_Utilities)
  produces this layout; its `scripts/refactor_journal.py` and `scripts/download_channel.py`
  are the canonical generators. Its `scripts/validate_journal.py` is the read-only
  integrity gate. See Journal-Utilities `docs/JOURNAL_SCHEMA.md` and
  `docs/REFACTOR_READINESS.md`.

## Branches

- `main` — content without audio (lightweight).
- `audio` — `main` + `<item>/audio/<name>.64k.m4a` (64 kbps media), same layout.

See also: [`OPERATIONS.md`](OPERATIONS.md) — CI workflows and local validation;
[`m4-site-spec.md`](m4-site-spec.md) — spec for the M4 static per-item pages +
sitemap/robots (for the Journal_Utilities builder agent); and
[`misfiling-findings.md`](misfiling-findings.md) — captions/translations misfiling
dispositions (Textbook Cohort 2 Meeting 20 SRT; 2021 Symposium `Translations/`
robotics duplicates).

