# .github

GitHub configuration for ActiveInferenceJournal: CI workflows, the pinned GNN
conformance record, and Dependabot settings. The workflows are described in
[`../docs/OPERATIONS.md`](../docs/OPERATIONS.md).

## Contents

| File | Purpose |
| --- | --- |
| [`workflows/journal-integrity.yml`](workflows/journal-integrity.yml) | Release gate: runs the `lint`, `docs`, `fast` and `full` arms of `./run.sh` (also callable via `workflow_call`). |
| [`workflows/gnn-conformance.yml`](workflows/gnn-conformance.yml) | Job `gnn-conformance`, display name `gnn conformance (pinned)`: runs `./run.sh gnn`. Separate from the deploy path because it installs a package from git. |
| [`workflows/deploy-pages.yml`](workflows/deploy-pages.yml) | Runs the integrity gate, then builds and deploys the static Pages bundle with the pinned Journal-Utilities builder and smoke-tests the deployed URLs. |
| [`workflows/weekly-ingest.yml`](workflows/weekly-ingest.yml) | Dispatch-only draft: secret-free channel enumeration, new-video delta, scaffold preview and reconciliation report. |
| [`GNN.md`](GNN.md) | What the pinned GNN conformance job parses, and how it picks sketches or the exemplar. |
| [`gnn-pin.json`](gnn-pin.json) | GNN pin (`gnn-importer-pin/v1`): repository, tag, revision. |
| [`journal-utilities-pin.json`](journal-utilities-pin.json) | Journal-Utilities pin (`journal-utilities-pin/v1`) with a `gate` and an `ingest` role. Read by the workflows via `scripts/gate/pin.py`. |
| [`dependabot.yml`](dependabot.yml) | Grouped weekly updates for GitHub Actions. |

Journal-Utilities and the GNN parser are pinned by commit SHA (tag and branch refs
drift silently). The workflows never carry a literal Journal-Utilities SHA: the
`ref` comes from the pin file through `python3 scripts/gate/pin.py --revision`, so
the gate, the deploy and the local `./run.sh` cannot drift apart, and the `lint`
arm fails if a literal SHA reappears.
