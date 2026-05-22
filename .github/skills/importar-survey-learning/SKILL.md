---
name: importar-survey-learning
description: Imports the Learning & Growth Survey results (Microsoft Forms export .xlsx, IDENTIFIED with name+email) into structured JSON. The survey has 32 questions across 7 sections (identification, self-perception of maturity, growth priorities, topics to learn, formats/cadence, champions, barriers/wishlist). Different from /importar-survey-devs (anonymous). Use when the user has respostas-survey-learning.xlsx and wants to generate the capacitation plan, or asks "importar survey de aprendizado", "importar Learning & Growth", "respostas-survey-learning.xlsx", "survey de treinamento", "survey-learning", "import learning survey", "import training survey", "learning & growth import".
argument-hint: optional path to .xlsx (default: respostas-survey-learning.xlsx at root)
---

# Skill: Import Learning & Growth Survey responses

## When to use
- Client collected Learning & Growth Survey via Microsoft Forms (IDENTIFIED — name+email per response)
- File `respostas-survey-learning.xlsx` exists at workspace root
- Output feeds `/plano-capacitacao` for the prioritized training roadmap

## Inputs
- **Excel**: `respostas-survey-learning.xlsx` at workspace root (default)
- **`survey-learning/perguntas-para-forms-learning.md`**: schema reference (32 questions in 7 sections)

## Expected output
- **`survey-learning/respostas-learning.json`**: structured JSON with all respondents (IDENTIFIED with name+email) and answers
- **`saida/import-learning-log-<DATE>.md`**: log (respondent count, parse warnings, missing fields)

## Expected Excel format (Microsoft Forms IDENTIFIED export)

```
| A   | B          | C               | D                       | E              | F                | G                |
| ID  | Start time | Completion time | Email                   | Name           | L1-Q1: Nome      | L1-Q2: Email     |
| 1   | timestamp  | timestamp       | maria@cliente.com       | Maria Silva    | "Maria Silva"    | "maria@..."     |
```

Headers MUST start with `L[1-7]-Q\d+:` pattern.

## Procedure

Same parser pattern as `/importar-survey-devs`, but:
- **DOES NOT validate anonymity** — Email and Name are EXPECTED to be filled
- Header pattern: `L[1-7]-Q\d+:` (not `S[1-9]-Q\d+:`)
- Output schema includes `name` and `email` per respondent

```python
import re, openpyxl
qid_pattern = re.compile(r"^(L[1-7]-Q\d+):")
wb = openpyxl.load_workbook(caminho)
ws = wb.active

col_to_qid = {}
for col_idx, header_cell in enumerate(ws[1], start=1):
    val = str(header_cell.value or "").strip()
    m = qid_pattern.match(val)
    if m:
        col_to_qid[col_idx] = m.group(1)

if len(col_to_qid) < 25:
    warn(f"Apenas {len(col_to_qid)} questões detectadas (esperado ~32). Verifique formato dos headers.")

respondents = []
for row_idx in range(2, ws.max_row + 1):
    row = ws[row_idx]
    email = str(row[3].value or "").strip()
    name = str(row[4].value or "").strip()
    # Sometimes name/email are also captured by L1-Q1 / L1-Q2 (better source)
    if not name or not email:
        # Try to get from L1-Q1, L1-Q2 columns
        for col, qid in col_to_qid.items():
            if qid == "L1-Q1" and not name:
                name = str(row[col - 1].value or "").strip()
            if qid == "L1-Q2" and not email:
                email = str(row[col - 1].value or "").strip()
    
    if not name and not email:
        continue  # skip empty rows
    
    r = {
        "respondent_id": row_idx - 1,
        "name": name,
        "email": email,
        "responses": {},
    }
    for col, qid in col_to_qid.items():
        val = row[col - 1].value
        if val is None:
            continue
        r["responses"][qid] = {"value": str(val).strip()}
    respondents.append(r)
```

## Output JSON schema

```json
{
  "metadata": {
    "source": "respostas-survey-learning.xlsx",
    "imported_at": "2026-05-08T14:30:00Z",
    "total_respondents": 12,
    "total_questions_detected": 32,
    "anonymous": false,
    "scope": "individual_identified"
  },
  "respondents": [
    {
      "respondent_id": 1,
      "name": "Maria Silva",
      "email": "maria@cliente.com.br",
      "responses": {
        "L1-Q3": {"value": "Tech Lead"},
        "L2-Q1": {"value": "L3 — Uso Agent + Spaces, mensuro ganho"},
        "L3-Q1": {"value": "D5 — Agent Concepts; D8 — Security; D2 — Copilot Adoption"},
        "L4-Q1": {"value": "Coding Agent (autônomo no GitHub.com); Copilot Spaces; PR review com Copilot"},
        ...
      }
    }
  ]
}
```

## Report in chat (PT-BR)

```
✓ Survey de Learning importado → survey-learning/respostas-learning.json
   12 respondentes IDENTIFICADOS, 32 questões processadas

📊 Cobertura: 95%
👥 Champions candidates (L6-Q1 = Sim): 4 pessoas
📅 Top tópicos solicitados: ...

🎯 Próximo: /plano-capacitacao  → gera plano priorizado em saida/
```

## Constraints
- **NEVER** modify `survey-learning/perguntas-para-forms-learning.md` or template Excel
- **DO NOT** anonymize — this survey is identified by design (need names to invite to workshops)
- Output to `survey-learning/respostas-learning.json` (not `saida/`) — input for `/plano-capacitacao`
- Different from `/importar-survey-devs` (anonymous, schema `S[1-9]`); don't confuse
- If respondent's name/email is empty in BOTH columns D/E AND L1-Q1/L1-Q2, skip the row (incomplete)
