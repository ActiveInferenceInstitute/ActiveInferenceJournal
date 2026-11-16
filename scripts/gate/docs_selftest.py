"""Offline Markdown regressions using real documents and the owning checker.

run() is called by the docs arm. Temporary roots replace only checker configuration;
link resolution, heading extraction and docs-index coverage use production code.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import arm_docs


class DocsTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.docs = self.root / "docs"
        self.docs.mkdir()
        self.index = self.docs / "documentation-index.md"
        configured = {
            "ROOT": self.root,
            "DOCS": self.docs,
            "INDEX": self.index,
            "failures": [],
            "_anchors": {},
        }
        original = {name: getattr(arm_docs, name) for name in configured}
        self.addCleanup(self.restore_configuration, original)
        for name, value in configured.items():
            setattr(arm_docs, name, value)

    @staticmethod
    def restore_configuration(original: dict) -> None:
        for name, value in original.items():
            setattr(arm_docs, name, value)

    def document(self, relative: str, text: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_garden_heading_and_repeated_inline_words_resolve(self) -> None:
        architecture = self.document(
            "docs/ARCHITECTURE.md",
            "# Architecture\n\n"
            "### `discord_bot.py` — the Iris Discord bot\n"
            "### `discord_bot.py` — the Iris Discord bot\n"
            "### discord_bot.py — the Iris Discord bot\n"
            "[First](#discord_botpy--the-iris-discord-bot)\n"
            "[Second](#discord_botpy--the-iris-discord-bot-1)\n"
            "[Third](#discord_botpy--the-iris-discord-bot-2)\n",
        )
        readme = self.document(
            "README.md",
            "[Discord](docs/ARCHITECTURE.md#discord_botpy--the-iris-discord-bot)\n"
            "[Repeated](docs/ARCHITECTURE.md#discord_botpy--the-iris-discord-bot-2)\n",
        )
        arm_docs.check_links([readme, architecture])
        self.assertEqual(arm_docs.failures, [])
        self.assertEqual(
            arm_docs.anchors(architecture),
            {
                "architecture",
                "discord_botpy--the-iris-discord-bot",
                "discord_botpy--the-iris-discord-bot-1",
                "discord_botpy--the-iris-discord-bot-2",
            },
        )

    def test_different_code_headings_do_not_share_duplicate_numbers(self) -> None:
        path = self.document(
            "README.md",
            "## `alpha.py`\n## `beta.py`\n## alpha.py\n"
            "[Alpha](#alphapy)\n[Beta](#betapy)\n[Again](#alphapy-1)\n",
        )
        arm_docs.check_links([path])
        self.assertEqual(arm_docs.failures, [])
        self.assertEqual(arm_docs.anchors(path), {"alphapy", "betapy", "alphapy-1"})

    def test_links_inside_inline_code_are_not_checked(self) -> None:
        path = self.document(
            "README.md",
            "# Real\n"
            "`[missing](absent.md)`\n"
            "`![missing image](absent.png)`\n"
            "`[reference]: absent.md`\n"
            "[Real](#real)\n",
        )
        arm_docs.check_links([path])
        self.assertEqual(arm_docs.failures, [])

    def test_code_links_do_not_make_a_doc_reachable(self) -> None:
        self.document("docs/hidden.md", "# Hidden\n")
        self.index.write_text(
            "# Index\n`[Hidden](hidden.md)`\n`[hidden]: hidden.md`\n",
            encoding="utf-8",
        )
        arm_docs.check_docs_index()
        self.assertEqual(
            arm_docs.failures,
            ["docs/hidden.md is not reachable from docs/documentation-index.md"],
        )
        arm_docs.failures.clear()
        self.index.write_text("# Index\n[Hidden](hidden.md)\n", encoding="utf-8")
        arm_docs.check_docs_index()
        self.assertEqual(arm_docs.failures, [])

    def test_fences_and_comments_do_not_claim_headings_or_links(self) -> None:
        path = self.document(
            "README.md",
            "# Visible\n"
            "<!--\n## `same`\n[Missing](comment.md)\n-->\n"
            "```md\n## `same`\n[Missing](fenced.md)\n```\n"
            "~~~md\n## `same`\n[Missing](tilde.md)\n~~~\n"
            "## `same`\n[Visible](#same)\n",
        )
        arm_docs.check_links([path])
        self.assertEqual(arm_docs.failures, [])
        self.assertEqual(arm_docs.anchors(path), {"visible", "same"})

    def test_missing_anchor_and_real_link_still_fail_at_original_lines(self) -> None:
        path = self.document(
            "README.md",
            "# `alpha.py`\n"
            "<!-- hidden\ncomment -->\n"
            "```md\n[Ignored](nope.md)\n```\n"
            "`[Ignored](also-nope.md)`\n"
            "[Wrong](#betapy)\n"
            "[Missing](real-missing.md)\n",
        )
        arm_docs.check_links([path])
        self.assertEqual(
            arm_docs.failures,
            [
                "README.md:8: missing anchor `#betapy` in this file",
                "README.md:9: link `real-missing.md` does not resolve",
            ],
        )

    def test_docs_index_ignores_fenced_and_commented_links(self) -> None:
        self.document("docs/hidden.md", "# Hidden\n")
        self.index.write_text(
            "# Index\n<!-- [Hidden](hidden.md) -->\n"
            "```md\n[Hidden](hidden.md)\n```\n",
            encoding="utf-8",
        )
        arm_docs.check_docs_index()
        self.assertEqual(
            arm_docs.failures,
            ["docs/hidden.md is not reachable from docs/documentation-index.md"],
        )


    def test_literal_code_links_retain_words_without_becoming_links(self) -> None:
        path = self.document(
            "README.md",
            "## `[label](missing.md)`\n"
            "## ``[label](other.md)``\n"
            "## [Visible `label`](README.md)\n"
            "[First](#labelmissingmd)\n"
            "[Second](#labelothermd)\n"
            "[Third](#visible-label)\n"
            "``[Ignored](absent.md) with a `literal` tick``\n",
        )
        arm_docs.check_links([path])
        self.assertEqual(arm_docs.failures, [])
        self.assertEqual(
            arm_docs.anchors(path),
            {"labelmissingmd", "labelothermd", "visible-label"},
        )


def run() -> list[str]:
    result = unittest.TestResult()
    unittest.defaultTestLoader.loadTestsFromTestCase(DocsTests).run(result)
    return [f"selftest: {test.id()}\n{detail}" for test, detail in result.errors + result.failures]


if __name__ == "__main__":
    import sys

    problems = run()
    for problem in problems:
        print(problem, file=sys.stderr)
    sys.exit(1 if problems else 0)
