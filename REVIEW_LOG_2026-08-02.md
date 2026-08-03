# REVIEW_LOG — 2026-08-02

Docs-deep review + implementation pass on `ActiveInferenceJournal` (branch `main`).
Started at HEAD `8a923301` (fast-forwarded from local `c48ff132`).

## Phase 0 — Preflight

- Default branch: `origin/main` (confirmed via `git symbolic-ref`).
- `git fetch origin` + `git pull --ff-only`: `c48ff132` → `8a923301` (5 commits,
  transcript raw/derived design + whisperx transcripts + slug renames).
- Working tree was dirty on arrival: 5 deleted caption `.srt` files and ~150
  untracked translation `.srt` files — pre-existing generated-content churn,
  **untouched and unstaged** throughout this pass.
- Doc inventory: root `README.md`, `AGENTS.md`, `LICENSE`, `INDEX.md` (generated),
  `docs/` (`README.md`, `AGENTS.md`, `SCHEMA.md`, `ORGANIZATION.md`, `PIPELINE.md`),
  structural `README.md`/`AGENTS.md` under `data/`, `data/video/`, the channel
  folder, and 19 series folders. CI: `.github/workflows/journal-integrity.yml`.
  No pre-existing TODO/CHANGELOG file. `Journal-Utilities` is not checked out here
  (separate public repo).

## Phase 1 — Mega-deep docs review (findings)

Verified against the actual repo (INDEX.json/INDEX.md, sampled `metadata.json`,
`transcript.json/.txt`, captions, `assets/`, CI config) and the public
Journal-Utilities repo (GitHub API).

**Minor**
1. `README.md` "Learn more" link → HTTP 404 (`activeinference.org/research/journal`).
2. `README.md` referenced `scripts/apply_speaker_names.py` without the owning repo
   (no `scripts/` dir exists here; script lives in Journal-Utilities).
3. `docs/SCHEMA.md` had an odd number of code fences (a stray closing fence
   marker at EOF).
4. `docs/SCHEMA.md` enrichment command omitted the `--journal` flag (inconsistent
   with `PIPELINE.md` and CI); no note that it runs from the Journal-Utilities
   checkout and is dry-run by default.
5. `docs/SCHEMA.md` "SCHEMA.md (mirrored into the journal repo)" — direction wrong;
   the mirror target is Journal-Utilities `docs/JOURNAL_SCHEMA.md`.
6. `docs/SCHEMA.md` claimed a `sources/` registry that exists in neither repo
   (verified via GitHub API contents listing).
7. `docs/SCHEMA.md` described `duplicate_of` as "the two symposium full uploads";
   reality: 34 records (individual symposium talks duplicating full recordings).
8. `docs/SCHEMA.md` per-item `assets/` block omitted `csv/` (legacy AssemblyAI
   sentence exports — present in real items).
9. Long lines: `docs/AGENTS.md` (125), `docs/README.md` (113), and all 19 series
   `AGENTS.md` guides (285–314 chars on the template line).
10. Channel README (`data/video/activeinferenceinstitute/README.md`) restated
    per-series counts that had drifted badly vs `INDEX.json` (e.g. Other 85→49,
    TextbookGroup 150→180, GuestStream 126→127).

**Medium**
11. `docs/SCHEMA.md` framed as "Target schema for the refactor" with a
    "Refactor rules" section — the refactor is long done; the doc should be the
    canonical current schema.
12. No `CONTRIBUTING.md` (new contributor would not know hand-editable vs
    generated, or the CI gate).
13. No `CITATION.cff` (Zenodo DOI badge exists in README; no machine-readable
    citation).

**Major**
14. Generated docs drift system-wide: 19 series `README.md` files restate stale
    counts; `TextbookGroup/README.md` has ~150 broken links (generated for a flat
    `Meeting_NNN` layout; the series now nests `Cohort_N/Meeting_NNN`);
    `Applied Active Inference Symposium/README.md` links to non-existent
    `First_Interval/` etc. (items nest under `2023 Ecosystem Symposium/`,
    `2024/part N`). These are generator-owned (Journal-Utilities) — not
    hand-editable here.
15. (Noted, out of scope) Legacy curated `assets/notes/*.md` contain broken image
    links (`images/orcid.png`, `../../Video/*.PNG`) from pre-refactor curation;
    preserved verbatim like translations.

**Claims verified accurate (no change needed)**
- "Most transcripts are WhisperX-diarized": 444/573 items have `transcript.json`,
  all 444 with `speaker` fields.
- Session-split `_sessNN` blocks and `## <video_id>_sessNN` headings exist
  (2024 symposium parts); multi-part `## <video_id>` headings confirmed.
- `parts[].speakers` mapping, `sessions[]` shape, `youtube_captions.txt`,
  legacy `assets/csv/*.sentences.csv`, `private_videos.json` all as documented.
- Enrichment fields (`doi`, `zenodo`, `thumbnails`, `sessions`, `enriched_from`,
  `paper_title`, `slides_url`) match the SCHEMA table (sampled ModelStream_007,
  ReviewStream, GuestStream_001).
- Every Journal-Utilities script/path referenced in docs exists (verified via
  GitHub API: `apply_speaker_names.py`, `enrich_metadata.py`,
  `generate_journal_indexes.py`, `repair_split_transcripts.py`,
  `validate_journal.py`, `refactor_journal.py`, `download_channel.py`;
  `docs/JOURNAL_SCHEMA.md`, `docs/REFACTOR_READINESS.md`, `CLAUDE.md`).
- All external links return 200 except the one fixed 404 (Zenodo badge,
  YouTube, creativecommons, Journal-Utilities, org sites).

## Phase 2 — Scoped TODO

`TO-DO.md` created at repo root (none existed): Minor / Medium / Major sections,
every finding above with file paths, completed items marked with commit refs,
open items listed at the end.

## Phase 3 — Implementation

| Commit | Scope |
| --- | --- |
| `9cd912f6` | README: fix dead link; qualify `apply_speaker_names.py` path |
| `e4cfe729` | SCHEMA.md modernization (see commit body for the 8 sub-fixes) |
| `4e208d58` | Channel README de-counting; wrap docs + 19 series AGENTS.md |
| `1c6df86e` | CONTRIBUTING.md + CITATION.cff |
| this commit | REVIEW_LOG_2026-08-02.md + TO-DO.md |
| `6618f2cf` | REVIEW_LOG fence-marker wording |
| `21f4ace7` | Regenerate 9 stale series READMEs (counts + links) |
| (final) | README documentation section; TO-DO/REVIEW_LOG update |

Skipped in the first pass, then **run locally**: the three CI gates
(Journal-Utilities cloned read-only to `/tmp/ju-check`; scripts are stdlib-only,
no install needed). All PASS — see Phase 4 follow-up below.

## Phase 4 — Verification & push

- Re-ran markdown link + fence checks on all hand-written docs: clean.
- `git status` contains only the intended files (5 commits); pre-existing dirty
  files (5 deletions, ~150 untracked translations) left untouched.
- Pushed to `origin/main`; confirmed up to date.

## Follow-up (same day) — deferred items

- **CI gates run locally (all PASS):**
  1. `generate_journal_indexes.py --check` → exit 0 (INDEX.json/INDEX.md current).
  2. `repair_split_transcripts.py --check` → exit 0.
  3. `validate_journal.py --manifest …/channel_videos.json` → "journal
     validation: PASS" (metadata_items 573, parts 744, canonical ids 710,
     forbidden_main_files 0, missing_manifest_videos 0; non-blocking warn: 5
     canonical IDs absent from the slightly older manifest — same class of warn
     CI tolerates without `--strict-manifest`).
- **Series README regeneration** (`21f4ace7`): read the current
  Journal-Utilities source first — `generate_journal_indexes.py` writes only
  `INDEX.json`/`INDEX.md`; `refactor_journal.py` writes only item READMEs at
  build time; nothing generates series READMEs. The 19 in-repo series READMEs
  are therefore legacy artifacts that no pipeline overwrites; rebuilt them from
  `INDEX.json` in the established format. 9 of 19 were stale/broken (worst:
  TextbookGroup ~150 dead links, 150→180 items; Symposium dead `First_Interval/`
  links; GuestStream 126→127 items). Verified: 0 broken links across all 19
  (was ~150).
- **Still deferred (genuinely generator-owned):** item README long lines
  (`refactor_journal.py` format), `INDEX.md` 140-char header
  (`generate_journal_indexes.py`), and legacy `assets/notes/*.md` broken image
  links (curated content preserved verbatim).

## Follow-up 2 (same day) — comprehensive completion

- **Item README regeneration** (`7a87b54c`): 573 item READMEs rewritten from
  canonical `metadata.json` in `refactor_journal.py`'s exact format. 250 part
  titles / 38 part URLs / `Contents:` lines had drifted (409 rewritten, 164
  already current). Item READMEs are written only by the one-time refactor
  build — nothing in the routine pipeline overwrites them.
- **Curated-asset image repair** (`dc1ba164`): the
  PhysicsAsInformationProcessing_ChrisFields notes/prose carried 345 broken
  image refs and 69 absolute machine paths (`/mnt/md0/projects/...` — a
  privacy leak in a public repo). Ground truth = the pre-refactor tree at
  `cf7e3458~1`: every ref resolved to its legacy target; legacy image → current
  `assets/images/` file via a verified 233↔233 bijection (name =
  `<legacy dir>__<basename>` or bare basename). 322 refs repaired, 23 refs to
  images absent from the corpus replaced with italic alt-text placeholders,
  CRLF line endings preserved. Repo-wide grep: no `/mnt/`, `/Users/`, or
  Windows-path leaks remain in any tracked `.md`.
- **`docs/ORGANIZATION.md` fix**: "Adding another source" named
  `refactor_journal.py` as the INDEX regenerator; the correct script is
  `generate_journal_indexes.py` (confirmed in generator source + CI).
- **`SECURITY.md` added**: credentials rule (per PIPELINE security note),
  no-audio-on-main, no machine-internal paths, private reporting guidance.
- **Still generator-owned (unchanged):** `INDEX.md` 140-char header —
  `generate_journal_indexes.py --check` compares byte-for-byte, so it is the
  only file that cannot be touched from this repo.
