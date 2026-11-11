# Agent guide — `.aii/docs/`

Read [`README.md`](README.md) and [`../README.md`](../README.md) first. The documents
here describe how `ActiveInferenceInstitute/ActiveInferenceJournal` is federated through InstituteOS; the authoritative
metadata is [`../config.yaml`](../config.yaml) and the rendered record is
[`INTEGRATION.md`](INTEGRATION.md).

## Rules

- `INTEGRATION.md` is rendered from the sidecar. Edit [`../config.yaml`](../config.yaml)
  and regenerate; never hand-edit the rendered file.
- Metadata only. Never copy project content, credentials, private URLs, or personal
  data into these documents, and never move private-repository content into a public
  repository.
- Keep every claim true for a reader who has only this repository checked out, with no
  vault and no parent monorepo.
- Keep this folder self-contained: a directory that carries documents carries its own
  `README.md` and `AGENTS.md`.

## Validate and regenerate

```bash
python -m aii_platform.aii_sidecar.validate <repo> --completeness
python -m aii_platform.aii_sidecar docs <repo> --overwrite
python -m aii_platform.aii_sidecar.run <repo> --list
```

