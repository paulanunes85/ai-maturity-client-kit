---
name: recomendar-estrategias
description: Maps gaps per capability to the 7 strategies S1-S7 and generates prioritized action plan with specific technologies. Reads saida/gaps.json + framework.json. Generates saida/recomendacoes.json. Use when user asks to "recomendar estratégias", "mapear ações", "que iniciativas devo priorizar".
---

# Skill: Recommend strategies S1–S7

## When to use
- After `/gap-analysis` (depends on `saida/gaps.json`).
- When client wants an **actionable plan**, not just a diagnosis.

## Inputs
- `saida/gaps.json` — prioritized gaps
- `framework.json::strategies` — definition of the 7 strategies
- `framework.json::technologies_per_strategy` — technologies per strategy
- `framework.json::pillars[].capabilities[].strategies` — cap→strategies mapping

## Expected output
- `saida/recomendacoes.json` — grouped by strategy + ranking
- Brief chat message (PT-BR): top 3 strategies by cumulative impact.

## Algorithm

### 1. Aggregate gaps per strategy
For each gap in `gaps.json::gaps`:
```
for each strategy_id in gap.strategies:
    estrategias[strategy_id].related_gaps.append(gap)
    estrategias[strategy_id].cumulative_priority += gap.priority_score
    estrategias[strategy_id].max_priority = max(P0, P1, P2, P3 of gaps)
```

### 2. Rank strategies
Sort by `cumulative_priority` desc. Tie → higher `max_priority` → more `related_gaps`.

### 3. Technologies and horizon
For each strategy:
- Pull `technologies_per_strategy[strategy_id]` from `framework.json`
- Determine aggregated `horizon` from the most critical gap in the group (P0=30d, P1=quarter, P2=semester)

### 4. Generate concrete actions (deterministic templates — DO NOT invent)

Use these templates based on the strategy (output text in PT-BR):

| Strategy | Recommended initial action |
|---|---|
| **S1** GitHub Migration | "Inventário de repositórios atuais → plano de migração para GitHub Enterprise Cloud em 3 ondas." |
| **S2** Foundry + SRE | "Definir SLOs/SLIs para serviços críticos; implantar Azure Monitor + dashboards Grafana." |
| **S3** App Modernization | "Selecionar 1–2 apps piloto; replatforming para Azure Container Apps + IaC com Terraform." |
| **S4** AI Applications | "Identificar 2 casos de uso de alto ROI; PoC com Azure OpenAI + Prompt Flow." |
| **S5** Copilot Acceleration | "Rollout Copilot Enterprise em 2 squads piloto; medir adoção e produtividade DORA por 8 semanas." |
| **S6** Agentic Activation | "Pilot Semantic Kernel para 1 workflow interno; estabelecer guardrails e observabilidade." |
| **S7** Security & Governance | "Habilitar GitHub Advanced Security em todos repos; gerar SBOM dos serviços críticos." |

## `saida/recomendacoes.json` schema

```json
{
  "metadata": {
    "computed_at": "2026-05-08T14:30:00Z",
    "based_on": "saida/gaps.json"
  },
  "ranked_strategies": [
    {
      "rank": 1,
      "strategy_id": "S5",
      "strategy_name": "GitHub Copilot Acceleration",
      "cumulative_priority": 8.42,
      "max_priority": "P0 — Crítico",
      "horizon": "30 dias",
      "related_capabilities": [
        {"id": "P1-C1", "name_pt_br": "Assistentes de Codificação IA", "gap_size": 1.4, "priority": "P1 — Alto"},
        {"id": "P1-C8", "name_pt_br": "Medição de Produtividade", "gap_size": 1.5, "priority": "P1 — Alto"}
      ],
      "technologies": [
        {"name": "GitHub Copilot Enterprise", "purpose": "AI-assisted coding across development teams"}
      ],
      "first_action": "Rollout Copilot Enterprise em 2 squads piloto; medir adoção e produtividade DORA por 8 semanas.",
      "expected_outcome": "Subir capabilities P1-C1 e P1-C8 para L3 em ~2 trimestres."
    }
  ],
  "skipped_strategies": ["S1"]
}
```

`skipped_strategies` = strategies that **didn't appear in any gap** (client already mature in them or related capabilities not answered).

## Report in chat (PT-BR)

```
✓ Recomendações → saida/recomendacoes.json

Top 3 estratégias por impacto cumulativo:
  🥇 S5 — GitHub Copilot Acceleration (priority 8.42, 4 capabilities)
     → Rollout Copilot em 2 squads piloto, medir DORA por 8 sem.
  🥈 S7 — Security & Governance (priority 5.10, 2 capabilities)
     → Habilitar GHAS em todos repos + SBOM dos serviços críticos.
  🥉 S6 — Agentic Activation (priority 2.94, 1 capability)
     → Pilot Semantic Kernel para 1 workflow interno.

Não recomendadas (sem gaps relevantes): S1
Próximo: /gerar-relatorio
```

## Constraints
- **DO NOT INVENT** actions outside the table above — if in doubt, write "Detalhar com arquiteto Microsoft GBB".
- Strategies with `cumulative_priority < 0.9` (only P3 gaps) → move to `skipped_strategies` with note "monitorar".
- Technologies must come EXCLUSIVELY from `framework.json::technologies_per_strategy`.
- Keep PT-BR in human-facing fields; technical IDs and names can stay in English.
