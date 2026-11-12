"""Selftest for the digest check the contract tells members to run.

The migration step asks each member to pin a `.py` copy, not only a schema, so
the drift test has to prove that path. This builds a fake checkout in a temp
directory — a module, a contract recording its sha256, and a prose line that
must not be mistaken for a digest — and asserts both directions: a matching copy
passes, a diverged copy fails with a drift message.

Deterministic, offline, no repository state touched. Run from the `identity`
arm so it cannot rot.
"""

from __future__ import annotations

import hashlib
import tempfile
from pathlib import Path

import identity

MODULE = "sample_module.py"
BODY = "VALUE = 1\n"
NOISE = (
    "A prose line that quotes  deadbeefdeadbeefdeadbeefdeadbeefdeadbeef  "
    "with two spaces and is not a digest record.\n"
)


def run() -> list[str]:
    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        module = root / "scripts" / "gate" / MODULE
        module.parent.mkdir(parents=True)
        module.write_text(BODY, encoding="utf-8")
        digest = hashlib.sha256(BODY.encode()).hexdigest()

        contract = root / "docs" / "workflows" / "publishing.md"
        contract.parent.mkdir(parents=True)
        contract.write_text(f"```text\n{MODULE}  {digest}\n```\n\n{NOISE}", encoding="utf-8")

        recorded = identity.recorded_digests(contract)
        if recorded != {MODULE: digest}:
            failures.append(f"selftest: parsed digests {recorded}, expected only {MODULE}")

        if identity.resolve_artifact(root, MODULE) != module:
            failures.append(f"selftest: could not resolve {MODULE} under {root}")

        problem = identity.verify_copy(module, contract)
        if problem is not None:
            failures.append(f"selftest: a matching .py copy was rejected: {problem}")

        module.write_text(BODY + "# drifted\n", encoding="utf-8")
        problem = identity.verify_copy(module, contract)
        if problem is None:
            failures.append("selftest: a diverged .py copy was accepted")
        elif "drifted" not in problem:
            failures.append(f"selftest: diverged copy failed without a drift message: {problem}")
    return failures


if __name__ == "__main__":  # pragma: no cover - the arm imports run()
    import sys

    problems = run()
    for message in problems:
        print(message, file=sys.stderr)
    sys.exit(1 if problems else 0)
