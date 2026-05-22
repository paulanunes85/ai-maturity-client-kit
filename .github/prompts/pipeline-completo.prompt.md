---
name: pipeline-completo
description: Run the end-to-end pipeline — import Excel (if present), populate spreadsheet, compute scores, gap analysis, recommend strategies and generate executive report. Use when client finished filling responses.json (or respostas-forms.xlsx) and wants everything at once.
agent: agent
---

# End-to-end pipeline

Execute the 6 skills in this exact order. Stop at first error and report to the user.

## Pre-checks

This prompt orchestrates the **AI Maturity Assessment** pipeline (organizational, leadership-driven). The kit also has 2 complementary surveys with their own pipelines — see "Related flows" at the end if user wants those.

1. **Input detection** — check workspace root in this order:
   - **If `respostas-forms.xlsx` exists** AND is more recent than `respostas.json`: run `/importar-respostas-excel` FIRST to convert Excel → JSON
   - **Else if `respostas.json` exists**: use directly
   - **Otherwise**: stop and instruct the user to either fill `respostas.json` or create `respostas-forms.xlsx` (see `coleta/INSTRUCOES-FORMS.md`)
2. Count questions with `level != null`. If 0, stop and instruct the user to fill at least some answers (ideally ≥25 to exit BLOCKED state).
3. If 1–24 answers: warn about BLOCKED threshold but ask if user wants to proceed anyway to generate a "preliminary draft".
4. **Check for complementary surveys** — if any of these exist at root, mention them in the final report:
   - `survey-devs/respostas-devs.json` (output of `/importar-survey-devs`) → mention "Developer Survey insights available — run /insights-developer-survey"
   - `survey-learning/respostas-learning.json` (output of `/importar-survey-learning`) → mention "Learning roadmap available — run /plano-capacitacao"
   - `implementation-guide-inputs.json` → already auto-merged in Step 5

## Execution sequence

### Step 0 · (Conditional) `/importar-respostas-excel`
- **Only if** `respostas-forms.xlsx` exists at root and is newer than `respostas.json`.
- Converts multi-respondent Excel from Forms into aggregated `respostas.json`.
- If `respostas.json` doesn't exist yet → this skill creates it.
- ✅ If ok → next step
- ❌ If parsing error → report and stop

### Step 1 · `/preencher-planilha`
- Generates `saida/pontuacao-preenchida-<DATE>.xlsx` (auditable spreadsheet with formulas)
- ✅ If ok → next step
- ❌ If error → report and stop

### Step 2 · `/calcular-scores`
- Generates `saida/scores.json`
- ✅ Report overall + threshold in chat
- ❌ Stop if invalid responses

### Step 3 · `/gap-analysis`
- Generates `saida/gaps.json`
- ✅ Report P0/P1/P2/P3 distribution

### Step 4 · `/recomendar-estrategias`
- Generates `saida/recomendacoes.json`
- ✅ Report top 3 strategies

### Step 4.5 · (Conditional) Suggest `/wizard-implementacao`
- **Only if** `implementation-guide-inputs.json` does NOT exist at root.
- Inform the user: "Part 4 of the PDF (Implementation Guide) will use generic placeholders. Run /wizard-implementacao first to personalize, OR proceed and personalize later."
- If user wants to personalize → STOP pipeline here and let them run `/wizard-implementacao`
- If user wants to proceed with placeholders → continue to Step 5

### Step 5 · `/gerar-relatorio`
- **Implementation:** invokes `python3 relatorios/scripts/build_payload_and_render.py` (DO NOT reimplement the merge logic in chat — the script does it correctly)
- The script: loads `relatorios/sample_payload.json` as base structure → overrides only fields we have client data for (organization, scores, capabilities, gap_analysis, implementation_guide_inputs) → invokes `render_reports.py` (Jinja2 + WeasyPrint)
- Generates 5 PDFs in `saida/`: `score_justification.pdf` + `roadmap_part_pillar_p1/p2/p3.pdf` + `roadmap_part4.pdf` (plus `payload.json` for debug/customization)
- If `implementation-guide-inputs.json` exists at root, automatically merges into payload (Part 4 personalized — no Acme placeholders)
- ✅ Report 5 PDFs with sizes (~330KB / 410KB / 410KB / 410KB / 510KB)

## Final report (in PT-BR for the user)

When complete, show a summary table:

```
🎯 Pipeline completo — AI Maturity Assessment

📂 Arquivos gerados em saida/:
   ✓ pontuacao-preenchida-2026-05-08.xlsx
   ✓ scores.json
   ✓ gaps.json
   ✓ recomendacoes.json
   ✓ payload.json                          (merged data — debug/customization)
   ✓ score_justification.pdf                (~330 KB)
   ✓ roadmap_part_pillar_p1.pdf             (~410 KB)
   ✓ roadmap_part_pillar_p2.pdf             (~410 KB)
   ✓ roadmap_part_pillar_p3.pdf             (~410 KB)
   ✓ roadmap_part4.pdf                      (~510 KB)

📊 Resumo dos resultados:
   Overall:     2.41 (L2 — Definido)
   PE:          1.87 (L1 — Em Desenvolvimento)
   Threshold:   WARNING (45/158)
   Pillars:     P1=2.6 L3 · P2=2.1 L2 · P3=2.4 L2
   Gaps top:    3 P0, 5 P1, 7 P2, 2 P3
   Estratégias: S5, S7, S6 (top 3)

📋 Próximos passos:
   1. Abrir saida/score_justification.pdf no preview
   2. Validar com stakeholders
   3. Completar respostas faltantes (113 ainda não respondidas) — prioridade nas P0/P1
```

## Error handling between steps

- Each step must verify its input (output of previous step) exists before running.
- If a step fails, **DO NOT PROCEED**. Report which step failed and why.
- Common errors:
  - `respostas.json` corrupted → instruct to validate JSON
  - Invalid levels → list problematic qids
  - 0 capabilities with score → client only answered questions outside the framework

## Constraints

- Don't skip steps.
- Don't modify `respostas.json`, `framework.json`, `referencia/`, `formularios/` or `coleta/`.
- All output to `saida/`.
- Final user-facing message in PT-BR.

## Related flows (mention to user if relevant)

This prompt covers ONLY the maturity assessment pipeline. The kit also has:

### Developer Survey (anonymous, behavioral) — separate flow
- Input: `respostas-survey-devs.xlsx` at root
- Skills: `/importar-survey-devs` → `/insights-developer-survey`
- Output: `saida/insights-developer-survey-<DATE>.md` + `saida/maturidade-developer-survey-<DATE>.json` (with rubric scores L0-L4 per dimension D2-D8)
- Use case: validate maturity assessment scores with real developer behavior
- Recommend: run BEFORE the maturity assessment if doing both

### Learning & Growth Survey (identified, capacitation) — separate flow
- Input: `respostas-survey-learning.xlsx` at root
- Skills: `/importar-survey-learning` → `/plano-capacitacao`
- Output: `saida/plano-capacitacao-<DATE>.md` (training roadmap with attendee lists, Champions Network, mentor pairs, calendar)
- Use case: build personalized training plan that feeds `/wizard-implementacao::training_plan + adkar_notes + quick_wins`
- Recommend: run BEFORE `/wizard-implementacao` to populate Part 4 of the PDF with real data

### When to run all three
For serious consulting engagement, run in this order:
1. Developer Survey (anonymous baseline of real behavior)
2. Learning Survey (identified — what devs want to learn)
3. Maturity Assessment (leadership avalia INFORMADA pelos dois acima)
4. `/wizard-implementacao` — auto-mescla `implementation-guide-inputs.json` + (if exists) `saida/plano-capacitacao-<DATE>.md` data
5. `/gerar-relatorio` — final 5 PDFs with real data from all three
