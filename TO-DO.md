# TO-DO — ActiveInferenceJournal docs pass

Last reviewed: 2026-11-12 (gate and documentation pass 5, below); previously
2026-11-12 (pass 4), 2026-08-02 (docs-deep review + implementation; see
[`REVIEW_LOG_2026-08-02.md`](REVIEW_LOG_2026-08-02.md)) and 2026-11-11
(docs completion pass 3).

Sections: **Minor** = typo, broken link, formatting; **Medium** = stale section
rewrite, doc restructure, added missing guide; **Major** = large doc system
overhaul, cross-cutting refactors.

## Gate and documentation pass 5 (2026-11-12)

- ✓ **`./run.sh identity` — new arm, and the publishing contract it enforces.**
  `docs/workflows/record-identity.schema.json` (`record-identity/v1`) is the one
  grammar for `metadata.json` record ids and the cross-repository join keys;
  `docs/workflows/publishing.md` is the group contract that pins it;
  `journal-integrity.yml` runs the arm directly after `docs`, and the sidecar
  gained an `identity` task. (`c7c555cb`, #43)
- ✓ **The contract's drift test now works for every artifact kind.** The digest
  block accepted only `.json` names, so a member that pinned `identity.py` — the
  copy its own migration step tells it to make — was told "records no digest"
  forever. The parser accepts `.json`, `.py`, `.mjs`, `.sh`, `.md` and `.ts`, and
  every recorded entry is resolved and re-hashed, so a stale or unlocatable pin
  fails instead of being ignored. `scripts/gate/identity_selftest.py` builds a
  fake checkout and asserts both directions (matching copy passes, diverged copy
  reports the drift); the arm runs it on every invocation. (`d8ec888a`, #44)
- ✓ **The GNN parser is bound to the pinned revision, not to the tag.**
  `arm_gnn.py` keys its environment cache by repository, revision and
  interpreter, and refuses a parser whose `direct_url.json` records another
  commit — a revision bump under the unchanged tag `v5.0.3` can no longer verify
  the old parser and print the new pin. (`1976ca15`, #42)
- ✓ **Sidecar publishing docs resolve from the repository root.**
  `.aii/config.yaml` points at `../docs/workflows/publishing.md` and carries the
  `docs/INTEGRATION.md` entry again, matching `.aii/docs/INTEGRATION.md` and
  `.aii/README.md`. (`a7c80580`, #45)
- ✓ **Checked, not changed: there is no `pymdp` / `inferactively-pymdp`
  dependency here.** The only non-`data/` mentions are item titles and legacy
  translation filenames in `docs/volunteer-transcript-tasks.md`,
  `docs/good-first-issues-draft.md` and `docs/translation-migration-map.md`;
  there is no 1.0.5 pin to adopt.
- Verification (this pass): `./run.sh docs` → `gate: docs: ok (765 Markdown
  files)` on `a7c80580`. Hosted Actions cannot corroborate anything — every run
  starts and is rejected with "The job was not started because your account is
  locked due to a billing issue" (run `43252922624`; see Open below).

## Gate and documentation pass 4 (2026-11-12)

- ✓ **`./run.sh` — new gate entry point** with separately runnable arms (`lint`,
  `docs`, `fast`, `full`, `gnn`, `all`, `bench`). Every arm is the command CI
  runs; the two Python heredocs that lived inline in `journal-integrity.yml`
  (manifest reconciliation, GNN install + verification) moved into
  `scripts/gate/` so they are one file, not two copies.
- ✓ **One Journal-Utilities pin** — `.github/journal-utilities-pin.json`
  (`journal-utilities-pin/v1`): a `gate` revision and an `ingest` role (needed
  because `journal_utilities.ingest.ytdlp` does not exist at the gate revision).
  Both workflows take their `ref` from `scripts/gate/pin.py`, and `./run.sh lint`
  fails if a literal SHA reappears in a workflow.
- ✓ **GNN conformance split into its own workflow** (`gnn-conformance.yml`, job
  `gnn-conformance`, display name `gnn conformance (pinned)`), so
  `deploy-pages.yml` no longer waits on a pip install through `workflow_call`.
- ✓ **`docs/documentation-index.md` — new** flat index; `./run.sh docs` fails
  when a document under `docs/` is unreachable from it.
- ✓ **`docs/_generated/` — new** generated-facts directory: `gate-timings.md` is
  written by `./run.sh bench`, and `gate-baseline.json` is the recorded
  pre-change receipt that table renders. No timing is typed by hand.
- ✓ **Documented pins** — `.github/GNN.md` now records the conformance job key
  and display name, the pin schema and revision, and exactly what it parses.

## Docs completion pass 3 (2026-11-11)

- ✓ **`docs/OPERATIONS.md` — new.** Documents the three CI workflows
  (`journal-integrity`, `deploy-pages`, `weekly-ingest`), the pinned
  Journal-Utilities and GNN revisions, Dependabot, the local validation
  commands, and the branch model.
- ✓ **`docs/README.md`** — index now links every document in `docs/`
  (previously omitted `OPERATIONS.md`, `m4-site-spec.md`,
  `misfiling-findings.md`, `volunteer-transcript-tasks.md`,
  `good-first-issues-draft.md` from the table).
- ✓ **`README.md`** — added a table of contents, a status statement (what works
  offline, what needs the sibling Journal-Utilities checkout or network), and an
  install/usage/validation section; the Pages site is described as a static
  bundle built by Journal-Utilities, not a Jekyll build.
- ✓ **`AGENTS.md`** — added the real test/lint command (`journal-check` and the
  CI gate) and pointed at `docs/OPERATIONS.md`.
- ✓ **`.github/README.md` — new.** Folder guide for the workflows, GNN pin and
  Dependabot config.
- ✓ **`.aii/`** — `config.yaml` `artifacts[]` now lists the `INDEX.json`/`INDEX.md`
  entry points; rendered `README.md`/`docs/INTEGRATION.md` hand-synced (the
  `aii_platform.aii_sidecar docs` renderer was unavailable offline).

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
- ✓ **M2 translations migration (J2/Y15)** — 2,880 legacy `Translations/` files
  across 131 items migrated non-destructively: 1,857 now normalized as
  `translations/<video_id>.<bcp47>.srt` (talkslug suffix for per-talk files in
  single-part interval items; 13 cross-item misfiles rescued via INDEX
  title-verification), 600 multi-version conflicts quarantined under
  `translations/conflicts/<series>/` with reasons in
  [`docs/translation-migration-map.md`](docs/translation-migration-map.md)
  (CONFLICTS appendix), 423 machine-unresolvable files left in place for
  volunteer triage (I16). Original paths recorded in each item's
  `metadata.json` `previous_paths` (1,857 entries). Verified with
  `validate_journal.py` (PASS) after every pass. (`74aab8f4`..`e38ae28f`)

## Verification (this pass)

- All three CI gates run locally against the repo (Journal-Utilities cloned to
  /tmp, read-only): `generate_journal_indexes.py --check` PASS,
  `repair_split_transcripts.py --check` PASS, `validate_journal.py` PASS
  ("journal validation: PASS"; 0 forbidden files, 0 missing manifest videos;
  one non-blocking warn: 5 canonical IDs absent from the slightly older
  manifest).

## Open / deferred

- **Hosted GitHub Actions is locked, org-wide.** Every run dies before its first
  step with "The job was not started because your account is locked due to a
  billing issue" (run `43252922624` for `estate/sidecar-defaults`; the CodeQL
  default-setup run `43264122709` fails the same way, 2026-11-12). No pull
  request can show a green check until the organisation's billing is restored, so
  `./run.sh all` locally is the only evidence a PR can carry. Owner: Institute
  GitHub organisation admin; the fix is outside this repository.
- **Legacy translation triage (I16).** 423 `.srt` files remain in capital-T
  `Translations/` across 30 items, and 600 quarantined files sit under
  `translations/conflicts/` across 44 items (counts re-derived from
  `git ls-files`, 2026-11-12; both are listed row by row in
  [`docs/volunteer-transcript-tasks.md`](docs/volunteer-transcript-tasks.md)).
  Each remaining file needs a human to confirm its `video_id` and language
  before the two-step `git mv` — no script can settle a guess, which is why the
  M2 pass stopped here. Owner: volunteers, coordinated from that page.
- **Weekly ingest is still a dispatch-only draft, and M5 does not exist.**
  `weekly-ingest.yml` has no `schedule:` and its guard fails any non-dispatch
  run; correspondingly `arm_manifest.py --strict` (manifest age and duplicate
  ids as failures) is documented as landing "when that lands"
  ([`docs/OPERATIONS.md`](docs/OPERATIONS.md), "Weekly ingest (draft)").
  Owner: maintainers; blocked on reviewing Journal-Utilities `docs/m3-ingest.md`
  and removing the guard, which is outside this repository.
- **GNN pin is `v5.0.3` (`8f293d9b`), one minor behind the org-wide `v5.1.0`
  (`75c834bd`).** Nothing here consumes the newer parser — the arm validates
  whatever revision `.github/gnn-pin.json` names — so this is a reviewed
  one-file bump (`./run.sh gnn --cold`) rather than a defect. Owner:
  maintainers.
- **`estate/sidecar-defaults` is unmerged with no PR.** One commit ahead of
  `main` (`a93f103c`), changing only `.aii/config.yaml` (drops
  `relation: references` from the Active_Inference_Ontology relation). Land it
  through the sidecar generator or delete the branch. Owner: whoever ran the
  estate sidecar pass; nothing in this repository blocks it except the hosted
  gate being unavailable.
- **`INDEX.md` line width** — generator output: the summary line is 143
  characters, item lines exactly 140. `generate_journal_indexes.py --check`
  compares the file byte-for-byte with generator output, so it cannot be
  hand-edited; generator-owned (Journal-Utilities).
- **Item README long lines** — inherent to `refactor_journal.py`'s format
  (URL-bearing title lines, `Contents:` line); regenerated in that format,
  not a defect to fix here.

## M4-pages wave (feat/m4-pages, 2026-09-23)

- ✓ **I4 verified on the real tree** — builder reads only lowercase
  `translations/` (Journal-Utilities `src/journal_utilities/site/builder.py:121`);
  tree holds 13 items with lowercase `translations/` (~336 SRTs) vs 131 items
  with capital-T `Translations/` (~2,880 SRTs); live `manifest.json` shows
  languages for 13/573 items (129 language entries). Fix + spec in
  [`docs/m4-site-spec.md`](docs/m4-site-spec.md) §0; permanent fix = M2
  translation migration.
- ✓ **Textbook Cohort 2 Meeting 20 SRT misfiled in
  `ModelStream_011/captions/`** — `git mv` to canonical
  `TextbookGroup/ParrPezzuloFriston2022/Cohort_2/Meeting_020/captions/`
  (video `QjGcN1l6NXg` via INDEX.json). 57 further byte-identical copies
  remain scattered (GuestStream/MathStream/ModelStream/MorphStream/Courses/
  symposium/Cohort_4) — owned by the J3/I10 captions-naming validator, see
  [`docs/misfiling-findings.md`](docs/misfiling-findings.md).
- ✓ **2022 Robotics translations inside 2021 Symposium `Translations/`** —
  verified near-duplicate second copy (22 files, diffs are re-translated
  lines); documented rather than moved (a move would clobber or double-count);
  to be resolved during the M2 per-series migration —
  [`docs/misfiling-findings.md`](docs/misfiling-findings.md) §2.
- ✓ **README.md** — Pages site link added.
- ✓ **`docs/m4-site-spec.md`** — M4 builder spec (static
  `/item/<slug>/index.html`, schema.org VideoObject JSON-LD, canonical/og,
  sitemap.xml + robots.txt), implemented by Journal-Utilities.

## M4 shipped (2026-11-02)

- ✓ **Builder implements the spec** — Journal-Utilities emits one
  `/item/<slug>/index.html` per `INDEX.json` item plus `sitemap.xml` and
  `robots.txt`, where `<slug>` is the item's INDEX path below its source
  directory. The flat `(series, item)` key was **not** unique: 573 records
  collapsed onto 444 keys, so 129 records silently overwrote another item's
  page, payload and manifest entry (one `TextbookGroup/Meeting_007` key covered
  8 cohort records; the check could not see it because it counted write
  operations, not files). Pages went 444 → 573, distinct manifest ids 444 → 573,
  sitemap unique `<loc>` 445 → 574; 369 published URLs kept their exact
  address, 204 pages are new, 75 flat shortcuts now resolve one level deeper
  under the item's own directory.
- ✓ **Deploy workflow pinned to the path-keyed builder, build now passes
  `--apply`** — the builder is dry-run by default, so a pin bump without the
  flag would publish an empty site. The post-deploy smoke test now covers
  `sitemap.xml`, `robots.txt`, one deep TextbookGroup item page and its payload,
  and asserts the item page's canonical link is server-rendered.
- ✓ **Translations prerequisite (I4)** — the pinned builder reads both
  `translations/` and `Translations/` (lowercase preferred), so the deploy sees
  every item's SRT files; the M2 migration has moved 2,193 `.srt` files across
  128 items to lowercase, with 423 files across 30 items still to migrate.

