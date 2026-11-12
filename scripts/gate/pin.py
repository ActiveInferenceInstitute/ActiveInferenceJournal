"""Print or validate the Journal-Utilities pin.

The workflows read the checkout ref from here, so the pin lives in exactly one
file: ``.github/journal-utilities-pin.json``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys

from common import JU_PIN, read_pin

HEX40 = re.compile(r"^[0-9a-f]{40}$")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", action="store_true", help="print the revision only")
    parser.add_argument(
        "--role",
        choices=("gate", "ingest"),
        default="gate",
        help="which pinned revision to print (default: gate)",
    )
    args = parser.parse_args(argv)

    pin = read_pin(JU_PIN)
    entry = pin if args.role == "gate" else pin.get("ingest", {})
    revision = str(entry.get("revision", ""))
    if not HEX40.match(revision):
        raise SystemExit(f"pin: {JU_PIN.name} has no 40-hex {args.role} revision")
    if args.revision:
        print(revision)
        return 0
    print(json.dumps(pin, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
