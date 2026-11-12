"""Arm: lint - structural invariants whose violation breaks CI silently.

Text- and JSON-level checks only, stdlib only: the same bytes run on a GitHub
runner and on a laptop, with nothing to install.
"""

from __future__ import annotations

import json
import re
import sys

from common import GNN_PIN, JU_PIN, ROOT, log, read_pin

WORKFLOWS = ROOT / ".github" / "workflows"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
USES = re.compile(r"^\s*(?:-\s*)?uses:\s*(\S+)(?:\s+#.*)?\s*$")
REF_OUTPUT = re.compile(
    r"^\s*ref:\s*\$\{\{\s*steps\.([A-Za-z0-9_-]+)\.outputs\.revision\s*\}\}"
)
LITERAL_REF = re.compile(r"^\s*ref:\s*([0-9a-f]{40})\s*$")
STEP_ID = re.compile(r"^\s*id:\s*(\S+)\s*$")
JU_CHECKOUT = "repository: ActiveInferenceInstitute/Journal_Utilities"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

failures: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


def check_workflows() -> None:
    for path in sorted(WORKFLOWS.glob("*.yml")):
        rel = path.relative_to(ROOT)
        lines = path.read_text(encoding="utf-8").splitlines()

        for key in ("name:", "on:", "permissions:"):
            if not any(line.startswith(key) for line in lines):
                fail(f"{rel}: missing top-level `{key}`")

        step_ids = {m.group(1) for line in lines for m in [STEP_ID.match(line)] if m}

        for number, line in enumerate(lines, 1):
            match = USES.match(line)
            if not match:
                continue
            target = match.group(1)
            if target.startswith(("./", "docker://")):
                continue
            if "@" not in target:
                fail(f"{rel}:{number}: `uses: {target}` has no ref")
            elif not HEX40.match(target.rsplit("@", 1)[1]):
                fail(f"{rel}:{number}: `uses: {target}` is not pinned to a 40-hex commit")

        for index, line in enumerate(lines):
            if line.strip() != JU_CHECKOUT:
                continue
            window = lines[max(0, index - 8) : index + 8]
            found = [m for m in (REF_OUTPUT.match(entry) for entry in window) if m]
            if not found:
                fail(
                    f"{rel}:{index + 1}: Journal-Utilities checkout must take its ref "
                    "from the pin step (`ref: ${{ steps.<id>.outputs.revision }}`)"
                )
            for match in found:
                if match.group(1) not in step_ids:
                    fail(
                        f"{rel}:{index + 1}: pin step id {match.group(1)!r} is not "
                        "defined in this workflow"
                    )
            for entry in window:
                literal = LITERAL_REF.match(entry)
                if literal:
                    fail(
                        f"{rel}:{index + 1}: literal Journal-Utilities SHA "
                        f"{literal.group(1)[:12]} - use the pin file instead"
                    )


def check_pin_files() -> None:
    ju = read_pin(JU_PIN)
    if ju.get("schema") != "journal-utilities-pin/v1":
        fail(f"{JU_PIN.name}: schema must be `journal-utilities-pin/v1`")
    if ju.get("repository") != "ActiveInferenceInstitute/Journal_Utilities":
        fail(f"{JU_PIN.name}: repository must be ActiveInferenceInstitute/Journal_Utilities")
    if not HEX40.match(str(ju.get("revision", ""))):
        fail(f"{JU_PIN.name}: revision must be a 40-hex commit")
    if not DATE.match(str(ju.get("recorded", ""))):
        fail(f"{JU_PIN.name}: recorded must be an ISO date (YYYY-MM-DD)")

    gnn = read_pin(GNN_PIN)
    if gnn.get("schema") != "gnn-importer-pin/v1":
        fail(f"{GNN_PIN.name}: schema must be `gnn-importer-pin/v1`")
    if gnn.get("repository") != "ActiveInferenceInstitute/Generalized_Notation_Notation":
        fail(f"{GNN_PIN.name}: unexpected repository")
    if not HEX40.match(str(gnn.get("revision", ""))):
        fail(f"{GNN_PIN.name}: revision must be a 40-hex commit")
    if not str(gnn.get("tag", "")).startswith("v"):
        fail(f"{GNN_PIN.name}: tag must look like vX.Y.Z")
    if not DATE.match(str(gnn.get("recorded", ""))):
        fail(f"{GNN_PIN.name}: recorded must be an ISO date (YYYY-MM-DD)")


def check_shipped_json() -> None:
    paths = sorted(ROOT.glob("*.json"))
    paths += sorted((ROOT / ".github").glob("*.json"))
    paths += sorted((ROOT / ".aii").glob("*.json"))
    for path in paths:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{path.relative_to(ROOT)}: invalid JSON ({exc})")


def run(argv: list[str]) -> int:
    if argv:
        raise SystemExit(f"gate: lint takes no arguments, got {argv}")
    check_workflows()
    check_pin_files()
    check_shipped_json()
    if failures:
        for message in failures:
            print(f"lint: FAIL {message}", file=sys.stderr)
        return 1
    log("lint: ok (workflow pins, pin files, shipped JSON)")
    return 0
