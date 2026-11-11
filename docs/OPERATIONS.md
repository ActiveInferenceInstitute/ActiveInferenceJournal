# Operations — CI, validation and deployment

This repository holds content only; every gate, build and deployment is driven by
GitHub Actions workflows under [`.github/workflows/`](../.github/workflows/) and by the
separate [Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal_Utilities)
engine. This page maps each workflow to what it does and how to reproduce it locally.

## Workflows

| Workflow | File | Trigger | Purpose |
| --- | --- | --- | --- |
| Validate journal integrity | [`journal-integrity.yml`](../.github/workflows/journal-integrity.yml) | `push`, `pull_request`, `workflow_call` | The release gate: derived indexes, split transcript artifacts, the read-only integrity gate, manifest reconciliation, and GNN conformance. |
| Deploy GitHub Pages | [`deploy-pages.yml`](../.github/workflows/deploy-pages.yml) | `push` to `main` touching `data/**` or `INDEX.json`; `workflow_dispatch` | Runs the integrity gate, then builds and deploys the static site bundle. |
| Weekly ingest | [`weekly-ingest.yml`](../.github/workflows/weekly-ingest.yml) | `workflow_dispatch` only (draft) | Secret-free channel enumeration, new-video delta, scaffold preview, and a reconciliation report. |

### Validate journal integrity

The `validate` job checks out the journal and a pinned Journal-Utilities revision
(`3b9700ad…`), then runs:

1. `generate_journal_indexes.py --journal . --check` — fails if `INDEX.json`/`INDEX.md`
   are stale.
2. `repair_split_transcripts.py --journal . --utilities .journal-utilities --check` —
   fails if merged session transcript artifacts are stale.
3. `validate_journal.py --journal . --manifest …/channel_videos.json` — the read-only
   integrity gate (metadata/path consistency, transcript shape, manifest coverage, and
   the rule that `main` carries no audio or credentials).
4. A manifest-staleness/reconciliation step (E13) that reports manifest age and any
   channel/manifest/INDEX disagreements; a manifest older than 7 days and duplicate
   ids are warnings, not failures, until a scheduled refresh exists.

The `gnn-conformance` job reads [`.github/gnn-pin.json`](../.github/gnn-pin.json), pins
`ActiveInferenceInstitute/Generalized_Notation_Notation` at `v5.0.3`
(`8f293d9b…`), and parses/type-checks every `*.gnn.md` sketch in the repository (or the
pinned upstream exemplar when none exist). See [`.github/GNN.md`](../.github/GNN.md).

### Deploy GitHub Pages

The build job checks out Journal-Utilities at the same pinned revision, then runs
`python3 utilities/scripts/build_pages_site.py --journal journal --output _site --apply`.
`--apply` is required — the builder is dry-run by default and would publish an empty
site without it. A `.nojekyll` file is written so the emitted bundle is served verbatim
(the site is a static HTML bundle produced by the Python builder, **not** a Jekyll
build). After deploying, a smoke test asserts HTTP 200 for `index.html`, `manifest.json`,
`.nojekyll`, `sitemap.xml`, `robots.txt`, one path-keyed item page and its payload, and
that the item page's `rel="canonical"` link is server-rendered.

The static per-item pages are specified in [`m4-site-spec.md`](m4-site-spec.md).

### Weekly ingest (draft)

`weekly-ingest.yml` is **dispatch-only** while it is a draft: a guard step fails the run
unless it was triggered by `workflow_dispatch`. It is secret-free by design — channel
enumeration and new-video resolution run on `yt-dlp`, so no API key is configured. It
enumerates the channel, prints dry-run scaffold previews, and uploads an ingest worklist,
a channel manifest and a reconciliation report as artifacts. Add a `schedule:` only after
reviewing Journal-Utilities `docs/m3-ingest.md` and removing the guard.

## Dependency updates

[`.github/dependabot.yml`](../.github/dependabot.yml) opens grouped, weekly pull requests
for GitHub Actions updates. Journal-Utilities is pinned by commit SHA in the workflows
(tag and branch refs drift silently), so a pin bump is a reviewed change rather than an
automatic one.

## Local validation

There is no in-repo script or test suite; all gates live in Journal-Utilities. Run these
from a Journal-Utilities checkout (see [`../CONTRIBUTING.md`](../CONTRIBUTING.md)):

```bash
uv run python scripts/generate_journal_indexes.py --journal ../ActiveInferenceJournal --check
uv run python scripts/repair_split_transcripts.py \
  --journal ../ActiveInferenceJournal --utilities .
uv run python run.py journal-check
```

`journal-check` is read-only and covers the same integrity checks as CI. Use
`--strict-manifest` after a fresh enumeration when canonical IDs absent from the channel
manifest must fail rather than warn. Offline, the repository itself can still be checked
with `actionlint`, a YAML/JSON parse, and a Markdown relative-link check.

## Branch model

- `main` — content without audio.
- `audio` — `main` plus `<item>/audio/<name>.64k.m4a` (64 kbps), same layout.

Audio is never committed to `main`; the integrity gate enforces this.
