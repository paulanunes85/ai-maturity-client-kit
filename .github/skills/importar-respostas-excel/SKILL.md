---
name: importar-respostas-excel
description: Converts an Excel exported from Microsoft Forms (or Google Forms / multi-respondent spreadsheet) into structured respostas.json for the AI Maturity Assessment, aggregating multiple respondents via mean per question. Use when the client collected responses via Forms and wants to run the pipeline. Trigger on "importar respostas", "import Forms", "converter Excel para JSON", "respostas-forms.xlsx", "Microsoft Forms para o assessment", "agregar respondentes". Looks for respostas-forms.xlsx at workspace root or path passed by the user.
argument-hint: optional path of the .xlsx (default: respostas-forms.xlsx at root)
---

# Skill: Import responses from Excel (Microsoft Forms)

## When to use
- Client created a Microsoft Forms with the 158 questions and wants to import responses.
- Client has multiple respondents (3+) and wants automatic mean aggregation.
- Before running `/pipeline-completo` or `/calcular-scores` when input is Excel.

## Inputs
- **Excel**: `respostas-forms.xlsx` at workspace root (default) **or** path passed as argument.
- **`framework.json`**: to map column → qid and validate all 158 questions are present.
- **`coleta/perguntas-para-forms.md`**: reference if there's doubt about header format.

## Expected output
- **`respostas.json`** overwritten (with automatic backup at `respostas.json.backup-<timestamp>`).
- **`saida/import-log-<DATE>.md`**: import log (how many respondents, how many questions, conflicts resolved, alerts).

## Expected Excel format (Microsoft Forms export)

```
| A   | B          | C               | D       | E    | F                       | G                  | H                       |
| ID  | Start time | Completion time | Email   | Name | P1-C1-Q1: <question>    | Evidência (P1-C1-Q1) | P1-C1-Q2: <question>   |
| 1   | timestamp  | timestamp       | x@y.com | João | L3 — Gerenciado — ...   | "evidence text"    | L2 — Definido — ...    |
| 2   | ...        | ...             | ...     | Ana  | L4 — Otimizando — ...   | "text"             | (empty = didn't answer) |
```

- **Row 1** = headers
- **Rows 2+** = one respondent per row
- **Columns F+** alternate: question (Choice) → evidence (Long Text) → next question...
- **Question header** ALWAYS starts with `qid` in pattern `P[1-3]-C[1-9][0-9]?-Q[1-9][0-9]?:`

## Procedure

### 1. Locate and validate Excel

```python
path = user_argument or "respostas-forms.xlsx"
if not exists → error: "Não encontrei o arquivo. Verifique o caminho ou rode com /importar-respostas-excel <caminho>"
```

### 2. Extract column → qid mapping

```python
import re, openpyxl
wb = openpyxl.load_workbook(path)
ws = wb.active
qid_pattern = re.compile(r"^(P[1-3]-C\d+-Q\d+):")
col_to_qid = {}
col_to_evidence_qid = {}
for col_idx, header_cell in enumerate(ws[1], start=1):
    val = str(header_cell.value or "").strip()
    m = qid_pattern.match(val)
    if m:
        col_to_qid[col_idx] = m.group(1)
    elif val.startswith("Evidência ("):
        em = re.match(r"Evidência \(([^)]+)\)", val)
        if em:
            col_to_evidence_qid[col_idx] = em.group(1)
```

Validate: `len(col_to_qid)` should be close to 158. If < 100, alert and stop.

### 3. Map option → level

```python
def parse_level(cell_value):
    """Forms exports the FULL option. E.g.: 'L3 — Gerenciado — >75% com métricas'.
       Take first 2 chars."""
    if not cell_value:
        return None
    s = str(cell_value).strip()
    if s.startswith("L0"): return 0
    if s.startswith("L1"): return 1
    if s.startswith("L2"): return 2
    if s.startswith("L3"): return 3
    if s.startswith("L4"): return 4
    if s.startswith("NA") or s.lower() in ("não sei", "n/a", "na"):
        return None  # explicit not applicable
    return None  # unknown — log warning
```

### 4. Collect responses per respondent

```python
respondents = []
for row in ws.iter_rows(min_row=2, values_only=False):
    name = row[4].value if len(row) > 4 else ""
    email = row[3].value if len(row) > 3 else ""
    if not name and not email:
        continue
    
    r = {"name": name, "email": email, "responses": {}}
    for col_idx, qid in col_to_qid.items():
        cell = row[col_idx - 1]
        level = parse_level(cell.value)
        if level is None and cell.value:
            log_warning(f"{name}: unrecognized value at {qid}: {cell.value!r}")
        evidence = ""
        ev_col = next((c for c, q in col_to_evidence_qid.items() if q == qid), None)
        if ev_col:
            ev_cell = row[ev_col - 1]
            evidence = str(ev_cell.value or "").strip()
        if level is not None or evidence:
            r["responses"][qid] = {"level": level, "evidence": evidence}
    respondents.append(r)
```

### 5. Aggregate per question (rule: mean of levels, concatenate evidences)

```python
agg = {}
for qid in framework_qids:
    levels = [r["responses"][qid]["level"] for r in respondents
              if qid in r["responses"] and r["responses"][qid]["level"] is not None]
    evidences = [
        f"[{r['name']}]: {r['responses'][qid]['evidence']}"
        for r in respondents
        if qid in r["responses"] and r["responses"][qid].get("evidence")
    ]
    if levels:
        # IMPORTANT: aligned with scoring.rs algorithm:
        #   selected_level = AVG(all respondents who answered)
        #   no per-respondent weight
        agg_level = sum(levels) / len(levels)
    else:
        agg_level = None
    agg[qid] = {
        "level": agg_level,
        "evidence": "\n".join(evidences) if evidences else "",
        "n_respondents": len(levels),
    }
```

### 6. Generate respostas.json

```python
import shutil, datetime
ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S")
if (KIT / "respostas.json").exists():
    shutil.copy(KIT / "respostas.json", KIT / f"respostas.json.backup-{ts}")

template = json.load(open(KIT / "respostas.json"))
template["metadata"] = {
    "respondent_name": f"Agregado de {len(respondents)} respondentes",
    "respondent_email": "—",
    "respondent_role": "Multi-respondente",
    "audience": ["all"],
    "organization": "<extracted from Forms or filled manually>",
    "assessment_date": datetime.date.today().isoformat(),
    "language": "pt-BR",
    "source": "microsoft-forms-import",
    "respondents": [{"name": r["name"], "email": r["email"]} for r in respondents],
}
for qid, body in agg.items():
    if qid in template["responses"]:
        template["responses"][qid]["level"] = body["level"]
        template["responses"][qid]["evidence"] = body["evidence"]

json.dump(template, open(KIT / "respostas.json", "w"), ensure_ascii=False, indent=2)
```

### 7. Generate import log (in PT-BR, written to saida/)

```markdown
# Import log — {DATE}

## Resumo
- Arquivo importado: respostas-forms.xlsx
- Respondentes: {N} ({names})
- Questões processadas: {X} / 158
- Questões com pelo menos 1 resposta: {Y}
- Backup do respostas.json anterior: respostas.json.backup-{TS}

## Cobertura por respondente
| Respondente       | Email            | Respondidas | Evidências |
|-------------------|------------------|-------------|------------|
| Maria Tech Leader | maria@...com.br  | 46 / 158    | 46         |

## Alertas
- {row N: unrecognized value at P2-C4-Q3 → "talvez" — treated as null}
- {question P3-C5-Q4 with no answer from any respondent — stays null in respostas.json}

## Próximo passo
Rode `/pipeline-completo` para calcular scores e gerar relatório.
```

## Report in chat (PT-BR)

```
✓ Importação concluída → respostas.json (atualizado)
✓ Backup: respostas.json.backup-20260508T144523
✓ Log: saida/import-log-2026-05-08.md

📥 Importados:
   • 3 respondentes: Maria Tech Leader, Joao Backend SRE, Ana Security Lead
   • 142 / 158 questões com pelo menos 1 resposta
   • 117 evidências capturadas

⚠️ 4 alertas (ver log) — valores não reconhecidos foram tratados como null

🎯 Próximo: /pipeline-completo
```

## Constraints
- **NEVER** modify `framework.json`.
- **ALWAYS** backup `respostas.json` before overwriting (`.backup-<timestamp>`).
- **NEVER** invent values: if the cell is empty or contains something unmappable, the result is `null`.
- If the Excel doesn't have any header starting with `P[1-3]-C\d+-Q\d+:`, stop and instruct the user to verify the format (maybe it's not a Forms export).
- Accept header variations: `P1-C1-Q1`, `P1-C1-Q1:`, `P1-C1-Q1 -`, `P1-C1-Q1 (...)` — always use regex.
- If there's a SINGLE respondent row, aggregation is trivial (original level); if multiple, use mean (aligned with `repos/scoring.rs:354-368`).

## Compatibility
- **Microsoft Forms** export → natively supported
- **Google Forms** → also works (similar column format; "Likert scale 0-4" maps the same)
- **Custom spreadsheet** → works as long as each question header starts with `P[1-3]-C\d+-Q\d+:`
- **Typeform** → exports CSV; convert to xlsx and adjust headers manually
