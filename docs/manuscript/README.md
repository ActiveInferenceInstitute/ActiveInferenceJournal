# A source-namespaced corpus of Active Inference Institute video records

This repository report documents the public implementation and its evidence.
Start with the [abstract](00_abstract.md) and [introduction](01_introduction.md).
The numbered Markdown sources assemble in order. [Configuration](config.yaml)
records metadata and enabled formats, and [the bibliography](references.bib)
records the source revisions. The [documentation hub](../README.md) links to
the operating guides.

## Render and validate

Run from a disposable checkout of this repository with Git, uv, a supported Python,
Pandoc, XeLaTeX, latexmk, and the [template TeX dependencies](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/docs/guides/startup-and-setup.md).
The [pinned renderer](https://github.com/docxology/template/tree/87704feae0a4490ef7dad9c931d268e8c30273c2)
discovers this `docs/manuscript/` and writes reports under `output/`.

```bash
source_checkout="$(pwd -P)"
project="$(basename "$source_checkout")"
renderer_checkout="$(mktemp -d)/template"
git clone https://github.com/docxology/template.git "$renderer_checkout"
git -C "$renderer_checkout" checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
cd "$renderer_checkout"
uv sync --locked --no-default-groups
mkdir -p projects/working
ln -s "$source_checkout" "projects/working/$project"
uv run --no-sync python scripts/pipeline/stage_03_render.py --project "working/$project"
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project "working/$project"
```

Review `output/pdf/<project>_combined.pdf`, the combined HTML under
`output/web/`, and the verdict and provenance under `output/reports/`.
The renderer's output is derived from these sources.
