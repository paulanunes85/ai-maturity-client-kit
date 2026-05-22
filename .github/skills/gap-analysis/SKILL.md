---
name: gap-analysis
description: Computes gap (target − current) per capability and priority P0-P3 (weight × gap). Reads saida/scores.json and respostas.json::target_overrides. Generates saida/gaps.json. Use when user asks for "gap analysis", "priorização", "onde estão minhas lacunas".
---

# Skill: Gap analysis and prioritization

## When to use
- After `/calcular-scores` (depends on `saida/scores.json`).
- When client wants to understand **where to invest first** or prioritize the roadmap.

## Inputs
- `saida/scores.json` — capability scores
- `respostas.json::target_overrides` — custom targets per capability (optional)
- `framework.json` — weights, names, cap→strategies mapping

## Expected output
- `saida/gaps.json` — list ordered by priority (P0 first)
- Brief chat message (PT-BR): top 5 P0/P1 gaps.

## Algorithm

```
default_target = 3.0
for each capability c in scores.capabilities (with score != null):
    target_c       = target_overrides.get(c.id, default_target)
    gap_size       = max(0, target_c − c.score)
    priority_score = c.weight × gap_size
    
    if gap_size ≤ 1e-9:  # already met target
        skip c   (don't enter gaps.json)
    
    classify:
        priority_score ≥ 2.4  → "P0 — Crítico"
        ≥ 1.6                 → "P1 — Alto"
        ≥ 0.9                 → "P2 — Médio"
        < 0.9                 → "P3 — Baixo"
```

Sort `saida/gaps.json::gaps` by `priority_score` desc.

## `saida/gaps.json` schema

```json
{
  "metadata": {
    "computed_at": "2026-05-08T14:25:00Z",
    "default_target": 3.0,
    "total_capabilities_with_gap": 17
  },
  "summary": {
    "P0": 3,  "P1": 5,  "P2": 7,  "P3": 2
  },
  "gaps": [
    {
      "rank": 1,
      "capability_id": "P3-C5",
      "capability_name_pt_br": "Aplicações Agênticas",
      "pillar_id": "P3",
      "current_score": 2.04,
      "current_label": "L2 — Definido",
      "target_level": 4.0,
      "gap_size": 1.96,
      "weight": 1.5,
      "priority_score": 2.94,
      "priority": "P0 — Crítico",
      "horizon_suggested": "30 dias",
      "strategies": ["S6", "S4"]
    }
  ]
}
```

## Horizon mapping by priority

| Priority | `horizon_suggested` |
|---|---|
| P0 | "30 dias" |
| P1 | "Próximo trimestre" |
| P2 | "Semestre" |
| P3 | "Backlog / monitorar" |

## Report in chat (PT-BR format)

```
✓ Gap analysis → saida/gaps.json
• Total com gap: 17 capabilities
• Distribuição: P0=3 · P1=5 · P2=7 · P3=2

Top 5 prioridades (P0/P1):
  1. P3-C5 Aplicações Agênticas        gap 1.96 → priority 2.94 (P0) — ações S6, S4
  2. P2-C4 DevSecOps                   gap 1.60 → priority 2.40 (P0) — S7
  3. P1-C8 Medição de Produtividade    gap 1.50 → priority 2.25 (P1) — S5

Próximo: /recomendar-estrategias
```

## Constraints
- Capabilities with `score=null` (no answers) **don't** enter gaps.json — should become "warning" in the report (insufficient coverage).
- Capabilities that already passed target (`gap_size ≤ 0`) also don't enter — could appear as "Atingido" in another report section if useful.
- Don't invent `target_level` — use exclusively `target_overrides` or default 3.0.
