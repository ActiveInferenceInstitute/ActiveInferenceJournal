# Operations - gate, CI and deployment

This repository holds content. Its gate and its deployment are the same code
whether they run on a laptop or on GitHub Actions: everything starts at
[`./run.sh`](../run.sh), and each workflow step calls one arm of it. No command
is duplicated in YAML.

## Gate arms

```bash
./run.sh            # list the arms
./run.sh lint       # workflow action pins, pin-file schemas, shipped JSON
./run.sh docs       # relative links, anchors, docs index coverage, documented pins
./run.sh identity   # publishing contract: record ids plus the schema digest
./run.sh fast       # pinned Journal-Utilities derived-index check
./run.sh full       # split transcripts, integrity gate, manifest reconciliation
./run.sh gnn        # pinned Generalized Notation Notation conformance
./run.sh all        # lint, docs, identity, full, gnn (fast is a subset of full)
./run.sh bench --cold   # measure every arm, refresh docs/_generated/gate-timings.md
```

| Arm | Cost | What it proves |
| --- | --- | --- |
| `lint` | seconds | Every `uses:` is pinned to a 40-hex commit, every workflow declares `name`/`on`/`permissions`, the Journal-Utilities checkout takes its ref from the pin file rather than a literal SHA, both pin files match their schema, and shipped JSON parses. |
| `docs` | seconds | Relative Markdown links, exact-case paths, anchors, docs-index reachability, timing-table coverage and documented pins; isolated real-file regressions preserve inline-code heading words and duplicate suffixes while ignoring code links, comments and fences. |
| `identity` | unmeasured for this source cohort | Contained corpus paths; schema-declared INDEX/metadata series, item, ordered parts and duplicate projection; Boolean transcript presence; session-to-part membership; local artifact digests and real-file selftests. This is not a general JSON Schema validator or live-channel check. |
| `fast` | ~1 s | `generate_journal_indexes.py --journal . --check` against the pinned Journal-Utilities: `INDEX.json`/`INDEX.md` are not stale. |
| `full` | ~30 s | The split-transcript check, the read-only `validate_journal.py` gate, and the manifest staleness/reconciliation report (E13). |
| `gnn` | minutes, network | The pinned GNN parser installs at the pinned revision, reports the pinned version, and parses/type-checks every `*.gnn.md` sketch (or the pinned upstream exemplar when the repository has none). The arm accepts only a literal `True` from the type checker's three-valued sentinel (`True`/`2`/`False`) and runs its own verdict selftest so a truthiness test cannot regress. |

There is no `types` arm: this repository ships no typed source. Arms are
stdlib-only Python for the offline `lint`, `docs` and `identity` arms. `fast` and
`full` also need the pinned Journal-Utilities objects and their admitted runtime.
`gnn` builds an isolated environment because its pinned package declares
`requires-python >=3.11,<3.15`; provisioning requires separate authority and an
appropriate interpreter.

That environment is keyed by repository, **revision** and interpreter, and the
installed parser is bound to the pin by the commit id pip records in
`direct_url.json`. A version string is not enough: bumping the revision while
the tag stays the same leaves `gnn.__version__` unchanged, so a version-keyed
cache would verify the old parser and print the new pin. Changing the pin
rebuilds the environment, and `verify` refuses a parser built from any other
commit.

Pinned revisions live in two files and nowhere else:

| Pin | File | Schema |
| --- | --- | --- |
| Journal-Utilities | [`.github/journal-utilities-pin.json`](../.github/journal-utilities-pin.json) | `journal-utilities-pin/v1` |
| GNN | [`.github/gnn-pin.json`](../.github/gnn-pin.json) | `gnn-importer-pin/v1` |

The Journal-Utilities pin carries two roles. `gate` (the top-level `revision`)
is what the integrity gate, the Pages builder and `./run.sh` use. `ingest` is
the newer revision `weekly-ingest.yml` needs: `journal_utilities.ingest.ytdlp`
does not exist at the gate revision. Workflows read the revision through
`python3 scripts/gate/pin.py --revision [--role ingest]`, so a bump is a
one-file, reviewable change.

Measured wall time per arm on this host, before and after the gate existed, is
generated in [`_generated/gate-timings.md`](_generated/gate-timings.md).
Those are historical measurements, not timings for the newly qualified identity
and docs implementations. Generated timing artifacts remain unchanged until a
separately admitted real measurement refresh.

## Workflows

| Workflow | File | Trigger | Purpose |
| --- | --- | --- | --- |
| Validate journal integrity | [`journal-integrity.yml`](../.github/workflows/journal-integrity.yml) | `push`, `pull_request`, `workflow_call` | `lint`, `docs`, `identity`, `fast`, `full` against the pinned Journal-Utilities; GNN is separate. |
| GNN conformance | [`gnn-conformance.yml`](../.github/workflows/gnn-conformance.yml) | `push`, `pull_request` | The `gnn-conformance` job, display name `gnn conformance (pinned)`: `./run.sh gnn`. |
| Deploy GitHub Pages | [`deploy-pages.yml`](../.github/workflows/deploy-pages.yml) | `push` to `main` touching `data/**` or `INDEX.json`; `workflow_dispatch` | Runs the integrity gate, then builds and deploys the static site bundle. |
| Weekly ingest | [`weekly-ingest.yml`](../.github/workflows/weekly-ingest.yml) | `workflow_dispatch` only (draft) | Secret-free channel enumeration, new-video delta, scaffold preview, reconciliation report. |

### Why GNN conformance is a separate workflow

The GNN arm installs a package from git, which took ~179 s cold on this host -
an order of magnitude more than everything else combined. While it lived in the
same workflow file, `deploy-pages.yml` inherited it through
`uses: ./.github/workflows/journal-integrity.yml`, so every Pages deploy waited
for a pip install it never uses. The job key (`gnn-conformance`) and display
name (`gnn conformance (pinned)`) are unchanged; only its workflow file moved.

### Validate journal integrity

The `validate` job checks out the journal and the pinned Journal-Utilities
revision, then runs lint, docs, identity, fast and full. The steps formerly inline
heredocs in the workflow are now `scripts/gate/arm_manifest.py` and the
`fast`/`full` arms, so the locally reproduced command and the CI command are
literally the same file.

The reconciliation script reports manifest age, duplicate IDs and differences
between manifest and INDEX part IDs. In the current `full` invocation, whole-day
`age_days > 7` and duplicate IDs warn without failing this reporting step.
The existing `arm_manifest.py --strict` makes either warning return 1; `full`
does not pass it. Set differences remain printed diagnostics even in strict
mode; producer integrity validation is a separate check. Strict-policy adoption
and scheduled refresh remain maintainer decisions.

### Deploy GitHub Pages

The build job checks out Journal-Utilities at the pin, then runs
`python3 utilities/scripts/build_pages_site.py --journal journal --output _site --apply`.
`--apply` is required - the builder is dry-run by default and would publish an
empty site without it. A `.nojekyll` file is written so the emitted bundle is
served verbatim: this is a static HTML bundle, **not** a Jekyll build. After
deploying, a smoke test asserts HTTP 200 for `index.html`, `manifest.json`,
`.nojekyll`, `sitemap.xml`, `robots.txt`, one path-keyed item page and its
payload, and that the item page's `rel="canonical"` link is server-rendered.

The static per-item pages are specified in [`m4-site-spec.md`](m4-site-spec.md).

### Weekly ingest (draft)

`weekly-ingest.yml` is **dispatch-only** while it is a draft: a guard step fails
the run unless it was triggered by `workflow_dispatch`. It is secret-free by
design - channel enumeration and new-video resolution run on `yt-dlp`, so no API
key is configured. It enumerates the channel, prints dry-run scaffold previews,
and uploads an ingest worklist, a channel manifest and a reconciliation report as
artifacts. Add a `schedule:` only after reviewing Journal-Utilities
`docs/m3-ingest.md` and removing the guard.

For the self-hosted Data API inventory and public backlog review, use the
[YouTube handoff](youtube/HANDOFF.md#review-the-public-ingest-backlog).

## Dependency updates

[`.github/dependabot.yml`](../.github/dependabot.yml) opens grouped, weekly pull
requests for GitHub Actions updates. Journal-Utilities and the GNN parser are
pinned by commit SHA (tag and branch refs drift silently), so those bumps are
reviewed changes to the pin files rather than automatic updates.

## Local validation

`./run.sh all` is the release gate, and it is what a pull request should be
screened with. Two notes about running it here:

- `fast` and `full` execute fresh context-managed snapshots of pinned Git objects.
  Warm objects can be reused, but executable snapshots are never reused, including
  in CI. `--utilities PATH` or `$GATE_JU_CLONE` is an explicit object source:
  it must already contain the exact commit, regardless of HEAD; invalid explicit
  sources fail without fetching. Without an explicit source, local/cache objects
  are preferred and cold acquisition uses a new owned bare store. A `.gate-pin`
  stamp alone is insufficient. Caller working-tree bytes are preserved.
- `gnn` needs network on a cold cache and a Python in the pinned package's range.
- `all` validates every option before effects, then runs lint, docs, identity,
  full and gnn, stopping at the first nonzero result. Its `--utilities PATH`
  goes only to full and `--cold` only to gnn. Direct fast/full `--utilities`,
  direct gnn `--cold` and bench `--cold` remain available.

`lint`, `docs` and `identity` are offline subsets, not release, scientific,
hosted-CI or live-channel acceptance.

## Branch model

- `main` - content without audio.
- `audio` - `main` plus `<item>/audio/<name>.64k.m4a` (64 kbps), same layout.

Audio is never committed to `main`; the integrity gate enforces this.
