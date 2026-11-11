# `.aii/docs` — sidecar documents

Longer-form companions to [`../README.md`](../README.md) for **`ActiveInferenceInstitute/ActiveInferenceJournal`**. The
machine-readable source of truth stays [`../config.yaml`](../config.yaml); these
documents are its human face, and a folder that carries documents carries its own
[`README.md`](README.md) and [`AGENTS.md`](AGENTS.md).

| Document | Purpose |
| --- | --- |
| [`INTEGRATION.md`](INTEGRATION.md) | How this repository is federated, validated, and operated through InstituteOS. |

## Validate

```bash
python -m aii_platform.aii_sidecar.validate <repo> --completeness
python -m aii_platform.aii_sidecar docs <repo> --overwrite
python -m aii_platform.aii_sidecar.run <repo> --list
```

