---
name: wizard-implementacao
description: Guides the client through the 9-step Implementation Guide Wizard (steering committee, TPO, RACI, comms plan, training plan, ADKAR, 3 quick-wins waves) by either pointing to the standalone HTML wizard OR conducting the conversation in chat. Output is implementation-guide-inputs.json that feeds Roadmap Part 4 PDF. Use when the user asks for "wizard", "implementation guide", "guia de implementação", "preencher parte 4", "TPO", "steering committee", "RACI", "ADKAR", "quick wins".
argument-hint: optional "chat" to force conversation mode (default: offer both options)
---

# Skill: Implementation Guide Wizard

## What this is

The platform's Implementation Guide Wizard (`app/frontend/src/components/dashboard/ImplementationGuideWizard.tsx`) collects 9 structured inputs that feed **Part 4 of the PDF report** (Implementation Guide consolidated). This kit provides **4 ways** to fill the same 9 inputs (mode D is automatic from Learning Survey):

| Mode | Best for | UX |
|---|---|---|
| **A. HTML wizard** (`wizard/implementation-guide-wizard.html`) | Visual users | Browser, step-by-step, saves localStorage, exports JSON |
| **B. JSON template** (`wizard/implementation-guide-inputs.template.json`) | Devs / power users | Direct edit in VS Code |
| **C. Chat conversation** (this skill in chat mode) | Quick draft / iteration | Copilot conducts 9 questions in chat |
| **D. Auto-fill from Learning Survey** ⭐ | When `/plano-capacitacao` already ran | Auto-extract from `saida/plano-capacitacao-<DATE>.md` |

All four produce the same artifact: **`implementation-guide-inputs.json`** at the workspace root.

## ⭐ Mode D — Auto-fill from Learning Survey output (REAL implementation)

**Implementation:** invoke the official script that parses `saida/plano-capacitacao-<DATE>.md` and generates `implementation-guide-inputs.json` with 6 of 9 fields auto-filled:

```bash
python3 wizard/scripts/auto_fill_from_plano.py
# Auto-detects latest plano-capacitacao-*.md in saida/
# Output: implementation-guide-inputs.json at root (67% complete — 6/9 fields)
```

**What it auto-fills (6 of 9):**
- `executive_steering_committee` ← Champions ativos (extraído da seção 4 do plano)
- `communication_plan` ← Calendário sugerido (seção 5)
- `training_plan` ← Cohorts por dimensão (seção 3)
- `adkar_notes` ← Knowledge stage usa Top 5 workshops do plano
- `quick_wins_w1_4` / `w5_8` / `w9_12` ← Calendário 90 dias

**What user MUST fill manually (Learning Survey doesn't cover):**
- `tpo` (Technology Product Owner)
- `raci_matrix`

After running auto_fill, the user can edit `implementation-guide-inputs.json` to fill the 2 missing fields, then run `/gerar-relatorio` to render PDFs with personalized Part 4.



If `saida/plano-capacitacao-<DATE>.md` exists (output of `/plano-capacitacao`), the data ALREADY contains:

| Wizard input | Data in plano-capacitacao |
|---|---|
| `executive_steering_committee` | Champions Network "ativos" (3-5 pessoas com nome+email) |
| `tpo` | (not in learning survey — keep manual or sample) |
| `raci_matrix` | (not in learning survey — keep manual or sample) |
| `communication_plan` | "Calendário sugerido de workshops" (audiência + canal + cadência) |
| `training_plan` | "Cohorts sugeridos por dimensão" (audiência × formato × cadência × Champion) |
| `adkar_notes` | Top 5 recommendations from learning survey (Knowledge stage = workshops top 5) |
| `quick_wins_w1_4` | First 4 weeks of "Calendário sugerido" |
| `quick_wins_w5_8` | Weeks 5-8 |
| `quick_wins_w9_12` | Weeks 9-12 + barrier removal actions |

**How to invoke Mode D:**

When user runs `/wizard-implementacao` and `saida/plano-capacitacao-*.md` exists, OFFER as first option:

```
🎓 Detectei saida/plano-capacitacao-2026-05-08.md (do Learning Survey).
   Posso EXTRAIR automaticamente: Champions, training_plan, calendário, quick wins.
   Você só precisa preencher: TPO + RACI Matrix (que o learning survey não cobre).

   [a] Auto-fill (modo D recomendado — preenche 6 dos 9 inputs)
   [b] Modo HTML / JSON / Chat (preencher tudo manualmente)
```

## When to use this skill
- Client asked about "wizard" / "implementation guide" / "Parte 4" / "guia de implementação"
- Before `/gerar-relatorio` if `implementation-guide-inputs.json` doesn't exist yet (or is incomplete)
- When client wants to iterate on the implementation plan without re-rendering everything

## Procedure

### Default behavior: offer the 3 modes

When invoked without arguments, present the 3 options and let the user choose. Reply in PT-BR:

```
🧙 Wizard de Guia de Implementação — 9 inputs alimentam a Parte 4 do PDF

Como prefere preencher?

  📋 [A] Modo visual (HTML standalone)
       Abra: wizard/implementation-guide-wizard.html no browser.
       9 passos, salva no localStorage, exporta JSON ao final.
       👉 Best para: experiência visual igual ao app web.

  📝 [B] Modo direto (editar JSON no VS Code)
       Copie wizard/implementation-guide-inputs.template.json para
       a raiz do kit-cliente/, renomeie para implementation-guide-inputs.json
       e preencha cada campo.
       👉 Best para: devs que preferem código.

  💬 [C] Modo conversa (eu te conduzo aqui no chat)
       Eu te faço as 9 perguntas uma a uma. Responda livremente.
       Ao final eu salvo implementation-guide-inputs.json automaticamente.
       👉 Best para: rascunho rápido, iteração interativa.

Qual prefere? Digite A, B ou C.
```

### If user picks A or B
- Confirme o caminho e termine. (Não há nada para fazer no chat.)

### If user picks C (chat mode) — conduct the 9 questions

For each step, ask ONE question at a time, wait for the answer, validate (non-empty), move on.

**Questions to ask (in PT-BR):**

#### 1/9 — Comitê Executivo Diretivo
> Quem são os 5-8 membros do Comitê Executivo Diretivo? Inclua: Sponsor, Programa Lead, Líder Financeiro, Líder de Segurança, Change Champion. Formato livre — pode ser uma lista com "Nome — Cargo (Papel)".

#### 2/9 — Technology Product Owner (TPO)
> Quem é o Technology Product Owner / qual a estrutura do escritório? Liste: Programa Manager (nome + dedicação %), Membros (3-5 pessoas), responsabilidades-chave, autoridade de decisão (até onde aprova sem escalar).

#### 3/9 — Matriz RACI
> Quais são as 5-8 atividades principais e seus papéis RACI (Responsible / Accountable / Consulted / Informed)? Pode listar em texto livre ou tabela.

#### 4/9 — Plano de Comunicação
> Como vão comunicar a transformação para cada audiência? Para cada uma (Toda Eng, Working Groups, Steering, Champions, Stakeholders externos), me dê: canal, frequência e owner.

#### 5/9 — Plano de Treinamento
> Qual o plano de capacitação? Para cada audiência (Devs, Champions, Eng Managers, SREs etc.), liste: formato, cadência, critério de conclusão.

#### 6/9 — Gestão de Mudança ADKAR
> Para cada estágio ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement), liste 1-3 intervenções concretas que vocês vão fazer.

#### 7/9 — Quick Wins · Semanas 1-4
> 4-6 quick wins do primeiro mês — iniciativas pequenas com resultado visível em 30 dias. Indique semana sugerida.

#### 8/9 — Quick Wins · Semanas 5-8
> 4-6 quick wins da segunda onda — expansão dos pilotos. Semana sugerida.

#### 9/9 — Quick Wins · Semanas 9-12
> 4-6 quick wins da terceira onda — solidificando antes de escalar para H2.

### After the 9 answers (chat mode)

1. Show a summary of all 9 fields collected
2. Ask: "Tudo certo? Posso salvar como `implementation-guide-inputs.json`?"
3. If yes:
   - Build the JSON with the schema below
   - Write to `implementation-guide-inputs.json` at workspace root
   - Confirm: `✓ Salvo em implementation-guide-inputs.json (X% completo). Próximo: /gerar-relatorio`

## Schema (output `implementation-guide-inputs.json`)

```json
{
  "metadata": {
    "generated_at": "ISO-8601 UTC",
    "generator": "wizard-implementacao skill v1.0 (chat mode)",
    "completion_pct": 100
  },
  "implementation_guide_inputs": {
    "executive_steering_committee": "...",
    "tpo": "...",
    "raci_matrix": "...",
    "communication_plan": "...",
    "training_plan": "...",
    "adkar_notes": "...",
    "quick_wins_w1_4": "...",
    "quick_wins_w5_8": "...",
    "quick_wins_w9_12": "..."
  }
}
```

The 9 keys mirror exactly `sample_payload.json::implementation_guide_inputs` and the wizard React component schema.

## Constraints

- **DO NOT** invent answers if the user gives short/vague input — ask for more detail or accept and mark as "minimal".
- **DO** allow markdown (tables, lists, bold) in answers — they render in the PDF.
- **DO** validate at the end: if any field is empty, warn but allow saving (placeholders kick in at render time).
- **NEVER** modify `framework.json`, `respostas.json`, or files in `relatorios/templates/`.
- Output JSON to workspace root (NOT to `saida/`) so the file persists across pipeline runs and serves as **input**, not output.

## Integration with other skills

- After this skill runs, `/gerar-relatorio` will **automatically detect** `implementation-guide-inputs.json` at the root and merge it into the payload before rendering the 5 PDFs.
- If client edits `implementation-guide-inputs.json` manually later (e.g., updates RACI), they just rerun `/gerar-relatorio` — no need to redo the wizard.

## Reference example

The folder `wizard/` contains:
- `implementation-guide-wizard.html` — full HTML wizard (mode A)
- `implementation-guide-inputs.template.json` — pre-filled JSON template with rich placeholders (mode B starting point)

Both produce JSONs with the same schema described above.
