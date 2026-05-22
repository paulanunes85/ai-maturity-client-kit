#!/usr/bin/env python3
"""End-to-end smoke test for the AI Maturity Assessment kit.

Runs `relatorios/scripts/build_payload_and_render.py --no-render` against the
bundled example data and asserts the resulting `saida/payload.json` has the
expected shape (organization, scores, capabilities, gap_analysis, optional
cross_survey_data when complementary survey artifacts are present).

Pure stdlib — no pytest/openpyxl required. Skips PDF rendering to avoid the
WeasyPrint dependency on contributors' machines.

Usage:
    python3 scripts/smoke_test.py
    python3 scripts/smoke_test.py --with-cross-survey   # also exercises survey artifacts
    make smoke                                          # convenience wrapper
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
SAIDA = KIT / "saida"
EXEMPLOS = KIT / "referencia" / "exemplo-saida"

# Files we will mutate; everything is restored on exit.
SENTINEL_FILES = [
    KIT / "respostas.json",
]


class SmokeError(RuntimeError):
    pass


def _color(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if sys.stdout.isatty() else text


def _ok(msg: str) -> None:
    print(_color("32", f"  ✓ {msg}"))


def _info(msg: str) -> None:
    print(_color("36", f"  • {msg}"))


def _fail(msg: str) -> None:
    print(_color("31", f"  ✗ {msg}"), file=sys.stderr)


def _backup(path: Path) -> Path | None:
    if not path.exists():
        return None
    backup = path.with_suffix(path.suffix + ".smoketest-backup")
    shutil.copy2(path, backup)
    return backup


def _restore(path: Path, backup: Path | None) -> None:
    if backup is None:
        path.unlink(missing_ok=True)
        return
    shutil.move(str(backup), str(path))


def stage_example_inputs(with_cross: bool) -> dict[str, Path | None]:
    """Stage example respostas + (optionally) complementary survey artifacts."""
    state: dict[str, Path | None] = {}

    for f in SENTINEL_FILES:
        state[f"backup:{f.name}"] = _backup(f)

    shutil.copy2(KIT / "respostas.json.example", KIT / "respostas.json")
    _ok("Copied respostas.json.example → respostas.json")

    staged: list[Path] = []
    if with_cross:
        for src_name, dest_name in [
            ("maturidade-developer-survey-EXEMPLO.json", "maturidade-developer-survey-smoketest.json"),
            ("insights-developer-survey-EXEMPLO.md", "insights-developer-survey-smoketest.md"),
            ("plano-capacitacao-EXEMPLO.md", "plano-capacitacao-smoketest.md"),
        ]:
            src = EXEMPLOS / src_name
            if not src.exists():
                continue
            dest = SAIDA / dest_name
            shutil.copy2(src, dest)
            staged.append(dest)
        if staged:
            _ok(f"Staged {len(staged)} cross-survey artifact(s) in saida/")
    state["staged"] = staged  # type: ignore[assignment]
    return state


def cleanup(state: dict[str, Path | None]) -> None:
    print()
    _info("Cleaning up...")
    for f in SENTINEL_FILES:
        _restore(f, state.get(f"backup:{f.name}"))
    for staged in state.get("staged") or []:
        Path(staged).unlink(missing_ok=True)
    (SAIDA / "payload.json").unlink(missing_ok=True)
    _ok("Workspace restored")


def run_build() -> None:
    _info("Running build_payload_and_render.py --no-render")
    result = subprocess.run(
        [sys.executable, "relatorios/scripts/build_payload_and_render.py", "--no-render"],
        cwd=str(KIT),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SmokeError(f"build script exited with code {result.returncode}")
    for line in result.stdout.splitlines():
        if line.strip().startswith(("✓", "⚠️")):
            print("   ", line)


def assert_payload(with_cross: bool) -> None:
    payload_path = SAIDA / "payload.json"
    if not payload_path.exists():
        raise SmokeError("payload.json was not generated")
    size = payload_path.stat().st_size
    if size < 20_000:
        raise SmokeError(f"payload.json suspiciously small ({size} bytes)")
    _ok(f"payload.json present ({size:,} bytes)")

    payload = json.loads(payload_path.read_text(encoding="utf-8"))

    required = ["organization", "assessment", "scores", "capabilities", "gap_analysis"]
    missing = [k for k in required if k not in payload]
    if missing:
        raise SmokeError(f"payload missing required keys: {missing}")
    _ok(f"all required keys present: {', '.join(required)}")

    overall = payload["scores"]["overall"].get("weighted_avg")
    if not isinstance(overall, (int, float)):
        raise SmokeError(f"scores.overall.weighted_avg is not numeric: {overall!r}")
    _ok(f"scores.overall.weighted_avg = {overall}")

    pillars = payload["scores"].get("pillars") or []
    pillar_ids = {p.get("id") for p in pillars}
    if not {"P1", "P2", "P3"} <= pillar_ids:
        raise SmokeError(f"missing pillar ids; got {pillar_ids}")
    _ok(f"pillars P1/P2/P3 present (n={len(pillars)})")

    if with_cross:
        cross = payload.get("cross_survey_data")
        if not cross or not cross.get("available"):
            raise SmokeError("cross_survey_data was expected but not attached")
        dsm = cross.get("developer_survey_maturity", {})
        dims = dsm.get("dimensions") or []
        if len(dims) < 5:
            raise SmokeError(f"expected ≥5 dimensions from rubric, got {len(dims)}")
        _ok(
            f"cross_survey_data attached "
            f"(respondents={dsm.get('respondents')}, dimensions={len(dims)})"
        )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--with-cross-survey",
        action="store_true",
        help="Also stage developer/learning survey artifacts and assert cross_survey_data",
    )
    args = ap.parse_args()

    print(_color("1", "AI Maturity kit — smoke test"))
    print(_color("90", f"  kit: {KIT}"))
    print()

    state: dict[str, Path | None] = {}
    try:
        state = stage_example_inputs(args.with_cross_survey)
        run_build()
        assert_payload(args.with_cross_survey)
        print()
        print(_color("32", "✓ SMOKE TEST PASSED"))
        return 0
    except SmokeError as exc:
        print()
        _fail(str(exc))
        print(_color("31", "✗ SMOKE TEST FAILED"))
        return 1
    finally:
        cleanup(state)


if __name__ == "__main__":
    sys.exit(main())
