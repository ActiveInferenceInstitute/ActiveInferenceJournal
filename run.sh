#!/bin/sh
# Single gate entry point. Every arm here is also the exact command CI runs:
#   ./run.sh <arm>
# See docs/OPERATIONS.md ("Gate arms") for what each arm covers.
set -eu
cd "$(dirname "$0")"
exec "${GATE_PYTHON:-python3}" -B scripts/gate/cli.py "$@"
