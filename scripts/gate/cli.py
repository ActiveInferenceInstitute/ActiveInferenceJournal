"""Single entry point for every gate arm.

``./run.sh <arm>`` execs this module, so the arm a developer runs and the arm CI
runs are the same command line. Arms are independent: each one runs alone, and
``all`` runs them in a fixed order.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import GateError  # noqa: E402

ARMS: dict[str, str] = {
    "lint": "repository invariants: action pins, pin-file schema, shipped JSON",
    "docs": "documentation: relative links, anchors, index coverage, documented pins",
    "identity": "publishing contract: record identity grammar and the schema digest",
    "fast": "pinned Journal-Utilities derived-index check (seconds)",
    "full": "pinned Journal-Utilities transcript + integrity gates, manifest reconciliation",
    "gnn": "pinned Generalized Notation Notation parser conformance",
    "all": "lint, docs, identity, full, gnn",
    "bench": "measure every arm and refresh docs/_generated/gate-timings.md",
}

# ``fast`` is a subset of ``full``, so ``all`` runs the longer arm only.
ORDER = ["lint", "docs", "identity", "full", "gnn"]


def usage() -> None:
    print("usage: ./run.sh <arm> [options]\n")
    width = max(len(name) for name in ARMS)
    for name, description in ARMS.items():
        print(f"  {name:<{width}}  {description}")
    print(
        "\noptions: --utilities PATH  use an existing Journal-Utilities tree"
        "\n         --write | --check  bench only: refresh or verify the timings doc"
    )


def main(argv: list[str]) -> int:
    if not argv or argv[0] in {"-h", "--help", "help", "--list"}:
        usage()
        return 0

    arm, rest = argv[0], argv[1:]
    if arm not in ARMS:
        usage()
        raise GateError(f"unknown arm {arm!r}")

    if arm == "all":
        for name in ORDER:
            importlib.import_module(f"arm_{name}").run([])
        return 0

    return importlib.import_module(f"arm_{arm}").run(rest)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
