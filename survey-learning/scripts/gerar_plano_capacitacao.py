#!/usr/bin/env python3
"""Gera plano de capacitação personalizado a partir do Learning Survey.

Lê: survey-learning/respostas-learning.json (output de /importar-survey-learning)
Gera: saida/plano-capacitacao-<DATE>.md (12 seções, com nomes/emails dos inscritos)
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
KIT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(KIT / "relatorios" / "scripts"))
import branding

DIMENSION_NAMES = {
    "D2": "Copilot Adoption",
    "D3": "MS/GH Tooling Breadth",
    "D4": "AI Dev Practices",
    "D5": "Agent Concepts Mastery",
    "D6": "Instructions Maturity",
    "D7": "Best Practices",
    "D8": "Security & Governance",
}


def safe_pct(num, total):
    return round(100 * num / total, 1) if total > 0 else 0


def collect_l2_self_perception(respondents):
    """L2-Q1 → D2, L2-Q2 → D3, ..., L2-Q7 → D8 (auto-perception L0-L4)."""
    dist = {}
    for i, did in enumerate(["D2", "D3", "D4", "D5", "D6", "D7", "D8"], start=1):
        qid = f"L2-Q{i}"
        counts = Counter()
        for r in respondents:
            ans = r["responses"].get(qid, {}).get("value", "")
            if not ans: continue
            for level in ["L0", "L1", "L2", "L3", "L4"]:
                if ans.startswith(level):
                    counts[level] += 1
                    break
        dist[did] = counts
    return dist


def collect_priorities(respondents):
    """L3-Q1 multi: top 3 dimensões prioritárias."""
    counts = Counter()
    for r in respondents:
        ans = r["responses"].get("L3-Q1", {}).get("value", "")
        if not ans: continue
        for opt in str(ans).split(";"):
            opt = opt.strip()
            for did in DIMENSION_NAMES:
                if opt.startswith(did):
                    counts[did] += 1
                    break
    return counts


def collect_topics(respondents):
    """L4-Q1 to L4-Q5: all topics requested → counts + attendees."""
    topic_counts = Counter()
    topic_attendees = defaultdict(list)
    for r in respondents:
        for qid in ["L4-Q1", "L4-Q2", "L4-Q3", "L4-Q4", "L4-Q5"]:
            ans = r["responses"].get(qid, {}).get("value", "")
            if not ans: continue
            for topic in str(ans).split(";"):
                topic = topic.strip()
                if not topic: continue
                if "Já domino" in topic or "Não tenho interesse" in topic or "Não conheço" in topic:
                    continue
                topic_counts[topic] += 1
                topic_attendees[topic].append({
                    "name": r.get("name", "?"),
                    "email": r.get("email", "?"),
                })
    return topic_counts, topic_attendees


def collect_format_prefs(respondents):
    formats = Counter()
    time_per_week = Counter()
    cohort_pref = Counter()
    schedule = Counter()
    for r in respondents:
        for opt in str(r["responses"].get("L5-Q1", {}).get("value", "")).split(";"):
            opt = opt.strip()
            if opt: formats[opt] += 1
        time_per_week[r["responses"].get("L5-Q2", {}).get("value", "")] += 1
        for opt in str(r["responses"].get("L5-Q3", {}).get("value", "")).split(";"):
            opt = opt.strip()
            if opt: schedule[opt] += 1
        cohort_pref[r["responses"].get("L5-Q4", {}).get("value", "")] += 1
    return formats, time_per_week, cohort_pref, schedule


def collect_champions(respondents):
    actives, supported, maybe = [], [], []
    for r in respondents:
        ans = r["responses"].get("L6-Q1", {}).get("value", "")
        person = {"name": r.get("name", "?"), "email": r.get("email", "?")}
        if ans.startswith("Sim — quero ser Champion ativo"):
            actives.append(person)
        elif "Sim — mas só se" in ans:
            supported.append(person)
        elif ans.startswith("Talvez"):
            maybe.append(person)
    return actives, supported, maybe


def collect_mentors_mentees(respondents):
    mentees, mentors = [], []
    references = Counter()
    for r in respondents:
        person = {"name": r.get("name", "?"), "email": r.get("email", "?")}
        if "Sim" in r["responses"].get("L6-Q3", {}).get("value", ""):
            mentees.append(person)
        if "Sim" in r["responses"].get("L6-Q4", {}).get("value", ""):
            topic = r["responses"].get("L6-Q5", {}).get("value", "")
            mentors.append({**person, "topic": topic[:80] if topic else "(não especificou)"})
        ref = r["responses"].get("L6-Q2", {}).get("value", "").strip()
        if ref and len(ref) > 2 and "[" not in ref:
            references[ref] += 1
    return mentors, mentees, references


def collect_barriers(respondents):
    counts = Counter()
    for r in respondents:
        for opt in str(r["responses"].get("L7-Q1", {}).get("value", "")).split(";"):
            opt = opt.strip()
            if opt and "sem barreiras" not in opt.lower():
                counts[opt] += 1
    return counts


def collect_quotes(respondents, qid, max_q=5):
    quotes = []
    for r in respondents:
        v = r["responses"].get(qid, {}).get("value", "").strip()
        if v and len(v) > 15 and "[" not in v[:5]:
            quotes.append((v, r.get("name", "?")))
    return quotes[:max_q]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default=str(KIT / "survey-learning/respostas-learning.json"))
    ap.add_argument("--out", default=str(KIT / "saida"))
    args = ap.parse_args()

    inp = Path(args.input)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not inp.exists():
        print(f"❌ {inp} não encontrado. Rode /importar-survey-learning primeiro.")
        return 1

    data = json.loads(inp.read_text(encoding="utf-8"))
    respondents = data.get("respondents", [])
    n = len(respondents)
    date = datetime.date.today().isoformat()

    if n < 3:
        print(f"⚠ Apenas {n} respondentes. Plano será preliminar.")

    # Aggregations
    self_perception = collect_l2_self_perception(respondents)
    priorities = collect_priorities(respondents)
    topic_counts, topic_attendees = collect_topics(respondents)
    formats, time_per_week, cohort_pref, schedule = collect_format_prefs(respondents)
    actives, supported, maybe = collect_champions(respondents)
    mentors, mentees, references = collect_mentors_mentees(respondents)
    barriers = collect_barriers(respondents)
    pain_quotes = collect_quotes(respondents, "L7-Q4")
    workshop_wishes = collect_quotes(respondents, "L7-Q2")
    speaker_wishes = collect_quotes(respondents, "L7-Q3")
    why_growth = collect_quotes(respondents, "L3-Q2")

    # Build report
    md = []
    md.append(branding.md_header().rstrip())
    md.append("")
    md.append("# Plano de Capacitação IA — Roadmap Personalizado")
    md.append("")
    md.append(f"**Data:** {date}  ·  **Respondentes:** {n} (identificados)  ·  Survey: Learning & Growth (32 perguntas)")
    md.append(f"**Autor:** {branding.META_BAR}  ·  **Contato:** {branding.CONTACT}")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 1 · Sumário Executivo")
    md.append("")

    # Maturity self-perception per dimension (mediana)
    md.append("### Maturidade IA percebida pelo time (auto-avaliação L2)")
    md.append("")
    md.append("| Dimensão | L0 | L1 | L2 | L3 | L4 | Mediana |")
    md.append("|---|---|---|---|---|---|---|")
    for did, name in DIMENSION_NAMES.items():
        d = self_perception[did]
        l0, l1, l2, l3, l4 = d.get("L0", 0), d.get("L1", 0), d.get("L2", 0), d.get("L3", 0), d.get("L4", 0)
        # Compute median
        sorted_levels = []
        for lvl, cnt in [("L0", l0), ("L1", l1), ("L2", l2), ("L3", l3), ("L4", l4)]:
            sorted_levels.extend([lvl] * cnt)
        median = sorted_levels[len(sorted_levels) // 2] if sorted_levels else "—"
        md.append(f"| **{did}** {name} | {l0} | {l1} | {l2} | {l3} | {l4} | {median} |")
    md.append("")

    # Top priorities
    md.append("### 🎯 Top 3 dimensões PRIORITÁRIAS para crescer (L3-Q1)")
    md.append("")
    for did, count in priorities.most_common(3):
        md.append(f"- **{did}** {DIMENSION_NAMES[did]} — {count}/{n} devs ({safe_pct(count, n):.0f}%)")
    md.append("")

    # Top topics
    md.append("### 📚 Top 10 tópicos mais demandados (L4)")
    md.append("")
    for i, (topic, count) in enumerate(topic_counts.most_common(10), 1):
        md.append(f"{i}. **{topic}** — {count} devs ({safe_pct(count, n):.0f}%)")
    md.append("")

    # Champions
    md.append("### 👥 Champions Network identificados")
    md.append("")
    md.append(f"- **{len(actives)} ativos** (querem ser Champion sem precisar suporte)")
    md.append(f"- **{len(supported)} com suporte** (querem ser Champion se tiver treino)")
    md.append(f"- **{len(maybe)} maybe** (precisam pensar)")
    if references:
        md.append(f"- **Top 3 referências naturais** (mencionados por colegas em L6-Q2):")
        for name, count in references.most_common(3):
            md.append(f"  - {name} (mencionado por {count} pessoas)")
    md.append("")

    # 3 quick wins
    md.append("### ⚡ 3 quick wins recomendados (próximos 30 dias)")
    md.append("")
    if topic_counts:
        top_topic, top_count = topic_counts.most_common(1)[0]
        md.append(f"1. **Workshop: {top_topic}** — {top_count} inscritos pré-validados")
    if actives:
        md.append(f"2. **Champions Kickoff** — ativar os {len(actives)} Champions ativos identificados")
    if barriers:
        top_barrier = barriers.most_common(1)[0]
        md.append(f"3. **Remover barreira #1: '{top_barrier[0]}'** — citada por {top_barrier[1]}/{n} devs")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 2 · Top 10 tópicos demandados (com inscritos pré-validados)")
    md.append("")
    for i, (topic, count) in enumerate(topic_counts.most_common(10), 1):
        md.append(f"### {i}. {topic} — {count} inscritos")
        md.append("")
        md.append(f"**Demanda:** {count}/{n} devs ({safe_pct(count, n):.0f}%)")
        md.append("")
        md.append("**Inscritos pré-validados** (já confirmados na resposta):")
        for att in topic_attendees[topic]:
            md.append(f"- {att['name']} ({att['email']})")
        md.append("")

    md.append("---")
    md.append("")
    md.append("## 3 · Cohorts sugeridos por dimensão da rubrica")
    md.append("")
    for did, name in DIMENSION_NAMES.items():
        n_priority = priorities.get(did, 0)
        if n_priority == 0:
            continue
        md.append(f"### Cohort {did} ({name})")
        md.append(f"- **{n_priority} devs querem evoluir nesta dimensão**")
        cohort_winning = cohort_pref.most_common(1)[0][0] if cohort_pref else "Híbrido"
        md.append(f"- **Formato preferido pelo time:** {cohort_winning}")
        md.append(f"- **Plano:** cohort de 4-6 semanas com sessões síncronas + lab self-paced")
        md.append("")

    md.append("---")
    md.append("")
    md.append("## 4 · Champions Network (3 tiers)")
    md.append("")
    md.append("### 🥇 Ativos (já querem ser Champion)")
    if actives:
        md.append("| Nome | Email | Próximo passo |")
        md.append("|---|---|---|")
        for c in actives:
            md.append(f"| {c['name']} | {c['email']} | Convidar para train-the-trainer |")
    else:
        md.append("_Nenhum dev se candidatou diretamente. Considere ativar tier 'com suporte'._")
    md.append("")

    md.append("### 🥈 Com suporte (querem se tiver treino dedicado)")
    if supported:
        md.append("| Nome | Email | Suporte necessário |")
        md.append("|---|---|---|")
        for c in supported:
            md.append(f"| {c['name']} | {c['email']} | Workshop de capacitação Champion + materiais |")
    else:
        md.append("_(nenhum)_")
    md.append("")

    md.append("### 🤝 Mentor candidates (se ofereceram em L6-Q4)")
    if mentors:
        md.append("| Nome | Email | Tópico que ensina |")
        md.append("|---|---|---|")
        for m in mentors:
            md.append(f"| {m['name']} | {m['email']} | {m['topic']} |")
    md.append("")

    md.append("### 🎓 Mentees (querem mentoria 1:1)")
    if mentees:
        md.append("| Nome | Email |")
        md.append("|---|---|")
        for m in mentees:
            md.append(f"| {m['name']} | {m['email']} |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 5 · Calendário sugerido (próximos 90 dias)")
    md.append("")
    md.append("| Semana | Workshop | Audiência | Champion | Formato |")
    md.append("|---|---|---|---|---|")
    md.append(f"| W1 | Champions Kickoff | {len(actives) + len(supported)} | Líder Eng | 2h síncrono |")
    if topic_counts:
        top3 = topic_counts.most_common(3)
        for i, (topic, count) in enumerate(top3, 2):
            champion_name = actives[0]["name"] if actives else "TBD"
            md.append(f"| W{i} | {topic} | {count} | {champion_name} | 4h hands-on |")
    md.append("| W4 | Office hours #1 | Todos | Champions | 1h Q&A |")
    md.append("| W6, W8, W10, W12 | Office hours quinzenal | Todos | Champions | 1h Q&A |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 6 · Formato e cadência preferidos")
    md.append("")
    md.append("### Formatos (top 5 — L5-Q1 multi)")
    md.append("| Formato | N | % |")
    md.append("|---|---|---|")
    for k, v in formats.most_common(5):
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")
    md.append("### Tempo disponível por semana (L5-Q2)")
    md.append("| Tempo | N | % |")
    md.append("|---|---|---|")
    for k, v in time_per_week.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")
    md.append("### Cohort vs self-paced (L5-Q4)")
    md.append("| Preferência | N | % |")
    md.append("|---|---|---|")
    for k, v in cohort_pref.most_common():
        md.append(f"| {k} | {v} | {safe_pct(v, n):.0f}% |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 7 · Barreiras a remover (priorizado)")
    md.append("")
    md.append("| Barreira | Devs afetados | % | Ação sugerida |")
    md.append("|---|---|---|---|")
    actions = {
        "Falta de tempo": "Bloquear 2h/sem no calendário",
        "Falta de licença Copilot": "Revisar licenças com TI, target 100%",
        "Falta de Champion no time": "Ativar Champions Network identificados",
        "Não sei por onde começar": "Criar learning path em Copilot Space",
    }
    for barrier, count in barriers.most_common(8):
        action = "Discutir com líder"
        for k, v in actions.items():
            if k.lower() in barrier.lower():
                action = v
                break
        md.append(f"| {barrier} | {count} | {safe_pct(count, n):.0f}% | {action} |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 8 · Wishlist do time")
    md.append("")
    if workshop_wishes:
        md.append("### Workshops sugeridos pelo time (L7-Q2)")
        for q, name in workshop_wishes:
            md.append(f"> _\"{q}\"_ — sugerido por {name}")
            md.append("")
    if speaker_wishes:
        md.append("### Palestrantes externos sugeridos (L7-Q3)")
        for q, name in speaker_wishes:
            md.append(f"> _\"{q}\"_ — sugerido por {name}")
            md.append("")
    if pain_quotes:
        md.append("### Outras sugestões (L7-Q4)")
        for q, name in pain_quotes[:3]:
            md.append(f"> _\"{q}\"_ — {name}")
            md.append("")

    md.append("---")
    md.append("")
    md.append("## 9 · 🔗 Conexão com outros surveys")
    md.append("")
    md.append("Se você rodou também o **Developer Survey** (anônimo) e o **Assessment principal**, compare:")
    md.append("")
    md.append("| Dimensão | Auto-perception (este survey, L2) | Rubrica medida (survey-devs, D-X) | Capability assessment |")
    md.append("|---|---|---|---|")
    for did, name in DIMENSION_NAMES.items():
        d = self_perception[did]
        sorted_levels = []
        for lvl, cnt in [("L0", d.get("L0", 0)), ("L1", d.get("L1", 0)),
                         ("L2", d.get("L2", 0)), ("L3", d.get("L3", 0)),
                         ("L4", d.get("L4", 0))]:
            sorted_levels.extend([lvl] * cnt)
        median = sorted_levels[len(sorted_levels) // 2] if sorted_levels else "—"
        md.append(f"| {did} {name} | mediana {median} | (rodar /insights-developer-survey) | (rodar /calcular-scores) |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 10 · 🎯 Top 5 ações priorizadas (impacto × facilidade)")
    md.append("")
    actions_ranked = []
    if topic_counts:
        top_topic, top_count = topic_counts.most_common(1)[0]
        actions_ranked.append((f"Workshop: {top_topic}", f"{top_count} inscritos pré-validados", "30 dias"))
    if actives:
        actions_ranked.append(("Champions Kickoff", f"{len(actives)} Champions ativos identificados", "30 dias"))
    if barriers:
        top_barrier = barriers.most_common(1)[0]
        actions_ranked.append((f"Remover barreira: {top_barrier[0]}", f"{top_barrier[1]} devs afetados", "60 dias"))
    if mentors and mentees:
        actions_ranked.append((f"Programa de mentoria 1:1", f"{len(mentors)} mentores × {len(mentees)} mentees", "60 dias"))
    actions_ranked.append(("Office hours quinzenal", "Atende todas as barreiras de baixa adoção", "Contínuo a partir de W2"))

    md.append("| # | Ação | Impacto | Horizonte |")
    md.append("|---|---|---|---|")
    for i, (action, impact, horizon) in enumerate(actions_ranked[:5], 1):
        md.append(f"| {i} | {action} | {impact} | {horizon} |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 11 · 📅 Cronograma 30 dias")
    md.append("")
    md.append("| Semana | Atividades |")
    md.append("|---|---|")
    md.append(f"| **W1** | Champions Kickoff ({len(actives)} pessoas) + agendamento de workshops |")
    if topic_counts:
        top_topic = topic_counts.most_common(1)[0][0]
        md.append(f"| **W2** | Workshop {top_topic} ({topic_counts.most_common(1)[0][1]} inscritos) |")
    md.append("| **W3** | Office hours #1 + remoção de barreira top |")
    md.append("| **W4** | Retrospectiva + revisão do plano |")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## 12 · 📋 Apêndice — Respondentes (para liderança usar para convites)")
    md.append("")
    md.append("> ⚠️ Esta tabela contém nomes/emails. **NÃO compartilhar publicamente** — só usar para convites de workshops.")
    md.append("")
    md.append("| Nome | Email | Quer Champion? |")
    md.append("|---|---|---|")
    for r in respondents:
        name = r.get("name", "?")
        email = r.get("email", "?")
        ch_ans = r["responses"].get("L6-Q1", {}).get("value", "")
        ch_short = "Sim ativo" if "Sim — quero" in ch_ans else "Sim com suporte" if "Sim — mas" in ch_ans else "Não"
        md.append(f"| {name} | {email} | {ch_short} |")
    md.append("")

    md.append("---")
    md.append("")
    md.append(f"*Plano gerado pela skill `/plano-capacitacao` · {date} · Sobrescreva editando manualmente o .md*")
    md.append(branding.md_footer())

    out_path = out_dir / f"plano-capacitacao-{date}.md"
    out_path.write_text("\n".join(md), encoding="utf-8")

    # Console summary
    print(f"\n✅ Plano de capacitação → {out_path.relative_to(KIT) if out_path.is_relative_to(KIT) else out_path}")
    print(f"\n📊 {n} respondentes IDENTIFICADOS")
    if topic_counts:
        print(f"\n📚 Top 3 tópicos demandados:")
        for i, (t, c) in enumerate(topic_counts.most_common(3), 1):
            print(f"   {i}. {t[:60]} — {c} inscritos")
    print(f"\n👥 Champions: {len(actives)} ativos · {len(supported)} com suporte · {len(maybe)} maybe")
    print(f"\n🎓 Mentor pairs: {len(mentors)} mentores · {len(mentees)} mentees")
    if barriers:
        print(f"\n⚠ Top barreira: {barriers.most_common(1)[0][0]} ({barriers.most_common(1)[0][1]}/{n} devs)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
