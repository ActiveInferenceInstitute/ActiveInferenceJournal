"""Single entry point for every gate arm.

``./run.sh <arm>`` execs this module, so the arm a developer runs and the arm CI
runs are the same command line. Arms are independent: each one runs alone, and
``all`` validates its options before running them in a fixed order, stopping at
the first failure and returning that arm's status.
"""

from __future__ import annotations

import argparse
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
        "\noptions: --utilities PATH  fast/full/all: snapshot a local Git object source"
        "\n         --cold            gnn/bench/all: rebuild the GNN environment"
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
        parser = argparse.ArgumentParser(
            prog="./run.sh all",
            description="Run lint, docs, identity, full and gnn; stop at the first failure.",
            allow_abbrev=False,
        )
        parser.add_argument("--utilities", help="Journal-Utilities Git object source")
        parser.add_argument("--cold", action="store_true", help="rebuild the GNN environment")
        args = parser.parse_args(rest)
        if args.utilities is not None and not args.utilities.strip():
            parser.error("--utilities requires a nonempty path")
        for name in ORDER:
            options: list[str] = []
            if name == "full" and args.utilities is not None:
                options = ["--utilities", args.utilities]
            elif name == "gnn" and args.cold:
                options = ["--cold"]
            result = importlib.import_module(f"arm_{name}").run(options)
            if result != 0:
                return result
        return 0

    return importlib.import_module(f"arm_{arm}").run(rest)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except GateError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(exc.code)
