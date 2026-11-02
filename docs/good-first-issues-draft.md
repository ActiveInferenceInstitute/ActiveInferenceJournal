# Good-first-issue drafts — I16 translations migration

Drafted 2026-09-24 against branch `feat/m2-translations` (HEAD `21c58548`). These are the ten
highest-value batches from [volunteer-transcript-tasks.md](volunteer-transcript-tasks.md) Part A
(423 REMAINING files). File each as a GitHub issue with label `good-first-issue`; keep the body
verbatim except for the checklists. The remaining batches (MathStream empty-title items, the 2021
'pt. 1 (Education)' investigation, and the 600-file conflicts backlog) follow once these land — see
the triage doc Parts B and C.

Common body for every issue (append below the issue-specific scope):

```markdown
**Read first:** [docs/volunteer-transcript-tasks.md](../docs/volunteer-transcript-tasks.md) —
sections "The 30-minute task (per file)" and "Exact command pattern".

**Steps, per file:**
1. Verify the guessed `video_id` in the item's `metadata.json` + a YouTube spot-check of the part.
2. Confirm the language by opening the `.srt` (normalize legacy codes per the migration map).
3. Move with the two-step `git mv` into `translations/<video_id>.<bcp47>.srt`.
4. Append the original repo-relative path to the destination item's `metadata.json` `previous_paths`.
5. One path-scoped commit per item: `translations(<series>): migrate <N> legacy files (I16 triage)`.

**Acceptance criteria:**
- [ ] every listed file moved (or deleted, if byte-identical to an already-migrated target) with `previous_paths` recorded
- [ ] no listed file remains in the item's `Translations/` folder; empty `Translations/` and `translations_tmp/` removed
- [ ] spot-checked target files open as valid subtitles and match the verified part/language
```

## 1. Migrate the 2021 Symposium leftovers: rehome 22 Robotics files, move 11 "pt. 3 (Tools)" files (33 files)

- **Series:** Applied Active Inference Symposium
- **Files:** 33
- **Estimated time:** ~120 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
The legacy `Translations/` folder of the 2021 Karl Friston symposium item holds two full language sets (de, es, fr, it, ja, ko, nl, pt, ru, zh-Hans, zh-Hant) of the **2nd Applied Active Inference Symposium on Robotics (2022)** — a different event, misfiled here. The correct destination item exists with two parts (1st session `zm2d9o5n0PU`, 2nd session `dTVHHenms_Y`); this is a cross-item rehome. The same folder also holds 11 files for 'pt. 3 (Tools)' — an in-item move to part `hW9IiOujS1E` ('…1st Applied Active Inference Symposium, part 3 (.tools)').

**Scope (from the triage doc, Part A):**
- Item `Applied Active Inference Symposium/2021 Symposium with Karl Friston` → rehome into `Applied Active Inference Symposium/2022 Symposium on Robotics`
  - 11 files, stem `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session` → target `translations/zm2d9o5n0PU.<bcp47>.srt`
  - 11 files, stem `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session` → target `translations/dTVHHenms_Y.<bcp47>.srt`
  - 11 files, stem `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools)` → target `translations/hW9IiOujS1E.<bcp47>.srt`
```

## 2. Rehome 8 Cohort 3 Meeting 1 translation files from Cohort_1/Meeting_001 into Cohort_3/Meeting_001

- **Series:** TextbookGroup
- **Files:** 8
- **Estimated time:** ~45 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
Eight translation files (es, fr, it, nl, pt, ru, zh-Hans, zh-Hant) named "ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)" sit in the Cohort 1, Meeting 1 item. The stem is a title-exact match for Cohort_3/Meeting_001 part `G9GfOMjF4g0`. Cross-item rehome.

**Scope (from the triage doc, Part A):**
- Item `TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_001` → rehome into `TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_001`
  - 8 files, stem `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)` → target `translations/G9GfOMjF4g0.<bcp47>.srt`
```

## 3. Rehome 11 LiveStream 053.1 files from LiveStream_052, then migrate the 22 remaining LiveStream_053 files

- **Series:** Livestream
- **Files:** 33
- **Estimated time:** ~90 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
Eleven translation files named "ActInf Livestream 053.1 ~ Snakes and Ladders…" sit in the LiveStream_052 item (misfiled — they belong to LiveStream_053 part `iHgxmn0ockg`); LiveStream_053 itself also still holds 22 of its own unmigrated files (11 × #053.0 → `c7ybFyP9KrI`, 11 × #053.1 → `iHgxmn0ockg`). Do the rehome first, then the in-item migrations.

**Scope (from the triage doc, Part A):**
- Item `Livestream/LiveStream_052` → rehome into `Livestream/LiveStream_053`
  - 11 files, stem `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'` → target `translations/iHgxmn0ockg.<bcp47>.srt`
- Item `Livestream/LiveStream_053`
  - 11 files, stem `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'` → target `translations/c7ybFyP9KrI.<bcp47>.srt`
  - 11 files, stem `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'` → target `translations/iHgxmn0ockg.<bcp47>.srt`
```

## 4. Migrate the BookStream 001/002 batches (65 files)

- **Series:** BookStream
- **Files:** 65
- **Estimated time:** ~150 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
BookStream_001 still holds 46 legacy files across six stems ("Active Inference BookStream 001.010/012/02/06/08/1 ~ Governing Continuous Transformation…"). Each token matches exactly one of the item's 12 same-titled parts; the extra "Active Inference" prefix defeated the M2 auto-matcher. Two files (`001.010`, `001.08` transcripts) have no language suffix — inspect content (likely `en`). BookStream_002 holds 19 more across two stems: "002.0 ~ …Chapters 1, 2, 3, 6" → part `FV7pW4p60VI` (#002.01 overview) and "002.02 ~ …Chapters 4, 5, 7, 8" → part `3_5pTCguAv4` (#002.02 overview); the chapter list in each stem matches the part title exactly.

**Scope (from the triage doc, Part A):**
- Item `BookStream/BookStream_001`
  - 1 files, stem `Active Inference BookStream 001.010 ~  Governing Continuous Transformation_transcript` → target `translations/eIZjx0miM9o.<bcp47>.srt`
  - 11 files, stem `Active Inference BookStream 001.012 ~  Governing Continuous Transformation` → target `translations/5IGzzm28qec.<bcp47>.srt`
  - 11 files, stem `Active Inference BookStream 001.02 ~  Governing Continuous Transformation` → target `translations/d8c0iFU8vms.<bcp47>.srt`
  - 11 files, stem `Active Inference BookStream 001.06 ~  Governing Continuous Transformation` → target `translations/0P_6ME2LpCw.<bcp47>.srt`
  - 1 files, stem `Active Inference BookStream 001.08 ~  Governing Continuous Transformation_transcript` → target `translations/yNZg5b63hb8.<bcp47>.srt`
  - 11 files, stem `Active Inference BookStream 001.1 ~  Governing Continuous Transformation` → target `translations/FB_93-zDqNo.<bcp47>.srt`
- Item `BookStream/BookStream_002`
  - 8 files, stem `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6` → target `translations/FV7pW4p60VI.<bcp47>.srt`
  - 11 files, stem `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8` → target `translations/3_5pTCguAv4.<bcp47>.srt`
```

## 5. Disambiguate and migrate the ModelStream 007/008/009 batches (55 files)

- **Series:** ModelStream
- **Files:** 55
- **Estimated time:** ~120 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
ModelStream_007 (11 files, "mo007-2" → part `uX8iSoDR83g` #007.2), ModelStream_008 (22 files across two stems → part `Fh1e4sKh3Vs` — Tom Ringstrom "Reward is Not Necessary"; two parts share the "#008.1" token, the title picks the right one) and ModelStream_009 (22 files → part `CEKWhxnH3-E` — Aswin Paul "On efficient computation"; again two "#009.1" parts, the title decides). Verify both disambiguations by opening the two candidate videos before moving.

**Scope (from the triage doc, Part A):**
- Item `ModelStream/ModelStream_007`
  - 11 files, stem `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp` → target `translations/uX8iSoDR83g.<bcp47>.srt`
- Item `ModelStream/ModelStream_008`
  - 11 files, stem `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary` → target `translations/Fh1e4sKh3Vs.<bcp47>.srt`
  - 11 files, stem `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary` → target `translations/Fh1e4sKh3Vs.<bcp47>.srt`
- Item `ModelStream/ModelStream_009`
  - 11 files, stem `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference` → target `translations/CEKWhxnH3-E.<bcp47>.srt`
  - 11 files, stem `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference` → target `translations/CEKWhxnH3-E.<bcp47>.srt`
```

## 6. Migrate the GuestStream 015/016/029/032/044 batches (56 files)

- **Series:** GuestStream
- **Files:** 56
- **Estimated time:** ~120 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
Five GuestStream items with unmigrated full language sets: #015.3 Bobby Azarian "Teleological Stance" → `S-tFHIqtbSI`; #016.2 Mark Solms "Consciousness as Precision Optimization" (AutoCaption variants, stem typo '#0161.2') → `c0_Vf5_qiWk` (compare against already-migrated #016.2 files — delete exact dupes); #029.1 "Making Up Our Minds… MathArt" → `UuXAjY9Wgdg` (sole part, metadata title empty — verify on YouTube); #032.1 Adam Pease → `0pMxBM3ahwQ`; #044.1 Tsuchiya & Saigo → `FymR0rKdLZo`.

**Scope (from the triage doc, Part A):**
- Item `GuestStream/GuestStream_015`
  - 12 files, stem `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023` → target `translations/S-tFHIqtbSI.<bcp47>.srt`
- Item `GuestStream/GuestStream_016`
  - 11 files, stem `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption` → target `translations/c0_Vf5_qiWk.<bcp47>.srt`
- Item `GuestStream/GuestStream_029`
  - 11 files, stem `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present` → target `translations/UuXAjY9Wgdg.<bcp47>.srt`
- Item `GuestStream/GuestStream_032`
  - 11 files, stem `ActInf GuestStream 032-1 ~ Adam Pease (audio)` → target `translations/0pMxBM3ahwQ.<bcp47>.srt`
- Item `GuestStream/GuestStream_044`
  - 11 files, stem `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video` → target `translations/FymR0rKdLZo.<bcp47>.srt`
```

## 7. Migrate the GuestStream 046/047/053/055/058 batches (56 files)

- **Series:** GuestStream
- **Files:** 56
- **Estimated time:** ~120 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
Five more GuestStream items, each a sole-part title match: #046.1 Denise Holt "Active Inference AI & the Spatial Web" → `dUW8cD8XUec`; #047.1 Bellini-Leite "Predicting & Reflecting" → `O6adLcDhOYU`; #053.1 Tolchinsky "A case for chaos theory" → `_GHJO_bnyrY`; #055.1 Pang & Fornito "Geometric constraints" → `a4DC1YCVpsU`; #058.1 "Working with Gerald Edelman" → `Sz7ZP2N6DuE`.

**Scope (from the triage doc, Part A):**
- Item `GuestStream/GuestStream_046`
  - 12 files, stem `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web` → target `translations/dUW8cD8XUec.<bcp47>.srt`
- Item `GuestStream/GuestStream_047`
  - 11 files, stem `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite` → target `translations/O6adLcDhOYU.<bcp47>.srt`
- Item `GuestStream/GuestStream_053`
  - 11 files, stem `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory` → target `translations/_GHJO_bnyrY.<bcp47>.srt`
- Item `GuestStream/GuestStream_055`
  - 11 files, stem `gs055 1 ~ James Pang, Alex Fornito Geometric constraints` → target `translations/a4DC1YCVpsU.<bcp47>.srt`
- Item `GuestStream/GuestStream_058`
  - 11 files, stem `gs058-1 Working with Gerald Edelman` → target `translations/Sz7ZP2N6DuE.<bcp47>.srt`
```

## 8. Migrate the Courses Semiotics & Semantics batches (22 files)

- **Series:** Courses
- **Files:** 22
- **Estimated time:** ~45 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
Two single-part course items from Lorena Sganzerla's 2023 "Active Inference for the Social Sciences" series still hold full 11-language sets: the Discussion item (stem "Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12" → sole part `MrAiB9X7Ock`) and the Lecture item (stem "CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30" → sole part `4ijYLWm4P2I`). The stems differ from the part titles only by date/course-code tokens.

**Scope (from the triage doc, Part A):**
- Item `Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Discussion`
  - 11 files, stem `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12` → target `translations/MrAiB9X7Ock.<bcp47>.srt`
- Item `Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Lecture`
  - 11 files, stem `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30` → target `translations/4ijYLWm4P2I.<bcp47>.srt`
```

## 9. Migrate the Livestream token batches 001/006/016/032/045/047 (36 files)

- **Series:** Livestream
- **Files:** 36
- **Estimated time:** ~90 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
Six smaller Livestream items: LiveStream_001 (1 file → `C94WDXAe4EE`); LiveStream_006 (1 file, "#006.2 (2020) REUPLOAD" → `HQadNEGAtbY` — two parts share "#006.2", the "(2020)" qualifier decides); LiveStream_016 (11 → `93lAa-xEmHY` #016.2); LiveStream_032 (11 → `7_JLMK3agpA` #032.0); LiveStream_045 (1 file, unknown legacy code 'che(translated)' → `S5-jXzhiG18`, identify the language by content); LiveStream_047 (11 → `riJYh87FPx4` #047.2).

**Scope (from the triage doc, Part A):**
- Item `Livestream/LiveStream_001`
  - 1 files, stem `Active Inference Podcast #001 “Narrative as active inference` → target `translations/C94WDXAe4EE.<bcp47>.srt`
- Item `Livestream/LiveStream_006`
  - 1 files, stem `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD` → target `translations/HQadNEGAtbY.<bcp47>.srt`
- Item `Livestream/LiveStream_016`
  - 11 files, stem `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP` → target `translations/93lAa-xEmHY.<bcp47>.srt`
- Item `Livestream/LiveStream_032`
  - 11 files, stem `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets` → target `translations/7_JLMK3agpA.<bcp47>.srt`
- Item `Livestream/LiveStream_045`
  - 1 files, stem `ActInf Livestream #045.2 ~ The free energy principle made simpler but not too simple` → target `translations/S5-jXzhiG18.<bcp47>.srt`
- Item `Livestream/LiveStream_047`
  - 11 files, stem `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction` → target `translations/riJYh87FPx4.<bcp47>.srt`
```

## 10. Migrate the LiveStream 054 batch (34 files)

- **Series:** Livestream
- **Files:** 34
- **Estimated time:** ~90 minutes
- **Labels:** `good-first-issue`, `i16-translations`

**Body.**

```markdown
LiveStream_054 ("Mathematical Foundations for a Compositional Account of the Bayesian Brain", Smithe) still holds 34 files in three stems: "…054.0…" → `HK9ZkbxieLY`, "ls054 1 …" → `fzFDvJhrn0U`, "054.2…" → `GfImcptiLsY`. Includes one `en(ie)` file (treat as `en`).

**Scope (from the triage doc, Part A):**
- Item `Livestream/LiveStream_054`
  - 11 files, stem `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe` → target `translations/HK9ZkbxieLY.<bcp47>.srt`
  - 11 files, stem `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe)` → target `translations/GfImcptiLsY.<bcp47>.srt`
  - 12 files, stem `ls054 1 Compositional Account of the Bayesian Brain Smithe` → target `translations/fzFDvJhrn0U.<bcp47>.srt`
```

