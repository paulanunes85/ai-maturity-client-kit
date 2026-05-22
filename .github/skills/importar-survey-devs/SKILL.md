---
name: importar-survey-devs
description: Imports the Developer Survey results (Microsoft Forms export .xlsx) into structured JSON. The survey has 75 questions across 9 sections (Profile, Copilot adoption + modes, MS/GitHub tools, AI dev practices, Agent concepts, Markdown/Instructions, Usability, Security/Governance, Pain points). Different from /importar-respostas-excel which handles the maturity assessment. Use when user has respostas-survey-devs.xlsx and wants to analyze it.
argument-hint: optional path to .xlsx (default: respostas-survey-devs.xlsx at root)
---

# Skill: Import Developer Survey responses

## When to use
- User collected responses for the **Developer Survey** (anonymous, individual, behavioral) via Microsoft Forms
- File `respostas-survey-devs.xlsx` exists at workspace root (or path passed by user)
- Output feeds `/insights-developer-survey` for aggregated reporting

## Inputs
- **Excel**: `respostas-survey-devs.xlsx` at workspace root (default)
- **`survey-devs/perguntas-para-forms-devs.md`**: reference for question schema (75 questions in 9 sections)
- Optional: schema validator at `survey-devs/respostas-mock-devs.json` (sample structure)

## Expected output
- **`survey-devs/respostas-devs.json`**: structured JSON with all respondents and answers
- **`saida/import-survey-log-<DATE>.md`**: log of import (respondent count, parse warnings, missing questions)

## Expected Excel format (Microsoft Forms anonymous export)

```
| A   | B          | C               | D     | E    | F                | G                |
| ID  | Start time | Completion time | Email | Name | S1-Q1: <text>    | S1-Q2: <text>    |
| 1   | timestamp  | timestamp       |       |      | "Backend Dev"    | "6-10 anos"      |
| 2   | ...        | ...             |       |      | "SRE"            | "11-15 anos"     |
```

Headers MUST start with `S[1-9]-Q\d+:` pattern. Email/Name are typically empty (anonymous form).

## Procedure

### 1. Locate Excel

```python
caminho = arg or "respostas-survey-devs.xlsx"
if not (KIT / caminho).exists():
    error: "Arquivo não encontrado. Veja survey-devs/INSTRUCOES-FORMS-DEVS.md"
```

### 2. Parse headers

```python
import re, openpyxl
qid_pattern = re.compile(r"^(S[1-9]-Q\d+):")
wb = openpyxl.load_workbook(caminho)
ws = wb.active

col_to_qid = {}
for col_idx, header_cell in enumerate(ws[1], start=1):
    val = str(header_cell.value or "").strip()
    m = qid_pattern.match(val)
    if m:
        col_to_qid[col_idx] = m.group(1)

# Validate: should be ~75 questions
if len(col_to_qid) < 50:
    warn(f"Apenas {len(col_to_qid)} questões detectadas (esperado ~69). Verifique formato dos headers.")
```

### 3. Detect question types from `survey-devs/perguntas-para-forms-devs.md`

Each question is `choice` (single value), `multi` (semicolon-separated), or `text` (long string). The skill should know the type of each qid to parse correctly. Hardcoded mapping or read from companion JSON.

### 4. Collect responses per respondent

```python
respondents = []
for row_idx in range(2, ws.max_row + 1):
    row = ws[row_idx]
    # Anonymous: skip if any qid column is filled
    has_response = any(
        row[col - 1].value for col in col_to_qid
    )
    if not has_response:
        continue
    
    r = {"respondent_id": row_idx - 1, "responses": {}}
    for col, qid in col_to_qid.items():
        val = row[col - 1].value
        if val is None:
            continue
        # Multi-answer Forms exports as "Option1; Option2; Option3"
        # Skill stores raw — analysis splits later
        r["responses"][qid] = {"value": str(val).strip()}
    respondents.append(r)
```

### 5. Output `survey-devs/respostas-devs.json`

```json
{
  "metadata": {
    "source": "respostas-survey-devs.xlsx",
    "imported_at": "2026-05-08T14:30:00Z",
    "total_respondents": 12,
    "total_questions_detected": 69,
    "anonymous": true
  },
  "respondents": [
    {
      "respondent_id": 1,
      "responses": {
        "S1-Q1": {"value": "Desenvolvedor Backend"},
        "S1-Q2": {"value": "6-10 anos"},
        "S2-Q1": {"value": "Sim — Copilot Enterprise"},
        "S2-Q3": {"value": "Ask (responder perguntas); Edit (edição inline); Agent (multi-arquivo, autônomo)"},
        ...
      }
    }
  ]
}
```

### 6. Generate log `saida/import-survey-log-<DATE>.md`

```markdown
# Import log — Developer Survey ({DATE})

## Resumo
- Arquivo: respostas-survey-devs.xlsx
- Respondentes: 12 (anônimos)
- Questões detectadas: 69 / 69 (100%)
- Saída: survey-devs/respostas-devs.json

## Cobertura por seção
| Seção | Respostas | % |
|---|---|---|
| S1 (Perfil) | 84/84 | 100% |
| S2 (Copilot) | 105/108 | 97% |
...

## Alertas
- (nenhum) ou listagem de problemas

## Próximo
Rode `/insights-developer-survey` para gerar relatório agregado.
```

## Report in chat (PT-BR)

```
✓ Survey importado → survey-devs/respostas-devs.json
   12 respondentes anônimos, 69 questões processadas

📊 Cobertura: 95% (algumas perguntas pulada por respondentes)
⚠️ 0 alertas

🎯 Próximo: /insights-developer-survey  → gera relatório consolidado
```

## Constraints

- **NEVER** modify `survey-devs/perguntas-para-forms-devs.md` or template Excel.
- **NEVER** capture or store names/emails — survey is anonymous (Forms config).
- If the Excel has Email/Name columns FILLED, warn the user (Forms anonymity not enforced) but proceed.
- Output to `survey-devs/respostas-devs.json` (not `saida/`) — this is INPUT for the insights skill, not the final output.
- Different from `/importar-respostas-excel` (assessment maturity Likert). Don't confuse the schemas.
