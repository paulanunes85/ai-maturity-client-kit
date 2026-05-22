# `wizard/` — Implementation Guide Wizard (Parte 4 do PDF)

📖 **Navegação:** [🏠 Índice](../README.md) · [« Learning Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.md) · Você está aqui

Esta pasta tem **3 maneiras** de preencher os 9 inputs estruturados que populam a **Parte 4 do `roadmap_part4.pdf`** (Implementation Guide consolidado: comitês, RACI, ADKAR, quick wins, etc.). Espelha o wizard React da plataforma web (`app/frontend/src/components/dashboard/ImplementationGuideWizard.tsx`).

> [!NOTE]
> **Output em qualquer modo:** `implementation-guide-inputs.json` na **raiz do kit-cliente/** (não nesta pasta). A skill `/gerar-relatorio` detecta automaticamente e mescla no payload.

## Os 9 inputs

| # | Input | O que é |
|---|---|---|
| 1 | **Steering Committee** | 5-8 nomes — Sponsor, Programa Lead, CFO, CISO, Change Champion |
| 2 | **TPO** (Technology Product Owner) | Programa Manager + escritório (3-5 pessoas) + autoridade de decisão |
| 3 | **RACI Matrix** | 5-8 atividades × R/A/C/I |
| 4 | **Plano de Comunicação** | Audiência × canal × frequência × owner |
| 5 | **Plano de Treinamento** | Cohort × formato × cadência × critério |
| 6 | **ADKAR** | Awareness · Desire · Knowledge · Ability · Reinforcement |
| 7 | **Quick Wins W1-4** | 4-6 iniciativas do primeiro mês |
| 8 | **Quick Wins W5-8** | Segunda onda |
| 9 | **Quick Wins W9-12** | Terceira onda |

## Os 3 modos

### A. Wizard HTML standalone (recomendado para visual)

```bash
open wizard/implementation-guide-wizard.html
```

- Browser abre página com 9 steps (cada um com helper + textarea grande)
- Salva automaticamente no `localStorage` — pode pausar e voltar depois
- Stepper no topo mostra progresso (✓ verde quando preenchido)
- Ao final: clique **💾 Baixar JSON** → mova `implementation-guide-inputs.json` para a raiz

**Tempo:** 30-60 min para preencher os 9 detalhadamente (15 min para rascunho).

### B. JSON template editável (recomendado para devs)

```bash
cp wizard/implementation-guide-inputs.template.json implementation-guide-inputs.json
code implementation-guide-inputs.json
```

O template tem placeholders ricos com instruções inline (`_help`, `_dicas`, exemplos por campo). Apague os exemplos e substitua pelos seus dados.

### C. Conversa via Copilot Chat (recomendado para rascunho colaborativo)

No Copilot Chat (modo Agent):

```
/wizard-implementacao
```

Selecione modo **C** quando o Copilot perguntar. Ele:
1. Faz 9 perguntas, uma por vez
2. Você responde livremente em PT-BR
3. No fim, monta o JSON e te pede confirmação para salvar

## Arquivos

| Arquivo | Tamanho | Para que serve |
|---|---|---|
| **[implementation-guide-wizard.html](implementation-guide-wizard.html)** | ~22 KB | Modo A — wizard visual standalone (Tailwind + JavaScript, salva em localStorage) |
| **[implementation-guide-inputs.template.json](implementation-guide-inputs.template.json)** | ~12 KB | Modo B — template JSON com 9 campos pré-preenchidos com instruções e exemplos |

## Após preencher

```bash
# Verificar que o JSON está na raiz do kit
ls implementation-guide-inputs.json

# Re-renderizar PDFs com a Parte 4 personalizada
/gerar-relatorio                 # via Copilot Chat
# ou
python3 relatorios/scripts/build_payload_and_render.py   # via CLI
```

## Skip e reuso

- Não preencher é OK — `/gerar-relatorio` usa placeholders profissionais do `sample_payload.json` (com nomes do "Acme Insurance Group"). Cliente pode rodar o wizard depois e re-gerar quando quiser.
- Você pode preencher só alguns dos 9 — campos vazios mantêm placeholders.
- Re-rodar o wizard sobrescreve apenas os campos preenchidos novamente.

## Documentação relacionada

- Skill que orquestra → [`../.github/skills/wizard-implementacao/SKILL.md`](../.github/skills/wizard-implementacao/SKILL.md)
- Wizard original (React/TS) que espelhamos → `app/frontend/src/components/dashboard/ImplementationGuideWizard.tsx`
- Como o JSON entra no PDF → [`../relatorios/templates/roadmap_part4.html.j2`](../relatorios/templates/roadmap_part4.html.j2) (procure por `wiz.`)

---

## 🧭 Navegação

| | |
|---|---|
| ← Anterior | **[Learning & Growth Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.md)** |
| → Próximo | **[🏠 Índice (voltar ao topo)](../README.md)** — você completou o fluxo! 🎉 |
| 🔗 Relacionado | [Guia passo-a-passo](../GUIA-PASSO-A-PASSO.md) · [Wizard standalone HTML](implementation-guide-wizard.html) |
