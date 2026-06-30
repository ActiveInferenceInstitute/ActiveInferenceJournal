# Agent guide — docs/

Technical documentation for ActiveInferenceJournal. Start at [`README.md`](README.md).

## For agents

- This folder is **hand-written technical docs**, not generated. Edit prose freely; keep
  it accurate to the actual layout and the [Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities)
  generators.
- The **schema of record** is [`SCHEMA.md`](SCHEMA.md). If the per-item structure changes,
  update it here and mirror it in Journal-Utilities `docs/JOURNAL_SCHEMA.md`.
- Do **not** restate counts (item/video totals) here — they drift. `INDEX.json` is the
  live source of truth.

## Conventions

- Content lives under `../data/`; never put generated content in `docs/`.
- Cross-link with relative paths. Signpost the tooling repo by full GitHub URL.
- Keep each doc single-purpose: SCHEMA (shape), ORGANIZATION (layout), PIPELINE (provenance).

## Parent

Repo root: [`../README.md`](../README.md) · [`../AGENTS.md`](../AGENTS.md).
