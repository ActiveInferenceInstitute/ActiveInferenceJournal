"""Exact-object snapshot regressions with real, temporary Git repositories.

Fixture scripts validate a small input record; they are object/execution probes,
not substitutes for qualification of the pinned Journal-Utilities corpus tools.
No network, dependency installation, user checkout mutation or provider runtime.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parent

HELPER = '''import json
from pathlib import Path

TREE = Path(__file__).resolve().parents[1]

def accepts(journal):
    expected = json.loads((TREE / "data" / "expected record.json").read_text())
    actual = json.loads((journal / "record.json").read_text())
    return actual == expected
'''
PROBE = '''#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path
from helper import TREE, accepts

parser = argparse.ArgumentParser()
parser.add_argument("--journal", type=Path, default=Path.cwd())
parser.add_argument("--check", action="store_true")
parser.add_argument("--utilities", type=Path)
parser.add_argument("--manifest", type=Path)
args = parser.parse_args()
if not accepts(args.journal):
    print("fixture record rejected", file=sys.stderr)
    sys.exit(23)
if args.utilities is not None and args.utilities.resolve() != TREE:
    sys.exit(24)
if args.manifest is not None:
    if args.manifest.resolve() != TREE / "data/output/channel_videos.json":
        sys.exit(25)
    json.loads(args.manifest.read_text())
with (args.journal / "executed.jsonl").open("a", encoding="utf-8") as stream:
    stream.write(json.dumps({"script": Path(__file__).name, "tree": str(TREE)}) + "\\n")
'''
DRIVER = '''import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

def deny_network(event, args):
    if event.startswith("socket."):
        raise RuntimeError("FORBIDDEN_NETWORK_ATTEMPT")
    if event == "subprocess.Popen":
        command = args[1]
        if isinstance(command, (list, tuple)) and Path(command[0]).name == "git":
            if any(word in command for word in ("fetch", "clone", "pull", "push")):
                raise RuntimeError("FORBIDDEN_NETWORK_ATTEMPT")
sys.addaudithook(deny_network)

import common
import utilities

mode, source = sys.argv[1:3]
source = None if source == "AUTO" else source

def inventory(root):
    result = {}
    for path in sorted(root.rglob("*")):
        name = path.relative_to(root).as_posix()
        if path.is_symlink():
            result[name] = ["link", os.readlink(path)]
        elif path.is_file():
            result[name] = ["file", path.read_bytes().hex(), bool(path.stat().st_mode & 0o111)]
    return result

try:
    if mode in {"fast", "full"}:
        sys.exit(utilities.main([] if source is None else ["--utilities", source], mode))
    if mode == "overlap":
        with common.journal_utilities(source) as first:
            (first / "scripts/helper.py").write_text("raise RuntimeError('dirty snapshot')\\n")
            with common.journal_utilities(source) as second:
                result = subprocess.run([sys.executable, "-B", str(second / "scripts/validate_journal.py")])
                distinct = first != second and first.exists() and second.exists()
            second_removed = not second.exists()
        print("SNAPSHOT_RESULT=" + json.dumps({"distinct": distinct, "cleaned": second_removed and not first.exists()}))
        sys.exit(result.returncode)
    with common.journal_utilities(source) as tree:
        contents = inventory(tree)
        if mode == "raise":
            raise RuntimeError("consumer failure")
        result = subprocess.run([sys.executable, "-B", str(tree / "scripts/validate_journal.py")])
    print("SNAPSHOT_RESULT=" + json.dumps({"tree": str(tree), "cleaned": not tree.exists(), "contents": contents}))
    sys.exit(result.returncode)
except common.GateError as exc:
    print(str(exc), file=sys.stderr)
    sys.exit(exc.code)
except RuntimeError as exc:
    if str(exc) != "consumer failure":
        raise
    print("SNAPSHOT_RESULT=" + json.dumps({"cleaned": not tree.exists()}))
    sys.exit(55)
'''


def inventory(root: Path, *, include_git: bool = True):
    result = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if not include_git and ".git" in relative.parts:
            continue
        if path.is_symlink():
            result[relative.as_posix()] = ["link", os.readlink(path)]
        elif path.is_file():
            result[relative.as_posix()] = ["file", path.read_bytes().hex(), bool(path.stat().st_mode & 0o111)]
    return result


class ExactSnapshotTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="aij-object-selftest-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.consumer = self.root / "consumer"
        self.gate = self.consumer / "scripts/gate"
        self.gate.mkdir(parents=True)
        for name in ("common.py", "utilities.py", "arm_manifest.py"):
            shutil.copy2(SOURCE / name, self.gate / name)
        (self.gate / "probe_driver.py").write_text(DRIVER, encoding="utf-8")
        self.cache = self.root / "cache"
        self.cache.mkdir()
        self.env = {
            key: value for key, value in os.environ.items()
            if not key.startswith(("GIT_", "GATE_", "PYTHON"))
        }
        self.env.update(
            GIT_CONFIG_GLOBAL=os.devnull,
            GIT_CONFIG_NOSYSTEM="1",
            GIT_TERMINAL_PROMPT="0",
            GIT_ALLOW_PROTOCOL="",
            GATE_CACHE=str(self.cache),
        )
        self.producer = self.root / "producer with spaces"
        scripts = self.producer / "scripts"
        scripts.mkdir(parents=True)
        (scripts / "helper.py").write_text(HELPER, encoding="utf-8")
        for name in ("validate_journal.py", "generate_journal_indexes.py", "repair_split_transcripts.py"):
            (scripts / name).write_text(PROBE, encoding="utf-8")
            (scripts / name).chmod(0o755)
        (scripts / "helper-link.py").symlink_to("helper.py")
        data = self.producer / "data"
        (data / "output").mkdir(parents=True)
        (data / "expected record.json").write_text('{"record": "committed"}', encoding="utf-8")
        (data / "format-é.txt").write_text("$Format:%H$\n", encoding="utf-8")
        (data / "output/channel_videos.json").write_text(
            json.dumps({"enumerated_at": "2000-01-01T00:00:00+00:00", "videos": []}), encoding="utf-8",
        )
        (self.producer / ".gitattributes").write_text(
            'scripts/helper.py export-ignore\n"data/format-é.txt" export-subst\n', encoding="utf-8",
        )
        self.git("init", "--quiet")
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", "owned fixture")
        self.revision = self.git("rev-parse", "HEAD").stdout.decode().strip()
        self.committed = inventory(self.producer, include_git=False)
        self.pin = self.consumer / ".github/journal-utilities-pin.json"
        self.pin.parent.mkdir()
        self.write_pin(self.revision)
        (self.consumer / "record.json").write_text('{"record": "committed"}', encoding="utf-8")
        (self.consumer / "INDEX.json").write_text('{"items": []}', encoding="utf-8")

    def git(self, *args, input=None):
        return subprocess.run(
            ["git", "-c", "core.fsmonitor=false", "-c", f"core.hooksPath={os.devnull}",
             "-c", "commit.gpgsign=false", "-c", "user.name=Gate fixture",
             "-c", "user.email=gate-fixture@example.invalid", *args],
            cwd=self.producer, env=self.env, input=input, capture_output=True, check=True,
        )

    def write_pin(self, revision):
        self.pin.write_text(json.dumps({
            "repository": "ActiveInferenceInstitute/Journal_Utilities", "revision": revision,
        }), encoding="utf-8")

    def invoke(self, mode="snapshot", *, source=None, auto=False, env=None):
        return subprocess.run(
            [sys.executable, "-I", "-B", str(self.gate / "probe_driver.py"), mode,
             "AUTO" if auto else str(source or self.producer)],
            cwd=self.consumer, env={**self.env, **(env or {})},
            capture_output=True, text=True, timeout=30,
        )

    def result(self, completed, code=0):
        self.assertEqual(completed.returncode, code, completed.stdout + completed.stderr)
        self.assertNotIn("FORBIDDEN_NETWORK_ATTEMPT", completed.stdout + completed.stderr)
        lines = [line for line in completed.stdout.splitlines() if line.startswith("SNAPSHOT_RESULT=")]
        self.assertEqual(len(lines), 1, completed.stdout)
        return json.loads(lines[0].partition("=")[2])

    def assert_no_snapshots(self):
        self.assertEqual(list(self.cache.glob("ju-snapshot-*")), [])

    def test_clean_pin_materializes_every_blob_link_and_mode_then_cleans(self):
        before = inventory(self.producer)
        result = self.result(self.invoke())
        self.assertEqual(result["contents"], self.committed)
        self.assertNotEqual(Path(result["tree"]), self.producer)
        self.assertTrue(result["cleaned"])
        self.assertEqual(inventory(self.producer), before)
        self.assert_no_snapshots()

    def test_dirty_validator_cannot_turn_a_rejected_record_green(self):
        (self.consumer / "record.json").write_text('{"record": "invalid"}')
        (self.producer / "scripts/validate_journal.py").write_text("raise SystemExit(0)\n")
        (self.producer / "untracked.txt").write_text("preserve this dirty tree")
        before = inventory(self.producer)
        result = self.result(self.invoke(), 23)
        self.assertEqual(result["contents"], self.committed)
        self.assertEqual(inventory(self.producer), before)
        self.assertFalse((self.consumer / "executed.jsonl").exists())

    def test_staged_imported_helper_cannot_bypass_record_validation(self):
        (self.consumer / "record.json").write_text('{"record": "invalid"}')
        (self.producer / "scripts/helper.py").write_text(
            "from pathlib import Path\nTREE = Path(__file__).resolve().parents[1]\ndef accepts(journal): return True\n",
        )
        self.git("add", "scripts/helper.py")
        (self.producer / "scripts/untracked.py").write_text("raise RuntimeError('untracked')\n")
        before = inventory(self.producer)
        result = self.result(self.invoke(), 23)
        self.assertEqual(result["contents"], self.committed)
        self.assertEqual(inventory(self.producer), before)

    def test_source_head_may_differ_but_pin_and_dirty_data_are_preserved(self):
        (self.producer / "data/expected record.json").write_text('{"record": "later"}')
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", "later source head")
        (self.producer / "scripts/helper.py").write_text("raise RuntimeError('dirty')\n")
        before = inventory(self.producer)
        result = self.result(self.invoke())
        self.assertEqual(result["contents"], self.committed)
        self.assertEqual(inventory(self.producer), before)

    def test_git_replacement_objects_do_not_override_pinned_blobs(self):
        old = self.git("rev-parse", f"{self.revision}:scripts/helper.py").stdout.decode().strip()
        new = self.git("hash-object", "-w", "--stdin", input=b"raise RuntimeError('replacement')\n").stdout.decode().strip()
        self.git("replace", old, new)
        before = inventory(self.producer)
        result = self.result(self.invoke())
        self.assertEqual(result["contents"], self.committed)
        self.assertEqual(inventory(self.producer), before)

    def test_linked_worktree_is_an_object_source_not_executed_content(self):
        worktree = self.root / "linked source"
        self.git("worktree", "add", "--quiet", "--detach", str(worktree), self.revision)
        (worktree / "scripts/helper.py").write_text("raise RuntimeError('worktree dirty')\n")
        before = inventory(worktree)
        source_before = inventory(self.producer)
        result = self.result(self.invoke(source=worktree))
        self.assertEqual(result["contents"], self.committed)
        self.assertEqual(inventory(worktree), before)
        self.assertEqual(inventory(self.producer), source_before)

    def test_mutable_stamped_export_is_refused_without_touching_it(self):
        exported = self.root / "export"
        shutil.copytree(self.producer, exported, symlinks=True, ignore=shutil.ignore_patterns(".git"))
        (exported / ".gate-pin").write_text(self.revision + "\n")
        (exported / "scripts/helper.py").write_text("raise RuntimeError('export dirty')\n")
        before = inventory(exported)
        completed = self.invoke(source=exported)
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("not an object source", completed.stderr)
        self.assertNotIn("FORBIDDEN_NETWORK_ATTEMPT", completed.stderr)
        self.assertEqual(inventory(exported), before)
        self.assert_no_snapshots()

    def test_dirty_stamped_git_cache_supplies_objects_only(self):
        cached = self.cache / f"ju-{self.revision[:12]}"
        self.producer.rename(cached)
        self.producer = cached
        (cached / ".gate-pin").write_text(self.revision + "\n")
        (cached / "scripts/validate_journal.py").write_text("raise SystemExit(42)\n")
        (cached / "data/expected record.json").write_text('{"record": "cache dirty"}')
        before = inventory(cached)
        result = self.result(self.invoke(auto=True))
        self.assertEqual(result["contents"], self.committed)
        self.assertEqual(inventory(cached), before)
        self.assert_no_snapshots()

    def test_stamped_export_cache_is_preserved_while_local_objects_are_used(self):
        exported = self.cache / f"ju-{self.revision[:12]}"
        exported.mkdir()
        (exported / ".gate-pin").write_text(self.revision + "\n")
        (exported / "dirty.txt").write_text("do not overwrite or delete")
        before = inventory(self.cache)
        result = self.result(self.invoke(auto=True, env={"GATE_JU_CLONE": str(self.producer)}))
        self.assertEqual(result["contents"], self.committed)
        self.assertEqual(inventory(self.cache), before)

    def test_missing_exact_commit_fails_without_network_or_source_changes(self):
        self.write_pin("f" * 40)
        before = inventory(self.producer)
        completed = self.invoke()
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("does not provide exact Git commit", completed.stderr)
        self.assertNotIn("FORBIDDEN_NETWORK_ATTEMPT", completed.stderr)
        self.assertEqual(inventory(self.producer), before)
        self.assert_no_snapshots()

    def test_escaping_symlink_and_gitlink_fail_instead_of_partial_execution(self):
        outside = self.root / "outside.txt"
        outside.write_text("untouched")
        (self.producer / "escape").symlink_to(outside)
        self.git("add", "escape")
        self.git("commit", "--quiet", "-m", "escaping link")
        self.write_pin(self.git("rev-parse", "HEAD").stdout.decode().strip())
        before = inventory(self.producer)
        completed = self.invoke()
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("symlink escapes", completed.stderr)
        self.assertEqual(outside.read_text(), "untouched")
        self.assertEqual(inventory(self.producer), before)
        self.assert_no_snapshots()
        self.git("update-index", "--add", "--cacheinfo", f"160000,{self.revision},submodule")
        self.git("commit", "--quiet", "-m", "gitlink")
        self.write_pin(self.git("rev-parse", "HEAD").stdout.decode().strip())
        completed = self.invoke()
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("cannot bind committed entry 'submodule'", completed.stderr)
        self.assert_no_snapshots()

    def test_overlapping_contexts_do_not_share_mutable_execution_trees(self):
        result = self.result(self.invoke("overlap"))
        self.assertTrue(result["distinct"])
        self.assertTrue(result["cleaned"])
        self.assert_no_snapshots()

    def test_consumer_exception_removes_only_its_snapshot(self):
        before = inventory(self.producer)
        result = self.result(self.invoke("raise"), 55)
        self.assertTrue(result["cleaned"])
        self.assertEqual(inventory(self.producer), before)
        self.assert_no_snapshots()

    def test_fast_and_full_keep_the_snapshot_through_all_real_child_processes(self):
        before = inventory(self.producer)
        for mode, scripts in (
            ("fast", ["generate_journal_indexes.py"]),
            ("full", ["generate_journal_indexes.py", "repair_split_transcripts.py", "validate_journal.py"]),
        ):
            with self.subTest(mode=mode):
                trace = self.consumer / "executed.jsonl"
                trace.unlink(missing_ok=True)
                completed = self.invoke(mode)
                self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
                self.assertNotIn("FORBIDDEN_NETWORK_ATTEMPT", completed.stderr)
                events = [json.loads(line) for line in trace.read_text().splitlines()]
                self.assertEqual([event["script"] for event in events], scripts)
                self.assertEqual(len({event["tree"] for event in events}), 1)
                self.assertFalse(Path(events[0]["tree"]).exists())
                if mode == "full":
                    self.assertIn("manifest: reconciliation complete", completed.stdout)
                self.assertEqual(inventory(self.producer), before)
                self.assert_no_snapshots()

    def test_failed_producer_process_cleans_snapshot_and_preserves_source(self):
        (self.consumer / "record.json").write_text('{"record": "invalid"}')
        before = inventory(self.producer)
        completed = self.invoke("full")
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("fixture record rejected", completed.stderr)
        self.assertIn("derived indexes failed (exit 23)", completed.stderr)
        self.assertFalse((self.consumer / "executed.jsonl").exists())
        self.assertEqual(inventory(self.producer), before)
        self.assert_no_snapshots()


if __name__ == "__main__":
    unittest.main()
