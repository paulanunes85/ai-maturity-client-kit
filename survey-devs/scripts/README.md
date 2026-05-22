# `survey-devs/scripts/`

📖 **Navegação:** [🏠 Índice](../../README.md) · [« Developer Survey](../README.md)

Scripts que computam maturidade IA dos desenvolvedores a partir do Developer Survey (anônimo).

## Conteúdo

| Arquivo | Propósito |
|---|---|
| [`rubric.py`](rubric.py) | **Rubrica determinística L0–L4** em 7 dimensões (D2-D8). Mapeia respostas → scores. Importável como módulo. |
| [`calcular_maturidade.py`](calcular_maturidade.py) | Lê `survey-devs/respostas-devs.json`, aplica `rubric.py`, gera `saida/maturidade-developer-survey-<DATE>.json` com scores agregados do time. |
| [`gerar_insights.py`](gerar_insights.py) | Gera o relatório completo em markdown (`saida/insights-developer-survey-<DATE>.md`) — demografia, adoção Copilot, governança, citações anonimizadas, recomendações ligadas às capabilities (P1-C1, P1-C5, P1-C8, P2-C4, P3-C6). |

## Uso

```bash
# Só os scores de maturidade
python3 survey-devs/scripts/calcular_maturidade.py

# Scores + relatório completo (recomendado)
python3 survey-devs/scripts/gerar_insights.py
```

> [!IMPORTANT]
> Estes scripts são invocados pelas skills `/insights-developer-survey`. Você normalmente não precisa rodar diretamente — o agente concierge faz isso.

## Documentação da rubrica

Veja [`../RUBRICA-MATURIDADE.md`](../RUBRICA-MATURIDADE.md) para regras de scoring por dimensão.
