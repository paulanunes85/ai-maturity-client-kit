---
name: insights-developer-survey
description: Generates aggregated insights report from imported Developer Survey responses. Reads survey-devs/respostas-devs.json and produces saida/insights-developer-survey-<DATE>.md with: respondent demographics, Copilot adoption + mode usage, agent/MCP awareness, governance gaps, pain points (anonymized quotes), and prioritized recommendations linked to the maturity assessment capabilities (P1-C1, P1-C5, P1-C8, P2-C4, P3-C6). Use after /importar-survey-devs.
---

# Skill: Generate Developer Survey Insights Report

## When to use
- After `/importar-survey-devs` (depends on `survey-devs/respostas-devs.json`)
- When the team wants to see aggregated insights from the developer survey
- To inform `/wizard-implementacao` (Implementation Guide of the maturity assessment) with real developer voice

## Inputs
- `survey-devs/respostas-devs.json` — all respondents and answers (output of `/importar-survey-devs`)
- `survey-devs/perguntas-para-forms-devs.md` — schema reference (for question text + types)
- `survey-devs/scripts/calcular_maturidade.py` — **invoke first** to compute team maturity scores per dimension (D2-D8) using deterministic rubric. Output: `saida/maturidade-developer-survey-<DATE>.json`
- `survey-devs/RUBRICA-MATURIDADE.md` — rubric documentation (read for explanations to include in the report)
- (optional) `saida/scores.json` — to cross-reference with maturity assessment scores (P1-C1, etc.)

## Expected output
- `saida/insights-developer-survey-<DATE>.md` — full report (PT-BR) with sections, tables, charts (ASCII), citations
- Brief chat summary (PT-BR): N respondents, top 3 insights, top 3 gaps

## Procedure

### Implementation: invoke the official script

The skill should INVOKE the script that does both maturity calculation AND insights generation in one go:

```bash
python3 survey-devs/scripts/gerar_insights.py
```

This script:
1. Loads `survey-devs/respostas-devs.json`
2. Computes maturity per respondent + aggregates team scores via `rubric.py`
3. Generates descriptive aggregations (% adoption, top tools, pain quotes)
4. Outputs:
   - `saida/maturidade-developer-survey-<DATE>.json` (rubric scores)
   - `saida/insights-developer-survey-<DATE>.md` (12-section report PT-BR)

**DO NOT reimplement aggregation in chat** — the script handles all of it deterministically.

### Optional: maturity only (without report)

If user wants just the maturity scores (without the full report):

```bash
python3 survey-devs/scripts/calcular_maturidade.py
# Output: saida/maturidade-developer-survey-<DATE>.json only
```

### 1. Load and validate

```python
import json
from pathlib import Path
KIT = Path.cwd()

data = json.load(open(KIT / "survey-devs/respostas-devs.json"))
maturity = json.load(open(KIT / f"saida/maturidade-developer-survey-{date}.json"))
n = data["metadata"]["total_respondents"]
if n < 3:
    warn(f"Apenas {n} respondentes — insights pouco confiáveis. Recomendado ≥5.")
```

### 2. Compute aggregations per question

For each question, group answers and count:

```python
from collections import Counter

def aggregate(qid, q_type):
    """Returns ordered list of (option, count, percent)."""
    counts = Counter()
    total = 0
    for r in data["respondents"]:
        if qid not in r["responses"]:
            continue
        val = r["responses"][qid]["value"]
        if q_type == "multi":
            for opt in val.split(";"):
                counts[opt.strip()] += 1
                total += 1
        elif q_type == "text":
            continue  # quotes handled separately
        else:  # choice
            counts[val] += 1
            total += 1
    return sorted(
        [(opt, n, round(100 * n / total, 1) if total else 0) for opt, n in counts.items()],
        key=lambda x: x[1],
        reverse=True,
    )
```

### 3. Generate ASCII bar charts

```python
def bar(pct, width=30):
    filled = int(round(pct * width / 100))
    return "█" * filled + "░" * (width - filled)
```

### 4. Build the report

Structure (PT-BR):

```markdown
# Developer Survey — Relatório de Insights

**Data:** {date}
**Respondentes:** {n} (anônimos)
**Cobertura:** {pct}% das questões respondidas em média

{#if n < 5}
> ⚠️ Apenas {n} respondentes — insights são preliminares. Considere buscar mais respostas (recomendado ≥15 para representatividade do time).
{/if}

---

## 1 · Sumário Executivo

### 🎯 Maturidade IA do Time (rubrica determinística)

> **Overall: {team_overall_score} ({team_overall_label})**
> Baseado em {n_respondents} respondentes, 7 dimensões, escala L0-L4 (mesma do assessment de maturidade).

| Dimensão | Score | Rótulo | % devs em L3+L4 |
|---|---|---|---|
| D2 Copilot Adoption | {d2.team_score} | {d2.label} | {d2.pct_l3_l4}% |
| D3 MS/GH Tooling Breadth | {d3.team_score} | {d3.label} | {d3.pct_l3_l4}% |
| D4 AI Dev Practices | {d4.team_score} | {d4.label} | {d4.pct_l3_l4}% |
| D5 Agent Concepts Mastery | {d5.team_score} | {d5.label} | {d5.pct_l3_l4}% |
| D6 Instructions Maturity | {d6.team_score} | {d6.label} | {d6.pct_l3_l4}% |
| D7 Best Practices | {d7.team_score} | {d7.label} | {d7.pct_l3_l4}% |
| D8 Security & Governance | {d8.team_score} | {d8.label} | {d8.pct_l3_l4}% |

### 🏆 3 dimensões mais fortes
- {ranking.top_1}: {score}
- {ranking.top_2}: {score}
- {ranking.top_3}: {score}

### ⚠️ 3 maiores gaps (oportunidades de roadmap)
- 🔴 {ranking.bottom_1}: {score} — {ação sugerida}
- 🟠 {ranking.bottom_2}: {score} — {ação sugerida}
- 🟡 {ranking.bottom_3}: {score} — {ação sugerida}

### 3 insights principais
- {insight_1 — gerado de maturity + descritivos}
- {insight_2}
- {insight_3}

---

## 2 · Quem respondeu (S1 - Perfil)

### Distribuição por cargo
| Cargo | N | % | Visual |
|---|---|---|---|
| Backend | 4 | 33% | █████████░░ |
| Frontend | 3 | 25% | ██████░░░░░ |
| ...

### Tempo de experiência
{tabela}

### Stack
{tabela}

---

## 3 · GitHub Copilot — Adoção (S2)

### Cobertura de licenças
| Tipo | N | % |
| Enterprise | 5 | 42% |
| Business | 3 | 25% |
| Pro (individual) | 2 | 17% |
| Free | 1 | 8% |
| Sem licença | 1 | 8% |

### Frequência de uso (S2-Q2)
{tabela}

### 🆕 Modos do Copilot Chat — quem usa o quê (S2-Q3)
| Modo | N usuários | % | Visual |
|---|---|---|---|
| Ask | 10 | 83% | ████████████████░░░░ |
| Edit | 8 | 67% | █████████████░░░░░░░ |
| Agent | 6 | 50% | ██████████░░░░░░░░░░ |
| Workspace | 3 | 25% | █████░░░░░░░░░░░░░░░ |
| Plan | 1 | 8% | ██░░░░░░░░░░░░░░░░░░ |
| **Não conhece** | 2 | 17% | ⚠️ |

**Insight:** {ex.: "50% já usa modo Agent — alta sofisticação para um time desse tamanho"}

### Modo MAIS usado (S2-Q4)
{tabela}

### Features ativas (S2-Q5)
{tabela top 5}

### Onde usam (S2-Q6)
{tabela}

### Ganho percebido (S2-Q7)
{tabela}

### Onde Copilot mais ajuda vs. NÃO ajuda
- ✅ Top 3 tarefas que Copilot acelera
- ❌ Top 3 onde NÃO ajuda (baseado em S2-Q9 quotes)

---

## 4 · Outras ferramentas Microsoft (S3)

### Adoção (% que usa)
| Ferramenta | N | % |
| GitHub Codespaces | ... |
| GitHub Advanced Security | ... |
| Azure OpenAI direto | ... |
| Azure AI Foundry | ... |
| Microsoft 365 Copilot | ... |

### Spec Kit / GitHub Models
{conhecimento}

---

## 5 · Práticas de Desenvolvimento com IA (S4)

### TDD com IA (S4-Q1)
{tabela}

### SDD — conhecimento (S4-Q2)
{tabela}

### Quando consultam IA (S4-Q3) — multi-select
{tabela}

### Trate IA como pair? (S4-Q4)
{tabela}

### Onboarding com IA (S4-Q8)
{tabela}

### Práticas que mudaram produtividade (S4-Q9 — quotes anonimizadas)
> "{quote 1}"
> "{quote 2}"
> "{quote 3}"

---

## 6 · Conceitos e Estrutura de Agentes (S5)

### Conhecimento de conceitos
| Conceito | Conhece+usa | Conhece | Não conhece |
|---|---|---|---|
| AI agent (vs assistant) | 4 | 5 | 3 |
| Modos Ask/Edit/Agent | 6 | 4 | 2 |
| Custom agents (.agent.md) | 2 | 4 | 6 |
| Custom skills (SKILL.md) | 1 | 3 | 8 |
| Prompt files (.prompt.md) | 3 | 4 | 5 |
| MCP (Model Context Protocol) | 1 | 5 | 6 |
| Handoffs entre agentes | 0 | 3 | 9 |
| Subagentes | 0 | 4 | 8 |

**Gap principal:** {ex.: "Conceitos avançados (MCP, handoffs, subagentes) são desconhecidos por >70% — oportunidade de workshop"}

### Primitivos JÁ CRIADOS (S5-Q9)
{tabela do que cada um já criou}

---

## 7 · Markdown / Memory / Instructions (S6)

### Quem usa instructions files (S6-Q1)
{tabela}

### Quem mantém (S6-Q2)
{tabela}

### Frequência de update (S6-Q3)
{tabela com alerta se "nunca" > 30%}

### Conteúdo dos instructions (S6-Q4)
{top 3}

### Prompt library compartilhada (S6-Q5)
{tabela}

---

## 8 · Usabilidade e Best Practices (S7)

### Como aprenderam (S7-Q1)
{top 3}

### Tem Champion no time? (S7-Q2)
{distribuição}

### Métricas de produtividade (S7-Q4)
{tabela}

### Iterações típicas (S7-Q5)
{tabela}

### Confiança em código IA sem revisão (S7-Q6)
{tabela com alerta se "quase sempre" > 30%}

### Hallucinations detectadas (S7-Q7)
{tabela}

### Aprendizado: mais ou menos? (S7-Q8)
{tabela}

---

## 9 · 🔒 Segurança e Governança (S8)

### Política documentada (S8-Q1)
{tabela com alerta se "não temos" > 30%}

### Conhecimento dos dados sensíveis (S8-Q2)
{tabela}

### Ferramentas de segurança ativas (S8-Q4)
{cobertura por ferramenta}

### Code Scanning em código IA (S8-Q5)
{tabela}

### SBOM (S8-Q6)
{tabela}

### Review formal de código IA (S8-Q7)
{tabela}

### DLP / Audit / Treinamento (S8-Q8 a Q10)
{tabela consolidada}

### Vulnerabilidades em código IA (S8-Q11)
{tabela}

**Score de Governança:** {0-100 baseado em respostas}
{interpretação}

---

## 10 · Pain Points & Wishlist (S9)

### Top 5 frustrações (S9-Q1, anonimizadas)
1. > "{quote 1}"
2. > "{quote 2}"
...

### Top 3 mudanças que dobrariam produtividade (S9-Q2)
1. > "{quote}"
...

### Top 3 features desejadas (S9-Q3)
1. > "{quote}"
...

---

## 11 · 🎯 Recomendações Priorizadas

Baseadas nos gaps acima, ranqueadas por impacto × facilidade.

### Quick wins (próximos 30 dias)
1. **{ação}** — atende {N respondentes} que mencionaram {gap}
2. ...

### Próximo trimestre
1. ...

### Estratégico (semestre)
1. ...

---

## 12 · 🔗 Conexão com o Assessment de Maturidade

Se você rodou o assessment principal (`/calcular-scores`), as respostas deste survey se relacionam:

| Capability do assessment | Sinal deste survey | O que isso significa |
|---|---|---|
| **P1-C1** Assistentes de Codificação IA | S2-Q1 (% com licença), S2-Q2 (frequência), S2-Q7 (ganho) | Score real vs. percepção da liderança |
| **P1-C5** Onboarding e Treinamento | S7-Q1 (como aprenderam), S7-Q2 (Champions) | Eficácia do programa de capacitação |
| **P1-C8** Medição de Produtividade | S7-Q4 (DORA/DX/SPACE) | Maturidade de medição |
| **P2-C4** DevSecOps | S8-Q4, S8-Q5, S8-Q11 | Cobertura real de scanners |
| **P3-C5** Aplicações Agênticas | S5-Q3 (custom agents), S5-Q6 (MCP) | Sofisticação técnica em IA |

**Recomendação:** se um capability do assessment está L3+ mas o survey mostra adoção fraca, há **dissonância entre liderança e prática** — investigar.

---

## Apêndice — Dados brutos

- Total de respondentes: {n}
- Cobertura média: {pct}%
- Gerado: {ISO date}
- Source: `survey-devs/respostas-devs.json`
- Importado de: {original_file}
```

### 5. Build "3 insights principais" automaticamente

Use heuristics:
- **Insight de adoção:** "X% usa Copilot diariamente, Y% só semanal" — destaca padrão dominante
- **Insight de modo:** "Modo MAIS usado é {X}, Y% nunca testou modo {Z}" — gap de exploração
- **Insight de conceito:** "Apenas X% conhece {conceito Y}" se < 30% — oportunidade
- **Insight de governance:** "X% não tem política de IA" se sem política > 50% — risco

### 6. Build "3 gaps" automaticamente

Use thresholds:
- 🔴 P0 (Crítico): governança ausente (S8-Q1 "não temos" > 50%) OU vulnerabilidade frequente (S8-Q11 "diariamente"+"semanalmente" > 30%)
- 🟠 P1 (Alto): conceitos desconhecidos (MCP/handoffs > 70% "não conhece") OU instructions inexistentes (S6-Q1 "nenhum" > 50%)
- 🟡 P2 (Médio): adoção parcial (S2-Q2 "raro" + "nunca" > 40%) OU sem Champion (S7-Q2 "não tem" > 50%)

## Report in chat (PT-BR)

```
✓ Maturidade calculada → saida/maturidade-developer-survey-2026-05-08.json
✓ Insights gerados → saida/insights-developer-survey-2026-05-08.md (~14 páginas eq.)

🎯 MATURIDADE DO TIME: 2.22 (L2 — Definido)
   Baseado em 12 respondentes anônimos, 7 dimensões, rubrica determinística

📊 Por dimensão:
   D2 Copilot Adoption       0.80  L1 (40% L0, 40% L1)  ⚠️
   D3 MS/GH Tooling          2.40  L2
   D4 AI Dev Practices       2.68  L3
   D5 Agent Concepts         2.56  L3
   D6 Instructions           2.31  L2
   D7 Best Practices         2.91  L3 ✨
   D8 Security & Governance  1.92  L2

🏆 Pontos fortes: D7 (Best Practices) · D4 (AI Practices) · D5 (Agents)
⚠️ Oportunidades: D2 (Copilot Adoption) · D8 (Security) · D6 (Instructions)

📋 Próximos passos:
   1. Para subir D2 → workshop Copilot + revisão de licenças
   2. Para subir D8 → política formal + JIT permissions
   3. /wizard-implementacao para incorporar no Implementation Guide
```

## Constraints

- **NEVER cite respondents by name** — survey is anonymous. Quotes are by question (e.g., "Resposta de S9-Q1") not by person.
- **NEVER infer beyond what the data says** — if N=3 respondents, don't claim "the team" — say "3 respondentes".
- **DO NOT** modify `survey-devs/respostas-devs.json` — read-only.
- Output to `saida/insights-developer-survey-<DATE>.md` only.
- Always include the date and respondent count prominently (data-driven, not opinion).
- If respondent count < 3, refuse to generate full report — only show raw aggregations with disclaimer.
