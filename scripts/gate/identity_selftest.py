"""Offline identity regressions over real temporary corpora and artifact copies.

The identity arm calls run(); direct execution uses the same cases. Fixtures
exercise the canonical schema and checker without reading or changing the corpus.
"""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

import identity

MODULE = "sample_module.py"
BODY = "VALUE = 1\n"
NOISE = (
    "A prose line that quotes  deadbeefdeadbeefdeadbeefdeadbeefdeadbeef  "
    "with two spaces and is not a digest record.\n"
)


class CorpusIdentityTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.root = self.base / "corpus"
        self.root.mkdir()
        self.spec = identity.load_schema(
            Path(__file__).resolve().parents[2] / "docs/workflows/record-identity.schema.json"
        )
        self.relative = "data/video/source/Series/2024/Item"
        self.record_dir = self.root / self.relative
        self.record_dir.mkdir(parents=True)
        self.metadata = {
            "series": "Series",
            "item": "Item",
            "source": "youtube",
            "channel": "source",
            "category": None,
            "episode": None,
            "parts": [
                {"video_id": "abcdefghijk", "url": "https://www.youtube.com/watch?v=abcdefghijk", "title": "First"},
                {"video_id": "lmnopqrstuv", "url": "https://www.youtube.com/watch?v=lmnopqrstuv", "title": "Second"},
            ],
            "sessions": [
                {"session_name": "abcdefghijk_sess01", "video_id": "wxyz0123456"},
                {"session_name": "lmnopqrstuv_sess02"},
            ],
        }
        self.record = {
            "path": self.relative,
            "series": "Series",
            "item": "Item",
            "parts": ["abcdefghijk", "lmnopqrstuv"],
            "has_transcript": True,
        }
        self.items = [self.record]
        self.save_metadata()
        self.save_index()
        (self.record_dir / "transcript.txt").write_text("Derived transcript.\n", encoding="utf-8")

    def save_metadata(self) -> None:
        (self.record_dir / "metadata.json").write_text(json.dumps(self.metadata), encoding="utf-8")

    def save_index(self) -> None:
        (self.root / "INDEX.json").write_text(json.dumps({"items": self.items}), encoding="utf-8")

    def assert_rejected(self, fragment: str, spec: identity.Spec | None = None) -> dict[str, int]:
        problems, counts = identity.check_corpus(self.root, spec or self.spec)
        self.assertTrue(any(fragment in problem for problem in problems), problems)
        return counts

    def test_nested_series_and_standalone_session_upload(self) -> None:
        for directory, name in (
            ("captions", "A human title.srt"),
            ("translations", "not-a-video-id.fr.srt"),
        ):
            target = self.record_dir / directory / name
            target.parent.mkdir()
            target.write_text("1\n00:00:00,000 --> 00:00:01,000\nWords\n", encoding="utf-8")
        # Raw transcript validation belongs to Journal-Utilities, not this checker.
        (self.record_dir / "transcript.json").write_text("raw-layer sentinel", encoding="utf-8")
        self.assertEqual(
            identity.check_corpus(self.root, self.spec),
            ([], {"records": 1, "parts": 2, "duplicates": 0}),
        )

    def test_source_relative_duplicate(self) -> None:
        canonical = self.root / "data/video/source/Series/Canonical"
        canonical.mkdir()
        metadata = dict(self.metadata, item="Canonical")
        (canonical / "metadata.json").write_text(json.dumps(metadata), encoding="utf-8")
        self.metadata["duplicate_of"] = "Series/Canonical"
        self.record["duplicate_of"] = "Series/Canonical"
        self.items.append(dict(self.record, path=canonical.relative_to(self.root).as_posix(),
                               item="Canonical", has_transcript=False))
        del self.items[1]["duplicate_of"]
        self.save_metadata()
        self.save_index()
        self.assertEqual(
            identity.check_corpus(self.root, self.spec),
            ([], {"records": 2, "parts": 4, "duplicates": 1}),
        )

    def test_internal_symlinks_and_explicit_symlinked_root(self) -> None:
        stored_index = self.root / "stored-index.json"
        (self.root / "INDEX.json").rename(stored_index)
        (self.root / "INDEX.json").symlink_to(stored_index.name)
        stored_record = self.root / "stored-record"
        self.record_dir.rename(stored_record)
        self.record_dir.symlink_to(stored_record, target_is_directory=True)
        linked_root = self.base / "corpus-link"
        linked_root.symlink_to(self.root, target_is_directory=True)
        self.assertEqual(
            identity.check_corpus(linked_root, self.spec),
            ([], {"records": 1, "parts": 2, "duplicates": 0}),
        )

    def test_index_path_admission_precedes_read(self) -> None:
        outside = self.base / "outside.json"
        outside.write_bytes(b"\xffoutside")
        for name in (str(outside), "../outside.json", "folder/../INDEX.json", "C:/outside.json"):
            with self.subTest(path=name):
                counts = self.assert_rejected("relative path without traversal", replace(self.spec, index_file=name))
                self.assertEqual(counts["records"], 0)

    def test_index_symlink_escape_precedes_read(self) -> None:
        outside = self.base / "outside.json"
        outside.write_bytes(b"\xffoutside")
        index = self.root / "INDEX.json"
        index.unlink()
        index.symlink_to(outside)
        self.assertEqual(self.assert_rejected("path escapes the corpus")["records"], 0)

    def test_record_path_admission_precedes_metadata_read(self) -> None:
        outside = self.base / "Outside"
        outside.mkdir()
        (outside / "metadata.json").write_bytes(b"\xffoutside")
        for value in (
            str(outside), "../Outside", "data/../Outside", "/missing", "C:/Outside",
            "", ".", None, 7, ["data"], "data\\Outside",
        ):
            with self.subTest(path=value):
                self.record["path"] = value
                self.save_index()
                self.assertEqual(
                    self.assert_rejected("relative path without traversal")["records"], 0
                )

    def test_record_symlink_escape_precedes_metadata_read(self) -> None:
        outside = self.base / "Outside"
        self.record_dir.rename(outside)
        (outside / "metadata.json").write_bytes(b"\xffoutside")
        self.record_dir.symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.assert_rejected("path escapes the corpus")["records"], 0)

    def test_metadata_symlink_escape_precedes_read(self) -> None:
        outside = self.base / "outside.json"
        outside.write_bytes(b"\xffoutside")
        metadata = self.record_dir / "metadata.json"
        metadata.unlink()
        metadata.symlink_to(outside)
        self.assertEqual(self.assert_rejected("path escapes the corpus")["records"], 0)

    def test_series_cannot_name_corpus_or_host_ancestor(self) -> None:
        for name in (self.root.name, self.base.name):
            with self.subTest(series=name):
                self.metadata["series"] = self.record["series"] = name
                self.save_metadata()
                self.save_index()
                self.assert_rejected("inside the corpus")

    def test_index_identity_mismatches(self) -> None:
        for key, wrong in (
            ("series", "Other"), ("item", "Other"),
            ("parts", ["lmnopqrstuv", "abcdefghijk"]),
            ("parts", ["abcdefghijk"]), ("parts", [{"video_id": "abcdefghijk"}]),
        ):
            with self.subTest(key=key, value=wrong):
                original = self.record[key]
                self.record[key] = wrong
                self.save_index()
                self.assert_rejected(f"INDEX `{key}` disagrees")
                self.record[key] = original

    def test_index_requires_identity_fields(self) -> None:
        for key in ("series", "item", "parts", "has_transcript"):
            with self.subTest(key=key):
                original = self.record.pop(key)
                self.save_index()
                self.assert_rejected(f"INDEX record lacks `{key}`")
                self.record[key] = original

    def test_metadata_identity_must_match_path(self) -> None:
        self.metadata["item"] = self.record["item"] = "Different"
        self.save_metadata()
        self.save_index()
        self.assert_rejected("item id must name its own directory")

    def test_duplicate_record_path(self) -> None:
        self.items.append(dict(self.record))
        self.save_index()
        self.assert_rejected("duplicate record path")

    def test_transcript_flag_binds_regular_file(self) -> None:
        for value in (False, 1, "true", None):
            with self.subTest(flag=value):
                self.record["has_transcript"] = value
                self.save_index()
                self.assert_rejected("INDEX `has_transcript` must be True")
        transcript = self.record_dir / "transcript.txt"
        transcript.unlink()
        self.record["has_transcript"] = True
        self.save_index()
        self.assert_rejected("INDEX `has_transcript` must be False")
        self.record["has_transcript"] = False
        self.save_index()
        self.assertEqual(identity.check_corpus(self.root, self.spec)[0], [])
        transcript.mkdir()
        self.assert_rejected("must be a regular file")

    def test_transcript_symlink_escape_even_when_flag_false(self) -> None:
        outside = self.base / "outside.txt"
        outside.write_text("Outside transcript", encoding="utf-8")
        transcript = self.record_dir / "transcript.txt"
        transcript.unlink()
        transcript.symlink_to(outside)
        for flag in (True, False):
            with self.subTest(flag=flag):
                self.record["has_transcript"] = flag
                self.save_index()
                self.assert_rejected("path escapes the corpus")

    def test_session_names_bind_part_ids_not_standalone_upload(self) -> None:
        for value, fragment in (
            ("abcdefghijk_sess1", "does not match session_id"),
            ("abcdefghijk_sess001", "does not match session_id"),
            ("abcdefghijk_sess01\n", "does not match session_id"),
            ("wxyz0123456_sess01", "does not belong to a record part"),
            (None, "does not match session_id"),
        ):
            with self.subTest(session=value):
                self.metadata["sessions"] = [{"session_name": value}]
                self.save_metadata()
                self.assert_rejected(fragment)
        for sessions in (None, "abcdefghijk_sess01", {}, [None], [{}]):
            with self.subTest(sessions=sessions):
                self.metadata["sessions"] = sessions
                self.save_metadata()
                self.assert_rejected("sessions")
        del self.metadata["sessions"]
        self.save_metadata()
        self.assertEqual(identity.check_corpus(self.root, self.spec)[0], [])

    def test_invalid_part_identity_and_shape(self) -> None:
        for value in ("short", "abcdefghijk\n", None, []):
            with self.subTest(video_id=value):
                self.metadata["parts"][0]["video_id"] = value
                self.save_metadata()
                self.assert_rejected("not an 11-character YouTube id")
        self.metadata["parts"] = [None]
        self.save_metadata()
        self.assert_rejected("parts[0] is not an object")
        self.metadata["parts"] = None
        self.save_metadata()
        self.assert_rejected("`parts` must be a list")

    def test_duplicate_index_presence_and_value(self) -> None:
        self.record["duplicate_of"] = "Series/Canonical"
        self.save_index()
        self.assert_rejected("INDEX `duplicate_of` disagrees")
        del self.record["duplicate_of"]
        self.metadata["duplicate_of"] = "Series/Canonical"
        self.save_metadata()
        self.save_index()
        self.assert_rejected("INDEX `duplicate_of` disagrees")
        self.record["duplicate_of"] = "Series/Different"
        self.save_index()
        self.assert_rejected("INDEX `duplicate_of` disagrees")

    def test_duplicate_path_is_source_relative_and_contained(self) -> None:
        for value, fragment in (
            ("Series/Missing", "not a record path"),
            (self.relative, "not a record path"),
            ("../Item", "relative path without traversal"),
            (str(self.record_dir), "relative path without traversal"),
            (None, "relative path without traversal"),
        ):
            with self.subTest(duplicate=value):
                self.metadata["duplicate_of"] = self.record["duplicate_of"] = value
                self.save_metadata()
                self.save_index()
                self.assert_rejected(fragment)
        outside = self.base / "external-record"
        outside.mkdir()
        (self.root / "data/video/source/Series/Escape").symlink_to(outside, target_is_directory=True)
        self.metadata["duplicate_of"] = self.record["duplicate_of"] = "Series/Escape"
        self.save_metadata()
        self.save_index()
        self.assert_rejected("path escapes the corpus")

    def test_malformed_json_and_nonregular_metadata(self) -> None:
        metadata = self.record_dir / "metadata.json"
        for value in (b"{", b"\xff", b"[]"):
            with self.subTest(content=value):
                metadata.write_bytes(value)
                self.assert_rejected("metadata.json")
        metadata.unlink()
        metadata.mkdir()
        self.assert_rejected("regular JSON file")

    def test_schema_drives_transcript_key_and_artifact(self) -> None:
        document = json.loads(self.spec.path.read_text(encoding="utf-8"))
        block = document["x-identity"]
        block["transcript_flag"] = {"key": "transcribed", "artifact": "derived/view.txt"}
        block["index_record_keys"].remove("has_transcript")
        block["index_record_keys"].append("transcribed")
        schema = self.root / "schema.json"
        schema.write_text(json.dumps(document), encoding="utf-8")
        spec = identity.load_schema(schema)
        del self.record["has_transcript"]
        self.record["transcribed"] = True
        self.save_index()
        self.assert_rejected("INDEX `transcribed` must be False", spec)
        artifact = self.record_dir / "derived/view.txt"
        artifact.parent.mkdir()
        artifact.write_text("Derived words", encoding="utf-8")
        self.assertEqual(identity.check_corpus(self.root, spec)[0], [])

    def test_schema_refuses_unsafe_paths_and_missing_relationships(self) -> None:
        schema = self.root / "schema.json"
        for key, value in (
            ("index_file", "../INDEX.json"),
            ("index_file", str(self.root / "INDEX.json")),
            ("transcript_flag", {"key": "has_transcript", "artifact": "../transcript.txt"}),
            ("transcript_flag", {"key": "has_transcript"}),
            ("index_record_keys", ["path"]),
            ("patterns", {"video_id": "^[a-z]{11}$", "session_id": "^[a-z]{11}_sess[0-9]{2}$"}),
        ):
            with self.subTest(key=key, value=value):
                document = json.loads(self.spec.path.read_text(encoding="utf-8"))
                document["x-identity"][key] = value
                schema.write_text(json.dumps(document), encoding="utf-8")
                with self.assertRaises(identity.IdentityError):
                    identity.load_schema(schema)


    def test_empty_parts_and_absent_sessions_are_valid(self) -> None:
        self.metadata["parts"] = self.record["parts"] = []
        del self.metadata["sessions"]
        (self.record_dir / "transcript.txt").unlink()
        self.record["has_transcript"] = False
        self.save_metadata()
        self.save_index()
        self.assertEqual(
            identity.check_corpus(self.root, self.spec),
            ([], {"records": 1, "parts": 0, "duplicates": 0}),
        )

    def artifact_contract(self) -> tuple[Path, identity.Spec, Path]:
        # Root discovery needs only this real marker, not a Git process/store.
        (self.root / ".git").mkdir()
        schema = self.root / "docs/workflows/record-identity.schema.json"
        schema.parent.mkdir(parents=True)
        schema.write_bytes(self.spec.path.read_bytes())
        module = self.root / "scripts/gate" / MODULE
        module.parent.mkdir(parents=True)
        module.write_text(BODY, encoding="utf-8")
        contract = schema.parent / "publishing.md"
        contract.write_text(
            f"{schema.name}  {hashlib.sha256(schema.read_bytes()).hexdigest()}\n"
            f"{MODULE}  {hashlib.sha256(module.read_bytes()).hexdigest()}\n",
            encoding="utf-8",
        )
        return contract, identity.load_schema(schema), module

    def test_contract_refuses_escaping_module_and_schema_symlinks(self) -> None:
        contract, spec, module = self.artifact_contract()
        self.assertEqual(identity.check_contract(contract, spec), [])
        for artifact in (module, spec.path):
            with self.subTest(artifact=artifact.name):
                original = artifact.read_bytes()
                outside = self.base / artifact.name
                outside.write_bytes(original)
                artifact.unlink()
                artifact.symlink_to(outside)
                problems = identity.check_contract(contract, spec)
                self.assertTrue(any("path escapes the corpus" in p for p in problems), problems)
                artifact.unlink()
                artifact.write_bytes(original)

    def test_contract_refuses_ambiguous_artifact(self) -> None:
        contract, spec, module = self.artifact_contract()
        duplicate = self.root / ".github" / MODULE
        duplicate.parent.mkdir()
        duplicate.write_bytes(module.read_bytes())
        self.assertIsNone(identity.resolve_artifact(self.root, MODULE))
        problems = identity.check_contract(contract, spec)
        self.assertTrue(any("not one file under" in p for p in problems), problems)

    def test_explicit_copy_is_not_replaced_by_discovered_artifact(self) -> None:
        contract, _, module = self.artifact_contract()
        selected = self.base / MODULE
        selected.write_bytes(module.read_bytes())
        self.assertIsNone(identity.verify_copy(selected, contract))
        selected.write_text(BODY + "# changed selected copy\n", encoding="utf-8")
        self.assertIn("drifted", identity.verify_copy(selected, contract))
        selected.unlink()
        selected.mkdir()
        self.assertIn("regular file", identity.verify_copy(selected, contract))


def run() -> list[str]:
    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        module = root / "scripts" / "gate" / MODULE
        module.parent.mkdir(parents=True)
        module.write_text(BODY, encoding="utf-8")
        digest = hashlib.sha256(BODY.encode()).hexdigest()

        contract = root / "docs" / "workflows" / "publishing.md"
        contract.parent.mkdir(parents=True)
        contract.write_text(f"```text\n{MODULE}  {digest}\n```\n\n{NOISE}", encoding="utf-8")

        recorded = identity.recorded_digests(contract)
        if recorded != {MODULE: digest}:
            failures.append(f"selftest: parsed digests {recorded}, expected only {MODULE}")

        if identity.resolve_artifact(root, MODULE) != module:
            failures.append(f"selftest: could not resolve {MODULE} under {root}")

        problem = identity.verify_copy(module, contract)
        if problem is not None:
            failures.append(f"selftest: a matching .py copy was rejected: {problem}")

        module.write_text(BODY + "# drifted\n", encoding="utf-8")
        problem = identity.verify_copy(module, contract)
        if problem is None:
            failures.append("selftest: a diverged .py copy was accepted")
        elif "drifted" not in problem:
            failures.append(f"selftest: diverged copy failed without a drift message: {problem}")
    result = unittest.TestResult()
    unittest.defaultTestLoader.loadTestsFromTestCase(CorpusIdentityTests).run(result)
    failures.extend(f"selftest: {test.id()}\n{detail}" for test, detail in result.errors + result.failures)
    return failures


if __name__ == "__main__":  # pragma: no cover - the arm imports run()
    import sys

    problems = run()
    for message in problems:
        print(message, file=sys.stderr)
    sys.exit(1 if problems else 0)
