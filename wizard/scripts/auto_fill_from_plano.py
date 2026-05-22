#!/usr/bin/env python3
"""Mode D do wizard: auto-fill implementation-guide-inputs.json a partir do plano-capacitacao.

Lê: saida/plano-capacitacao-<DATE>.md (output de /plano-capacitacao)
Extrai: Champions, training, calendário, ADKAR-knowledge, quick wins
Gera: implementation-guide-inputs.json (na raiz do kit) com 6 dos 9 campos preenchidos

Uso:
    python3 auto_fill_from_plano.py
    python3 auto_fill_from_plano.py --plano X --out Y
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
KIT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(KIT / "relatorios" / "scripts"))
import branding


def find_latest_plano(out_dir: Path) -> Path | None:
    """Find the most recent plano-capacitacao-*.md in saida/."""
    candidates = sorted(out_dir.glob("plano-capacitacao-*.md"), reverse=True)
    return candidates[0] if candidates else None


def extract_section(plano_md: str, section_header_pattern: str) -> str:
    """Extract content of a section by header regex (until next ## or end)."""
    pat = re.compile(
        rf"## {section_header_pattern}.*?\n(.*?)(?=\n## |\Z)",
        re.DOTALL,
    )
    m = pat.search(plano_md)
    return m.group(1).strip() if m else ""


def extract_champions_active(plano_md: str) -> str:
    """Extract Active Champions table from section 4."""
    section = extract_section(plano_md, r"4 · Champions Network")
    # Find the "Ativos" subsection table
    active_block = re.search(
        r"### 🥇 Ativos.*?\n(.*?)(?=\n### |\Z)",
        section,
        re.DOTALL,
    )
    if not active_block:
        return ""
    block = active_block.group(1)
    # Extract names from table (column 1 between |)
    names = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|@]+@[^|\s]+)\s*\|", block, re.MULTILINE)
    if not names:
        return ""
    lines = ["Comitê Executivo Diretivo (Champions ativos identificados pelo Learning Survey):", ""]
    for name, email in names:
        if name.strip().lower() not in ("nome", "---"):
            lines.append(f"- {name.strip()} — {email.strip()}")
    return "\n".join(lines)


def extract_calendar(plano_md: str) -> str:
    """Extract calendar from section 5 (próximos 90 dias)."""
    section = extract_section(plano_md, r"5 · Calendário sugerido")
    if not section:
        return ""
    # Return as markdown table (already in plano)
    table_match = re.search(r"\|.*?\|.*?(?=\n\n|\Z)", section, re.DOTALL)
    return table_match.group(0).strip() if table_match else section[:500]


def extract_top_topics(plano_md: str, n=5) -> list[tuple[str, int]]:
    """Extract top topics from sumário (top 10 listed as 1. **topic** — N devs)."""
    section = extract_section(plano_md, r"1 · Sumário Executivo")
    matches = re.findall(r"^\d+\.\s+\*\*(.+?)\*\* — (\d+) devs", section, re.MULTILINE)
    return [(m[0], int(m[1])) for m in matches[:n]]


def extract_format_prefs(plano_md: str) -> str:
    """Extract format preferences from section 6."""
    section = extract_section(plano_md, r"6 · Formato e cadência")
    table_match = re.search(r"### Formatos.*?\n(\|.*?\n(?:\|.*?\n)+)", section, re.DOTALL)
    return table_match.group(1).strip() if table_match else ""


def extract_barriers(plano_md: str) -> str:
    """Extract top barriers from section 7."""
    section = extract_section(plano_md, r"7 · Barreiras")
    table_match = re.search(r"\|.*?\n(?:\|[-: ]+\|\n)?(\|.*?\n)+", section)
    return table_match.group(0).strip() if table_match else ""


def extract_quick_wins_calendar(plano_md: str, weeks_range: tuple[int, int]) -> str:
    """Extract quick wins for a week range from section 11 (cronograma 30 dias) + section 5."""
    section_5 = extract_section(plano_md, r"5 · Calendário sugerido")
    section_11 = extract_section(plano_md, r"11 · Cronograma")

    items = []
    for src in [section_5, section_11]:
        for line in src.split("\n"):
            # Extract W{N} entries
            m = re.search(r"W(\d+)[,\-\s]+W?(\d+)?\s*\|([^|]+)\|", line)
            if m:
                start_week = int(m.group(1))
                if weeks_range[0] <= start_week <= weeks_range[1]:
                    activity = m.group(3).strip()
                    if activity and activity != "Workshop":
                        items.append(f"- W{start_week}: {activity}")
    return "\n".join(items) if items else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plano", default=None, help="Path to plano-capacitacao-DATE.md (default: latest in saida/)")
    ap.add_argument("--out", default=str(KIT / "implementation-guide-inputs.json"))
    args = ap.parse_args()

    out_path = Path(args.out)

    if args.plano:
        plano_path = Path(args.plano)
    else:
        plano_path = find_latest_plano(KIT / "saida")

    if not plano_path or not plano_path.exists():
        print(f"❌ Plano de capacitação não encontrado em saida/.")
        print(f"   Rode /plano-capacitacao primeiro (após /importar-survey-learning).")
        return 1

    plano_md = plano_path.read_text(encoding="utf-8")
    print(f"📖 Lendo: {plano_path.relative_to(KIT) if plano_path.is_relative_to(KIT) else plano_path}")

    # Extract sections
    champions = extract_champions_active(plano_md)
    calendar = extract_calendar(plano_md)
    formats = extract_format_prefs(plano_md)
    barriers = extract_barriers(plano_md)
    top_topics = extract_top_topics(plano_md)
    quick_w1_4 = extract_quick_wins_calendar(plano_md, (1, 4))
    quick_w5_8 = extract_quick_wins_calendar(plano_md, (5, 8))
    quick_w9_12 = extract_quick_wins_calendar(plano_md, (9, 12))

    # Build communication_plan from formats
    comm_plan = "Plano de Comunicação derivado do calendário sugerido:\n\n"
    comm_plan += calendar if calendar else "(ver Parte 5 do plano de capacitação)"

    # Build training_plan from cohorts (section 3)
    cohorts_section = extract_section(plano_md, r"3 · Cohorts sugeridos")
    training = "Plano de Treinamento (cohorts por dimensão derivados do Learning Survey):\n\n"
    training += cohorts_section[:1500] if cohorts_section else "(ver Parte 3 do plano de capacitação)"

    # Build ADKAR notes — Knowledge stage uses top topics
    adkar = """Plano de Mudança ADKAR derivado do Learning Survey:

**Awareness:** Comunicar plano de capacitação consolidado em all-hands; cada dev recebe seu plano personalizado por email.

**Desire:** Tornar visível que workshops têm inscritos pré-validados (não opt-in genérico).

**Knowledge:** Workshops top 5 (do Learning Survey):
"""
    for i, (topic, count) in enumerate(top_topics[:5], 1):
        adkar += f"{i}. {topic} ({count} inscritos)\n"
    adkar += """
**Ability:** Office hours quinzenal (sem agenda fixa, devs trazem dúvidas práticas).

**Reinforcement:** Métricas de adoção mensais publicadas; reconhecimento dos Champions; revisão trimestral do plano com novo Learning Survey.
"""

    # Compose JSON
    payload = {
        "metadata": {
            "generated_at": datetime.datetime.now(datetime.UTC).isoformat(),
            "generator": "wizard/scripts/auto_fill_from_plano.py (Mode D)",
            "source_plano": str(plano_path.name),
            "completion_pct": 67,  # 6 dos 9 campos preenchidos
            "manual_required": ["tpo", "raci_matrix"],
            **branding.json_metadata(),
        },
        "implementation_guide_inputs": {
            "executive_steering_committee": champions or "(preencher manualmente — sem Champions ativos identificados pelo Learning Survey)",
            "tpo": "(preencher manualmente — Learning Survey não cobre TPO. Liste Programa Manager + escritório + autoridade de decisão)",
            "raci_matrix": "(preencher manualmente — Learning Survey não cobre RACI. Use template em wizard/implementation-guide-inputs.template.json)",
            "communication_plan": comm_plan,
            "training_plan": training,
            "adkar_notes": adkar,
            "quick_wins_w1_4": quick_w1_4 or "(preencher — sem dados suficientes nas semanas 1-4 do calendário)",
            "quick_wins_w5_8": quick_w5_8 or "(preencher — sem dados suficientes nas semanas 5-8)",
            "quick_wins_w9_12": quick_w9_12 or "(preencher — sem dados suficientes nas semanas 9-12)",
        },
    }

    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✅ Mode D auto-fill → {out_path.relative_to(KIT) if out_path.is_relative_to(KIT) else out_path}")
    print(f"\n📊 Preenchimento automático:")
    print(f"   ✓ executive_steering_committee  (Champions ativos)")
    print(f"   ✓ communication_plan            (Calendário)")
    print(f"   ✓ training_plan                 (Cohorts por dimensão)")
    print(f"   ✓ adkar_notes                   (Knowledge = Top 5 workshops)")
    print(f"   ✓ quick_wins_w1_4 / w5_8 / w9_12 (Cronograma)")
    print(f"\n⚠ Você precisa preencher MANUALMENTE (Learning Survey não cobre):")
    print(f"   • tpo (Technology Product Owner)")
    print(f"   • raci_matrix")
    print(f"\n💡 Próximo: /gerar-relatorio  → 5 PDFs com Parte 4 personalizada")
    return 0


if __name__ == "__main__":
    sys.exit(main())
