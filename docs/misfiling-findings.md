# Misfiling findings — captions and translations triage

Recorded: 2026-09-23 (M4-pages wave, fleet handoff `/tmp/aii_journal_handoff.md`).
Scope: the two known misfilings called out in the handoff baseline, verified
against the real tree. Generator-owned rewrites should consult this file.

## 1. Textbook Cohort 2 Meeting 20 SRT in `ModelStream_011/captions/` — FIXED

- Symptom: `ModelStream/ModelStream_011/captions/` held
  `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).en.srt`
  alongside the item's own `youtube_captions.txt` for video `Y9hP79tBXHo`
  (ModelStream #011.1 ~ Poisson Variational Autoencoder).
- Correct home identified: `TextbookGroup/ParrPezzuloFriston2022/Cohort_2/Meeting_020`
  (canonical video `QjGcN1l6NXg`, resolved via `INDEX.json`).
- Disposition: `git mv` into that item's `captions/` (non-destructive rename,
  committed on `feat/m4-pages`).
- Context: this file was one of **58 byte-identical copies** of the same
  YouTube-derived SRT scattered across unrelated items (GuestStream 051–070,
  MathStream 006–012, ModelStream 008–013, MorphStream 001–005, Courses,
  symposium items, TextbookGroup Cohort_4). Commit `0bbc97d1` (2026-08-11)
  already deleted one copy (Insights_005) and repurposed 4 more as translation
  sources; the other 57 copies remain and are tracked as the broader J3/I10
  captions-naming work item in Journal-Utilities, not re-fixed here. The copy
  in `Meeting_020` was chosen because that item lacked a `.en.srt` variant
  (only `.eng(transcribed).srt`), so the move fills the canonical item's
  YouTube-captions slot without overwriting anything.

## 2. 2022 Robotics translations inside `2021 Symposium .../Translations/` — DOCUMENTED, NOT MOVED

- Symptom:
  `Applied Active Inference Symposium/2021 Symposium with Karl Friston/Translations/`
  (capital-T, item videos `INRaCBikpso`, `X2GwqUVLlcs`, `hW9IiOujS1E` — the
  three Prof. Karl Friston symposium parts) contains 22 files named
  `2nd Applied Active Inference Symposium on  Robotics  ~ {1st,2nd} session.<lang>.srt`.
  These belong to `2022 Symposium on Robotics` (videos `zm2d9o5n0PU`,
  `dTVHHenms_Y`), which already has its own lowercase `translations/` with the
  same 22 files.
- Verified: every one of the 22 pairs is near-identical (cue counts equal,
  e.g. 5638 cues for the 1st session de pair); diffs are a handful of
  re-translated lines. The 2021 item's directory additionally holds the 33
  genuine Friston-symposium translations (3 parts × 11 languages).
- Why not moved: the robotics files are **not an orphaned misfiling but a
  near-duplicate second copy**; `git mv` would either clobber the 2022 item's
  (newer-translation) files or create a `migrate/` duplicate that the builder
  would count twice — both regressions. The M2 translation migration
  (`git mv Translations/ → translations/`, normalize `<video_id>.<bcp47>.srt`,
  record `previous_paths` in `metadata.json`) is the right vehicle: during that
  per-series PR the duplicates should be diffed once more and the loser deleted,
  keeping the 2021 item's directory for the 33 genuine Friston files only.
- Interim state: left untouched on `feat/m4-pages`; case-sensitivity already
  hides the capital-T directory from the site builder (see
  [`m4-site-spec.md`](m4-site-spec.md) and handoff item I4), so the duplicates
  are not user-visible on the site.
