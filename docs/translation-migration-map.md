# Translation migration map (M2 — J2/Y15, part 1: non-destructive)

Generated: 2026-09-23, against worktree branch `feat/m2-translations` (HEAD `d88cb2ae`).

**This map only documents the planned moves. No files are moved in this change.** The
actual `git mv` (two-step rename `Translations/` → `translations_tmp/` → `translations/`,
with `previous_paths` recorded in each item's `metadata.json`, per-series PRs) is a
reviewable follow-up executed strictly from the approved rows of this map.

## Verified counts

| Metric | Value |
|---|---|
| Legacy `Translations/` folders | 131 |
| Legacy `Translations/` files | 2880 |
| Rows auto-movable in part 2 (verified, unique targets) | 1540 |
| Rows requiring review before any move | 1340 |
| Distinct targets for auto-movable rows | 1540 |

Handoff claim "~2,880 files / ~131 items" is **verified exactly: 2,880 files in 131 folders**.

## Method

Source: `git ls-tree -r HEAD --name-only` (`core.quotePath=false`), filtered to `/Translations/`.
Target naming: `translations/<video_id>.<bcp47>.srt` (lowercase directory, same item).
`video_id` verification — a filename is only auto-movable when one of these resolves it to
exactly one `parts[].video_id` of the item's `metadata.json`:

1. **episode token** — the stem's `#<n>.<m>` token appears in exactly one part title (1,120+ rows).
2. **title exact / prefix** — normalized stem equals (or prefixes) exactly one part title.
3. Legacy 3-letter language codes mapped per the handoff table; `(translated)` suffixes stripped.
4. `chi` resolves to `zh-Hant` when a `Trad` qualifier is present, `zh-Hans` when `Simp` is present
   or by default (default flagged in notes).

Notably, **no legacy filename embeds a real video id** (11-char-looking tokens in stems are
ordinary words), so id-level verification relies entirely on the metadata.json matching above.

### Language normalization table

| Legacy token(s) | Target | Rows |
|---|---|---|
| `fr` | `fr` | 199 |
| `de` | `de` | 198 |
| `es` | `es` | 198 |
| `it` | `it` | 198 |
| `nl` | `nl` | 195 |
| `pt` | `pt` | 195 |
| `ja` | `ja` | 187 |
| `ru` | `ru` | 185 |
| `ko` | `ko` | 182 |
| `zh-Hans` | `zh-Hans` | 180 |
| `zh-Hant` | `zh-Hant` | 179 |
| `chi(translated)` | `zh-Hans/Hant` | 138 |
| `ger(translated)` | `de` | 77 |
| `rus(translated)` | `ru` | 74 |
| `ita(translated)` | `it` | 73 |
| `por(translated)` | `pt` | 72 |
| `dut(translated)` | `nl` | 70 |
| `kor(translated)` | `ko` | 68 |
| `spa(translated)` | `es` | 68 |
| `fre(translated)` | `fr` | 67 |
| `jpn(translated)` | `ja` | 67 |
| `en(ie)` | `en` | 3 |
| `eng(transcribed)` | `en` | 2 |
| `010 ~  Governing Continuous Transformation_transcript` | `010 ~  Governing Continuous Transformation_transcript` | 1 |
| `08 ~  Governing Continuous Transformation_transcript` | `08 ~  Governing Continuous Transformation_transcript` | 1 |
| `en` | `en` | 1 |
| `che(translated)` | `che` | 1 |
| `es (1)` | `es` | 1 |

Special cases: `che(translated)` (1) — unknown code, not in the handoff mapping; `en(ie)` (3) —
unknown qualifier; `es (1)` (1) — apparent duplicate copy; 2 files have **no language suffix at
all** (ending `_transcript.srt`). All are quarantined as review rows.

## Needs-review buckets

- 917 — multiple files collapse to one target (conflict)
- 277 — no verified video_id / language
- 134 — stem unrelated to sole part title (unverified single-part)
- 12 — ambiguous episode/title match

Root causes observed: per-talk files from multi-session events (e.g. `3Symp1 01 Andre Bastos…`)
stored in a single-part interval item; duplicate copies (`(2)` suffixes); files from other events
(the 2021 Symposium folder holds 2022 Robotics files) — matching the handoff's misfiling notes.
**Conflicting rows are NOT moved in part 2** until each file is individually resolved.

## Per-item mapping

`target` = final path relative to the item directory. Empty target = no move until resolved.

### `data/video/activeinferenceinstitute/Applied Active Inference Symposium/2021 Symposium with Karl Friston`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).de.srt` | `de` | `translations/X2GwqUVLlcs.de.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).es.srt` | `es` | `translations/X2GwqUVLlcs.es.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).fr.srt` | `fr` | `translations/X2GwqUVLlcs.fr.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).it.srt` | `it` | `translations/X2GwqUVLlcs.it.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).ja.srt` | `ja` | `translations/X2GwqUVLlcs.ja.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).ko.srt` | `ko` | `translations/X2GwqUVLlcs.ko.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).nl.srt` | `nl` | `translations/X2GwqUVLlcs.nl.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).pt.srt` | `pt` | `translations/X2GwqUVLlcs.pt.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).ru.srt` | `ru` | `translations/X2GwqUVLlcs.ru.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).zh-Hans.srt` | `zh-Hans` | `translations/X2GwqUVLlcs.zh-Hans.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 2 (Communication).zh-Hant.srt` | `zh-Hant` | `translations/X2GwqUVLlcs.zh-Hant.srt` | yes (title exact) |  |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `3Symp1 01 Andre Bastos.de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 01 Andre Bastos.zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 02 Keith Duggar.zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 03 Sanjeev Namjoshi.zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 04 Inês Hipólito.zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 05 Aswin Paul.zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 06 Takuya Isomura.zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 07 Shanna Dobson.zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp1 08 Nynke Boiten.zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).ja.srt` | `ja` | `translations/rIemcswLfGg.ja.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).ko.srt` | `ko` | `translations/rIemcswLfGg.ko.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).zh-Hans.srt` | `zh-Hans` | `translations/rIemcswLfGg.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).zh-Hant.srt` | `zh-Hant` | `translations/rIemcswLfGg.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 12 files map to same target; CONFLICT: 12 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).de.srt` | `de` | `translations/rIemcswLfGg.de.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).es.srt` | `es` | `translations/rIemcswLfGg.es.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).fr.srt` | `fr` | `translations/rIemcswLfGg.fr.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).it.srt` | `it` | `translations/rIemcswLfGg.it.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).nl.srt` | `nl` | `translations/rIemcswLfGg.nl.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).pt.srt` | `pt` | `translations/rIemcswLfGg.pt.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).ru.srt` | `ru` | `translations/rIemcswLfGg.ru.srt` | **assumed (sole part)** | CONFLICT: 13 files map to same target; CONFLICT: 13 files map to same target; stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/Applied Active Inference Symposium/2023 Ecosystem Symposium/Second_Interval`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.de.srt` | `de` | `translations/PVeyvHSAwmk.de.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.es.srt` | `es` | `translations/PVeyvHSAwmk.es.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.fr.srt` | `fr` | `translations/PVeyvHSAwmk.fr.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.it.srt` | `it` | `translations/PVeyvHSAwmk.it.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.ja.srt` | `ja` | `translations/PVeyvHSAwmk.ja.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.ko.srt` | `ko` | `translations/PVeyvHSAwmk.ko.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.nl.srt` | `nl` | `translations/PVeyvHSAwmk.nl.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.pt.srt` | `pt` | `translations/PVeyvHSAwmk.pt.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.ru.srt` | `ru` | `translations/PVeyvHSAwmk.ru.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.zh-Hans.srt` | `zh-Hans` | `translations/PVeyvHSAwmk.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Sym2 09 - 2nd Interval, Session 9, Roundtable.zh-Hant.srt` | `zh-Hant` | `translations/PVeyvHSAwmk.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.de.srt` | `de` | `translations/PVeyvHSAwmk.de.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.es.srt` | `es` | `translations/PVeyvHSAwmk.es.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.fr.srt` | `fr` | `translations/PVeyvHSAwmk.fr.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.it.srt` | `it` | `translations/PVeyvHSAwmk.it.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.ja.srt` | `ja` | `translations/PVeyvHSAwmk.ja.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.ko.srt` | `ko` | `translations/PVeyvHSAwmk.ko.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.nl.srt` | `nl` | `translations/PVeyvHSAwmk.nl.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.pt.srt` | `pt` | `translations/PVeyvHSAwmk.pt.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.ru.srt` | `ru` | `translations/PVeyvHSAwmk.ru.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.zh-Hans.srt` | `zh-Hans` | `translations/PVeyvHSAwmk.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 02 Conor Heins.zh-Hant.srt` | `zh-Hant` | `translations/PVeyvHSAwmk.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.de.srt` | `de` | `translations/PVeyvHSAwmk.de.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.es.srt` | `es` | `translations/PVeyvHSAwmk.es.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.fr.srt` | `fr` | `translations/PVeyvHSAwmk.fr.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.it.srt` | `it` | `translations/PVeyvHSAwmk.it.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.ja.srt` | `ja` | `translations/PVeyvHSAwmk.ja.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.ko.srt` | `ko` | `translations/PVeyvHSAwmk.ko.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.nl.srt` | `nl` | `translations/PVeyvHSAwmk.nl.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.pt.srt` | `pt` | `translations/PVeyvHSAwmk.pt.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.ru.srt` | `ru` | `translations/PVeyvHSAwmk.ru.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.zh-Hans.srt` | `zh-Hans` | `translations/PVeyvHSAwmk.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 03.zh-Hant.srt` | `zh-Hant` | `translations/PVeyvHSAwmk.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.de.srt` | `de` | `translations/PVeyvHSAwmk.de.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.es.srt` | `es` | `translations/PVeyvHSAwmk.es.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.fr.srt` | `fr` | `translations/PVeyvHSAwmk.fr.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.it.srt` | `it` | `translations/PVeyvHSAwmk.it.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.ja.srt` | `ja` | `translations/PVeyvHSAwmk.ja.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.ko.srt` | `ko` | `translations/PVeyvHSAwmk.ko.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.nl.srt` | `nl` | `translations/PVeyvHSAwmk.nl.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.pt.srt` | `pt` | `translations/PVeyvHSAwmk.pt.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.ru.srt` | `ru` | `translations/PVeyvHSAwmk.ru.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.zh-Hans.srt` | `zh-Hans` | `translations/PVeyvHSAwmk.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 04 In the Active Inference Ecosystem.zh-Hant.srt` | `zh-Hant` | `translations/PVeyvHSAwmk.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.de.srt` | `de` | `translations/PVeyvHSAwmk.de.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.es.srt` | `es` | `translations/PVeyvHSAwmk.es.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.fr.srt` | `fr` | `translations/PVeyvHSAwmk.fr.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.it.srt` | `it` | `translations/PVeyvHSAwmk.it.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.ja.srt` | `ja` | `translations/PVeyvHSAwmk.ja.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.ko.srt` | `ko` | `translations/PVeyvHSAwmk.ko.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.nl.srt` | `nl` | `translations/PVeyvHSAwmk.nl.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.pt.srt` | `pt` | `translations/PVeyvHSAwmk.pt.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.ru.srt` | `ru` | `translations/PVeyvHSAwmk.ru.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.zh-Hans.srt` | `zh-Hans` | `translations/PVeyvHSAwmk.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 05 Rafael Kaufmann.zh-Hant.srt` | `zh-Hant` | `translations/PVeyvHSAwmk.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.de.srt` | `de` | `translations/PVeyvHSAwmk.de.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.es.srt` | `es` | `translations/PVeyvHSAwmk.es.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.fr.srt` | `fr` | `translations/PVeyvHSAwmk.fr.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.it.srt` | `it` | `translations/PVeyvHSAwmk.it.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.ja.srt` | `ja` | `translations/PVeyvHSAwmk.ja.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.ko.srt` | `ko` | `translations/PVeyvHSAwmk.ko.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.nl.srt` | `nl` | `translations/PVeyvHSAwmk.nl.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.pt.srt` | `pt` | `translations/PVeyvHSAwmk.pt.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.ru.srt` | `ru` | `translations/PVeyvHSAwmk.ru.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.zh-Hans.srt` | `zh-Hans` | `translations/PVeyvHSAwmk.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 06 Avel Guénin-Carlut.zh-Hant.srt` | `zh-Hant` | `translations/PVeyvHSAwmk.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 07 Pablo Fernandez-Maquieira.de.srt` | `de` | `translations/PVeyvHSAwmk.de.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 07 Pablo Fernandez-Maquieira.es.srt` | `es` | `translations/PVeyvHSAwmk.es.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 07 Pablo Fernandez-Maquieira.fr.srt` | `fr` | `translations/PVeyvHSAwmk.fr.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 07 Pablo Fernandez-Maquieira.it.srt` | `it` | `translations/PVeyvHSAwmk.it.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 07 Pablo Fernandez-Maquieira.ja.srt` | `ja` | `translations/PVeyvHSAwmk.ja.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 07 Pablo Fernandez-Maquieira.ko.srt` | `ko` | `translations/PVeyvHSAwmk.ko.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.de.srt` | `de` | `translations/PVeyvHSAwmk.de.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.es.srt` | `es` | `translations/PVeyvHSAwmk.es.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.fr.srt` | `fr` | `translations/PVeyvHSAwmk.fr.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.it.srt` | `it` | `translations/PVeyvHSAwmk.it.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.ja.srt` | `ja` | `translations/PVeyvHSAwmk.ja.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.ko.srt` | `ko` | `translations/PVeyvHSAwmk.ko.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.nl.srt` | `nl` | `translations/PVeyvHSAwmk.nl.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.pt.srt` | `pt` | `translations/PVeyvHSAwmk.pt.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.ru.srt` | `ru` | `translations/PVeyvHSAwmk.ru.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.zh-Hans.srt` | `zh-Hans` | `translations/PVeyvHSAwmk.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp2 08.zh-Hant.srt` | `zh-Hant` | `translations/PVeyvHSAwmk.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.de.srt` | `de` | `translations/PVeyvHSAwmk.de.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.es.srt` | `es` | `translations/PVeyvHSAwmk.es.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.fr.srt` | `fr` | `translations/PVeyvHSAwmk.fr.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.it.srt` | `it` | `translations/PVeyvHSAwmk.it.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.ja.srt` | `ja` | `translations/PVeyvHSAwmk.ja.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.ko.srt` | `ko` | `translations/PVeyvHSAwmk.ko.srt` | **assumed (sole part)** | CONFLICT: 9 files map to same target; CONFLICT: 9 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.nl.srt` | `nl` | `translations/PVeyvHSAwmk.nl.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.pt.srt` | `pt` | `translations/PVeyvHSAwmk.pt.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.ru.srt` | `ru` | `translations/PVeyvHSAwmk.ru.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.zh-Hans.srt` | `zh-Hans` | `translations/PVeyvHSAwmk.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |
| `3Symp_2_01 Interval 2 Session 01 Jean-François Cloutier.zh-Hant.srt` | `zh-Hant` | `translations/PVeyvHSAwmk.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 8 files map to same target; CONFLICT: 8 files map to same target; stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/BookStream/BookStream_001`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/eIZjx0miM9o.de.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/eIZjx0miM9o.es.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/eIZjx0miM9o.fr.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/eIZjx0miM9o.it.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/eIZjx0miM9o.ja.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/eIZjx0miM9o.ko.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/eIZjx0miM9o.nl.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/eIZjx0miM9o.pt.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/eIZjx0miM9o.ru.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/eIZjx0miM9o.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.010 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/eIZjx0miM9o.zh-Hant.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/rCmq0TVGpW0.de.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/rCmq0TVGpW0.es.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/rCmq0TVGpW0.fr.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/rCmq0TVGpW0.it.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/rCmq0TVGpW0.ja.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/rCmq0TVGpW0.ko.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/rCmq0TVGpW0.nl.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/rCmq0TVGpW0.pt.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/rCmq0TVGpW0.ru.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/rCmq0TVGpW0.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.03 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/rCmq0TVGpW0.zh-Hant.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/0_yvUA0lsdI.de.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/0_yvUA0lsdI.es.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/0_yvUA0lsdI.fr.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/0_yvUA0lsdI.it.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/0_yvUA0lsdI.ja.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/0_yvUA0lsdI.ko.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/0_yvUA0lsdI.nl.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/0_yvUA0lsdI.pt.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/0_yvUA0lsdI.ru.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/0_yvUA0lsdI.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.07 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/0_yvUA0lsdI.zh-Hant.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/yNZg5b63hb8.de.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/yNZg5b63hb8.es.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/yNZg5b63hb8.fr.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/yNZg5b63hb8.it.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/yNZg5b63hb8.ja.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/yNZg5b63hb8.ko.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/yNZg5b63hb8.nl.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/yNZg5b63hb8.pt.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/yNZg5b63hb8.ru.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/yNZg5b63hb8.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.08 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/yNZg5b63hb8.zh-Hant.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/3oFfxaKBBXY.de.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/3oFfxaKBBXY.es.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/3oFfxaKBBXY.fr.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/3oFfxaKBBXY.it.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/3oFfxaKBBXY.ja.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/3oFfxaKBBXY.ko.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/3oFfxaKBBXY.nl.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/3oFfxaKBBXY.pt.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/3oFfxaKBBXY.ru.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/3oFfxaKBBXY.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.09 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/3oFfxaKBBXY.zh-Hant.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/DQhPABvJBFk.de.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/DQhPABvJBFk.es.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/DQhPABvJBFk.fr.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/DQhPABvJBFk.it.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/DQhPABvJBFk.ja.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/DQhPABvJBFk.ko.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/DQhPABvJBFk.nl.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/DQhPABvJBFk.pt.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/DQhPABvJBFk.ru.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/DQhPABvJBFk.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference BookStream #001.2 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/DQhPABvJBFk.zh-Hant.srt` | yes (episode token) |  |
| `Active Inference BookStream 001.010 ~  Governing Continuous Transformation_transcript.srt` | `010 ~  Governing Continuous Transformation_transcript` | — | **NO (unmatched)** | no language suffix — manual review; no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.08 ~  Governing Continuous Transformation_transcript.srt` | `08 ~  Governing Continuous Transformation_transcript` | — | **NO (unmatched)** | no language suffix — manual review; no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/BookStream/BookStream_002`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.de.srt` | `de` | `translations/xlrZ00NQNHo.de.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.es.srt` | `es` | `translations/xlrZ00NQNHo.es.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.fr.srt` | `fr` | `translations/xlrZ00NQNHo.fr.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.it.srt` | `it` | `translations/xlrZ00NQNHo.it.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.ja.srt` | `ja` | `translations/xlrZ00NQNHo.ja.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.ko.srt` | `ko` | `translations/xlrZ00NQNHo.ko.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.nl.srt` | `nl` | `translations/xlrZ00NQNHo.nl.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.pt.srt` | `pt` | `translations/xlrZ00NQNHo.pt.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.ru.srt` | `ru` | `translations/xlrZ00NQNHo.ru.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.zh-Hans.srt` | `zh-Hans` | `translations/xlrZ00NQNHo.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference BookStream #002.1 ~ Thomas Parr ~ Active Inference and Free Energy Principle.zh-Hant.srt` | `zh-Hant` | `translations/xlrZ00NQNHo.zh-Hant.srt` | yes (episode token) |  |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/ActInf_Basics_Discussion`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.de.srt` | `de` | `translations/u6taX0npOY8.de.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.es.srt` | `es` | `translations/u6taX0npOY8.es.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.fr.srt` | `fr` | `translations/u6taX0npOY8.fr.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.it.srt` | `it` | `translations/u6taX0npOY8.it.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.ja.srt` | `ja` | `translations/u6taX0npOY8.ja.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.ko.srt` | `ko` | `translations/u6taX0npOY8.ko.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.nl.srt` | `nl` | `translations/u6taX0npOY8.nl.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.pt.srt` | `pt` | `translations/u6taX0npOY8.pt.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.ru.srt` | `ru` | `translations/u6taX0npOY8.ru.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.zh-Hans.srt` | `zh-Hans` | `translations/u6taX0npOY8.zh-Hans.srt` | yes (title exact) |  |
| `Basics of Active Inference (Discussion) ~ Ben White ~ Active Inference for the Social Sciences 2023.zh-Hant.srt` | `zh-Hant` | `translations/u6taX0npOY8.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/ActInf_Basics_Lecture`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.de.srt` | `de` | `translations/BNLnbOFdgc0.de.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.es.srt` | `es` | `translations/BNLnbOFdgc0.es.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.fr.srt` | `fr` | `translations/BNLnbOFdgc0.fr.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.it.srt` | `it` | `translations/BNLnbOFdgc0.it.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.ja.srt` | `ja` | `translations/BNLnbOFdgc0.ja.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.ko.srt` | `ko` | `translations/BNLnbOFdgc0.ko.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.nl.srt` | `nl` | `translations/BNLnbOFdgc0.nl.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.pt.srt` | `pt` | `translations/BNLnbOFdgc0.pt.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.ru.srt` | `ru` | `translations/BNLnbOFdgc0.ru.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.zh-Hans.srt` | `zh-Hans` | `translations/BNLnbOFdgc0.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.zh-Hant.srt` | `zh-Hant` | `translations/BNLnbOFdgc0.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.de.srt` | `de` | `translations/BNLnbOFdgc0.de.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.es.srt` | `es` | `translations/BNLnbOFdgc0.es.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.fr.srt` | `fr` | `translations/BNLnbOFdgc0.fr.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.it.srt` | `it` | `translations/BNLnbOFdgc0.it.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.ja.srt` | `ja` | `translations/BNLnbOFdgc0.ja.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.ko.srt` | `ko` | `translations/BNLnbOFdgc0.ko.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.nl.srt` | `nl` | `translations/BNLnbOFdgc0.nl.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.pt.srt` | `pt` | `translations/BNLnbOFdgc0.pt.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.ru.srt` | `ru` | `translations/BNLnbOFdgc0.ru.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.zh-Hans.srt` | `zh-Hans` | `translations/BNLnbOFdgc0.zh-Hans.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics of Active Inference (Lecture) ~ Ben White ~ Active Inference for the Social Sciences 2023.zh-Hant.srt` | `zh-Hant` | `translations/BNLnbOFdgc0.zh-Hant.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/CollectiveBehavior_Discussion`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.de.srt` | `de` | `translations/2IxxzY2ZDHA.de.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.es.srt` | `es` | `translations/2IxxzY2ZDHA.es.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.fr.srt` | `fr` | `translations/2IxxzY2ZDHA.fr.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.it.srt` | `it` | `translations/2IxxzY2ZDHA.it.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ja.srt` | `ja` | `translations/2IxxzY2ZDHA.ja.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ko.srt` | `ko` | `translations/2IxxzY2ZDHA.ko.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.de.srt` | `de` | `translations/2IxxzY2ZDHA.de.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.es.srt` | `es` | `translations/2IxxzY2ZDHA.es.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.fr.srt` | `fr` | `translations/2IxxzY2ZDHA.fr.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.it.srt` | `it` | `translations/2IxxzY2ZDHA.it.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.pt.srt` | `pt` | `translations/2IxxzY2ZDHA.pt.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.nl.srt` | `nl` | `translations/2IxxzY2ZDHA.nl.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.pt.srt` | `pt` | `translations/2IxxzY2ZDHA.pt.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ru.srt` | `ru` | `translations/2IxxzY2ZDHA.ru.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hans.srt` | `zh-Hans` | `translations/2IxxzY2ZDHA.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hant.srt` | `zh-Hant` | `translations/2IxxzY2ZDHA.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.de.srt` | `de` | `translations/2IxxzY2ZDHA.de.srt` | **yes (title exact)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.es.srt` | `es` | `translations/2IxxzY2ZDHA.es.srt` | **yes (title exact)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.fr.srt` | `fr` | `translations/2IxxzY2ZDHA.fr.srt` | **yes (title exact)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.it.srt` | `it` | `translations/2IxxzY2ZDHA.it.srt` | **yes (title exact)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ja.srt` | `ja` | `translations/2IxxzY2ZDHA.ja.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ko.srt` | `ko` | `translations/2IxxzY2ZDHA.ko.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.nl.srt` | `nl` | `translations/2IxxzY2ZDHA.nl.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.pt.srt` | `pt` | `translations/2IxxzY2ZDHA.pt.srt` | **yes (title exact)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ru.srt` | `ru` | `translations/2IxxzY2ZDHA.ru.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hans.srt` | `zh-Hans` | `translations/2IxxzY2ZDHA.zh-Hans.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Collective Behavior (Discussion) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hant.srt` | `zh-Hant` | `translations/2IxxzY2ZDHA.zh-Hant.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/CollectiveBehavior_Lecture`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.de.srt` | `de` | `translations/ran1M2UmD80.de.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.es.srt` | `es` | `translations/ran1M2UmD80.es.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.fr.srt` | `fr` | `translations/ran1M2UmD80.fr.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.it.srt` | `it` | `translations/ran1M2UmD80.it.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ja.srt` | `ja` | `translations/ran1M2UmD80.ja.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ko.srt` | `ko` | `translations/ran1M2UmD80.ko.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.nl.srt` | `nl` | `translations/ran1M2UmD80.nl.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.pt.srt` | `pt` | `translations/ran1M2UmD80.pt.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ru.srt` | `ru` | `translations/ran1M2UmD80.ru.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hans.srt` | `zh-Hans` | `translations/ran1M2UmD80.zh-Hans.srt` | yes (title exact) |  |
| `Collective Behavior (Lecture) ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hant.srt` | `zh-Hant` | `translations/ran1M2UmD80.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/NormsScripts_Lecture`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.de.srt` | `de` | `translations/Qbmuu61dnWY.de.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.es.srt` | `es` | `translations/Qbmuu61dnWY.es.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.fr.srt` | `fr` | `translations/Qbmuu61dnWY.fr.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.it.srt` | `it` | `translations/Qbmuu61dnWY.it.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.ja.srt` | `ja` | `translations/Qbmuu61dnWY.ja.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.ko.srt` | `ko` | `translations/Qbmuu61dnWY.ko.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.nl.srt` | `nl` | `translations/Qbmuu61dnWY.nl.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.pt.srt` | `pt` | `translations/Qbmuu61dnWY.pt.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.ru.srt` | `ru` | `translations/Qbmuu61dnWY.ru.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.zh-Hans.srt` | `zh-Hans` | `translations/Qbmuu61dnWY.zh-Hans.srt` | yes (title exact) |  |
| `Norms, Scripts, Narratives, Languages Lecture ~ Mahault Albarracin ~ ActInf Social Sciences 2023.zh-Hant.srt` | `zh-Hant` | `translations/Qbmuu61dnWY.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Discussion`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.de.srt` | `de` | `translations/MrAiB9X7Ock.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.es.srt` | `es` | `translations/MrAiB9X7Ock.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.fr.srt` | `fr` | `translations/MrAiB9X7Ock.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.it.srt` | `it` | `translations/MrAiB9X7Ock.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.ja.srt` | `ja` | `translations/MrAiB9X7Ock.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.ko.srt` | `ko` | `translations/MrAiB9X7Ock.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.nl.srt` | `nl` | `translations/MrAiB9X7Ock.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.pt.srt` | `pt` | `translations/MrAiB9X7Ock.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.ru.srt` | `ru` | `translations/MrAiB9X7Ock.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.zh-Hans.srt` | `zh-Hans` | `translations/MrAiB9X7Ock.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.zh-Hant.srt` | `zh-Hant` | `translations/MrAiB9X7Ock.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Lecture`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.de.srt` | `de` | `translations/4ijYLWm4P2I.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.es.srt` | `es` | `translations/4ijYLWm4P2I.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.fr.srt` | `fr` | `translations/4ijYLWm4P2I.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.it.srt` | `it` | `translations/4ijYLWm4P2I.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.ja.srt` | `ja` | `translations/4ijYLWm4P2I.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.ko.srt` | `ko` | `translations/4ijYLWm4P2I.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.nl.srt` | `nl` | `translations/4ijYLWm4P2I.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.pt.srt` | `pt` | `translations/4ijYLWm4P2I.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.ru.srt` | `ru` | `translations/4ijYLWm4P2I.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.zh-Hans.srt` | `zh-Hans` | `translations/4ijYLWm4P2I.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.zh-Hant.srt` | `zh-Hant` | `translations/4ijYLWm4P2I.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_010`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.chi(translated-Simp).chi(translated).srt` | `zh-Hans` | `translations/Hvr-RgWZ7p4.zh-Hans.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.chi(translated-Trad) (2).chi(translated).srt` | `zh-Hant` | `translations/Hvr-RgWZ7p4.zh-Hant.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.dut(translated).dut(translated).srt` | `nl` | `translations/Hvr-RgWZ7p4.nl.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.fre(translated).fre(translated).srt` | `fr` | `translations/Hvr-RgWZ7p4.fr.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.ger(translated).ger(translated).srt` | `de` | `translations/Hvr-RgWZ7p4.de.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.ita(translated).ita(translated).srt` | `it` | `translations/Hvr-RgWZ7p4.it.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.jpn(translated).jpn(translated).srt` | `ja` | `translations/Hvr-RgWZ7p4.ja.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.kor(translated).kor(translated).srt` | `ko` | `translations/Hvr-RgWZ7p4.ko.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.por(translated).por(translated).srt` | `pt` | `translations/Hvr-RgWZ7p4.pt.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.rus(translated).rus(translated).srt` | `ru` | `translations/Hvr-RgWZ7p4.ru.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #010.1 ~ Philip Gerrans.spa(translated).spa(translated).srt` | `es` | `translations/Hvr-RgWZ7p4.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_013`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab GuestStream #013.1 ~ Adam Safron.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/eVbWeWEX9dA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/eVbWeWEX9dA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.dut(translated).dut(translated).srt` | `nl` | `translations/eVbWeWEX9dA.nl.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.fre(translated).fre(translated).srt` | `fr` | `translations/eVbWeWEX9dA.fr.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.ger(translated).ger(translated).srt` | `de` | `translations/eVbWeWEX9dA.de.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.ita(translated).ita(translated).srt` | `it` | `translations/eVbWeWEX9dA.it.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.jpn(translated).jpn(translated).srt` | `ja` | `translations/eVbWeWEX9dA.ja.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.kor(translated).kor(translated).srt` | `ko` | `translations/eVbWeWEX9dA.ko.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.por(translated).por(translated).srt` | `pt` | `translations/eVbWeWEX9dA.pt.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.rus(translated).rus(translated).srt` | `ru` | `translations/eVbWeWEX9dA.ru.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #013.1 ~ Adam Safron.spa(translated).spa(translated).srt` | `es` | `translations/eVbWeWEX9dA.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_015`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.de.srt` | `de` | `translations/_JCaic5Cxms.de.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.es.srt` | `es` | `translations/_JCaic5Cxms.es.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.fr.srt` | `fr` | `translations/_JCaic5Cxms.fr.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.it.srt` | `it` | `translations/_JCaic5Cxms.it.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.ja.srt` | `ja` | `translations/_JCaic5Cxms.ja.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.ko.srt` | `ko` | `translations/_JCaic5Cxms.ko.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.nl.srt` | `nl` | `translations/_JCaic5Cxms.nl.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.pt.srt` | `pt` | `translations/_JCaic5Cxms.pt.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.ru.srt` | `ru` | `translations/_JCaic5Cxms.ru.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.zh-Hans.srt` | `zh-Hans` | `translations/_JCaic5Cxms.zh-Hans.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.1 Bobby Azarian, Universal Bayesianism A New Kind of Theory of Everything.zh-Hant.srt` | `zh-Hant` | `translations/_JCaic5Cxms.zh-Hant.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.de.srt` | `de` | `translations/WEfc9X437yY.de.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.es.srt` | `es` | `translations/WEfc9X437yY.es.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.fr.srt` | `fr` | `translations/WEfc9X437yY.fr.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.it.srt` | `it` | `translations/WEfc9X437yY.it.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.ja.srt` | `ja` | `translations/WEfc9X437yY.ja.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.ko.srt` | `ko` | `translations/WEfc9X437yY.ko.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.nl.srt` | `nl` | `translations/WEfc9X437yY.nl.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.pt.srt` | `pt` | `translations/WEfc9X437yY.pt.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.ru.srt` | `ru` | `translations/WEfc9X437yY.ru.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.zh-Hans.srt` | `zh-Hans` | `translations/WEfc9X437yY.zh-Hans.srt` | yes (episode token) |  |
| `ActInf GuestStream #015.2 ~ Bobby Azarian  The Integrated Evolutionary Synthesis.zh-Hant.srt` | `zh-Hant` | `translations/WEfc9X437yY.zh-Hant.srt` | yes (episode token) |  |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.en(ie).srt` | `en` | — | **NO (unmatched)** | en qualifier in "en(ie)"; no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_016`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_024`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.de.srt` | `de` | `translations/tOFA7FODn8w.de.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.es.srt` | `es` | `translations/tOFA7FODn8w.es.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.fr.srt` | `fr` | `translations/tOFA7FODn8w.fr.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.it.srt` | `it` | `translations/tOFA7FODn8w.it.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.ja.srt` | `ja` | `translations/tOFA7FODn8w.ja.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.ko.srt` | `ko` | `translations/tOFA7FODn8w.ko.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.nl.srt` | `nl` | `translations/tOFA7FODn8w.nl.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.pt.srt` | `pt` | `translations/tOFA7FODn8w.pt.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.ru.srt` | `ru` | `translations/tOFA7FODn8w.ru.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.zh-Hans.srt` | `zh-Hans` | `translations/tOFA7FODn8w.zh-Hans.srt` | yes (episode token) |  |
| `ActInfLab GuestStream #024.1 ~ Stephen Grossberg,  Explainable and Reliable AI.zh-Hant.srt` | `zh-Hant` | `translations/tOFA7FODn8w.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_025`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.de.srt` | `de` | `translations/ZYhrtsyzS_w.de.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.es.srt` | `es` | `translations/ZYhrtsyzS_w.es.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.fr.srt` | `fr` | `translations/ZYhrtsyzS_w.fr.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.it.srt` | `it` | `translations/ZYhrtsyzS_w.it.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.ja.srt` | `ja` | `translations/ZYhrtsyzS_w.ja.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.ko.srt` | `ko` | `translations/ZYhrtsyzS_w.ko.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.nl.srt` | `nl` | `translations/ZYhrtsyzS_w.nl.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.pt.srt` | `pt` | `translations/ZYhrtsyzS_w.pt.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.ru.srt` | `ru` | `translations/ZYhrtsyzS_w.ru.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.zh-Hans.srt` | `zh-Hans` | `translations/ZYhrtsyzS_w.zh-Hans.srt` | yes (episode token) |  |
| `ActInf GuestStream #025.1 ~  Autistic-Like Traits, Positive Schizotypy, Predictive Mind.zh-Hant.srt` | `zh-Hant` | `translations/ZYhrtsyzS_w.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_027`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference GuestStream #027.1 ~ John Vervaeke.de.srt` | `de` | `translations/Pw2vxMRxF5o.de.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.en.srt` | `en` | `translations/Pw2vxMRxF5o.en.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.es.srt` | `es` | `translations/Pw2vxMRxF5o.es.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.fr.srt` | `fr` | `translations/Pw2vxMRxF5o.fr.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.it.srt` | `it` | `translations/Pw2vxMRxF5o.it.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.ja.srt` | `ja` | `translations/Pw2vxMRxF5o.ja.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.ko.srt` | `ko` | `translations/Pw2vxMRxF5o.ko.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.nl.srt` | `nl` | `translations/Pw2vxMRxF5o.nl.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.pt.srt` | `pt` | `translations/Pw2vxMRxF5o.pt.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.ru.srt` | `ru` | `translations/Pw2vxMRxF5o.ru.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.zh-Hans.srt` | `zh-Hans` | `translations/Pw2vxMRxF5o.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference GuestStream #027.1 ~ John Vervaeke.zh-Hant.srt` | `zh-Hant` | `translations/Pw2vxMRxF5o.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_028`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.de.srt` | `de` | `translations/KqiLO9Dfj-4.de.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.es.srt` | `es` | `translations/KqiLO9Dfj-4.es.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.fr.srt` | `fr` | `translations/KqiLO9Dfj-4.fr.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.it.srt` | `it` | `translations/KqiLO9Dfj-4.it.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.ja.srt` | `ja` | `translations/KqiLO9Dfj-4.ja.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.ko.srt` | `ko` | `translations/KqiLO9Dfj-4.ko.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.nl.srt` | `nl` | `translations/KqiLO9Dfj-4.nl.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.pt.srt` | `pt` | `translations/KqiLO9Dfj-4.pt.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.ru.srt` | `ru` | `translations/KqiLO9Dfj-4.ru.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.zh-Hans.srt` | `zh-Hans` | `translations/KqiLO9Dfj-4.zh-Hans.srt` | yes (episode token) |  |
| `ActInf GuestStream #028.1 ~ Reconceiving rationality situating rationality into enactive cognition.zh-Hant.srt` | `zh-Hant` | `translations/KqiLO9Dfj-4.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_029`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.de.srt` | `de` | `translations/UuXAjY9Wgdg.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.es.srt` | `es` | `translations/UuXAjY9Wgdg.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.fr.srt` | `fr` | `translations/UuXAjY9Wgdg.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.it.srt` | `it` | `translations/UuXAjY9Wgdg.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.ja.srt` | `ja` | `translations/UuXAjY9Wgdg.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.ko.srt` | `ko` | `translations/UuXAjY9Wgdg.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.nl.srt` | `nl` | `translations/UuXAjY9Wgdg.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.pt.srt` | `pt` | `translations/UuXAjY9Wgdg.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.ru.srt` | `ru` | `translations/UuXAjY9Wgdg.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.zh-Hans.srt` | `zh-Hans` | `translations/UuXAjY9Wgdg.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.zh-Hant.srt` | `zh-Hant` | `translations/UuXAjY9Wgdg.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_030`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.de.srt` | `de` | `translations/QUBmgn7K_4E.de.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.es.srt` | `es` | `translations/QUBmgn7K_4E.es.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.fr.srt` | `fr` | `translations/QUBmgn7K_4E.fr.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.it.srt` | `it` | `translations/QUBmgn7K_4E.it.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.ja.srt` | `ja` | `translations/QUBmgn7K_4E.ja.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.ko.srt` | `ko` | `translations/QUBmgn7K_4E.ko.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.nl.srt` | `nl` | `translations/QUBmgn7K_4E.nl.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.pt.srt` | `pt` | `translations/QUBmgn7K_4E.pt.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.ru.srt` | `ru` | `translations/QUBmgn7K_4E.ru.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.zh-Hans.srt` | `zh-Hans` | `translations/QUBmgn7K_4E.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference GuestStream #030.1 ~ Kyrtin Atreides ~  The Human Governance Problem.zh-Hant.srt` | `zh-Hant` | `translations/QUBmgn7K_4E.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_031`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.de.srt` | `de` | `translations/57-aRIjUrC4.de.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.es.srt` | `es` | `translations/57-aRIjUrC4.es.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.fr.srt` | `fr` | `translations/57-aRIjUrC4.fr.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.it.srt` | `it` | `translations/57-aRIjUrC4.it.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.ja.srt` | `ja` | `translations/57-aRIjUrC4.ja.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.ko.srt` | `ko` | `translations/57-aRIjUrC4.ko.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.nl.srt` | `nl` | `translations/57-aRIjUrC4.nl.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.pt.srt` | `pt` | `translations/57-aRIjUrC4.pt.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.ru.srt` | `ru` | `translations/57-aRIjUrC4.ru.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.zh-Hans.srt` | `zh-Hans` | `translations/57-aRIjUrC4.zh-Hans.srt` | yes (episode token) |  |
| `ActInf GuestStream #031.1 ~ Brett Kagan & Adeel Razi.zh-Hant.srt` | `zh-Hant` | `translations/57-aRIjUrC4.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_032`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).de.srt` | `de` | `translations/0pMxBM3ahwQ.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).es.srt` | `es` | `translations/0pMxBM3ahwQ.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).fr.srt` | `fr` | `translations/0pMxBM3ahwQ.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).it.srt` | `it` | `translations/0pMxBM3ahwQ.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).ja.srt` | `ja` | `translations/0pMxBM3ahwQ.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).ko.srt` | `ko` | `translations/0pMxBM3ahwQ.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).nl.srt` | `nl` | `translations/0pMxBM3ahwQ.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).pt.srt` | `pt` | `translations/0pMxBM3ahwQ.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).ru.srt` | `ru` | `translations/0pMxBM3ahwQ.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).zh-Hans.srt` | `zh-Hans` | `translations/0pMxBM3ahwQ.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).zh-Hant.srt` | `zh-Hant` | `translations/0pMxBM3ahwQ.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_035`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.de.srt` | `de` | `translations/tbHZC6D39C4.de.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.es.srt` | `es` | `translations/tbHZC6D39C4.es.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.fr.srt` | `fr` | `translations/tbHZC6D39C4.fr.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.it.srt` | `it` | `translations/tbHZC6D39C4.it.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.ja.srt` | `ja` | `translations/tbHZC6D39C4.ja.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.ko.srt` | `ko` | `translations/tbHZC6D39C4.ko.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.nl.srt` | `nl` | `translations/tbHZC6D39C4.nl.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.pt.srt` | `pt` | `translations/tbHZC6D39C4.pt.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.ru.srt` | `ru` | `translations/tbHZC6D39C4.ru.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.zh-Hans.srt` | `zh-Hans` | `translations/tbHZC6D39C4.zh-Hans.srt` | yes (episode token) |  |
| `ActInf GuestStream #035.1 ~ Jordan Hall & Matthew Pirkowski.zh-Hant.srt` | `zh-Hant` | `translations/tbHZC6D39C4.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_038`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).de.srt` | `de` | `translations/mrFZwfYuthk.de.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).es.srt` | `es` | `translations/mrFZwfYuthk.es.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).fr.srt` | `fr` | `translations/mrFZwfYuthk.fr.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).it.srt` | `it` | `translations/mrFZwfYuthk.it.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).ja.srt` | `ja` | `translations/mrFZwfYuthk.ja.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).ko.srt` | `ko` | `translations/mrFZwfYuthk.ko.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).nl.srt` | `nl` | `translations/mrFZwfYuthk.nl.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).pt.srt` | `pt` | `translations/mrFZwfYuthk.pt.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).ru.srt` | `ru` | `translations/mrFZwfYuthk.ru.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).zh-Hans.srt` | `zh-Hans` | `translations/mrFZwfYuthk.zh-Hans.srt` | yes (title prefix) |  |
| `ActInf GuestStream 038.1 ~ Max Berg ~ Oversampled and undersolved (audio only).zh-Hant.srt` | `zh-Hant` | `translations/mrFZwfYuthk.zh-Hant.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_040`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.de.srt` | `de` | `translations/eZDSNPFS0Fs.de.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.es.srt` | `es` | `translations/eZDSNPFS0Fs.es.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.fr.srt` | `fr` | `translations/eZDSNPFS0Fs.fr.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.it.srt` | `it` | `translations/eZDSNPFS0Fs.it.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.ja.srt` | `ja` | `translations/eZDSNPFS0Fs.ja.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.ko.srt` | `ko` | `translations/eZDSNPFS0Fs.ko.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.nl.srt` | `nl` | `translations/eZDSNPFS0Fs.nl.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.pt.srt` | `pt` | `translations/eZDSNPFS0Fs.pt.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.ru.srt` | `ru` | `translations/eZDSNPFS0Fs.ru.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.zh-Hans.srt` | `zh-Hans` | `translations/eZDSNPFS0Fs.zh-Hans.srt` | yes (episode token) |  |
| `ActInf GuestStream #040.1 ~ Wanja Wiese ~ Could large language models be conscious.zh-Hant.srt` | `zh-Hant` | `translations/eZDSNPFS0Fs.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_041`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.de.srt` | `de` | `translations/EEyVd9d3D5U.de.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.es.srt` | `es` | `translations/EEyVd9d3D5U.es.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.fr.srt` | `fr` | `translations/EEyVd9d3D5U.fr.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.it.srt` | `it` | `translations/EEyVd9d3D5U.it.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.ja.srt` | `ja` | `translations/EEyVd9d3D5U.ja.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.ko.srt` | `ko` | `translations/EEyVd9d3D5U.ko.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.nl.srt` | `nl` | `translations/EEyVd9d3D5U.nl.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.pt.srt` | `pt` | `translations/EEyVd9d3D5U.pt.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.ru.srt` | `ru` | `translations/EEyVd9d3D5U.ru.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.zh-Hans.srt` | `zh-Hans` | `translations/EEyVd9d3D5U.zh-Hans.srt` | yes (title exact) |  |
| `ActInf GuestStream #041.1 ~ A conversation on Chomsky & Large Language Models ~ Murphy & Piantadosi.zh-Hant.srt` | `zh-Hant` | `translations/EEyVd9d3D5U.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_044`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.de.srt` | `de` | `translations/FymR0rKdLZo.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.es.srt` | `es` | `translations/FymR0rKdLZo.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.fr.srt` | `fr` | `translations/FymR0rKdLZo.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.it.srt` | `it` | `translations/FymR0rKdLZo.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.ja.srt` | `ja` | `translations/FymR0rKdLZo.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.ko.srt` | `ko` | `translations/FymR0rKdLZo.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.nl.srt` | `nl` | `translations/FymR0rKdLZo.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.pt.srt` | `pt` | `translations/FymR0rKdLZo.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.ru.srt` | `ru` | `translations/FymR0rKdLZo.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.zh-Hans.srt` | `zh-Hans` | `translations/FymR0rKdLZo.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.zh-Hant.srt` | `zh-Hant` | `translations/FymR0rKdLZo.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_045`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.de.srt` | `de` | `translations/y0Jyj6LAb8g.de.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.es.srt` | `es` | `translations/y0Jyj6LAb8g.es.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.fr.srt` | `fr` | `translations/y0Jyj6LAb8g.fr.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.it.srt` | `it` | `translations/y0Jyj6LAb8g.it.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.ja.srt` | `ja` | `translations/y0Jyj6LAb8g.ja.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.ko.srt` | `ko` | `translations/y0Jyj6LAb8g.ko.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.nl.srt` | `nl` | `translations/y0Jyj6LAb8g.nl.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.pt.srt` | `pt` | `translations/y0Jyj6LAb8g.pt.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.ru.srt` | `ru` | `translations/y0Jyj6LAb8g.ru.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.zh-Hans.srt` | `zh-Hans` | `translations/y0Jyj6LAb8g.zh-Hans.srt` | yes (title prefix) |  |
| `ActInf GuestStream 045.1, Ramstead & Albarracin. The inner screen model of consciousness. 2023-06-19.zh-Hant.srt` | `zh-Hant` | `translations/y0Jyj6LAb8g.zh-Hant.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_046`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.de.srt` | `de` | `translations/dUW8cD8XUec.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.en(ie).srt` | `en` | `translations/dUW8cD8XUec.en.srt` | **assumed (sole part)** | en qualifier in "en(ie)"; stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.es.srt` | `es` | `translations/dUW8cD8XUec.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.fr.srt` | `fr` | `translations/dUW8cD8XUec.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.it.srt` | `it` | `translations/dUW8cD8XUec.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.ja.srt` | `ja` | `translations/dUW8cD8XUec.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.ko.srt` | `ko` | `translations/dUW8cD8XUec.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.nl.srt` | `nl` | `translations/dUW8cD8XUec.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.pt.srt` | `pt` | `translations/dUW8cD8XUec.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.ru.srt` | `ru` | `translations/dUW8cD8XUec.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.zh-Hans.srt` | `zh-Hans` | `translations/dUW8cD8XUec.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.zh-Hant.srt` | `zh-Hant` | `translations/dUW8cD8XUec.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_047`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.de.srt` | `de` | `translations/O6adLcDhOYU.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.es.srt` | `es` | `translations/O6adLcDhOYU.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.fr.srt` | `fr` | `translations/O6adLcDhOYU.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.it.srt` | `it` | `translations/O6adLcDhOYU.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.ja.srt` | `ja` | `translations/O6adLcDhOYU.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.ko.srt` | `ko` | `translations/O6adLcDhOYU.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.nl.srt` | `nl` | `translations/O6adLcDhOYU.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.pt.srt` | `pt` | `translations/O6adLcDhOYU.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.ru.srt` | `ru` | `translations/O6adLcDhOYU.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.zh-Hans.srt` | `zh-Hans` | `translations/O6adLcDhOYU.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.zh-Hant.srt` | `zh-Hant` | `translations/O6adLcDhOYU.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_048`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.de.srt` | `de` | `translations/aFwuucck7a8.de.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.es.srt` | `es` | `translations/aFwuucck7a8.es.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.fr.srt` | `fr` | `translations/aFwuucck7a8.fr.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.it.srt` | `it` | `translations/aFwuucck7a8.it.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.ja.srt` | `ja` | `translations/aFwuucck7a8.ja.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.ko.srt` | `ko` | `translations/aFwuucck7a8.ko.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.nl.srt` | `nl` | `translations/aFwuucck7a8.nl.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.pt.srt` | `pt` | `translations/aFwuucck7a8.pt.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.ru.srt` | `ru` | `translations/aFwuucck7a8.ru.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.zh-Hans.srt` | `zh-Hans` | `translations/aFwuucck7a8.zh-Hans.srt` | yes (title exact) |  |
| `ActInf GuestStream 048.1 ~ Arthur Juliani & Adam Safron  Deep CANALs.zh-Hant.srt` | `zh-Hant` | `translations/aFwuucck7a8.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_049`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.de.srt` | `de` | `translations/dUXfgzKHV1c.de.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.es.srt` | `es` | `translations/dUXfgzKHV1c.es.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.fr.srt` | `fr` | `translations/dUXfgzKHV1c.fr.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.it.srt` | `it` | `translations/dUXfgzKHV1c.it.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.ja.srt` | `ja` | `translations/dUXfgzKHV1c.ja.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.ko.srt` | `ko` | `translations/dUXfgzKHV1c.ko.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.nl.srt` | `nl` | `translations/dUXfgzKHV1c.nl.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.pt.srt` | `pt` | `translations/dUXfgzKHV1c.pt.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.ru.srt` | `ru` | `translations/dUXfgzKHV1c.ru.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.zh-Hans.srt` | `zh-Hans` | `translations/dUXfgzKHV1c.zh-Hans.srt` | yes (title exact) |  |
| `ActInf GuestStream 049.1 ~  Clickbait, consciousness science, and responsible journalism.zh-Hant.srt` | `zh-Hant` | `translations/dUXfgzKHV1c.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_050`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.de.srt` | `de` | `translations/vBk0zZEy59E.de.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.es.srt` | `es` | `translations/vBk0zZEy59E.es.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.fr.srt` | `fr` | `translations/vBk0zZEy59E.fr.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.it.srt` | `it` | `translations/vBk0zZEy59E.it.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.ja.srt` | `ja` | `translations/vBk0zZEy59E.ja.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.ko.srt` | `ko` | `translations/vBk0zZEy59E.ko.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.nl.srt` | `nl` | `translations/vBk0zZEy59E.nl.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.pt.srt` | `pt` | `translations/vBk0zZEy59E.pt.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.ru.srt` | `ru` | `translations/vBk0zZEy59E.ru.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.zh-Hans.srt` | `zh-Hans` | `translations/vBk0zZEy59E.zh-Hans.srt` | yes (title exact) |  |
| `ActInf GuestStream 050.1 ~ Valeria Becattini & Anna Ciaunica,  Selfless Minds, Unlimited Bodies.zh-Hant.srt` | `zh-Hant` | `translations/vBk0zZEy59E.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_051`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.de.srt` | `de` | `translations/NOj0mB8I6BI.de.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.es.srt` | `es` | `translations/NOj0mB8I6BI.es.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.fr.srt` | `fr` | `translations/NOj0mB8I6BI.fr.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.it.srt` | `it` | `translations/NOj0mB8I6BI.it.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.ja.srt` | `ja` | `translations/NOj0mB8I6BI.ja.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.ko.srt` | `ko` | `translations/NOj0mB8I6BI.ko.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.nl.srt` | `nl` | `translations/NOj0mB8I6BI.nl.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.pt.srt` | `pt` | `translations/NOj0mB8I6BI.pt.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.ru.srt` | `ru` | `translations/NOj0mB8I6BI.ru.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.zh-Hans.srt` | `zh-Hans` | `translations/NOj0mB8I6BI.zh-Hans.srt` | yes (title exact) |  |
| `ActInf GuestStream 051.1 ~ Tommaso Salvatori  Causal Inference via Predictive Coding.zh-Hant.srt` | `zh-Hant` | `translations/NOj0mB8I6BI.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_052`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.de.srt` | `de` | `translations/KPeOC9eNDnA.de.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.es.srt` | `es` | `translations/KPeOC9eNDnA.es.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.fr.srt` | `fr` | `translations/KPeOC9eNDnA.fr.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.it.srt` | `it` | `translations/KPeOC9eNDnA.it.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.ja.srt` | `ja` | `translations/KPeOC9eNDnA.ja.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.ko.srt` | `ko` | `translations/KPeOC9eNDnA.ko.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.nl.srt` | `nl` | `translations/KPeOC9eNDnA.nl.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.pt.srt` | `pt` | `translations/KPeOC9eNDnA.pt.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.ru.srt` | `ru` | `translations/KPeOC9eNDnA.ru.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.zh-Hans.srt` | `zh-Hans` | `translations/KPeOC9eNDnA.zh-Hans.srt` | yes (title exact) |  |
| `ActInf GuestStream 052.1 ~ A ElSaid, T Desell, A Ororbia  Ant-Based Neural Topology Search.zh-Hant.srt` | `zh-Hant` | `translations/KPeOC9eNDnA.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_053`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.de.srt` | `de` | `translations/_GHJO_bnyrY.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.es.srt` | `es` | `translations/_GHJO_bnyrY.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.fr.srt` | `fr` | `translations/_GHJO_bnyrY.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.it.srt` | `it` | `translations/_GHJO_bnyrY.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.ja.srt` | `ja` | `translations/_GHJO_bnyrY.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.ko.srt` | `ko` | `translations/_GHJO_bnyrY.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.nl.srt` | `nl` | `translations/_GHJO_bnyrY.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.pt.srt` | `pt` | `translations/_GHJO_bnyrY.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.ru.srt` | `ru` | `translations/_GHJO_bnyrY.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.zh-Hans.srt` | `zh-Hans` | `translations/_GHJO_bnyrY.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.zh-Hant.srt` | `zh-Hant` | `translations/_GHJO_bnyrY.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_054`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).de.srt` | `de` | `translations/bhLPZaLmi2k.de.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).es.srt` | `es` | `translations/bhLPZaLmi2k.es.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).fr.srt` | `fr` | `translations/bhLPZaLmi2k.fr.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).it.srt` | `it` | `translations/bhLPZaLmi2k.it.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).ja.srt` | `ja` | `translations/bhLPZaLmi2k.ja.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).ko.srt` | `ko` | `translations/bhLPZaLmi2k.ko.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).nl.srt` | `nl` | `translations/bhLPZaLmi2k.nl.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).pt.srt` | `pt` | `translations/bhLPZaLmi2k.pt.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).ru.srt` | `ru` | `translations/bhLPZaLmi2k.ru.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).zh-Hans.srt` | `zh-Hans` | `translations/bhLPZaLmi2k.zh-Hans.srt` | yes (title prefix) |  |
| `ActInf GuestStream 054.1 ~ A Gómez Emilsson & C Percy ~ Electromagnetic Field Topology Consciousness (2).zh-Hant.srt` | `zh-Hant` | `translations/bhLPZaLmi2k.zh-Hant.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_055`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.de.srt` | `de` | `translations/a4DC1YCVpsU.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.es.srt` | `es` | `translations/a4DC1YCVpsU.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.fr.srt` | `fr` | `translations/a4DC1YCVpsU.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.it.srt` | `it` | `translations/a4DC1YCVpsU.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.ja.srt` | `ja` | `translations/a4DC1YCVpsU.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.ko.srt` | `ko` | `translations/a4DC1YCVpsU.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.nl.srt` | `nl` | `translations/a4DC1YCVpsU.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.pt.srt` | `pt` | `translations/a4DC1YCVpsU.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.ru.srt` | `ru` | `translations/a4DC1YCVpsU.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.zh-Hans.srt` | `zh-Hans` | `translations/a4DC1YCVpsU.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.zh-Hant.srt` | `zh-Hant` | `translations/a4DC1YCVpsU.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_056`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.de.srt` | `de` | `translations/h0Tfm2lw6PQ.de.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.es.srt` | `es` | `translations/h0Tfm2lw6PQ.es.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.fr.srt` | `fr` | `translations/h0Tfm2lw6PQ.fr.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.it.srt` | `it` | `translations/h0Tfm2lw6PQ.it.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.ja.srt` | `ja` | `translations/h0Tfm2lw6PQ.ja.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.ko.srt` | `ko` | `translations/h0Tfm2lw6PQ.ko.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.nl.srt` | `nl` | `translations/h0Tfm2lw6PQ.nl.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.pt.srt` | `pt` | `translations/h0Tfm2lw6PQ.pt.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.ru.srt` | `ru` | `translations/h0Tfm2lw6PQ.ru.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.zh-Hans.srt` | `zh-Hans` | `translations/h0Tfm2lw6PQ.zh-Hans.srt` | yes (title exact) |  |
| `ActInf GuestStream 056.1 ~ Grégoire Sergeant,  Agency with structured latent state-spaces.zh-Hant.srt` | `zh-Hant` | `translations/h0Tfm2lw6PQ.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_057`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.de.srt` | `de` | `translations/1uIRljnLtc4.de.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.es.srt` | `es` | `translations/1uIRljnLtc4.es.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.fr.srt` | `fr` | `translations/1uIRljnLtc4.fr.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.it.srt` | `it` | `translations/1uIRljnLtc4.it.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.ja.srt` | `ja` | `translations/1uIRljnLtc4.ja.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.ko.srt` | `ko` | `translations/1uIRljnLtc4.ko.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.nl.srt` | `nl` | `translations/1uIRljnLtc4.nl.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.pt.srt` | `pt` | `translations/1uIRljnLtc4.pt.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.ru.srt` | `ru` | `translations/1uIRljnLtc4.ru.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.zh-Hans.srt` | `zh-Hans` | `translations/1uIRljnLtc4.zh-Hans.srt` | yes (title prefix) |  |
| `ActInf GuestStream 057 1~ Andy Keller, Natural Neural Structure.zh-Hant.srt` | `zh-Hant` | `translations/1uIRljnLtc4.zh-Hant.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_058`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `gs058-1 Working with Gerald Edelman.de.srt` | `de` | `translations/Sz7ZP2N6DuE.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.es.srt` | `es` | `translations/Sz7ZP2N6DuE.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.fr.srt` | `fr` | `translations/Sz7ZP2N6DuE.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.it.srt` | `it` | `translations/Sz7ZP2N6DuE.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.ja.srt` | `ja` | `translations/Sz7ZP2N6DuE.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.ko.srt` | `ko` | `translations/Sz7ZP2N6DuE.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.nl.srt` | `nl` | `translations/Sz7ZP2N6DuE.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.pt.srt` | `pt` | `translations/Sz7ZP2N6DuE.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.ru.srt` | `ru` | `translations/Sz7ZP2N6DuE.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.zh-Hans.srt` | `zh-Hans` | `translations/Sz7ZP2N6DuE.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `gs058-1 Working with Gerald Edelman.zh-Hant.srt` | `zh-Hant` | `translations/Sz7ZP2N6DuE.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/Insights/Insights_001`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Karl Friston ~ Active Inference Insights 001.de.srt` | `de` | `translations/N5H5I6cvcrQ.de.srt` | yes (title prefix) |  |
| `Karl Friston ~ Active Inference Insights 001.es.srt` | `es` | `translations/N5H5I6cvcrQ.es.srt` | yes (title prefix) |  |
| `Karl Friston ~ Active Inference Insights 001.fr.srt` | `fr` | `translations/N5H5I6cvcrQ.fr.srt` | yes (title prefix) |  |
| `Karl Friston ~ Active Inference Insights 001.it.srt` | `it` | `translations/N5H5I6cvcrQ.it.srt` | yes (title prefix) |  |
| `Karl Friston ~ Active Inference Insights 001.ja.srt` | `ja` | `translations/N5H5I6cvcrQ.ja.srt` | yes (title prefix) |  |
| `Karl Friston ~ Active Inference Insights 001.nl.srt` | `nl` | `translations/N5H5I6cvcrQ.nl.srt` | yes (title prefix) |  |
| `Karl Friston ~ Active Inference Insights 001.pt.srt` | `pt` | `translations/N5H5I6cvcrQ.pt.srt` | yes (title prefix) |  |
| `Karl Friston ~ Active Inference Insights 001.ru.srt` | `ru` | `translations/N5H5I6cvcrQ.ru.srt` | yes (title prefix) |  |
| `Karl Friston ~ Active Inference Insights 001.zh-Hans.srt` | `zh-Hans` | `translations/N5H5I6cvcrQ.zh-Hans.srt` | yes (title prefix) |  |
| `Karl Friston ~ Active Inference Insights 001.zh-Hant.srt` | `zh-Hant` | `translations/N5H5I6cvcrQ.zh-Hant.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_001`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference Podcast #001 “Narrative as active inference.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/C94WDXAe4EE.zh-Hans.srt` | **assumed (sole part)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/C94WDXAe4EE.zh-Hans.srt` | **assumed (sole part)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.de.srt` | `de` | `translations/C94WDXAe4EE.de.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.dut(translated).dut(translated).srt` | `nl` | `translations/C94WDXAe4EE.nl.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/C94WDXAe4EE.de.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/C94WDXAe4EE.es.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/C94WDXAe4EE.fr.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/C94WDXAe4EE.it.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/C94WDXAe4EE.ja.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/C94WDXAe4EE.ko.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/C94WDXAe4EE.nl.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/C94WDXAe4EE.pt.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/C94WDXAe4EE.ru.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/C94WDXAe4EE.zh-Hans.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/C94WDXAe4EE.zh-Hant.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.es.srt` | `es` | `translations/C94WDXAe4EE.es.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.fr.srt` | `fr` | `translations/C94WDXAe4EE.fr.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.it.srt` | `it` | `translations/C94WDXAe4EE.it.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.jpn(translated).jpn(translated).srt` | `ja` | `translations/C94WDXAe4EE.ja.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.kor(translated).kor(translated).srt` | `ko` | `translations/C94WDXAe4EE.ko.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.por(translated).por(translated).srt` | `pt` | `translations/C94WDXAe4EE.pt.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `Active Inference Podcast #001 “Narrative as active inference.rus(translated).rus(translated).srt` | `ru` | `translations/C94WDXAe4EE.ru.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_002`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/601-lt_8eVE.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/601-lt_8eVE.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/601-lt_8eVE.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/601-lt_8eVE.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/601-lt_8eVE.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/601-lt_8eVE.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/601-lt_8eVE.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/601-lt_8eVE.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/601-lt_8eVE.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/601-lt_8eVE.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/601-lt_8eVE.zh-Hant.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.de.srt` | `de` | `translations/601-lt_8eVE.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.es.srt` | `es` | `translations/601-lt_8eVE.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.fr.srt` | `fr` | `translations/601-lt_8eVE.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.it.srt` | `it` | `translations/601-lt_8eVE.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.ja.srt` | `ja` | `translations/601-lt_8eVE.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.ko.srt` | `ko` | `translations/601-lt_8eVE.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.nl.srt` | `nl` | `translations/601-lt_8eVE.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.pt.srt` | `pt` | `translations/601-lt_8eVE.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.ru.srt` | `ru` | `translations/601-lt_8eVE.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.zh-Hans.srt` | `zh-Hans` | `translations/601-lt_8eVE.zh-Hans.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Livestream #002.1  Is the free-energy principle a formal theory of semantics.zh-Hant.srt` | `zh-Hant` | `translations/601-lt_8eVE.zh-Hant.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_003`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.de.srt` | `de` | `translations/ijuxHfPDd3U.de.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/ijuxHfPDd3U.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/ijuxHfPDd3U.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/ijuxHfPDd3U.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/ijuxHfPDd3U.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/ijuxHfPDd3U.ja.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/ijuxHfPDd3U.ko.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/ijuxHfPDd3U.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/ijuxHfPDd3U.pt.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/ijuxHfPDd3U.ru.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/ijuxHfPDd3U.zh-Hans.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/ijuxHfPDd3U.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.es.srt` | `es` | `translations/ijuxHfPDd3U.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.fr.srt` | `fr` | `translations/ijuxHfPDd3U.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.ger(translated).ger(translated).srt` | `de` | `translations/ijuxHfPDd3U.de.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.it.srt` | `it` | `translations/ijuxHfPDd3U.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.nl.srt` | `nl` | `translations/ijuxHfPDd3U.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/mz7L4GD5g-E.de.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/mz7L4GD5g-E.es.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/mz7L4GD5g-E.fr.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/mz7L4GD5g-E.it.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/mz7L4GD5g-E.ja.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/mz7L4GD5g-E.ko.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/mz7L4GD5g-E.nl.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/mz7L4GD5g-E.pt.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/mz7L4GD5g-E.ru.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/mz7L4GD5g-E.zh-Hans.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Podcast #003.1  A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/mz7L4GD5g-E.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_004`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.de.srt` | `de` | `translations/Y6qx6C1tmjs.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/Y6qx6C1tmjs.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/Y6qx6C1tmjs.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/Y6qx6C1tmjs.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/Y6qx6C1tmjs.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/Y6qx6C1tmjs.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/Y6qx6C1tmjs.ko.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/Y6qx6C1tmjs.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/Y6qx6C1tmjs.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/Y6qx6C1tmjs.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/Y6qx6C1tmjs.zh-Hans.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/Y6qx6C1tmjs.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.es.srt` | `es` | `translations/Y6qx6C1tmjs.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.fr.srt` | `fr` | `translations/Y6qx6C1tmjs.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.it.srt` | `it` | `translations/Y6qx6C1tmjs.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.ja.srt` | `ja` | `translations/Y6qx6C1tmjs.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.nl.srt` | `nl` | `translations/Y6qx6C1tmjs.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.pt.srt` | `pt` | `translations/Y6qx6C1tmjs.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.ru.srt` | `ru` | `translations/Y6qx6C1tmjs.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.de.srt` | `de` | `translations/SAc1F1AWRAs.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/SAc1F1AWRAs.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/SAc1F1AWRAs.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/SAc1F1AWRAs.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/SAc1F1AWRAs.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/SAc1F1AWRAs.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/SAc1F1AWRAs.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/SAc1F1AWRAs.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/SAc1F1AWRAs.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/SAc1F1AWRAs.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/SAc1F1AWRAs.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/SAc1F1AWRAs.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.es.srt` | `es` | `translations/SAc1F1AWRAs.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.fr.srt` | `fr` | `translations/SAc1F1AWRAs.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.it.srt` | `it` | `translations/SAc1F1AWRAs.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.ja.srt` | `ja` | `translations/SAc1F1AWRAs.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.ko.srt` | `ko` | `translations/SAc1F1AWRAs.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.nl.srt` | `nl` | `translations/SAc1F1AWRAs.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.pt.srt` | `pt` | `translations/SAc1F1AWRAs.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.ru.srt` | `ru` | `translations/SAc1F1AWRAs.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.zh-Hans.srt` | `zh-Hans` | `translations/SAc1F1AWRAs.zh-Hans.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_005`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/g2n47dPUyNY.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/g2n47dPUyNY.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).dut(translated).dut(translated).srt` | `nl` | `translations/g2n47dPUyNY.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/g2n47dPUyNY.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/g2n47dPUyNY.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/g2n47dPUyNY.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/g2n47dPUyNY.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/g2n47dPUyNY.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/g2n47dPUyNY.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/g2n47dPUyNY.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/g2n47dPUyNY.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/g2n47dPUyNY.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/g2n47dPUyNY.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/g2n47dPUyNY.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).fre(translated).fre(translated).srt` | `fr` | `translations/g2n47dPUyNY.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).ger(translated).ger(translated).srt` | `de` | `translations/g2n47dPUyNY.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).ita(translated).ita(translated).srt` | `it` | `translations/g2n47dPUyNY.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).jpn(translated).jpn(translated).srt` | `ja` | `translations/g2n47dPUyNY.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).kor(translated).kor(translated).srt` | `ko` | `translations/g2n47dPUyNY.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).por(translated).por(translated).srt` | `pt` | `translations/g2n47dPUyNY.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).rus(translated).rus(translated).srt` | `ru` | `translations/g2n47dPUyNY.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).spa(translated).spa(translated).srt` | `es` | `translations/g2n47dPUyNY.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/B6Uqf_T-nec.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/B6Uqf_T-nec.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).dut(translated).dut(translated).srt` | `nl` | `translations/B6Uqf_T-nec.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/B6Uqf_T-nec.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/B6Uqf_T-nec.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/B6Uqf_T-nec.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/B6Uqf_T-nec.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/B6Uqf_T-nec.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/B6Uqf_T-nec.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/B6Uqf_T-nec.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/B6Uqf_T-nec.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/B6Uqf_T-nec.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/B6Uqf_T-nec.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/B6Uqf_T-nec.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).fre(translated).fre(translated).srt` | `fr` | `translations/B6Uqf_T-nec.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).ger(translated).ger(translated).srt` | `de` | `translations/B6Uqf_T-nec.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).ita(translated).ita(translated).srt` | `it` | `translations/B6Uqf_T-nec.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).jpn(translated).jpn(translated).srt` | `ja` | `translations/B6Uqf_T-nec.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).kor(translated).kor(translated).srt` | `ko` | `translations/B6Uqf_T-nec.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).por(translated).por(translated).srt` | `pt` | `translations/B6Uqf_T-nec.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).rus(translated).rus(translated).srt` | `ru` | `translations/B6Uqf_T-nec.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).spa(translated).spa(translated).srt` | `es` | `translations/B6Uqf_T-nec.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/V7yNq_KpHo8.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/V7yNq_KpHo8.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).dut(translated).dut(translated).srt` | `nl` | `translations/V7yNq_KpHo8.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/V7yNq_KpHo8.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/V7yNq_KpHo8.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/V7yNq_KpHo8.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/V7yNq_KpHo8.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/V7yNq_KpHo8.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/V7yNq_KpHo8.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/V7yNq_KpHo8.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/V7yNq_KpHo8.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/V7yNq_KpHo8.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/V7yNq_KpHo8.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/V7yNq_KpHo8.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).fre(translated).fre(translated).srt` | `fr` | `translations/V7yNq_KpHo8.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).ger(translated).ger(translated).srt` | `de` | `translations/V7yNq_KpHo8.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).ita(translated).ita(translated).srt` | `it` | `translations/V7yNq_KpHo8.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).jpn(translated).jpn(translated).srt` | `ja` | `translations/V7yNq_KpHo8.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).kor(translated).kor(translated).srt` | `ko` | `translations/V7yNq_KpHo8.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).por(translated).por(translated).srt` | `pt` | `translations/V7yNq_KpHo8.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).rus(translated).rus(translated).srt` | `ru` | `translations/V7yNq_KpHo8.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).spa(translated).spa(translated).srt` | `es` | `translations/V7yNq_KpHo8.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_006`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/HQadNEGAtbY.zh-Hans.srt` | **NO (ambiguous)** | chi default zh-Hans (no Simp/Trad qualifier); episode token matches 2 parts; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/HQadNEGAtbY.zh-Hans.srt` | **NO (ambiguous)** | chi default zh-Hans (no Simp/Trad qualifier); episode token matches 2 parts; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.dut(translated).dut(translated).srt` | `nl` | `translations/HQadNEGAtbY.nl.srt` | **NO (ambiguous)** | episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/HQadNEGAtbY.de.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/HQadNEGAtbY.es.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/HQadNEGAtbY.fr.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/HQadNEGAtbY.it.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/HQadNEGAtbY.ja.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/HQadNEGAtbY.ko.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/HQadNEGAtbY.nl.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/HQadNEGAtbY.pt.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/HQadNEGAtbY.ru.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/HQadNEGAtbY.zh-Hans.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/HQadNEGAtbY.zh-Hant.srt` | **NO (ambiguous)** | base eng(transcribed) — transcription not translation; episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.fre(translated).fre(translated).srt` | `fr` | `translations/HQadNEGAtbY.fr.srt` | **NO (ambiguous)** | episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.ger(translated).ger(translated).srt` | `de` | `translations/HQadNEGAtbY.de.srt` | **NO (ambiguous)** | episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.ita(translated).ita(translated).srt` | `it` | `translations/HQadNEGAtbY.it.srt` | **NO (ambiguous)** | episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.jpn(translated).jpn(translated).srt` | `ja` | `translations/HQadNEGAtbY.ja.srt` | **NO (ambiguous)** | episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.kor(translated).kor(translated).srt` | `ko` | `translations/HQadNEGAtbY.ko.srt` | **NO (ambiguous)** | episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.por(translated).por(translated).srt` | `pt` | `translations/HQadNEGAtbY.pt.srt` | **NO (ambiguous)** | episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.rus(translated).rus(translated).srt` | `ru` | `translations/HQadNEGAtbY.ru.srt` | **NO (ambiguous)** | episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.spa(translated).spa(translated).srt` | `es` | `translations/HQadNEGAtbY.es.srt` | **NO (ambiguous)** | episode token matches 2 parts; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; ambiguous match — manual resolution |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/jHWCQ1dpoK0.de.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/jHWCQ1dpoK0.es.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/jHWCQ1dpoK0.fr.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/jHWCQ1dpoK0.it.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/jHWCQ1dpoK0.ja.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/jHWCQ1dpoK0.ko.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/jHWCQ1dpoK0.nl.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/jHWCQ1dpoK0.pt.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/jHWCQ1dpoK0.ru.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/jHWCQ1dpoK0.zh-Hans.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #006.0  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/jHWCQ1dpoK0.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/9IIsoNMRSb8.de.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/9IIsoNMRSb8.es.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/9IIsoNMRSb8.fr.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/9IIsoNMRSb8.it.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/9IIsoNMRSb8.ja.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/9IIsoNMRSb8.ko.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/9IIsoNMRSb8.nl.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/9IIsoNMRSb8.pt.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/9IIsoNMRSb8.ru.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/9IIsoNMRSb8.zh-Hans.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #006.1  A tale of two densities active inference is enactive...  (2020).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/9IIsoNMRSb8.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_007`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/7cJ8dmO3qlY.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/7cJ8dmO3qlY.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).dut(translated).dut(translated).srt` | `nl` | `translations/7cJ8dmO3qlY.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/7cJ8dmO3qlY.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/7cJ8dmO3qlY.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/7cJ8dmO3qlY.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/7cJ8dmO3qlY.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/7cJ8dmO3qlY.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/7cJ8dmO3qlY.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/7cJ8dmO3qlY.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/7cJ8dmO3qlY.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/7cJ8dmO3qlY.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/7cJ8dmO3qlY.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/7cJ8dmO3qlY.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).fre(translated).fre(translated).srt` | `fr` | `translations/7cJ8dmO3qlY.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).ger(translated).ger(translated).srt` | `de` | `translations/7cJ8dmO3qlY.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).ita(translated).ita(translated).srt` | `it` | `translations/7cJ8dmO3qlY.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).jpn(translated).jpn(translated).srt` | `ja` | `translations/7cJ8dmO3qlY.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).kor(translated).kor(translated).srt` | `ko` | `translations/7cJ8dmO3qlY.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).por(translated).por(translated).srt` | `pt` | `translations/7cJ8dmO3qlY.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).rus(translated).rus(translated).srt` | `ru` | `translations/7cJ8dmO3qlY.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).spa(translated).spa(translated).srt` | `es` | `translations/7cJ8dmO3qlY.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/72g62XJ-SpA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).dut(translated).dut(translated).srt` | `nl` | `translations/72g62XJ-SpA.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/72g62XJ-SpA.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/72g62XJ-SpA.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/72g62XJ-SpA.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/72g62XJ-SpA.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/72g62XJ-SpA.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/72g62XJ-SpA.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/72g62XJ-SpA.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/72g62XJ-SpA.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/72g62XJ-SpA.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/72g62XJ-SpA.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/72g62XJ-SpA.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).fre(translated).fre(translated).srt` | `fr` | `translations/72g62XJ-SpA.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).ger(translated).ger(translated).srt` | `de` | `translations/72g62XJ-SpA.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).ita(translated).ita(translated).srt` | `it` | `translations/72g62XJ-SpA.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).jpn(translated).jpn(translated).srt` | `ja` | `translations/72g62XJ-SpA.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).kor(translated).kor(translated).srt` | `ko` | `translations/72g62XJ-SpA.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).por(translated).por(translated).srt` | `pt` | `translations/72g62XJ-SpA.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).rus(translated).rus(translated).srt` | `ru` | `translations/72g62XJ-SpA.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).spa(translated).spa(translated).srt` | `es` | `translations/72g62XJ-SpA.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/qf4S9bK5VKQ.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/qf4S9bK5VKQ.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).de.srt` | `de` | `translations/qf4S9bK5VKQ.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).dut(translated).dut(translated).srt` | `nl` | `translations/qf4S9bK5VKQ.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/qf4S9bK5VKQ.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/qf4S9bK5VKQ.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/qf4S9bK5VKQ.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/qf4S9bK5VKQ.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/qf4S9bK5VKQ.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/qf4S9bK5VKQ.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/qf4S9bK5VKQ.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/qf4S9bK5VKQ.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/qf4S9bK5VKQ.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/qf4S9bK5VKQ.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/qf4S9bK5VKQ.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).fr.srt` | `fr` | `translations/qf4S9bK5VKQ.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).ita(translated).ita(translated).srt` | `it` | `translations/qf4S9bK5VKQ.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).jpn(translated).jpn(translated).srt` | `ja` | `translations/qf4S9bK5VKQ.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).kor(translated).kor(translated).srt` | `ko` | `translations/qf4S9bK5VKQ.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).por(translated).por(translated).srt` | `pt` | `translations/qf4S9bK5VKQ.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).rus(translated).rus(translated).srt` | `ru` | `translations/qf4S9bK5VKQ.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).spa(translated).spa(translated).srt` | `es` | `translations/qf4S9bK5VKQ.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_008`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference podcast #008.0 “Scaling active inference  (2019).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/kXw1CPRkJCw.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/kXw1CPRkJCw.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).dut(translated).dut(translated).srt` | `nl` | `translations/kXw1CPRkJCw.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/kXw1CPRkJCw.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/kXw1CPRkJCw.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/kXw1CPRkJCw.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/kXw1CPRkJCw.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/kXw1CPRkJCw.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/kXw1CPRkJCw.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/kXw1CPRkJCw.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/kXw1CPRkJCw.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/kXw1CPRkJCw.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/kXw1CPRkJCw.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/kXw1CPRkJCw.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).fre(translated).fre(translated).srt` | `fr` | `translations/kXw1CPRkJCw.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).ger(translated).ger(translated).srt` | `de` | `translations/kXw1CPRkJCw.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).ita(translated).ita(translated).srt` | `it` | `translations/kXw1CPRkJCw.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).jpn(translated).jpn(translated).srt` | `ja` | `translations/kXw1CPRkJCw.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).kor(translated).kor(translated).srt` | `ko` | `translations/kXw1CPRkJCw.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).por(translated).por(translated).srt` | `pt` | `translations/kXw1CPRkJCw.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).rus(translated).rus(translated).srt` | `ru` | `translations/kXw1CPRkJCw.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.0 “Scaling active inference  (2019).spa(translated).spa(translated).srt` | `es` | `translations/kXw1CPRkJCw.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/zG0qP7un91k.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/zG0qP7un91k.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).dut(translated).dut(translated).srt` | `nl` | `translations/zG0qP7un91k.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/zG0qP7un91k.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/zG0qP7un91k.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/zG0qP7un91k.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/zG0qP7un91k.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/zG0qP7un91k.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/zG0qP7un91k.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/zG0qP7un91k.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/zG0qP7un91k.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/zG0qP7un91k.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/zG0qP7un91k.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/zG0qP7un91k.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).fre(translated).fre(translated).srt` | `fr` | `translations/zG0qP7un91k.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).ger(translated).ger(translated).srt` | `de` | `translations/zG0qP7un91k.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).ita(translated).ita(translated).srt` | `it` | `translations/zG0qP7un91k.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).jpn(translated).jpn(translated).srt` | `ja` | `translations/zG0qP7un91k.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).kor(translated).kor(translated).srt` | `ko` | `translations/zG0qP7un91k.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).por(translated).por(translated).srt` | `pt` | `translations/zG0qP7un91k.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).rus(translated).rus(translated).srt` | `ru` | `translations/zG0qP7un91k.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.1 “Scaling active inference  (2019).spa(translated).spa(translated).srt` | `es` | `translations/zG0qP7un91k.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/gv8RuRiZTQA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/gv8RuRiZTQA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).dut(translated).dut(translated).srt` | `nl` | `translations/gv8RuRiZTQA.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/gv8RuRiZTQA.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/gv8RuRiZTQA.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/gv8RuRiZTQA.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/gv8RuRiZTQA.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/gv8RuRiZTQA.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/gv8RuRiZTQA.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/gv8RuRiZTQA.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/gv8RuRiZTQA.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/gv8RuRiZTQA.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/gv8RuRiZTQA.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/gv8RuRiZTQA.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).fre(translated).fre(translated).srt` | `fr` | `translations/gv8RuRiZTQA.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).ger(translated).ger(translated).srt` | `de` | `translations/gv8RuRiZTQA.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).ita(translated).ita(translated).srt` | `it` | `translations/gv8RuRiZTQA.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).jpn(translated).jpn(translated).srt` | `ja` | `translations/gv8RuRiZTQA.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).kor(translated).kor(translated).srt` | `ko` | `translations/gv8RuRiZTQA.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).por(translated).por(translated).srt` | `pt` | `translations/gv8RuRiZTQA.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).rus(translated).rus(translated).srt` | `ru` | `translations/gv8RuRiZTQA.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #008.2 “Scaling active inference  (2019).spa(translated).spa(translated).srt` | `es` | `translations/gv8RuRiZTQA.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_009`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/XnOfWFnN2iI.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/XnOfWFnN2iI.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/XnOfWFnN2iI.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/XnOfWFnN2iI.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/XnOfWFnN2iI.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/XnOfWFnN2iI.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/XnOfWFnN2iI.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/XnOfWFnN2iI.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/XnOfWFnN2iI.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/XnOfWFnN2iI.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/XnOfWFnN2iI.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/pSWRTkmR8eg.de.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/pSWRTkmR8eg.es.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/pSWRTkmR8eg.fr.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/pSWRTkmR8eg.it.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/pSWRTkmR8eg.ja.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/pSWRTkmR8eg.ko.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/pSWRTkmR8eg.nl.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/pSWRTkmR8eg.pt.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/pSWRTkmR8eg.ru.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/pSWRTkmR8eg.zh-Hans.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.1 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/pSWRTkmR8eg.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/XYRKlh2c-ps.de.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/XYRKlh2c-ps.es.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/XYRKlh2c-ps.fr.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/XYRKlh2c-ps.it.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/XYRKlh2c-ps.ja.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/XYRKlh2c-ps.ko.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/XYRKlh2c-ps.nl.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/XYRKlh2c-ps.pt.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/XYRKlh2c-ps.ru.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/XYRKlh2c-ps.zh-Hans.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference Stream #009.2 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/XYRKlh2c-ps.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/XnOfWFnN2iI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/XnOfWFnN2iI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).dut(translated).dut(translated).srt` | `nl` | `translations/XnOfWFnN2iI.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).fre(translated).fre(translated).srt` | `fr` | `translations/XnOfWFnN2iI.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).ger(translated).ger(translated).srt` | `de` | `translations/XnOfWFnN2iI.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).ita(translated).ita(translated).srt` | `it` | `translations/XnOfWFnN2iI.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).jpn(translated).jpn(translated).srt` | `ja` | `translations/XnOfWFnN2iI.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).kor(translated).kor(translated).srt` | `ko` | `translations/XnOfWFnN2iI.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).por(translated).por(translated).srt` | `pt` | `translations/XnOfWFnN2iI.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).rus(translated).rus(translated).srt` | `ru` | `translations/XnOfWFnN2iI.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).spa(translated).spa(translated).srt` | `es` | `translations/XnOfWFnN2iI.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_010`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/5DB77oxbABo.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/5DB77oxbABo.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).dut(translated).dut(translated).srt` | `nl` | `translations/5DB77oxbABo.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/5DB77oxbABo.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/5DB77oxbABo.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/5DB77oxbABo.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/5DB77oxbABo.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/5DB77oxbABo.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/5DB77oxbABo.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/5DB77oxbABo.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/5DB77oxbABo.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/5DB77oxbABo.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/5DB77oxbABo.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/5DB77oxbABo.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).fre(translated).fre(translated).srt` | `fr` | `translations/5DB77oxbABo.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).ger(translated).ger(translated).srt` | `de` | `translations/5DB77oxbABo.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).ita(translated).ita(translated).srt` | `it` | `translations/5DB77oxbABo.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).jpn(translated).jpn(translated).srt` | `ja` | `translations/5DB77oxbABo.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).kor(translated).kor(translated).srt` | `ko` | `translations/5DB77oxbABo.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).por(translated).por(translated).srt` | `pt` | `translations/5DB77oxbABo.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).rus(translated).rus(translated).srt` | `ru` | `translations/5DB77oxbABo.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).spa(translated).spa(translated).srt` | `es` | `translations/5DB77oxbABo.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/3Sg1sAlgQaM.de.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/3Sg1sAlgQaM.es.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/3Sg1sAlgQaM.fr.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/3Sg1sAlgQaM.it.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/3Sg1sAlgQaM.ja.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/3Sg1sAlgQaM.ko.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/3Sg1sAlgQaM.nl.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/3Sg1sAlgQaM.pt.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/3Sg1sAlgQaM.ru.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/3Sg1sAlgQaM.zh-Hans.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.1  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/3Sg1sAlgQaM.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/IGKUS1W25rY.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/IGKUS1W25rY.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).dut(translated).dut(translated).srt` | `nl` | `translations/IGKUS1W25rY.nl.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/IGKUS1W25rY.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/IGKUS1W25rY.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/IGKUS1W25rY.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/IGKUS1W25rY.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/IGKUS1W25rY.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/IGKUS1W25rY.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/IGKUS1W25rY.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/IGKUS1W25rY.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/IGKUS1W25rY.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/IGKUS1W25rY.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/IGKUS1W25rY.zh-Hant.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).fre(translated).fre(translated).srt` | `fr` | `translations/IGKUS1W25rY.fr.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).ger(translated).ger(translated).srt` | `de` | `translations/IGKUS1W25rY.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).ita(translated).ita(translated).srt` | `it` | `translations/IGKUS1W25rY.it.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).jpn(translated).jpn(translated).srt` | `ja` | `translations/IGKUS1W25rY.ja.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).kor(translated).kor(translated).srt` | `ko` | `translations/IGKUS1W25rY.ko.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).por(translated).por(translated).srt` | `pt` | `translations/IGKUS1W25rY.pt.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).rus(translated).rus(translated).srt` | `ru` | `translations/IGKUS1W25rY.ru.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).spa(translated).spa(translated).srt` | `es` | `translations/IGKUS1W25rY.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_011`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #011.0  Sophisticated Affective Inference Simulating Anticipatory  (2020).fre(translated).fre(translated).srt` | `fr` | `translations/HSu9sDa6-BQ.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.0  Sophisticated Affective Inference Simulating Anticipatory  (2020).ita(translated).ita(translated).srt` | `it` | `translations/HSu9sDa6-BQ.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.0  Sophisticated Affective Inference Simulating Anticipatory  (2020).por(translated).por(translated).srt` | `pt` | `translations/HSu9sDa6-BQ.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.0  Sophisticated Affective Inference Simulating Anticipatory  (2020).rus(translated).rus(translated).srt` | `ru` | `translations/HSu9sDa6-BQ.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.0  Sophisticated Affective Inference Simulating Anticipatory  (2020).spa(translated).spa(translated).srt` | `es` | `translations/HSu9sDa6-BQ.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/xCqavxpiw44.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/xCqavxpiw44.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).dut(translated).dut(translated).srt` | `nl` | `translations/xCqavxpiw44.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).fre(translated).fre(translated).srt` | `fr` | `translations/xCqavxpiw44.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).ger(translated).ger(translated).srt` | `de` | `translations/xCqavxpiw44.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).ita(translated).ita(translated).srt` | `it` | `translations/xCqavxpiw44.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).jpn(translated).jpn(translated).srt` | `ja` | `translations/xCqavxpiw44.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).kor(translated).kor(translated).srt` | `ko` | `translations/xCqavxpiw44.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).por(translated).por(translated).srt` | `pt` | `translations/xCqavxpiw44.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).rus(translated).rus(translated).srt` | `ru` | `translations/xCqavxpiw44.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).spa(translated).spa(translated).srt` | `es` | `translations/xCqavxpiw44.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_013`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/8dPps0qLrp4.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/8dPps0qLrp4.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.dut(translated).dut(translated).srt` | `nl` | `translations/8dPps0qLrp4.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.fre(translated).fre(translated).srt` | `fr` | `translations/8dPps0qLrp4.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.ger(translated).ger(translated).srt` | `de` | `translations/8dPps0qLrp4.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.ita(translated).ita(translated).srt` | `it` | `translations/8dPps0qLrp4.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.jpn(translated).jpn(translated).srt` | `ja` | `translations/8dPps0qLrp4.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.kor(translated).kor(translated).srt` | `ko` | `translations/8dPps0qLrp4.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.por(translated).por(translated).srt` | `pt` | `translations/8dPps0qLrp4.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.rus(translated).rus(translated).srt` | `ru` | `translations/8dPps0qLrp4.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.spa(translated).spa(translated).srt` | `es` | `translations/8dPps0qLrp4.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/QG2gOoX4XdA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....chi(translated).chi(translated).srt` | `zh-Hans` | `translations/QG2gOoX4XdA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....dut(translated).dut(translated).srt` | `nl` | `translations/QG2gOoX4XdA.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....fre(translated).fre(translated).srt` | `fr` | `translations/QG2gOoX4XdA.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....ger(translated).ger(translated).srt` | `de` | `translations/QG2gOoX4XdA.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....ita(translated).ita(translated).srt` | `it` | `translations/QG2gOoX4XdA.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....jpn(translated).jpn(translated).srt` | `ja` | `translations/QG2gOoX4XdA.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....kor(translated).kor(translated).srt` | `ko` | `translations/QG2gOoX4XdA.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....por(translated).por(translated).srt` | `pt` | `translations/QG2gOoX4XdA.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....rus(translated).rus(translated).srt` | `ru` | `translations/QG2gOoX4XdA.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....spa(translated).spa(translated).srt` | `es` | `translations/QG2gOoX4XdA.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/PyyHd4P8dbs.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/PyyHd4P8dbs.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.dut(translated).dut(translated).srt` | `nl` | `translations/PyyHd4P8dbs.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.fre(translated).fre(translated).srt` | `fr` | `translations/PyyHd4P8dbs.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.ger(translated).ger(translated).srt` | `de` | `translations/PyyHd4P8dbs.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.ita(translated).ita(translated).srt` | `it` | `translations/PyyHd4P8dbs.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.jpn(translated).jpn(translated).srt` | `ja` | `translations/PyyHd4P8dbs.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.kor(translated).kor(translated).srt` | `ko` | `translations/PyyHd4P8dbs.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.por(translated).por(translated).srt` | `pt` | `translations/PyyHd4P8dbs.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.rus(translated).rus(translated).srt` | `ru` | `translations/PyyHd4P8dbs.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.spa(translated).spa(translated).srt` | `es` | `translations/PyyHd4P8dbs.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_014`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/Uheml5XRCWk.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/Uheml5XRCWk.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.dut(translated).dut(translated).srt` | `nl` | `translations/Uheml5XRCWk.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.fre(translated).fre(translated).srt` | `fr` | `translations/Uheml5XRCWk.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.ger(translated).ger(translated).srt` | `de` | `translations/Uheml5XRCWk.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.ita(translated).ita(translated).srt` | `it` | `translations/Uheml5XRCWk.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.jpn(translated).jpn(translated).srt` | `ja` | `translations/Uheml5XRCWk.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.kor(translated).kor(translated).srt` | `ko` | `translations/Uheml5XRCWk.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.por(translated).por(translated).srt` | `pt` | `translations/Uheml5XRCWk.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.rus(translated).rus(translated).srt` | `ru` | `translations/Uheml5XRCWk.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.spa(translated).spa(translated).srt` | `es` | `translations/Uheml5XRCWk.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/gQQyd8Hd3AA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/gQQyd8Hd3AA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.dut(translated).dut(translated).srt` | `nl` | `translations/gQQyd8Hd3AA.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.fre(translated).fre(translated).srt` | `fr` | `translations/gQQyd8Hd3AA.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.ger(translated).ger(translated).srt` | `de` | `translations/gQQyd8Hd3AA.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.ita(translated).ita(translated).srt` | `it` | `translations/gQQyd8Hd3AA.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.jpn(translated).jpn(translated).srt` | `ja` | `translations/gQQyd8Hd3AA.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.kor(translated).kor(translated).srt` | `ko` | `translations/gQQyd8Hd3AA.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.por(translated).por(translated).srt` | `pt` | `translations/gQQyd8Hd3AA.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.rus(translated).rus(translated).srt` | `ru` | `translations/gQQyd8Hd3AA.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.spa(translated).spa(translated).srt` | `es` | `translations/gQQyd8Hd3AA.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/4Mu8lDqzBog.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/4Mu8lDqzBog.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.dut(translated).dut(translated).srt` | `nl` | `translations/4Mu8lDqzBog.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.fre(translated).fre(translated).srt` | `fr` | `translations/4Mu8lDqzBog.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.ger(translated).ger(translated).srt` | `de` | `translations/4Mu8lDqzBog.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.ita(translated).ita(translated).srt` | `it` | `translations/4Mu8lDqzBog.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.jpn(translated).jpn(translated).srt` | `ja` | `translations/4Mu8lDqzBog.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.kor(translated).kor(translated).srt` | `ko` | `translations/4Mu8lDqzBog.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.por(translated).por(translated).srt` | `pt` | `translations/4Mu8lDqzBog.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.rus(translated).rus(translated).srt` | `ru` | `translations/4Mu8lDqzBog.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.spa(translated).spa(translated).srt` | `es` | `translations/4Mu8lDqzBog.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_015`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/6Z-6p1XPn8A.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/6Z-6p1XPn8A.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.dut(translated).dut(translated).srt` | `nl` | `translations/6Z-6p1XPn8A.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.fre(translated).fre(translated).srt` | `fr` | `translations/6Z-6p1XPn8A.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.ger(translated).ger(translated).srt` | `de` | `translations/6Z-6p1XPn8A.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.ita(translated).ita(translated).srt` | `it` | `translations/6Z-6p1XPn8A.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.jpn(translated).jpn(translated).srt` | `ja` | `translations/6Z-6p1XPn8A.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.kor(translated).kor(translated).srt` | `ko` | `translations/6Z-6p1XPn8A.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.por(translated).por(translated).srt` | `pt` | `translations/6Z-6p1XPn8A.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.rus(translated).rus(translated).srt` | `ru` | `translations/6Z-6p1XPn8A.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.spa(translated).spa(translated).srt` | `es` | `translations/6Z-6p1XPn8A.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/5VPKmVoRvRY.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/5VPKmVoRvRY.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.dut(translated).dut(translated).srt` | `nl` | `translations/5VPKmVoRvRY.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.fre(translated).fre(translated).srt` | `fr` | `translations/5VPKmVoRvRY.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.ger(translated).ger(translated).srt` | `de` | `translations/5VPKmVoRvRY.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.ita(translated).ita(translated).srt` | `it` | `translations/5VPKmVoRvRY.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.jpn(translated).jpn(translated).srt` | `ja` | `translations/5VPKmVoRvRY.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.kor(translated).kor(translated).srt` | `ko` | `translations/5VPKmVoRvRY.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.por(translated).por(translated).srt` | `pt` | `translations/5VPKmVoRvRY.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.rus(translated).rus(translated).srt` | `ru` | `translations/5VPKmVoRvRY.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.spa(translated).spa(translated).srt` | `es` | `translations/5VPKmVoRvRY.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/iJp_Tm6Ej68.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/iJp_Tm6Ej68.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.dut(translated).dut(translated).srt` | `nl` | `translations/iJp_Tm6Ej68.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.fre(translated).fre(translated).srt` | `fr` | `translations/iJp_Tm6Ej68.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.ger(translated).ger(translated).srt` | `de` | `translations/iJp_Tm6Ej68.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.ita(translated).ita(translated).srt` | `it` | `translations/iJp_Tm6Ej68.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.jpn(translated).jpn(translated).srt` | `ja` | `translations/iJp_Tm6Ej68.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.kor(translated).kor(translated).srt` | `ko` | `translations/iJp_Tm6Ej68.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.por(translated).por(translated).srt` | `pt` | `translations/iJp_Tm6Ej68.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.rus(translated).rus(translated).srt` | `ru` | `translations/iJp_Tm6Ej68.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.spa(translated).spa(translated).srt` | `es` | `translations/iJp_Tm6Ej68.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_016`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/i13aBAWuJxk.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/i13aBAWuJxk.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.dut(translated).dut(translated).srt` | `nl` | `translations/i13aBAWuJxk.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.fre(translated).fre(translated).srt` | `fr` | `translations/i13aBAWuJxk.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.ger(translated).ger(translated).srt` | `de` | `translations/i13aBAWuJxk.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.ita(translated).ita(translated).srt` | `it` | `translations/i13aBAWuJxk.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.jpn(translated).jpn(translated).srt` | `ja` | `translations/i13aBAWuJxk.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.kor(translated).kor(translated).srt` | `ko` | `translations/i13aBAWuJxk.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.por(translated).por(translated).srt` | `pt` | `translations/i13aBAWuJxk.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.rus(translated).rus(translated).srt` | `ru` | `translations/i13aBAWuJxk.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.spa(translated).spa(translated).srt` | `es` | `translations/i13aBAWuJxk.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/P6LiF4gTfUo.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/P6LiF4gTfUo.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.dut(translated).dut(translated).srt` | `nl` | `translations/P6LiF4gTfUo.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.fre(translated).fre(translated).srt` | `fr` | `translations/P6LiF4gTfUo.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.ger(translated).ger(translated).srt` | `de` | `translations/P6LiF4gTfUo.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.ita(translated).ita(translated).srt` | `it` | `translations/P6LiF4gTfUo.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.jpn(translated).jpn(translated).srt` | `ja` | `translations/P6LiF4gTfUo.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.kor(translated).kor(translated).srt` | `ko` | `translations/P6LiF4gTfUo.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.por(translated).por(translated).srt` | `pt` | `translations/P6LiF4gTfUo.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.rus(translated).rus(translated).srt` | `ru` | `translations/P6LiF4gTfUo.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.spa(translated).spa(translated).srt` | `es` | `translations/P6LiF4gTfUo.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_017`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/o7sJ-5vFJGk.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/o7sJ-5vFJGk.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.fre(translated).fre(translated).srt` | `fr` | `translations/o7sJ-5vFJGk.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.ger(translated).ger(translated).srt` | `de` | `translations/o7sJ-5vFJGk.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.ita(translated).ita(translated).srt` | `it` | `translations/o7sJ-5vFJGk.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.jpn(translated).jpn(translated).srt` | `ja` | `translations/o7sJ-5vFJGk.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.por(translated).por(translated).srt` | `pt` | `translations/o7sJ-5vFJGk.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.rus(translated).rus(translated).srt` | `ru` | `translations/o7sJ-5vFJGk.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.spa(translated).spa(translated).srt` | `es` | `translations/o7sJ-5vFJGk.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/ldg2An-tEIE.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/ldg2An-tEIE.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.dut(translated).dut(translated).srt` | `nl` | `translations/ldg2An-tEIE.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.fre(translated).fre(translated).srt` | `fr` | `translations/ldg2An-tEIE.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.ger(translated).ger(translated).srt` | `de` | `translations/ldg2An-tEIE.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.ita(translated).ita(translated).srt` | `it` | `translations/ldg2An-tEIE.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.jpn(translated).jpn(translated).srt` | `ja` | `translations/ldg2An-tEIE.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.kor(translated).kor(translated).srt` | `ko` | `translations/ldg2An-tEIE.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.por(translated).por(translated).srt` | `pt` | `translations/ldg2An-tEIE.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.rus(translated).rus(translated).srt` | `ru` | `translations/ldg2An-tEIE.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.spa(translated).spa(translated).srt` | `es` | `translations/ldg2An-tEIE.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.2 ~ Information flow in context-dependent hierarchical Bayesian inference.fre(translated).fre(translated).srt` | `fr` | `translations/zF-EUnA-di4.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.2 ~ Information flow in context-dependent hierarchical Bayesian inference.ger(translated).ger(translated).srt` | `de` | `translations/zF-EUnA-di4.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.2 ~ Information flow in context-dependent hierarchical Bayesian inference.ita(translated).ita(translated).srt` | `it` | `translations/zF-EUnA-di4.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.2 ~ Information flow in context-dependent hierarchical Bayesian inference.por(translated).por(translated).srt` | `pt` | `translations/zF-EUnA-di4.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.2 ~ Information flow in context-dependent hierarchical Bayesian inference.rus(translated).rus(translated).srt` | `ru` | `translations/zF-EUnA-di4.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #017.2 ~ Information flow in context-dependent hierarchical Bayesian inference.spa(translated).spa(translated).srt` | `es` | `translations/zF-EUnA-di4.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_018`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/1z1MHiHiYuM.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/1z1MHiHiYuM.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.dut(translated).dut(translated).srt` | `nl` | `translations/1z1MHiHiYuM.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.fre(translated).fre(translated).srt` | `fr` | `translations/1z1MHiHiYuM.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.ger(translated).ger(translated).srt` | `de` | `translations/1z1MHiHiYuM.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.ita(translated).ita(translated).srt` | `it` | `translations/1z1MHiHiYuM.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.jpn(translated).jpn(translated).srt` | `ja` | `translations/1z1MHiHiYuM.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.kor(translated).kor(translated).srt` | `ko` | `translations/1z1MHiHiYuM.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.por(translated).por(translated).srt` | `pt` | `translations/1z1MHiHiYuM.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.rus(translated).rus(translated).srt` | `ru` | `translations/1z1MHiHiYuM.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.spa(translated).spa(translated).srt` | `es` | `translations/1z1MHiHiYuM.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/Y8Y4f-SEcsI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/Y8Y4f-SEcsI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.dut(translated).dut(translated).srt` | `nl` | `translations/Y8Y4f-SEcsI.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.fre(translated).fre(translated).srt` | `fr` | `translations/Y8Y4f-SEcsI.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.ger(translated).ger(translated).srt` | `de` | `translations/Y8Y4f-SEcsI.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.ita(translated).ita(translated).srt` | `it` | `translations/Y8Y4f-SEcsI.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.jpn(translated).jpn(translated).srt` | `ja` | `translations/Y8Y4f-SEcsI.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.kor(translated).kor(translated).srt` | `ko` | `translations/Y8Y4f-SEcsI.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.por(translated).por(translated).srt` | `pt` | `translations/Y8Y4f-SEcsI.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.rus(translated).rus(translated).srt` | `ru` | `translations/Y8Y4f-SEcsI.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.spa(translated).spa(translated).srt` | `es` | `translations/Y8Y4f-SEcsI.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/3iQBiClVHuo.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/3iQBiClVHuo.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.dut(translated).dut(translated).srt` | `nl` | `translations/3iQBiClVHuo.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.fre(translated).fre(translated).srt` | `fr` | `translations/3iQBiClVHuo.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.ger(translated).ger(translated).srt` | `de` | `translations/3iQBiClVHuo.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.ita(translated).ita(translated).srt` | `it` | `translations/3iQBiClVHuo.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.jpn(translated).jpn(translated).srt` | `ja` | `translations/3iQBiClVHuo.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.kor(translated).kor(translated).srt` | `ko` | `translations/3iQBiClVHuo.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.por(translated).por(translated).srt` | `pt` | `translations/3iQBiClVHuo.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.rus(translated).rus(translated).srt` | `ru` | `translations/3iQBiClVHuo.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.spa(translated).spa(translated).srt` | `es` | `translations/3iQBiClVHuo.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_019`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/1FbOzAJ8CRQ.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/1FbOzAJ8CRQ.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.dut(translated).dut(translated).srt` | `nl` | `translations/1FbOzAJ8CRQ.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.fre(translated).fre(translated).srt` | `fr` | `translations/1FbOzAJ8CRQ.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.ger(translated).ger(translated).srt` | `de` | `translations/1FbOzAJ8CRQ.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.ita(translated).ita(translated).srt` | `it` | `translations/1FbOzAJ8CRQ.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.jpn(translated).jpn(translated).srt` | `ja` | `translations/1FbOzAJ8CRQ.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.kor(translated).kor(translated).srt` | `ko` | `translations/1FbOzAJ8CRQ.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.por(translated).por(translated).srt` | `pt` | `translations/1FbOzAJ8CRQ.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.rus(translated).rus(translated).srt` | `ru` | `translations/1FbOzAJ8CRQ.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.spa(translated).spa(translated).srt` | `es` | `translations/1FbOzAJ8CRQ.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/SMQvRspIzpQ.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/SMQvRspIzpQ.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.dut(translated).dut(translated).srt` | `nl` | `translations/SMQvRspIzpQ.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.fre(translated).fre(translated).srt` | `fr` | `translations/SMQvRspIzpQ.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.ger(translated).ger(translated).srt` | `de` | `translations/SMQvRspIzpQ.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.ita(translated).ita(translated).srt` | `it` | `translations/SMQvRspIzpQ.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.jpn(translated).jpn(translated).srt` | `ja` | `translations/SMQvRspIzpQ.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.kor(translated).kor(translated).srt` | `ko` | `translations/SMQvRspIzpQ.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.por(translated).por(translated).srt` | `pt` | `translations/SMQvRspIzpQ.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.rus(translated).rus(translated).srt` | `ru` | `translations/SMQvRspIzpQ.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.spa(translated).spa(translated).srt` | `es` | `translations/SMQvRspIzpQ.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/z_hArARMQ20.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/z_hArARMQ20.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.dut(translated).dut(translated).srt` | `nl` | `translations/z_hArARMQ20.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.fre(translated).fre(translated).srt` | `fr` | `translations/z_hArARMQ20.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.ger(translated).ger(translated).srt` | `de` | `translations/z_hArARMQ20.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.ita(translated).ita(translated).srt` | `it` | `translations/z_hArARMQ20.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.jpn(translated).jpn(translated).srt` | `ja` | `translations/z_hArARMQ20.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.kor(translated).kor(translated).srt` | `ko` | `translations/z_hArARMQ20.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.por(translated).por(translated).srt` | `pt` | `translations/z_hArARMQ20.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.rus(translated).rus(translated).srt` | `ru` | `translations/z_hArARMQ20.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.spa(translated).spa(translated).srt` | `es` | `translations/z_hArARMQ20.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_020`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/1VTviUyntt8.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/1VTviUyntt8.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.dut(translated).dut(translated).srt` | `nl` | `translations/1VTviUyntt8.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.fre(translated).fre(translated).srt` | `fr` | `translations/1VTviUyntt8.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.ger(translated).ger(translated).srt` | `de` | `translations/1VTviUyntt8.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.ita(translated).ita(translated).srt` | `it` | `translations/1VTviUyntt8.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.jpn(translated).jpn(translated).srt` | `ja` | `translations/1VTviUyntt8.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.kor(translated).kor(translated).srt` | `ko` | `translations/1VTviUyntt8.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.por(translated).por(translated).srt` | `pt` | `translations/1VTviUyntt8.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.rus(translated).rus(translated).srt` | `ru` | `translations/1VTviUyntt8.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.spa(translated).spa(translated).srt` | `es` | `translations/1VTviUyntt8.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/szCSh8pVEa4.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/szCSh8pVEa4.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).dut(translated).dut(translated).srt` | `nl` | `translations/szCSh8pVEa4.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).fre(translated).fre(translated).srt` | `fr` | `translations/szCSh8pVEa4.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).ger(translated).ger(translated).srt` | `de` | `translations/szCSh8pVEa4.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).ita(translated).ita(translated).srt` | `it` | `translations/szCSh8pVEa4.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).jpn(translated).jpn(translated).srt` | `ja` | `translations/szCSh8pVEa4.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).kor(translated).kor(translated).srt` | `ko` | `translations/szCSh8pVEa4.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).por(translated).por(translated).srt` | `pt` | `translations/szCSh8pVEa4.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).rus(translated).rus(translated).srt` | `ru` | `translations/szCSh8pVEa4.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).spa(translated).spa(translated).srt` | `es` | `translations/szCSh8pVEa4.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/q3qBepJf3vA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/q3qBepJf3vA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.dut(translated).dut(translated).srt` | `nl` | `translations/q3qBepJf3vA.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.fre(translated).fre(translated).srt` | `fr` | `translations/q3qBepJf3vA.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.ger(translated).ger(translated).srt` | `de` | `translations/q3qBepJf3vA.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.ita(translated).ita(translated).srt` | `it` | `translations/q3qBepJf3vA.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.jpn(translated).jpn(translated).srt` | `ja` | `translations/q3qBepJf3vA.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.kor(translated).kor(translated).srt` | `ko` | `translations/q3qBepJf3vA.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.por(translated).por(translated).srt` | `pt` | `translations/q3qBepJf3vA.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.rus(translated).rus(translated).srt` | `ru` | `translations/q3qBepJf3vA.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.spa(translated).spa(translated).srt` | `es` | `translations/q3qBepJf3vA.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_021`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #021.03 ~ John Boik.de.srt` | `de` | `translations/idO34jucRIw.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.es.srt` | `es` | `translations/idO34jucRIw.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.fr.srt` | `fr` | `translations/idO34jucRIw.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.it.srt` | `it` | `translations/idO34jucRIw.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.ja.srt` | `ja` | `translations/idO34jucRIw.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.ko.srt` | `ko` | `translations/idO34jucRIw.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.nl.srt` | `nl` | `translations/idO34jucRIw.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.pt.srt` | `pt` | `translations/idO34jucRIw.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.ru.srt` | `ru` | `translations/idO34jucRIw.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.zh-Hans.srt` | `zh-Hans` | `translations/idO34jucRIw.zh-Hans.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.03 ~ John Boik.zh-Hant.srt` | `zh-Hant` | `translations/idO34jucRIw.zh-Hant.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.04 ~ John Boik.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/PakWPvu07OM.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #021.04 ~ John Boik.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/PakWPvu07OM.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #021.04 ~ John Boik.dut(translated).dut(translated).srt` | `nl` | `translations/PakWPvu07OM.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.04 ~ John Boik.fre(translated).fre(translated).srt` | `fr` | `translations/PakWPvu07OM.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.04 ~ John Boik.ger(translated).ger(translated).srt` | `de` | `translations/PakWPvu07OM.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.04 ~ John Boik.ita(translated).ita(translated).srt` | `it` | `translations/PakWPvu07OM.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.04 ~ John Boik.jpn(translated).jpn(translated).srt` | `ja` | `translations/PakWPvu07OM.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.04 ~ John Boik.kor(translated).kor(translated).srt` | `ko` | `translations/PakWPvu07OM.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.04 ~ John Boik.por(translated).por(translated).srt` | `pt` | `translations/PakWPvu07OM.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.04 ~ John Boik.rus(translated).rus(translated).srt` | `ru` | `translations/PakWPvu07OM.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.04 ~ John Boik.spa(translated).spa(translated).srt` | `es` | `translations/PakWPvu07OM.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.de.srt` | `de` | `translations/mbEqoCV16q4.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.es.srt` | `es` | `translations/mbEqoCV16q4.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.fr.srt` | `fr` | `translations/mbEqoCV16q4.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.it.srt` | `it` | `translations/mbEqoCV16q4.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.ja.srt` | `ja` | `translations/mbEqoCV16q4.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.ko.srt` | `ko` | `translations/mbEqoCV16q4.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.nl.srt` | `nl` | `translations/mbEqoCV16q4.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.pt.srt` | `pt` | `translations/mbEqoCV16q4.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.ru.srt` | `ru` | `translations/mbEqoCV16q4.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.zh-Hans.srt` | `zh-Hans` | `translations/mbEqoCV16q4.zh-Hans.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.1 ~ John Boik.zh-Hant.srt` | `zh-Hant` | `translations/mbEqoCV16q4.zh-Hant.srt` | yes (episode token) |  |
| `ActInfLab Livestream #021.2 ~ John Boik.ger(translated) (2).ger(translated).srt` | `de` | `translations/i5WwQ4WXGNo.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #021.2 ~ John Boik.ger(translated).ger(translated).srt` | `de` | `translations/i5WwQ4WXGNo.de.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_022`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #022.0 ~  Psychophysical identity and free energy.ger(translated).ger(translated).srt` | `de` | `translations/bNB-7nQDdwM.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.de.srt` | `de` | `translations/v60cQUiu1NE.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.es.srt` | `es` | `translations/v60cQUiu1NE.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.fr.srt` | `fr` | `translations/v60cQUiu1NE.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.it.srt` | `it` | `translations/v60cQUiu1NE.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.ja.srt` | `ja` | `translations/v60cQUiu1NE.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.ko.srt` | `ko` | `translations/v60cQUiu1NE.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.nl.srt` | `nl` | `translations/v60cQUiu1NE.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.pt.srt` | `pt` | `translations/v60cQUiu1NE.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.ru.srt` | `ru` | `translations/v60cQUiu1NE.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.zh-Hans.srt` | `zh-Hans` | `translations/v60cQUiu1NE.zh-Hans.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.1 ~ Psychophysical identity and free energy.zh-Hant.srt` | `zh-Hant` | `translations/v60cQUiu1NE.zh-Hant.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.de.srt` | `de` | `translations/wiUDw6vk644.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.es.srt` | `es` | `translations/wiUDw6vk644.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.fr.srt` | `fr` | `translations/wiUDw6vk644.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.it.srt` | `it` | `translations/wiUDw6vk644.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.ja.srt` | `ja` | `translations/wiUDw6vk644.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.ko.srt` | `ko` | `translations/wiUDw6vk644.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.nl.srt` | `nl` | `translations/wiUDw6vk644.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.pt.srt` | `pt` | `translations/wiUDw6vk644.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.ru.srt` | `ru` | `translations/wiUDw6vk644.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.zh-Hans.srt` | `zh-Hans` | `translations/wiUDw6vk644.zh-Hans.srt` | yes (episode token) |  |
| `ActInfLab Livestream #022.2 ~ Psychophysical identity and free energy.zh-Hant.srt` | `zh-Hant` | `translations/wiUDw6vk644.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_023`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.de.srt` | `de` | `translations/8JrGE02KzuY.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.es.srt` | `es` | `translations/8JrGE02KzuY.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.fr.srt` | `fr` | `translations/8JrGE02KzuY.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.it.srt` | `it` | `translations/8JrGE02KzuY.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.ja.srt` | `ja` | `translations/8JrGE02KzuY.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.ko.srt` | `ko` | `translations/8JrGE02KzuY.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.nl.srt` | `nl` | `translations/8JrGE02KzuY.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.pt.srt` | `pt` | `translations/8JrGE02KzuY.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.ru.srt` | `ru` | `translations/8JrGE02KzuY.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.zh-Hans.srt` | `zh-Hans` | `translations/8JrGE02KzuY.zh-Hans.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.0 ~  Embodied skillful performance where the action is.zh-Hant.srt` | `zh-Hant` | `translations/8JrGE02KzuY.zh-Hant.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.1 ~   Embodied skillful performance where the action is.ger(translated).ger(translated).srt` | `de` | `translations/PgzQrHSu1CU.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/bjYUbKlfHUo.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/bjYUbKlfHUo.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.dut(translated).dut(translated).srt` | `nl` | `translations/bjYUbKlfHUo.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.fre(translated).fre(translated).srt` | `fr` | `translations/bjYUbKlfHUo.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.ger(translated).ger(translated).srt` | `de` | `translations/bjYUbKlfHUo.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.ita(translated).ita(translated).srt` | `it` | `translations/bjYUbKlfHUo.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.jpn(translated).jpn(translated).srt` | `ja` | `translations/bjYUbKlfHUo.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.kor(translated).kor(translated).srt` | `ko` | `translations/bjYUbKlfHUo.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.por(translated).por(translated).srt` | `pt` | `translations/bjYUbKlfHUo.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.rus(translated).rus(translated).srt` | `ru` | `translations/bjYUbKlfHUo.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.spa(translated).spa(translated).srt` | `es` | `translations/bjYUbKlfHUo.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_024`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/Fx7xWUU1MlI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/Fx7xWUU1MlI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.dut(translated).dut(translated).srt` | `nl` | `translations/Fx7xWUU1MlI.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.fre(translated).fre(translated).srt` | `fr` | `translations/Fx7xWUU1MlI.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.ger(translated).ger(translated).srt` | `de` | `translations/Fx7xWUU1MlI.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.ita(translated).ita(translated).srt` | `it` | `translations/Fx7xWUU1MlI.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.jpn(translated).jpn(translated).srt` | `ja` | `translations/Fx7xWUU1MlI.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.kor(translated).kor(translated).srt` | `ko` | `translations/Fx7xWUU1MlI.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.por(translated).por(translated).srt` | `pt` | `translations/Fx7xWUU1MlI.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.rus(translated).rus(translated).srt` | `ru` | `translations/Fx7xWUU1MlI.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.spa(translated).spa(translated).srt` | `es` | `translations/Fx7xWUU1MlI.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/a089q9RaI14.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/a089q9RaI14.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.dut(translated).dut(translated).srt` | `nl` | `translations/a089q9RaI14.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.fre(translated).fre(translated).srt` | `fr` | `translations/a089q9RaI14.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.ger(translated).ger(translated).srt` | `de` | `translations/a089q9RaI14.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.ita(translated).ita(translated).srt` | `it` | `translations/a089q9RaI14.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.jpn(translated).jpn(translated).srt` | `ja` | `translations/a089q9RaI14.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.kor(translated).kor(translated).srt` | `ko` | `translations/a089q9RaI14.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.por(translated).por(translated).srt` | `pt` | `translations/a089q9RaI14.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.rus(translated).rus(translated).srt` | `ru` | `translations/a089q9RaI14.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.spa(translated).spa(translated).srt` | `es` | `translations/a089q9RaI14.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/lqxl8w_JGek.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/lqxl8w_JGek.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.dut(translated).dut(translated).srt` | `nl` | `translations/lqxl8w_JGek.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.fre(translated).fre(translated).srt` | `fr` | `translations/lqxl8w_JGek.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.ger(translated).ger(translated).srt` | `de` | `translations/lqxl8w_JGek.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.ita(translated).ita(translated).srt` | `it` | `translations/lqxl8w_JGek.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.jpn(translated).jpn(translated).srt` | `ja` | `translations/lqxl8w_JGek.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.kor(translated).kor(translated).srt` | `ko` | `translations/lqxl8w_JGek.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.por(translated).por(translated).srt` | `pt` | `translations/lqxl8w_JGek.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.rus(translated).rus(translated).srt` | `ru` | `translations/lqxl8w_JGek.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.spa(translated).spa(translated).srt` | `es` | `translations/lqxl8w_JGek.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_025`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #025.0 ~  The Computational Boundary of a Self.ger(translated).ger(translated).srt` | `de` | `translations/4JfGs_m5QHo.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.0 ~  The Computational Boundary of a Self.spa(translated).spa(translated).srt` | `es` | `translations/4JfGs_m5QHo.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/v0oJvbVuAF0.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/v0oJvbVuAF0.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.dut(translated).dut(translated).srt` | `nl` | `translations/v0oJvbVuAF0.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.fre(translated).fre(translated).srt` | `fr` | `translations/v0oJvbVuAF0.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.ger(translated).ger(translated).srt` | `de` | `translations/v0oJvbVuAF0.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.ita(translated).ita(translated).srt` | `it` | `translations/v0oJvbVuAF0.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.jpn(translated).jpn(translated).srt` | `ja` | `translations/v0oJvbVuAF0.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.kor(translated).kor(translated).srt` | `ko` | `translations/v0oJvbVuAF0.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.por(translated).por(translated).srt` | `pt` | `translations/v0oJvbVuAF0.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.rus(translated).rus(translated).srt` | `ru` | `translations/v0oJvbVuAF0.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.spa(translated).spa(translated).srt` | `es` | `translations/v0oJvbVuAF0.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.2  ~  The Computational Boundary of a Self.ger(translated).ger(translated).srt` | `de` | `translations/XSYxOt8CRDI.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #025.2  ~  The Computational Boundary of a Self.kor(translated).kor(translated).srt` | `ko` | `translations/XSYxOt8CRDI.ko.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_026`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.de.srt` | `de` | `translations/eZlG_J7sPj4.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.es.srt` | `es` | `translations/eZlG_J7sPj4.es.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.fr.srt` | `fr` | `translations/eZlG_J7sPj4.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.it.srt` | `it` | `translations/eZlG_J7sPj4.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.ja.srt` | `ja` | `translations/eZlG_J7sPj4.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.ko.srt` | `ko` | `translations/eZlG_J7sPj4.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.nl.srt` | `nl` | `translations/eZlG_J7sPj4.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.pt.srt` | `pt` | `translations/eZlG_J7sPj4.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.ru.srt` | `ru` | `translations/eZlG_J7sPj4.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.zh-Hans.srt` | `zh-Hans` | `translations/eZlG_J7sPj4.zh-Hans.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.0 ~ “Bayesian Mechanics for Stationary Processes”.zh-Hant.srt` | `zh-Hant` | `translations/eZlG_J7sPj4.zh-Hant.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/1rHz3Ir5v9c.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/1rHz3Ir5v9c.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.dut(translated).dut(translated).srt` | `nl` | `translations/1rHz3Ir5v9c.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.fre(translated).fre(translated).srt` | `fr` | `translations/1rHz3Ir5v9c.fr.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.ger(translated).ger(translated).srt` | `de` | `translations/1rHz3Ir5v9c.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.ita(translated).ita(translated).srt` | `it` | `translations/1rHz3Ir5v9c.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.jpn(translated).jpn(translated).srt` | `ja` | `translations/1rHz3Ir5v9c.ja.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.kor(translated).kor(translated).srt` | `ko` | `translations/1rHz3Ir5v9c.ko.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.por(translated).por(translated).srt` | `pt` | `translations/1rHz3Ir5v9c.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.rus(translated).rus(translated).srt` | `ru` | `translations/1rHz3Ir5v9c.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.spa(translated).spa(translated).srt` | `es` | `translations/1rHz3Ir5v9c.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_027`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #027.0 ~ “Active Inference Applicability to Different Types of ....dut(translated).dut(translated).srt` | `nl` | `translations/qw0SkhnHWWI.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #027.0 ~ “Active Inference Applicability to Different Types of ....ger(translated).ger(translated).srt` | `de` | `translations/qw0SkhnHWWI.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #027.0 ~ “Active Inference Applicability to Different Types of ....ita(translated).ita(translated).srt` | `it` | `translations/qw0SkhnHWWI.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #027.0 ~ “Active Inference Applicability to Different Types of ....rus(translated).rus(translated).srt` | `ru` | `translations/qw0SkhnHWWI.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #027.1 ~ “Active Inference Applicability to Different Types of ....dut(translated).dut(translated).srt` | `nl` | `translations/Oq2oM55OKzE.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #027.1 ~ “Active Inference Applicability to Different Types of ....ger(translated).ger(translated).srt` | `de` | `translations/Oq2oM55OKzE.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #027.1 ~ “Active Inference Applicability to Different Types of ....ita(translated).ita(translated).srt` | `it` | `translations/Oq2oM55OKzE.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #027.1 ~ “Active Inference Applicability to Different Types of ....rus(translated).rus(translated).srt` | `ru` | `translations/Oq2oM55OKzE.ru.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_028`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream #028.0 ~ “Towards a computational phenomenology of mental action.dut(translated).dut(translated).srt` | `nl` | `translations/sjdjRJMRVfw.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.0 ~ “Towards a computational phenomenology of mental action.eng(transcribed).eng(transcribed).srt` | `en` | `translations/sjdjRJMRVfw.en.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInfLab Livestream #028.0 ~ “Towards a computational phenomenology of mental action.ger(translated).ger(translated).srt` | `de` | `translations/sjdjRJMRVfw.de.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.0 ~ “Towards a computational phenomenology of mental action.ita(translated).ita(translated).srt` | `it` | `translations/sjdjRJMRVfw.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.0 ~ “Towards a computational phenomenology of mental action.por(translated).por(translated).srt` | `pt` | `translations/sjdjRJMRVfw.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.0 ~ “Towards a computational phenomenology of mental action.rus(translated).rus(translated).srt` | `ru` | `translations/sjdjRJMRVfw.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.1 ~ “Towards a computational phenomenology of mental action.dut(translated).dut(translated).srt` | `nl` | `translations/eX5jt3HP27c.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.1 ~ “Towards a computational phenomenology of mental action.ita(translated).ita(translated).srt` | `it` | `translations/eX5jt3HP27c.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.1 ~ “Towards a computational phenomenology of mental action.por(translated).por(translated).srt` | `pt` | `translations/eX5jt3HP27c.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.1 ~ “Towards a computational phenomenology of mental action.rus(translated).rus(translated).srt` | `ru` | `translations/eX5jt3HP27c.ru.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.2 ~ “Towards a computational phenomenology of mental action.dut(translated).dut(translated).srt` | `nl` | `translations/sEyNwzUuiII.nl.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.2 ~ “Towards a computational phenomenology of mental action.ita(translated).ita(translated).srt` | `it` | `translations/sEyNwzUuiII.it.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.2 ~ “Towards a computational phenomenology of mental action.por(translated).por(translated).srt` | `pt` | `translations/sEyNwzUuiII.pt.srt` | yes (episode token) |  |
| `ActInfLab Livestream #028.2 ~ “Towards a computational phenomenology of mental action.rus(translated).rus(translated).srt` | `ru` | `translations/sEyNwzUuiII.ru.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_029`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/SNbfAkOokAI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/SNbfAkOokAI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.dut(translated).dut(translated).srt` | `nl` | `translations/SNbfAkOokAI.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.eng(transcribed).eng(transcribed).srt` | `en` | `translations/SNbfAkOokAI.en.srt` | yes (episode token) | base eng(transcribed) — transcription not translation |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.fre(translated).fre(translated).srt` | `fr` | `translations/SNbfAkOokAI.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.ger(translated).ger(translated).srt` | `de` | `translations/SNbfAkOokAI.de.srt` | yes (episode token) |  |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.ita(translated).ita(translated).srt` | `it` | `translations/SNbfAkOokAI.it.srt` | yes (episode token) |  |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.jpn(translated).jpn(translated).srt` | `ja` | `translations/SNbfAkOokAI.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.kor(translated).kor(translated).srt` | `ko` | `translations/SNbfAkOokAI.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.por(translated).por(translated).srt` | `pt` | `translations/SNbfAkOokAI.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.rus(translated).rus(translated).srt` | `ru` | `translations/SNbfAkOokAI.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.spa(translated).spa(translated).srt` | `es` | `translations/SNbfAkOokAI.es.srt` | yes (episode token) |  |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/Z0fpX5Lpp0Y.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/Z0fpX5Lpp0Y.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.dut(translated).dut(translated).srt` | `nl` | `translations/Z0fpX5Lpp0Y.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.fre(translated).fre(translated).srt` | `fr` | `translations/Z0fpX5Lpp0Y.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.ger(translated).ger(translated).srt` | `de` | `translations/Z0fpX5Lpp0Y.de.srt` | yes (episode token) |  |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.ita(translated).ita(translated).srt` | `it` | `translations/Z0fpX5Lpp0Y.it.srt` | yes (episode token) |  |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.jpn(translated).jpn(translated).srt` | `ja` | `translations/Z0fpX5Lpp0Y.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.kor(translated).kor(translated).srt` | `ko` | `translations/Z0fpX5Lpp0Y.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.por(translated).por(translated).srt` | `pt` | `translations/Z0fpX5Lpp0Y.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.rus(translated).rus(translated).srt` | `ru` | `translations/Z0fpX5Lpp0Y.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.spa(translated).spa(translated).srt` | `es` | `translations/Z0fpX5Lpp0Y.es.srt` | yes (episode token) |  |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/Z4S5JVoeGBw.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/Z4S5JVoeGBw.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.dut(translated).dut(translated).srt` | `nl` | `translations/Z4S5JVoeGBw.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.fre(translated).fre(translated).srt` | `fr` | `translations/Z4S5JVoeGBw.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.ger(translated).ger(translated).srt` | `de` | `translations/Z4S5JVoeGBw.de.srt` | yes (episode token) |  |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.ita(translated).ita(translated).srt` | `it` | `translations/Z4S5JVoeGBw.it.srt` | yes (episode token) |  |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.jpn(translated).jpn(translated).srt` | `ja` | `translations/Z4S5JVoeGBw.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.kor(translated).kor(translated).srt` | `ko` | `translations/Z4S5JVoeGBw.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.por(translated).por(translated).srt` | `pt` | `translations/Z4S5JVoeGBw.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.rus(translated).rus(translated).srt` | `ru` | `translations/Z4S5JVoeGBw.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.spa(translated).spa(translated).srt` | `es` | `translations/Z4S5JVoeGBw.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_030`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/N3WUpVH8-D8.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated).chi(translated).srt` | `zh-Hans` | `translations/N3WUpVH8-D8.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....dut(translated).dut(translated).srt` | `nl` | `translations/N3WUpVH8-D8.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....fre(translated).fre(translated).srt` | `fr` | `translations/N3WUpVH8-D8.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....ger(translated).ger(translated).srt` | `de` | `translations/N3WUpVH8-D8.de.srt` | yes (episode token) |  |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....ita(translated).ita(translated).srt` | `it` | `translations/N3WUpVH8-D8.it.srt` | yes (episode token) |  |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....jpn(translated).jpn(translated).srt` | `ja` | `translations/N3WUpVH8-D8.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....kor(translated).kor(translated).srt` | `ko` | `translations/N3WUpVH8-D8.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....por(translated).por(translated).srt` | `pt` | `translations/N3WUpVH8-D8.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....rus(translated).rus(translated).srt` | `ru` | `translations/N3WUpVH8-D8.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....spa(translated).spa(translated).srt` | `es` | `translations/N3WUpVH8-D8.es.srt` | yes (episode token) |  |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/5H164LqEwiA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated).chi(translated).srt` | `zh-Hans` | `translations/5H164LqEwiA.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....dut(translated).dut(translated).srt` | `nl` | `translations/5H164LqEwiA.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....fre(translated).fre(translated).srt` | `fr` | `translations/5H164LqEwiA.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....ger(translated).ger(translated).srt` | `de` | `translations/5H164LqEwiA.de.srt` | yes (episode token) |  |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....ita(translated).ita(translated).srt` | `it` | `translations/5H164LqEwiA.it.srt` | yes (episode token) |  |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....jpn(translated).jpn(translated).srt` | `ja` | `translations/5H164LqEwiA.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....kor(translated).kor(translated).srt` | `ko` | `translations/5H164LqEwiA.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....por(translated).por(translated).srt` | `pt` | `translations/5H164LqEwiA.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....rus(translated).rus(translated).srt` | `ru` | `translations/5H164LqEwiA.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....spa(translated).spa(translated).srt` | `es` | `translations/5H164LqEwiA.es.srt` | yes (episode token) |  |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/VXLNOfkH5Rg.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated).chi(translated).srt` | `zh-Hans` | `translations/VXLNOfkH5Rg.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....dut(translated).dut(translated).srt` | `nl` | `translations/VXLNOfkH5Rg.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....fre(translated).fre(translated).srt` | `fr` | `translations/VXLNOfkH5Rg.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....ger(translated).ger(translated).srt` | `de` | `translations/VXLNOfkH5Rg.de.srt` | yes (episode token) |  |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....ita(translated).ita(translated).srt` | `it` | `translations/VXLNOfkH5Rg.it.srt` | yes (episode token) |  |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....jpn(translated).jpn(translated).srt` | `ja` | `translations/VXLNOfkH5Rg.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....kor(translated).kor(translated).srt` | `ko` | `translations/VXLNOfkH5Rg.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....por(translated).por(translated).srt` | `pt` | `translations/VXLNOfkH5Rg.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....rus(translated).rus(translated).srt` | `ru` | `translations/VXLNOfkH5Rg.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....spa(translated).spa(translated).srt` | `es` | `translations/VXLNOfkH5Rg.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_032`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_035`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.de.srt` | `de` | `translations/e-Ck8sxCME0.de.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.es.srt` | `es` | `translations/e-Ck8sxCME0.es.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.fr.srt` | `fr` | `translations/e-Ck8sxCME0.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.it.srt` | `it` | `translations/e-Ck8sxCME0.it.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.ja.srt` | `ja` | `translations/e-Ck8sxCME0.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.ko.srt` | `ko` | `translations/e-Ck8sxCME0.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.nl.srt` | `nl` | `translations/e-Ck8sxCME0.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.pt.srt` | `pt` | `translations/e-Ck8sxCME0.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.ru.srt` | `ru` | `translations/e-Ck8sxCME0.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.zh-Hans.srt` | `zh-Hans` | `translations/e-Ck8sxCME0.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #035.0 ~  A tale of two architectures free energy, its models, and modularity.zh-Hant.srt` | `zh-Hant` | `translations/e-Ck8sxCME0.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.de.srt` | `de` | `translations/RoMCBXy-7E0.de.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.fr.srt` | `fr` | `translations/RoMCBXy-7E0.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.it.srt` | `it` | `translations/RoMCBXy-7E0.it.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.ja.srt` | `ja` | `translations/RoMCBXy-7E0.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.ko.srt` | `ko` | `translations/RoMCBXy-7E0.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.nl.srt` | `nl` | `translations/RoMCBXy-7E0.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.pt.srt` | `pt` | `translations/RoMCBXy-7E0.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.ru.srt` | `ru` | `translations/RoMCBXy-7E0.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.zh-Hans.srt` | `zh-Hans` | `translations/RoMCBXy-7E0.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #035.1 ~  A tale of two architectures free energy, its models, and modularity.zh-Hant.srt` | `zh-Hant` | `translations/RoMCBXy-7E0.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.de.srt` | `de` | `translations/sQWSkDQvnqk.de.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.es.srt` | `es` | `translations/sQWSkDQvnqk.es.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.fr.srt` | `fr` | `translations/sQWSkDQvnqk.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.it.srt` | `it` | `translations/sQWSkDQvnqk.it.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.ja.srt` | `ja` | `translations/sQWSkDQvnqk.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.ko.srt` | `ko` | `translations/sQWSkDQvnqk.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.nl.srt` | `nl` | `translations/sQWSkDQvnqk.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.pt.srt` | `pt` | `translations/sQWSkDQvnqk.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.ru.srt` | `ru` | `translations/sQWSkDQvnqk.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.zh-Hans.srt` | `zh-Hans` | `translations/sQWSkDQvnqk.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #035.2 ~  A tale of two architectures free energy, its models, and modularity.zh-Hant.srt` | `zh-Hant` | `translations/sQWSkDQvnqk.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_036`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.de.srt` | `de` | `translations/99xQbWozPjc.de.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.es.srt` | `es` | `translations/99xQbWozPjc.es.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.fr.srt` | `fr` | `translations/99xQbWozPjc.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.it.srt` | `it` | `translations/99xQbWozPjc.it.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.ja.srt` | `ja` | `translations/99xQbWozPjc.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.ko.srt` | `ko` | `translations/99xQbWozPjc.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.nl.srt` | `nl` | `translations/99xQbWozPjc.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.pt.srt` | `pt` | `translations/99xQbWozPjc.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.ru.srt` | `ru` | `translations/99xQbWozPjc.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.zh-Hans.srt` | `zh-Hans` | `translations/99xQbWozPjc.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #036.0 ~  Modelling ourselves - What the free energy principle reveals.zh-Hant.srt` | `zh-Hant` | `translations/99xQbWozPjc.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......es.srt` | `es` | `translations/YKn2njZ_ICg.es.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......fr.srt` | `fr` | `translations/YKn2njZ_ICg.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......it.srt` | `it` | `translations/YKn2njZ_ICg.it.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......ja.srt` | `ja` | `translations/YKn2njZ_ICg.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......ko.srt` | `ko` | `translations/YKn2njZ_ICg.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......nl.srt` | `nl` | `translations/YKn2njZ_ICg.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......pt.srt` | `pt` | `translations/YKn2njZ_ICg.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......ru.srt` | `ru` | `translations/YKn2njZ_ICg.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......zh-Hans.srt` | `zh-Hans` | `translations/YKn2njZ_ICg.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #036.1 ~  Modelling ourselves what the free energy principle reveals.......zh-Hant.srt` | `zh-Hant` | `translations/YKn2njZ_ICg.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......de.srt` | `de` | `translations/Lo95GakwV5w.de.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......es.srt` | `es` | `translations/Lo95GakwV5w.es.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......fr.srt` | `fr` | `translations/Lo95GakwV5w.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......it.srt` | `it` | `translations/Lo95GakwV5w.it.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......ja.srt` | `ja` | `translations/Lo95GakwV5w.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......ko.srt` | `ko` | `translations/Lo95GakwV5w.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......nl.srt` | `nl` | `translations/Lo95GakwV5w.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......pt.srt` | `pt` | `translations/Lo95GakwV5w.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......ru.srt` | `ru` | `translations/Lo95GakwV5w.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......zh-Hans.srt` | `zh-Hans` | `translations/Lo95GakwV5w.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #036.2 ~  Modelling ourselves what the free energy principle reveals.......zh-Hant.srt` | `zh-Hant` | `translations/Lo95GakwV5w.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_037`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.de.srt` | `de` | `translations/chpbMBgDR84.de.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.es.srt` | `es` | `translations/chpbMBgDR84.es.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.fr.srt` | `fr` | `translations/chpbMBgDR84.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.it.srt` | `it` | `translations/chpbMBgDR84.it.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.ja.srt` | `ja` | `translations/chpbMBgDR84.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.ko.srt` | `ko` | `translations/chpbMBgDR84.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.nl.srt` | `nl` | `translations/chpbMBgDR84.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.pt.srt` | `pt` | `translations/chpbMBgDR84.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.ru.srt` | `ru` | `translations/chpbMBgDR84.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.zh-Hans.srt` | `zh-Hans` | `translations/chpbMBgDR84.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #037.0 ~  Free Energy A User's Guide.zh-Hant.srt` | `zh-Hant` | `translations/chpbMBgDR84.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #037.1 ~  Free Energy A User's Guide.de.srt` | `de` | `translations/GHcpJ_bMuu4.de.srt` | yes (episode token) |  |
| `ActInf Livestream #037.1 ~  Free Energy A User's Guide.es.srt` | `es` | `translations/GHcpJ_bMuu4.es.srt` | yes (episode token) |  |
| `ActInf Livestream #037.1 ~  Free Energy A User's Guide.fr.srt` | `fr` | `translations/GHcpJ_bMuu4.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #037.1 ~  Free Energy A User's Guide.it.srt` | `it` | `translations/GHcpJ_bMuu4.it.srt` | yes (episode token) |  |
| `ActInf Livestream #037.1 ~  Free Energy A User's Guide.ja.srt` | `ja` | `translations/GHcpJ_bMuu4.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #037.1 ~  Free Energy A User's Guide.ko.srt` | `ko` | `translations/GHcpJ_bMuu4.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #037.1 ~  Free Energy A User's Guide.nl.srt` | `nl` | `translations/GHcpJ_bMuu4.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #037.1 ~  Free Energy A User's Guide.pt.srt` | `pt` | `translations/GHcpJ_bMuu4.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.de.srt` | `de` | `translations/6WP7mY13lzc.de.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.es.srt` | `es` | `translations/6WP7mY13lzc.es.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.fr.srt` | `fr` | `translations/6WP7mY13lzc.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.it.srt` | `it` | `translations/6WP7mY13lzc.it.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.ja.srt` | `ja` | `translations/6WP7mY13lzc.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.ko.srt` | `ko` | `translations/6WP7mY13lzc.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.nl.srt` | `nl` | `translations/6WP7mY13lzc.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.pt.srt` | `pt` | `translations/6WP7mY13lzc.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.ru.srt` | `ru` | `translations/6WP7mY13lzc.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.zh-Hans.srt` | `zh-Hans` | `translations/6WP7mY13lzc.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #037.2 ~  Free Energy A User's Guide.zh-Hant.srt` | `zh-Hant` | `translations/6WP7mY13lzc.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_038`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.de.srt` | `de` | `translations/0OQx04x8-zA.de.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.es.srt` | `es` | `translations/0OQx04x8-zA.es.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.fr.srt` | `fr` | `translations/0OQx04x8-zA.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.it.srt` | `it` | `translations/0OQx04x8-zA.it.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.ja.srt` | `ja` | `translations/0OQx04x8-zA.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.ko.srt` | `ko` | `translations/0OQx04x8-zA.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.nl.srt` | `nl` | `translations/0OQx04x8-zA.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.pt.srt` | `pt` | `translations/0OQx04x8-zA.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.ru.srt` | `ru` | `translations/0OQx04x8-zA.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.zh-Hans.srt` | `zh-Hans` | `translations/0OQx04x8-zA.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #038.2 ~  The evolution of brain architectures for predictive coding and ActInf.zh-Hant.srt` | `zh-Hant` | `translations/0OQx04x8-zA.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_039`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.de.srt` | `de` | `translations/yC-hgjv3ANk.de.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.es.srt` | `es` | `translations/yC-hgjv3ANk.es.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.fr.srt` | `fr` | `translations/yC-hgjv3ANk.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.it.srt` | `it` | `translations/yC-hgjv3ANk.it.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.ja.srt` | `ja` | `translations/yC-hgjv3ANk.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.ko.srt` | `ko` | `translations/yC-hgjv3ANk.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.nl.srt` | `nl` | `translations/yC-hgjv3ANk.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.pt.srt` | `pt` | `translations/yC-hgjv3ANk.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.ru.srt` | `ru` | `translations/yC-hgjv3ANk.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.zh-Hans.srt` | `zh-Hans` | `translations/yC-hgjv3ANk.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #039.0 ~  Morphogenesis as Bayesian inference.zh-Hant.srt` | `zh-Hant` | `translations/yC-hgjv3ANk.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_040`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/Cgo-0UU848M.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/Cgo-0UU848M.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.dut(translated).dut(translated).srt` | `nl` | `translations/Cgo-0UU848M.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.fre(translated).fre(translated).srt` | `fr` | `translations/Cgo-0UU848M.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.ger(translated).ger(translated).srt` | `de` | `translations/Cgo-0UU848M.de.srt` | yes (episode token) |  |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.ita(translated).ita(translated).srt` | `it` | `translations/Cgo-0UU848M.it.srt` | yes (episode token) |  |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.jpn(translated).jpn(translated).srt` | `ja` | `translations/Cgo-0UU848M.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.kor(translated).kor(translated).srt` | `ko` | `translations/Cgo-0UU848M.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.por(translated).por(translated).srt` | `pt` | `translations/Cgo-0UU848M.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.rus(translated).rus(translated).srt` | `ru` | `translations/Cgo-0UU848M.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.spa(translated).spa(translated).srt` | `es` | `translations/Cgo-0UU848M.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_041`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.de.srt` | `de` | `translations/VsOqIxNYpPQ.de.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.es.srt` | `es` | `translations/VsOqIxNYpPQ.es.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.fr.srt` | `fr` | `translations/VsOqIxNYpPQ.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.it.srt` | `it` | `translations/VsOqIxNYpPQ.it.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.ja.srt` | `ja` | `translations/VsOqIxNYpPQ.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.ko.srt` | `ko` | `translations/VsOqIxNYpPQ.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.nl.srt` | `nl` | `translations/VsOqIxNYpPQ.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.pt.srt` | `pt` | `translations/VsOqIxNYpPQ.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.ru.srt` | `ru` | `translations/VsOqIxNYpPQ.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.zh-Hans.srt` | `zh-Hans` | `translations/VsOqIxNYpPQ.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #041.0, Extended active inference Constructing predictive cognition beyond skulls.zh-Hant.srt` | `zh-Hant` | `translations/VsOqIxNYpPQ.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.de.srt` | `de` | `translations/H6rjjPZE5hs.de.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.es.srt` | `es` | `translations/H6rjjPZE5hs.es.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.fr.srt` | `fr` | `translations/H6rjjPZE5hs.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.it.srt` | `it` | `translations/H6rjjPZE5hs.it.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.ja.srt` | `ja` | `translations/H6rjjPZE5hs.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.ko.srt` | `ko` | `translations/H6rjjPZE5hs.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.nl.srt` | `nl` | `translations/H6rjjPZE5hs.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.pt.srt` | `pt` | `translations/H6rjjPZE5hs.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.ru.srt` | `ru` | `translations/H6rjjPZE5hs.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.zh-Hans.srt` | `zh-Hans` | `translations/H6rjjPZE5hs.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #041.1, Extended active inference Constructing predictive cognition beyond skulls.zh-Hant.srt` | `zh-Hant` | `translations/H6rjjPZE5hs.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.de.srt` | `de` | `translations/RB2axUYnE8I.de.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.es.srt` | `es` | `translations/RB2axUYnE8I.es.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.fr.srt` | `fr` | `translations/RB2axUYnE8I.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.it.srt` | `it` | `translations/RB2axUYnE8I.it.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.ja.srt` | `ja` | `translations/RB2axUYnE8I.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.ko.srt` | `ko` | `translations/RB2axUYnE8I.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.nl.srt` | `nl` | `translations/RB2axUYnE8I.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.pt.srt` | `pt` | `translations/RB2axUYnE8I.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.ru.srt` | `ru` | `translations/RB2axUYnE8I.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.zh-Hans.srt` | `zh-Hans` | `translations/RB2axUYnE8I.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #041.2, Extended active inference Constructing predictive cognition beyond skulls.zh-Hant.srt` | `zh-Hant` | `translations/RB2axUYnE8I.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_042`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #042.0 ~  Robot navigation as hierarchical active inference.de.srt` | `de` | `translations/Dl6v-3COgCo.de.srt` | yes (episode token) |  |
| `ActInf Livestream #042.0 ~  Robot navigation as hierarchical active inference.es.srt` | `es` | `translations/Dl6v-3COgCo.es.srt` | yes (episode token) |  |
| `ActInf Livestream #042.0 ~  Robot navigation as hierarchical active inference.fr.srt` | `fr` | `translations/Dl6v-3COgCo.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #042.0 ~  Robot navigation as hierarchical active inference.it.srt` | `it` | `translations/Dl6v-3COgCo.it.srt` | yes (episode token) |  |
| `ActInf Livestream #042.0 ~  Robot navigation as hierarchical active inference.nl.srt` | `nl` | `translations/Dl6v-3COgCo.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #042.0 ~  Robot navigation as hierarchical active inference.pt.srt` | `pt` | `translations/Dl6v-3COgCo.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #042.1 ~  Robot navigation as hierarchical active inference.de.srt` | `de` | `translations/UUQIVqcI-yw.de.srt` | yes (episode token) |  |
| `ActInf Livestream #042.1 ~  Robot navigation as hierarchical active inference.es.srt` | `es` | `translations/UUQIVqcI-yw.es.srt` | yes (episode token) |  |
| `ActInf Livestream #042.1 ~  Robot navigation as hierarchical active inference.fr.srt` | `fr` | `translations/UUQIVqcI-yw.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #042.1 ~  Robot navigation as hierarchical active inference.it.srt` | `it` | `translations/UUQIVqcI-yw.it.srt` | yes (episode token) |  |
| `ActInf Livestream #042.1 ~  Robot navigation as hierarchical active inference.nl.srt` | `nl` | `translations/UUQIVqcI-yw.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #042.1 ~  Robot navigation as hierarchical active inference.pt.srt` | `pt` | `translations/UUQIVqcI-yw.pt.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_043`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #043.0 ~  Predictive Coding a Theoretical and Experimental Review.de.srt` | `de` | `translations/cLe-rBtRXiQ.de.srt` | yes (episode token) |  |
| `ActInf Livestream #043.0 ~  Predictive Coding a Theoretical and Experimental Review.es.srt` | `es` | `translations/cLe-rBtRXiQ.es.srt` | yes (episode token) |  |
| `ActInf Livestream #043.0 ~  Predictive Coding a Theoretical and Experimental Review.fr.srt` | `fr` | `translations/cLe-rBtRXiQ.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #043.0 ~  Predictive Coding a Theoretical and Experimental Review.it.srt` | `it` | `translations/cLe-rBtRXiQ.it.srt` | yes (episode token) |  |
| `ActInf Livestream #043.0 ~  Predictive Coding a Theoretical and Experimental Review.nl.srt` | `nl` | `translations/cLe-rBtRXiQ.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #043.0 ~  Predictive Coding a Theoretical and Experimental Review.pt.srt` | `pt` | `translations/cLe-rBtRXiQ.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #043.1 ~  Predictive Coding a Theoretical and Experimental Review.de.srt` | `de` | `translations/O4u8PRzk1vY.de.srt` | yes (episode token) |  |
| `ActInf Livestream #043.1 ~  Predictive Coding a Theoretical and Experimental Review.es.srt` | `es` | `translations/O4u8PRzk1vY.es.srt` | yes (episode token) |  |
| `ActInf Livestream #043.1 ~  Predictive Coding a Theoretical and Experimental Review.fr.srt` | `fr` | `translations/O4u8PRzk1vY.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #043.1 ~  Predictive Coding a Theoretical and Experimental Review.it.srt` | `it` | `translations/O4u8PRzk1vY.it.srt` | yes (episode token) |  |
| `ActInf Livestream #043.1 ~  Predictive Coding a Theoretical and Experimental Review.nl.srt` | `nl` | `translations/O4u8PRzk1vY.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #043.1 ~  Predictive Coding a Theoretical and Experimental Review.pt.srt` | `pt` | `translations/O4u8PRzk1vY.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #043.2 ~  Predictive Coding a Theoretical and Experimental Review.de.srt` | `de` | `translations/X0Q6JLDYWJo.de.srt` | yes (episode token) |  |
| `ActInf Livestream #043.2 ~  Predictive Coding a Theoretical and Experimental Review.es.srt` | `es` | `translations/X0Q6JLDYWJo.es.srt` | yes (episode token) |  |
| `ActInf Livestream #043.2 ~  Predictive Coding a Theoretical and Experimental Review.fr.srt` | `fr` | `translations/X0Q6JLDYWJo.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #043.2 ~  Predictive Coding a Theoretical and Experimental Review.it.srt` | `it` | `translations/X0Q6JLDYWJo.it.srt` | yes (episode token) |  |
| `ActInf Livestream #043.2 ~  Predictive Coding a Theoretical and Experimental Review.nl.srt` | `nl` | `translations/X0Q6JLDYWJo.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #043.2 ~  Predictive Coding a Theoretical and Experimental Review.pt.srt` | `pt` | `translations/X0Q6JLDYWJo.pt.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_044`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #044.0 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch.de.srt` | `de` | `translations/yNubOHOJeIQ.de.srt` | yes (episode token) |  |
| `ActInf Livestream #044.0 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch.es.srt` | `es` | `translations/yNubOHOJeIQ.es.srt` | yes (episode token) |  |
| `ActInf Livestream #044.0 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch.fr.srt` | `fr` | `translations/yNubOHOJeIQ.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #044.0 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch.it.srt` | `it` | `translations/yNubOHOJeIQ.it.srt` | yes (episode token) |  |
| `ActInf Livestream #044.0 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch.nl.srt` | `nl` | `translations/yNubOHOJeIQ.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #044.0 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch.pt.srt` | `pt` | `translations/yNubOHOJeIQ.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #044.1 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...de.srt` | `de` | `translations/y1vtKYzVUaY.de.srt` | yes (episode token) |  |
| `ActInf Livestream #044.1 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...es.srt` | `es` | `translations/y1vtKYzVUaY.es.srt` | yes (episode token) |  |
| `ActInf Livestream #044.1 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...fr.srt` | `fr` | `translations/y1vtKYzVUaY.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #044.1 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...it.srt` | `it` | `translations/y1vtKYzVUaY.it.srt` | yes (episode token) |  |
| `ActInf Livestream #044.1 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...nl.srt` | `nl` | `translations/y1vtKYzVUaY.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #044.1 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...pt.srt` | `pt` | `translations/y1vtKYzVUaY.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #044.2 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...de.srt` | `de` | `translations/epoHxFdzFkw.de.srt` | yes (episode token) |  |
| `ActInf Livestream #044.2 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...es.srt` | `es` | `translations/epoHxFdzFkw.es.srt` | yes (episode token) |  |
| `ActInf Livestream #044.2 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...fr.srt` | `fr` | `translations/epoHxFdzFkw.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #044.2 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...it.srt` | `it` | `translations/epoHxFdzFkw.it.srt` | yes (episode token) |  |
| `ActInf Livestream #044.2 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...nl.srt` | `nl` | `translations/epoHxFdzFkw.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #044.2 ~ Therapeutic Alliance as Active Inference The Role of Therapeutic Touch...pt.srt` | `pt` | `translations/epoHxFdzFkw.pt.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_045`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/9MQQKaKEXs0.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/9MQQKaKEXs0.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.fre(translated).fre(translated).srt` | `fr` | `translations/9MQQKaKEXs0.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.ger(translated).ger(translated).srt` | `de` | `translations/9MQQKaKEXs0.de.srt` | yes (episode token) |  |
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.ita(translated).ita(translated).srt` | `it` | `translations/9MQQKaKEXs0.it.srt` | yes (episode token) |  |
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.jpn(translated).srt` | `ja` | `translations/9MQQKaKEXs0.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.kor(translated).srt` | `ko` | `translations/9MQQKaKEXs0.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.por(translated).por(translated).srt` | `pt` | `translations/9MQQKaKEXs0.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.rus(translated).rus(translated).srt` | `ru` | `translations/9MQQKaKEXs0.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.spa(translated).spa(translated).srt` | `es` | `translations/9MQQKaKEXs0.es.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.chi(translated-Simp).chi(translated).srt` | `zh-Hans` | `translations/V0l9fOJgbtc.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.chi(translated-Trad) (2).chi(translated).srt` | `zh-Hant` | `translations/V0l9fOJgbtc.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.dut(translated).dut(translated).srt` | `nl` | `translations/V0l9fOJgbtc.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.fre(translated).fre(translated).srt` | `fr` | `translations/V0l9fOJgbtc.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.ger(translated).ger(translated).srt` | `de` | `translations/V0l9fOJgbtc.de.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.ita(translated).ita(translated).srt` | `it` | `translations/V0l9fOJgbtc.it.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.jpn(translated).jpn(translated).srt` | `ja` | `translations/V0l9fOJgbtc.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.kor(translated).kor(translated).srt` | `ko` | `translations/V0l9fOJgbtc.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.por(translated).por(translated).srt` | `pt` | `translations/V0l9fOJgbtc.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.rus(translated).rus(translated).srt` | `ru` | `translations/V0l9fOJgbtc.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #045.1 ~  The free energy principle made simpler but not too simple.spa(translated).spa(translated).srt` | `es` | `translations/V0l9fOJgbtc.es.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.chi(translated-Simp).chi(translated).srt` | `zh-Hans` | `translations/S5-jXzhiG18.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.chi(translated-Trad) (2).chi(translated).srt` | `zh-Hant` | `translations/S5-jXzhiG18.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.dut(translated).dut(translated).srt` | `nl` | `translations/S5-jXzhiG18.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.fre(translated).fre(translated).srt` | `fr` | `translations/S5-jXzhiG18.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.ger(translated).ger(translated).srt` | `de` | `translations/S5-jXzhiG18.de.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.ita(translated).ita(translated).srt` | `it` | `translations/S5-jXzhiG18.it.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.jpn(translated).jpn(translated).srt` | `ja` | `translations/S5-jXzhiG18.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.kor(translated).kor(translated).srt` | `ko` | `translations/S5-jXzhiG18.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.por(translated).por(translated).srt` | `pt` | `translations/S5-jXzhiG18.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.rus(translated).rus(translated).srt` | `ru` | `translations/S5-jXzhiG18.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~  The free energy principle made simpler but not too simple.spa(translated).spa(translated).srt` | `es` | `translations/S5-jXzhiG18.es.srt` | yes (episode token) |  |
| `ActInf Livestream #045.2 ~ The free energy principle made simpler but not too simple.che(translated).srt` | `che(translated)` | — | **yes (episode token)** | unknown code che; no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_046`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/skcKoCcAQJI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/skcKoCcAQJI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.dut(translated).dut(translated).srt` | `nl` | `translations/skcKoCcAQJI.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.fre(translated).fre(translated).srt` | `fr` | `translations/skcKoCcAQJI.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.ger(translated).ger(translated).srt` | `de` | `translations/skcKoCcAQJI.de.srt` | yes (episode token) |  |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.ita(translated).ita(translated).srt` | `it` | `translations/skcKoCcAQJI.it.srt` | yes (episode token) |  |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.jpn(translated).jpn(translated).srt` | `ja` | `translations/skcKoCcAQJI.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.kor(translated).kor(translated).srt` | `ko` | `translations/skcKoCcAQJI.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.por(translated).por(translated).srt` | `pt` | `translations/skcKoCcAQJI.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.rus(translated).rus(translated).srt` | `ru` | `translations/skcKoCcAQJI.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.spa(translated).spa(translated).srt` | `es` | `translations/skcKoCcAQJI.es.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.de.srt` | `de` | `translations/JPsdk7pVa1I.de.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.es.srt` | `es` | `translations/JPsdk7pVa1I.es.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.fr.srt` | `fr` | `translations/JPsdk7pVa1I.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.it.srt` | `it` | `translations/JPsdk7pVa1I.it.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.ja.srt` | `ja` | `translations/JPsdk7pVa1I.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.ko.srt` | `ko` | `translations/JPsdk7pVa1I.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.nl.srt` | `nl` | `translations/JPsdk7pVa1I.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.pt.srt` | `pt` | `translations/JPsdk7pVa1I.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.ru.srt` | `ru` | `translations/JPsdk7pVa1I.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.zh-Hans.srt` | `zh-Hans` | `translations/JPsdk7pVa1I.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #046.1 ~  Active inference models do not contradict folk psychology.zh-Hant.srt` | `zh-Hant` | `translations/JPsdk7pVa1I.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/7_YNInrALU8.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/7_YNInrALU8.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.dut(translated).dut(translated).srt` | `nl` | `translations/7_YNInrALU8.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.fre(translated).fre(translated).srt` | `fr` | `translations/7_YNInrALU8.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.ger(translated).ger(translated).srt` | `de` | `translations/7_YNInrALU8.de.srt` | yes (episode token) |  |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.ita(translated).ita(translated).srt` | `it` | `translations/7_YNInrALU8.it.srt` | yes (episode token) |  |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.jpn(translated).jpn(translated).srt` | `ja` | `translations/7_YNInrALU8.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.kor(translated).kor(translated).srt` | `ko` | `translations/7_YNInrALU8.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.por(translated).por(translated).srt` | `pt` | `translations/7_YNInrALU8.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.rus(translated).rus(translated).srt` | `ru` | `translations/7_YNInrALU8.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.spa(translated).spa(translated).srt` | `es` | `translations/7_YNInrALU8.es.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_047`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.de.srt` | `de` | `translations/WKjqw3My_xM.de.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.es.srt` | `es` | `translations/WKjqw3My_xM.es.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.fr.srt` | `fr` | `translations/WKjqw3My_xM.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.it.srt` | `it` | `translations/WKjqw3My_xM.it.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.ja.srt` | `ja` | `translations/WKjqw3My_xM.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.ko.srt` | `ko` | `translations/WKjqw3My_xM.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.nl.srt` | `nl` | `translations/WKjqw3My_xM.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.pt.srt` | `pt` | `translations/WKjqw3My_xM.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.ru.srt` | `ru` | `translations/WKjqw3My_xM.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.zh-Hans.srt` | `zh-Hans` | `translations/WKjqw3My_xM.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #047.0 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.zh-Hant.srt` | `zh-Hant` | `translations/WKjqw3My_xM.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.de.srt` | `de` | `translations/1yYFJnf_mHY.de.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.es.srt` | `es` | `translations/1yYFJnf_mHY.es.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.fr.srt` | `fr` | `translations/1yYFJnf_mHY.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.it.srt` | `it` | `translations/1yYFJnf_mHY.it.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.ja.srt` | `ja` | `translations/1yYFJnf_mHY.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.ko.srt` | `ko` | `translations/1yYFJnf_mHY.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.nl.srt` | `nl` | `translations/1yYFJnf_mHY.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.pt.srt` | `pt` | `translations/1yYFJnf_mHY.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.ru.srt` | `ru` | `translations/1yYFJnf_mHY.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.zh-Hans.srt` | `zh-Hans` | `translations/1yYFJnf_mHY.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #047.1 ~ “Enactive-Dynamic Social Cognition  _ “Active Inference and Abduction”.zh-Hant.srt` | `zh-Hant` | `translations/1yYFJnf_mHY.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_048`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.de.srt` | `de` | `translations/zqiZjjY9H7M.de.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.es.srt` | `es` | `translations/zqiZjjY9H7M.es.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.fr.srt` | `fr` | `translations/zqiZjjY9H7M.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.it.srt` | `it` | `translations/zqiZjjY9H7M.it.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.ja.srt` | `ja` | `translations/zqiZjjY9H7M.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.ko.srt` | `ko` | `translations/zqiZjjY9H7M.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.nl.srt` | `nl` | `translations/zqiZjjY9H7M.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.pt.srt` | `pt` | `translations/zqiZjjY9H7M.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.ru.srt` | `ru` | `translations/zqiZjjY9H7M.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.zh-Hans.srt` | `zh-Hans` | `translations/zqiZjjY9H7M.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #048.0 ~  Communication as Socially Extended Active Inference.zh-Hant.srt` | `zh-Hant` | `translations/zqiZjjY9H7M.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.de.srt` | `de` | `translations/nWFM5zrdmG8.de.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.es.srt` | `es` | `translations/nWFM5zrdmG8.es.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.fr.srt` | `fr` | `translations/nWFM5zrdmG8.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.it.srt` | `it` | `translations/nWFM5zrdmG8.it.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.ja.srt` | `ja` | `translations/nWFM5zrdmG8.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.ko.srt` | `ko` | `translations/nWFM5zrdmG8.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.nl.srt` | `nl` | `translations/nWFM5zrdmG8.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.pt.srt` | `pt` | `translations/nWFM5zrdmG8.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.ru.srt` | `ru` | `translations/nWFM5zrdmG8.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.zh-Hans.srt` | `zh-Hans` | `translations/nWFM5zrdmG8.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #048.1 ~  Communication as Socially Extended Active Inference.zh-Hant.srt` | `zh-Hant` | `translations/nWFM5zrdmG8.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_049`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.de.srt` | `de` | `translations/dAtC-Enmc8M.de.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.es.srt` | `es` | `translations/dAtC-Enmc8M.es.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.fr.srt` | `fr` | `translations/dAtC-Enmc8M.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.it.srt` | `it` | `translations/dAtC-Enmc8M.it.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.ja.srt` | `ja` | `translations/dAtC-Enmc8M.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.ko.srt` | `ko` | `translations/dAtC-Enmc8M.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.nl.srt` | `nl` | `translations/dAtC-Enmc8M.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.pt.srt` | `pt` | `translations/dAtC-Enmc8M.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.ru.srt` | `ru` | `translations/dAtC-Enmc8M.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.zh-Hans.srt` | `zh-Hans` | `translations/dAtC-Enmc8M.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #049.1 ~  A Worked Example of the Bayesian Mechanics of Classical Objects.zh-Hant.srt` | `zh-Hant` | `translations/dAtC-Enmc8M.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_050`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.de.srt` | `de` | `translations/l7r0ISlr-Hc.de.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.es.srt` | `es` | `translations/l7r0ISlr-Hc.es.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.fr.srt` | `fr` | `translations/l7r0ISlr-Hc.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.it.srt` | `it` | `translations/l7r0ISlr-Hc.it.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.ja.srt` | `ja` | `translations/l7r0ISlr-Hc.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.ko.srt` | `ko` | `translations/l7r0ISlr-Hc.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.nl.srt` | `nl` | `translations/l7r0ISlr-Hc.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.pt.srt` | `pt` | `translations/l7r0ISlr-Hc.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.ru.srt` | `ru` | `translations/l7r0ISlr-Hc.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.zh-Hans.srt` | `zh-Hans` | `translations/l7r0ISlr-Hc.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #050.0~  Interoception as modeling, allostasis as control.zh-Hant.srt` | `zh-Hant` | `translations/l7r0ISlr-Hc.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.de.srt` | `de` | `translations/tGd-mgSdbio.de.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.es.srt` | `es` | `translations/tGd-mgSdbio.es.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.fr.srt` | `fr` | `translations/tGd-mgSdbio.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.it.srt` | `it` | `translations/tGd-mgSdbio.it.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.ja.srt` | `ja` | `translations/tGd-mgSdbio.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.ko.srt` | `ko` | `translations/tGd-mgSdbio.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.nl.srt` | `nl` | `translations/tGd-mgSdbio.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.pt.srt` | `pt` | `translations/tGd-mgSdbio.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.ru.srt` | `ru` | `translations/tGd-mgSdbio.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.zh-Hans.srt` | `zh-Hans` | `translations/tGd-mgSdbio.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #050.1~  Interoception as modeling, allostasis as control.zh-Hant.srt` | `zh-Hant` | `translations/tGd-mgSdbio.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.de.srt` | `de` | `translations/4o-LmkycAC0.de.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.es.srt` | `es` | `translations/4o-LmkycAC0.es.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.fr.srt` | `fr` | `translations/4o-LmkycAC0.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.it.srt` | `it` | `translations/4o-LmkycAC0.it.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.ja.srt` | `ja` | `translations/4o-LmkycAC0.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.ko.srt` | `ko` | `translations/4o-LmkycAC0.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.nl.srt` | `nl` | `translations/4o-LmkycAC0.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.pt.srt` | `pt` | `translations/4o-LmkycAC0.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.ru.srt` | `ru` | `translations/4o-LmkycAC0.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.zh-Hans.srt` | `zh-Hans` | `translations/4o-LmkycAC0.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #050.2 ~  Interoception as modeling, allostasis as control.zh-Hant.srt` | `zh-Hant` | `translations/4o-LmkycAC0.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_052`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_053`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….de.srt` | `de` | `translations/L6dhr5hUu8o.de.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….es.srt` | `es` | `translations/L6dhr5hUu8o.es.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….fr.srt` | `fr` | `translations/L6dhr5hUu8o.fr.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….it.srt` | `it` | `translations/L6dhr5hUu8o.it.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….ja.srt` | `ja` | `translations/L6dhr5hUu8o.ja.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….ko.srt` | `ko` | `translations/L6dhr5hUu8o.ko.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….nl.srt` | `nl` | `translations/L6dhr5hUu8o.nl.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….pt.srt` | `pt` | `translations/L6dhr5hUu8o.pt.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….ru.srt` | `ru` | `translations/L6dhr5hUu8o.ru.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….zh-Hans.srt` | `zh-Hans` | `translations/L6dhr5hUu8o.zh-Hans.srt` | yes (episode token) |  |
| `ActInf Livestream #053.2 ~  Snakes and Ladders in Paleoanthropology  &  To copy or not to copy….zh-Hant.srt` | `zh-Hant` | `translations/L6dhr5hUu8o.zh-Hant.srt` | yes (episode token) |  |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/Livestream/LiveStream_054`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.en(ie).srt` | `en` | — | **NO (unmatched)** | en qualifier in "en(ie)"; no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/MathStream/MathStream_001`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.chi(translated-Simp).chi(translated).srt` | `zh-Hans` | `translations/1HKjMeEGLyY.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.chi(translated-Trad) (2).chi(translated).srt` | `zh-Hant` | `translations/1HKjMeEGLyY.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.dut(translated).dut(translated).srt` | `nl` | `translations/1HKjMeEGLyY.nl.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.fre(translated).fre(translated).srt` | `fr` | `translations/1HKjMeEGLyY.fr.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.ger(translated).ger(translated).srt` | `de` | `translations/1HKjMeEGLyY.de.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.ita(translated).ita(translated).srt` | `it` | `translations/1HKjMeEGLyY.it.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.jpn(translated).jpn(translated).srt` | `ja` | `translations/1HKjMeEGLyY.ja.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.kor(translated).kor(translated).srt` | `ko` | `translations/1HKjMeEGLyY.ko.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.por(translated).por(translated).srt` | `pt` | `translations/1HKjMeEGLyY.pt.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.rus(translated).rus(translated).srt` | `ru` | `translations/1HKjMeEGLyY.ru.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.spa(translated).spa(translated).srt` | `es` | `translations/1HKjMeEGLyY.es.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.de.srt` | `de` | `translations/1HKjMeEGLyY.de.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.es.srt` | `es` | `translations/1HKjMeEGLyY.es.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.fr.srt` | `fr` | `translations/1HKjMeEGLyY.fr.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.it.srt` | `it` | `translations/1HKjMeEGLyY.it.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.ja.srt` | `ja` | `translations/1HKjMeEGLyY.ja.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.ko.srt` | `ko` | `translations/1HKjMeEGLyY.ko.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.nl.srt` | `nl` | `translations/1HKjMeEGLyY.nl.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.pt.srt` | `pt` | `translations/1HKjMeEGLyY.pt.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.ru.srt` | `ru` | `translations/1HKjMeEGLyY.ru.srt` | **assumed (sole part)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.zh-Hans.srt` | `zh-Hans` | `translations/1HKjMeEGLyY.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson Emergent Time and Chromatic Types.zh-Hant.srt` | `zh-Hant` | `translations/1HKjMeEGLyY.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/1HKjMeEGLyY.de.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/1HKjMeEGLyY.es.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/1HKjMeEGLyY.fr.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/1HKjMeEGLyY.it.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/1HKjMeEGLyY.ja.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/1HKjMeEGLyY.nl.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/1HKjMeEGLyY.pt.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/1HKjMeEGLyY.ru.srt` | **assumed (sole part)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target; stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/MathStream/MathStream_002`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab MathStream #002.1 ~ Shanna Dobson.chi(translated-Simp).chi(translated).srt` | `zh-Hans` | `translations/RQb6wLWoYok.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #002.1 ~ Shanna Dobson.chi(translated-Trad) (2).chi(translated).srt` | `zh-Hant` | `translations/RQb6wLWoYok.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #002.1 ~ Shanna Dobson.ger(translated).ger(translated).srt` | `de` | `translations/RQb6wLWoYok.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/MathStream/MathStream_003`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.chi(translated-Simp).chi(translated).srt` | `zh-Hans` | `translations/bBE2w_BpuAw.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.chi(translated-Trad) (2).chi(translated).srt` | `zh-Hant` | `translations/bBE2w_BpuAw.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.dut(translated).dut(translated).srt` | `nl` | `translations/bBE2w_BpuAw.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.fre(translated).fre(translated).srt` | `fr` | `translations/bBE2w_BpuAw.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.ger(translated).ger(translated).srt` | `de` | `translations/bBE2w_BpuAw.de.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.ita(translated).ita(translated).srt` | `it` | `translations/bBE2w_BpuAw.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.jpn(translated).jpn(translated).srt` | `ja` | `translations/bBE2w_BpuAw.ja.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.kor(translated).kor(translated).srt` | `ko` | `translations/bBE2w_BpuAw.ko.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.por(translated).por(translated).srt` | `pt` | `translations/bBE2w_BpuAw.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.rus(translated).rus(translated).srt` | `ru` | `translations/bBE2w_BpuAw.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.spa(translated).spa(translated).srt` | `es` | `translations/bBE2w_BpuAw.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/MathStream/MathStream_005`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.de.srt` | `de` | `translations/QqEp4jtaQ2E.de.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.es.srt` | `es` | `translations/QqEp4jtaQ2E.es.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.fr.srt` | `fr` | `translations/QqEp4jtaQ2E.fr.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.it.srt` | `it` | `translations/QqEp4jtaQ2E.it.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.ja.srt` | `ja` | `translations/QqEp4jtaQ2E.ja.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.ko.srt` | `ko` | `translations/QqEp4jtaQ2E.ko.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.nl.srt` | `nl` | `translations/QqEp4jtaQ2E.nl.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.pt.srt` | `pt` | `translations/QqEp4jtaQ2E.pt.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.ru.srt` | `ru` | `translations/QqEp4jtaQ2E.ru.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.zh-Hans.srt` | `zh-Hans` | `translations/QqEp4jtaQ2E.zh-Hans.srt` | yes (title exact) |  |
| `ActInf MathStream 005.1 ~ Cristian Bodnar   Topological Deep Learning Graphs, Complexes, Sheaves.zh-Hant.srt` | `zh-Hant` | `translations/QqEp4jtaQ2E.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/MathStream/MathStream_006`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.de.srt` | `de` | `translations/p1GMPGBJGfw.de.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.es.srt` | `es` | `translations/p1GMPGBJGfw.es.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.fr.srt` | `fr` | `translations/p1GMPGBJGfw.fr.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.it.srt` | `it` | `translations/p1GMPGBJGfw.it.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.ja.srt` | `ja` | `translations/p1GMPGBJGfw.ja.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.ko.srt` | `ko` | `translations/p1GMPGBJGfw.ko.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.nl.srt` | `nl` | `translations/p1GMPGBJGfw.nl.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.pt.srt` | `pt` | `translations/p1GMPGBJGfw.pt.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.ru.srt` | `ru` | `translations/p1GMPGBJGfw.ru.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.zh-Hans.srt` | `zh-Hans` | `translations/p1GMPGBJGfw.zh-Hans.srt` | yes (episode token) |  |
| `ActInf MathStream #006.1 ~ Sean Tull ~ Active Inference in String Diagrams Sep. 1, 2023.zh-Hant.srt` | `zh-Hant` | `translations/p1GMPGBJGfw.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_002`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/UDm0lriAIJw.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/UDm0lriAIJw.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.dut(translated).dut(translated).srt` | `nl` | `translations/UDm0lriAIJw.nl.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.fre(translated).fre(translated).srt` | `fr` | `translations/UDm0lriAIJw.fr.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.ger(translated).ger(translated).srt` | `de` | `translations/UDm0lriAIJw.de.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.ita(translated).ita(translated).srt` | `it` | `translations/UDm0lriAIJw.it.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.jpn(translated).jpn(translated).srt` | `ja` | `translations/UDm0lriAIJw.ja.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.kor(translated).kor(translated).srt` | `ko` | `translations/UDm0lriAIJw.ko.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.por(translated).por(translated).srt` | `pt` | `translations/UDm0lriAIJw.pt.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.rus(translated).rus(translated).srt` | `ru` | `translations/UDm0lriAIJw.ru.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.spa(translated).spa(translated).srt` | `es` | `translations/UDm0lriAIJw.es.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/UDm0lriAIJw.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/UDm0lriAIJw.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/UDm0lriAIJw.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/UDm0lriAIJw.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/UDm0lriAIJw.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/UDm0lriAIJw.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/UDm0lriAIJw.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/UDm0lriAIJw.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/UDm0lriAIJw.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/UDm0lriAIJw.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/UDm0lriAIJw.zh-Hant.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab ModelStream #002.1.de.srt` | `de` | `translations/UDm0lriAIJw.de.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1.es.srt` | `es` | `translations/UDm0lriAIJw.es.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1.fr.srt` | `fr` | `translations/UDm0lriAIJw.fr.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1.it.srt` | `it` | `translations/UDm0lriAIJw.it.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1.ja.srt` | `ja` | `translations/UDm0lriAIJw.ja.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1.ko.srt` | `ko` | `translations/UDm0lriAIJw.ko.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1.nl.srt` | `nl` | `translations/UDm0lriAIJw.nl.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1.pt.srt` | `pt` | `translations/UDm0lriAIJw.pt.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1.ru.srt` | `ru` | `translations/UDm0lriAIJw.ru.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #002.1.zh-Hans.srt` | `zh-Hans` | `translations/UDm0lriAIJw.zh-Hans.srt` | **yes (episode token)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #002.1.zh-Hant.srt` | `zh-Hant` | `translations/UDm0lriAIJw.zh-Hant.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_003`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/G-S-kq42evw.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/G-S-kq42evw.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.de.srt` | `de` | `translations/G-S-kq42evw.de.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.es.srt` | `es` | `translations/G-S-kq42evw.es.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.fr.srt` | `fr` | `translations/G-S-kq42evw.fr.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.it.srt` | `it` | `translations/G-S-kq42evw.it.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.ja.srt` | `ja` | `translations/G-S-kq42evw.ja.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.kor(translated).kor(translated).srt` | `ko` | `translations/G-S-kq42evw.ko.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.nl.srt` | `nl` | `translations/G-S-kq42evw.nl.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.pt.srt` | `pt` | `translations/G-S-kq42evw.pt.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.ru.srt` | `ru` | `translations/G-S-kq42evw.ru.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/G-S-kq42evw.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/G-S-kq42evw.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/G-S-kq42evw.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/G-S-kq42evw.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/G-S-kq42evw.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/G-S-kq42evw.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/G-S-kq42evw.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/G-S-kq42evw.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/G-S-kq42evw.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/G-S-kq42evw.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/G-S-kq42evw.zh-Hant.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab ModelStream #003.1.de.srt` | `de` | `translations/G-S-kq42evw.de.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1.es.srt` | `es` | `translations/G-S-kq42evw.es.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1.fr.srt` | `fr` | `translations/G-S-kq42evw.fr.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1.it.srt` | `it` | `translations/G-S-kq42evw.it.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1.ja.srt` | `ja` | `translations/G-S-kq42evw.ja.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1.ko.srt` | `ko` | `translations/G-S-kq42evw.ko.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1.nl.srt` | `nl` | `translations/G-S-kq42evw.nl.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1.pt.srt` | `pt` | `translations/G-S-kq42evw.pt.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1.ru.srt` | `ru` | `translations/G-S-kq42evw.ru.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #003.1.zh-Hans.srt` | `zh-Hans` | `translations/G-S-kq42evw.zh-Hans.srt` | **yes (episode token)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #003.1.zh-Hant.srt` | `zh-Hant` | `translations/G-S-kq42evw.zh-Hant.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_004`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/uePR4DQv0yI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.chi(translated).chi(translated).srt` | `zh-Hans` | `translations/uePR4DQv0yI.zh-Hans.srt` | **yes (episode token)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.dut(translated).dut(translated).srt` | `nl` | `translations/uePR4DQv0yI.nl.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).de.srt` | `de` | `translations/uePR4DQv0yI.de.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).es.srt` | `es` | `translations/uePR4DQv0yI.es.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).fr.srt` | `fr` | `translations/uePR4DQv0yI.fr.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).it.srt` | `it` | `translations/uePR4DQv0yI.it.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).ja.srt` | `ja` | `translations/uePR4DQv0yI.ja.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).ko.srt` | `ko` | `translations/uePR4DQv0yI.ko.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).nl.srt` | `nl` | `translations/uePR4DQv0yI.nl.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).pt.srt` | `pt` | `translations/uePR4DQv0yI.pt.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).ru.srt` | `ru` | `translations/uePR4DQv0yI.ru.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).zh-Hans.srt` | `zh-Hans` | `translations/uePR4DQv0yI.zh-Hans.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/uePR4DQv0yI.zh-Hant.srt` | **yes (episode token)** | base eng(transcribed) — transcription not translation; CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.fre(translated).fre(translated).srt` | `fr` | `translations/uePR4DQv0yI.fr.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.ger(translated).ger(translated).srt` | `de` | `translations/uePR4DQv0yI.de.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.ita(translated).ita(translated).srt` | `it` | `translations/uePR4DQv0yI.it.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.jpn(translated).jpn(translated).srt` | `ja` | `translations/uePR4DQv0yI.ja.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.kor(translated).kor(translated).srt` | `ko` | `translations/uePR4DQv0yI.ko.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.por(translated).por(translated).srt` | `pt` | `translations/uePR4DQv0yI.pt.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.rus(translated).rus(translated).srt` | `ru` | `translations/uePR4DQv0yI.ru.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.spa(translated).spa(translated).srt` | `es` | `translations/uePR4DQv0yI.es.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.de.srt` | `de` | `translations/uePR4DQv0yI.de.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.es.srt` | `es` | `translations/uePR4DQv0yI.es.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.fr.srt` | `fr` | `translations/uePR4DQv0yI.fr.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.it.srt` | `it` | `translations/uePR4DQv0yI.it.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.ja.srt` | `ja` | `translations/uePR4DQv0yI.ja.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.ko.srt` | `ko` | `translations/uePR4DQv0yI.ko.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.nl.srt` | `nl` | `translations/uePR4DQv0yI.nl.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.pt.srt` | `pt` | `translations/uePR4DQv0yI.pt.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.ru.srt` | `ru` | `translations/uePR4DQv0yI.ru.srt` | **yes (episode token)** | CONFLICT: 3 files map to same target; CONFLICT: 3 files map to same target |
| `ActInfLab ModelStream #004.1.zh-Hans.srt` | `zh-Hans` | `translations/uePR4DQv0yI.zh-Hans.srt` | **yes (episode token)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInfLab ModelStream #004.1.zh-Hant.srt` | `zh-Hant` | `translations/uePR4DQv0yI.zh-Hant.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_006`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.de.srt` | `de` | `translations/xBKRLG97cz4.de.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.es.srt` | `es` | `translations/xBKRLG97cz4.es.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.fr.srt` | `fr` | `translations/xBKRLG97cz4.fr.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.it.srt` | `it` | `translations/xBKRLG97cz4.it.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.ja.srt` | `ja` | `translations/xBKRLG97cz4.ja.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.ko.srt` | `ko` | `translations/xBKRLG97cz4.ko.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.nl.srt` | `nl` | `translations/xBKRLG97cz4.nl.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.pt.srt` | `pt` | `translations/xBKRLG97cz4.pt.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.ru.srt` | `ru` | `translations/xBKRLG97cz4.ru.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.zh-Hans.srt` | `zh-Hans` | `translations/xBKRLG97cz4.zh-Hans.srt` | yes (episode token) |  |
| `ActInf ModelStream #006.1 ~  Branching Time Active Inference the theory and its generality.zh-Hant.srt` | `zh-Hant` | `translations/xBKRLG97cz4.zh-Hant.srt` | yes (episode token) |  |

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_007`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.de.srt` | `de` | `translations/skf3sOM-7WI.de.srt` | yes (episode token) |  |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.es (1).srt` | `es` | `translations/skf3sOM-7WI.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.es.srt` | `es` | `translations/skf3sOM-7WI.es.srt` | **yes (episode token)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.fr.srt` | `fr` | `translations/skf3sOM-7WI.fr.srt` | yes (episode token) |  |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.it.srt` | `it` | `translations/skf3sOM-7WI.it.srt` | yes (episode token) |  |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.ja.srt` | `ja` | `translations/skf3sOM-7WI.ja.srt` | yes (episode token) |  |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.ko.srt` | `ko` | `translations/skf3sOM-7WI.ko.srt` | yes (episode token) |  |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.nl.srt` | `nl` | `translations/skf3sOM-7WI.nl.srt` | yes (episode token) |  |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.pt.srt` | `pt` | `translations/skf3sOM-7WI.pt.srt` | yes (episode token) |  |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.ru.srt` | `ru` | `translations/skf3sOM-7WI.ru.srt` | yes (episode token) |  |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.zh-Hans.srt` | `zh-Hans` | `translations/skf3sOM-7WI.zh-Hans.srt` | yes (episode token) |  |
| `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.zh-Hant.srt` | `zh-Hant` | `translations/skf3sOM-7WI.zh-Hant.srt` | yes (episode token) |  |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_008`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.de.srt` | `de` | `translations/0pKxmZg5qXA.de.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.es.srt` | `es` | `translations/0pKxmZg5qXA.es.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.fr.srt` | `fr` | `translations/0pKxmZg5qXA.fr.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.it.srt` | `it` | `translations/0pKxmZg5qXA.it.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ja.srt` | `ja` | `translations/0pKxmZg5qXA.ja.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ko.srt` | `ko` | `translations/0pKxmZg5qXA.ko.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.nl.srt` | `nl` | `translations/0pKxmZg5qXA.nl.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.pt.srt` | `pt` | `translations/0pKxmZg5qXA.pt.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ru.srt` | `ru` | `translations/0pKxmZg5qXA.ru.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hans.srt` | `zh-Hans` | `translations/0pKxmZg5qXA.zh-Hans.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hant.srt` | `zh-Hant` | `translations/0pKxmZg5qXA.zh-Hant.srt` | **NO (ambiguous)** | episode token matches 2 parts; ambiguous match — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_009`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.de.srt` | `de` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.es.srt` | `es` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.fr.srt` | `fr` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.it.srt` | `it` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ja.srt` | `ja` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ko.srt` | `ko` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.nl.srt` | `nl` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.pt.srt` | `pt` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ru.srt` | `ru` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hans.srt` | `zh-Hans` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hant.srt` | `zh-Hant` | — | **NO (unmatched)** | no verified video_id/language — manual resolution |

### `data/video/activeinferenceinstitute/MorphStream/MorphStream_001`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.de.srt` | `de` | `translations/MzYmdBaJIYc.de.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.es.srt` | `es` | `translations/MzYmdBaJIYc.es.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.fr.srt` | `fr` | `translations/MzYmdBaJIYc.fr.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.it.srt` | `it` | `translations/MzYmdBaJIYc.it.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.ja.srt` | `ja` | `translations/MzYmdBaJIYc.ja.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.ko.srt` | `ko` | `translations/MzYmdBaJIYc.ko.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.nl.srt` | `nl` | `translations/MzYmdBaJIYc.nl.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.pt.srt` | `pt` | `translations/MzYmdBaJIYc.pt.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.ru.srt` | `ru` | `translations/MzYmdBaJIYc.ru.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.zh-Hans.srt` | `zh-Hans` | `translations/MzYmdBaJIYc.zh-Hans.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.zh-Hant.srt` | `zh-Hant` | `translations/MzYmdBaJIYc.zh-Hant.srt` | **yes (title exact)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).de.srt` | `de` | `translations/MzYmdBaJIYc.de.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).es.srt` | `es` | `translations/MzYmdBaJIYc.es.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).fr.srt` | `fr` | `translations/MzYmdBaJIYc.fr.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).it.srt` | `it` | `translations/MzYmdBaJIYc.it.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).ja.srt` | `ja` | `translations/MzYmdBaJIYc.ja.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).ko.srt` | `ko` | `translations/MzYmdBaJIYc.ko.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).nl.srt` | `nl` | `translations/MzYmdBaJIYc.nl.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).pt.srt` | `pt` | `translations/MzYmdBaJIYc.pt.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).ru.srt` | `ru` | `translations/MzYmdBaJIYc.ru.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).zh-Hans.srt` | `zh-Hans` | `translations/MzYmdBaJIYc.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 2 ~ Meeting 20 (Chapter 9, part 1).zh-Hant.srt` | `zh-Hant` | `translations/MzYmdBaJIYc.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target; stem unrelated to sole part title — unverified |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.de.srt` | `de` | `translations/MzYmdBaJIYc.de.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.es.srt` | `es` | `translations/MzYmdBaJIYc.es.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.fr.srt` | `fr` | `translations/MzYmdBaJIYc.fr.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.it.srt` | `it` | `translations/MzYmdBaJIYc.it.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ja.srt` | `ja` | `translations/MzYmdBaJIYc.ja.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ko.srt` | `ko` | `translations/MzYmdBaJIYc.ko.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.nl.srt` | `nl` | `translations/MzYmdBaJIYc.nl.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.pt.srt` | `pt` | `translations/MzYmdBaJIYc.pt.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ru.srt` | `ru` | `translations/MzYmdBaJIYc.ru.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hans.srt` | `zh-Hans` | `translations/MzYmdBaJIYc.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hant.srt` | `zh-Hant` | `translations/MzYmdBaJIYc.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.de.srt` | `de` | `translations/MzYmdBaJIYc.de.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.es.srt` | `es` | `translations/MzYmdBaJIYc.es.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.fr.srt` | `fr` | `translations/MzYmdBaJIYc.fr.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.it.srt` | `it` | `translations/MzYmdBaJIYc.it.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ja.srt` | `ja` | `translations/MzYmdBaJIYc.ja.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ko.srt` | `ko` | `translations/MzYmdBaJIYc.ko.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.nl.srt` | `nl` | `translations/MzYmdBaJIYc.nl.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.pt.srt` | `pt` | `translations/MzYmdBaJIYc.pt.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ru.srt` | `ru` | `translations/MzYmdBaJIYc.ru.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hans.srt` | `zh-Hans` | `translations/MzYmdBaJIYc.zh-Hans.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |
| `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hant.srt` | `zh-Hant` | `translations/MzYmdBaJIYc.zh-Hant.srt` | **assumed (sole part)** | CONFLICT: 4 files map to same target; CONFLICT: 4 files map to same target |

### `data/video/activeinferenceinstitute/Roundtable/Roundtable_2022.3`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.de.srt` | `de` | `translations/DJ9n6a8mMzM.de.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.es.srt` | `es` | `translations/DJ9n6a8mMzM.es.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.fr.srt` | `fr` | `translations/DJ9n6a8mMzM.fr.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.it.srt` | `it` | `translations/DJ9n6a8mMzM.it.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.ja.srt` | `ja` | `translations/DJ9n6a8mMzM.ja.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.ko.srt` | `ko` | `translations/DJ9n6a8mMzM.ko.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.nl.srt` | `nl` | `translations/DJ9n6a8mMzM.nl.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.pt.srt` | `pt` | `translations/DJ9n6a8mMzM.pt.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.ru.srt` | `ru` | `translations/DJ9n6a8mMzM.ru.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.zh-Hans.srt` | `zh-Hans` | `translations/DJ9n6a8mMzM.zh-Hans.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2022 Quarterly Roundtable #3.zh-Hant.srt` | `zh-Hant` | `translations/DJ9n6a8mMzM.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/Roundtable/Roundtable_2023.1`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.de.srt` | `de` | `translations/XYMPAAynUu8.de.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.es.srt` | `es` | `translations/XYMPAAynUu8.es.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.fr.srt` | `fr` | `translations/XYMPAAynUu8.fr.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.it.srt` | `it` | `translations/XYMPAAynUu8.it.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.ja.srt` | `ja` | `translations/XYMPAAynUu8.ja.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.ko.srt` | `ko` | `translations/XYMPAAynUu8.ko.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.nl.srt` | `nl` | `translations/XYMPAAynUu8.nl.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.pt.srt` | `pt` | `translations/XYMPAAynUu8.pt.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.ru.srt` | `ru` | `translations/XYMPAAynUu8.ru.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.zh-Hans.srt` | `zh-Hans` | `translations/XYMPAAynUu8.zh-Hans.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable #1.zh-Hant.srt` | `zh-Hant` | `translations/XYMPAAynUu8.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/Roundtable/Roundtable_2023.2`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.de.srt` | `de` | `translations/aJ9Py86ZFjU.de.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.es.srt` | `es` | `translations/aJ9Py86ZFjU.es.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.fr.srt` | `fr` | `translations/aJ9Py86ZFjU.fr.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.it.srt` | `it` | `translations/aJ9Py86ZFjU.it.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.ja.srt` | `ja` | `translations/aJ9Py86ZFjU.ja.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.ko.srt` | `ko` | `translations/aJ9Py86ZFjU.ko.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.nl.srt` | `nl` | `translations/aJ9Py86ZFjU.nl.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.pt.srt` | `pt` | `translations/aJ9Py86ZFjU.pt.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.ru.srt` | `ru` | `translations/aJ9Py86ZFjU.ru.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.zh-Hans.srt` | `zh-Hans` | `translations/aJ9Py86ZFjU.zh-Hans.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 2.zh-Hant.srt` | `zh-Hant` | `translations/aJ9Py86ZFjU.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/Roundtable/Roundtable_2023.3`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.de.srt` | `de` | `translations/93-rNtJR-9I.de.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.es.srt` | `es` | `translations/93-rNtJR-9I.es.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.fr.srt` | `fr` | `translations/93-rNtJR-9I.fr.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.it.srt` | `it` | `translations/93-rNtJR-9I.it.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.ja.srt` | `ja` | `translations/93-rNtJR-9I.ja.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.ko.srt` | `ko` | `translations/93-rNtJR-9I.ko.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.nl.srt` | `nl` | `translations/93-rNtJR-9I.nl.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.pt.srt` | `pt` | `translations/93-rNtJR-9I.pt.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.ru.srt` | `ru` | `translations/93-rNtJR-9I.ru.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.zh-Hans.srt` | `zh-Hans` | `translations/93-rNtJR-9I.zh-Hans.srt` | yes (title exact) |  |
| `Active Inference Institute ~ 2023 Quarterly Roundtable 3.zh-Hant.srt` | `zh-Hant` | `translations/93-rNtJR-9I.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_001`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 1 (Onboarding).ja.srt` | `ja` | `translations/ogV63M3uTlQ.ja.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 1 (Onboarding).ko.srt` | `ko` | `translations/ogV63M3uTlQ.ko.srt` | **yes (title exact)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).es.srt` | `es` | `translations/ogV63M3uTlQ.es.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).fr.srt` | `fr` | `translations/ogV63M3uTlQ.fr.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).it.srt` | `it` | `translations/ogV63M3uTlQ.it.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).ja.srt` | `ja` | `translations/ogV63M3uTlQ.ja.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).ko.srt` | `ko` | `translations/ogV63M3uTlQ.ko.srt` | **assumed (sole part)** | CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target; stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).nl.srt` | `nl` | `translations/ogV63M3uTlQ.nl.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).pt.srt` | `pt` | `translations/ogV63M3uTlQ.pt.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).ru.srt` | `ru` | `translations/ogV63M3uTlQ.ru.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).zh-Hans.srt` | `zh-Hans` | `translations/ogV63M3uTlQ.zh-Hans.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).zh-Hant.srt` | `zh-Hant` | `translations/ogV63M3uTlQ.zh-Hant.srt` | **assumed (sole part)** | stem unrelated to sole part title — unverified |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_002`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 2 (Chapter 1).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/pJy1M1RnirA.zh-Hans.srt` | yes (title prefix) | chi default zh-Hans (no Simp/Trad qualifier) |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_003`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/8OT2EC-l0N4.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/8OT2EC-l0N4.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).dut(translated).dut(translated).srt` | `nl` | `translations/8OT2EC-l0N4.nl.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).fre(translated).fre(translated).srt` | `fr` | `translations/8OT2EC-l0N4.fr.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).ger(translated).ger(translated).srt` | `de` | `translations/8OT2EC-l0N4.de.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).ita(translated).ita(translated).srt` | `it` | `translations/8OT2EC-l0N4.it.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).jpn(translated).jpn(translated).srt` | `ja` | `translations/8OT2EC-l0N4.ja.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).kor(translated).kor(translated).srt` | `ko` | `translations/8OT2EC-l0N4.ko.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).por(translated).por(translated).srt` | `pt` | `translations/8OT2EC-l0N4.pt.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).rus(translated).rus(translated).srt` | `ru` | `translations/8OT2EC-l0N4.ru.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).spa(translated).spa(translated).srt` | `es` | `translations/8OT2EC-l0N4.es.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_004`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/Z7Z29pu6NnY.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/Z7Z29pu6NnY.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).dut(translated).dut(translated).srt` | `nl` | `translations/Z7Z29pu6NnY.nl.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).fre(translated).fre(translated).srt` | `fr` | `translations/Z7Z29pu6NnY.fr.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).ger(translated).ger(translated).srt` | `de` | `translations/Z7Z29pu6NnY.de.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).ita(translated).ita(translated).srt` | `it` | `translations/Z7Z29pu6NnY.it.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).jpn(translated).jpn(translated).srt` | `ja` | `translations/Z7Z29pu6NnY.ja.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).kor(translated).kor(translated).srt` | `ko` | `translations/Z7Z29pu6NnY.ko.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).por(translated).por(translated).srt` | `pt` | `translations/Z7Z29pu6NnY.pt.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).rus(translated).rus(translated).srt` | `ru` | `translations/Z7Z29pu6NnY.ru.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_005`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/JJaQ0F81Ucs.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/JJaQ0F81Ucs.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).dut(translated).dut(translated).srt` | `nl` | `translations/JJaQ0F81Ucs.nl.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).fre(translated).fre(translated).srt` | `fr` | `translations/JJaQ0F81Ucs.fr.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).ger(translated).ger(translated).srt` | `de` | `translations/JJaQ0F81Ucs.de.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).ita(translated).ita(translated).srt` | `it` | `translations/JJaQ0F81Ucs.it.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).jpn(translated).jpn(translated).srt` | `ja` | `translations/JJaQ0F81Ucs.ja.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).kor(translated).kor(translated).srt` | `ko` | `translations/JJaQ0F81Ucs.ko.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).por(translated).por(translated).srt` | `pt` | `translations/JJaQ0F81Ucs.pt.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).rus(translated).rus(translated).srt` | `ru` | `translations/JJaQ0F81Ucs.ru.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).spa(translated).spa(translated).srt` | `es` | `translations/JJaQ0F81Ucs.es.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_006`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/MXbknE8EZp0.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/MXbknE8EZp0.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).dut(translated).dut(translated).srt` | `nl` | `translations/MXbknE8EZp0.nl.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).fre(translated).fre(translated).srt` | `fr` | `translations/MXbknE8EZp0.fr.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).ger(translated).ger(translated).srt` | `de` | `translations/MXbknE8EZp0.de.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).ita(translated).ita(translated).srt` | `it` | `translations/MXbknE8EZp0.it.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).jpn(translated).jpn(translated).srt` | `ja` | `translations/MXbknE8EZp0.ja.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).kor(translated).kor(translated).srt` | `ko` | `translations/MXbknE8EZp0.ko.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).por(translated).por(translated).srt` | `pt` | `translations/MXbknE8EZp0.pt.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).rus(translated).rus(translated).srt` | `ru` | `translations/MXbknE8EZp0.ru.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).spa(translated).spa(translated).srt` | `es` | `translations/MXbknE8EZp0.es.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_007`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).chi(translated) (2).chi(translated).srt` | `zh-Hans` | `translations/AKeKLERgmQA.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).chi(translated).chi(translated).srt` | `zh-Hans` | `translations/AKeKLERgmQA.zh-Hans.srt` | **yes (title prefix)** | chi default zh-Hans (no Simp/Trad qualifier); CONFLICT: 2 files map to same target; CONFLICT: 2 files map to same target |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).dut(translated).dut(translated).srt` | `nl` | `translations/AKeKLERgmQA.nl.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).fre(translated).fre(translated).srt` | `fr` | `translations/AKeKLERgmQA.fr.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).ger(translated).ger(translated).srt` | `de` | `translations/AKeKLERgmQA.de.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).ita(translated).ita(translated).srt` | `it` | `translations/AKeKLERgmQA.it.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).jpn(translated).jpn(translated).srt` | `ja` | `translations/AKeKLERgmQA.ja.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).kor(translated).kor(translated).srt` | `ko` | `translations/AKeKLERgmQA.ko.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).por(translated).por(translated).srt` | `pt` | `translations/AKeKLERgmQA.pt.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).rus(translated).rus(translated).srt` | `ru` | `translations/AKeKLERgmQA.ru.srt` | yes (title prefix) |  |
| `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).spa(translated).spa(translated).srt` | `es` | `translations/AKeKLERgmQA.es.srt` | yes (title prefix) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_002`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).de.srt` | `de` | `translations/HyKS1A0Ga8s.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).es.srt` | `es` | `translations/HyKS1A0Ga8s.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).fr.srt` | `fr` | `translations/HyKS1A0Ga8s.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).it.srt` | `it` | `translations/HyKS1A0Ga8s.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).ja.srt` | `ja` | `translations/HyKS1A0Ga8s.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).ko.srt` | `ko` | `translations/HyKS1A0Ga8s.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).nl.srt` | `nl` | `translations/HyKS1A0Ga8s.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).pt.srt` | `pt` | `translations/HyKS1A0Ga8s.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).ru.srt` | `ru` | `translations/HyKS1A0Ga8s.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).zh-Hans.srt` | `zh-Hans` | `translations/HyKS1A0Ga8s.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 2 (Chapter 1, part 1).zh-Hant.srt` | `zh-Hant` | `translations/HyKS1A0Ga8s.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_003`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).de.srt` | `de` | `translations/awqzJPntNz4.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).es.srt` | `es` | `translations/awqzJPntNz4.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).fr.srt` | `fr` | `translations/awqzJPntNz4.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).it.srt` | `it` | `translations/awqzJPntNz4.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).ja.srt` | `ja` | `translations/awqzJPntNz4.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).ko.srt` | `ko` | `translations/awqzJPntNz4.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).nl.srt` | `nl` | `translations/awqzJPntNz4.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).pt.srt` | `pt` | `translations/awqzJPntNz4.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).ru.srt` | `ru` | `translations/awqzJPntNz4.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).zh-Hans.srt` | `zh-Hans` | `translations/awqzJPntNz4.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 3 (Chapter 1, part 2).zh-Hant.srt` | `zh-Hant` | `translations/awqzJPntNz4.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_004`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).de.srt` | `de` | `translations/wFjXz896pKU.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).es.srt` | `es` | `translations/wFjXz896pKU.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).fr.srt` | `fr` | `translations/wFjXz896pKU.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).it.srt` | `it` | `translations/wFjXz896pKU.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).ja.srt` | `ja` | `translations/wFjXz896pKU.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).ko.srt` | `ko` | `translations/wFjXz896pKU.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).nl.srt` | `nl` | `translations/wFjXz896pKU.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).pt.srt` | `pt` | `translations/wFjXz896pKU.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).ru.srt` | `ru` | `translations/wFjXz896pKU.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).zh-Hans.srt` | `zh-Hans` | `translations/wFjXz896pKU.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 4 (Chapter 2, part 1).zh-Hant.srt` | `zh-Hant` | `translations/wFjXz896pKU.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_005`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).de.srt` | `de` | `translations/MJXyGtYuK1U.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).es.srt` | `es` | `translations/MJXyGtYuK1U.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).fr.srt` | `fr` | `translations/MJXyGtYuK1U.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).it.srt` | `it` | `translations/MJXyGtYuK1U.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).ja.srt` | `ja` | `translations/MJXyGtYuK1U.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).ko.srt` | `ko` | `translations/MJXyGtYuK1U.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).nl.srt` | `nl` | `translations/MJXyGtYuK1U.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).pt.srt` | `pt` | `translations/MJXyGtYuK1U.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).ru.srt` | `ru` | `translations/MJXyGtYuK1U.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).zh-Hans.srt` | `zh-Hans` | `translations/MJXyGtYuK1U.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 5 (Chapter 2, part 2).zh-Hant.srt` | `zh-Hant` | `translations/MJXyGtYuK1U.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_006`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).de.srt` | `de` | `translations/lMsOOXaM2-E.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).es.srt` | `es` | `translations/lMsOOXaM2-E.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).fr.srt` | `fr` | `translations/lMsOOXaM2-E.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).it.srt` | `it` | `translations/lMsOOXaM2-E.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).ja.srt` | `ja` | `translations/lMsOOXaM2-E.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).ko.srt` | `ko` | `translations/lMsOOXaM2-E.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).nl.srt` | `nl` | `translations/lMsOOXaM2-E.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).pt.srt` | `pt` | `translations/lMsOOXaM2-E.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).ru.srt` | `ru` | `translations/lMsOOXaM2-E.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).zh-Hans.srt` | `zh-Hans` | `translations/lMsOOXaM2-E.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 6 (Chapter 3, part 1).zh-Hant.srt` | `zh-Hant` | `translations/lMsOOXaM2-E.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_007`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).de.srt` | `de` | `translations/0zUYswqn8aI.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).es.srt` | `es` | `translations/0zUYswqn8aI.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).fr.srt` | `fr` | `translations/0zUYswqn8aI.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).it.srt` | `it` | `translations/0zUYswqn8aI.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).ja.srt` | `ja` | `translations/0zUYswqn8aI.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).ko.srt` | `ko` | `translations/0zUYswqn8aI.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).nl.srt` | `nl` | `translations/0zUYswqn8aI.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).pt.srt` | `pt` | `translations/0zUYswqn8aI.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).ru.srt` | `ru` | `translations/0zUYswqn8aI.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).zh-Hans.srt` | `zh-Hans` | `translations/0zUYswqn8aI.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 7 (Chapter 3, part 2).zh-Hant.srt` | `zh-Hant` | `translations/0zUYswqn8aI.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_008`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).de.srt` | `de` | `translations/JEz3du5S1os.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).es.srt` | `es` | `translations/JEz3du5S1os.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).fr.srt` | `fr` | `translations/JEz3du5S1os.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).it.srt` | `it` | `translations/JEz3du5S1os.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).ja.srt` | `ja` | `translations/JEz3du5S1os.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).ko.srt` | `ko` | `translations/JEz3du5S1os.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).nl.srt` | `nl` | `translations/JEz3du5S1os.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).pt.srt` | `pt` | `translations/JEz3du5S1os.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).ru.srt` | `ru` | `translations/JEz3du5S1os.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).zh-Hans.srt` | `zh-Hans` | `translations/JEz3du5S1os.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 8 (Chapter 4, part 1).zh-Hant.srt` | `zh-Hant` | `translations/JEz3du5S1os.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_009`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).de.srt` | `de` | `translations/Nak508NmYYA.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).es.srt` | `es` | `translations/Nak508NmYYA.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).fr.srt` | `fr` | `translations/Nak508NmYYA.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).it.srt` | `it` | `translations/Nak508NmYYA.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).ja.srt` | `ja` | `translations/Nak508NmYYA.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).ko.srt` | `ko` | `translations/Nak508NmYYA.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).nl.srt` | `nl` | `translations/Nak508NmYYA.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).pt.srt` | `pt` | `translations/Nak508NmYYA.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).ru.srt` | `ru` | `translations/Nak508NmYYA.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).zh-Hans.srt` | `zh-Hans` | `translations/Nak508NmYYA.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 9 (Chapter 4, part 2).zh-Hant.srt` | `zh-Hant` | `translations/Nak508NmYYA.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_010`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).de.srt` | `de` | `translations/l6aGBYmFGCc.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).es.srt` | `es` | `translations/l6aGBYmFGCc.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).fr.srt` | `fr` | `translations/l6aGBYmFGCc.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).it.srt` | `it` | `translations/l6aGBYmFGCc.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).ja.srt` | `ja` | `translations/l6aGBYmFGCc.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).ko.srt` | `ko` | `translations/l6aGBYmFGCc.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).nl.srt` | `nl` | `translations/l6aGBYmFGCc.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).pt.srt` | `pt` | `translations/l6aGBYmFGCc.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).ru.srt` | `ru` | `translations/l6aGBYmFGCc.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).zh-Hans.srt` | `zh-Hans` | `translations/l6aGBYmFGCc.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 10 (Chapter 5, part 1).zh-Hant.srt` | `zh-Hant` | `translations/l6aGBYmFGCc.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_011`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 11 (Chapter 5, part 2).de.srt` | `de` | `translations/Ui8SwfQDhmA.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 11 (Chapter 5, part 2).es.srt` | `es` | `translations/Ui8SwfQDhmA.es.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_015`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).de.srt` | `de` | `translations/5F8kbj05KHU.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).es.srt` | `es` | `translations/5F8kbj05KHU.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).fr.srt` | `fr` | `translations/5F8kbj05KHU.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).it.srt` | `it` | `translations/5F8kbj05KHU.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).ja.srt` | `ja` | `translations/5F8kbj05KHU.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).ko.srt` | `ko` | `translations/5F8kbj05KHU.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).nl.srt` | `nl` | `translations/5F8kbj05KHU.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).pt.srt` | `pt` | `translations/5F8kbj05KHU.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).ru.srt` | `ru` | `translations/5F8kbj05KHU.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).zh-Hans.srt` | `zh-Hans` | `translations/5F8kbj05KHU.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 15 (Chapter 6, part 2).zh-Hant.srt` | `zh-Hant` | `translations/5F8kbj05KHU.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_016`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).de.srt` | `de` | `translations/ych0eX3C3YY.de.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).es.srt` | `es` | `translations/ych0eX3C3YY.es.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).fr.srt` | `fr` | `translations/ych0eX3C3YY.fr.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).it.srt` | `it` | `translations/ych0eX3C3YY.it.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).ja.srt` | `ja` | `translations/ych0eX3C3YY.ja.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).ko.srt` | `ko` | `translations/ych0eX3C3YY.ko.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).nl.srt` | `nl` | `translations/ych0eX3C3YY.nl.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).pt.srt` | `pt` | `translations/ych0eX3C3YY.pt.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).ru.srt` | `ru` | `translations/ych0eX3C3YY.ru.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).zh-Hans.srt` | `zh-Hans` | `translations/ych0eX3C3YY.zh-Hans.srt` | yes (title exact) |  |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 16 (Chapter 7, part 1).zh-Hant.srt` | `zh-Hant` | `translations/ych0eX3C3YY.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/Twitter Spaces/TwitterSpaces_001`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.de.srt` | `de` | `translations/3SjbReGPZME.de.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.es.srt` | `es` | `translations/3SjbReGPZME.es.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.fr.srt` | `fr` | `translations/3SjbReGPZME.fr.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.it.srt` | `it` | `translations/3SjbReGPZME.it.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.ja.srt` | `ja` | `translations/3SjbReGPZME.ja.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.ko.srt` | `ko` | `translations/3SjbReGPZME.ko.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.nl.srt` | `nl` | `translations/3SjbReGPZME.nl.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.pt.srt` | `pt` | `translations/3SjbReGPZME.pt.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.ru.srt` | `ru` | `translations/3SjbReGPZME.ru.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.zh-Hans.srt` | `zh-Hans` | `translations/3SjbReGPZME.zh-Hans.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter spaces #001 ~ December 9th 2021.zh-Hant.srt` | `zh-Hant` | `translations/3SjbReGPZME.zh-Hant.srt` | yes (title exact) |  |

### `data/video/activeinferenceinstitute/Twitter Spaces/TwitterSpaces_002`

| Old file (in `Translations/`) | Lang | Target (relative to item) | Verified video_id match | Note |
|---|---|---|---|---|
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.de.srt` | `de` | `translations/Sb8A0jNzWPE.de.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.es.srt` | `es` | `translations/Sb8A0jNzWPE.es.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.fr.srt` | `fr` | `translations/Sb8A0jNzWPE.fr.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.it.srt` | `it` | `translations/Sb8A0jNzWPE.it.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.ja.srt` | `ja` | `translations/Sb8A0jNzWPE.ja.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.ko.srt` | `ko` | `translations/Sb8A0jNzWPE.ko.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.nl.srt` | `nl` | `translations/Sb8A0jNzWPE.nl.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.pt.srt` | `pt` | `translations/Sb8A0jNzWPE.pt.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.ru.srt` | `ru` | `translations/Sb8A0jNzWPE.ru.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.zh-Hans.srt` | `zh-Hans` | `translations/Sb8A0jNzWPE.zh-Hans.srt` | yes (title exact) |  |
| `Active Inference ~ Twitter Spaces #002 ~ Web3 survive without cognitive modeling.zh-Hant.srt` | `zh-Hant` | `translations/Sb8A0jNzWPE.zh-Hant.srt` | yes (title exact) |  |

## Conflict-resolution pass (2026-09-23, pass 2b)

The 917 collapse-conflict rows of part 1 were resolved as follows:

| Outcome | Files |
|---|---|
| Migrated — unique verified video_id, plain target | 122 |
| Migrated — talkslug target `<vid>.<lang>.<talkslug>.srt` (per-talk files in single-part interval items) | 182 |
| Migrated — cross-item rescue (INDEX title matched exactly one part of a *different* item) | 13 |
| Quarantined to `translations/conflicts/<series>/` | 600 |

Verification used: normalized-stem == part-title (INDEX cross-check), unique
`#<n>.<m>` episode tokens, YouTube-dump provenance (plain `.<lang>.srt` names
preferred over derivative regenerations), and byte-level dedupe. Files with
multiple genuinely-different versions for one target cannot be machine-resolved
and are quarantined with their original names (md5-prefixed) under
`translations/conflicts/<series>/`; their collisions are listed in the CONFLICTS
appendix below. `previous_paths` was written for migrated/rescued files only.


## CONFLICTS appendix (quarantined this pass)

Each row: quarantined file (md5-prefixed under `translations/conflicts/<series>/`)
<- original `Translations/` path, with reason.

### `data/video/activeinferenceinstitute/Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval` — 51 quarantined

- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).de.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).es.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).fr.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).it.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).ja.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).ko.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).nl.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).pt.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).ru.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).zh-Hans.srt` — superseded-by-dump
- `3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).zh-Hant.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).de.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).es.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).fr.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).it.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).ja.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).ko.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).nl.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).pt.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).ru.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).zh-Hans.srt` — superseded-by-dump
- `3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).zh-Hant.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).de.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).es.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).fr.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).it.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).ja.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).ko.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).nl.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).pt.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).ru.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).zh-Hans.srt` — superseded-by-dump
- `3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).zh-Hant.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).de.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).es.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).fr.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).it.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).ja.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).ko.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).nl.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).pt.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).ru.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).zh-Hans.srt` — superseded-by-dump
- `3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).zh-Hant.srt` — superseded-by-dump
- `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).de.srt` — superseded-by-dump
- `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).es.srt` — superseded-by-dump
- `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).fr.srt` — superseded-by-dump
- `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).it.srt` — superseded-by-dump
- `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).nl.srt` — superseded-by-dump
- `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).pt.srt` — superseded-by-dump
- `3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).ru.srt` — superseded-by-dump

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/ActInf_Basics_Lecture` — 11 quarantined

- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.de.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.es.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.fr.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.it.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.ja.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.ko.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.nl.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.pt.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.ru.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.zh-Hans.srt` — dump-variant
- `AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.zh-Hant.srt` — dump-variant

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/CollectiveBehavior_Discussion` — 16 quarantined

- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.de.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.es.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.fr.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.it.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ja.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ko.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.de.srt` — superseded-by-dump
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.es.srt` — superseded-by-dump
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.fr.srt` — superseded-by-dump
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.it.srt` — superseded-by-dump
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.pt.srt` — superseded-by-dump
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.nl.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.pt.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ru.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hans.srt` — dump-variant
- `Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hant.srt` — dump-variant

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_013` — 2 quarantined

- `ActInfLab GuestStream #013.1 ~ Adam Safron.chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab GuestStream #013.1 ~ Adam Safron.chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token

### `data/video/activeinferenceinstitute/Livestream/LiveStream_001` — 17 quarantined

- `Active Inference Podcast #001 “Narrative as active inference.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).de.srt` — superseded-by-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).es.srt` — superseded-by-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).fr.srt` — superseded-by-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).it.srt` — superseded-by-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.por(translated).por(translated).srt` — multiple-versions-no-dump
- `Active Inference Podcast #001 “Narrative as active inference.rus(translated).rus(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_002` — 11 quarantined

- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).de.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).es.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).fr.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).it.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).ja.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).ko.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).nl.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).pt.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).ru.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).zh-Hans.srt` — superseded-by-dump
- `ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).zh-Hant.srt` — superseded-by-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_003` — 6 quarantined

- `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).de.srt` — superseded-by-dump
- `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).es.srt` — superseded-by-dump
- `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).fr.srt` — superseded-by-dump
- `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).it.srt` — superseded-by-dump
- `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).nl.srt` — superseded-by-dump
- `ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.ger(translated).ger(translated).srt` — superseded-by-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_004` — 18 quarantined

- `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).de.srt` — superseded-by-dump
- `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).es.srt` — superseded-by-dump
- `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).fr.srt` — superseded-by-dump
- `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).it.srt` — superseded-by-dump
- `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ja.srt` — superseded-by-dump
- `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).nl.srt` — superseded-by-dump
- `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).pt.srt` — superseded-by-dump
- `Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ru.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).de.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).es.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).fr.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).it.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ja.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ko.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).nl.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).pt.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ru.srt` — superseded-by-dump
- `Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).zh-Hans.srt` — superseded-by-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_005` — 63 quarantined

- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).por(translated).por(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).spa(translated).spa(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).por(translated).por(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).spa(translated).spa(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).por(translated).por(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).spa(translated).spa(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_006` — 21 quarantined

- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.por(translated).por(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.spa(translated).spa(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_007` — 62 quarantined

- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).por(translated).por(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).spa(translated).spa(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).por(translated).por(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).spa(translated).spa(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).de.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).dut(translated).dut(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).de.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).es.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).fr.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).it.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ja.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ko.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).nl.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).pt.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ru.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).fr.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).ita(translated).ita(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).jpn(translated).jpn(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).kor(translated).kor(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).por(translated).por(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).rus(translated).rus(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).spa(translated).spa(translated).srt` — rescue-version-conflict:episode-token

### `data/video/activeinferenceinstitute/Livestream/LiveStream_008` — 63 quarantined

- `Active Inference podcast #008.0 “Scaling active inference  (2019).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).por(translated).por(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.0 “Scaling active inference  (2019).spa(translated).spa(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).por(translated).por(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.1 “Scaling active inference  (2019).spa(translated).spa(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #008.2 “Scaling active inference  (2019).chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).dut(translated).dut(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).de.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).es.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).fr.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).it.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ja.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ko.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).nl.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).pt.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ru.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).fre(translated).fre(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).ger(translated).ger(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).ita(translated).ita(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).jpn(translated).jpn(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).kor(translated).kor(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).por(translated).por(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).rus(translated).rus(translated).srt` — rescue-version-conflict:episode-token
- `Active Inference podcast #008.2 “Scaling active inference  (2019).spa(translated).spa(translated).srt` — rescue-version-conflict:episode-token

### `data/video/activeinferenceinstitute/Livestream/LiveStream_009` — 21 quarantined

- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).por(translated).por(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).spa(translated).spa(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_010` — 42 quarantined

- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).por(translated).por(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.0  A variational approach to scripts  (2020).spa(translated).spa(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).dut(translated).dut(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).de.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).es.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).fr.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).it.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ja.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ko.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).nl.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).pt.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ru.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hans.srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).fre(translated).fre(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).ger(translated).ger(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).ita(translated).ita(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).jpn(translated).jpn(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).kor(translated).kor(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).por(translated).por(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).rus(translated).rus(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #010.2  A variational approach to scripts  (2020).spa(translated).spa(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_011` — 2 quarantined

- `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token

### `data/video/activeinferenceinstitute/Livestream/LiveStream_013` — 6 quarantined

- `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_014` — 6 quarantined

- `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token

### `data/video/activeinferenceinstitute/Livestream/LiveStream_015` — 6 quarantined

- `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated) (2).chi(translated).srt` — rescue-dest-occupied
- `ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated).chi(translated).srt` — rescue-dest-occupied
- `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated) (2).chi(translated).srt` — rescue-dest-occupied
- `ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated).chi(translated).srt` — rescue-dest-occupied

### `data/video/activeinferenceinstitute/Livestream/LiveStream_016` — 4 quarantined

- `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_017` — 4 quarantined

- `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token

### `data/video/activeinferenceinstitute/Livestream/LiveStream_018` — 6 quarantined

- `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_019` — 6 quarantined

- `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_020` — 6 quarantined

- `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_021` — 4 quarantined

- `ActInfLab Livestream #021.04 ~ John Boik.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #021.04 ~ John Boik.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #021.2 ~ John Boik.ger(translated) (2).ger(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #021.2 ~ John Boik.ger(translated).ger(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_023` — 2 quarantined

- `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_024` — 6 quarantined

- `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated) (2).chi(translated).srt` — rescue-dest-occupied
- `ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated).chi(translated).srt` — rescue-dest-occupied
- `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_025` — 2 quarantined

- `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.chi(translated) (2).chi(translated).srt` — rescue-dest-occupied
- `ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.chi(translated).chi(translated).srt` — rescue-dest-occupied

### `data/video/activeinferenceinstitute/Livestream/LiveStream_026` — 2 quarantined

- `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.chi(translated) (2).chi(translated).srt` — rescue-version-conflict:episode-token
- `ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.chi(translated).chi(translated).srt` — rescue-version-conflict:episode-token

### `data/video/activeinferenceinstitute/Livestream/LiveStream_029` — 6 quarantined

- `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_030` — 6 quarantined

- `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated) (2).chi(translated).srt` — rescue-dest-occupied
- `ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated).chi(translated).srt` — rescue-dest-occupied
- `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_040` — 2 quarantined

- `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_045` — 2 quarantined

- `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/Livestream/LiveStream_046` — 4 quarantined

- `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.chi(translated).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/MathStream/MathStream_001` — 19 quarantined

- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.chi(translated-Simp).chi(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.chi(translated-Trad) (2).chi(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.dut(translated).dut(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.fre(translated).fre(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.ger(translated).ger(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.ita(translated).ita(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.jpn(translated).jpn(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.kor(translated).kor(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.por(translated).por(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.rus(translated).rus(translated).srt` — superseded-by-dump
- `ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.spa(translated).spa(translated).srt` — superseded-by-dump
- `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).de.srt` — superseded-by-dump
- `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).es.srt` — superseded-by-dump
- `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).fr.srt` — superseded-by-dump
- `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).it.srt` — superseded-by-dump
- `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).ja.srt` — superseded-by-dump
- `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).nl.srt` — superseded-by-dump
- `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).pt.srt` — superseded-by-dump
- `ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).ru.srt` — superseded-by-dump

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_002` — 22 quarantined

- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.chi(translated) (2).chi(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.chi(translated).chi(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.dut(translated).dut(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.fre(translated).fre(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.ger(translated).ger(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.ita(translated).ita(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.jpn(translated).jpn(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.kor(translated).kor(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.por(translated).por(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.rus(translated).rus(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.spa(translated).spa(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).de.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).es.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).fr.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).it.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).ja.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).ko.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).nl.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).pt.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).ru.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).zh-Hans.srt` — superseded-by-dump
- `ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).zh-Hant.srt` — superseded-by-dump

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_003` — 22 quarantined

- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.chi(translated) (2).chi(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.chi(translated).chi(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.de.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.es.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.fr.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.it.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.ja.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.kor(translated).kor(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.nl.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.pt.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.ru.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).ko.srt` — superseded-by-dump
- `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).zh-Hans.srt` — superseded-by-dump
- `ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).zh-Hant.srt` — superseded-by-dump
- `ActInfLab ModelStream #003.1.de.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1.es.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1.fr.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1.it.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1.ja.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1.nl.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1.pt.srt` — multiple-dump-versions
- `ActInfLab ModelStream #003.1.ru.srt` — multiple-dump-versions

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_004` — 22 quarantined

- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.chi(translated) (2).chi(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.chi(translated).chi(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.dut(translated).dut(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).de.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).es.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).fr.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).it.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).ja.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).ko.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).nl.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).pt.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).ru.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).zh-Hans.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).zh-Hant.srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.fre(translated).fre(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.ger(translated).ger(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.ita(translated).ita(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.jpn(translated).jpn(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.kor(translated).kor(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.por(translated).por(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.rus(translated).rus(translated).srt` — superseded-by-dump
- `ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.spa(translated).spa(translated).srt` — superseded-by-dump

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_007` — 1 quarantined

- `Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.es (1).srt` — superseded-by-dump

### `data/video/activeinferenceinstitute/MorphStream/MorphStream_001` — 22 quarantined

- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.de.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.es.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.fr.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.it.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ja.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ko.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.nl.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.pt.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ru.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hans.srt` — superseded-by-dump
- `Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hant.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.de.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.es.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.fr.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.it.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ja.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ko.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.nl.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.pt.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ru.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hans.srt` — superseded-by-dump
- `mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hant.srt` — superseded-by-dump

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_003` — 2 quarantined

- `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).chi(translated) (2).chi(translated).srt` — multiple-versions-no-dump
- `ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).chi(translated).chi(translated).srt` — multiple-versions-no-dump

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_004` — 1 quarantined

- `ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).chi(translated).chi(translated).srt` — byte-identical-extra

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_005` — 1 quarantined

- `ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).chi(translated).chi(translated).srt` — byte-identical-extra

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_006` — 1 quarantined

- `ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).chi(translated).chi(translated).srt` — byte-identical-extra

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_007` — 1 quarantined

- `ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).chi(translated).chi(translated).srt` — byte-identical-extra


## REMAINING (still not migrated)

423 files remain untouched at their original `Translations/` paths
(machine-unresolvable: no verified video_id/language, unverified single-part, or
ambiguous match). Volunteer good-first-issue material (I16).

### `data/video/activeinferenceinstitute/Applied Active Inference Symposium/2021 Symposium with Karl Friston` — 44 remaining

- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education).zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/BookStream/BookStream_001` — 46 remaining

- `Active Inference BookStream 001.010 ~  Governing Continuous Transformation_transcript.srt` — no verified video_id/language (no language suffix) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.08 ~  Governing Continuous Transformation_transcript.srt` — no verified video_id/language (no language suffix) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/BookStream/BookStream_002` — 19 remaining

- `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Discussion` — 11 remaining

- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Lecture` — 11 remaining

- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_015` — 12 remaining

- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.en(ie).srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_016` — 11 remaining

- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_029` — 11 remaining

- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_032` — 11 remaining

- `ActInf GuestStream 032-1 ~ Adam Pease (audio).de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 032-1 ~ Adam Pease (audio).zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_044` — 11 remaining

- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_046` — 12 remaining

- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.en(ie).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_047` — 11 remaining

- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_053` — 11 remaining

- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_055` — 11 remaining

- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/GuestStream/GuestStream_058` — 11 remaining

- `gs058-1 Working with Gerald Edelman.de.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.ja.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.ko.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `gs058-1 Working with Gerald Edelman.zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Livestream/LiveStream_001` — 1 remaining

- `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Livestream/LiveStream_006` — 1 remaining

- `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).zh-Hant.srt` — ambiguous match — needs human review

### `data/video/activeinferenceinstitute/Livestream/LiveStream_016` — 11 remaining

- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Livestream/LiveStream_032` — 11 remaining

- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Livestream/LiveStream_045` — 1 remaining

- `ActInf Livestream #045.2 ~ The free energy principle made simpler but not too simple.che(translated).srt` — no verified video_id/language (unknown language code) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Livestream/LiveStream_047` — 11 remaining

- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Livestream/LiveStream_052` — 11 remaining

- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Livestream/LiveStream_053` — 22 remaining

- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/Livestream/LiveStream_054` — 34 remaining

- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.en(ie).srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ls054 1 Compositional Account of the Bayesian Brain Smithe.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/MathStream/MathStream_002` — 3 remaining

- `ActInfLab MathStream #002.1 ~ Shanna Dobson.chi(translated-Simp).chi(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #002.1 ~ Shanna Dobson.chi(translated-Trad) (2).chi(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #002.1 ~ Shanna Dobson.ger(translated).ger(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/MathStream/MathStream_003` — 11 remaining

- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.chi(translated-Simp).chi(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.chi(translated-Trad) (2).chi(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.dut(translated).dut(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.fre(translated).fre(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.ger(translated).ger(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.ita(translated).ita(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.jpn(translated).jpn(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.kor(translated).kor(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.por(translated).por(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.rus(translated).rus(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.spa(translated).spa(translated).srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_007` — 11 remaining

- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_008` — 22 remaining

- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.de.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.es.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.fr.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.it.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ja.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ko.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.nl.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.pt.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ru.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hans.srt` — ambiguous match — needs human review
- `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hant.srt` — ambiguous match — needs human review
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/ModelStream/ModelStream_009` — 22 remaining

- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.de.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.es.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.fr.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.it.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ja.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ko.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.nl.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.pt.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ru.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hans.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)
- `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hant.srt` — no verified video_id/language (stem unmatched to any part) — good-first-issue material (I16)

### `data/video/activeinferenceinstitute/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_001` — 8 remaining

- `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).es.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).fr.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).it.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).nl.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).pt.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).ru.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).zh-Hans.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)
- `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).zh-Hant.srt` — stem unrelated to sole part title (unverified single-part) — good-first-issue material (I16)

