# docs — ActiveInferenceJournal technical documentation

Technical documentation for the ActiveInferenceJournal data repository. The journal is a
source-namespaced corpus of transcripts, metadata, captions, translations, and curated
materials from the Active Inference Institute video library.

## Contents

| Doc | What it covers |
| --- | --- |
| [`SCHEMA.md`](SCHEMA.md) | Canonical per-item schema (`metadata.json`, `transcript.*`, `captions/`, `translations/`, `assets/`) and the `INDEX.json` contract. |
| [`ORGANIZATION.md`](ORGANIZATION.md) | The top-level namespace (`data/video/<source>/`, `data/<type>/<source>/`), how series and items are organized, and how to add other channels / non-video sources. |
| [`PIPELINE.md`](PIPELINE.md) | How content is produced and kept complete + idempotent — the collaboration with the [Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities) engine. |
| [`AGENTS.md`](AGENTS.md) | Conventions for AI agents and programs operating on this repo. |

## Quick orientation

- **Machine entry point:** [`../INDEX.json`](../INDEX.json) — every item, its videos, and paths.
- **Human entry point:** [`../INDEX.md`](../INDEX.md) and the repo [`../README.md`](../README.md).
- **Content root:** [`../data/video/activeinferenceinstitute/`](../data/video/activeinferenceinstitute/).
- **Tooling (separate repo):**
  [Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities)
  produces this layout; its `scripts/refactor_journal.py` and `scripts/download_channel.py`
  are the canonical generators. Its `scripts/validate_journal.py` is the read-only
  integrity gate. See Journal-Utilities `docs/JOURNAL_SCHEMA.md` and
  `docs/REFACTOR_READINESS.md`.

## Branches

- `main` — content without audio (lightweight).
- `audio` — `main` + `<item>/audio/<name>.64k.m4a` (64 kbps media), same layout.
