# Volunteer transcript triage (I16)

Generated 2026-09-24 against branch `feat/m2-translations` (HEAD `21c58548`), from the
[M2 translation migration map](translation-migration-map.md) (part 1 + pass 2b appendices).
**Tree re-verification (2026-09-24, HEAD `fbc1ab8e`).** All counts below were re-derived from the git
index and match the rows exactly: REMAINING 423 files across 30 items (412 rows in Part A + the 11
files with no verified home deferred to Part C), CONFLICTS 600 files across 44 items with the reason
tally 301 `multiple-versions-no-dump` / 187 `superseded-by-dump` / 60 `rescue-version-conflict:episode-token`
/ 22 `dump-variant` / 16 `multiple-dump-versions` / 10 `rescue-dest-occupied` / 4 `byte-identical-extra`.
Note for volunteers: legacy `Translations/` folders and migrated `translations/` folders collide on
case-insensitive checkouts (both are tracked in git) — derive counts and paths from `git ls-files`,
never from a filesystem walk.

**Context.** M2 moved 1,857 legacy translation files into per-item `translations/<video_id>.<bcp47>.srt`
(1,540 verified rows in part 2, 317 rescued in pass 2b, plus conflict handling). What remains: **423 files**
still in legacy `Translations/` folders ("REMAINING", 30 items) and **600 files** quarantined under
`translations/conflicts/<series>/` ("CONFLICTS", 44 items) because several versions collided on one target.
This doc is the volunteer triage list for both. GitHub-issue versions of the highest-value batches live in
[good-first-issues-draft.md](good-first-issues-draft.md).

REMAINING breakdown: 277 no verified video_id/language, 134 unverified single-part, 12 ambiguous.
Every guess below was produced by fuzzy-matching the legacy filename stem against every part title of the
item **and of all other items** (misfiled files are common — four cross-item rehomes are already flagged).
Every guess still needs the verification step below before any move.

## The 30-minute task (per file)

1. **Verify the video_id** — open the item's `metadata.json`, confirm the guessed `parts[].video_id`, and
   spot-check `https://www.youtube.com/watch?v=<video_id>` (title/date match the stem's episode token).
2. **Confirm the language** by opening the `.srt` (first ~20 subtitle lines). Normalize per the table in the
   [migration map](translation-migration-map.md) (`chi` → `zh-Hans`/`zh-Hant`, legacy 3-letter codes, etc.).
3. **Move with the two-step `git mv`** (see command pattern below) into
   `translations/<video_id>.<bcp47>.srt`.

4. **Record `previous_paths`** — append the original repo-relative path to the **destination item's**
   `metadata.json` `previous_paths` array (same convention M2 used for all 1,857 moved files).

5. **Commit path-scoped** — one commit per item (or per series batch), message style:

   `translations(<series>): migrate <N> legacy files (I16 triage)`.


### Exact command pattern

```bash

NEW="<video_id>.<bcp47>.srt"                       # verified target name


# two-step move (intermediate dir makes the Translations/ → translations/ case-rename visible to git)

git mv "$ITEM/$OLD" "$ITEM/translations_tmp/$(basename "$OLD")"

git mv "$ITEM/translations_tmp/$(basename "$OLD")" "$ITEM/translations/$NEW"

rmdir "$ITEM/translations_tmp" "$ITEM/Translations" 2>/dev/null   # when the last file leaves them


# record previous_paths in the destination item metadata (repo-relative original path)

jq --arg p "$ITEM/$OLD" \

   '.previous_paths = ((.previous_paths // []) + [$p] | unique)' \

   "$ITEM/metadata.json" > "$ITEM/metadata.json.tmp" && mv "$ITEM/metadata.json.tmp" "$ITEM/metadata.json"

```


Notes:

- If a target file already exists in `translations/`, **do not overwrite**: byte-compare (`cmp`). Identical →
  delete the legacy copy instead of moving (still record nothing; mention in the PR). Different → this is a
  version conflict; use the Part B playbook.

- Cross-item rehomes (marked ⚠ **REHOME**): run the same steps with `ITEM` set to the destination item,
  and record `previous_paths` in the **destination** item's `metadata.json`.

- Per-talk translations (quarantined interval files) use `<video_id>.<bcp47>.<talkslug>.srt`; copy the talkslug
  convention already present in that item's `translations/` (e.g. `rIemcswLfGg.de.01-andre-bastos.srt`).


---

## Part A — REMAINING: 423 files still in `Translations/` (move targets known)


Confidence: **high** = unique episode-token or title evidence; **med** = verify identity more carefully
(empty title, typo in stem, or an ambiguity the stem itself resolves). Every row still requires the
30-minute task.


### Series: `Applied Active Inference Symposium`


#### `Applied Active Inference Symposium/2021 Symposium with Karl Friston` — 44 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.de.srt` | `de` | `translations/zm2d9o5n0PU.de.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.es.srt` | `es` | `translations/zm2d9o5n0PU.es.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.fr.srt` | `fr` | `translations/zm2d9o5n0PU.fr.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.it.srt` | `it` | `translations/zm2d9o5n0PU.it.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.ja.srt` | `ja` | `translations/zm2d9o5n0PU.ja.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.ko.srt` | `ko` | `translations/zm2d9o5n0PU.ko.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.nl.srt` | `nl` | `translations/zm2d9o5n0PU.nl.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.pt.srt` | `pt` | `translations/zm2d9o5n0PU.pt.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.ru.srt` | `ru` | `translations/zm2d9o5n0PU.ru.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.zh-Hans.srt` | `zh-Hans` | `translations/zm2d9o5n0PU.zh-Hans.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 1st session.zh-Hant.srt` | `zh-Hant` | `translations/zm2d9o5n0PU.zh-Hant.srt` | stem names the **2nd Applied Active Inference Symposium on Robotics (2022)**, 1st session — the 2021 item holds only the 2021 Friston sessions (map's misfiling note); destination item's part 1 is titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 1' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.de.srt` | `de` | `translations/dTVHHenms_Y.de.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.es.srt` | `es` | `translations/dTVHHenms_Y.es.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.fr.srt` | `fr` | `translations/dTVHHenms_Y.fr.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.it.srt` | `it` | `translations/dTVHHenms_Y.it.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.ja.srt` | `ja` | `translations/dTVHHenms_Y.ja.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.ko.srt` | `ko` | `translations/dTVHHenms_Y.ko.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.nl.srt` | `nl` | `translations/dTVHHenms_Y.nl.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.pt.srt` | `pt` | `translations/dTVHHenms_Y.pt.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.ru.srt` | `ru` | `translations/dTVHHenms_Y.ru.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.zh-Hans.srt` | `zh-Hans` | `translations/dTVHHenms_Y.zh-Hans.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `2nd Applied Active Inference Symposium on  Robotics  ~ 2nd session.zh-Hant.srt` | `zh-Hant` | `translations/dTVHHenms_Y.zh-Hant.srt` | same misfiling: 2022 Robotics 2nd session; destination part 2 titled '…Robotics 2022 ~ 2nd Applied Active Inference Symposium, part 2' ⚠ **REHOME → `Applied Active Inference Symposium/2022 Symposium on Robotics`** — cross-item rehome: metadata `previous_paths` goes in the **2022 Symposium on Robotics** item | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).de.srt` | `de` | `translations/hW9IiOujS1E.de.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).es.srt` | `es` | `translations/hW9IiOujS1E.es.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).fr.srt` | `fr` | `translations/hW9IiOujS1E.fr.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).it.srt` | `it` | `translations/hW9IiOujS1E.it.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).ja.srt` | `ja` | `translations/hW9IiOujS1E.ja.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).ko.srt` | `ko` | `translations/hW9IiOujS1E.ko.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).nl.srt` | `nl` | `translations/hW9IiOujS1E.nl.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).pt.srt` | `pt` | `translations/hW9IiOujS1E.pt.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).ru.srt` | `ru` | `translations/hW9IiOujS1E.ru.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).zh-Hans.srt` | `zh-Hans` | `translations/hW9IiOujS1E.zh-Hans.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |
| `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 3 (Tools).zh-Hant.srt` | `zh-Hant` | `translations/hW9IiOujS1E.zh-Hant.srt` | in-item part hW9IiOujS1E is titled '…1st Applied Active Inference Symposium, part 3 (.tools)' — matches 'pt. 3 (Tools)' | high |

### Series: `BookStream`


#### `BookStream/BookStream_001` — 46 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `Active Inference BookStream 001.010 ~  Governing Continuous Transformation_transcript.srt` | **inspect** (no language suffix — inspect content) | `translations/eIZjx0miM9o.<bcp47>.srt` | token '001.010' matches part 'BookStream #001.010' uniquely — transcript file without language suffix (likely en; inspect) — no language suffix — inspect content, likely `en` | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/5IGzzm28qec.de.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/5IGzzm28qec.es.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/5IGzzm28qec.fr.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/5IGzzm28qec.it.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/5IGzzm28qec.ja.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/5IGzzm28qec.ko.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/5IGzzm28qec.nl.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/5IGzzm28qec.pt.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/5IGzzm28qec.ru.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/5IGzzm28qec.zh-Hans.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.012 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/5IGzzm28qec.zh-Hant.srt` | token '001.012' matches part 'BookStream #001.012' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/d8c0iFU8vms.de.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/d8c0iFU8vms.es.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/d8c0iFU8vms.fr.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/d8c0iFU8vms.it.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/d8c0iFU8vms.ja.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/d8c0iFU8vms.ko.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/d8c0iFU8vms.nl.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/d8c0iFU8vms.pt.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/d8c0iFU8vms.ru.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/d8c0iFU8vms.zh-Hans.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.02 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/d8c0iFU8vms.zh-Hant.srt` | token '001.02' matches part 'BookStream #001.02' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/0P_6ME2LpCw.de.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/0P_6ME2LpCw.es.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/0P_6ME2LpCw.fr.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/0P_6ME2LpCw.it.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/0P_6ME2LpCw.ja.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/0P_6ME2LpCw.ko.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/0P_6ME2LpCw.nl.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/0P_6ME2LpCw.pt.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/0P_6ME2LpCw.ru.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/0P_6ME2LpCw.zh-Hans.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.06 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/0P_6ME2LpCw.zh-Hant.srt` | token '001.06' matches part 'BookStream #001.06' uniquely | high |
| `Active Inference BookStream 001.08 ~  Governing Continuous Transformation_transcript.srt` | **inspect** (no language suffix — inspect content) | `translations/yNZg5b63hb8.<bcp47>.srt` | token '001.08' matches part 'BookStream #001.08' uniquely — no language suffix — inspect content, likely `en` | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.de.srt` | `de` | `translations/FB_93-zDqNo.de.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.es.srt` | `es` | `translations/FB_93-zDqNo.es.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.fr.srt` | `fr` | `translations/FB_93-zDqNo.fr.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.it.srt` | `it` | `translations/FB_93-zDqNo.it.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.ja.srt` | `ja` | `translations/FB_93-zDqNo.ja.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.ko.srt` | `ko` | `translations/FB_93-zDqNo.ko.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.nl.srt` | `nl` | `translations/FB_93-zDqNo.nl.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.pt.srt` | `pt` | `translations/FB_93-zDqNo.pt.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.ru.srt` | `ru` | `translations/FB_93-zDqNo.ru.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.zh-Hans.srt` | `zh-Hans` | `translations/FB_93-zDqNo.zh-Hans.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |
| `Active Inference BookStream 001.1 ~  Governing Continuous Transformation.zh-Hant.srt` | `zh-Hant` | `translations/FB_93-zDqNo.zh-Hant.srt` | token '001.1' matches part 'BookStream #001.1' uniquely (not #001.10 — that part does not exist) | high |

#### `BookStream/BookStream_002` — 19 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.de.srt` | `de` | `translations/FV7pW4p60VI.de.srt` | part 'BookStream #002.01 ~ Parr, Pezzulo, Friston 2022 ~ Chapter 1, 2, 3, 6 overview' — stem '002.0' ≈ '#002.01' and the chapter list matches the part title | high |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.es.srt` | `es` | `translations/FV7pW4p60VI.es.srt` | part 'BookStream #002.01 ~ Parr, Pezzulo, Friston 2022 ~ Chapter 1, 2, 3, 6 overview' — stem '002.0' ≈ '#002.01' and the chapter list matches the part title | high |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.fr.srt` | `fr` | `translations/FV7pW4p60VI.fr.srt` | part 'BookStream #002.01 ~ Parr, Pezzulo, Friston 2022 ~ Chapter 1, 2, 3, 6 overview' — stem '002.0' ≈ '#002.01' and the chapter list matches the part title | high |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.it.srt` | `it` | `translations/FV7pW4p60VI.it.srt` | part 'BookStream #002.01 ~ Parr, Pezzulo, Friston 2022 ~ Chapter 1, 2, 3, 6 overview' — stem '002.0' ≈ '#002.01' and the chapter list matches the part title | high |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.ja.srt` | `ja` | `translations/FV7pW4p60VI.ja.srt` | part 'BookStream #002.01 ~ Parr, Pezzulo, Friston 2022 ~ Chapter 1, 2, 3, 6 overview' — stem '002.0' ≈ '#002.01' and the chapter list matches the part title | high |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.nl.srt` | `nl` | `translations/FV7pW4p60VI.nl.srt` | part 'BookStream #002.01 ~ Parr, Pezzulo, Friston 2022 ~ Chapter 1, 2, 3, 6 overview' — stem '002.0' ≈ '#002.01' and the chapter list matches the part title | high |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.pt.srt` | `pt` | `translations/FV7pW4p60VI.pt.srt` | part 'BookStream #002.01 ~ Parr, Pezzulo, Friston 2022 ~ Chapter 1, 2, 3, 6 overview' — stem '002.0' ≈ '#002.01' and the chapter list matches the part title | high |
| `Active Inference BookStream 002.0 ~ Parr, Pezzulo, Friston ~ Chapters 1, 2, 3, 6.ru.srt` | `ru` | `translations/FV7pW4p60VI.ru.srt` | part 'BookStream #002.01 ~ Parr, Pezzulo, Friston 2022 ~ Chapter 1, 2, 3, 6 overview' — stem '002.0' ≈ '#002.01' and the chapter list matches the part title | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.de.srt` | `de` | `translations/3_5pTCguAv4.de.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.es.srt` | `es` | `translations/3_5pTCguAv4.es.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.fr.srt` | `fr` | `translations/3_5pTCguAv4.fr.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.it.srt` | `it` | `translations/3_5pTCguAv4.it.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.ja.srt` | `ja` | `translations/3_5pTCguAv4.ja.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.ko.srt` | `ko` | `translations/3_5pTCguAv4.ko.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.nl.srt` | `nl` | `translations/3_5pTCguAv4.nl.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.pt.srt` | `pt` | `translations/3_5pTCguAv4.pt.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.ru.srt` | `ru` | `translations/3_5pTCguAv4.ru.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.zh-Hans.srt` | `zh-Hans` | `translations/3_5pTCguAv4.zh-Hans.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |
| `Active Inference BookStream 002.02 ~ Parr, Pezzulo, Friston ~ Chapters 4, 5, 7, 8.zh-Hant.srt` | `zh-Hant` | `translations/3_5pTCguAv4.zh-Hant.srt` | part 'BookStream #002.02 ~ … Chapter 4, 5, 7, 8 overview' — chapter list matches exactly | high |

### Series: `Courses`


#### `Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Discussion` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.de.srt` | `de` | `translations/MrAiB9X7Ock.de.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.es.srt` | `es` | `translations/MrAiB9X7Ock.es.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.fr.srt` | `fr` | `translations/MrAiB9X7Ock.fr.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.it.srt` | `it` | `translations/MrAiB9X7Ock.it.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.ja.srt` | `ja` | `translations/MrAiB9X7Ock.ja.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.ko.srt` | `ko` | `translations/MrAiB9X7Ock.ko.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.nl.srt` | `nl` | `translations/MrAiB9X7Ock.nl.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.pt.srt` | `pt` | `translations/MrAiB9X7Ock.pt.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.ru.srt` | `ru` | `translations/MrAiB9X7Ock.ru.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.zh-Hans.srt` | `zh-Hans` | `translations/MrAiB9X7Ock.zh-Hans.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |
| `Semiotics and Semantics Discussion ~ Lorena Sganzerla ~ Active Inference for Social Sciences 9 12.zh-Hant.srt` | `zh-Hant` | `translations/MrAiB9X7Ock.zh-Hant.srt` | sole part of the item: 'Semiotics and Semantics (Discussion) ~ Lorena Sganzerla ~ Active Inference for Social Sciences 2023' — stem differs only by the date token '9 12' | med |

#### `Courses/ActiveInferenceForTheSocialSciences/SemioticsSemantics_Lecture` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.de.srt` | `de` | `translations/4ijYLWm4P2I.de.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.es.srt` | `es` | `translations/4ijYLWm4P2I.es.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.fr.srt` | `fr` | `translations/4ijYLWm4P2I.fr.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.it.srt` | `it` | `translations/4ijYLWm4P2I.it.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.ja.srt` | `ja` | `translations/4ijYLWm4P2I.ja.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.ko.srt` | `ko` | `translations/4ijYLWm4P2I.ko.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.nl.srt` | `nl` | `translations/4ijYLWm4P2I.nl.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.pt.srt` | `pt` | `translations/4ijYLWm4P2I.pt.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.ru.srt` | `ru` | `translations/4ijYLWm4P2I.ru.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.zh-Hans.srt` | `zh-Hans` | `translations/4ijYLWm4P2I.zh-Hans.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |
| `CCL2023.06 Semiotics and Semantics Lecture ~ Lorena Sganzerla, 2023-08-30.zh-Hant.srt` | `zh-Hant` | `translations/4ijYLWm4P2I.zh-Hant.srt` | sole part of the item: 'Semiotics and Semantics (Lecture) ~ Lorena Sganzerla ~ Active Inference for the Social Sciences 2023' — stem adds a course code and the date | med |

### Series: `GuestStream`


#### `GuestStream/GuestStream_015` — 12 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.de.srt` | `de` | `translations/S-tFHIqtbSI.de.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.en(ie).srt` | `en` | `translations/S-tFHIqtbSI.en.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.es.srt` | `es` | `translations/S-tFHIqtbSI.es.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.fr.srt` | `fr` | `translations/S-tFHIqtbSI.fr.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.it.srt` | `it` | `translations/S-tFHIqtbSI.it.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.ja.srt` | `ja` | `translations/S-tFHIqtbSI.ja.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.ko.srt` | `ko` | `translations/S-tFHIqtbSI.ko.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.nl.srt` | `nl` | `translations/S-tFHIqtbSI.nl.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.pt.srt` | `pt` | `translations/S-tFHIqtbSI.pt.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.ru.srt` | `ru` | `translations/S-tFHIqtbSI.ru.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.zh-Hans.srt` | `zh-Hans` | `translations/S-tFHIqtbSI.zh-Hans.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |
| `ActInf GuestStream 015.3 ~ Bobby Azarian, The Teleological Stance, 6 1 2023.zh-Hant.srt` | `zh-Hant` | `translations/S-tFHIqtbSI.zh-Hant.srt` | in-item part S-tFHIqtbSI is 'GuestStream #015.3 ~ The Teleological Stance: The Free Energy Principle as a Basis for a Scientific Self-Help System' — episode token 015.3 + title match (Bobby Azarian's talk) | high |

#### `GuestStream/GuestStream_016` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.de.srt` | `de` | `translations/c0_Vf5_qiWk.de.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.es.srt` | `es` | `translations/c0_Vf5_qiWk.es.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.fr.srt` | `fr` | `translations/c0_Vf5_qiWk.fr.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.it.srt` | `it` | `translations/c0_Vf5_qiWk.it.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.ja.srt` | `ja` | `translations/c0_Vf5_qiWk.ja.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.ko.srt` | `ko` | `translations/c0_Vf5_qiWk.ko.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.nl.srt` | `nl` | `translations/c0_Vf5_qiWk.nl.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.pt.srt` | `pt` | `translations/c0_Vf5_qiWk.pt.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.ru.srt` | `ru` | `translations/c0_Vf5_qiWk.ru.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.zh-Hans.srt` | `zh-Hans` | `translations/c0_Vf5_qiWk.zh-Hans.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |
| `ActInfLab GuestStream #0161.2 ~ Mark Solms  Consciousness as Precision Optimization AutoCaption.zh-Hant.srt` | `zh-Hant` | `translations/c0_Vf5_qiWk.zh-Hant.srt` | stem typo '#0161.2' → '#016.2'; part c0_Vf5_qiWk is 'GuestStream #016.2 ~ Consciousness as Precision Optimization…' — 'AutoCaption' flags a YouTube-derived variant, compare against already-migrated #016.2 files for redundancy | med |

#### `GuestStream/GuestStream_029` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.de.srt` | `de` | `translations/UuXAjY9Wgdg.de.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.es.srt` | `es` | `translations/UuXAjY9Wgdg.es.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.fr.srt` | `fr` | `translations/UuXAjY9Wgdg.fr.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.it.srt` | `it` | `translations/UuXAjY9Wgdg.it.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.ja.srt` | `ja` | `translations/UuXAjY9Wgdg.ja.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.ko.srt` | `ko` | `translations/UuXAjY9Wgdg.ko.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.nl.srt` | `nl` | `translations/UuXAjY9Wgdg.nl.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.pt.srt` | `pt` | `translations/UuXAjY9Wgdg.pt.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.ru.srt` | `ru` | `translations/UuXAjY9Wgdg.ru.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.zh-Hans.srt` | `zh-Hans` | `translations/UuXAjY9Wgdg.zh-Hans.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |
| `ActInf GuestStream #029.1 Making Up Our Minds Imaginative Deconstruction in MathArt, 1920 – Present.zh-Hant.srt` | `zh-Hant` | `translations/UuXAjY9Wgdg.zh-Hant.srt` | sole part of the item (UuXAjY9Wgdg) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=UuXAjY9Wgdg before moving | med |

#### `GuestStream/GuestStream_032` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).de.srt` | `de` | `translations/0pMxBM3ahwQ.de.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).es.srt` | `es` | `translations/0pMxBM3ahwQ.es.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).fr.srt` | `fr` | `translations/0pMxBM3ahwQ.fr.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).it.srt` | `it` | `translations/0pMxBM3ahwQ.it.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).ja.srt` | `ja` | `translations/0pMxBM3ahwQ.ja.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).ko.srt` | `ko` | `translations/0pMxBM3ahwQ.ko.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).nl.srt` | `nl` | `translations/0pMxBM3ahwQ.nl.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).pt.srt` | `pt` | `translations/0pMxBM3ahwQ.pt.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).ru.srt` | `ru` | `translations/0pMxBM3ahwQ.ru.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).zh-Hans.srt` | `zh-Hans` | `translations/0pMxBM3ahwQ.zh-Hans.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |
| `ActInf GuestStream 032-1 ~ Adam Pease (audio).zh-Hant.srt` | `zh-Hant` | `translations/0pMxBM3ahwQ.zh-Hant.srt` | sole part 'ActInf GuestStream #032.1 ~ Adam Pease "A Neuro-Symbolic Approach to Language Understanding"' — '032-1' = '#032.1' | high |

#### `GuestStream/GuestStream_044` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.de.srt` | `de` | `translations/FymR0rKdLZo.de.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.es.srt` | `es` | `translations/FymR0rKdLZo.es.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.fr.srt` | `fr` | `translations/FymR0rKdLZo.fr.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.it.srt` | `it` | `translations/FymR0rKdLZo.it.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.ja.srt` | `ja` | `translations/FymR0rKdLZo.ja.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.ko.srt` | `ko` | `translations/FymR0rKdLZo.ko.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.nl.srt` | `nl` | `translations/FymR0rKdLZo.nl.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.pt.srt` | `pt` | `translations/FymR0rKdLZo.pt.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.ru.srt` | `ru` | `translations/FymR0rKdLZo.ru.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.zh-Hans.srt` | `zh-Hans` | `translations/FymR0rKdLZo.zh-Hans.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |
| `ActInf GuestStream 044.1 ~ Tsuchiya & Saigo, Category TheoryNew video.zh-Hant.srt` | `zh-Hant` | `translations/FymR0rKdLZo.zh-Hant.srt` | sole part 'ActInf GuestStream 044.1 ~ Tsuchiya & Saigo: Category Theory, Consciousness, Integrated Information' — 'New video' is a filename-capture artifact | high |

#### `GuestStream/GuestStream_046` — 12 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.de.srt` | `de` | `translations/dUW8cD8XUec.de.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.en(ie).srt` | `en` | `translations/dUW8cD8XUec.en.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.es.srt` | `es` | `translations/dUW8cD8XUec.es.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.fr.srt` | `fr` | `translations/dUW8cD8XUec.fr.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.it.srt` | `it` | `translations/dUW8cD8XUec.it.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.ja.srt` | `ja` | `translations/dUW8cD8XUec.ja.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.ko.srt` | `ko` | `translations/dUW8cD8XUec.ko.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.nl.srt` | `nl` | `translations/dUW8cD8XUec.nl.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.pt.srt` | `pt` | `translations/dUW8cD8XUec.pt.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.ru.srt` | `ru` | `translations/dUW8cD8XUec.ru.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.zh-Hans.srt` | `zh-Hans` | `translations/dUW8cD8XUec.zh-Hans.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |
| `gs046.1 ~ Denise Holt, Active Inference AI & the Spatial Web.zh-Hant.srt` | `zh-Hant` | `translations/dUW8cD8XUec.zh-Hant.srt` | sole part 'ActInf GuestStream 046.1 ~ Denise Holt, "Active Inference AI & the Spatial Web"' | high |

#### `GuestStream/GuestStream_047` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.de.srt` | `de` | `translations/O6adLcDhOYU.de.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.es.srt` | `es` | `translations/O6adLcDhOYU.es.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.fr.srt` | `fr` | `translations/O6adLcDhOYU.fr.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.it.srt` | `it` | `translations/O6adLcDhOYU.it.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.ja.srt` | `ja` | `translations/O6adLcDhOYU.ja.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.ko.srt` | `ko` | `translations/O6adLcDhOYU.ko.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.nl.srt` | `nl` | `translations/O6adLcDhOYU.nl.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.pt.srt` | `pt` | `translations/O6adLcDhOYU.pt.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.ru.srt` | `ru` | `translations/O6adLcDhOYU.ru.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.zh-Hans.srt` | `zh-Hans` | `translations/O6adLcDhOYU.zh-Hans.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |
| `ActInf GuestStream 047.1 Predicting, Reflecting Framework for Dual Process Theory, S. Bellini-Leite.zh-Hant.srt` | `zh-Hant` | `translations/O6adLcDhOYU.zh-Hant.srt` | sole part 'ActInf GuestStream 047.1 ~ "Predicting & Reflecting Framework for Dual Process Theory" Bellini-Leite' | high |

#### `GuestStream/GuestStream_053` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.de.srt` | `de` | `translations/_GHJO_bnyrY.de.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.es.srt` | `es` | `translations/_GHJO_bnyrY.es.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.fr.srt` | `fr` | `translations/_GHJO_bnyrY.fr.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.it.srt` | `it` | `translations/_GHJO_bnyrY.it.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.ja.srt` | `ja` | `translations/_GHJO_bnyrY.ja.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.ko.srt` | `ko` | `translations/_GHJO_bnyrY.ko.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.nl.srt` | `nl` | `translations/_GHJO_bnyrY.nl.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.pt.srt` | `pt` | `translations/_GHJO_bnyrY.pt.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.ru.srt` | `ru` | `translations/_GHJO_bnyrY.ru.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.zh-Hans.srt` | `zh-Hans` | `translations/_GHJO_bnyrY.zh-Hans.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |
| `ActInf GuestStream 053.1 ~ Tolchinsky et al  2023 A case for chaos theory.zh-Hant.srt` | `zh-Hant` | `translations/_GHJO_bnyrY.zh-Hant.srt` | sole part 'ActInf GuestStream 053.1 ~ A case for chaos theory inclusion in neuropsychoanalytic modeling' (Tolchinsky et al. 2023) | high |

#### `GuestStream/GuestStream_055` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.de.srt` | `de` | `translations/a4DC1YCVpsU.de.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.es.srt` | `es` | `translations/a4DC1YCVpsU.es.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.fr.srt` | `fr` | `translations/a4DC1YCVpsU.fr.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.it.srt` | `it` | `translations/a4DC1YCVpsU.it.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.ja.srt` | `ja` | `translations/a4DC1YCVpsU.ja.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.ko.srt` | `ko` | `translations/a4DC1YCVpsU.ko.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.nl.srt` | `nl` | `translations/a4DC1YCVpsU.nl.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.pt.srt` | `pt` | `translations/a4DC1YCVpsU.pt.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.ru.srt` | `ru` | `translations/a4DC1YCVpsU.ru.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.zh-Hans.srt` | `zh-Hans` | `translations/a4DC1YCVpsU.zh-Hans.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |
| `gs055 1 ~ James Pang, Alex Fornito Geometric constraints.zh-Hant.srt` | `zh-Hant` | `translations/a4DC1YCVpsU.zh-Hant.srt` | sole part 'ActInf GuestStream 055.1~ James Pang & Alex Fornito "Geometric constraints on human brain function"' | high |

#### `GuestStream/GuestStream_058` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `gs058-1 Working with Gerald Edelman.de.srt` | `de` | `translations/Sz7ZP2N6DuE.de.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.es.srt` | `es` | `translations/Sz7ZP2N6DuE.es.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.fr.srt` | `fr` | `translations/Sz7ZP2N6DuE.fr.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.it.srt` | `it` | `translations/Sz7ZP2N6DuE.it.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.ja.srt` | `ja` | `translations/Sz7ZP2N6DuE.ja.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.ko.srt` | `ko` | `translations/Sz7ZP2N6DuE.ko.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.nl.srt` | `nl` | `translations/Sz7ZP2N6DuE.nl.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.pt.srt` | `pt` | `translations/Sz7ZP2N6DuE.pt.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.ru.srt` | `ru` | `translations/Sz7ZP2N6DuE.ru.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.zh-Hans.srt` | `zh-Hans` | `translations/Sz7ZP2N6DuE.zh-Hans.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |
| `gs058-1 Working with Gerald Edelman.zh-Hant.srt` | `zh-Hant` | `translations/Sz7ZP2N6DuE.zh-Hant.srt` | sole part 'ActInf GuestStream 058.1 ~ Working with Gerald Edelman' | high |

### Series: `Livestream`


#### `Livestream/LiveStream_001` — 1 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/C94WDXAe4EE.zh-Hant.srt` | sole part 'ActInf Livestream #001.1 ~ "Narrative as active inference"' — file language chain ends zh-Hant (earlier 'eng(transcribed)' tokens are provenance) | med |

#### `Livestream/LiveStream_006` — 1 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).zh-Hant.srt` | `zh-Hant` | `translations/HQadNEGAtbY.zh-Hant.srt` | two parts share '#006.2' (machine-flagged ambiguous); stem says '(2020)' which matches part HQadNEGAtbY '…"A tale of two densities…" (2020)' — verify against y4tljwMAWho (same title, no year) | med |

#### `Livestream/LiveStream_016` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.de.srt` | `de` | `translations/93lAa-xEmHY.de.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.es.srt` | `es` | `translations/93lAa-xEmHY.es.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.fr.srt` | `fr` | `translations/93lAa-xEmHY.fr.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.it.srt` | `it` | `translations/93lAa-xEmHY.it.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.ja.srt` | `ja` | `translations/93lAa-xEmHY.ja.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.ko.srt` | `ko` | `translations/93lAa-xEmHY.ko.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.nl.srt` | `nl` | `translations/93lAa-xEmHY.nl.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.pt.srt` | `pt` | `translations/93lAa-xEmHY.pt.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.ru.srt` | `ru` | `translations/93lAa-xEmHY.ru.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.zh-Hans.srt` | `zh-Hans` | `translations/93lAa-xEmHY.zh-Hans.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |
| `ActInfLab Livestream #016-2 “Neural correlates of consciousness under the FEP.zh-Hant.srt` | `zh-Hant` | `translations/93lAa-xEmHY.zh-Hant.srt` | '#016-2' → '#016.2'; part 93lAa-xEmHY is 'Livestream #016.2 ~ "The neural correlates of consciousness under the free energy principle…"' | high |

#### `Livestream/LiveStream_032` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.de.srt` | `de` | `translations/7_JLMK3agpA.de.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.es.srt` | `es` | `translations/7_JLMK3agpA.es.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.fr.srt` | `fr` | `translations/7_JLMK3agpA.fr.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.it.srt` | `it` | `translations/7_JLMK3agpA.it.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.ja.srt` | `ja` | `translations/7_JLMK3agpA.ja.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.ko.srt` | `ko` | `translations/7_JLMK3agpA.ko.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.nl.srt` | `nl` | `translations/7_JLMK3agpA.nl.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.pt.srt` | `pt` | `translations/7_JLMK3agpA.pt.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.ru.srt` | `ru` | `translations/7_JLMK3agpA.ru.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.zh-Hans.srt` | `zh-Hans` | `translations/7_JLMK3agpA.zh-Hans.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |
| `ActInf Livestream 032.0 ~  Stochastic Chaos and Markov Blankets.zh-Hant.srt` | `zh-Hant` | `translations/7_JLMK3agpA.zh-Hant.srt` | token '032.0' matches part 'Livestream #032.0 ~ Stochastic Chaos and Markov Blankets' uniquely (parts #032.0–#032.3) | high |

#### `Livestream/LiveStream_045` — 1 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf Livestream #045.2 ~ The free energy principle made simpler but not too simple.che(translated).srt` | **inspect** (unknown legacy code 'che' — inspect content (likely cs or zh)) | `translations/S5-jXzhiG18.<bcp47>.srt` | token '045.2' matches part 'Livestream #045.2' uniquely; language suffix 'che(translated)' is unknown — inspect content — unknown legacy language code 'che' — inspect content (likely cs, or a 'chi' typo → zh) | med |

#### `Livestream/LiveStream_047` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.de.srt` | `de` | `translations/riJYh87FPx4.de.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.es.srt` | `es` | `translations/riJYh87FPx4.es.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.fr.srt` | `fr` | `translations/riJYh87FPx4.fr.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.it.srt` | `it` | `translations/riJYh87FPx4.it.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.ja.srt` | `ja` | `translations/riJYh87FPx4.ja.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.ko.srt` | `ko` | `translations/riJYh87FPx4.ko.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.nl.srt` | `nl` | `translations/riJYh87FPx4.nl.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.pt.srt` | `pt` | `translations/riJYh87FPx4.pt.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.ru.srt` | `ru` | `translations/riJYh87FPx4.ru.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.zh-Hans.srt` | `zh-Hans` | `translations/riJYh87FPx4.zh-Hans.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |
| `ActInf Livestream _047.2 ~ Enactive-Dynamic Social Cognition_ Active Inference and Abduction.zh-Hant.srt` | `zh-Hant` | `translations/riJYh87FPx4.zh-Hant.srt` | token '_047.2' → '#047.2'; part riJYh87FPx4 is 'Livestream #047.2 ~ "Enactive-Dynamic Social Cognition and Active Inference"…' (parts share a title, token disambiguates) | high |

#### `Livestream/LiveStream_052` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.de.srt` | `de` | `translations/iHgxmn0ockg.de.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.es.srt` | `es` | `translations/iHgxmn0ockg.es.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.fr.srt` | `fr` | `translations/iHgxmn0ockg.fr.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.it.srt` | `it` | `translations/iHgxmn0ockg.it.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ja.srt` | `ja` | `translations/iHgxmn0ockg.ja.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ko.srt` | `ko` | `translations/iHgxmn0ockg.ko.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.nl.srt` | `nl` | `translations/iHgxmn0ockg.nl.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.pt.srt` | `pt` | `translations/iHgxmn0ockg.pt.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ru.srt` | `ru` | `translations/iHgxmn0ockg.ru.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hans.srt` | `zh-Hans` | `translations/iHgxmn0ockg.zh-Hans.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hant.srt` | `zh-Hant` | `translations/iHgxmn0ockg.zh-Hant.srt` | stem names **Livestream #053.1** but the file sits in the LiveStream_052 item — misfiled; LiveStream_053 part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' ⚠ **REHOME → `Livestream/LiveStream_053`** — cross-item rehome: metadata `previous_paths` goes in the **LiveStream_053** item | high |

#### `Livestream/LiveStream_053` — 22 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.de.srt` | `de` | `translations/c7ybFyP9KrI.de.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.es.srt` | `es` | `translations/c7ybFyP9KrI.es.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.fr.srt` | `fr` | `translations/c7ybFyP9KrI.fr.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.it.srt` | `it` | `translations/c7ybFyP9KrI.it.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ja.srt` | `ja` | `translations/c7ybFyP9KrI.ja.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ko.srt` | `ko` | `translations/c7ybFyP9KrI.ko.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.nl.srt` | `nl` | `translations/c7ybFyP9KrI.nl.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.pt.srt` | `pt` | `translations/c7ybFyP9KrI.pt.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ru.srt` | `ru` | `translations/c7ybFyP9KrI.ru.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hans.srt` | `zh-Hans` | `translations/c7ybFyP9KrI.zh-Hans.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053 0 'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hant.srt` | `zh-Hant` | `translations/c7ybFyP9KrI.zh-Hant.srt` | token '053 0' → '#053.0'; part c7ybFyP9KrI is 'Livestream #053.0 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.de.srt` | `de` | `translations/iHgxmn0ockg.de.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.es.srt` | `es` | `translations/iHgxmn0ockg.es.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.fr.srt` | `fr` | `translations/iHgxmn0ockg.fr.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.it.srt` | `it` | `translations/iHgxmn0ockg.it.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ja.srt` | `ja` | `translations/iHgxmn0ockg.ja.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ko.srt` | `ko` | `translations/iHgxmn0ockg.ko.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.nl.srt` | `nl` | `translations/iHgxmn0ockg.nl.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.pt.srt` | `pt` | `translations/iHgxmn0ockg.pt.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.ru.srt` | `ru` | `translations/iHgxmn0ockg.ru.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hans.srt` | `zh-Hans` | `translations/iHgxmn0ockg.zh-Hans.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |
| `ActInf Livestream 053.1 ~  'Snakes and Ladders in Paleoanthropology' & 'To copy or not to copy'.zh-Hant.srt` | `zh-Hant` | `translations/iHgxmn0ockg.zh-Hant.srt` | token '053.1' → '#053.1'; part iHgxmn0ockg is 'Livestream #053.1 ~ Snakes and Ladders…' | high |

#### `Livestream/LiveStream_054` — 34 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.de.srt` | `de` | `translations/HK9ZkbxieLY.de.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.es.srt` | `es` | `translations/HK9ZkbxieLY.es.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.fr.srt` | `fr` | `translations/HK9ZkbxieLY.fr.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.it.srt` | `it` | `translations/HK9ZkbxieLY.it.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.ja.srt` | `ja` | `translations/HK9ZkbxieLY.ja.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.ko.srt` | `ko` | `translations/HK9ZkbxieLY.ko.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.nl.srt` | `nl` | `translations/HK9ZkbxieLY.nl.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.pt.srt` | `pt` | `translations/HK9ZkbxieLY.pt.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.ru.srt` | `ru` | `translations/HK9ZkbxieLY.ru.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.zh-Hans.srt` | `zh-Hans` | `translations/HK9ZkbxieLY.zh-Hans.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.0 ~ Compositional Account of the Bayesian Brain - Smithe.zh-Hant.srt` | `zh-Hant` | `translations/HK9ZkbxieLY.zh-Hant.srt` | token '054.0' matches part 'Livestream #054.0 ~ Mathematical Foundations for a Compositional Account of the Bayesian Brain' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).de.srt` | `de` | `translations/GfImcptiLsY.de.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).es.srt` | `es` | `translations/GfImcptiLsY.es.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).fr.srt` | `fr` | `translations/GfImcptiLsY.fr.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).it.srt` | `it` | `translations/GfImcptiLsY.it.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).ja.srt` | `ja` | `translations/GfImcptiLsY.ja.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).ko.srt` | `ko` | `translations/GfImcptiLsY.ko.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).nl.srt` | `nl` | `translations/GfImcptiLsY.nl.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).pt.srt` | `pt` | `translations/GfImcptiLsY.pt.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).ru.srt` | `ru` | `translations/GfImcptiLsY.ru.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).zh-Hans.srt` | `zh-Hans` | `translations/GfImcptiLsY.zh-Hans.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `Active Inference LiveStream 054.2 ~ “...Compositional Account of the Bayesian Brain” (Smithe).zh-Hant.srt` | `zh-Hant` | `translations/GfImcptiLsY.zh-Hant.srt` | token '054.2' matches part 'Livestream #054.2' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.de.srt` | `de` | `translations/fzFDvJhrn0U.de.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.en(ie).srt` | `en` | `translations/fzFDvJhrn0U.en.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.es.srt` | `es` | `translations/fzFDvJhrn0U.es.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.fr.srt` | `fr` | `translations/fzFDvJhrn0U.fr.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.it.srt` | `it` | `translations/fzFDvJhrn0U.it.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.ja.srt` | `ja` | `translations/fzFDvJhrn0U.ja.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.ko.srt` | `ko` | `translations/fzFDvJhrn0U.ko.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.nl.srt` | `nl` | `translations/fzFDvJhrn0U.nl.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.pt.srt` | `pt` | `translations/fzFDvJhrn0U.pt.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.ru.srt` | `ru` | `translations/fzFDvJhrn0U.ru.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.zh-Hans.srt` | `zh-Hans` | `translations/fzFDvJhrn0U.zh-Hans.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |
| `ls054 1 Compositional Account of the Bayesian Brain Smithe.zh-Hant.srt` | `zh-Hant` | `translations/fzFDvJhrn0U.zh-Hant.srt` | 'ls054 1' → '#054.1'; part fzFDvJhrn0U is 'Livestream #054.1' | high |

### Series: `MathStream`


#### `MathStream/MathStream_002` — 3 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInfLab MathStream #002.1 ~ Shanna Dobson.chi(translated-Simp).chi(translated).srt` | `zh-Hans` (chi → zh-Hans (Simp qualifier)) | `translations/RQb6wLWoYok.zh-Hans.srt` | sole part of the item (RQb6wLWoYok) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=RQb6wLWoYok before moving. Filenames carry Simp/Trad qualifiers: chi(translated-Simp) → zh-Hans, chi(translated-Trad) → zh-Hant | med |
| `ActInfLab MathStream #002.1 ~ Shanna Dobson.chi(translated-Trad) (2).chi(translated).srt` | `zh-Hant` (chi → zh-Hant (Trad qualifier)) | `translations/RQb6wLWoYok.zh-Hant.srt` | sole part of the item (RQb6wLWoYok) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=RQb6wLWoYok before moving. Filenames carry Simp/Trad qualifiers: chi(translated-Simp) → zh-Hans, chi(translated-Trad) → zh-Hant | med |
| `ActInfLab MathStream #002.1 ~ Shanna Dobson.ger(translated).ger(translated).srt` | `de` (legacy 3-letter code) | `translations/RQb6wLWoYok.de.srt` | sole part of the item (RQb6wLWoYok) but its metadata title is **empty** — confirm identity at https://www.youtube.com/watch?v=RQb6wLWoYok before moving. Filenames carry Simp/Trad qualifiers: chi(translated-Simp) → zh-Hans, chi(translated-Trad) → zh-Hant | med |

#### `MathStream/MathStream_003` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.chi(translated-Simp).chi(translated).srt` | `zh-Hans` (chi → zh-Hans (Simp qualifier)) | `translations/bBE2w_BpuAw.zh-Hans.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.chi(translated-Trad) (2).chi(translated).srt` | `zh-Hant` (chi → zh-Hant (Trad qualifier)) | `translations/bBE2w_BpuAw.zh-Hant.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.dut(translated).dut(translated).srt` | `nl` (legacy 3-letter code) | `translations/bBE2w_BpuAw.nl.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.fre(translated).fre(translated).srt` | `fr` (legacy 3-letter code) | `translations/bBE2w_BpuAw.fr.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.ger(translated).ger(translated).srt` | `de` (legacy 3-letter code) | `translations/bBE2w_BpuAw.de.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.ita(translated).ita(translated).srt` | `it` (legacy 3-letter code) | `translations/bBE2w_BpuAw.it.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.jpn(translated).jpn(translated).srt` | `ja` (legacy 3-letter code) | `translations/bBE2w_BpuAw.ja.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.kor(translated).kor(translated).srt` | `ko` (legacy 3-letter code) | `translations/bBE2w_BpuAw.ko.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.por(translated).por(translated).srt` | `pt` (legacy 3-letter code) | `translations/bBE2w_BpuAw.pt.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.rus(translated).rus(translated).srt` | `ru` (legacy 3-letter code) | `translations/bBE2w_BpuAw.ru.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |
| `ActInfLab MathStream #003.1 ~ Shanna Dobson et al.spa(translated).spa(translated).srt` | `es` (legacy 3-letter code) | `translations/bBE2w_BpuAw.es.srt` | sole part of the item (bBE2w_BpuAw), title **empty** in metadata — confirm identity at https://www.youtube.com/watch?v=bBE2w_BpuAw before moving | med |

### Series: `ModelStream`


#### `ModelStream/ModelStream_007` — 11 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.de.srt` | `de` | `translations/uX8iSoDR83g.de.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.es.srt` | `es` | `translations/uX8iSoDR83g.es.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.fr.srt` | `fr` | `translations/uX8iSoDR83g.fr.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.it.srt` | `it` | `translations/uX8iSoDR83g.it.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.ja.srt` | `ja` | `translations/uX8iSoDR83g.ja.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.ko.srt` | `ko` | `translations/uX8iSoDR83g.ko.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.nl.srt` | `nl` | `translations/uX8iSoDR83g.nl.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.pt.srt` | `pt` | `translations/uX8iSoDR83g.pt.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.ru.srt` | `ru` | `translations/uX8iSoDR83g.ru.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.zh-Hans.srt` | `zh-Hans` | `translations/uX8iSoDR83g.zh-Hans.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |
| `mo007-2_Active Inference ModelStream 007.2 ~ Conor Heins, pymdp.zh-Hant.srt` | `zh-Hant` | `translations/uX8iSoDR83g.zh-Hant.srt` | token '007.2' matches part 'ModelStream #007.2 ~ pymdp' uniquely (parts #007.1/#007.2/#007.3 share the title) | high |

#### `ModelStream/ModelStream_008` — 22 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.de.srt` | `de` | `translations/Fh1e4sKh3Vs.de.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.es.srt` | `es` | `translations/Fh1e4sKh3Vs.es.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.fr.srt` | `fr` | `translations/Fh1e4sKh3Vs.fr.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.it.srt` | `it` | `translations/Fh1e4sKh3Vs.it.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ja.srt` | `ja` | `translations/Fh1e4sKh3Vs.ja.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ko.srt` | `ko` | `translations/Fh1e4sKh3Vs.ko.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.nl.srt` | `nl` | `translations/Fh1e4sKh3Vs.nl.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.pt.srt` | `pt` | `translations/Fh1e4sKh3Vs.pt.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ru.srt` | `ru` | `translations/Fh1e4sKh3Vs.ru.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hans.srt` | `zh-Hans` | `translations/Fh1e4sKh3Vs.zh-Hans.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `ActInf ModelStream #008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hant.srt` | `zh-Hant` | `translations/Fh1e4sKh3Vs.zh-Hant.srt` | machine-flagged ambiguous: two parts share '#008.1' — but only Fh1e4sKh3Vs is titled 'Reward is Not Necessary: A Compositional Theory…' (Ringstrom's paper); the other #008.1 part is 'Online Generalised Predictive Coding'. Verify by spot-checking the video | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.de.srt` | `de` | `translations/Fh1e4sKh3Vs.de.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.es.srt` | `es` | `translations/Fh1e4sKh3Vs.es.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.fr.srt` | `fr` | `translations/Fh1e4sKh3Vs.fr.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.it.srt` | `it` | `translations/Fh1e4sKh3Vs.it.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ja.srt` | `ja` | `translations/Fh1e4sKh3Vs.ja.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ko.srt` | `ko` | `translations/Fh1e4sKh3Vs.ko.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.nl.srt` | `nl` | `translations/Fh1e4sKh3Vs.nl.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.pt.srt` | `pt` | `translations/Fh1e4sKh3Vs.pt.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.ru.srt` | `ru` | `translations/Fh1e4sKh3Vs.ru.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hans.srt` | `zh-Hans` | `translations/Fh1e4sKh3Vs.zh-Hans.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |
| `mo008-1_ActInf ModelStream 008.1 ~ Tom Ringstrom ~ Reward is Not Necessary.zh-Hant.srt` | `zh-Hant` | `translations/Fh1e4sKh3Vs.zh-Hant.srt` | same as above — title 'Reward is Not Necessary' selects Fh1e4sKh3Vs among the two '#008.1' parts | med |

#### `ModelStream/ModelStream_009` — 22 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.de.srt` | `de` | `translations/CEKWhxnH3-E.de.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.es.srt` | `es` | `translations/CEKWhxnH3-E.es.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.fr.srt` | `fr` | `translations/CEKWhxnH3-E.fr.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.it.srt` | `it` | `translations/CEKWhxnH3-E.it.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ja.srt` | `ja` | `translations/CEKWhxnH3-E.ja.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ko.srt` | `ko` | `translations/CEKWhxnH3-E.ko.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.nl.srt` | `nl` | `translations/CEKWhxnH3-E.nl.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.pt.srt` | `pt` | `translations/CEKWhxnH3-E.pt.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ru.srt` | `ru` | `translations/CEKWhxnH3-E.ru.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hans.srt` | `zh-Hans` | `translations/CEKWhxnH3-E.zh-Hans.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hant.srt` | `zh-Hant` | `translations/CEKWhxnH3-E.zh-Hant.srt` | two parts share '#009.1'; title 'On efficient computation in active inference' selects CEKWhxnH3-E (the other is 'Formal Verification … in PRISM') | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.de.srt` | `de` | `translations/CEKWhxnH3-E.de.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.es.srt` | `es` | `translations/CEKWhxnH3-E.es.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.fr.srt` | `fr` | `translations/CEKWhxnH3-E.fr.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.it.srt` | `it` | `translations/CEKWhxnH3-E.it.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ja.srt` | `ja` | `translations/CEKWhxnH3-E.ja.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ko.srt` | `ko` | `translations/CEKWhxnH3-E.ko.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.nl.srt` | `nl` | `translations/CEKWhxnH3-E.nl.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.pt.srt` | `pt` | `translations/CEKWhxnH3-E.pt.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.ru.srt` | `ru` | `translations/CEKWhxnH3-E.ru.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hans.srt` | `zh-Hans` | `translations/CEKWhxnH3-E.zh-Hans.srt` | same — title match selects CEKWhxnH3-E | med |
| `mo009-1_ActInf ModelStream 009.1 ~ Aswin Paul  On efficient computation in active inference.zh-Hant.srt` | `zh-Hant` | `translations/CEKWhxnH3-E.zh-Hant.srt` | same — title match selects CEKWhxnH3-E | med |

### Series: `TextbookGroup`


#### `TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_001` — 8 files

| File (in `Translations/`) | Lang | Likely target | Best guess & evidence | Conf |
|---|---|---|---|---|
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).es.srt` | `es` | `translations/G9GfOMjF4g0.es.srt` | stem says **Cohort 3** but the file sits in the Cohort_1 item — title-exact match: Cohort_3/Meeting_001 part G9GfOMjF4g0 is 'ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)' ⚠ **REHOME → `TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_001`** — cross-item rehome: metadata `previous_paths` goes in the **Cohort_3/Meeting_001** item | high |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).fr.srt` | `fr` | `translations/G9GfOMjF4g0.fr.srt` | stem says **Cohort 3** but the file sits in the Cohort_1 item — title-exact match: Cohort_3/Meeting_001 part G9GfOMjF4g0 is 'ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)' ⚠ **REHOME → `TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_001`** — cross-item rehome: metadata `previous_paths` goes in the **Cohort_3/Meeting_001** item | high |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).it.srt` | `it` | `translations/G9GfOMjF4g0.it.srt` | stem says **Cohort 3** but the file sits in the Cohort_1 item — title-exact match: Cohort_3/Meeting_001 part G9GfOMjF4g0 is 'ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)' ⚠ **REHOME → `TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_001`** — cross-item rehome: metadata `previous_paths` goes in the **Cohort_3/Meeting_001** item | high |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).nl.srt` | `nl` | `translations/G9GfOMjF4g0.nl.srt` | stem says **Cohort 3** but the file sits in the Cohort_1 item — title-exact match: Cohort_3/Meeting_001 part G9GfOMjF4g0 is 'ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)' ⚠ **REHOME → `TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_001`** — cross-item rehome: metadata `previous_paths` goes in the **Cohort_3/Meeting_001** item | high |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).pt.srt` | `pt` | `translations/G9GfOMjF4g0.pt.srt` | stem says **Cohort 3** but the file sits in the Cohort_1 item — title-exact match: Cohort_3/Meeting_001 part G9GfOMjF4g0 is 'ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)' ⚠ **REHOME → `TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_001`** — cross-item rehome: metadata `previous_paths` goes in the **Cohort_3/Meeting_001** item | high |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).ru.srt` | `ru` | `translations/G9GfOMjF4g0.ru.srt` | stem says **Cohort 3** but the file sits in the Cohort_1 item — title-exact match: Cohort_3/Meeting_001 part G9GfOMjF4g0 is 'ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)' ⚠ **REHOME → `TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_001`** — cross-item rehome: metadata `previous_paths` goes in the **Cohort_3/Meeting_001** item | high |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).zh-Hans.srt` | `zh-Hans` | `translations/G9GfOMjF4g0.zh-Hans.srt` | stem says **Cohort 3** but the file sits in the Cohort_1 item — title-exact match: Cohort_3/Meeting_001 part G9GfOMjF4g0 is 'ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)' ⚠ **REHOME → `TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_001`** — cross-item rehome: metadata `previous_paths` goes in the **Cohort_3/Meeting_001** item | high |
| `ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding).zh-Hant.srt` | `zh-Hant` | `translations/G9GfOMjF4g0.zh-Hant.srt` | stem says **Cohort 3** but the file sits in the Cohort_1 item — title-exact match: Cohort_3/Meeting_001 part G9GfOMjF4g0 is 'ActInf Textbook Group ~ Cohort 3 ~ Meeting 1 (Welcome and Onboarding)' ⚠ **REHOME → `TextbookGroup/ParrPezzuloFriston2022/Cohort_3/Meeting_001`** — cross-item rehome: metadata `previous_paths` goes in the **Cohort_3/Meeting_001** item | high |

_412 REMAINING file rows listed above; 11 files with no verified home are listed in Part C._


---

## Part B — CONFLICTS: 600 quarantined files (version conflicts)


Pass 2b quarantined 600 files that collided with an already-migrated file at their destination. On disk each
copy lives at `<item>/translations/conflicts/<Series>/<md5-8>-<original name>.srt`; the original
`Translations/` path it came from is recoverable from the name. The item is already known (it is the item
whose quarantine folder holds the file) — the task is to decide **which version wins** for a given
`<video_id>.<bcp47>` target.


### Reason playbook

| Quarantine reason | Files | What it means | Volunteer resolution |
|---|---|---|---|

| `multiple-versions-no-dump` | 301 | Two+ genuinely different versions of the same translation, no dump-derived file migrated for that target | Pick the canonical version (prefer the fuller/newer one), move it into `translations/<vid>.<lang>.srt` via the two-step `git mv` + `previous_paths`; byte-compare the runner-up — if it is genuinely a different earlier version, delete it and note the decision in the PR (do not keep both under one target name) |

| `superseded-by-dump` | 187 | A dump-derived file was migrated to the target; this legacy variant probably predates it | Byte-compare with the existing `translations/<vid>.<lang>.srt` (or `….<talkslug>.srt`). Same lineage → **delete** the quarantined copy, note in PR. Genuinely different/earlier full version → move in under a `<vid>.<lang>.<talkslug>.srt` variant name |

| `rescue-version-conflict:episode-token` | 60 | A cross-item rescue (misfiled-file repair) collided with an existing file at the destination | Same as `multiple-versions-no-dump`, but first re-verify that the rescue destination (episode token) is right |

| `dump-variant` | 22 | A variant of a dump file (duplicate upload, AutoCaption, etc.) | Byte-compare; usually delete as redundant, else keep under a talkslug/variant name |

| `multiple-dump-versions` | 16 | Two dump-derived files for one target | Keep the fuller/newer, delete the other after recording the decision in the PR |

| `rescue-dest-occupied` | 10 | Rescue target slot occupied by an earlier rescue | Compare the two rescued candidates, keep one |

| `byte-identical-extra` | 4 | Exact duplicate of an already-migrated file | Verify `md5` equality with the migrated file, then **delete** |


Every deletion happens with `git rm` inside the same path-scoped PR, with the decision stated in the PR body.



### Series: `Applied Active Inference Symposium`


#### `Applied Active Inference Symposium/2023 Ecosystem Symposium/First_Interval` — 51 quarantined, 1 part(s): `rIemcswLfGg`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Applied Active Inference Symposium/cb8e1524-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).de.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/7fdfe7f3-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).es.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/85ede8b0-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).fr.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/4059a7db-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).it.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/88bd62c7-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).ja.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/d39299ba-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).ko.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/39604978-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).nl.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/a84e2b5a-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).pt.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/4032f645-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).ru.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/1f2c440e-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).zh-Hans.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/fdb11f20-3Symp_1_01_Int1-Sess01-AndreBastos.wav.en(ca).zh-Hant.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/22b68fa8-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).de.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/5edd2362-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).es.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/ec3e6e41-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).fr.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/5931c3da-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).it.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/11dc0afa-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).ja.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/26c02016-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).ko.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/e4494eca-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).nl.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/1af05d01-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).pt.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/ce246005-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).ru.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/19702594-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).zh-Hans.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/0f001468-3Symp_1_02_Int1-Sess02-KeithDuggar.wav.en(ca).zh-Hant.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.28 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/df01d83a-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).de.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/7a1d992c-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).es.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/c635ee05-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).fr.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/814f6da5-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).it.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/49e15ee6-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).ja.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/cefe8b07-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).ko.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/fce13fe8-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).nl.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/6a5f1bb7-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).pt.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/1d2aa9a4-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).ru.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/206d9135-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).zh-Hans.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/ea14b76d-3Symp_1_03_Int1-Sess03-SanjeevNamjoshi.wav.en(ca).zh-Hant.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.27 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/4b51ddb4-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).de.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/de00bfcf-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).es.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/09d59ad1-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).fr.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/e0952a4f-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).it.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/ef8389a0-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).ja.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/02197401-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).ko.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/e77bf855-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).nl.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/864de271-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).pt.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/9adcaac5-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).ru.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/c048c73d-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).zh-Hans.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/0e1928c3-3Symp_1_04_Int1-Sess04-InesHipolito.wav.en(ca).zh-Hant.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.29 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/4b444233-3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).de.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.30 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/ce28dff5-3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).es.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.30 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/8cc99aac-3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).fr.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.30 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/804e893b-3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).it.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.30 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/c86f0dc3-3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).nl.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.30 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/c4b828e3-3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).pt.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.30 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |
| `translations/conflicts/Applied Active Inference Symposium/cbad3087-3Symp_1_05_Int1-Sess05-Aswin Paul.wav.en(ca).ru.srt` | superseded-by-dump | `rIemcswLfGg` (title similarity 0.30 — verify) | `rIemcswLfGg.<bcp47>.<NN-speaker>.srt` — follow the item's existing talkslugs |

### Series: `Courses`


#### `Courses/ActiveInferenceForTheSocialSciences/ActInf_Basics_Lecture` — 11 quarantined, 1 part(s): `BNLnbOFdgc0`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Courses/3b1f1043-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.de.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/af398c54-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.es.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/3b1f1043-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.fr.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/8e0648ac-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.it.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/3b1f1043-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.ja.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/3b1f1043-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.ko.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/3b1f1043-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.nl.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/3b1f1043-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.pt.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/3b1f1043-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.ru.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/3b1f1043-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.zh-Hans.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |
| `translations/conflicts/Courses/3b1f1043-AIFSS-02L_cPxLuwUDTSWYpG6-Z4rflqbxigh9K9-DDzkVzu5J1pA.zh-Hant.srt` | dump-variant | `BNLnbOFdgc0` (title similarity 0.10 — verify) | `BNLnbOFdgc0.<bcp47>.srt` |

#### `Courses/ActiveInferenceForTheSocialSciences/CollectiveBehavior_Discussion` — 16 quarantined, 1 part(s): `2IxxzY2ZDHA`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.de.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.es.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.fr.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.it.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ja.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ko.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/5f2557fb-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.de.srt` | superseded-by-dump | `2IxxzY2ZDHA` (title similarity 0.81 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/5f2557fb-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.es.srt` | superseded-by-dump | `2IxxzY2ZDHA` (title similarity 0.81 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/5f2557fb-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.fr.srt` | superseded-by-dump | `2IxxzY2ZDHA` (title similarity 0.81 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/78957c20-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.it.srt` | superseded-by-dump | `2IxxzY2ZDHA` (title similarity 0.81 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/5f2557fb-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.m4a.sentences.csv_transcript.pt.srt` | superseded-by-dump | `2IxxzY2ZDHA` (title similarity 0.81 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.nl.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.pt.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.ru.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hans.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |
| `translations/conflicts/Courses/c26a3e9b-Basics2023-05_Collective Behavior Discussion ~ Daniel Friedman ~ Active Inference for the Social Sciences 2023.zh-Hant.srt` | dump-variant | `2IxxzY2ZDHA` (title similarity 0.93 — verify) | `2IxxzY2ZDHA.<bcp47>.srt` |

### Series: `GuestStream`


#### `GuestStream/GuestStream_013` — 2 quarantined, 1 part(s): `eVbWeWEX9dA`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/GuestStream/ddd0da00-ActInfLab GuestStream #013.1 ~ Adam Safron.chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `eVbWeWEX9dA` (episode-token match) | `eVbWeWEX9dA.<bcp47>.srt` |
| `translations/conflicts/GuestStream/70e6ff3c-ActInfLab GuestStream #013.1 ~ Adam Safron.chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `eVbWeWEX9dA` (episode-token match) | `eVbWeWEX9dA.<bcp47>.srt` |

### Series: `Livestream`


#### `Livestream/LiveStream_001` — 17 quarantined, 1 part(s): `C94WDXAe4EE`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/8d4770e1-Active Inference Podcast #001 “Narrative as active inference.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/cd957bad-Active Inference Podcast #001 “Narrative as active inference.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/002bbbc8-Active Inference Podcast #001 “Narrative as active inference.dut(translated).dut(translated).srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/38d5af2e-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).de.srt` | superseded-by-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/45fb7977-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).es.srt` | superseded-by-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/fe9955a0-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).fr.srt` | superseded-by-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/a9f4833f-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).it.srt` | superseded-by-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/19ca8410-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/1925340a-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/10143db5-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/d8d5ca24-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/9181245c-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/55765505-Active Inference Podcast #001 “Narrative as active inference.eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/41b6280e-Active Inference Podcast #001 “Narrative as active inference.jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/a37040c7-Active Inference Podcast #001 “Narrative as active inference.kor(translated).kor(translated).srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/c2a6f196-Active Inference Podcast #001 “Narrative as active inference.por(translated).por(translated).srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |
| `translations/conflicts/Livestream/016d7c19-Active Inference Podcast #001 “Narrative as active inference.rus(translated).rus(translated).srt` | multiple-versions-no-dump | `C94WDXAe4EE` (title similarity 0.78 — verify) | `C94WDXAe4EE.<bcp47>.srt` |

#### `Livestream/LiveStream_002` — 11 quarantined, 1 part(s): `601-lt_8eVE`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/e8258c5b-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).de.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/c3ba044f-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).es.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/f9f5c4e4-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).fr.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/05a6dc68-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).it.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/b0f45041-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).ja.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/5f38a378-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).ko.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/60237afc-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).nl.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/853abbcf-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).pt.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/0823f24c-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).ru.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/59a9c44e-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).zh-Hans.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |
| `translations/conflicts/Livestream/6248fbd2-ActInfLab Livestream #002.1  Is the free-energy principle a formal theory of semantics.eng(transcribed).eng(transcribed).zh-Hant.srt` | superseded-by-dump | `601-lt_8eVE` (episode-token match) | `601-lt_8eVE.<bcp47>.srt` |

#### `Livestream/LiveStream_003` — 6 quarantined, 2 part(s): `mz7L4GD5g-E`, `ijuxHfPDd3U`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/a93082bd-ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).de.srt` | superseded-by-dump | `ijuxHfPDd3U` (episode-token match) | `ijuxHfPDd3U.<bcp47>.srt` |
| `translations/conflicts/Livestream/a25a77c9-ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).es.srt` | superseded-by-dump | `ijuxHfPDd3U` (episode-token match) | `ijuxHfPDd3U.<bcp47>.srt` |
| `translations/conflicts/Livestream/12bd6499-ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).fr.srt` | superseded-by-dump | `ijuxHfPDd3U` (episode-token match) | `ijuxHfPDd3U.<bcp47>.srt` |
| `translations/conflicts/Livestream/5b75cbb4-ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).it.srt` | superseded-by-dump | `ijuxHfPDd3U` (episode-token match) | `ijuxHfPDd3U.<bcp47>.srt` |
| `translations/conflicts/Livestream/7e79d978-ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.eng(transcribed).eng(transcribed).nl.srt` | superseded-by-dump | `ijuxHfPDd3U` (episode-token match) | `ijuxHfPDd3U.<bcp47>.srt` |
| `translations/conflicts/Livestream/5730d716-ActInfLab Livestream #003.2   A World Unto Itself Human Communication as Active Inference.ger(translated).ger(translated).srt` | superseded-by-dump | `ijuxHfPDd3U` (episode-token match) | `ijuxHfPDd3U.<bcp47>.srt` |

#### `Livestream/LiveStream_004` — 18 quarantined, 2 part(s): `Y6qx6C1tmjs`, `SAc1F1AWRAs`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/f97e19c4-Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).de.srt` | superseded-by-dump | `Y6qx6C1tmjs` (episode-token match) | `Y6qx6C1tmjs.<bcp47>.srt` |
| `translations/conflicts/Livestream/6475c8f3-Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).es.srt` | superseded-by-dump | `Y6qx6C1tmjs` (episode-token match) | `Y6qx6C1tmjs.<bcp47>.srt` |
| `translations/conflicts/Livestream/54c8620f-Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).fr.srt` | superseded-by-dump | `Y6qx6C1tmjs` (episode-token match) | `Y6qx6C1tmjs.<bcp47>.srt` |
| `translations/conflicts/Livestream/7c155a61-Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).it.srt` | superseded-by-dump | `Y6qx6C1tmjs` (episode-token match) | `Y6qx6C1tmjs.<bcp47>.srt` |
| `translations/conflicts/Livestream/af64500f-Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ja.srt` | superseded-by-dump | `Y6qx6C1tmjs` (episode-token match) | `Y6qx6C1tmjs.<bcp47>.srt` |
| `translations/conflicts/Livestream/da25f6ef-Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).nl.srt` | superseded-by-dump | `Y6qx6C1tmjs` (episode-token match) | `Y6qx6C1tmjs.<bcp47>.srt` |
| `translations/conflicts/Livestream/7d7f6825-Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).pt.srt` | superseded-by-dump | `Y6qx6C1tmjs` (episode-token match) | `Y6qx6C1tmjs.<bcp47>.srt` |
| `translations/conflicts/Livestream/38772a6c-Active Inference podcast #004.1 “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ru.srt` | superseded-by-dump | `Y6qx6C1tmjs` (episode-token match) | `Y6qx6C1tmjs.<bcp47>.srt` |
| `translations/conflicts/Livestream/7191dc52-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).de.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |
| `translations/conflicts/Livestream/f9cff681-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).es.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |
| `translations/conflicts/Livestream/842c83ee-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).fr.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |
| `translations/conflicts/Livestream/1adae862-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).it.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |
| `translations/conflicts/Livestream/5efc20ab-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ja.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |
| `translations/conflicts/Livestream/2ce589f9-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ko.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |
| `translations/conflicts/Livestream/4a23319c-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).nl.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |
| `translations/conflicts/Livestream/4ef4593d-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).pt.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |
| `translations/conflicts/Livestream/8a52dd1b-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).ru.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |
| `translations/conflicts/Livestream/db4bcb89-Active Inference podcast #004.2  “Cultural Affordances Scaffolding Local Worlds.eng(transcribed).eng(transcribed).zh-Hans.srt` | superseded-by-dump | `SAc1F1AWRAs` (episode-token match) | `SAc1F1AWRAs.<bcp47>.srt` |

#### `Livestream/LiveStream_005` — 63 quarantined, 3 part(s): `g2n47dPUyNY`, `B6Uqf_T-nec`, `V7yNq_KpHo8`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/f84b8cca-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/3ed2bff7-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/7afadb96-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/293d5741-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/a5d615e9-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/a9cf4afb-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/8afd26f7-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/cabba4b5-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/b9c40344-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/ab1eaacd-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/870dd766-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/f3e46bee-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/d5e4ac2b-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/11274d17-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/b1e3dd3a-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/4fcfac5e-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/ac9abdd7-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/2f56d7e9-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/8334d142-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).por(translated).por(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/79715725-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/575d9073-Active Inference podcast #005.0 Context for  Multiscale integration beyond internalism...  (2019).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `g2n47dPUyNY` (episode-token match) | `g2n47dPUyNY.<bcp47>.srt` |
| `translations/conflicts/Livestream/fd2d7569-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/a6c1cee8-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/69889f07-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/17e5afb9-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/026fcb12-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/1404164e-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/f2f197bb-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/4df080e0-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/924dee1e-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/c00a70e0-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/3ef3b0d5-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/d2ff9dc3-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/db177dda-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/12da783c-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/8b5c43a7-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/eabdb8e8-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/82ddf1a0-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/a5691982-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/9d36df8a-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).por(translated).por(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/e6a8ae08-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/7650ef7c-Active Inference podcast #005.1  Multiscale integration beyond internalism...  (2019).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `B6Uqf_T-nec` (episode-token match) | `B6Uqf_T-nec.<bcp47>.srt` |
| `translations/conflicts/Livestream/588cde6d-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/e5018fc9-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/81d5fbb1-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/249767d2-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/26cc66f5-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/f8bfe2d7-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/0f49d10f-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/d8b80c30-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/bb43e73a-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/d551425a-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/532b61b2-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/cbe1ff0c-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/de8570a0-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/a151247a-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/555f2558-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/72e0c7ad-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/44cbcf4c-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/b926caaf-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/c5f5ff6b-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).por(translated).por(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/3904dcba-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |
| `translations/conflicts/Livestream/e9925f9f-Active Inference podcast #005.2  Multiscale integration beyond internalism...  (2019).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `V7yNq_KpHo8` (episode-token match) | `V7yNq_KpHo8.<bcp47>.srt` |

#### `Livestream/LiveStream_006` — 21 quarantined, 4 part(s): `9IIsoNMRSb8`, `HQadNEGAtbY`, `y4tljwMAWho`, `jHWCQ1dpoK0`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/9091e16c-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/0886d3de-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/65f058a5-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.dut(translated).dut(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/f1cf3419-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/644eb6ce-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/e549a3c8-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/858b00d7-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/cae03d6c-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/52004f8a-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/65ae4a22-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/5c1c4373-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/c479093a-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/20d66050-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/f5e74a33-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.fre(translated).fre(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/eb9711eb-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.ger(translated).ger(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/0d8a7938-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.ita(translated).ita(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/0e5d299c-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/47516e7f-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.kor(translated).kor(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/0b41e062-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.por(translated).por(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/d66c54e8-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.rus(translated).rus(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |
| `translations/conflicts/Livestream/5becdcfd-ActInfLab Livestream #006.2  A tale of two densities  (2020) REUPLOAD.spa(translated).spa(translated).srt` | multiple-versions-no-dump | `HQadNEGAtbY` (episode-token ambiguous (2 candidate parts) — verify) | `HQadNEGAtbY.<bcp47>.srt` |

#### `Livestream/LiveStream_007` — 62 quarantined, 3 part(s): `7cJ8dmO3qlY`, `72g62XJ-SpA`, `qf4S9bK5VKQ`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/6242b488-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/01b02189-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/a52a0159-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/5442540b-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/8ce97ebd-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/c661b4ea-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/f180edcb-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/97233e5d-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/ea3a3d4f-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/1b9ccff4-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/469e7adf-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/4bf9ae99-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/eb251271-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/5827c968-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/a718fdeb-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/baf7349b-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/3a7321a4-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/14724911-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/85502f33-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).por(translated).por(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/66560e1a-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/6af3be67-Active Inference podcast #007.0  Variational ecology and the physics of sentient systems  (2019).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `7cJ8dmO3qlY` (episode-token match) | `7cJ8dmO3qlY.<bcp47>.srt` |
| `translations/conflicts/Livestream/cbb530ad-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/6156f2b3-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/4aa8de39-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/b932f774-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/f7985e72-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/c960c608-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/d07d3b96-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/e1c7d7a5-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/66484e51-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/804fa3d1-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/bab6fd34-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/4af4f01b-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/321ac6c4-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/68613603-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/1f82db9e-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/27a6fafb-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/ff8f29f4-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/55be38b0-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).por(translated).por(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/bdb19524-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/a7383956-Active Inference podcast #007.1  Variational ecology and the physics of sentient systems  (2019).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `72g62XJ-SpA` (episode-token match) | `72g62XJ-SpA.<bcp47>.srt` |
| `translations/conflicts/Livestream/2731e6e1-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/0b6b80ac-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/a1e2564f-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).de.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/e16cb355-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).dut(translated).dut(translated).srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/1fbf614e-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).de.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/f8f4c078-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).es.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/7c0ee79e-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).fr.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/60936991-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).it.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/85eaaee0-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ja.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/fc6ceb04-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ko.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/5d830e67-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).nl.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/2d6858d5-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).pt.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/37cac52b-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).ru.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/34b8aa12-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/0b304fac-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).fr.srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/c8c69717-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).ita(translated).ita(translated).srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/cd95ff46-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).jpn(translated).jpn(translated).srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/52a0b27b-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).kor(translated).kor(translated).srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/c4ad96f3-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).por(translated).por(translated).srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/353d7290-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).rus(translated).rus(translated).srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/99ea30a5-Active Inference podcast #007.2  Variational ecology and the physics of sentient systems  (2019).spa(translated).spa(translated).srt` | rescue-version-conflict:episode-token | `qf4S9bK5VKQ` (episode-token match) | `qf4S9bK5VKQ.<bcp47>.srt` |

#### `Livestream/LiveStream_008` — 63 quarantined, 3 part(s): `kXw1CPRkJCw`, `zG0qP7un91k`, `gv8RuRiZTQA`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/a9767f5b-Active Inference podcast #008.0 “Scaling active inference  (2019).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/cf9c5a5f-Active Inference podcast #008.0 “Scaling active inference  (2019).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/8dc5befc-Active Inference podcast #008.0 “Scaling active inference  (2019).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/b50d6a51-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/adace071-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/3ee95250-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/db8963fd-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/36a67bee-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/0d111a13-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/b45e31a7-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/5a1db8d8-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/3c0b861b-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/a7403ca7-Active Inference podcast #008.0 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/743f4999-Active Inference podcast #008.0 “Scaling active inference  (2019).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/e6e474c0-Active Inference podcast #008.0 “Scaling active inference  (2019).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/985137fd-Active Inference podcast #008.0 “Scaling active inference  (2019).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/6a6bb198-Active Inference podcast #008.0 “Scaling active inference  (2019).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/37f43dc1-Active Inference podcast #008.0 “Scaling active inference  (2019).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/c6c85035-Active Inference podcast #008.0 “Scaling active inference  (2019).por(translated).por(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/bae6a316-Active Inference podcast #008.0 “Scaling active inference  (2019).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/059bf551-Active Inference podcast #008.0 “Scaling active inference  (2019).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `kXw1CPRkJCw` (episode-token match) | `kXw1CPRkJCw.<bcp47>.srt` |
| `translations/conflicts/Livestream/bf039606-Active Inference podcast #008.1 “Scaling active inference  (2019).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/84bea8b1-Active Inference podcast #008.1 “Scaling active inference  (2019).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/9a96ccbf-Active Inference podcast #008.1 “Scaling active inference  (2019).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/c140e6f5-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/6188f792-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/9f0845ff-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/c925b3f8-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/b0e908b8-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/b5853f92-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/4e0c46a2-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/dceec3c5-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/a8beea7d-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/b2f5bfee-Active Inference podcast #008.1 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/ab314a79-Active Inference podcast #008.1 “Scaling active inference  (2019).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/50cb744a-Active Inference podcast #008.1 “Scaling active inference  (2019).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/da92e1f9-Active Inference podcast #008.1 “Scaling active inference  (2019).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/d860d609-Active Inference podcast #008.1 “Scaling active inference  (2019).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/c158bda6-Active Inference podcast #008.1 “Scaling active inference  (2019).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/d09634cc-Active Inference podcast #008.1 “Scaling active inference  (2019).por(translated).por(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/4b85ce4b-Active Inference podcast #008.1 “Scaling active inference  (2019).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/864fd6fb-Active Inference podcast #008.1 “Scaling active inference  (2019).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `zG0qP7un91k` (episode-token match) | `zG0qP7un91k.<bcp47>.srt` |
| `translations/conflicts/Livestream/06d0fffb-Active Inference podcast #008.2 “Scaling active inference  (2019).chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/4d0d3c29-Active Inference podcast #008.2 “Scaling active inference  (2019).chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/929254ad-Active Inference podcast #008.2 “Scaling active inference  (2019).dut(translated).dut(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/b4b36f0a-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).de.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/00f7891b-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).es.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/5a569a1e-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).fr.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/d54b4bc9-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).it.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/05c00928-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ja.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/4d431639-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ko.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/41395a2a-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).nl.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/0f6a8ea8-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).pt.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/9e8086b0-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).ru.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/edd380fa-Active Inference podcast #008.2 “Scaling active inference  (2019).eng(transcribed).eng(transcribed).zh-Hans.srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/9222112d-Active Inference podcast #008.2 “Scaling active inference  (2019).fre(translated).fre(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/05b30570-Active Inference podcast #008.2 “Scaling active inference  (2019).ger(translated).ger(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/471fb4a9-Active Inference podcast #008.2 “Scaling active inference  (2019).ita(translated).ita(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/b1fa461b-Active Inference podcast #008.2 “Scaling active inference  (2019).jpn(translated).jpn(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/e22fc021-Active Inference podcast #008.2 “Scaling active inference  (2019).kor(translated).kor(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/1ee1fc97-Active Inference podcast #008.2 “Scaling active inference  (2019).por(translated).por(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/8f29b6b2-Active Inference podcast #008.2 “Scaling active inference  (2019).rus(translated).rus(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |
| `translations/conflicts/Livestream/a1adaed6-Active Inference podcast #008.2 “Scaling active inference  (2019).spa(translated).spa(translated).srt` | rescue-version-conflict:episode-token | `gv8RuRiZTQA` (episode-token match) | `gv8RuRiZTQA.<bcp47>.srt` |

#### `Livestream/LiveStream_009` — 21 quarantined, 3 part(s): `XnOfWFnN2iI`, `pSWRTkmR8eg`, `XYRKlh2c-ps`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/d07316e6-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/870d0b0e-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/0d00909f-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/17e86f7b-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/5cca6aab-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/ca9cfdfd-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/5045ea25-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/4b8e89c8-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/d8ed26bd-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/d16b1f7f-Active Inference Stream #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/9b3537bb-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/c40d0eac-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/ec796621-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/6c452e81-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/cf3787f5-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/9a9d9db9-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/04bda75f-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/35ed7297-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/1330d7d5-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).por(translated).por(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/4540c8f6-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |
| `translations/conflicts/Livestream/2ebe2d40-Active Inference podcast #009.0 “The Projective Consciousness Model and Phenomenal Selfhood  (2018).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `XnOfWFnN2iI` (episode-token match) | `XnOfWFnN2iI.<bcp47>.srt` |

#### `Livestream/LiveStream_010` — 42 quarantined, 3 part(s): `5DB77oxbABo`, `IGKUS1W25rY`, `3Sg1sAlgQaM`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/d9ca933c-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/fed3bf28-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/4fe379b1-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/1313ff92-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/a1537979-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/d76569b4-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/97c4bc28-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/145dc127-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/9ae46527-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/4949799b-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/389836dc-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/c0274194-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/d9814f45-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/994e42c4-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/bfa880a9-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/1e99adb4-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/3fbfda8f-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/ae124d95-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/a2a2e5e4-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).por(translated).por(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/23ad407b-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/b12b1cc1-ActInfLab Livestream #010.0  A variational approach to scripts  (2020).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `5DB77oxbABo` (episode-token match) | `5DB77oxbABo.<bcp47>.srt` |
| `translations/conflicts/Livestream/0d352347-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/945e7822-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/b9b50a69-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).dut(translated).dut(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/0e012d58-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).de.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/346f4355-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).es.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/aa941541-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).fr.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/84c9e227-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).it.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/d8bd5b8a-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ja.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/4b26c280-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ko.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/096404f2-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).nl.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/0ba98ad6-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).pt.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/57bbb778-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).ru.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/44185d38-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).eng(transcribed).eng(transcribed).zh-Hans.srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/55f82364-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).fre(translated).fre(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/baa57ddc-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).ger(translated).ger(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/cbb7451d-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).ita(translated).ita(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/6f2d6706-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).jpn(translated).jpn(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/d02d8787-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).kor(translated).kor(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/8a9c0c8c-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).por(translated).por(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/ad9a58b5-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).rus(translated).rus(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |
| `translations/conflicts/Livestream/4520eb73-ActInfLab Livestream #010.2  A variational approach to scripts  (2020).spa(translated).spa(translated).srt` | multiple-versions-no-dump | `IGKUS1W25rY` (episode-token match) | `IGKUS1W25rY.<bcp47>.srt` |

#### `Livestream/LiveStream_011` — 2 quarantined, 3 part(s): `HSu9sDa6-BQ`, `xCqavxpiw44`, `gx9yAF607ko`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/77f62f5a-ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `xCqavxpiw44` (episode-token match) | `xCqavxpiw44.<bcp47>.srt` |
| `translations/conflicts/Livestream/65e910fb-ActInfLab Livestream #011.1  Sophisticated Affective Inference Simulating Anticipatory  (2020).chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `xCqavxpiw44` (episode-token match) | `xCqavxpiw44.<bcp47>.srt` |

#### `Livestream/LiveStream_013` — 6 quarantined, 3 part(s): `8dPps0qLrp4`, `QG2gOoX4XdA`, `PyyHd4P8dbs`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/6faa5ec9-ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `8dPps0qLrp4` (episode-token match) | `8dPps0qLrp4.<bcp47>.srt` |
| `translations/conflicts/Livestream/a043d495-ActInfLab Livestream #013.0  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `8dPps0qLrp4` (episode-token match) | `8dPps0qLrp4.<bcp47>.srt` |
| `translations/conflicts/Livestream/8525161d-ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `QG2gOoX4XdA` (episode-token match) | `QG2gOoX4XdA.<bcp47>.srt` |
| `translations/conflicts/Livestream/71e37330-ActInfLab Livestream #013.1  Cybernetic Big Five Theory with the Free Energy Principle....chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `QG2gOoX4XdA` (episode-token match) | `QG2gOoX4XdA.<bcp47>.srt` |
| `translations/conflicts/Livestream/cf9c2564-ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `PyyHd4P8dbs` (episode-token match) | `PyyHd4P8dbs.<bcp47>.srt` |
| `translations/conflicts/Livestream/5ca570be-ActInfLab Livestream #013.2  Cybernetic Big Five Theory with the Free Energy Principle.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `PyyHd4P8dbs` (episode-token match) | `PyyHd4P8dbs.<bcp47>.srt` |

#### `Livestream/LiveStream_014` — 6 quarantined, 3 part(s): `Uheml5XRCWk`, `gQQyd8Hd3AA`, `4Mu8lDqzBog`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/d85d9b1b-ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `Uheml5XRCWk` (episode-token match) | `Uheml5XRCWk.<bcp47>.srt` |
| `translations/conflicts/Livestream/a32693ff-ActInfLab Livestream #014.0 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `Uheml5XRCWk` (episode-token match) | `Uheml5XRCWk.<bcp47>.srt` |
| `translations/conflicts/Livestream/8e30875e-ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `gQQyd8Hd3AA` (episode-token match) | `gQQyd8Hd3AA.<bcp47>.srt` |
| `translations/conflicts/Livestream/35517ab1-ActInfLab Livestream #014.1 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `gQQyd8Hd3AA` (episode-token match) | `gQQyd8Hd3AA.<bcp47>.srt` |
| `translations/conflicts/Livestream/c7bed6e4-ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `4Mu8lDqzBog` (episode-token match) | `4Mu8lDqzBog.<bcp47>.srt` |
| `translations/conflicts/Livestream/f7b4e100-ActInfLab Livestream #014.2 ~ The Math is not the Territory Navigating the Free Energy Principle.chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `4Mu8lDqzBog` (episode-token match) | `4Mu8lDqzBog.<bcp47>.srt` |

#### `Livestream/LiveStream_015` — 6 quarantined, 3 part(s): `6Z-6p1XPn8A`, `5VPKmVoRvRY`, `iJp_Tm6Ej68`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/572c1da7-ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `6Z-6p1XPn8A` (episode-token match) | `6Z-6p1XPn8A.<bcp47>.srt` |
| `translations/conflicts/Livestream/30d3bea7-ActInfLab Livestream #015.0 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `6Z-6p1XPn8A` (episode-token match) | `6Z-6p1XPn8A.<bcp47>.srt` |
| `translations/conflicts/Livestream/766debe9-ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated) (2).chi(translated).srt` | rescue-dest-occupied | `5VPKmVoRvRY` (episode-token match) | `5VPKmVoRvRY.<bcp47>.srt` |
| `translations/conflicts/Livestream/d908e605-ActInfLab Livestream #015.1 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated).chi(translated).srt` | rescue-dest-occupied | `5VPKmVoRvRY` (episode-token match) | `5VPKmVoRvRY.<bcp47>.srt` |
| `translations/conflicts/Livestream/39d17d81-ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated) (2).chi(translated).srt` | rescue-dest-occupied | `iJp_Tm6Ej68` (episode-token match) | `iJp_Tm6Ej68.<bcp47>.srt` |
| `translations/conflicts/Livestream/8400397e-ActInfLab Livestream #015.2 ~ “Free-Energy Principle, Computationalism and Realism a Tragedy.chi(translated).chi(translated).srt` | rescue-dest-occupied | `iJp_Tm6Ej68` (episode-token match) | `iJp_Tm6Ej68.<bcp47>.srt` |

#### `Livestream/LiveStream_016` — 4 quarantined, 3 part(s): `i13aBAWuJxk`, `P6LiF4gTfUo`, `93lAa-xEmHY`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/1fbccdfc-ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `i13aBAWuJxk` (episode-token match) | `i13aBAWuJxk.<bcp47>.srt` |
| `translations/conflicts/Livestream/28d3a41d-ActInfLab Livestream #016.0 “Neural correlates of consciousness under the FEP.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `i13aBAWuJxk` (episode-token match) | `i13aBAWuJxk.<bcp47>.srt` |
| `translations/conflicts/Livestream/dd03d7b3-ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `P6LiF4gTfUo` (episode-token match) | `P6LiF4gTfUo.<bcp47>.srt` |
| `translations/conflicts/Livestream/72a5e866-ActInfLab Livestream #016.1 “Neural correlates of consciousness under the FEP.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `P6LiF4gTfUo` (episode-token match) | `P6LiF4gTfUo.<bcp47>.srt` |

#### `Livestream/LiveStream_017` — 4 quarantined, 3 part(s): `o7sJ-5vFJGk`, `ldg2An-tEIE`, `zF-EUnA-di4`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/dfed8f1c-ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `o7sJ-5vFJGk` (episode-token match) | `o7sJ-5vFJGk.<bcp47>.srt` |
| `translations/conflicts/Livestream/0ee3981e-ActInfLab Livestream #017.0 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `o7sJ-5vFJGk` (episode-token match) | `o7sJ-5vFJGk.<bcp47>.srt` |
| `translations/conflicts/Livestream/d1a70994-ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `ldg2An-tEIE` (episode-token match) | `ldg2An-tEIE.<bcp47>.srt` |
| `translations/conflicts/Livestream/57aeac9d-ActInfLab Livestream #017.1 ~ Information flow in context-dependent hierarchical Bayesian inference.chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `ldg2An-tEIE` (episode-token match) | `ldg2An-tEIE.<bcp47>.srt` |

#### `Livestream/LiveStream_018` — 6 quarantined, 3 part(s): `1z1MHiHiYuM`, `Y8Y4f-SEcsI`, `3iQBiClVHuo`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/d7b7c7eb-ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `1z1MHiHiYuM` (episode-token match) | `1z1MHiHiYuM.<bcp47>.srt` |
| `translations/conflicts/Livestream/1e41dac7-ActInfLab Livestream #018.0 ~ The predictive global neuronal workspace A formal act inf model.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `1z1MHiHiYuM` (episode-token match) | `1z1MHiHiYuM.<bcp47>.srt` |
| `translations/conflicts/Livestream/cec743cc-ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `Y8Y4f-SEcsI` (episode-token match) | `Y8Y4f-SEcsI.<bcp47>.srt` |
| `translations/conflicts/Livestream/a6c08020-ActInfLab Livestream #018.1 ~ The predictive global neuronal workspace A formal act inf model.chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `Y8Y4f-SEcsI` (episode-token match) | `Y8Y4f-SEcsI.<bcp47>.srt` |
| `translations/conflicts/Livestream/4aea81bf-ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `3iQBiClVHuo` (episode-token match) | `3iQBiClVHuo.<bcp47>.srt` |
| `translations/conflicts/Livestream/c278a10c-ActInfLab Livestream #018.2 ~ The predictive global neuronal workspace A formal act inf model.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `3iQBiClVHuo` (episode-token match) | `3iQBiClVHuo.<bcp47>.srt` |

#### `Livestream/LiveStream_019` — 6 quarantined, 3 part(s): `1FbOzAJ8CRQ`, `SMQvRspIzpQ`, `z_hArARMQ20`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/6eaf536e-ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `1FbOzAJ8CRQ` (episode-token match) | `1FbOzAJ8CRQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/70bdf664-ActInfLab Livestream #019.0 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `1FbOzAJ8CRQ` (episode-token match) | `1FbOzAJ8CRQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/ec8d945f-ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `SMQvRspIzpQ` (episode-token match) | `SMQvRspIzpQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/3ba2020f-ActInfLab Livestream #019.1 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `SMQvRspIzpQ` (episode-token match) | `SMQvRspIzpQ.<bcp47>.srt` |
| `translations/conflicts/Livestream/fe69490f-ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `z_hArARMQ20` (episode-token match) | `z_hArARMQ20.<bcp47>.srt` |
| `translations/conflicts/Livestream/8b36e885-ActInfLab Livestream #019.2 ~ Deeply Felt Affect The Emergence of Valence in Deep Active Inference.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `z_hArARMQ20` (episode-token match) | `z_hArARMQ20.<bcp47>.srt` |

#### `Livestream/LiveStream_020` — 6 quarantined, 3 part(s): `1VTviUyntt8`, `szCSh8pVEa4`, `q3qBepJf3vA`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/da41c0e7-ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `1VTviUyntt8` (episode-token match) | `1VTviUyntt8.<bcp47>.srt` |
| `translations/conflicts/Livestream/143d2a58-ActInfLab Livestream #020.0 ~ The Emperor’s New Markov Blankets.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `1VTviUyntt8` (episode-token match) | `1VTviUyntt8.<bcp47>.srt` |
| `translations/conflicts/Livestream/5a57fb25-ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `szCSh8pVEa4` (episode-token match) | `szCSh8pVEa4.<bcp47>.srt` |
| `translations/conflicts/Livestream/7082330f-ActInfLab Livestream #020.1 ~ The Emperor’s New Markov Blankets (full upload).chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `szCSh8pVEa4` (episode-token match) | `szCSh8pVEa4.<bcp47>.srt` |
| `translations/conflicts/Livestream/7535d433-ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `q3qBepJf3vA` (episode-token match) | `q3qBepJf3vA.<bcp47>.srt` |
| `translations/conflicts/Livestream/e137951b-ActInfLab Livestream #020.2 ~ The Emperor’s New Markov Blankets.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `q3qBepJf3vA` (episode-token match) | `q3qBepJf3vA.<bcp47>.srt` |

#### `Livestream/LiveStream_021` — 4 quarantined, 6 part(s): `z9ZCjd2rqGY`, `MlvyehPDQXg`, `idO34jucRIw`, `PakWPvu07OM`, `mbEqoCV16q4`, `i5WwQ4WXGNo`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/e80cd77c-ActInfLab Livestream #021.04 ~ John Boik.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `PakWPvu07OM` (episode-token match) | `PakWPvu07OM.<bcp47>.srt` |
| `translations/conflicts/Livestream/d238a7ef-ActInfLab Livestream #021.04 ~ John Boik.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `PakWPvu07OM` (episode-token match) | `PakWPvu07OM.<bcp47>.srt` |
| `translations/conflicts/Livestream/2635055c-ActInfLab Livestream #021.2 ~ John Boik.ger(translated) (2).ger(translated).srt` | multiple-versions-no-dump | `i5WwQ4WXGNo` (episode-token ambiguous (2 candidate parts) — verify) | `i5WwQ4WXGNo.<bcp47>.srt` |
| `translations/conflicts/Livestream/6d06ce25-ActInfLab Livestream #021.2 ~ John Boik.ger(translated).ger(translated).srt` | multiple-versions-no-dump | `i5WwQ4WXGNo` (episode-token ambiguous (2 candidate parts) — verify) | `i5WwQ4WXGNo.<bcp47>.srt` |

#### `Livestream/LiveStream_023` — 2 quarantined, 3 part(s): `8JrGE02KzuY`, `PgzQrHSu1CU`, `bjYUbKlfHUo`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/ff2fea04-ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `bjYUbKlfHUo` (episode-token match) | `bjYUbKlfHUo.<bcp47>.srt` |
| `translations/conflicts/Livestream/8822193e-ActInfLab Livestream #023.2 ~   Embodied skillful performance where the action is.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `bjYUbKlfHUo` (episode-token match) | `bjYUbKlfHUo.<bcp47>.srt` |

#### `Livestream/LiveStream_024` — 6 quarantined, 3 part(s): `Fx7xWUU1MlI`, `a089q9RaI14`, `lqxl8w_JGek`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/5c4684a0-ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `Fx7xWUU1MlI` (episode-token match) | `Fx7xWUU1MlI.<bcp47>.srt` |
| `translations/conflicts/Livestream/c96c1ccc-ActInfLab Livestream #024.0 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `Fx7xWUU1MlI` (episode-token match) | `Fx7xWUU1MlI.<bcp47>.srt` |
| `translations/conflicts/Livestream/5e85c8c8-ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated) (2).chi(translated).srt` | rescue-dest-occupied | `a089q9RaI14` (episode-token match) | `a089q9RaI14.<bcp47>.srt` |
| `translations/conflicts/Livestream/b50c165e-ActInfLab Livestream #024.1 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated).chi(translated).srt` | rescue-dest-occupied | `a089q9RaI14` (episode-token match) | `a089q9RaI14.<bcp47>.srt` |
| `translations/conflicts/Livestream/e92f4e01-ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `lqxl8w_JGek` (episode-token match) | `lqxl8w_JGek.<bcp47>.srt` |
| `translations/conflicts/Livestream/153ebc8b-ActInfLab Livestream #024.2 ~  An empirical evaluation of active inference in multi-armed bandits.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `lqxl8w_JGek` (episode-token match) | `lqxl8w_JGek.<bcp47>.srt` |

#### `Livestream/LiveStream_025` — 2 quarantined, 3 part(s): `4JfGs_m5QHo`, `v0oJvbVuAF0`, `XSYxOt8CRDI`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/e071f27e-ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.chi(translated) (2).chi(translated).srt` | rescue-dest-occupied | `v0oJvbVuAF0` (episode-token match) | `v0oJvbVuAF0.<bcp47>.srt` |
| `translations/conflicts/Livestream/4969b94d-ActInfLab Livestream #025.1 ~  The Computational Boundary of a Self.chi(translated).chi(translated).srt` | rescue-dest-occupied | `v0oJvbVuAF0` (episode-token match) | `v0oJvbVuAF0.<bcp47>.srt` |

#### `Livestream/LiveStream_026` — 2 quarantined, 3 part(s): `eZlG_J7sPj4`, `1rHz3Ir5v9c`, `SH2v6joMD4k`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/30572852-ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.chi(translated) (2).chi(translated).srt` | rescue-version-conflict:episode-token | `1rHz3Ir5v9c` (episode-token match) | `1rHz3Ir5v9c.<bcp47>.srt` |
| `translations/conflicts/Livestream/e89f67b6-ActInfLab Livestream #026.1 ~ “Bayesian Mechanics for Stationary Processes”.chi(translated).chi(translated).srt` | rescue-version-conflict:episode-token | `1rHz3Ir5v9c` (episode-token match) | `1rHz3Ir5v9c.<bcp47>.srt` |

#### `Livestream/LiveStream_029` — 6 quarantined, 3 part(s): `SNbfAkOokAI`, `Z0fpX5Lpp0Y`, `Z4S5JVoeGBw`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/3f7c9e55-ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `SNbfAkOokAI` (episode-token match) | `SNbfAkOokAI.<bcp47>.srt` |
| `translations/conflicts/Livestream/09cee538-ActInf Livestream #029.0 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `SNbfAkOokAI` (episode-token match) | `SNbfAkOokAI.<bcp47>.srt` |
| `translations/conflicts/Livestream/a12afd3e-ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `Z0fpX5Lpp0Y` (episode-token match) | `Z0fpX5Lpp0Y.<bcp47>.srt` |
| `translations/conflicts/Livestream/abd6e7bb-ActInf Livestream #029.1 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `Z0fpX5Lpp0Y` (episode-token match) | `Z0fpX5Lpp0Y.<bcp47>.srt` |
| `translations/conflicts/Livestream/587ca8bb-ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `Z4S5JVoeGBw` (episode-token match) | `Z4S5JVoeGBw.<bcp47>.srt` |
| `translations/conflicts/Livestream/d4e841aa-ActInf Livestream #029.2 ~ “Active Inferants An Active Inference Framework for Ant Colony Behavior”.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `Z4S5JVoeGBw` (episode-token match) | `Z4S5JVoeGBw.<bcp47>.srt` |

#### `Livestream/LiveStream_030` — 6 quarantined, 3 part(s): `N3WUpVH8-D8`, `5H164LqEwiA`, `VXLNOfkH5Rg`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/25865d3c-ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `N3WUpVH8-D8` (episode-token match) | `N3WUpVH8-D8.<bcp47>.srt` |
| `translations/conflicts/Livestream/dcd5f02d-ActInf Livestream #030.0 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated).chi(translated).srt` | multiple-versions-no-dump | `N3WUpVH8-D8` (episode-token match) | `N3WUpVH8-D8.<bcp47>.srt` |
| `translations/conflicts/Livestream/3b3a4aa3-ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated) (2).chi(translated).srt` | rescue-dest-occupied | `5H164LqEwiA` (episode-token match) | `5H164LqEwiA.<bcp47>.srt` |
| `translations/conflicts/Livestream/707a1c39-ActInf Livestream #030.1 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated).chi(translated).srt` | rescue-dest-occupied | `5H164LqEwiA` (episode-token match) | `5H164LqEwiA.<bcp47>.srt` |
| `translations/conflicts/Livestream/a5bcb5f9-ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `VXLNOfkH5Rg` (episode-token match) | `VXLNOfkH5Rg.<bcp47>.srt` |
| `translations/conflicts/Livestream/a907d754-ActInf Livestream #030.2 ~ “How to count biological minds symbiosis, the free energy principle....chi(translated).chi(translated).srt` | multiple-versions-no-dump | `VXLNOfkH5Rg` (episode-token match) | `VXLNOfkH5Rg.<bcp47>.srt` |

#### `Livestream/LiveStream_040` — 2 quarantined, 3 part(s): `-qZYxSbJ38E`, `NkJKl_yF274`, `Cgo-0UU848M`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/f3763cb4-ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `Cgo-0UU848M` (episode-token match) | `Cgo-0UU848M.<bcp47>.srt` |
| `translations/conflicts/Livestream/786b0e0b-ActInf Livestream #040.2 ~  A free energy principle for generic quantum systems.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `Cgo-0UU848M` (episode-token match) | `Cgo-0UU848M.<bcp47>.srt` |

#### `Livestream/LiveStream_045` — 2 quarantined, 3 part(s): `9MQQKaKEXs0`, `V0l9fOJgbtc`, `S5-jXzhiG18`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/f129deab-ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `9MQQKaKEXs0` (episode-token match) | `9MQQKaKEXs0.<bcp47>.srt` |
| `translations/conflicts/Livestream/fcff4b17-ActInf Livestream #045.0 ~  The free energy principle made simpler but not too simple.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `9MQQKaKEXs0` (episode-token match) | `9MQQKaKEXs0.<bcp47>.srt` |

#### `Livestream/LiveStream_046` — 4 quarantined, 3 part(s): `skcKoCcAQJI`, `JPsdk7pVa1I`, `7_YNInrALU8`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/Livestream/9aa038e0-ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `skcKoCcAQJI` (episode-token match) | `skcKoCcAQJI.<bcp47>.srt` |
| `translations/conflicts/Livestream/b3d6c710-ActInf Livestream #046.0 ~  Active inference models do not contradict folk psychology.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `skcKoCcAQJI` (episode-token match) | `skcKoCcAQJI.<bcp47>.srt` |
| `translations/conflicts/Livestream/5768c8a4-ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `7_YNInrALU8` (episode-token match) | `7_YNInrALU8.<bcp47>.srt` |
| `translations/conflicts/Livestream/2da9e88f-ActInf Livestream #046.2 ~  Active inference models do not contradict folk psychology.chi(translated).chi(translated).srt` | multiple-versions-no-dump | `7_YNInrALU8` (episode-token match) | `7_YNInrALU8.<bcp47>.srt` |

### Series: `MathStream`


#### `MathStream/MathStream_001` — 19 quarantined, 1 part(s): `1HKjMeEGLyY`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/MathStream/7af94266-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.chi(translated-Simp).chi(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/2bb7cc34-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.chi(translated-Trad) (2).chi(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/caaceba0-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.dut(translated).dut(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/751d61bb-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.fre(translated).fre(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/ab517ece-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.ger(translated).ger(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/b440981e-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.ita(translated).ita(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/793e65a9-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.jpn(translated).jpn(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/6416e6d1-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.kor(translated).kor(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/47d58756-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.por(translated).por(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/f1e88ca2-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.rus(translated).rus(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/d3728931-ActInfLab Livestream MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.spa(translated).spa(translated).srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/dea7707f-ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).de.srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/972d4767-ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).es.srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/f3dc6da4-ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).fr.srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/2175a887-ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).it.srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/239c5a10-ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).ja.srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/d1d8dd0d-ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).nl.srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/55f4df08-ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).pt.srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |
| `translations/conflicts/MathStream/f475dc88-ActInfLab MathStream #001.1 ~ Shanna Dobson ~  Emergent Time and Chromatic Types.eng(transcribed).eng(transcribed).ru.srt` | superseded-by-dump | `1HKjMeEGLyY` (sole part of the item) | `1HKjMeEGLyY.<bcp47>.srt` |

### Series: `ModelStream`


#### `ModelStream/ModelStream_002` — 22 quarantined, 1 part(s): `UDm0lriAIJw`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/ModelStream/76fc9cf4-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.chi(translated) (2).chi(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/4301b443-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.chi(translated).chi(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/43c783e7-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.dut(translated).dut(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/13413bad-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.fre(translated).fre(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/13f8b914-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.ger(translated).ger(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/e4de4610-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.ita(translated).ita(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/7b54bab1-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.jpn(translated).jpn(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/eef2daec-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.kor(translated).kor(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/d8778594-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.por(translated).por(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/79ab18ab-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.rus(translated).rus(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/48c87648-ActInfLab ModelStream #002.1 ~ Noor Sajid & Philip Ball.spa(translated).spa(translated).srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/e105d18d-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).de.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/939c75f7-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).es.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/f6e85bb9-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).fr.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/2882e126-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).it.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/9659649e-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).ja.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/fd85c4cc-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).ko.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/ca9073fc-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).nl.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/62db4f43-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).pt.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/72573846-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).ru.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/693f2328-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).zh-Hans.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/c7d41259-ActInfLab ModelStream #002.1 ~ Noor Sajid _ Philip Ball.eng(transcribed).eng(transcribed).zh-Hant.srt` | superseded-by-dump | `UDm0lriAIJw` (episode-token match) | `UDm0lriAIJw.<bcp47>.srt` |

#### `ModelStream/ModelStream_003` — 22 quarantined, 1 part(s): `G-S-kq42evw`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/ModelStream/647c9947-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.chi(translated) (2).chi(translated).srt` | superseded-by-dump | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/c7deff9a-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.chi(translated).chi(translated).srt` | superseded-by-dump | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/ada81fe4-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.de.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/cbe82196-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.es.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/b702afc2-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.fr.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/ebe98963-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.it.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/b6e58876-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.ja.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/9edf844a-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.kor(translated).kor(translated).srt` | superseded-by-dump | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/3ba55c39-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.nl.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/13ef3e33-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.pt.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/d9c422b8-ActInfLab ModelStream #003.1 ~ Ozan Catal & Tim Verbelen.ru.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/0e512948-ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).ko.srt` | superseded-by-dump | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/bc3abb6f-ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).zh-Hans.srt` | superseded-by-dump | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/aa9788dc-ActInfLab ModelStream #003.1 ~ Ozan Catal _ Tim Verbelen.eng(transcribed).eng(transcribed).zh-Hant.srt` | superseded-by-dump | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/b80b84f2-ActInfLab ModelStream #003.1.de.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/24235497-ActInfLab ModelStream #003.1.es.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/36c118e1-ActInfLab ModelStream #003.1.fr.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/6b31523d-ActInfLab ModelStream #003.1.it.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/bc42d553-ActInfLab ModelStream #003.1.ja.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/52786855-ActInfLab ModelStream #003.1.nl.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/79826bcf-ActInfLab ModelStream #003.1.pt.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |
| `translations/conflicts/ModelStream/3c442bb5-ActInfLab ModelStream #003.1.ru.srt` | multiple-dump-versions | `G-S-kq42evw` (episode-token match) | `G-S-kq42evw.<bcp47>.srt` |

#### `ModelStream/ModelStream_004` — 22 quarantined, 1 part(s): `uePR4DQv0yI`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/ModelStream/a0d985c8-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.chi(translated) (2).chi(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/a86573ac-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.chi(translated).chi(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/afc76b60-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.dut(translated).dut(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/2340b129-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).de.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/40f7e5da-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).es.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/ebb81924-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).fr.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/37e29d64-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).it.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/130b54f8-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).ja.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/57e2371d-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).ko.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/6cba54e3-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).nl.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/54eaa120-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).pt.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/cba19b42-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).ru.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/d10a5610-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).zh-Hans.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/37b8af8f-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.eng(transcribed).eng(transcribed).zh-Hant.srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/9d98c2d5-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.fre(translated).fre(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/f9b753a6-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.ger(translated).ger(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/cbcb5650-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.ita(translated).ita(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/98c4032c-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.jpn(translated).jpn(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/b5020658-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.kor(translated).kor(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/1a4514e6-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.por(translated).por(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/e8336659-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.rus(translated).rus(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |
| `translations/conflicts/ModelStream/8a4b5670-ActInfLab ModelStream #004.1 ~  Implementing Active Inference by Message Passing in a Factor Graph.spa(translated).spa(translated).srt` | superseded-by-dump | `uePR4DQv0yI` (episode-token match) | `uePR4DQv0yI.<bcp47>.srt` |

#### `ModelStream/ModelStream_007` — 1 quarantined, 3 part(s): `dBAx-VDVcPQ`, `skf3sOM-7WI`, `uX8iSoDR83g`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/ModelStream/137bb013-Active Inference ModelStream #007.1 ~ Conor Heins & Daphne Demekas ~ pymdp.es (1).srt` | superseded-by-dump | `skf3sOM-7WI` (episode-token match) | `skf3sOM-7WI.<bcp47>.srt` |

### Series: `MorphStream`


#### `MorphStream/MorphStream_001` — 22 quarantined, 1 part(s): `MzYmdBaJIYc`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.de.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/3738c204-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.es.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.fr.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.it.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ja.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ko.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.nl.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.pt.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ru.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hans.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-Transcripts_Captions__mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hant.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.de.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.es.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.fr.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.it.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ja.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ko.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.nl.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.pt.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.ru.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hans.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |
| `translations/conflicts/MorphStream/cc831bf5-mph001-1_ActInf MorphStream 001.1 ~ David Kappel and Sarah Hamburg.m4a.zh-Hant.srt` | superseded-by-dump | `MzYmdBaJIYc` (episode-token match) | `MzYmdBaJIYc.<bcp47>.srt` |

### Series: `TextbookGroup`


#### `TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_003` — 2 quarantined, 1 part(s): `8OT2EC-l0N4`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/TextbookGroup/d41d8cd9-ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).chi(translated) (2).chi(translated).srt` | multiple-versions-no-dump | `8OT2EC-l0N4` (episode-token match) | `8OT2EC-l0N4.<bcp47>.srt` |
| `translations/conflicts/TextbookGroup/aba8d12d-ActInf Textbook Group ~ Cohort 1 ~ Meeting 3 (Appendix A + Appendix B + 2nd hour discussion).chi(translated).chi(translated).srt` | multiple-versions-no-dump | `8OT2EC-l0N4` (episode-token match) | `8OT2EC-l0N4.<bcp47>.srt` |

#### `TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_004` — 1 quarantined, 1 part(s): `Z7Z29pu6NnY`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/TextbookGroup/d41d8cd9-ActInf Textbook Group ~ Cohort 1 ~ Meeting 4 (Chapter 2 pt. 1).chi(translated).chi(translated).srt` | byte-identical-extra | `Z7Z29pu6NnY` (episode-token match) | `Z7Z29pu6NnY.<bcp47>.srt` |

#### `TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_005` — 1 quarantined, 1 part(s): `JJaQ0F81Ucs`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/TextbookGroup/d41d8cd9-ActInf Textbook Group ~ Cohort 1 ~ Meeting 5 (Chapter 2 pt. 2).chi(translated).chi(translated).srt` | byte-identical-extra | `JJaQ0F81Ucs` (episode-token match) | `JJaQ0F81Ucs.<bcp47>.srt` |

#### `TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_006` — 1 quarantined, 1 part(s): `MXbknE8EZp0`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/TextbookGroup/d41d8cd9-ActInf Textbook Group ~ Cohort 1 ~ Meeting 6 (Chapter 3 pt. 1).chi(translated).chi(translated).srt` | byte-identical-extra | `MXbknE8EZp0` (episode-token match) | `MXbknE8EZp0.<bcp47>.srt` |

#### `TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_007` — 1 quarantined, 1 part(s): `AKeKLERgmQA`

| On-disk copy (in `translations/conflicts/<Series>/`) | Reason | Likely part | Target naming |
|---|---|---|---|
| `translations/conflicts/TextbookGroup/d41d8cd9-ActInf Textbook Group ~ Cohort 1 ~ Meeting 7 (Chapter 3 pt. 2).chi(translated).chi(translated).srt` | byte-identical-extra | `AKeKLERgmQA` (episode-token match) | `AKeKLERgmQA.<bcp47>.srt` |

_600 quarantined file rows listed (0 without a resolved on-disk name — locate via md5-prefix glob); every resolution is a byte-compare plus one of the playbook decisions above._


---

## Part C — Investigation items (do NOT move yet)


### `Applied Active Inference Symposium/2021 Symposium with Karl Friston` — `Prof. Karl Friston ~ Applied Active Inference Symposium pt. 1 (Education)` cluster (11 files: de, es, fr, it, ja, ko, nl, pt, ru, zh-Hans, zh-Hant)


The 2021 item's parts are: INRaCBikpso ('…1st Applied Active Inference Symposium, part 2 (.comms)'),
X2GwqUVLlcs ('…pt. 2 (Communication)'), hW9IiOujS1E ('…part 3 (.tools)'). **No part 1 / '(Education)'
video exists in this item or anywhere in the channel metadata.** Either the 1st-symposium part-1 video was
never cataloged (would need a new item via the Journal-Utilities generator) or these stems are mislabeled.
Action: verify on YouTube whether '1st Applied Active Inference Symposium, part 1' exists as a video; report
findings on the tracking issue; leave files in place until a catalog decision exists.


### Empty-title parts (verify, move, and optionally report)

- `MathStream/MathStream_002` → part `RQb6wLWoYok` (title empty in metadata)

- `MathStream/MathStream_003` → part `bBE2w_BpuAw` (title empty in metadata)

- `GuestStream/GuestStream_029` → part `UuXAjY9Wgdg` (title empty in metadata)


`metadata.json` is generated (Journal-Utilities) — do not hand-fill titles; report the gap on the tracking
issue instead. The move itself can proceed once the video identity is confirmed.

