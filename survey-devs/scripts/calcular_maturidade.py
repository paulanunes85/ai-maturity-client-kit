#!/usr/bin/env python3
"""Calcula maturidade IA dos devs a partir das respostas do survey.

Lê: survey-devs/respostas-devs.json (output do /importar-survey-devs)
Aplica: rubric.py (regras determinísticas L0-L4 por dimensão)
Gera:
  - saida/maturidade-developer-survey-<DATE>.json (estruturado, para programs)
  - Resumo no stdout

Uso:
    python3 calcular_maturidade.py
    python3 calcular_maturidade.py --input survey-devs/respostas-devs.json
    python3 calcular_maturidade.py --out saida/
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

# Allow running from any directory
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from rubric import score_respondent, aggregate_team, DIMENSIONS, label_for


def main():
    ap = argparse.ArgumentParser()
    kit_root = SCRIPT_DIR.parent.parent  # kit-cliente/
    ap.add_argument("--input", default=str(kit_root / "survey-devs/respostas-devs.json"),
                    help="Path to respostas-devs.json")
    ap.add_argument("--out", default=str(kit_root / "saida"),
                    help="Output directory")
    args = ap.parse_args()

    inp = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not inp.exists():
        print(f"❌ Input não encontrado: {inp}")
        print(f"   Rode /importar-survey-devs primeiro.")
        return 1

    data = json.loads(inp.read_text(encoding="utf-8"))
    respondents = data.get("respondents", [])
    n = len(respondents)
    print(f"\n📊 Calculando maturidade IA — {n} respondentes (anônimos)\n")

    if n == 0:
        print("❌ Nenhum respondente.")
        return 1

    # Score each respondent (internal — never shown individually in output report)
    individual_scores = []
    for r in respondents:
        scores = score_respondent(r["responses"])
        individual_scores.append(scores)

    # Aggregate
    team = aggregate_team(individual_scores)

    # Build output JSON
    date = datetime.date.today().isoformat()
    output = {
        "metadata": {
            "computed_at": datetime.datetime.utcnow().isoformat() + "Z",
            "source": str(inp.relative_to(kit_root)) if inp.is_relative_to(kit_root) else str(inp),
            "n_respondents": n,
            "rubric_version": "1.0 (deterministic)",
            "anonymous": True,
            "scope": "team aggregate (no individual scores in output)",
        },
        "team_overall": {
            "score": team["team_overall_score"],
            "label": team["team_overall_label"],
            "respondents_with_overall": team["n_with_overall"],
        },
        "dimensions": team["dimensions"],
        "ranking": _ranking(team["dimensions"]),
    }

    out_path = out_dir / f"maturidade-developer-survey-{date}.json"
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Output: {out_path.relative_to(kit_root) if out_path.is_relative_to(kit_root) else out_path}\n")

    # Console summary
    print("═" * 60)
    print(f"MATURIDADE IA DO TIME (n={n} devs anônimos)")
    print("═" * 60)
    if team["team_overall_score"] is not None:
        print(f"\n🎯 Overall: {team['team_overall_score']:.2f} ({team['team_overall_label']})\n")
    else:
        print("\n⚠ Sem cobertura suficiente para calcular overall.\n")

    print(f"{'Dimensão':<10} {'Score':<8} {'Rótulo':<28} {'Distribuição (% devs)':<35}")
    print("-" * 90)
    for did, _, _, _ in DIMENSIONS:
        d = team["dimensions"][did]
        if d["team_score"] is None:
            print(f"{did:<10} {'—':<8} {'Sem dados':<28}")
            continue
        dist = d["distribution_pct"]
        dist_str = f"L0={dist['L0']}% L1={dist['L1']}% L2={dist['L2']}% L3={dist['L3']}% L4={dist['L4']}%"
        score_str = f"{d['team_score']:.2f}"
        print(f"{did:<10} {score_str:<8} {d['label']:<28} {dist_str:<35}")
    print()

    print(f"🏆 Top 3 dimensões mais fortes:")
    for i, (did, name, score) in enumerate(_ranking(team["dimensions"])["top"], 1):
        print(f"   {i}. {did} {name} — {score:.2f} ({label_for(score)})")
    print()

    print(f"⚠ Top 3 dimensões mais fracas (oportunidades):")
    for i, (did, name, score) in enumerate(_ranking(team["dimensions"])["bottom"], 1):
        print(f"   {i}. {did} {name} — {score:.2f} ({label_for(score)})")
    print()

    print("Próximo: /insights-developer-survey gera o relatório completo em PT-BR.")
    return 0


def _ranking(dims: dict) -> dict:
    """Top/bottom 3 dimensions by team score."""
    scored = [
        (did, d["name"], d["team_score"])
        for did, d in dims.items()
        if d["team_score"] is not None
    ]
    sorted_desc = sorted(scored, key=lambda x: x[2], reverse=True)
    return {
        "top": sorted_desc[:3],
        "bottom": list(reversed(sorted_desc[-3:])) if len(sorted_desc) >= 3 else sorted_desc,
    }


if __name__ == "__main__":
    sys.exit(main())
