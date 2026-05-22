#!/usr/bin/env python3
"""Gera relatório de insights do Developer Survey.

Lê: survey-devs/respostas-devs.json (output de /importar-survey-devs)
Aplica: rubric.py (calcula maturidade L0-L4 em 7 dimensões)
Combina: agregação descritiva (% adoção, top tools, pain points)
Gera:
  - saida/maturidade-developer-survey-<DATE>.json
  - saida/insights-developer-survey-<DATE>.md (relatório completo PT-BR)

Uso:
    python3 gerar_insights.py
    python3 gerar_insights.py --input X --out Y
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPT_DIR.parent.parent / "relatorios" / "scripts"))
from rubric import score_respondent, aggregate_team, DIMENSIONS, label_for
from calcular_maturidade import _ranking
import branding


def safe_pct(num, total):
    return round(100 * num / total, 1) if total > 0 else 0


def aggregate_responses(respondents, qid, multi=False):
    """Counter of options for a given question."""
    counts = Counter()
    total_responses = 0
    for r in respondents:
        ans = r["responses"].get(qid, {}).get("value", "")
        if not ans:
            continue
        if multi:
            for opt in str(ans).split(";"):
                opt = opt.strip()
                if opt:
                    counts[opt] += 1
                    total_responses += 1
        else:
            counts[str(ans).strip()] += 1
            total_responses += 1
    return counts, total_responses


def collect_quotes(respondents, qid, max_q=5):
    """Get text-livre quotes (anonymized — no respondent_id)."""
    quotes = []
    for r in respondents:
        v = r["responses"].get(qid, {}).get("value", "").strip()
        if v and len(v) > 20 and "[texto livre" not in v.lower() and "[resposta livre" not in v.lower():
            quotes.append(v)
    return quotes[:max_q]


def bar(pct, width=20):
    filled = int(round(pct * width / 100))
    return "█" * filled + "░" * (width - filled)


def main():
    ap = argparse.ArgumentParser()
    kit = SCRIPT_DIR.parent.parent
    ap.add_argument("--input", default=str(kit / "survey-devs/respostas-devs.json"))
    ap.add_argument("--out", default=str(kit / "saida"))
    args = ap.parse_args()

    inp = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not inp.exists():
        print(f"❌ {inp} não encontrado. Rode /importar-survey-devs primeiro.")
        return 1

    data = json.loads(inp.read_text(encoding="utf-8"))
    respondents = data.get("respondents", [])
    n = len(respondents)
    date = datetime.date.today().isoformat()

    if n < 3:
        print(f"⚠ Apenas {n} respondentes. Insights serão preliminares.")

    # Compute maturity per respondent + aggregate
    individual_scores = [score_respondent(r["responses"]) for r in respondents]
    team = aggregate_team(individual_scores)

    # Save maturity JSON (consolidates with calcular_maturidade.py output schema)
    maturity_path = out_dir / f"maturidade-developer-survey-{date}.json"
    maturity_data = {
        "metadata": {
            "computed_at": datetime.datetime.now(datetime.UTC).isoformat(),
            "source": str(inp.name),
            "n_respondents": n,
            "rubric_version": "1.0 (deterministic)",
            "anonymous": True,
            "scope": "team aggregate (no individual scores in output)",
            **branding.json_metadata(),
        },
        "team_overall": {
            "score": team["team_overall_score"],
            "label": team["team_overall_label"],
            "respondents_with_overall": team["n_with_overall"],
        },
        "dimensions": team["dimensions"],
        "ranking": _ranking(team["dimensions"]),
    }
    maturity_path.write_text(json.dumps(maturity_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # Build descriptive aggregations (used in report)
    s2_q1 = aggregate_responses(respondents, "S2-Q1")[0]            # licença
    s2_q2 = aggregate_responses(respondents, "S2-Q2")[0]            # frequência
    s2_q3, s2_q3_t = aggregate_responses(respondents, "S2-Q3", multi=True)  # modos
    s2_q5, s2_q5_t = aggregate_responses(respondents, "S2-Q5", multi=True)  # features
    s2_q7 = aggregate_responses(respondents, "S2-Q7")[0]            # ganho
    s2_q8, s2_q8_t = aggregate_responses(respondents, "S2-Q8", multi=True)  # tarefas

    s3_q1, s3_q1_t = aggregate_responses(respondents, "S3-Q1", multi=True)  # MS/GH tools

    s4_q1 = aggregate_responses(respondents, "S4-Q1")[0]            # TDD
    s4_q2 = aggregate_responses(respondents, "S4-Q2")[0]            # SDD

    # S5 — knowledge of agent concepts
    s5_concepts = {
        "S5-Q1": ("AI agent", aggregate_responses(respondents, "S5-Q1")[0]),
        "S5-Q3": ("Custom agents (.agent.md)", aggregate_responses(respondents, "S5-Q3")[0]),
        "S5-Q4": ("Skills (SKILL.md)", aggregate_responses(respondents, "S5-Q4")[0]),
        "S5-Q5": ("Prompt files (.prompt.md)", aggregate_responses(respondents, "S5-Q5")[0]),
        "S5-Q6": ("A2A protocol", aggregate_responses(respondents, "S5-Q6")[0]),
        "S5-Q9": ("Personas Agentic DevOps", aggregate_responses(respondents, "S5-Q9")[0]),
    }

    s6_q1, _ = aggregate_responses(respondents, "S6-Q1", multi=True)  # instructions files

    s7_q2 = aggregate_responses(respondents, "S7-Q2")[0]            # Champion?
    s7_q4, _ = aggregate_responses(respondents, "S7-Q4", multi=True)  # métricas

    s8_q1 = aggregate_responses(respondents, "S8-Q1")[0]            # política IA
    s8_q4, _ = aggregate_responses(respondents, "S8-Q4", multi=True)  # security tools

    s9_pain = collect_quotes(respondents, "S9-Q1")
    s9_change = collect_quotes(respondents, "S9-Q2")
    s9_wishlist = collect_quotes(respondents, "S9-Q3")

    # Threshold checks for insights
    no_policy = sum(c for k, c in s8_q1.items() if "Não temos política" in k or "Não sei" in k)
    pct_no_policy = safe_pct(no_policy, n)

    no_champion = s7_q2.get("Não — cada um se vira", 0) + s7_q2.get("Não, mas precisava ter", 0)
    pct_no_champion = safe_pct(no_champion, n)

    daily_copilot = s2_q2.get("Diariamente (várias horas)", 0) + s2_q2.get("Diariamente (esporádico)", 0)
    pct_daily = safe_pct(daily_copilot, n)

    uses_coding_agent = sum(c for k, c in s2_q3.items() if "Coding Agent" in k)
    pct_coding_agent = safe_pct(uses_coding_agent, n)

    knows_mcp_strong = s5_concepts["S5-Q6"][1].get("Uso (ex.: Foundry A2A Tool)", 0) + \
                       s5_concepts["S5-Q6"][1].get("Conheço o conceito", 0)
    pct_mcp = safe_pct(knows_mcp_strong, n)

    # Build report
    md = []
    md.append(branding.md_header().rstrip())
    md.append("")
    md.append("# Developer Survey — Relatório de Insights")
    md.append("")
    md.append(f"**Data:** {date}  ·  **Respondentes:** {n} (anônimos)  ·  **Versão da rubrica:** 1.0")
    md.append(f"**Autor:** {branding.META_BAR}  ·  **Contato:** {branding.CONTACT}")
    md.append("")

    if n < 5:
        md.append(f"> ⚠️ **Resultado preliminar** — apenas {n} respondentes. Considere buscar mais respostas (recomendado ≥15 para representatividade do time).")
        md.append("")

    md.append("---")
    md.append("")
    md.append("## 1 · Sumário Executivo")
    md.append("")

    # Maturity table
    overall = team["team_overall_score"]
    md.append(f"### 🎯 Maturidade IA do Time (rubrica determinística)")
    md.append("")
    overall_str = f"{overall:.2f}" if overall is not None else "N/A"
    md.append(f"> **Overall: {overall_str} ({team['team_overall_label']})**")
    md.append(f"> Baseado em {n} respondentes, 7 dimensões, escala L0-L4 (mesma do assessment principal)")
    md.append("")
    md.append("| Dimensão | Score | Rótulo | % devs em L3+L4 |")
    md.append("|---|---|---|---|")
    for did, name, _, _ in DIMENSIONS:
        d = team["dimensions"][did]
        if d["team_score"] is None:
            md.append(f"| {did} {name} | — | Sem dados | — |")
            continue
        dist = d["distribution_pct"]
        pct_l3l4 = dist["L3"] + dist["L4"]
        md.append(f"| {did} {name} | **{d['team_score']:.2f}** | {d['label']} | {pct_l3l4:.0f}% |")
    md.append("")

    # Top/bottom rankings
    rk = _ranking(team["dimensions"])
    md.append("### 🏆 3 dimensões mais fortes")
    for did, name, score in rk["top"]:
        md.append(f"- **{did}** {name} — score **{score:.2f}** ({label_for(score)})")
    md.append("")
    md.append("### ⚠️ 3 maiores gaps (oportunidades de roadmap)")
    for did, name, score in rk["bottom"]:
        md.append(f"- 🔴 **{did}** {name} — score **{score:.2f}** ({label_for(score)})")
    md.append("")

    # Top 3 insights
    insights = []
    if pct_no_policy > 30:
        insights.append(f"**Risco de governança crítico:** {pct_no_policy:.0f}% dos devs não conhecem política de IA documentada (S8-Q1) — precisa formalizar")
    if pct_no_champion > 50:
        insights.append(f"**Falta de Champions:** {pct_no_champion:.0f}% dos devs não têm AI Champion no time (S7-Q2) — oportunidade de criar Champions Network")
    if pct_daily > 70:
        insights.append(f"**Adoção alta de Copilot:** {pct_daily:.0f}% usa diariamente (S2-Q2) — pronto para mover para modos avançados (Agent, Coding Agent, Spaces)")
    if pct_coding_agent < 30:
        insights.append(f"**Underutilization de Coding Agent:** apenas {pct_coding_agent:.0f}% conhece/usa Coding Agent autônomo (S2-Q3) — tópico de workshop urgente")
    if pct_mcp < 20:
        insights.append(f"**Conceitos avançados desconhecidos:** apenas {pct_mcp:.0f}% conhece MCP/A2A — gap de capacitação técnica")

    md.append("### 💡 3 insights principais")
    for i, ins in enumerate(insights[:3], 1):
        md.append(f"{i}. {ins}")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 2 · Demografia (S1)")
    md.append("")
    s1_q1 = aggregate_responses(respondents, "S1-Q1")[0]
    md.append("### Distribuição por cargo")
    md.append("| Cargo | N | % |")
    md.append("|---|---|---|")
    for cargo, count in s1_q1.most_common(10):
        pct = safe_pct(count, n)
        md.append(f"| {cargo} | {count} | {pct:.0f}% |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 3 · GitHub Copilot — Adoção e Modos (S2)")
    md.append("")
    md.append("### Cobertura de licenças (S2-Q1)")
    md.append("| Tipo | N | % |")
    md.append("|---|---|---|")
    for k, v in s2_q1.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("### Frequência de uso (S2-Q2)")
    md.append("| Frequência | N | % |")
    md.append("|---|---|---|")
    for k, v in s2_q2.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("### 🆕 Modos do Copilot Chat usados (S2-Q3, multi-select)")
    md.append("| Modo | N usuários | % devs |")
    md.append("|---|---|---|")
    for k, v in s2_q3.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("### Features ativas (S2-Q5, multi-select) — Top 8")
    md.append("| Feature | N | % devs |")
    md.append("|---|---|---|")
    for k, v in s2_q5.most_common(8):
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("### Ganho de produtividade percebido (S2-Q7)")
    md.append("| Faixa | N | % |")
    md.append("|---|---|---|")
    for k, v in s2_q7.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 4 · Outras ferramentas Microsoft / GitHub AI (S3)")
    md.append("")
    md.append("### Adoção (S3-Q1, multi-select)")
    md.append("| Ferramenta | N usuários | % devs |")
    md.append("|---|---|---|")
    for k, v in s3_q1.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 5 · Práticas de Desenvolvimento com IA (S4)")
    md.append("")
    md.append("### TDD com IA (S4-Q1)")
    md.append("| Frequência | N | % |")
    md.append("|---|---|---|")
    for k, v in s4_q1.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")
    md.append("### SDD (Spec-Driven Development) (S4-Q2)")
    md.append("| Conhecimento | N | % |")
    md.append("|---|---|---|")
    for k, v in s4_q2.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 6 · Conceitos de Agentes (S5)")
    md.append("")
    md.append("### Conhecimento por conceito")
    md.append("| Conceito | Distribuição |")
    md.append("|---|---|")
    for qid, (name, counts) in s5_concepts.items():
        top = ", ".join(f"{k}={v}" for k, v in counts.most_common(3))
        md.append(f"| **{qid}** {name} | {top} |")
    md.append("")
    md.append(f"**Insight:** apenas {pct_mcp:.0f}% conhece MCP — conceitos avançados (A2A, handoffs, subagentes, personas) são desconhecidos pela maioria. Oportunidade de workshop técnico.")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 7 · Markdown / Memory / Instructions (S6)")
    md.append("")
    md.append("### Arquivos de instruções usados (S6-Q1, multi)")
    md.append("| Arquivo | N usuários | % |")
    md.append("|---|---|---|")
    for k, v in s6_q1.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 8 · Usabilidade e Best Practices (S7)")
    md.append("")
    md.append("### Champions no time (S7-Q2)")
    md.append("| Resposta | N | % |")
    md.append("|---|---|---|")
    for k, v in s7_q2.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("### Métricas de produtividade (S7-Q4, multi)")
    md.append("| Framework | N | % |")
    md.append("|---|---|---|")
    for k, v in s7_q4.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 9 · 🔒 Segurança e Governança (S8)")
    md.append("")
    md.append("### Política documentada (S8-Q1)")
    md.append("| Resposta | N | % |")
    md.append("|---|---|---|")
    for k, v in s8_q1.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    if pct_no_policy > 30:
        md.append("")
        md.append(f"> 🚨 **{pct_no_policy:.0f}% sem política clara — risco de governança alto.**")
    md.append("")

    md.append("### Ferramentas de segurança ativas (S8-Q4, multi)")
    md.append("| Ferramenta | N | % |")
    md.append("|---|---|---|")
    for k, v in s8_q4.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 10 · Pain Points & Wishlist (S9, anonimizadas)")
    md.append("")
    if s9_pain:
        md.append("### Top frustrações (S9-Q1)")
        for q in s9_pain:
            md.append(f"> {q}")
            md.append("")
    if s9_change:
        md.append("### Top mudanças que dobrariam produtividade (S9-Q2)")
        for q in s9_change:
            md.append(f"> {q}")
            md.append("")
    if s9_wishlist:
        md.append("### Wishlist de features Microsoft/GitHub (S9-Q3)")
        for q in s9_wishlist:
            md.append(f"> {q}")
            md.append("")

    md.append("---")
    md.append("")
    md.append("## 11 · 🎯 Recomendações Priorizadas")
    md.append("")
    recs = []
    if pct_no_policy > 30:
        recs.append(("🔴 P0", "Documentar política formal de uso de IA", f"{pct_no_policy:.0f}% sem política"))
    if pct_coding_agent < 30:
        recs.append(("🟠 P1", "Workshop de Coding Agent (autônomo no GitHub.com)", f"apenas {pct_coding_agent:.0f}% conhece"))
    if pct_mcp < 20:
        recs.append(("🟠 P1", "Treinamento técnico avançado: MCP, A2A, custom agents", f"apenas {pct_mcp:.0f}% conhece MCP"))
    if pct_no_champion > 50:
        recs.append(("🟡 P2", "Formar Champions Network (3-5 devs por time)", f"{pct_no_champion:.0f}% sem Champion"))

    md.append("| Prioridade | Ação | Justificativa |")
    md.append("|---|---|---|")
    for pri, action, why in recs[:5]:
        md.append(f"| {pri} | {action} | {why} |")
    md.append("")
    md.append("> 💡 Para plano de capacitação detalhado com Champions, cohorts e calendário, rode também o **Learning & Growth Survey** (`survey-learning/`) e a skill `/plano-capacitacao`.")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 12 · 🔗 Conexão com Assessment de Maturidade")
    md.append("")
    md.append("Se você rodou o assessment principal, compare:")
    md.append("")
    md.append("| Dimensão (survey) | Capability (assessment) | Validar |")
    md.append("|---|---|---|")
    md.append("| **D2** Copilot Adoption | P1-C1 Assistentes IA | Score declarado vs. adoção real |")
    md.append("| **D3** MS/GH Tooling | P3-C3, P3-C5 | Sofisticação técnica |")
    md.append("| **D4** AI Dev Practices | P1-C2, P1-C8 | Práticas estruturadas |")
    md.append("| **D5** Agent Concepts | P3-C5 | Conhecimento avançado |")
    md.append("| **D6** Instructions | P1-C7 | Manutenção contexto IA |")
    md.append("| **D7** Best Practices | P1-C5, P1-C8 | Cultura de adoção |")
    md.append("| **D8** Security & Governance | P2-C4, P2-C10 | Governance real |")
    md.append("")
    md.append("> **Padrão clássico:** liderança avalia P1-C1 como L3, mas survey D2 mostra L1 → **dissonância** entre estratégia e prática.")
    md.append("")

    md.append("---")
    md.append("")
    md.append(f"*Relatório gerado pela skill `/insights-developer-survey` · Rubrica determinística v1.0 · {date}*")
    md.append(branding.md_footer())

    insights_path = out_dir / f"insights-developer-survey-{date}.md"
    insights_path.write_text("\n".join(md), encoding="utf-8")

    # Console summary
    print(f"\n✅ Outputs gerados:")
    print(f"   📊 {maturity_path.relative_to(kit) if maturity_path.is_relative_to(kit) else maturity_path}")
    print(f"   📄 {insights_path.relative_to(kit) if insights_path.is_relative_to(kit) else insights_path}")
    print(f"\n🎯 Maturidade do time: {overall:.2f} ({team['team_overall_label']}) — {n} respondentes")
    print(f"\n💡 Top insights:")
    for i, ins in enumerate(insights[:3], 1):
        # truncate for console
        short = ins.split("**")[1] if "**" in ins else ins[:50]
        print(f"   {i}. {short}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
