# Agent guide — .aii/

Read [`README.md`](README.md) first. This folder is the committed InstituteOS sidecar
for `ActiveInferenceInstitute/ActiveInferenceJournal`; `config.yaml` is its single source of truth.

## Rules

- Keep `schema: aii-sidecar/v1` and bump `meta.updated` whenever the sidecar changes.
- Only curated metadata belongs here. Never duplicate GitHub-API facts (stars, size,
  language) and never copy repository content into the sidecar.
- `artifacts[].path`, `provenance.releases_manifest`, and `docs[]` are validated to
  exist. Keep them repository-relative and current.
- `ecosystem.relations[].repo` must be `owner/repo`; use the relation vocabulary in
  the schema (`references`, `referenced-by`, `derived-from`, `feeds`, `documents`,
  `mirrors`, `depends-on`).
- Keep the sidecar standalone: it must validate and make sense without the parent
  vault or monorepo.
- Do not put credentials, private URLs, personal data, or unverified claims in the
  sidecar. Private repositories must not copy sidecar content into a public repo.
- Task commands execute repository-declared commands. Run them only for trusted
  checkouts, and never add a task that mutates shared state.

## Validate and regenerate

```bash
python -m aii_platform.aii_sidecar.validate <repo> --completeness
python -m aii_platform.aii_sidecar docs <repo> --overwrite
python -m aii_platform.aii_sidecar.run <repo> --list
```

Regenerating the sidecar docs is safe: it rewrites only `README.md`, `AGENTS.md`,
`docs/README.md`, `docs/AGENTS.md`, and `docs/INTEGRATION.md` inside `.aii/`, never
project source.
