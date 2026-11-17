"""Offline dispatcher regressions using real subprocess exits and real offline arms.

The process fixtures exercise aggregation, not GNN or producer qualification.
Run explicitly with the existing stdlib Python; no downloads or installations.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parent
ROOT = SOURCE.parents[1]
ORDER = ["lint", "docs", "identity", "full", "gnn"]

PROCESS_ARM = '''import subprocess
import sys
from pathlib import Path

def run(argv):
    root = Path(__file__).resolve().parents[2]
    return subprocess.run(
        [sys.executable, "-B", str(root / "arm_process.py"),
         Path(__file__).stem.removeprefix("arm_"), *argv], cwd=root,
    ).returncode
'''
PROCESS_BODY = '''import argparse
import json
import os
import sys
from pathlib import Path

arm, options = sys.argv[1], sys.argv[2:]
parser = argparse.ArgumentParser(prog=arm, allow_abbrev=False)
if arm == "full":
    parser.add_argument("--utilities")
elif arm == "gnn":
    parser.add_argument("--cold", action="store_true")
parser.parse_args(options)
with Path("executed.jsonl").open("a", encoding="utf-8") as stream:
    stream.write(json.dumps({"arm": arm, "options": options}) + "\\n")
sys.exit(json.loads(os.environ["ARM_FAILURES"]).get(arm, 0))
'''
AUDITED_DISPATCH = '''import runpy
import sys
from pathlib import Path

def deny_acquisition(event, args):
    if event.startswith("socket."):
        raise RuntimeError("FORBIDDEN_ACQUISITION")
    if event == "subprocess.Popen":
        command = args[1]
        if isinstance(command, (list, tuple)):
            git_fetch = Path(command[0]).name == "git" and any(
                word in command for word in ("fetch", "clone", "pull", "push")
            )
            install = "-m" in command and any(word in command for word in ("pip", "venv"))
            if git_fetch or install:
                raise RuntimeError("FORBIDDEN_ACQUISITION")
sys.addaudithook(deny_acquisition)
cli = Path(__file__).resolve().parent / "scripts/gate/cli.py"
sys.argv = [str(cli), *sys.argv[1:]]
runpy.run_path(str(cli), run_name="__main__")
'''


class AggregateProcessTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="aij-cli-selftest-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.gate = self.root / "scripts" / "gate"
        self.gate.mkdir(parents=True)
        for source in SOURCE.glob("*.py"):
            shutil.copy2(source, self.gate / source.name)
        self.driver = self.root / "dispatch.py"
        self.driver.write_text(AUDITED_DISPATCH, encoding="utf-8")
        self.env = {
            key: value for key, value in os.environ.items()
            if not key.startswith(("GIT_", "GATE_", "PYTHON"))
        }
        self.env.update(
            GIT_CONFIG_GLOBAL=os.devnull,
            GIT_CONFIG_NOSYSTEM="1",
            GIT_ALLOW_PROTOCOL="",
            GIT_TERMINAL_PROMPT="0",
            GATE_CACHE=str(self.root / "cache"),
        )

    def dispatch(self, options=(), failures=None):
        env = {**self.env, "ARM_FAILURES": json.dumps(failures or {})}
        return subprocess.run(
            [sys.executable, "-I", "-B", str(self.driver), "all", *options],
            cwd=self.root, env=env, capture_output=True, text=True, timeout=30,
        )

    def process_arms(self):
        (self.root / "arm_process.py").write_text(PROCESS_BODY, encoding="utf-8")
        for arm in ORDER:
            (self.gate / f"arm_{arm}.py").write_text(PROCESS_ARM, encoding="utf-8")

    def executed(self):
        trace = self.root / "executed.jsonl"
        return [json.loads(line) for line in trace.read_text().splitlines()] if trace.exists() else []

    def test_each_nonzero_process_status_stops_the_aggregate(self):
        self.process_arms()
        for position, arm in enumerate(ORDER):
            with self.subTest(arm=arm):
                (self.root / "executed.jsonl").unlink(missing_ok=True)
                code = 11 + position
                result = self.dispatch(failures={arm: code, **{later: 41 for later in ORDER[position + 1:]}})
                self.assertEqual(result.returncode, code, result.stdout + result.stderr)
                self.assertEqual([event["arm"] for event in self.executed()], ORDER[:position + 1])

    def test_all_success_and_options_reach_only_their_owners(self):
        self.process_arms()
        path = str(self.root / "source with spaces")
        result = self.dispatch(["--utilities", path, "--cold"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.executed(), [
            {"arm": arm, "options": ["--utilities", path] if arm == "full" else ["--cold"] if arm == "gnn" else []}
            for arm in ORDER
        ])

    def test_all_success_without_options(self):
        self.process_arms()
        result = self.dispatch()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.executed(), [{"arm": arm, "options": []} for arm in ORDER])

    def test_invalid_options_have_no_arm_side_effects(self):
        self.process_arms()
        cases = [
            ["--unknown"], ["--write"], ["--check"], ["--verify-only"],
            ["--utilities"], ["--utilities", ""], ["--utilities", "   "],
            ["--util", "somewhere"], ["--cold", "unexpected"],
        ]
        for options in cases:
            with self.subTest(options=options):
                result = self.dispatch(options)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertEqual(self.executed(), [])

    def test_help_does_not_run_an_arm(self):
        self.process_arms()
        result = self.dispatch(["--help"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.executed(), [])

    def offline_corpus(self):
        github = self.root / ".github"
        github.mkdir()
        for name in ("journal-utilities-pin.json", "gnn-pin.json"):
            shutil.copy2(ROOT / ".github" / name, github / name)
        workflows = self.root / "docs" / "workflows"
        workflows.mkdir(parents=True)
        schema = workflows / "record-identity.schema.json"
        shutil.copy2(ROOT / "docs" / "workflows" / schema.name, schema)
        digest = hashlib.sha256(schema.read_bytes()).hexdigest()
        (workflows / "publishing.md").write_text(f"{schema.name}  {digest}\n", encoding="utf-8")
        (self.root / "docs" / "documentation-index.md").write_text(
            "[Publishing](workflows/publishing.md)\n", encoding="utf-8",
        )
        generated = self.root / "docs" / "_generated"
        generated.mkdir()
        (generated / "gate-timings.md").write_text(
            "\n".join(f"| `{arm}` | fixture |" for arm in ["lint", "docs", "identity", "fast", "full", "gnn"]),
            encoding="utf-8",
        )
        relative = "data/video/source/Series/Item"
        record = self.root / relative
        record.mkdir(parents=True)
        metadata = {"item": "Item", "series": "Series", "parts": [{"video_id": "abcdefghijk"}]}
        (record / "metadata.json").write_text(json.dumps(metadata), encoding="utf-8")
        index_record = {
            "path": relative,
            "series": metadata["series"],
            "item": metadata["item"],
            "parts": [part["video_id"] for part in metadata["parts"]],
            "has_transcript": False,
        }
        (self.root / "INDEX.json").write_text(json.dumps({"items": [index_record]}), encoding="utf-8")
        return record / "metadata.json"

    def assert_offline_failure(self, expected):
        result = self.dispatch()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(expected, result.stdout + result.stderr)
        self.assertNotIn("FORBIDDEN_ACQUISITION", result.stdout + result.stderr)

    def test_real_malformed_json_stops_before_docs_or_providers(self):
        self.offline_corpus()
        (self.root / "INDEX.json").write_text("{", encoding="utf-8")
        self.assert_offline_failure("INDEX.json: invalid JSON")

    def test_real_unresolved_link_stops_before_identity_or_providers(self):
        self.offline_corpus()
        (self.root / "README.md").write_text("[missing](absent.md)\n", encoding="utf-8")
        self.assert_offline_failure("link `absent.md` does not resolve")

    def test_real_full_receives_explicit_source_and_refuses_before_gnn(self):
        self.offline_corpus()
        missing = self.root / "missing object source"
        result = self.dispatch(["--utilities", str(missing), "--cold"])
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("does not provide exact Git commit", result.stderr)
        self.assertIn(str(missing), result.stderr)
        self.assertNotIn("FORBIDDEN_ACQUISITION", result.stdout + result.stderr)
        self.assertIn("identity: ok", result.stdout)

    def test_real_record_identity_failure_stops_before_providers(self):
        metadata = self.offline_corpus()
        record = json.loads(metadata.read_text())
        record["item"] = "another-item"
        metadata.write_text(json.dumps(record), encoding="utf-8")
        self.assert_offline_failure("the item id must name its own directory")


if __name__ == "__main__":
    unittest.main()
