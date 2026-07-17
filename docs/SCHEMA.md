# ActiveInferenceJournal — v2 Schema (agent- & program-navigable)

Target schema for the refactor of the `ActiveInferenceJournal` repo. Goal: uniform,
flat, machine-readable item folders with a canonical `metadata.json`, no placeholder
cruft, audio kept off `main`, and top-level indexes.

## Per-item folder

```
<Series>/<Series>_<NNN[.E]>/
  metadata.json        # canonical record (see below) — single source of truth
  README.md            # generated human nav: title(s), date, links, contents
  transcript.txt       # clean text (per part: "## Part N" headers when multi-part)
  transcript.json      # timestamped segments (array; part/session-tagged)
  captions/            # original-language *.srt
  translations/        # translated *.srt (one per language) — preserved verbatim
  assets/
    images/   html/   prose/   appendices/   bibliography/   # curated content, by type
  # audio/ is NOT on main (gitignored). The `audio` branch carries audio/<video_id>.64k.m4a
```

### `metadata.json`

```json
{
  "series": "GuestStream",
  "item": "GuestStream_094",
  "title": "ActInf GuestStream 094 ~ ...",
  "source": "youtube",
  "channel": "ActiveInferenceInstitute",
  "parts": [
    {"part": "094.1", "video_id": "1Qr7um2W-Rc",
     "url": "https://www.youtube.com/watch?v=1Qr7um2W-Rc",
     "title": "...", "published": "2026-..", "duration": 0,
     "has_transcript": true, "has_captions": true, "has_audio": true}
  ]
}
```

Note: the example above shows aspirational per-part flags (`published`,
`has_transcript`, …). Files currently on `main` carry the core keys
`series, item, source, channel, category, episode` and `parts[]` entries with
`video_id, url, title` (plus `duration`, `upload_date` where known).

## Enrichment fields (v2.1)

Items are enriched from the Institute's Coda table (now Superhuman Docs), the
session split-files, and the channel manifest by
`Journal-Utilities/scripts/enrich_metadata.py`. Regenerate with:

```bash
python scripts/enrich_metadata.py --apply   # from Journal-Utilities; dry-run without --apply
python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal
python scripts/validate_journal.py --journal ../ActiveInferenceJournal \
  --manifest data/output/channel_videos.json
```

Enrichment-owned keys — the script only ever sets these; it never deletes or
rewrites other keys, empty values are omitted, and re-running is idempotent.
Invalid values in enrichment-owned URL fields are normalized into their
corresponding display fields without losing the source text:

| Field | Type | Source | Level |
|-------|------|--------|-------|
| `title` | string | Coda `"<Unique event name> ~ <Title or name of stream>"` | item |
| `date` | ISO date | Coda "Date" | item (or per-part when parts differ) |
| `guests` | string[] | Coda "Guests" | item (multi-row lists union) |
| `other_participants` | string[] | Coda "Other Participants" | item (union) |
| `description` | string | split-file session description (shared text) | item |
| `github` | url | generated: canonical link to the item's folder in this repo | item |
| `slides_url` | url | Coda "Slides" / legacy session DB; real `http(s)` URL only | item / per-part |
| `slides_label` | string | Coda "Slides" display text when no URL is available | item / per-part |
| `paper_link` | url | Coda "Paper link" when it is a real `http(s)` URL | item / per-part |
| `paper_title` | string | Coda "Paper link" display text when no URL is available | item / per-part |
| `doi` | string | Coda "DOI" | item / per-part |
| `zenodo` | url | Coda "Zenodo Link" | item / per-part |
| `keywords` | string[] | Coda "Keywords" | item (union) |
| `thumbnails` | object | Coda "Thumbnail Image" / "Cover image" | item |
| `summaries` | object | Coda summaries: `human`, `ai`, `word_300`, `abstract` | item |
| `enriched_from` | string[] | provenance: `coda`, `split_file`, `youtube`, `db` (legacy session DB), `generated`, `curated` (human-verified correction) | item |
| `sessions` | object[] | split-files (multi-talk videos) | item |
| `duplicate_of` | string | item path this uncategorized item duplicates | item |

- **`title` vs `parts[].title`:** the item-level `title` is the Coda *event*
  title; `parts[].title` stays the verbatim YouTube video title. They differ by
  design — do not "fix" one to match the other.
- **`sessions[]`** (talks within one long video):
  `{index, session_name ("<video_id>_sessNN"), start ("H:MM:SS"), title?,
  guests[]?, other_participants[]?, video_id?}`. `video_id` links a session
  to its standalone per-talk upload when one exists; that upload's own item
  carries `duplicate_of` back to the full recording. `title` may be a segment label
  ("Roundtable") when the talk has no distinct title.
  **Ownership: this repo.** The enrichment script *seeds* `sessions[]` —
  from YouTube chapter lists (timestamped video descriptions, cached by
  `fetch_chapters.py`) or curated data — only when an item has none, and
  never overwrites. Edit sessions directly here (add speakers, fix titles);
  regeneration preserves your edits.
- **Split transcript identity:** when source transcripts are split into sessions,
  corresponding `transcript.txt` headings and `transcript.json` `video_id` fields use
  the stable `<video_id>_sessNN` session name rather than an empty placeholder.
- **`duplicate_of`** marks an `Other/<video_id>` item whose content is a
  duplicate of a curated item (the two symposium full uploads). The duplicate
  intentionally repeats the canonical video's ID; coverage reconciliation
  excludes the secondary record and `INDEX.json` exposes both record and unique
  video counts.
- **`data/video/activeinferenceinstitute/private_videos.json`** documents
  private/unlisted channel videos known to the Institute (from the legacy
  session database) that are deliberately absent from this public corpus.

## Top-level

- `INDEX.json` — machine index: every item + parts + paths + flags. `videos`
  counts part records, including deliberate duplicates; `unique_videos` counts
  distinct video IDs.
- `INDEX.md` — human index grouped by series.
- `SCHEMA.md` — this spec (mirrored into the journal repo).
- `sources/` — registry of channels/sources (channel id → series rules) so other
  open-source sources plug in (Institute-first, source-pluggable).

## Refactor rules (non-destructive)

- Drop placeholders: `blank_document.txt`, `blank.txt`, empty `.gitkeep`-only dirs.
- `Metadata/<item>.json` → `metadata.json` parts; `*.simple.txt` → `transcript.txt`;
  timestamped json → `transcript.json`.
- `Captions/`, `Transcripts/Captions/` `*.srt` → `captions/`.
- `Translations/*.srt` → `translations/` (verbatim).
- `Images/`→`assets/images/`, `HTML/`/`Transcripts/HTML/`→`assets/html/`,
  `Transcripts/Prose/`/`Prose/`→`assets/prose/`, `Appendices/`→`assets/appendices/`,
  `Bibliographic Information/`→`assets/bibliography/`. `pdf/odt/zip` → `assets/` by type.
- `Audio/*.m4a` → moved to the `audio` branch as `audio/<video_id>.64k.m4a`; removed from `main`.
- **Coverage invariant:** every non-duplicate channel video is a part in exactly
  one canonical item. Records with `duplicate_of` are deliberate secondary
  copies and are excluded from missing/duplicate coverage counts.
- **File invariant:** every non-placeholder source file is accounted for (moved or
  intentionally dropped). The converter's `--dry-run` reports any unmapped file.
```
