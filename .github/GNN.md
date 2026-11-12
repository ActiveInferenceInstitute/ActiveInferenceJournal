# GNN conformance

The conformance job is `gnn-conformance`, display name `gnn conformance (pinned)`.
It lives in [`.github/workflows/gnn-conformance.yml`](workflows/gnn-conformance.yml)
and runs one gate arm, `./run.sh gnn`, which is what CI runs too.

## Pin

It reads [`gnn-pin.json`](gnn-pin.json), schema `gnn-importer-pin/v1`:

| Field | Value |
| --- | --- |
| `repository` | `ActiveInferenceInstitute/Generalized_Notation_Notation` |
| `tag` | `v5.0.3` |
| `revision` | `8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1` |

The arm asserts the pin's fields, installs the package from that exact revision
into an isolated environment, and fails unless the imported `gnn.__version__`
equals the tag without its leading `v` **and** the installed distribution's
`direct_url.json` records that same revision as its commit. The environment is
cached per repository, revision and interpreter, so a revision bump rebuilds it;
a version-only check would have passed a stale build, because the version string
does not change when only the revision does. The pinned package declares
`requires-python >=3.11,<3.15`.

## What it parses

| Situation | What is checked |
| --- | --- |
| The repository has `*.gnn.md` sketches | Every sketch is parsed, syntax-validated, then type-checked together. |
| The repository has none (current state) | The pinned upstream `input/gnn_files/basics/static_perception.md` at the pin is downloaded, parsed, syntax-validated and type-checked. |

The exemplar branch is a pipeline and pin conformance baseline: it does **not**
claim that this repository contains a model. The arm prints a JSON receipt with
`gnn-version`, `pin-revision`, `models`, `source` (`repository` or
`pinned-exemplar`) and `result`.

## Why it is not in the integrity workflow

The job installs a package from git, which is minutes on a cold runner. It used
to share a workflow file with the integrity gate, so `deploy-pages.yml` - which
calls that workflow - waited for it on every content deploy. The job key and
display name are unchanged; only the file moved.

## Running it

```bash
./run.sh gnn           # reuse the cached environment
./run.sh gnn --cold    # discard it and reinstall
```
