# Organization

How the ActiveInferenceJournal repository is laid out, and how to extend it to other
sources.

## Top-level namespace

Content is **source-namespaced** so multiple channels and non-video sources coexist
cleanly:

```
data/
  video/
    activeinferenceinstitute/        # the Active Inference Institute YouTube channel
      <Series>/<item>/               # one item per event (may have multiple video parts)
    <other-channel>/                 # future: other YouTube channels, same per-item schema
  <other-type>/<source>/             # future: non-video sources (papers, datasets, …)
docs/                                # technical documentation (this folder)
INDEX.json   INDEX.md   README.md    # top-level entry points
```

- **Type axis** (`video/`, …) groups by medium.
- **Source axis** (`activeinferenceinstitute/`, …) groups by origin within a type.
- This keeps every corpus independently addressable and lets agents/programs target a
  single source or sweep across all of them.

## Series and items

Within `data/video/activeinferenceinstitute/`:

- A **series** folder (`GuestStream`, `Roundtable`, `Livestream`, `Courses`,
  `Applied Active Inference Symposium`, … and `Other` for uncategorized videos) groups
  related content.
- An **item** folder (`GuestStream_082`, `Roundtable_2026.2`, …) is one event. An item
  may bundle several **video parts** (e.g. a multi-session stream); every part is a
  `video_id` in the item's `metadata.json`.
- Each item follows the per-item schema in [`SCHEMA.md`](SCHEMA.md).

Every video on the Institute channel is represented as a part in exactly one item; videos
whose titles don't match a known series pattern live under `Other/<video_id>/`.

## Adding another source

1. Create `data/video/<channel-slug>/` (or `data/<type>/<source>/`).
2. Produce items under it with the same per-item schema (`metadata.json` carries
   `source` + `channel`).
3. Regenerate `INDEX.json` / `INDEX.md` (Journal-Utilities `scripts/generate_journal_indexes.py`).

See [`PIPELINE.md`](PIPELINE.md) for how the Institute channel is pulled and kept complete.
