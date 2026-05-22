# `wizard/scripts/`

📖 **Navegação:** [🏠 Índice](../../README.md) · [« Wizard](../README.md)

Scripts que apoiam o Wizard de Implementation Guide.

## Conteúdo

| Arquivo | Propósito |
|---|---|
| [`auto_fill_from_plano.py`](auto_fill_from_plano.py) | **Modo D** do wizard: lê `saida/plano-capacitacao-<DATE>.md` (output do Learning Survey) e gera `implementation-guide-inputs.json` na raiz, preenchendo automaticamente **6 dos 9 campos** (Champions, training_plan, calendário, ADKAR-knowledge, quick wins). |

## Uso

```bash
python3 wizard/scripts/auto_fill_from_plano.py
```

Detecta automaticamente o último `plano-capacitacao-*.md` em `saida/`. Output: `implementation-guide-inputs.json` na raiz (67 % completo — você ainda precisa preencher TPO e RACI Matrix manualmente).

> [!TIP]
> Só faz sentido rodar se você já gerou o plano de capacitação via `/plano-capacitacao`. Se não, prefira o modo A (HTML wizard), B (editar JSON template) ou C (conduzir no chat) — todos descritos em [`../README.md`](../README.md).
