# M4 site spec — static per-item pages, sitemap, robots.txt

Status: **implemented and deployed.** The builder is Journal-Utilities
`src/journal_utilities/site/pages_site.py` (+ `sitemap.py`), driven by
`scripts/build_pages_site.py`; the deploy is
[`.github/workflows/deploy-pages.yml`](../.github/workflows/deploy-pages.yml),
which builds with `--apply` (the builder is dry-run by default — without that
flag the page publishes an empty site) and smoke-tests the SPA entry points,
one path-keyed item page, its payload, `sitemap.xml` and `robots.txt`. The SPA
stays at `/` as the interactive view; the static pages are additive.

## 0. Prerequisite fix bundled with M4 (handoff I4)

The builder reads **both** `translations/` and `Translations/` spellings
(lowercase preferred), so a site build sees the union of the item's SRT files
regardless of directory case, and derives the language from the `.srt` name
with the legacy ISO-639-2 annotations normalized. The M2 migration moved the
bulk of the files to the lowercase spelling; the remainder is tracked in
[`../TO-DO.md`](../TO-DO.md), and a deployed build reads both spellings, so an
unmigrated directory no longer hides an item's languages.

## 1. URL scheme

Base URL (canonical, used everywhere below):
`https://activeinferenceinstitute.github.io/ActiveInferenceJournal/`

- SPA stays at `/` (hash routing preserved for backward compatibility).
- One static page per INDEX item:
  `output/item/<slug>/index.html` → canonical URL `.../item/<slug>/`
  (trailing slash, no `index.html` in canonicals).
- `<slug>` is the item's `INDEX.json items[].path` **below its source
  directory**: `data/video/<source>/<series>/…/<item>` → `<series>/…/<item>`.
  The path components are the exact on-disk directory names — including spaces
  (e.g. `Applied Active Inference Symposium`) — percent-encoded in emitted URLs.
  Directory names ARE the slugs; M4 must not invent new slugs (folder
  slugification is the DAF decision §6/J11, out of scope).
- The slug, not the flat `(series, item)` pair, is the item's identity: flat
  pairs are not unique in this tree (one `TextbookGroup/Meeting_007` pair once
  covered 8 cohort records), so pages, payloads, manifest ids and sitemap
  entries all key on the slug. A duplicate slug fails the build before any
  payload is written.
- Payload files are `data/<slug>.json` (this supersedes the earlier
  `data/<series>_<item>.json` — the flat name is what collided), and each
  manifest item carries both `id` (the slug) and `path` (`items[].path`).

## 2. Per-item page contract

Emit `output/item/<slug>/index.html` for **every** item in
`INDEX.json items[]`. Requirements:

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
4. **Head tags** — `<link rel="canonical" href="<base>item/<slug>/">`,
   Open Graph (`og:type=video`, `og:title`, `og:description`, `og:url`,
   `og:image` = thumbnail), Twitter `summary_large_image`.
5. **Language list** — translations actually present for the item (union of
   both `translations/` spellings), linking to the interactive view; do not
   fabricate languages.
6. **Navigation** — breadcrumb (journal → series → item), links to
   prev/next item in the same directory series, link back to the SPA
   (`#/item/<slug>`) for the interactive player.
7. **Non-goals**: no search, no client-side filtering, no new JS frameworks;
   static HTML + the existing CSS.

## 3. sitemap.xml

Emit at `<base>/sitemap.xml`:

- `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">` with **one
  `<url>` per item**: `<loc>` = canonical `item/<slug>/` URL,
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

Both files are generated by the builder (not committed by hand) and are
included in the Pages artifact alongside `.nojekyll`.

## 5. Deployment notes (handoff E5/J7)

- The workflow checks out Journal-Utilities at a reviewed **SHA pin**, with a
  sparse checkout of `scripts/build_pages_site.py` + `src/journal_utilities`,
  and builds with plain `python3` (stdlib only: `json/logging/re/shutil/
  pathlib`) — no `uv sync`, no torch/CUDA. There is a single Pages deployment
  (`upload-pages-artifact` → `deploy-pages`).
- The build step must pass **`--apply`**: the builder is dry-run by default, so
  a pin bump without it publishes an empty site.
- Post-deploy smoke test: SPA entry points (`index.html`, `manifest.json`,
  `.nojekyll`), `sitemap.xml`, `robots.txt`, plus one **deep** item page
  (`item/TextbookGroup/ParrPezzuloFriston2022/Cohort_1/Meeting_007/`, i.e. one
  level below its series directory, which only resolves with path keying) and
  its `data/<slug>.json` payload; the item page must contain its canonical link
  without running JS.
- Rich Results Test on a sampled item page remains a manual check.

## 6. Acceptance criteria

- Every INDEX item has a static URL returning 200 with server-rendered title,
  guests, date, summary, chapters, transcript, and a valid VideoObject
  JSON-LD block per part.
- `sitemap.xml` lists the root + all item URLs — one unique `<loc>` per item
  (no duplicates from colliding keys); `robots.txt` references it.
- Rich Results Test validates a sampled item page (no VideoObject errors).
- Site language counts reflect the union of both `translations/` spellings.
- Canonical URLs resolve against `INDEX.json` `items[].path` (the path below
  the source directory); a test asserts the emitted `<loc>` ↔ item-path
  bijection and that a duplicate path aborts the build.
