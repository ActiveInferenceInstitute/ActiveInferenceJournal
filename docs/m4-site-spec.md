# M4 site spec — static per-item pages, sitemap, robots.txt

Status: **specification for implementation, not yet implemented.** The current
deployed site (hash-routed SPA fed by `manifest.json` + `data/*.json`, built by
Journal-Utilities `src/journal_utilities/site/builder.py` via
`scripts/build_pages_site.py`, deployed by
[`.github/workflows/deploy-pages.yml`](../.github/workflows/deploy-pages.yml))
exposes exactly one crawlable URL. This file states what the M4 wave must emit
so the Journal_Utilities builder agent (or a later wave) can implement it.
Handoff context: `/tmp/aii_journal_handoff.md` milestone M4.

## 0. Prerequisite fix bundled with M4 (handoff I4)

`builder.py` reads only lowercase `translations/` (`tr_dir = item_dir /
"translations"`, builder.py:121) while the journal tree holds **131 items with
capital-T `Translations/`** (~2,880 SRTs) vs **13 items with lowercase
`translations/`** (~336 SRTs). Verified 2026-09-23 on this tree and against the
live deployed `manifest.json` (13/573 items with `languages`, 129 language
entries; the site ships 3,552 fewer translation files than the journal holds:
6,432 total SRTs vs 3,552 readable).

Fix (permanent fix remains the M2 `Translations/ → translations/` migration):

```python
tr_dir = next(
    (d for d in (item_dir / "translations", item_dir / "Translations") if d.is_dir()),
    None,
)
```

Also strip legacy ISO-639-2 parenthesized tags when deriving `lang`
(builder.py:124 derives it from `name.split(".")[-2]`, so
`...chi(translated)` yields `chi(translated)` today). Map `chi→zh-Hans`
or `zh-Hant`, `dut→nl`, `fre→fr`, `ger→de`, `jpn→ja`, `kor→ko`, `rus→ru`,
`por→pt`, `spa→es`, `ita→it` per the M2 table; `translate_subtitles_openrouter.py:381`
must not re-translate files that already exist under the normalized name.

## 1. URL scheme

Base URL (canonical, used everywhere below):
`https://activeinferenceinstitute.github.io/ActiveInferenceJournal/`

- SPA stays at `/` (hash routing preserved for backward compatibility).
- New per-item page per INDEX item:
  `/item/<series>/<item>/index.html` → canonical URL
  `.../item/<series>/<item>/` (trailing slash, no `index.html` in canonicals).
- `<series>` and `<item>` are the exact on-disk directory names from
  `INDEX.json items[].path` (`data/video/activeinferenceinstitute/<series>/<item>`) —
  including spaces (e.g. `Applied Active Inference Symposium`) — percent-encoded
  in emitted URLs. Directory names ARE the slugs; M4 must not invent new slugs
  (folder slugification is DAF decision §6/J11, out of scope).
- `data/<series>_<item>.json` payload files keep their existing location; item
  pages reference them for the interactive transcript view.

## 2. Per-item page contract

Emit `output/item/<series>/<item>/index.html` for **every** item in
`INDEX.json items[]` (573 items at the time of writing). Requirements:

1. **Server-rendered (baked) content** — no JS required to read the core
   metadata: title, series, date (`parts[].upload_date`, ISO 8601), guests,
   summary/abstract from `metadata.json`, chapter list
   (`parts[].chapters`, present only with provenance), full transcript text
   (from `transcript.txt`, `parts`-tagged when multi-part).
2. **Embedded video** — YouTube iframe per part using `parts[].video_id`
   (`https://www.youtube-nocookie.com/embed/<video_id>`), part titles as
   headings.
3. **Structured data** — one `application/ld+json` block per part:
   schema.org `VideoObject` with
   `name`, `description` (abstract from metadata), `uploadDate` (ISO 8601),
   `contentUrl`/`embedUrl` (the YouTube URL from `parts[].url`),
   `thumbnailUrl` (`https://i.ytimg.com/vi/<id>/hqdefault.jpg`),
   `inLanguage` (source language, `en`), `transcript` reference, and
   `hasPart` → `Clip` entries from gated chapters (`name`, `startOffsetTime`,
   `endOffsetTime`, `url` with `?t=` fragment). Top level: an `Dataset` node
   for the item (name, `license` = CC-BY-4.0, `isPartOf` → the journal Dataset,
   `citation` → Zenodo DOI `10.5281/zenodo.7299755`).
4. **Head tags** — `<link rel="canonical" href="<base>item/<series>/<item>/">`,
   Open Graph (`og:type=video`, `og:title`, `og:description`, `og:url`,
   `og:image` = thumbnail), Twitter `summary_large_image`.
5. **Language list** — translations actually present for the item (post-I4-fix
   set), linking to the interactive view; do not fabricate languages.
6. **Navigation** — breadcrumb (journal → series → item), links to
   prev/next item in series, link back to the SPA for the interactive player.
7. **Non-goals**: no search, no client-side filtering, no new JS frameworks;
   static HTML + the existing CSS.

## 3. sitemap.xml

Emit at `<base>/sitemap.xml`:

- `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">` with **one
  `<url>` per item** (573): `<loc>` = canonical item URL,
  `<lastmod>` = max `parts[].upload_date` for the item (ISO 8601, omit if
  unknown — never fabricate), **no** `changefreq`/`priority` (noise).
- Plus the root `<loc>` = `<base>/`.
- Single file is fine (well under the 50k-URL / 50 MB limits); if it ever
  exceeds them, switch to a sitemap index `<base>/sitemap-index.xml`.
- Post-build assertion: `sitemap` URL count == processed item count (builder
  already returns `items_processed`); fail the build on mismatch.

## 4. robots.txt

Emit at `<base>/robots.txt`:

```
User-agent: *
Allow: /
Sitemap: https://activeinferenceinstitute.github.io/ActiveInferenceJournal/sitemap.xml
```

Both files are generated by the builder (not committed by hand) and must be
included in the Pages artifact alongside the existing `.nojekyll`.

## 5. Deployment notes (ties to handoff E5/J7, owned by the workflow wave)

- Builder changes land in Journal-Utilities; pin the workflow's utilities
  checkout to a tag/SHA, sparse-checkout, plain `python` (no torch/CUDA), and
  keep a single Pages deployment (drop the dual actions+gh-pages deploy or
  make branch-mode the fallback behind a flag).
- Post-deploy smoke test (CI): fetch `<base>/sitemap.xml`, assert URL count
  equals `manifest.json` `total_items`, spot-check Rich Results Test on one
  sample item page, assert `<base>/robots.txt` returns 200.

## 6. Acceptance criteria

- Every INDEX item has a static URL returning 200 with server-rendered title,
  guests, date, summary, chapters, transcript, and a valid VideoObject
  JSON-LD block per part.
- `sitemap.xml` lists the root + all item URLs; `robots.txt` references it.
- Rich Results Test validates a sampled item page (no VideoObject errors).
- Site language counts reflect the union of both `translations/` spellings
  (post-fix: 144 items with ≥1 translation at current tree state).
- Canonical URLs resolve against `INDEX.json` `items[].path` (series/item
  exactly); a test asserts emitted `<loc>` ↔ item-path bijection.
