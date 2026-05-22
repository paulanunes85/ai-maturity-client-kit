# `survey-learning/scripts/`

📖 **Navegação:** [🏠 Índice](../../README.md) · [« Learning Survey](../README.md)

Scripts que constroem o plano de capacitação a partir do Learning & Growth Survey (identificado).

## Conteúdo

| Arquivo | Propósito |
|---|---|
| [`gerar_plano_capacitacao.py`](gerar_plano_capacitacao.py) | Lê `survey-learning/respostas-learning.json` e gera `saida/plano-capacitacao-<DATE>.md` — 12 seções com top 10 tópicos demandados, cohorts por dimensão D2-D8 (com listas nominais de inscritos), Champions Network em 3 tiers, mentor↔mentee pairs, calendário 90 dias, barreiras priorizadas. |

## Uso

```bash
python3 survey-learning/scripts/gerar_plano_capacitacao.py
```

> [!IMPORTANT]
> Este script é invocado pela skill `/plano-capacitacao`. O agente concierge faz isso automaticamente; você só roda diretamente se quiser regenerar sem passar pelo chat.

## Output

Markdown completo em PT-BR (~10 páginas equivalentes), pronto para apresentar à liderança ou anexar em proposta de capacitação.
