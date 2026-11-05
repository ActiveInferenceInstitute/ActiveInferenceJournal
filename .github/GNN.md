# GNN conformance

`gnn conformance (pinned)` is defined in `.github/workflows/journal-integrity.yml` and reads
`.github/gnn-pin.json`, which pins
`ActiveInferenceInstitute/Generalized_Notation_Notation` at `v5.0.3`
(`8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1`).

The job verifies the pin and installed parser, parses every `*.gnn.md` sketch
in the repository, and type-checks them. When the repository has no sketch yet,
it parses the pinned upstream `input/gnn_files/basics/static_perception.md`
exemplar; this is a pipeline and pin conformance baseline, not a claim that the
repository already contains a model.
