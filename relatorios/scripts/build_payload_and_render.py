#!/usr/bin/env python3
"""Build payload from kit data and render the 5 PDF reports.

Strategy: use sample_payload.json as the BASE STRUCTURE (provides all the
nested fields the Jinja2 templates expect — scoring_rationale, h1_initiatives,
technology_resources_per_pillar, success_metrics_per_pillar, risks_per_pillar,
horizons narrative, three_horizons technologies, branding, etc.) and OVERWRITE
only the fields we have real client data for:
  - organization (from respostas.json)
  - assessment.id / assessment.completed_date
  - scores.overall.weighted_avg / level_label / gap
  - scores.pillars[].weighted_avg / level_label / gap
  - capabilities[].current_score / current_level_label / gap (matched by id)
  - gap_analysis[] (rebuilt from gaps.json, structure mirrors sample)
  - implementation_guide_inputs (from implementation-guide-inputs.json if exists)

Fields we DON'T have client data for (h1_initiatives, scoring_rationale,
risks, technology recommendations, etc.) keep the rich sample placeholders —
client can edit saida/payload.json and re-render to personalize them.

Usage:
    python3 build_payload_and_render.py
    python3 build_payload_and_render.py --kit /path/to/kit-cliente
    python3 build_payload_and_render.py --no-render   # only build payload, skip PDFs
"""
from __future__ import annotations

import argparse
import copy
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

# Local imports
sys.path.insert(0, str(Path(__file__).resolve().parent))
import branding

DEFAULT_TARGET = 3.0


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def label_from_score(score: float | None) -> str:
    if score is None: return "Sem resposta"
    if score < 0.5:   return "L0 — Inicial"
    if score < 1.5:   return "L1 — Em Desenvolvimento"
    if score < 2.5:   return "L2 — Definido"
    if score < 3.5:   return "L3 — Gerenciado"
    return "L4 — Otimizando"


def priority_from_ps(ps: float) -> str:
    if ps >= 2.4: return "P0 — Crítico"
    if ps >= 1.6: return "P1 — Alto"
    if ps >= 0.9: return "P2 — Médio"
    return "P3 — Baixo"


def build_payload(kit: Path) -> dict:
    """Merge sample_payload.json (structure) with client data (overrides)."""
    sample = load_json(kit / "relatorios/sample_payload.json")
    payload = copy.deepcopy(sample)

    # Merge paulasilva-ms branding into existing payload (preserves required fields like platform_name)
    payload.setdefault("branding", {}).update({
        "primary_color": branding.MS_BLUE,
        "author": branding.AUTHOR,
        "role": branding.ROLE,
        "author_name": branding.META_BAR,
        "contact": branding.CONTACT,
        "tagline": branding.TAGLINE,
        "design_system": branding.DESIGN_SYSTEM,
        "palette_red": branding.MS_RED,
        "palette_green": branding.MS_GREEN,
        "palette_yellow": branding.MS_YELLOW,
        "palette_blue": branding.MS_BLUE,
    })

    # ─── INPUTS ─────────────────────────────────────
    respostas_path = kit / "respostas.json"
    scores_path = kit / "saida/scores.json"
    gaps_path = kit / "saida/gaps.json"
    recs_path = kit / "saida/recomendacoes.json"
    ig_path = kit / "implementation-guide-inputs.json"

    have_client_data = scores_path.exists()
    if not have_client_data:
        print("⚠️ saida/scores.json não encontrado — gerando PDFs com dados do sample (Acme).")
        print("   Para gerar com seus dados, rode /pipeline-completo primeiro.\n")
        # Cross-survey artifacts may still exist independently — attach them.
        _attach_cross_survey(payload, kit)
        return payload

    respostas = load_json(respostas_path) if respostas_path.exists() else {}
    scores = load_json(scores_path)
    gaps = load_json(gaps_path) if gaps_path.exists() else {"gaps": [], "summary": {}}
    recs = load_json(recs_path) if recs_path.exists() else {"ranked_strategies": []}

    meta = respostas.get("metadata", {})

    # ─── LOCALE ─────────────────────────────────────
    locale = meta.get("language", "pt-br").lower().replace("_", "-")
    if locale not in ("en", "es", "pt-br"):
        locale = "pt-br"
    payload["locale"] = locale

    # ─── ORGANIZATION (override only known fields) ──
    org = payload["organization"]
    org["name"] = meta.get("organization") or org["name"]
    if meta.get("respondent_role"):
        org["primary_contact_role"] = meta["respondent_role"]

    # ─── ASSESSMENT ─────────────────────────────────
    assess = payload["assessment"]
    assess["id"] = scores.get("metadata", {}).get("respondent", assess.get("id", "—"))
    assess["completed_date"] = meta.get("assessment_date", assess["completed_date"])
    assess["generated_date"] = datetime.date.today().isoformat()
    assess["framework_version"] = scores.get("metadata", {}).get(
        "framework_version", assess["framework_version"]
    )

    # ─── SCORES.OVERALL ─────────────────────────────
    overall_score = scores["overall"]["score"]
    payload["scores"]["overall"]["weighted_avg"] = round(overall_score, 2)
    payload["scores"]["overall"]["level_label"] = label_from_score(overall_score)
    target_overall = payload["scores"]["overall"].get("target", 3.0)
    payload["scores"]["overall"]["gap"] = max(0, round(target_overall - overall_score, 2))

    # ─── SCORES.PILLARS ─────────────────────────────
    # Index sample pillars by id for safe override
    sample_pillars_by_id = {p["id"]: p for p in payload["scores"]["pillars"]}
    for p_client in scores.get("pillars", []):
        pid = p_client["id"]
        sample_p = sample_pillars_by_id.get(pid)
        if not sample_p:
            continue
        sample_p["weighted_avg"] = round(p_client["score"], 2)
        sample_p["level_label"] = label_from_score(p_client["score"])
        target = sample_p.get("target", 3.0)
        sample_p["gap"] = max(0, round(target - p_client["score"], 2))

    # ─── SCORES.PE_READINESS ────────────────────────
    pe_score = scores["overall"].get("pe_score")
    if pe_score is not None:
        payload["scores"]["pe_readiness"]["weighted_score"] = round(pe_score, 2)
        payload["scores"]["pe_readiness"]["level"] = label_from_score(pe_score)

    # ─── CAPABILITIES (override scores, keep narrative fields from sample) ─
    target_overrides = respostas.get("target_overrides", {})
    sample_caps_by_id = {c.get("id") or c.get("code"): c for c in payload["capabilities"]}

    for c_client in scores.get("capabilities", []):
        cid = c_client["id"]
        sample_c = sample_caps_by_id.get(cid)
        if not sample_c:
            continue
        score = c_client.get("score")
        sample_c["current_score"] = round(score, 2) if score is not None else 0.0
        sample_c["current_level_label"] = label_from_score(score)
        target = target_overrides.get(cid, DEFAULT_TARGET)
        sample_c["target_score"] = round(float(target), 2)
        sample_c["target_level_label"] = label_from_score(float(target))
        if score is not None:
            sample_c["gap"] = max(0, round(target - score, 2))
            ps = c_client.get("weight", 1.0) * (target - score)
            sample_c["gap_priority"] = priority_from_ps(ps).split(" ")[0]
        else:
            sample_c["gap"] = 0
            sample_c["gap_priority"] = "P3"

    # ─── GAP_ANALYSIS (rebuild list from gaps.json, mimic sample structure) ─
    new_gap_analysis = []
    for g in gaps.get("gaps", []):
        # Find existing sample item with same code to inherit recommended_actions
        existing = next(
            (gi for gi in payload["gap_analysis"]
             if gi.get("capability_code") == g["capability_id"]),
            None,
        )
        recommended_actions = (
            existing.get("recommended_actions", {})
            if existing
            else {
                "h1": "Definir baseline e estabelecer métricas de cobertura.",
                "h2": "Expandir piloto para >50% das equipes; instrumentar OKRs.",
                "h3": "Atingir cobertura universal e otimização contínua.",
            }
        )
        new_gap_analysis.append({
            "pillar_id": g["pillar_id"],
            "capability_code": g["capability_id"],
            "capability_name": g["capability_name_pt_br"],
            "current": round(g["current_score"], 2),
            "target": round(g["target_level"], 2),
            "gap": round(g["gap_size"], 2),
            "priority": g["priority"].split(" ")[0],  # "P0 — Crítico" → "P0"
            "recommended_actions": recommended_actions,
        })
    if new_gap_analysis:
        payload["gap_analysis"] = new_gap_analysis

    # ─── IMPLEMENTATION_GUIDE_INPUTS (from wizard) ──
    if ig_path.exists():
        ig = load_json(ig_path)
        wizard_inputs = ig.get("implementation_guide_inputs", {})
        if wizard_inputs:
            # Merge: keep sample structure where wizard didn't fill; override what's provided
            current_ig = payload.get("implementation_guide_inputs", {})
            for key, value in wizard_inputs.items():
                if value and (isinstance(value, str) and value.strip()):
                    # For string fields, parse markdown lists/tables into structured form
                    # if the sample expects structured data — for now, store as raw markdown.
                    # Templates handle both cases via wizard_placeholder() macro.
                    current_ig[f"{key}_raw_markdown"] = value
            payload["implementation_guide_inputs"] = current_ig
            print(f"✓ Merged implementation-guide-inputs.json "
                  f"({ig.get('metadata', {}).get('completion_pct', 0)}% completo)")

    # ─── CROSS-SURVEY DATA (optional) ────────────────
    _attach_cross_survey(payload, kit)

    return payload


def _attach_cross_survey(payload: dict, kit: Path) -> None:
    """Detect optional survey artifacts and attach them to ``payload``."""
    cross = collect_cross_survey_data(kit)
    if not cross:
        return
    payload["cross_survey_data"] = cross
    bits = []
    if "developer_survey_maturity" in cross:
        n = cross["developer_survey_maturity"].get("respondents") or "?"
        bits.append(f"survey-devs maturity (n={n})")
    if "developer_survey_insights" in cross:
        bits.append("survey-devs insights")
    if "learning_plan" in cross:
        bits.append("learning plan")
    print(f"✓ cross_survey_data attached: {', '.join(bits)}")


def collect_cross_survey_data(kit: Path) -> dict | None:
    """Detect optional outputs from the two complementary surveys and
    expose them as ``payload.cross_survey_data`` for downstream consumption.

    The PDF templates may ignore this field; surfacing it in ``payload.json``
    keeps the data inspectable and unblocks future template iterations.
    """
    out_dir = kit / "saida"
    if not out_dir.exists():
        return None

    cross: dict = {"available": False}

    # Latest maturidade-developer-survey-*.json (structured rubric scores)
    mat_candidates = sorted(out_dir.glob("maturidade-developer-survey-*.json"), reverse=True)
    if mat_candidates:
        try:
            mat = load_json(mat_candidates[0])
            meta = mat.get("metadata", {}) or {}
            # Dimensions live at the top level: {"D2": {"team_score": .., "label": ..}, ...}
            raw_dims = mat.get("dimensions") or {}
            dims = []
            for did, entry in raw_dims.items():
                if not isinstance(entry, dict):
                    continue
                score = entry.get("team_score", entry.get("score"))
                if score is None:
                    continue
                dims.append({
                    "dimension": did,
                    "name": entry.get("name"),
                    "score": round(float(score), 2),
                    "label": entry.get("label") or label_from_score(float(score)),
                    "respondents": entry.get("respondents_with_score"),
                })
            team_overall = mat.get("team_overall", {}) or {}
            cross["developer_survey_maturity"] = {
                "source_file": str(mat_candidates[0].relative_to(kit)),
                "respondents": meta.get("n_respondents") or meta.get("total_respondents"),
                "overall_score": team_overall.get("score"),
                "overall_label": team_overall.get("label"),
                "dimensions": dims,
            }
            cross["available"] = True
        except (json.JSONDecodeError, OSError, ValueError):
            pass

    # Latest insights-developer-survey-*.md
    ins_candidates = sorted(out_dir.glob("insights-developer-survey-*.md"), reverse=True)
    if ins_candidates:
        cross["developer_survey_insights"] = {
            "source_file": str(ins_candidates[0].relative_to(kit)),
        }
        cross["available"] = True

    # Latest plano-capacitacao-*.md
    plano_candidates = sorted(out_dir.glob("plano-capacitacao-*.md"), reverse=True)
    if plano_candidates:
        cross["learning_plan"] = {
            "source_file": str(plano_candidates[0].relative_to(kit)),
        }
        cross["available"] = True

    return cross if cross["available"] else None


def render_pdfs(payload_path: Path, out_dir: Path, kit: Path) -> int:
    """Invoke render_reports.py to produce the 5 PDFs."""
    script = kit / "relatorios/scripts/render_reports.py"
    cmd = [sys.executable, str(script), "--payload", str(payload_path), "--out", str(out_dir)]
    print(f"\n→ Renderizando 5 PDFs com {payload_path.name}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("STDERR:", result.stderr, file=sys.stderr)
    return result.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kit", default=str(Path(__file__).resolve().parent.parent.parent),
                    help="Path to kit-cliente/")
    ap.add_argument("--out", default=None, help="Output dir (default: <kit>/saida/)")
    ap.add_argument("--no-render", action="store_true", help="Only build payload, skip PDF rendering")
    args = ap.parse_args()

    kit = Path(args.kit).resolve()
    out_dir = Path(args.out).resolve() if args.out else kit / "saida"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Kit:     {kit}")
    print(f"Out:     {out_dir}")
    print()

    # Build payload (merge sample + client data)
    payload = build_payload(kit)
    payload_path = out_dir / "payload.json"
    payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Payload merged: {payload_path} ({payload_path.stat().st_size:,} bytes)")
    print(f"  Locale:  {payload.get('locale')}")
    print(f"  Org:     {payload['organization']['name']}")
    print(f"  Overall: {payload['scores']['overall']['weighted_avg']} ({payload['scores']['overall']['level_label']})")

    if args.no_render:
        return 0

    return render_pdfs(payload_path, out_dir, kit)


if __name__ == "__main__":
    sys.exit(main())
