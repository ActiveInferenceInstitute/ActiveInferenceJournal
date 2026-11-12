"""Selftest for the GNN conformance verdict.

``GNNTypeChecker.validate_gnn_files`` returns three sentinels: ``True`` when
every file validates, ``2`` when the run completed but one or more files had
type/consistency problems **or no GNN files were found**, and ``False`` on a
hard failure. The arm must accept only ``True``: a truthiness test accepts
``2`` and prints ``"result": "verified"`` for a rejected run.

This drives the real ``arm_gnn.verify()`` against a valid sketch with the
checker's verdict stubbed, and asserts that every value other than ``True`` is
refused and that the refusal reports the returned value. Run from the ``gnn``
arm so it cannot rot.
"""

from __future__ import annotations

import contextlib
import io
import tempfile
from pathlib import Path

import arm_gnn

SKETCH = """# GNN Example: Selftest Model

# GNN Version: 1.0

## GNNSection

ActInfPOMDP

## GNNVersionAndFlags

GNN v1

## ModelName

Selftest Model

## ModelAnnotation

Minimal static perception model used by the gate's own verdict selftest.

## StateSpaceBlock

A[2,2,type=float]
s[2,1,type=float]
o[2,1,type=int]

## Connections

s-A
A-o

## InitialParameterization

A={(0.9, 0.2),(0.1, 0.8)}

## Equations

A[o,s] = P(o | s).

## Time

Static

## ActInfOntologyAnnotation

A=LikelihoodMatrix
s=HiddenState
o=Observation

## Footer

Selftest Model v1.

## Signature

Cryptographic signature goes here
"""

VERDICTS = (2, False, None, 0)


def _attempt(verdict: object) -> tuple[bool, str]:
    """Run ``arm_gnn.verify()`` with ``verdict`` stubbed; return (refused, output)."""
    from gnn.type_checker import GNNTypeChecker

    original = GNNTypeChecker.validate_gnn_files
    original_root = arm_gnn.ROOT
    with tempfile.TemporaryDirectory(prefix="gnn-selftest-") as tmp:
        root = Path(tmp)
        (root / "selftest.gnn.md").write_text(SKETCH, encoding="utf-8")
        arm_gnn.ROOT = root
        GNNTypeChecker.validate_gnn_files = lambda self, *args, **kwargs: verdict
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output):
                arm_gnn.verify()
        except SystemExit as exc:
            return True, f"{exc}\n{output.getvalue()}"
        finally:
            GNNTypeChecker.validate_gnn_files = original
            arm_gnn.ROOT = original_root
    return False, output.getvalue()


def run() -> list[str]:
    failures: list[str] = []
    for verdict in VERDICTS:
        refused, output = _attempt(verdict)
        if not refused:
            failures.append(
                f"selftest: the arm accepted validate_gnn_files() -> {verdict!r}; "
                f"output: {output.strip()!r}"
            )
        elif repr(verdict) not in output:
            failures.append(
                f"selftest: refusal for {verdict!r} did not report the returned value; "
                f"output: {output.strip()!r}"
            )
    refused, output = _attempt(True)
    if refused:
        failures.append(f"selftest: the arm refused a conformant run; output: {output.strip()!r}")
    elif '"result": "verified"' not in output:
        failures.append(f"selftest: a conformant run did not print verified; output: {output.strip()!r}")
    return failures


if __name__ == "__main__":  # pragma: no cover - the arm runs it as a subprocess
    import sys

    problems = run()
    for message in problems:
        print(message, file=sys.stderr)
    sys.exit(1 if problems else 0)
