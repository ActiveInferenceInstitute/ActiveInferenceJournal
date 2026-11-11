# .github

GitHub configuration for ActiveInferenceJournal: CI workflows, the pinned GNN
conformance record, and Dependabot settings. The workflows are described in
[`../docs/OPERATIONS.md`](../docs/OPERATIONS.md).

## Contents

| File | Purpose |
| --- | --- |
| [`workflows/journal-integrity.yml`](workflows/journal-integrity.yml) | Release gate — derived indexes, split transcript artifacts, the read-only journal integrity check, manifest reconciliation, and GNN conformance (also callable via `workflow_call`). |
| [`workflows/deploy-pages.yml`](workflows/deploy-pages.yml) | Builds and deploys the static Pages bundle with the pinned Journal-Utilities builder, then smoke-tests the deployed URLs. |
| [`workflows/weekly-ingest.yml`](workflows/weekly-ingest.yml) | Dispatch-only draft: secret-free channel enumeration, new-video delta, scaffold preview and reconciliation report. |
| [`GNN.md`](GNN.md) | Notes on the pinned Generalized Notation Notation conformance job. |
| [`gnn-pin.json`](gnn-pin.json) | The pinned GNN repository, tag and commit read by the conformance job. |
| [`dependabot.yml`](dependabot.yml) | Grouped weekly updates for GitHub Actions. |

Journal-Utilities is pinned by commit SHA in the workflows (tag and branch refs drift
silently), so pin bumps are reviewed changes rather than automatic updates.
