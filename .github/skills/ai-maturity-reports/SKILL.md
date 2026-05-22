---
name: ai-maturity-reports
description: Orchestrates the production of all client-ready report deliverables for the AI Maturity Assessment Platform. Wraps the lower-level skills /preencher-planilha + /calcular-scores + /gap-analysis + /recomendar-estrategias + /wizard-implementacao + /gerar-relatorio. Renders 5 PDFs (Score Justification + 3 Pillar Roadmaps + Implementation Guide) using Jinja2 + WeasyPrint with paulasilva-ms branding (Microsoft 4-color palette). Mirror of the global skill `~/.github/skills/ai-maturity-reports/` adapted to this self-service kit. Use when the user asks for "pacote completo de relatórios", "gerar todos os PDFs", "todos os 5 PDFs", "rodar tudo de ponta a ponta", "rodar pipeline de reports", "AI Maturity report", "Score Justification", "Transformation Roadmap", "render the assessment PDFs", "ai-maturity-reports", "full reports pipeline", "complete pack", "all pdfs", "generate the bundle".
---

# Skill: ai-maturity-reports (kit edition)

High-level orchestrator that produces the **6 client-ready report deliverables**:
- 5 PDFs (Score Justification + 3 Pillar Roadmaps + Implementation Guide consolidated)
- 1 auditable XLSX workbook

This is the kit-scoped version of the global skill `.github/skills/ai-maturity-reports/`. The global skill is the source of truth for templates, references, and validation specs. This kit-scoped version uses the same templates (synced into `relatorios/templates/`) and adapts the orchestration to the kit's lower-level skills.

## When to use this skill (vs. lower-level skills)

| Use this skill | Use lower-level skills |
|---|---|
| Client wants the **full bundle of deliverables** | Client wants to iterate on one piece (just scores, just gap analysis) |
| End-to-end pipeline from `respostas.json` to PDFs | Already past Step 4, need to refine Part 4 wizard inputs |
| Branding paulasilva-ms enforced | Same — branding is always applied |

For step-by-step execution of individual steps, prefer the granular skills:
- `/importar-respostas-excel` (Microsoft Forms → respostas.json)
- `/preencher-planilha` (respostas → auditable xlsx)
- `/calcular-scores` (SUMPRODUCT 3 layers)
- `/gap-analysis` (P0–P3 priorities)
- `/recomendar-estrategias` (S1–S7 mapping)
- `/wizard-implementacao` (Part 4 personalization, with Mode D auto-fill)
- `/gerar-relatorio` (the actual PDF rendering)

## Inputs

| File | Required | Source |
|---|---|---|
| `respostas.json` | yes | client (or `/importar-respostas-excel`) |
| `framework.json` | yes | bundled with kit |
| `relatorios/templates/*.html.j2` | yes | bundled (synced from global skill) |
| `relatorios/i18n/<locale>.json` | yes | bundled |
| `relatorios/sample_payload.json` | yes | bundled — schema source |
| `implementation-guide-inputs.json` | optional | `/wizard-implementacao` (or `/wizard-implementacao` Mode D) |
| `saida/plano-capacitacao-<DATE>.md` | optional | `/plano-capacitacao` (Learning Survey) |
| `saida/insights-developer-survey-<DATE>.md` | optional | `/insights-developer-survey` (Survey-devs) |

## Procedure

### Standard pipeline (delegates to /pipeline-completo)

```
/pipeline-completo
```

Which expands to:

1. (if `respostas-forms.xlsx` newer than `respostas.json`) `/importar-respostas-excel`
2. `/preencher-planilha`
3. `/calcular-scores`
4. `/gap-analysis`
5. `/recomendar-estrategias`
6. (offer) `/wizard-implementacao` to personalize Part 4
7. `/gerar-relatorio` invokes `relatorios/scripts/build_payload_and_render.py`

### Direct invocation (skip the orchestration prompt)

If client wants to go straight from existing scores to PDFs:

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

The script:
- Loads `relatorios/sample_payload.json` as base structure
- Overrides only fields with client data (organization, scores, capabilities, gaps)
- Merges `implementation-guide-inputs.json` if present (auto-fills Part 4)
- Injects paulasilva-ms branding into payload (`branding.primary_color`, `branding.author`, etc.)
- Invokes `relatorios/scripts/render_reports.py` to render 5 PDFs

## Output

In `saida/`:
- `payload.json` (~80 KB) — debug/customization
- `score_justification.pdf` (~330 KB)
- `roadmap_part_pillar_p1.pdf` (~410 KB)
- `roadmap_part_pillar_p2.pdf` (~410 KB)
- `roadmap_part_pillar_p3.pdf` (~410 KB)
- `roadmap_part4.pdf` (~510 KB)

Plus the auditable workbook from `/preencher-planilha`.

## Branding (paulasilva-ms, applied automatically)

All 5 PDFs render with:
- **Primary** = MS Blue `#00A4EF`
- **Positive** = MS Green `#7FBA00`
- **Warn** = MS Yellow `#FFB900`
- **Critical** = MS Red `#F25022`
- **Author block:** Paula Silva, Software Global Black Belt, paulasilva@microsoft.com
- **Tagline:** "Building the future of software development with AI and Agentic DevOps"
- **Fonts:** Inter (body), JetBrains Mono (code/labels)

The `_print.css` `:root` already maps these tokens. The script `build_payload_and_render.py` injects branding metadata into `payload.branding` before rendering. See `referencia/branding/IDENTITY.md` for canonical strings.

## Sync with global skill

When the global skill `~/.github/skills/ai-maturity-reports/` updates templates, sync into the kit:

```bash
SKILL=~/.github/skills/ai-maturity-reports
KIT=$(pwd)  # in kit-cliente/

cp $SKILL/assets/templates/*.html.j2 $KIT/relatorios/templates/
cp $SKILL/assets/templates/_print.css $KIT/relatorios/templates/_print.css
cp $SKILL/assets/i18n/*.json $KIT/relatorios/i18n/
cp $SKILL/assets/fixtures/sample_payload.json $KIT/relatorios/sample_payload.json

# Re-apply paulasilva-ms branding to _print.css :root tokens
# (see referencia/branding/IDENTITY.md for the exact MS palette)
```

After syncing, re-render the example PDFs to validate:

```bash
cp respostas.json.example respostas.json
python3 survey-devs/scripts/calcular_maturidade.py
# (run other skills to populate saida/)
python3 relatorios/scripts/build_payload_and_render.py
# Copy outputs to referencia/exemplo-saida/
```

## Reference example outputs

The folder `referencia/exemplo-saida/` contains the 5 PDFs rendered from `respostas.json.example` (Cliente Exemplo S.A.). Plus EN versions in `referencia/exemplo-saida/en/`. These are reference outputs to show the client "before/after" before they run the pipeline.

## Constraints

- **DO NOT modify** `relatorios/templates/*.html.j2` directly. Edit them in the global skill (`~/.github/skills/ai-maturity-reports/assets/templates/`) and sync.
- **DO NOT change** the MS palette in `_print.css :root` without updating `referencia/branding/IDENTITY.md`.
- **DO NOT skip** the script — running Jinja2 manually misses i18n, CSS, and WeasyPrint setup.
- WeasyPrint dependencies: `pip install --user --break-system-packages weasyprint jinja2 openpyxl`
- Mac: `brew install cairo pango gdk-pixbuf libffi`
- Output language follows `respostas.json::metadata.language` (en / es / pt-br).

## Related skills (in this kit)

- `/preencher-planilha` — auditable XLSX
- `/calcular-scores` — SUMPRODUCT scoring
- `/gap-analysis` — gap prioritization
- `/recomendar-estrategias` — S1-S7 mapping
- `/wizard-implementacao` — Part 4 personalization (Mode A/B/C/D)
- `/gerar-relatorio` — the actual PDF rendering (this skill wraps it)

## Related global skill

For deck patterns, multi-page playbook, full design system showcase: `.github/skills/paulasilva-ms/`
For canonical templates and validation specs: `.github/skills/ai-maturity-reports/`
