"""The pinned Journal-Utilities gates shared by the ``fast`` and ``full`` arms.

``fast`` is the derived-index check alone (seconds). ``full`` adds the split
transcript check, the read-only integrity gate, and manifest reconciliation.
Both run the pinned revision; an explicit ``--utilities`` tree is accepted only
when it sits on the pin (see ``common.journal_utilities``).
"""

from __future__ import annotations

import argparse

from common import ROOT, journal_utilities, run


def main(argv: list[str], arm: str) -> int:
    parser = argparse.ArgumentParser(prog=f"./run.sh {arm}", description=__doc__)
    parser.add_argument("--utilities", help="existing Journal-Utilities tree at the pin")
    args = parser.parse_args(argv)

    tree = journal_utilities(args.utilities)
    scripts = tree / "scripts"
    manifest = tree / "data" / "output" / "channel_videos.json"
    python = "python3"

    run("derived indexes", [python, str(scripts / "generate_journal_indexes.py"), "--journal", ".", "--check"])
    if arm == "fast":
        return 0

    run(
        "split transcript artifacts",
        [python, str(scripts / "repair_split_transcripts.py"), "--journal", ".", "--utilities", str(tree), "--check"],
    )
    run(
        "journal integrity",
        [python, str(scripts / "validate_journal.py"), "--journal", ".", "--manifest", str(manifest)],
    )
    run(
        "manifest reconciliation",
        [python, str(ROOT / "scripts" / "gate" / "arm_manifest.py"), "--manifest", str(manifest)],
    )
    return 0
