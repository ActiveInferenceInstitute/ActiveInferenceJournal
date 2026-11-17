"""The pinned Journal-Utilities gates shared by the ``fast`` and ``full`` arms.

``fast`` is the derived-index check alone (seconds). ``full`` adds the split
transcript check, the read-only integrity gate, and manifest reconciliation.
Both execute an owned snapshot of the pinned Git objects. An explicit
``--utilities`` source need only contain the commit; its working tree is not run.
"""

from __future__ import annotations

import argparse

from common import ROOT, journal_utilities, run


def main(argv: list[str], arm: str) -> int:
    parser = argparse.ArgumentParser(prog=f"./run.sh {arm}", description=__doc__)
    parser.add_argument("--utilities", help="local Git object source containing the Journal-Utilities pin")
    args = parser.parse_args(argv)

    with journal_utilities(args.utilities) as tree:
        scripts = tree / "scripts"
        manifest = tree / "data" / "output" / "channel_videos.json"
        python = "python3"

        run("derived indexes", [python, "-B", str(scripts / "generate_journal_indexes.py"), "--journal", ".", "--check"])
        if arm == "fast":
            return 0

        run(
            "split transcript artifacts",
            [python, "-B", str(scripts / "repair_split_transcripts.py"), "--journal", ".", "--utilities", str(tree), "--check"],
        )
        run(
            "journal integrity",
            [python, "-B", str(scripts / "validate_journal.py"), "--journal", ".", "--manifest", str(manifest)],
        )
        run(
            "manifest reconciliation",
            [python, "-B", str(ROOT / "scripts" / "gate" / "arm_manifest.py"), "--manifest", str(manifest)],
        )
    return 0
