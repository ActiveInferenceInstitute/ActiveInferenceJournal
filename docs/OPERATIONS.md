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
| `docs` | seconds | Every relative link in every tracked Markdown file resolves with the exact case GitHub serves, in-page anchors exist, each doc under `docs/` is reachable from [`documentation-index.md`](documentation-index.md), the timings table covers exactly the arms, and every documented pin prefix matches a pin file. |
| `identity` | ~0.1 s | The publishing group contract: [`workflows/record-identity.schema.json`](workflows/record-identity.schema.json) parses and declares `record-identity/v1`, the digest recorded in [`workflows/publishing.md`](workflows/publishing.md) matches the file (the same `--verify-copy` path a member runs), every `item` names its own directory, every `series` names a directory above it, and every `parts[].video_id` is an 11-character id. |
| `fast` | ~1 s | `generate_journal_indexes.py --journal . --check` against the pinned Journal-Utilities: `INDEX.json`/`INDEX.md` are not stale. |
| `full` | ~30 s | The split-transcript check, the read-only `validate_journal.py` gate, and the manifest staleness/reconciliation report (E13). |
| `gnn` | minutes, network | The pinned GNN parser installs at the pinned revision, reports the pinned version, and parses/type-checks every `*.gnn.md` sketch (or the pinned upstream exemplar when the repository has none). The arm accepts only a literal `True` from the type checker's three-valued sentinel (`True`/`2`/`False`) and runs its own verdict selftest so a truthiness test cannot regress. |

There is no `types` arm: this repository ships no typed source. Arms are
stdlib-only Python, so there is no environment to install for `lint`, `docs`,
`fast` or `full`. `gnn` builds its own isolated environment because the pinned
package declares `requires-python >=3.11,<3.15`; on a host without such an
interpreter, set `GATE_PYTHON` or run `uv python install 3.12`.

That environment is keyed by repository, **revision** and interpreter, and the
installed parser is bound to the pin by the commit id pip records in
`direct_url.json`. A version string is not enough: bumping the revision while
the tag stays `v5.0.3` leaves `gnn.__version__` unchanged, so a version-keyed
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

## Workflows

| Workflow | File | Trigger | Purpose |
| --- | --- | --- | --- |
| Validate journal integrity | [`journal-integrity.yml`](../.github/workflows/journal-integrity.yml) | `push`, `pull_request`, `workflow_call` | Release gate: `lint`, `docs`, `fast`, `full` against the pinned Journal-Utilities. |
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
revision, then runs the four gate arms. The steps that used to be inline Python
heredocs in the workflow are now `scripts/gate/arm_manifest.py` and the
`fast`/`full` arms, so the locally reproduced command and the CI command are
literally the same file.

The reconciliation step reports manifest age and any channel/manifest/INDEX
disagreement; a manifest older than 7 days and duplicate ids are warnings, not
failures, until the scheduled refresh (M5) exists. `arm_manifest.py --strict`
turns them into failures when that lands.

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

## Dependency updates

[`.github/dependabot.yml`](../.github/dependabot.yml) opens grouped, weekly pull
requests for GitHub Actions updates. Journal-Utilities and the GNN parser are
pinned by commit SHA (tag and branch refs drift silently), so those bumps are
reviewed changes to the pin files rather than automatic updates.

## Local validation

`./run.sh all` is the release gate, and it is what a pull request should be
screened with. Two notes about running it here:

- `fast` and `full` need the pinned Journal-Utilities tree. With no arguments the
  gate exports it from a local clone (`$GATE_JU_CLONE`, else `../Journal_Utilities`)
  into `$GATE_CACHE` (default: the system temp directory) and reuses it; if the
  clone lacks the pinned commit it fetches it. Pass `--utilities PATH` to use an
  existing tree - it is refused unless it is at the pin.
- `gnn` needs network on a cold cache and a Python in the pinned package's range.

Offline, `lint` and `docs` are the whole gate, and both are seconds.

## Branch model

- `main` - content without audio.
- `audio` - `main` plus `<item>/audio/<name>.64k.m4a` (64 kbps), same layout.

Audio is never committed to `main`; the integrity gate enforces this.
