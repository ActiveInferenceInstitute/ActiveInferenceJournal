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
  transcript.json      # timestamped segments (array; part-tagged)
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

## Top-level

- `INDEX.json` — machine index: every item + parts + paths + flags.
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
- **Invariant:** every non-placeholder source file is accounted for (moved or
  intentionally dropped). The converter's `--dry-run` reports any unmapped file.
```
