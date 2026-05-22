---
name: gerar-relatorio
description: Renders 5 client-ready PDF reports (Score Justification + 3 Pillar Roadmaps + Implementation Guide) by invoking relatorios/scripts/build_payload_and_render.py. The script merges sample_payload.json (rich structure) with client data from saida/scores.json + gaps.json + recomendacoes.json + respostas.json + implementation-guide-inputs.json. Output is identical-quality to the platform's production PDFs. Use when the user asks to "gerar relatório", "produzir o report executivo", "gerar PDFs", "PDF final", "consolidar resultados", "executive report", "final report", "render PDF", "generate report PDFs", "produzir o PDF executivo".
---

# Skill: Generate executive PDF reports

## What this does

Invokes the script **`relatorios/scripts/build_payload_and_render.py`** which:
1. Loads `relatorios/sample_payload.json` as **base structure** (provides all the rich nested fields the Jinja2 templates need: scoring_rationale, h1_initiatives, technology_resources, success_metrics, risks, etc.)
2. **Overrides only the fields we have client data for**:
   - `organization` ← `respostas.json::metadata`
   - `scores.overall.weighted_avg` / `level_label` / `gap` ← `saida/scores.json`
   - `scores.pillars[].weighted_avg` / `level_label` / `gap` ← `saida/scores.json`
   - `capabilities[].current_score` / `current_level_label` / `gap` ← `saida/scores.json` (matched by id)
   - `gap_analysis[]` ← rebuilt from `saida/gaps.json` (preserves sample's `recommended_actions` per cap)
   - `implementation_guide_inputs.*` ← `implementation-guide-inputs.json` if exists (output of `/wizard-implementacao`)
3. Writes merged payload to `saida/payload.json`
4. Invokes `relatorios/scripts/render_reports.py` to produce 5 PDFs in `saida/`

## When to use
- After `/calcular-scores`, `/gap-analysis`, `/recomendar-estrategias` (pipeline order).
- When client wants the final **5 production-quality PDFs**.
- After editing `implementation-guide-inputs.json` (re-renders Part 4 with personalized content).
- After manually editing `saida/payload.json` (re-renders with custom narrative).

## Inputs (from workspace root unless specified)

| File | Required | Source |
|---|---|---|
| `respostas.json` | yes | client (or `/importar-respostas-excel`) |
| `saida/scores.json` | yes | `/calcular-scores` |
| `saida/gaps.json` | yes | `/gap-analysis` |
| `saida/recomendacoes.json` | yes | `/recomendar-estrategias` |
| `implementation-guide-inputs.json` | optional | `/wizard-implementacao` |
| `saida/plano-capacitacao-<DATE>.md` | optional | `/plano-capacitacao` (Learning Survey) |
| `saida/insights-developer-survey-<DATE>.md` | optional | `/insights-developer-survey` (Survey-devs) |
| `saida/maturidade-developer-survey-<DATE>.json` | optional | `/insights-developer-survey` (rubric scores) |
| `relatorios/sample_payload.json` | yes | bundled with kit |
| `relatorios/templates/*.html.j2` | yes | bundled with kit |
| `relatorios/i18n/<locale>.json` | yes | bundled with kit |

### Cross-survey integration (when complementary survey outputs exist)

If `/insights-developer-survey` or `/plano-capacitacao` already ran, the script `build_payload_and_render.py` populates `payload.cross_survey_data` with structured pointers to the latest artifacts:

| Field in `payload.cross_survey_data` | Source artifact | Content |
|---|---|---|
| `developer_survey_maturity` | `saida/maturidade-developer-survey-<DATE>.json` | Per-dimension rubric scores (D2–D8) + respondent count |
| `developer_survey_insights` | `saida/insights-developer-survey-<DATE>.md` | Path reference (full markdown stays alongside the PDFs) |
| `learning_plan` | `saida/plano-capacitacao-<DATE>.md` | Path reference (auto-fill into Part 4 happens via `wizard/scripts/auto_fill_from_plano.py`) |

The data is always written to `saida/payload.json` for inspection. The shipped Jinja2 templates currently do **not** render a dedicated cross-survey section — if you want one, edit `payload.json` and re-render, or extend `relatorios/templates/score_justification.html.j2` with a `{% if payload.cross_survey_data %}` block.

## Output (in `saida/`)

| File | Size (approx) | Content |
|---|---|---|
| **payload.json** | ~80 KB | Merged data the templates consumed (debug/customization) |
| **score_justification.pdf** | ~330 KB | Justification + PE Readiness + path recommendation |
| **roadmap_part_pillar_p1.pdf** | ~410 KB | Productivity pillar deep-dive |
| **roadmap_part_pillar_p2.pdf** | ~410 KB | DevOps pillar deep-dive |
| **roadmap_part_pillar_p3.pdf** | ~410 KB | Platform pillar deep-dive |
| **roadmap_part4.pdf** | ~510 KB | Implementation Guide consolidated (uses `implementation-guide-inputs.json` if present) |

## Procedure

### 1. Pre-flight checks

```python
from pathlib import Path
KIT = Path.cwd()  # workspace root

required = ["respostas.json", "saida/scores.json", "saida/gaps.json", "saida/recomendacoes.json"]
missing = [f for f in required if not (KIT / f).exists()]
if missing:
    error(f"Faltando: {missing}. Rode /pipeline-completo primeiro.")
```

### 2. Confirm dependencies installed

```bash
python3 -c "import jinja2, weasyprint, openpyxl" 2>&1 \
  || python3 -m pip install --user --break-system-packages jinja2 weasyprint openpyxl
```

### 3. Invoke the script

```bash
python3 relatorios/scripts/build_payload_and_render.py
```

Script does everything: merge → write payload.json → render 5 PDFs. Reports each step.

### 4. Verify outputs

```python
expected = [
    "score_justification.pdf",
    "roadmap_part_pillar_p1.pdf",
    "roadmap_part_pillar_p2.pdf",
    "roadmap_part_pillar_p3.pdf",
    "roadmap_part4.pdf",
    "payload.json",
]
for name in expected:
    f = KIT / "saida" / name
    if not f.exists() or f.stat().st_size < 50_000:
        warn(f"Output suspeito: {name}")
```

## Report in chat (PT-BR)

```
✓ 5 PDFs production-quality gerados em saida/:
   📄 score_justification.pdf       (331 KB) — Justificativa + PE Readiness
   📄 roadmap_part_pillar_p1.pdf    (415 KB) — Pilar Produtividade
   📄 roadmap_part_pillar_p2.pdf    (417 KB) — Pilar DevOps
   📄 roadmap_part_pillar_p3.pdf    (419 KB) — Pilar Plataforma
   📄 roadmap_part4.pdf             (516 KB) — Guia de Implementação

📊 Resumo:
   Organização: Cliente Exemplo S.A.
   Overall: 1.99 (L2 — Definido)
   Locale: pt-br
   Threshold: OK (46/158 respondidas)

⚠️ Personalização:
   Algumas seções narrativas (RACI matrix, technology stack details,
   risk register, success metrics per pillar) usam placeholders profissionais
   do sample_payload.json. Para personalizar:

   1. Rode /wizard-implementacao para Parte 4 (Implementation Guide)
   2. OU edite saida/payload.json diretamente e re-renderize:
        python3 relatorios/scripts/render_reports.py --payload saida/payload.json

📋 Próximos passos:
   1. Abrir saida/score_justification.pdf no Preview/Acrobat
   2. Validar Cliente Exemplo S.A. e os scores aparecem corretos
   3. Compartilhar PDFs com liderança
```

## Customization patterns

### Pattern 1: Personalize Implementation Guide (Part 4)
```
/wizard-implementacao    # 9 steps, gera implementation-guide-inputs.json
/gerar-relatorio         # re-renderiza com Parte 4 personalizada
```

### Pattern 2: Personalize narrative fields (capabilities, risks, etc.)
```bash
# 1. Render once to create payload.json
/gerar-relatorio

# 2. Edit saida/payload.json manually:
#    - capabilities[].scoring_rationale (replace sample text)
#    - capabilities[].h1_initiatives (replace with client-specific actions)
#    - technology_resources_per_pillar (customize tools)
#    - risks_per_pillar (real risks identified)
#    - success_metrics_per_pillar (real KPIs being tracked)

# 3. Re-render only (skip merge):
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida
```

### Pattern 3: Different language
```bash
# Edit respostas.json::metadata.language to "en", "es" or "pt-br"
/gerar-relatorio   # re-renders in selected locale
```

## Branding (paulasilva-ms)

The script automatically injects **paulasilva-ms branding** into the payload (replaces the sample's default branding block):

- `payload.branding.name` = "Paula Silva | Software Global Black Belt"
- `payload.branding.contact` = "paulasilva@microsoft.com"
- `payload.branding.tagline` = "Building the future of software development with AI and Agentic DevOps"
- `payload.branding.palette` = MS 4-color (#00A4EF, #7FBA00, #FFB900, #F25022)

The CSS used (`relatorios/templates/_print.css`) already uses the MS palette in `:root` tokens. So all 5 PDFs render with:
- Primary color = MS Blue
- Positive = MS Green · Warn = MS Yellow · Critical = MS Red
- Pillar accents: P1 = Blue, P2 = Yellow, P3 = Green
- Inter font for body, JetBrains Mono for code/labels

The branding is consistent with the chrome bar shown in the kit's interactive HTMLs (calculadora, formulários, wizard). See `referencia/branding/IDENTITY.md` for canonical strings + logo SVG.

## Constraints

- **DO NOT modify** files in `relatorios/templates/` (mirror official platform code).
- **DO NOT regenerate** payload.json structure from scratch — always start from `sample_payload.json`.
- **DO NOT skip** the script — running Jinja2 manually misses i18n + CSS + WeasyPrint setup.
- WeasyPrint must be installed: `pip install --user --break-system-packages weasyprint jinja2 openpyxl`.
- macOS may need: `brew install cairo pango gdk-pixbuf libffi`.
- Outputs in `saida/` only.

## What the script does NOT do (yet)

The current implementation **preserves placeholder data** from `sample_payload.json` for fields we don't have structured client data for:
- `executive_steering_committee` (5 names of Acme leaders)
- `tpo.program_manager` and `members`
- `raci_matrix` (5 activities)
- `communication_plan` / `training_plan`
- `adkar_notes` (long narrative)
- `quick_wins_w1_4` / `w5_8` / `w9_12`
- `risks_per_pillar`
- `success_metrics_per_pillar`
- `next_steps_per_pillar` (text)
- Per-capability `scoring_rationale`, `h1_initiatives`, `evidence_collected`, `h2_key_enabler`, etc.

**Workaround:** the wizard data flows in via `implementation-guide-inputs.json` for the steering/RACI/comms/training/ADKAR/quick wins. For the rest, the client edits `saida/payload.json` and re-renders.

**Future improvement:** a `/personalizar-narrativa` skill could prompt the client through each capability's narrative fields, replacing sample placeholders one by one.

## Reference example

The folder `referencia/exemplo-saida/` contains 5 PDFs generated from `respostas.json.example` (Cliente Exemplo S.A.) with the exact algorithm above. Compare these to confirm fidelity when you run `/gerar-relatorio` with your data.

## Troubleshooting

| Problem | Solution |
|---|---|
| `weasyprint not found` | `pip install --user --break-system-packages weasyprint` |
| `cairo / pango missing` (Mac) | `brew install cairo pango gdk-pixbuf libffi` |
| `StrictUndefined: 'X' is undefined` (rare) | Sample payload missing a field — open issue or add to sample |
| PDF still shows "Acme Insurance" | `respostas.json::metadata.organization` is empty — fix and re-run |
| PDF still has "James Carter" in Part 4 | Run `/wizard-implementacao` to replace steering committee placeholders |
| Wrong language | Edit `respostas.json::metadata.language` (en / es / pt-br) and re-run |
