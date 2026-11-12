# Documentation index

Flat index of the long-lived documents in this repository. The hub is
[`README.md`](README.md); this page exists so nothing under `docs/` is reachable
only by memory. Generated facts live in [`_generated/`](_generated/README.md).

## Technical documentation (`docs/`)

| Document | Covers | Owner |
| --- | --- | --- |
| [`SCHEMA.md`](SCHEMA.md) | Canonical per-item schema: `metadata.json`, `transcript.*`, `captions/`, `translations/`, `assets/`, and the `INDEX.json` contract. | hand-written |
| [`ORGANIZATION.md`](ORGANIZATION.md) | Top-level namespace (`data/video/<source>/`, `data/<type>/<source>/`), series and item layout, adding other channels or non-video sources. | hand-written |
| [`PIPELINE.md`](PIPELINE.md) | How content is produced and kept complete and idempotent, and the Journal-Utilities boundary. | hand-written |
| [`OPERATIONS.md`](OPERATIONS.md) | CI workflows, the gate arms (`./run.sh`), pins, dependency updates, local validation, branch model. | hand-written |
| [`m4-site-spec.md`](m4-site-spec.md) | Spec for the static per-item pages plus `sitemap.xml`/`robots.txt`, implemented by the Journal-Utilities builder. | hand-written |
| [`translation-migration-map.md`](translation-migration-map.md) | Item-by-item map of the legacy `Translations/` migration and the quarantined conflicts. | hand-written |
| [`volunteer-transcript-tasks.md`](volunteer-transcript-tasks.md) | Volunteer triage list of remaining translation files and conflict backlog. | hand-written |
| [`good-first-issues-draft.md`](good-first-issues-draft.md) | Ready-to-file `good-first-issue` drafts for volunteer batches. | hand-written |
| [`misfiling-findings.md`](misfiling-findings.md) | Captions/translations misfiling dispositions. | hand-written |
| [`AGENTS.md`](AGENTS.md) | Conventions for agents and programs operating on this repository. | hand-written |
| [`workflows/publishing.md`](workflows/publishing.md) | Publishing group contract: members and their gate commands, the record identity schema and its canonical home, shared concerns and their owners, the member migration step. | hand-written |
| [`workflows/record-identity.schema.json`](workflows/record-identity.schema.json) | The canonical identity grammar (`record-identity/v1`) for `metadata.json` and the cross-repository join keys; enforced by `./run.sh identity`. | hand-written |

## Generated facts (`docs/_generated/`)

| Document | Producer |
| --- | --- |
| [`gate-timings.md`](_generated/gate-timings.md) | `./run.sh bench` |
| [`gate-baseline.json`](_generated/gate-baseline.json) | recorded once at the pre-change commit; rendered by the bench arm |

## Repository-level documents

| Document | Covers |
| --- | --- |
| [`README.md`](../README.md) | What the journal is, layout, branches, usage, provenance, InstituteOS sidecar. |
| [`AGENTS.md`](../AGENTS.md) | Agent entry points, rules, gate commands, layout. |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Hand-editable vs generated files, rules, validation. |
| [`TO-DO.md`](../TO-DO.md) | Scoped improvement list and open items. |
| [`SECURITY.md`](../SECURITY.md) | Credentials, audio off `main`, private reporting. |
| [`CITATION.cff`](../CITATION.cff) | Dataset citation. |
| [`INDEX.json`](../INDEX.json) / [`INDEX.md`](../INDEX.md) | Machine and human entry points to the content (generated). |
| [`.github/README.md`](../.github/README.md) | Workflows, pins and Dependabot settings. |
| [`.aii/README.md`](../.aii/README.md) | InstituteOS sidecar. |

## Keeping this index honest

`./run.sh docs` fails when a Markdown file under `docs/` is not reachable from
this page, when a relative link does not resolve with the exact case GitHub
serves, or when a documented pin prefix does not match
[`.github/journal-utilities-pin.json`](../.github/journal-utilities-pin.json) or
[`.github/gnn-pin.json`](../.github/gnn-pin.json).
