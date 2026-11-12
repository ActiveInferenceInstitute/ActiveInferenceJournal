"""Arm: docs - documentation integrity.

Checks that what the docs promise still exists: relative links resolve with the
exact case GitHub serves, in-page anchors exist, every long-lived doc under
``docs/`` is reachable from the flat index, the generated timings table covers
every arm, and documented pin prefixes match the pin files.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from arm_bench import MEASURED
from common import GNN_PIN, JU_PIN, ROOT, log, read_pin, tracked_markdown

FENCE = re.compile(r"^ {0,3}(?:```|~~~)")
COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
LINK = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\s*\)")
REFDEF = re.compile(r"^ {0,3}\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
HEX_TOKEN = re.compile(r"\b[0-9a-f]{8,40}\b")

DOCS = ROOT / "docs"
INDEX = DOCS / "documentation-index.md"
TIMINGS = DOCS / "_generated" / "gate-timings.md"
PIN_DOCS = [
    DOCS / "OPERATIONS.md",
    DOCS / "documentation-index.md",
    ROOT / ".github" / "GNN.md",
    ROOT / ".github" / "README.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "AGENTS.md",
]

failures: list[str] = []
_anchors: dict[Path, set[str]] = {}


def fail(message: str) -> None:
    failures.append(message)


def strip_noise(text: str) -> str:
    """Drop HTML comments, fenced blocks and inline code, keeping line numbers."""
    text = COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    kept: list[str] = []
    fenced = False
    for line in text.splitlines():
        if FENCE.match(line):
            fenced = not fenced
            kept.append("")
            continue
        kept.append("" if fenced else INLINE_CODE.sub("``", line))
    return "\n".join(kept)


def slugify(title: str) -> str:
    title = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", title)
    title = title.replace("`", "").strip().lower()
    title = re.sub(r"[^\w\s-]", "", title, flags=re.UNICODE)
    return re.sub(r"\s+", "-", title)


def anchors(path: Path) -> set[str]:
    if path not in _anchors:
        found: set[str] = set()
        seen: dict[str, int] = {}
        for line in strip_noise(path.read_text(encoding="utf-8")).splitlines():
            match = HEADING.match(line)
            if not match:
                continue
            base = slugify(match.group(2))
            count = seen.get(base, 0)
            seen[base] = count + 1
            found.add(base if count == 0 else f"{base}-{count}")
        _anchors[path] = found
    return _anchors[path]


def exists_exact(path: Path) -> bool:
    if not path.parent.exists():
        return False
    try:
        return path.name in set(os.listdir(path.parent))
    except OSError:
        return False


def links_in(text: str) -> list[tuple[int, str]]:
    found: list[tuple[int, str]] = []
    for number, line in enumerate(text.splitlines(), 1):
        for match in LINK.finditer(line):
            target = match.group(1).strip("<>").strip()
            if target:
                found.append((number, target))
    for match in REFDEF.finditer(text):
        line = text[: match.start()].count("\n") + 1
        found.append((line, match.group(1).strip("<>")))
    return found


def check_links() -> None:
    for path in tracked_markdown():
        if not path.exists():
            continue
        rel = path.relative_to(ROOT)
        for number, target in links_in(strip_noise(path.read_text(encoding="utf-8"))):
            if target.startswith("#"):
                anchor = unquote(target[1:])
                if anchor and anchor not in anchors(path):
                    fail(f"{rel}:{number}: missing anchor `#{anchor}` in this file")
                continue
            if SCHEME.match(target) or target.startswith(("/", "//")):
                continue
            resolved, _, anchor = target.partition("#")
            resolved = unquote(resolved)
            if not resolved:
                continue
            destination = (path.parent / resolved).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                fail(f"{rel}:{number}: link `{target}` escapes the repository")
                continue
            if not exists_exact(destination):
                fail(f"{rel}:{number}: link `{target}` does not resolve")
                continue
            if anchor and destination.suffix == ".md":
                if unquote(anchor) not in anchors(destination):
                    fail(f"{rel}:{number}: link `{target}` names a missing anchor")


def check_docs_index() -> None:
    if not INDEX.exists():
        fail("docs/documentation-index.md is missing")
        return
    indexed = {
        (INDEX.parent / unquote(target.partition("#")[0])).resolve()
        for _, target in links_in(strip_noise(INDEX.read_text(encoding="utf-8")))
        if not SCHEME.match(target) and not target.startswith(("#", "/"))
    }
    for path in sorted(DOCS.rglob("*.md")):
        relative = path.relative_to(DOCS)
        if relative.as_posix() in {"README.md", "documentation-index.md"}:
            continue
        if relative.parts[0] == "_generated":
            continue
        if path.resolve() not in indexed:
            fail(f"docs/{relative} is not reachable from docs/documentation-index.md")


def check_timings() -> None:
    if not TIMINGS.exists():
        fail("docs/_generated/gate-timings.md is missing (run ./run.sh bench --write)")
        return
    table = {
        match.group(1)
        for match in re.finditer(r"^\|\s*`([a-z]+)`\s*\|", TIMINGS.read_text(encoding="utf-8"), re.M)
    }
    for arm in MEASURED:
        if arm not in table:
            fail(f"docs/_generated/gate-timings.md does not report arm `{arm}`")
    for arm in sorted(table - set(MEASURED)):
        fail(f"docs/_generated/gate-timings.md reports unknown arm `{arm}`")


def check_documented_pins() -> None:
    revisions = [read_pin(JU_PIN)["revision"], read_pin(GNN_PIN)["revision"]]
    for path in PIN_DOCS:
        if not path.exists():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for token in HEX_TOKEN.findall(line):
                if any(revision.startswith(token) for revision in revisions):
                    continue
                fail(
                    f"{path.relative_to(ROOT)}:{number}: `{token}` matches no pin file "
                    f"(pins: {', '.join(r[:8] for r in revisions)})"
                )


def run(argv: list[str]) -> int:
    if argv:
        raise SystemExit(f"gate: docs takes no arguments, got {argv}")
    check_links()
    check_docs_index()
    check_timings()
    check_documented_pins()
    if failures:
        for message in failures:
            print(f"docs: FAIL {message}", file=sys.stderr)
        return 1
    log(f"docs: ok ({len(tracked_markdown())} Markdown files)")
    return 0
