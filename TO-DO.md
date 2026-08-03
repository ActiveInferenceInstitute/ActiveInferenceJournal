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
- ✓ `docs/ORGANIZATION.md` — fix wrong generator script in "Adding another
  source": `refactor_journal.py` → `generate_journal_indexes.py` (the
  refactor is a migration tool; only the indexes script writes `INDEX.*`).
  (`9b9990c5`)
- ✓ `SECURITY.md` — new: credentials rule (per PIPELINE security note), no
  audio on `main`, no machine-internal paths, private reporting guidance.
  (`9b9990c5`)
- ✓ `README.md` — add Journal integrity CI badge (URL verified 200);
  `docs/README.md` — cross-link root-level guides (CONTRIBUTING, SECURITY,
  CITATION, TO-DO) from Quick orientation; `AGENTS.md` — add TO-DO.md to
  entry points; channel `AGENTS.md` — wrap the 474-char description line.
  (`7e559057`)

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
- ✓ **Regenerate the series `README.md` files** from `INDEX.json` — 9 of 19
  were stale/broken (GuestStream 126 vs 127 items; TextbookGroup 150 vs 180
  items with ~150 dead links to a pre-cohort layout; Symposium links to
  non-existent `First_Interval/`/`part N`). Rebuilt in the established format
  with correct counts, ✓/· transcript status, and working per-item links.
  Verified: 0 broken links across all 19. Note: the current Journal-Utilities
  generator does **not** produce series READMEs (only `INDEX.*` via
  `generate_journal_indexes.py` and item READMEs via `refactor_journal.py`),
  so nothing overwrites these. (`21f4ace7`)
- ✓ **Regenerate the 573 item `README.md` files** from canonical
  `metadata.json` in `refactor_journal.py`'s own format — 250 part titles,
  38 part URLs, and `Contents:` lines had drifted since migration (titles
  enriched from Coda; translations/captions added later). 409 rewritten,
  164 already current. (`7a87b54c`)
- ✓ **Repair broken image references in curated assets** — the
  PhysicsAsInformationProcessing_ChrisFields notes/prose referenced images
  via pre-refactor paths and 69 absolute machine paths (`/mnt/md0/...`,
  a privacy leak). Resolved every ref against the pre-refactor tree
  (cf7e3458~1): 322 refs rewritten to `assets/images/` (233-file bijection
  verified), 23 refs to absent images replaced with italic alt-text
  placeholders, line endings preserved. Verified 0 broken refs remain.
  (`dc1ba164`)

## Verification (this pass)

- All three CI gates run locally against the repo (Journal-Utilities cloned to
  /tmp, read-only): `generate_journal_indexes.py --check` PASS,
  `repair_split_transcripts.py --check` PASS, `validate_journal.py` PASS
  ("journal validation: PASS"; 0 forbidden files, 0 missing manifest videos;
  one non-blocking warn: 5 canonical IDs absent from the slightly older
  manifest).

## Open / deferred

- **`INDEX.md` header line wraps at 140 chars** — produced by
  `generate_journal_indexes.py`; the `--check` gate compares the file
  byte-for-byte against generator output, so it cannot be hand-edited;
  generator-owned.
- **Item README long lines** — inherent to `refactor_journal.py`'s format
  (URL-bearing title lines, `Contents:` line); regenerated in that format,
  not a defect to fix here.
- **Curated assets elsewhere** — after the image-repair pass, no `.md` under
  `assets/` has broken relative refs and no machine paths remain anywhere in
  the repo (verified by grep).
