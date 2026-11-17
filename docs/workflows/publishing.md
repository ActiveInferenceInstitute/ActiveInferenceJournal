# Publishing — the group contract

Nine repositories produce, describe, publish and analyse the Institute's video and
document record. They coordinate one GNN pin and carry nine different
implementations of everything else. This page is the contract between them: which
repository owns which concern, what a record's identity is, and the one step each
member takes to stop carrying its own copy of a solved problem.

`./run.sh identity` checks the schema-declared record relationships and local
artifact agreement described below, using
[`record-identity.schema.json`](record-identity.schema.json) and
[`scripts/gate/identity.py`](../../scripts/gate/identity.py).
It is not a general JSON Schema validator, channel-freshness check, hosted-CI
receipt, scientific qualification or authenticated upstream release.

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
| Journal_Utilities | `uv run python run.py gate <arm>` | `lint format types test test-full docs gnn` | `docs/documentation-index.md` | none | member copy |
| institute_website | `./run.sh <arm>` | `lint fast full docs gnn build browser` | `docs/documentation-index.md` | none | member copy |
| ISSS | `./run.sh <arm>` | `lint test test-cov docs gnn ci timings` | `docs/documentation-index.md` | none | member copy |
| Knowledge-Engineering | `python .github/scripts/gate.py <arm>` | `links python notebooks checkpoints archive tests gnn fast full timings` | `docs/documentation-index.md` | none | member copy |
| Research-Discovery-Engine | `./run.sh <arm>` | `fast build website docs gnn lint types metrics all strict` | `Docs/documentation-index.md` | none | member copy |
| act_inf_metaanalysis | `./run.sh <arm>` | `lint types test-fast test-full docs gnn render all bench` | `docs/documentation-index.md` | `./run.sh render` → `uv run python scripts/15_render_publication.py --output-root .render-check` | member copy |
| ATLAS | `./gate <arm>` | `setup lint docs fast test gnn measure` | `docs/documentation-index.md` | none | member copy |
| Garden-of-Iris | `python scripts/gate.py <arm>` | `syntax docs fast tests models gnn` | `docs/documentation-index.md` | none | member copy |

Two of those arms are admitted red and must stay named as such: Research-Discovery-Engine
`lint` and `types` are excluded from its blocking `all`, and are documented in its
`Docs/RUN_GUIDE.md`. A red arm that is quietly dropped is worse than a documented one.

On 2026-11-12 all nine repositories carried the same `v5.0.3` pin at
`8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1`. The lead pin now names
`v5.1.0` at `75c834bd8519dc7b5adc4d24f16bf393cfd1ecdf`. The digest
below identifies its exact bytes. Each member advances in its own change
by taking those bytes and the associated digest from the accepted lead
revision, then running its local source and GNN conformance gates.
The lead's move does not advance the eight member copies.

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
| `session` | `<video_id>_sessNN` | this repository | `metadata.json` `sessions[].session_name`; `transcript.json` blocks | the leading 11 characters are a part's `video_id`, `NN` is a positive ordinal zero-padded to at least two digits (`01`–`99`, `100+`) |
| `session upload` | optional standalone video id | this repository | `metadata.json` `sessions[].video_id` | a separate upload link, not required to equal a part ID |
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
When `duplicate_of` is present in INDEX, its optional projection must agree
with metadata and resolve to an admitted indexed record under the same source
prefix. Identity checking adds no cycle, self-reference or video-equality policy.

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
| GNN pin | 9 files, 9 wrappers | published lead pin and dated member observations (above); wrappers: `arm_gnn.py`, `scripts/gnn_conformance.py` (JU, ISSS, ATLAS), `scripts/check_gnn_conformance.py` (website, Garden), `scripts/gnn_conformance.py` (RDE), `scripts/gnn_conformance.py` (act_inf) | this repository: [`../../.github/GNN.md`](../../.github/GNN.md) + [`../../.github/gnn-pin.json`](../../.github/gnn-pin.json) |
| Record identity grammar | 1 schema, 0 members | this page and [`record-identity.schema.json`](record-identity.schema.json) | this repository |
| Journal schema prose, mirrored by hand | 2 | [`../SCHEMA.md`](../SCHEMA.md) and Journal_Utilities `docs/JOURNAL_SCHEMA.md`, declared mirrored and measured 2026-11-12 at 183 differing lines | this repository: [`../SCHEMA.md`](../SCHEMA.md) |

The last row is the reason this contract exists. A declared mirror with no drift test
drifted. The replacement is a schema with a recorded digest, and a check that fails
when the digest and the file disagree.

## The drift test

The contract records each pinned artifact's sha256 next to its name, one `name  sha256`
line per copy. `./run.sh identity` recomputes every one, so an edited artifact with a stale
digest fails this repository's gate:

```text
record-identity.schema.json  e1e51b19fc3e6e90f478a0138ceef5ce53a57489573412aaf5128c933c509147
identity.py  a7258f6a92e95437091332de222066f4bdf89f78df16dc82867f29d751654100
identity_selftest.py  8021a807d62ece306e4076ca5b418f6c11356967f553f749f80eb0be3f1577cf
arm_docs.py  fdab3423cc0ef72f38f7f1e3037d7f71a74aa81f25a10b1adf006c73c3b816b2
docs_selftest.py  2d5c7b24f22ad78dbd0d3d799d790909b5e519968a820f7e02756f5ad396f5d8
gnn-pin.json  397e5f2803fadb6dfde336dbacf50ed195090effff1fdd13f54d0a8813cc1fa9
```

A member verifies its own copy with the same module and the same rule:

```bash
python3 scripts/gate/identity.py --verify-copy docs/workflows/record-identity.schema.json
python3 scripts/gate/identity.py --verify-copy scripts/gate/identity.py
```

That reads the digest recorded in the local `docs/workflows/publishing.md`-equivalent and
compares it to the file. A copy that has drifted, or a digest that was updated without
the file, fails. The lead repository runs exactly this command as part of `./run.sh
identity`, so the path members use is exercised by the lead's gate rather than assumed to
work.
These digests bind source artifacts, not their Git provenance. An adopting
owner must select an actual immutable producer revision and update selected
copies and their digest contract together; a dirty base revision cannot
identify new working-tree bytes. `--verify-copy`
checks exactly the caller-selected file against its local contract: it does not
fetch or authenticate a producer, establish freshness, or validate a member's
research corpus.

Knowledge-Engineering's archive consumer verifies copies, not a fabricated local
Journal corpus. Garden-of-Iris retains its own Markdown inventory, adapter and
generated-facts check. Its direct `check_links()`/`check_docs_index()` path needs
the selected `arm_docs.py` and existing dependencies; adopting/exposing the
native docs arm also requires `docs_selftest.py`. Adopting the new identity
arm/selftests requires the coherent identity module, selftest and unchanged
schema. No member copies or pins are changed by lead source qualification.

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
   add the digest check. The block above is a list of `name  sha256` lines and takes any
   artifact kind the contract pins — `.json`, `.py`, `.mjs`, `.sh` — so pin the Python
   modules too, not just the schema:
   - `scripts/gate/identity.py` takes no configuration; it reads the schema.
   - add `<file>  <sha256>` for every copy you keep to your contract copy, and run
     `python3 scripts/gate/identity.py --verify-copy <your copy>` from your gate.
     Identity real-file selftests exercise matching and independently diverged
     copies plus corpus/schema/path relationships; docs selftests exercise actual
     Markdown anchors, masked links and index reachability.
3. Replace a prose mirror with a pointer. Journal_Utilities' `docs/JOURNAL_SCHEMA.md` and
   this repository's [`../SCHEMA.md`](../SCHEMA.md) must not both define the schema; the
   mirror keeps its "How the pipeline writes this" chapters and links here for identity.
4. Do not adopt an arm you cannot run offline. `identity` is stdlib-only by design; a
   member whose interpreter lacks a JSON Schema validator does not need one — the module
   enforces the `x-identity` block directly.

Where a member's own gate already proves something this contract mentions, keep that and
do not duplicate it. This identity arm admits corpus-derived paths inside the
selected root before content reads; INDEX series/item/ordered part IDs and the
optional duplicate marker agree with metadata, the Boolean transcript flag
matches its regular artifact, and each schema-parsed session name belongs to a
part. Series ancestry stops at the corpus boundary. Contained symlinks and an
explicit symlinked root remain supported; this is not descriptor-level defense
against an adversarial concurrent writer. The pinned Journal-Utilities
`validate_journal.py` remains responsible for raw transcript blocks, URL
agreement, canonical-video uniqueness and manifest reconciliation. Caption and
translation filenames carry no inferred identity.

## Tools this host does not have

`jsonschema` is not installed on the reference host (probe 2026-11-12:
`python3 -c "import jsonschema"` → `ModuleNotFoundError`). The gate therefore does not run
a general JSON Schema engine: `scripts/gate/identity.py` enforces the `x-identity` block,
which is where every rule this contract claims lives. A member that wants the full
draft 2020-12 document validated can run
`uv run --with jsonschema python -m jsonschema -i <file> docs/workflows/record-identity.schema.json`;
that is an extra check, not the contract.

## Keeping this page honest

`./run.sh identity` fails for an invalid/incomplete schema contract, missing or
ambiguous artifacts, escaping discovered artifact paths, stale digests, or
real-file selftest failures. Corpus admission rejects unsafe/escaping INDEX,
record, metadata and transcript paths before content reads. It reconciles
metadata/path identity, the complete required INDEX projection and ordered
parts, strict Boolean transcript presence, optional session membership and
optional source-relative duplicate targets. The schema version remains
`record-identity/v1`; legitimate null category/episode values and empty parts
without sessions/transcripts remain supported. `./run.sh docs` checks links,
anchors, index coverage and isolated real-Markdown regressions. Neither arm
establishes immutable delivery or substitutes for the remaining producer/GNN
and member-owned acceptance.
