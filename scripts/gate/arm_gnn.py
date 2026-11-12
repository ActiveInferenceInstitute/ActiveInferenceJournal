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


def provenance(python: str) -> dict:
    """What the installed distribution says it was built from (PEP 610)."""
    code = (
        "import json\n"
        "from importlib.metadata import PackageNotFoundError, distribution\n"
        "try:\n"
        "    dist = distribution('generalized-notation-notation')\n"
        "except PackageNotFoundError:\n"
        "    print(json.dumps({}))\n"
        "else:\n"
        "    url = json.loads(dist.read_text('direct_url.json') or '{}')\n"
        "    print(json.dumps({'version': dist.version, 'url': url.get('url'),\n"
        "                      'commit': (url.get('vcs_info') or {}).get('commit_id')}))\n"
    )
    completed = subprocess.run([python, "-c", code], capture_output=True, text=True)
    if completed.returncode != 0:
        return {}
    try:
        return json.loads(completed.stdout or "{}")
    except json.JSONDecodeError:
        return {}


def environment_matches(python: str, pin: dict) -> bool:
    """True only when the environment holds the parser built from the pinned commit.

    The version alone is not enough: bumping the revision while the tag stays
    v5.0.3 leaves ``gnn.__version__`` unchanged, so reuse keyed on the version
    would verify the old parser and report the new pin. The version is checked
    separately by ``verify()``, which reports it against the pin's tag.
    """
    return provenance(python).get("commit") == pin["revision"]


def ensure_environment(pin: dict, cold: bool) -> str:
    revision = pin["revision"]
    slug = pin["repository"].replace("/", "-")
    interpreter_path = interpreter()
    major, minor = version(interpreter_path)
    # The cache key carries repository, revision and interpreter, so changing
    # any of them builds a different environment instead of reusing a wrong one.
    root = cache_dir() / f"gnn-{slug}-{revision}-py{major}.{minor}"
    if cold and root.exists():
        shutil.rmtree(root)
    python = root / "bin" / "python"
    if not python.exists():
        log(f"gnn: creating isolated environment at {root} with {interpreter_path}")
        subprocess.run([interpreter_path, "-m", "venv", str(root)], check=True)

    if environment_matches(str(python), pin):
        log(f"gnn: reusing parser {pin['tag']} at {revision[:12]}")
        return str(python)

    if provenance(str(python)):
        log(f"gnn: cached environment holds a different build; reinstalling {revision[:12]}")
    log(f"gnn: installing pinned {pin['repository']}@{pin['tag']} ({revision[:12]})")
    subprocess.run(
        [str(python), "-m", "pip", "install", "--quiet", "--disable-pip-version-check", *RUNTIME_DEPS],
        check=True,
    )
    spec = f"git+https://github.com/{pin['repository']}.git@{revision}"
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
    landed = provenance(str(python)).get("commit")
    if landed != revision:
        raise SystemExit(
            f"gnn: install did not land on {revision[:12]}; provenance reports {landed}"
        )
    return str(python)


def verify() -> int:
    from gnn import __version__
    from gnn.parsers.basic import parse_gnn_formal, validate_gnn_syntax
    from gnn.type_checker import GNNTypeChecker

    pin = read_pin(GNN_PIN)
    expected = pin["tag"].removeprefix("v")
    if __version__ != expected:
        raise SystemExit(f"gnn: installed {__version__!r} does not match pin {pin['tag']!r}")

    # The version is shared across revisions of a tag, so bind the parser to the
    # pinned commit as well: this is the check that a same-tag revision bump
    # cannot pass on a stale environment.
    from importlib.metadata import PackageNotFoundError, distribution

    try:
        raw = distribution("generalized-notation-notation").read_text("direct_url.json")
    except PackageNotFoundError:
        raise SystemExit("gnn: the pinned parser is not installed in this environment") from None
    if not raw:
        raise SystemExit("gnn: installed parser has no direct_url.json; cannot bind it to the pin")
    direct = json.loads(raw)
    commit = (direct.get("vcs_info") or {}).get("commit_id")
    if commit != pin["revision"]:
        raise SystemExit(
            f"gnn: installed parser is from {commit or 'a non-VCS source'}, "
            f"but the pin is {pin['revision']}"
        )

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
            verdict = GNNTypeChecker().validate_gnn_files(model_dir, Path(output_dir))
            if verdict is not True:
                raise SystemExit(
                    "gnn: type checker rejected the repository sketches "
                    f"(validate_gnn_files returned {verdict!r})"
                )
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
            verdict = GNNTypeChecker().validate_gnn_files(model_dir, Path(output_dir))
            if verdict is not True:
                raise SystemExit(
                    "gnn: type checker rejected the pinned exemplar "
                    f"(validate_gnn_files returned {verdict!r})"
                )
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
    if completed.returncode != 0:
        return completed.returncode
    # The verdict selftest runs in the same isolated environment as verify, so
    # the arm's acceptance rule cannot regress without turning the gate red.
    selftest = Path(__file__).resolve().parent / "gnn_selftest.py"
    return subprocess.run([python, str(selftest)], cwd=str(ROOT)).returncode


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
