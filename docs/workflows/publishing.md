# Publishing — the group contract

Nine repositories produce, describe, publish and analyse the Institute's video and
document record. They already share one pin byte-for-byte and nine different
implementations of everything else. This page is the contract between them: which
repository owns which concern, what a record's identity is, and the one step each
member takes to stop carrying its own copy of a solved problem.

The contract is enforceable, not aspirational. Every rule below is checked by
`./run.sh identity` in this repository against
[`record-identity.schema.json`](record-identity.schema.json), and a member can run the
same check against its own copy with
[`scripts/gate/identity.py`](../../scripts/gate/identity.py).

## Evidence rule

Documentation here is a view over source-owned facts, not a second place to keep them.

| Claim | Authoritative source |
| --- | --- |
| A record's identity fields and their grammar | [`record-identity.schema.json`](record-identity.schema.json) — `x-identity` |
| A member's gate command and arms | that member's gate entry point, listed below |
| Pin revisions | each member's `.github/gnn-pin.json` and `.github/journal-utilities-pin.json` |
| Arm wall time | this repository's [`_generated/gate-timings.md`](../_generated/gate-timings.md); never a number in prose |
| What a repository currently contains | the repository, read on the day of the claim; dated measurements below say when |

## Members

One active copy per repository. The gate command is the *only* documented way to run a
member's checks; a command that is not an arm of that entry point is not part of the gate.

| Repository | Gate entry point | Arms | Docs index | Manuscript command | GNN pin |
| --- | --- | --- | --- | --- | --- |
| ActiveInferenceJournal (lead) | `./run.sh <arm>` | `lint docs identity fast full gnn all bench` | `docs/documentation-index.md` | none | `.github/gnn-pin.json` |
| Journal_Utilities | `uv run python run.py gate <arm>` | `lint format types test test-full docs gnn` | `docs/documentation-index.md` | none | same pin |
| institute_website | `./run.sh <arm>` | `lint fast full docs gnn build browser` | `docs/documentation-index.md` | none | same pin |
| ISSS | `./run.sh <arm>` | `lint test test-cov docs gnn ci timings` | `docs/documentation-index.md` | none | same pin |
| Knowledge-Engineering | `python .github/scripts/gate.py <arm>` | `links python notebooks checkpoints archive tests gnn fast full timings` | `docs/documentation-index.md` | none | same pin |
| Research-Discovery-Engine | `./run.sh <arm>` | `fast build website docs gnn lint types metrics all strict` | `Docs/documentation-index.md` | none | same pin |
| act_inf_metaanalysis | `./run.sh <arm>` | `lint types test-fast test-full docs gnn render all bench` | `docs/documentation-index.md` | `./run.sh render` → `uv run python scripts/15_render_publication.py --output-root .render-check` | same pin |
| ATLAS | `./gate <arm>` | `setup lint docs fast test gnn measure` | `docs/documentation-index.md` | none | same pin |
| Garden-of-Iris | `python scripts/gate.py <arm>` | `syntax docs fast tests models gnn` | `docs/documentation-index.md` | none | same pin |

Two of those arms are admitted red and must stay named as such: Research-Discovery-Engine
`lint` and `types` are excluded from its blocking `all`, and are documented in its
`Docs/RUN_GUIDE.md`. A red arm that is quietly dropped is worse than a documented one.

The pin is byte-identical in all nine repositories as of 2026-11-12:
`8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1` (`v5.0.3`), sha256
`eb83f7f1b73eb31e116bd05b1f457dd07e6874a2a4ba0e9e95e5bc91f094cd55`. Its *consumers*
are nine independently written wrappers; see "Shared concerns" below.

## The record and its identity

A record is one item folder in this corpus: `data/<type>/<source>/…/<series>/<item>/`
with a canonical `metadata.json`. Everything else — transcripts, captions,
translations, derived pages, graph nodes, publication snapshots — hangs off that
record by one of the keys below.

Canonical home: **this repository**,
[`record-identity.schema.json`](record-identity.schema.json), schema_version
`record-identity/v1`. The human-readable description of the folder and the
transcript layers is [`../SCHEMA.md`](../SCHEMA.md); that page is prose over this
schema, not a second definition of it.

| Namespace | Key | Owner | Carrier | Rule |
| --- | --- | --- | --- | --- |
| `item` | item id | this repository | `metadata.json` `item`; `INDEX.json` `path` | equals the item directory name |
| `video` | 11-character YouTube id | this repository records; YouTube assigns | `metadata.json` `parts[].video_id`; `INDEX.json` `parts[]` | `^[A-Za-z0-9_-]{11}$` |
| `session` | `<video_id>_sessNN` | this repository | `metadata.json` `sessions[].session_name`; `transcript.json` blocks | the leading 11 characters are a part's `video_id`, `NN` is two digits |
| `paper` | `doi:`/`arxiv:`/`s2:`/`openalex:`/`title:` id | act_inf_metaanalysis | `output/data/corpus.jsonl` `paper_id`; this repository's `metadata.json` `doi` | prefix decides the scheme |
| `doc` | `document_name` | ISSS | `archived_documents/metadata.json` `document_name` | the basename of the source URL |
| `pub` | DOI + version | act_inf_metaanalysis | `manuscript/config.yaml` `doi` + `version` | one deposited publication |

Join rules, in the order a consumer should apply them:

1. **Video content**: join on `video`. `video_id` is the only key every video
   producer writes and every video consumer can obtain. institute_website's
   `scripts/sync_video_transcripts.py` is the reference consumer: it reads this
   repository's `INDEX.json`, derives the id from `parts[].url` and matches it
   against its own `youtubeId`.
2. **Documents**: join on `paper`. A DOI is the only thing ISSS, Knowledge-Engineering,
   Research-Discovery-Engine and act_inf_metaanalysis all hold.
3. **Publications**: join on `pub`, never on a PDF filename or a directory name.
4. **Item ids are local.** `GuestStream_094` means nothing outside this corpus.
   A cross-repository reference carries the path (`<type>/<source>/…/<item>`) or the
   `video_id`, never the bare item id.

### `duplicate_of` is a path, with the source prefix removed

Measured 2026-11-12: 34 records carry `duplicate_of`, and all 34 resolve uniquely when
the first three path components (`data/<type>/<source>/`) are dropped from the record
path. The value is therefore **not** an `INDEX.json` path and **not** a bare item id.
A consumer that concatenates `duplicate_of` onto an `INDEX.json` path gets a path that
does not exist; a consumer that matches it as a suffix gets the right record.

### What carries no identity

The identity of a record is `metadata.json`. Two folders hold files whose names look
like identity and are not:

- `captions/` — names are verbatim source names. Measured 2026-11-12: 624 files, 421
  starting `youtube_captions`, the rest human video titles. Never derive a record id
  from a caption filename.
- `translations/` — 249 distinct name prefixes, most but not all of them video ids.
  Resolve the record through `metadata.json` first.

An `INDEX.json`-only consumer is safe: `path`, `series`, `item`, `parts` and
`has_transcript` are enough to address a record and to find its transcript.

## Shared concerns and their canonical home

Each concern below is implemented in every member. That is why it is a contract and
not a preference: nine copies of a link checker are nine chances to disagree about
what a broken link is.

| Concern | Copies | Evidence | Canonical home |
| --- | --- | --- | --- |
| Gate entry point and arm registry | 9 | `run.sh:7` → `scripts/gate/cli.py:19-26` (this repo); `run.py:641-655` (JU); `run.sh:38-48` (ISSS); `run.sh:4` → `scripts/gates.mjs:6-18` (website); `.github/scripts/gate.py:67-78` (KE); `run.sh:46-108` (RDE); `scripts/gate.py:28-48` (act_inf); `gate:27-38` (ATLAS); `scripts/gate.py:76-101` (Garden) | this repository: [`../../scripts/gate/cli.py`](../../scripts/gate/cli.py) |
| Relative-link and anchor checker | 9 | `scripts/gate/arm_docs.py:110-150`; `scripts/check_docs_links.py` (JU); `scripts/check_docs.py:81-93` (ISSS); `package.json:17` (website); `.github/scripts/archive_checks.py:59-83` (KE); `scripts/check_docs_links.py` (RDE); `scripts/docs_qa.py:44-63` (ATLAS); `scripts/check_docs.py:81-93` (act_inf); `scripts/check_markdown_links.py:81-100` (Garden) | this repository: [`../../scripts/gate/arm_docs.py`](../../scripts/gate/arm_docs.py) |
| Docs-index coverage rule | 4 | `arm_docs.py:153-172`; `check_docs_links.py:86-96` (JU); `check_docs.py:97-111` (act_inf); `scripts/measure_gates.py:59-66` (website). ISSS, KE, RDE, ATLAS, Garden check no coverage at all. | this repository: [`../../scripts/gate/arm_docs.py`](../../scripts/gate/arm_docs.py) |
| Arm measurement → generated Markdown | 9 | `arm_bench.py`; `run.py:809-912` (JU); `scripts/gate_report.py:176-185` (ISSS); `scripts/gate.py:159-203` (act_inf); `scripts/gate_metrics.py:215-216` (RDE); `scripts/gate_metrics.py:277,290` (ATLAS); `.github/scripts/gate.py:208-232` (KE); `scripts/gate.py:373-418` (Garden); `scripts/measure_gates.py:110-111` (website) | this repository: [`../../scripts/gate/arm_bench.py`](../../scripts/gate/arm_bench.py) |
| GNN pin | 9 files, 9 wrappers | identical sha256 in all nine (above); wrappers: `arm_gnn.py`, `scripts/gnn_conformance.py` (JU, ISSS, ATLAS), `scripts/check_gnn_conformance.py` (website, Garden), `scripts/gnn_conformance.py` (RDE), `scripts/gnn_conformance.py` (act_inf) | this repository: [`../../.github/GNN.md`](../../.github/GNN.md) + [`../../.github/gnn-pin.json`](../../.github/gnn-pin.json) |
| Record identity grammar | 1 schema, 0 members | this page and [`record-identity.schema.json`](record-identity.schema.json) | this repository |
| Journal schema prose, mirrored by hand | 2 | [`../SCHEMA.md`](../SCHEMA.md) and Journal_Utilities `docs/JOURNAL_SCHEMA.md`, declared mirrored and measured 2026-11-12 at 183 differing lines | this repository: [`../SCHEMA.md`](../SCHEMA.md) |

The last row is the reason this contract exists. A declared mirror with no drift test
drifted. The replacement is a schema with a recorded digest, and a check that fails
when the digest and the file disagree.

## The drift test

The contract records the schema's sha256 next to its name. `./run.sh identity` recomputes
it, so an edited schema with a stale digest fails this repository's gate:

```text
record-identity.schema.json  84f6c4df6efc3f15f0d8a9a05c8aabd0cbdc08b0f4feac5fcc8ae860a81e306b
```

A member verifies its own copy with the same module and the same rule:

```bash
python3 scripts/gate/identity.py --verify-copy docs/workflows/record-identity.schema.json
```

That reads the digest recorded in the local `docs/workflows/publishing.md`-equivalent and
compares it to the file. A copy that has drifted, or a digest that was updated without
the file, fails. The lead repository runs exactly this command as part of `./run.sh
identity`, so the path members use is exercised by the lead's gate rather than assumed to
work.

## Migration step for every member

Every member takes the same step, and it is one step, not a rewrite: **stop keeping a
private copy of a shared concern; point at the canonical one and pin it by digest.**

1. Record the four facts this page lists for you (gate command, docs index path, manuscript
   command, pin) in your `.aii/config.yaml` under `tasks:` — one task per documented arm
   command, so the sidecar cannot claim a command the gate does not have. Five members
   (Journal_Utilities, ISSS, Knowledge-Engineering, Research-Discovery-Engine,
   act_inf_metaanalysis) list a `docs:` path that does not exist — `docs/INTEGRATION.md` in
   all five, and `docs/AGENTS.md` in the last two; fix those paths in the same edit. This
   repository's own sidecar had the same `docs/INTEGRATION.md` entry and lost it when this
   page landed.
2. For the concerns you keep locally (all five at present), copy the canonical file and
   add the digest check:
   - `scripts/gate/identity.py` takes no configuration; it reads the schema.
   - add `<file>  <sha256>` to your copy of this page's digest block, and run
     `python3 scripts/gate/identity.py --verify-copy <your copy>` from your gate.
3. Replace a prose mirror with a pointer. Journal_Utilities' `docs/JOURNAL_SCHEMA.md` and
   this repository's [`../SCHEMA.md`](../SCHEMA.md) must not both define the schema; the
   mirror keeps its "How the pipeline writes this" chapters and links here for identity.
4. Do not adopt an arm you cannot run offline. `identity` is stdlib-only by design; a
   member whose interpreter lacks a JSON Schema validator does not need one — the module
   enforces the `x-identity` block directly.

Where a member's own gate already proves something this contract mentions, keep that and
do not duplicate it. `validate_journal.py` in the pinned Journal-Utilities revision is the
authority for the raw transcript layer (blank session ids, part URL agreement,
`duplicate_of` resolution, manifest reconciliation); this repository's `identity` arm
deliberately does not re-check it.

## Tools this host does not have

`jsonschema` is not installed on the reference host (probe 2026-11-12:
`python3 -c "import jsonschema"` → `ModuleNotFoundError`). The gate therefore does not run
a general JSON Schema engine: `scripts/gate/identity.py` enforces the `x-identity` block,
which is where every rule this contract claims lives. A member that wants the full
draft 2020-12 document validated can run
`uv run --with jsonschema python -m jsonschema -i <file> docs/workflows/record-identity.schema.json`;
that is an extra check, not the contract.

## Keeping this page honest

`./run.sh identity` fails when the schema does not parse, when its `schema_version` is not
`record-identity/v1`, when its `x-identity` block is incomplete, when the recorded digest
above does not match the file, when a record's `item` does not name its own directory, when
its `series` names no directory above it, or when a part's `video_id` is not an
11-character id. `./run.sh docs` fails when a link on this page does not resolve with the
exact case GitHub serves.
