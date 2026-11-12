"""Arm: gnn - Generalized Notation Notation conformance against the pin.

Two modes in one file: the default bootstraps an isolated environment holding
the pinned parser and then re-execs itself with ``--verify-only`` in that
environment, so the verification code is identical locally and in CI.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

from common import GNN_PIN, GNN_PYTHON_RANGE, ROOT, cache_dir, find_python, log, read_pin

RUNTIME_DEPS = ["defusedxml", "psutil", "pyyaml"]


def version(exe: str) -> tuple[int, int]:
    completed = subprocess.run(
        [exe, "-c", "import sys; print(f'{sys.version_info[0]}.{sys.version_info[1]}')"],
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        return (0, 0)
    major, minor = completed.stdout.strip().split(".")
    return (int(major), int(minor))


def supported(exe: str) -> bool:
    return (3, 11) <= version(exe) < (3, 15)


def interpreter() -> str:
    candidates = [os.environ.get("GATE_PYTHON", ""), sys.executable, "python3.12", "python3.11"]
    for candidate in candidates:
        if not candidate:
            continue
        resolved = find_python([candidate]) if shutil.which(candidate) or Path(candidate).exists() else ""
        if resolved and supported(resolved):
            return resolved
    uv = shutil.which("uv")
    if uv:
        completed = subprocess.run([uv, "python", "find", "3.12"], capture_output=True, text=True)
        if completed.returncode == 0:
            candidate = completed.stdout.strip().splitlines()[-1].strip()
            if candidate and supported(candidate):
                return candidate
    raise SystemExit(
        f"gnn: no interpreter in {GNN_PYTHON_RANGE} found for the pinned parser; "
        f"set GATE_PYTHON or run `uv python install 3.12`"
    )


def installed_version(python: str) -> str:
    completed = subprocess.run(
        [python, "-c", "import gnn; print(gnn.__version__)"],
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip() if completed.returncode == 0 else ""


def ensure_environment(pin: dict, cold: bool) -> str:
    tag = pin["tag"]
    interpreter_path = interpreter()
    root = cache_dir() / f"gnn-{tag}-py{version(interpreter_path)[0]}.{version(interpreter_path)[1]}"
    if cold and root.exists():
        shutil.rmtree(root)
    python = root / "bin" / "python"
    if not python.exists():
        log(f"gnn: creating isolated environment at {root} with {interpreter_path}")
        subprocess.run([interpreter_path, "-m", "venv", str(root)], check=True)
    expected = tag.removeprefix("v")
    if installed_version(str(python)) != expected:
        log(f"gnn: installing pinned {pin['repository']}@{tag}")
        subprocess.run(
            [str(python), "-m", "pip", "install", "--quiet", "--disable-pip-version-check", *RUNTIME_DEPS],
            check=True,
        )
        spec = f"git+https://github.com/{pin['repository']}.git@{pin['revision']}"
        subprocess.run(
            [
                str(python),
                "-m",
                "pip",
                "install",
                "--quiet",
                "--disable-pip-version-check",
                "--no-deps",
                f"generalized-notation-notation @ {spec}",
            ],
            check=True,
        )
    else:
        log(f"gnn: reusing installed parser {expected} at {root}")
    return str(python)


def verify() -> int:
    from gnn import __version__
    from gnn.parsers.basic import parse_gnn_formal, validate_gnn_syntax
    from gnn.type_checker import GNNTypeChecker

    pin = read_pin(GNN_PIN)
    expected = pin["tag"].removeprefix("v")
    if __version__ != expected:
        raise SystemExit(f"gnn: installed {__version__!r} does not match pin {pin['tag']!r}")

    sketches = sorted(ROOT.rglob("*.gnn.md"))
    if sketches:
        for sketch in sketches:
            parsed = parse_gnn_formal(sketch)
            if parsed is None or getattr(parsed, "parse_errors", None):
                raise SystemExit(f"gnn: {sketch.relative_to(ROOT)} did not parse cleanly")
            valid, errors = validate_gnn_syntax(sketch.read_text(encoding="utf-8"))
            if not valid:
                raise SystemExit(f"gnn: {sketch.relative_to(ROOT)} syntax errors: {errors!r}")
        with tempfile.TemporaryDirectory(prefix="repo-gnn-") as output_dir:
            model_dir = Path(output_dir) / "models"
            model_dir.mkdir()
            for index, sketch in enumerate(sketches):
                shutil.copy2(sketch, model_dir / f"{index:03d}_{sketch.name}")
            if not GNNTypeChecker().validate_gnn_files(model_dir, Path(output_dir)):
                raise SystemExit("gnn: type checker rejected the repository sketches")
        checked, source = len(sketches), "repository"
    else:
        url = (
            "https://raw.githubusercontent.com/ActiveInferenceInstitute/"
            "Generalized_Notation_Notation/"
            f"{pin['revision']}/input/gnn_files/basics/static_perception.md"
        )
        with tempfile.TemporaryDirectory(prefix="pinned-exemplar-") as output_dir:
            exemplar = Path(output_dir) / "static_perception.md"
            urllib.request.urlretrieve(url, exemplar)
            parsed = parse_gnn_formal(exemplar)
            if parsed is None or getattr(parsed, "parse_errors", None):
                raise SystemExit("gnn: pinned exemplar did not parse cleanly")
            valid, errors = validate_gnn_syntax(exemplar.read_text(encoding="utf-8"))
            if not valid:
                raise SystemExit(f"gnn: pinned exemplar syntax errors: {errors!r}")
            model_dir = Path(output_dir) / "models"
            model_dir.mkdir()
            shutil.copy2(exemplar, model_dir / exemplar.name)
            if not GNNTypeChecker().validate_gnn_files(model_dir, Path(output_dir)):
                raise SystemExit("gnn: type checker rejected the pinned exemplar")
        checked, source = 1, "pinned-exemplar"

    print(
        json.dumps(
            {
                "gnn-version": __version__,
                "pin-revision": pin["revision"],
                "models": checked,
                "source": source,
                "result": "verified",
            },
            sort_keys=True,
        )
    )
    return 0


def run(argv: list[str]) -> int:
    if argv and argv[0] == "--verify-only":
        return verify()
    pin = read_pin(GNN_PIN)
    cold = "--cold" in argv
    unknown = [item for item in argv if item not in {"--cold", "--verify-only"}]
    if unknown:
        raise SystemExit(f"gnn: unknown arguments {unknown}")
    python = ensure_environment(pin, cold)
    completed = subprocess.run([python, str(Path(__file__).resolve()), "--verify-only"], cwd=str(ROOT))
    return completed.returncode


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
