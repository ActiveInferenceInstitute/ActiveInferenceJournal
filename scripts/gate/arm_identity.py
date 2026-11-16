"""Arm: identity - the publishing group's record-identity contract.

The schema declares contained corpus paths, the INDEX/metadata identity
projection, transcript presence and session-to-part membership. The arm checks
those relationships, local artifact digests and real-file regressions.
Series ancestry stops at the selected corpus boundary. This is not a general
JSON Schema validator, live freshness check or authenticated upstream release.

The raw transcript layer is deliberately out of scope: the pinned
``validate_journal.py`` in the ``full`` arm already refuses a split record with
a blank ``video_id``, a mismatched part URL, a duplicate canonical video id and
an unresolved ``duplicate_of``. Re-checking it here would be a second copy of
a check this repository already runs.
"""

from __future__ import annotations

import sys

import identity
import identity_selftest
from common import ROOT, log

SCHEMA = ROOT / "docs" / "workflows" / "record-identity.schema.json"
CONTRACT = ROOT / "docs" / "workflows" / "publishing.md"


def run(argv: list[str]) -> int:
    if argv:
        raise SystemExit(f"gate: identity takes no arguments, got {argv}")

    spec = identity.load_schema(SCHEMA)
    failures = identity.check_contract(CONTRACT, spec)
    corpus_failures, counts = identity.check_corpus(ROOT, spec)
    failures += corpus_failures

    problem = identity.verify_copy(SCHEMA, CONTRACT)
    if problem:
        failures.append(problem)

    # Real-file corpus admission and matching/diverged artifact-copy regressions.
    failures += identity_selftest.run()

    if failures:
        for message in failures:
            print(f"identity: FAIL {message}", file=sys.stderr)
        return 1
    log(
        f"identity: ok ({counts['records']} records, {counts['parts']} videos, "
        f"{counts['duplicates']} duplicate records; {SCHEMA.name} {spec.digest()[:12]})"
    )
    return 0
