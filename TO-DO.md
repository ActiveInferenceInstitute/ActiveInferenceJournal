# TO-DO — ActiveInferenceJournal docs pass

Last reviewed: 2026-08-02 (docs-deep review + implementation; see
[`REVIEW_LOG_2026-08-02.md`](REVIEW_LOG_2026-08-02.md)).

Sections: **Minor** = typo, broken link, formatting; **Medium** = stale section
rewrite, doc restructure, added missing guide; **Major** = large doc system
overhaul, cross-cutting refactors.

## Minor

- ✓ `README.md` — replace dead "Learn more" link (404) with the live
  Institute learning page. (`9cd912f6`)
- ✓ `README.md` — qualify `scripts/apply_speaker_names.py` as
  `Journal-Utilities/scripts/apply_speaker_names.py` (no `scripts/` here).
  (`9cd912f6`)
- ✓ `docs/SCHEMA.md` — remove stray unclosed code fence at EOF (odd fence
  count). (`e4cfe729`)
- ✓ `docs/SCHEMA.md` — enrichment command missing `--journal` flag; note
  dry-run default and that commands run from the Journal-Utilities checkout.
  (`e4cfe729`)
- ✓ `docs/SCHEMA.md` — fix "mirrored into the journal repo" direction
  (mirror target: Journal-Utilities `docs/JOURNAL_SCHEMA.md`). (`e4cfe729`)
- ✓ `docs/SCHEMA.md` — remove `sources/` registry claim (exists in neither
  repo; verified). (`e4cfe729`)
- ✓ `docs/SCHEMA.md` — correct `duplicate_of` description: 34 per-talk
  symposium records, not "the two symposium full uploads". (`e4cfe729`)
- ✓ `docs/SCHEMA.md` — add `assets/csv/` (legacy AssemblyAI sentence
  exports) to the per-item layout. (`e4cfe729`)
- ✓ `docs/AGENTS.md`, `docs/README.md` — wrap long lines. (`4e208d58`)
- ✓ 19 series `AGENTS.md` guides — wrap 285–314-char template lines to ≤100
  chars. (`4e208d58`)

## Medium

- ✓ `docs/SCHEMA.md` — reframe from "Target schema for the refactor" to the
  canonical current schema; convert "Refactor rules (non-destructive)" into
  a "Layout history" section pointing at Journal-Utilities
  `docs/REFACTOR_READINESS.md`; keep the live coverage invariant.
  (`e4cfe729`)
- ✓ `data/video/activeinferenceinstitute/README.md` — remove stale per-series
  counts (drifted vs `INDEX.json`), link the live `INDEX.md`/`INDEX.json`
  instead, per the repo's own "counts drift" convention. (`4e208d58`)
- ✓ `CONTRIBUTING.md` — new: hand-editable vs generated files, repo rules,
  CI gate + local validation commands. (`1c6df86e`)
- ✓ `CITATION.cff` — new: dataset citation, Zenodo DOI
  `10.5281/zenodo.21074926` (resolved from the README badge), CC-BY-4.0.
  (`1c6df86e`)

## Major

- ✓ `docs/SCHEMA.md` modernization (cross-cutting restructure of the schema
  of record — see Medium above). (`e4cfe729`)

## Open / deferred

- **Regenerate generated docs (Journal-Utilities owned).** The 19 series
  `README.md` files restate stale counts (GuestStream 126 vs 127 items;
  TextbookGroup 150 vs 180), `TextbookGroup/README.md` carries ~150 broken
  links (generated for a flat `Meeting_NNN` layout — the series now nests
  `Cohort_N/Meeting_NNN`), and `Applied Active Inference Symposium/README.md`
  links to non-existent `First_Interval/`, `part N/` paths (items nest under
  `2023 Ecosystem Symposium/`, `2024/part N`). Fix in Journal-Utilities
  (regenerate series READMEs; teach the generator nested series folders),
  then regenerate here. *Reason deferred: generator lives in a sibling repo;
  per `AGENTS.md`, generated files are not hand-edited.*
- **Item-level README long lines.** Generated item `README.md` files have
  115–165-char lines — cosmetic; generator-owned, fold into the regeneration
  item above.
- **`INDEX.md` header line wraps at 140 chars** — generated; generator-owned.
- **Legacy curated `assets/notes/*.md` broken image links** (`images/orcid.png`,
  `../../Video/*.PNG`) — pre-refactor curated content preserved verbatim;
  left untouched (content, not documentation).
- **Full CI suite not run locally** — the `--check` gates require a
  Journal-Utilities checkout (sibling repo, not present). CI
  (`.github/workflows/journal-integrity.yml`) runs the three gates on push.
