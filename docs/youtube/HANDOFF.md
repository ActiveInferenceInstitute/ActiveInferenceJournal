# Active Inference Institute YouTube handoff

The November 20, 2026 handoff was reviewed against Journal commit `cd32e2f4`.
The public channel is [@ActiveInference](https://www.youtube.com/@ActiveInference),
with channel ID `UCbPq2w41ZaJSWtpCq4BE6Dg`. Use the channel ID for inventory
and match entries to the Journal by the YouTube video ID in
[`INDEX.json`](../../INDEX.json).

## Work already recorded

The handoff records updated upload defaults and an added Journal link in the
default description. The recent channel pass corrected broken description
links, put the affected textbook playlists in session order, and standardized
the Parr cohort playlist titles. GuestStreams and ModelStreams were enabled
as podcasts. The English-caption pilot covered Insights 001, 003, and 021.
Use a fresh audit to find remaining gaps before proposing additional edits.

## Review the public ingest backlog

Run the read-only Data API audit from a Journal-Utilities checkout at the
reviewed [ingest pin](../../.github/journal-utilities-pin.json). Supply the
restricted `YOUTUBE_API_KEY` from the local credential store.
Keep report paths in a run directory on the approved private storage volume.
From the Journal root, use absolute paths for the utilities checkout and the
existing report directory.

```sh
journal="$(pwd -P)"
utilities="/path/to/Journal_Utilities"
reports="/path/to/private/report-directory"

uv run --project "$utilities" --frozen --extra youtube python "$utilities/scripts/youtube_channel_audit.py" audit \
  --journal "$journal" --worklist "$reports/public-backlog.json" &&
python3 scripts/review_youtube_ingest.py \
  --worklist "$reports/public-backlog.json" --output "$reports/reviewed-worklist.json" &&
uv run --project "$utilities" --frozen python -m journal_utilities.ingest.scaffold \
  --journal "$journal" --worklist "$reports/reviewed-worklist.json"
```

The audit combines the channel's uploads with videos in its public playlists,
deduplicates video IDs, and verifies channel ownership and completion before
saving the public backlog. The Journal review requires explicit public,
processed, completed status for every row, refuses repeated IDs, and removes
IDs already covered by the current Journal index. It preserves public playlist
titles as labels for human review. The dry-run scaffolder gives established
video title patterns precedence and uses approved public playlist mappings
to route selected series. The classifier supplies the directory names and
derives item names from video metadata.

Prioritize the 2026 Applied Active Inference Symposium, Fundamentals Cohort 1,
and Parr Cohorts 8 and 9. Then review GuestStream, ModelStream, and GEO-INFER.
Use `Applied Active Inference Symposium/2026` for the 2026 Symposium and
`TextbookGroup/ParrPezzuloFriston2022/Cohort_9` for Parr Cohort 9 under the
Journal's [video namespace](../../data/video/activeinferenceinstitute/).
Create item paths from reviewed public source metadata and retain each video's
correct series and session. Unmatched sessions need source verification before
they become Journal records.

Use API enumeration for the weekly inventory and run media acquisition on an
approved self-hosted machine. The [GitHub workflow](../OPERATIONS.md#weekly-ingest-draft)
is dispatch-only. The local job can run on the approved host's weekly schedule
once its credential and storage bindings have been validated. For the weekly
QA run, add `--fail-on-findings` to the audit and retain its report for review.

An approved video can enter the Journal as a catalog record with its published
title, video ID, and YouTube link. Add captions and transcripts when an approved
source asset can be tied to that exact video ID. The Journal index and public
pages report transcript availability from the files in the repository.

After ingest, regenerate the Journal indexes using Journal-Utilities and run
`./run.sh full`. Add a `RESOURCES & TRANSCRIPT` backlink using the published
item URL once the Journal item is live. Add cohort and Symposium playlist
backlinks after their Journal collections are published.

## Captions, descriptions, and chapters

- Render an English SRT from each item's timed WhisperX `transcript.json`.
  Review cue timing, speaker changes, and named entities against the item
  metadata. Use reviewed name corrections for Karl Friston, Iain McGilchrist,
  and Darius Parvizi-Wayne where applicable.
- Keep existing human-edited English tracks. Resolve conflicting video and
  metadata language settings before submitting an English track. Use the
  reviewed English track as the translation source and record each completed
  upload by video ID and SRT SHA-256 in the private operator ledger.
- Review link-audit findings and exact replacement URLs before updating a
  description. Keep each series' structure and use the Institute's maintained
  footer. Preserve series-first titles and the Fundamentals session wording,
  applying only verified date or typo corrections to those sessions.
- Spot-check chapter proposals against the video. Start at `0:00` and require
  at least three entries separated by ten seconds or more. Keep automatic
  chapters available where no reviewed manual list exists.

The [Journal-Utilities YouTube guide](https://github.com/ActiveInferenceInstitute/Journal_Utilities/blob/main/docs/pipeline/youtube.md)
describes the tooling boundary. Record approval and verification for channel
mutations in the private operator record. Channel visibility decisions, caption
conflicts, and auto-dubbing remain with the channel owner.

## Editorial follow-through

Keep CC BY and the standing trailer decision. Review series thumbnail designs
before comparing their performance in Studio. Short-form edits need a
self-contained excerpt, captions, human review, and a source-video link.
YouTube Studio is the review path for end screens, cards, featured video, and
channel home sections. Review any newcomer playlist with the channel owner.
