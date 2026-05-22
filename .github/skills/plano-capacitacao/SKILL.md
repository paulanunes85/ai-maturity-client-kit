---
name: plano-capacitacao
description: Generates a prioritized capacitation roadmap (plano de capacitação) from the Learning & Growth Survey responses. Reads survey-learning/respostas-learning.json (IDENTIFIED respondents with name+email) and produces saida/plano-capacitacao-<DATE>.md with: top 10 topics demanded, suggested cohorts per dimension D2-D8 (with attendee lists), Champions Network candidates, mentor↔mentee pairs, calendar of workshops, barriers to remove, capacitation roadmap, training plan. Use after /importar-survey-learning when user asks for "plano de capacitação", "training roadmap", "Champions Network", "workshops priorizados", "treinamento", "capacitation plan", "plano-capacitacao".
---

# Skill: Generate Capacitation Plan from Learning Survey

## When to use
- After `/importar-survey-learning` (depends on `survey-learning/respostas-learning.json`)
- When liderança quer **plano acionável** de treinamento + Champions + workshops
- Output feeds `/wizard-implementacao` (alimenta steps de Training Plan, ADKAR, Quick Wins)

## Inputs
- `survey-learning/respostas-learning.json` — respondentes identificados + respostas
- `survey-learning/perguntas-para-forms-learning.md` — schema reference
- (optional) `saida/maturidade-developer-survey-<DATE>.json` — para cross-reference com maturidade real
- (optional) `saida/scores.json` — capabilities do assessment principal (P1-C1 etc.)

## Expected output
- `saida/plano-capacitacao-<DATE>.md` — plano completo PT-BR (15+ seções, ~10 páginas eq.)
- Brief chat summary (PT-BR): N respondentes, top 5 tópicos, N Champions, top 3 workshops sugeridos

## Procedure

### Implementation: invoke the official script

The skill should INVOKE the script that aggregates and generates the full plan:

```bash
python3 survey-learning/scripts/gerar_plano_capacitacao.py
```

This script:
1. Loads `survey-learning/respostas-learning.json`
2. Aggregates: priorities (L3-Q1), topics (L4), formats (L5), Champions (L6), barriers (L7), wishlist (L7)
3. Generates 12-section report in PT-BR with:
   - Top 10 topics with attendee names+emails
   - Cohorts per dimension D2-D8
   - Champions Network (3 tiers)
   - Mentor↔mentee pairs
   - Calendar 90 days
   - 5 prioritized actions
4. Outputs: `saida/plano-capacitacao-<DATE>.md`

**DO NOT reimplement aggregation in chat** — the script handles all of it deterministically.

### Manual fallback (if user asks)

```python
import json
data = json.load(open("survey-learning/respostas-learning.json"))
n = data["metadata"]["total_respondents"]
if n < 3:
    warn(f"Apenas {n} respondentes — plano será preliminar.")
```

### 2. Aggregate self-perception by dimension (L2)

For each dimension D2-D8, count how many respondents are at each L0-L4. This is the "**team perceived maturity**" (different from D2-D8 measured by `/insights-developer-survey`).

```python
from collections import Counter
self_perception = {}
for did in ["D2", "D3", "D4", "D5", "D6", "D7", "D8"]:
    qid = f"L2-Q{int(did[1])-1}"   # L2-Q1 = D2, L2-Q2 = D3, ...
    counts = Counter()
    for r in data["respondents"]:
        ans = r["responses"].get(qid, {}).get("value", "")
        # Extract level from "L0 — ..." pattern
        if ans.startswith("L0"): counts["L0"] += 1
        elif ans.startswith("L1"): counts["L1"] += 1
        elif ans.startswith("L2"): counts["L2"] += 1
        elif ans.startswith("L3"): counts["L3"] += 1
        elif ans.startswith("L4"): counts["L4"] += 1
    self_perception[did] = counts
```

### 3. Aggregate priority dimensions (L3-Q1)

Count which dimensions devs want to grow MOST:

```python
priorities = Counter()
for r in data["respondents"]:
    ans = r["responses"].get("L3-Q1", {}).get("value", "")
    for d in ["D2", "D3", "D4", "D5", "D6", "D7", "D8"]:
        if d in ans:
            priorities[d] += 1
```

### 4. Aggregate desired topics (L4-Q1 to L4-Q5)

Top 10 topics most-requested across all 5 question groups:

```python
topic_counts = Counter()
topic_to_attendees = {}  # topic -> list of (name, email)
for r in data["respondents"]:
    for qid in ["L4-Q1", "L4-Q2", "L4-Q3", "L4-Q4", "L4-Q5"]:
        topics = r["responses"].get(qid, {}).get("value", "").split(";")
        for t in topics:
            t = t.strip()
            if not t or "Já domino" in t or "Não tenho interesse" in t:
                continue
            topic_counts[t] += 1
            topic_to_attendees.setdefault(t, []).append((r["name"], r["email"]))
```

### 5. Aggregate format preferences (L5)

```python
formats = Counter()
for r in data["respondents"]:
    fmts = r["responses"].get("L5-Q1", {}).get("value", "").split(";")
    for f in fmts:
        formats[f.strip()] += 1

time_per_week = Counter()
for r in data["respondents"]:
    time_per_week[r["responses"].get("L5-Q2", {}).get("value", "")] += 1

cohort_pref = Counter()
for r in data["respondents"]:
    cohort_pref[r["responses"].get("L5-Q4", {}).get("value", "")] += 1
```

### 6. Identify Champions candidates (L6-Q1)

```python
champions = []
for r in data["respondents"]:
    ans = r["responses"].get("L6-Q1", {}).get("value", "")
    if ans.startswith("Sim — quero ser Champion ativo"):
        champions.append({"name": r["name"], "email": r["email"], "tier": "active"})
    elif "Sim — mas só se tiver suporte" in ans:
        champions.append({"name": r["name"], "email": r["email"], "tier": "supported"})
    elif ans.startswith("Talvez"):
        champions.append({"name": r["name"], "email": r["email"], "tier": "maybe"})
```

### 7. Identify mentor↔mentee pairs

```python
mentees = []  # who wants mentoring
mentors = []  # who offers to mentor

for r in data["respondents"]:
    if "Sim" in r["responses"].get("L6-Q3", {}).get("value", ""):
        mentees.append({"name": r["name"], "email": r["email"]})
    if "Sim" in r["responses"].get("L6-Q4", {}).get("value", ""):
        topic = r["responses"].get("L6-Q5", {}).get("value", "")
        mentors.append({"name": r["name"], "email": r["email"], "topic": topic})

# Cross-reference with referenced people in L6-Q2 ("quem você considera referência")
references = Counter()
for r in data["respondents"]:
    ref = r["responses"].get("L6-Q2", {}).get("value", "").strip()
    if ref and len(ref) > 2:
        references[ref] += 1
```

### 8. Aggregate barriers (L7-Q1)

```python
barriers = Counter()
for r in data["respondents"]:
    bs = r["responses"].get("L7-Q1", {}).get("value", "").split(";")
    for b in bs:
        if b.strip() and "sem barreiras" not in b.lower():
            barriers[b.strip()] += 1
```

### 9. Build the report

Structure (PT-BR):

```markdown
# Plano de Capacitação IA — Roadmap Personalizado

**Data:** {date} · **Respondentes:** {n} (identificados)

---

## 1 · Sumário Executivo

### Maturidade IA percebida pelo time (auto-avaliação L2)
| Dimensão | L0 | L1 | L2 | L3 | L4 | Mediana |
|---|---|---|---|---|---|---|
| D2 Copilot | 2 | 5 | 3 | 1 | 0 | L1 |
| D3 Tooling | ... |
...

### Top 3 dimensões PRIORITÁRIAS para crescer (L3-Q1)
1. D5 Agent Concepts (8 votos)
2. D2 Copilot Adoption (6 votos)
3. D8 Security (5 votos)

### Top 10 tópicos mais demandados (L4)
1. Coding Agent autônomo (10 devs)
2. SDD com Spec Kit (8 devs)
...

### Champions Network identificados
- 3 ativos · 2 com suporte · 4 maybe
- Top 3 referências mencionadas: {nomes}

### 3 quick wins recomendados
1. **Workshop Coding Agent (4h)** — 10 inscritos pre-validados
2. **Cohort Spec Kit (6 semanas, self-paced)** — 8 inscritos
3. **Office hours quinzenal** — atende 100% dos respondentes

---

## 2 · Tópicos demandados — Top 10 (com lista de inscritos pré-validados)

### 1. Coding Agent autônomo (D5) — 10 inscritos
**Demanda:** 10/12 devs (83%)
**Workshop sugerido:** 4h hands-on
**Pré-requisito:** L1+ em D5 (Agent Concepts)
**Inscritos pré-validados** (pré-confirmados na resposta):
- Maria Silva (maria@...)
- João Santos (joao@...)
...

**Ação:** agendar workshop em ≤30 dias. Convidar Maria como Champion (já se candidatou em L6-Q1).

### 2. SDD com Spec Kit (D4) — 8 inscritos
...

(Repetir para top 10)

---

## 3 · Cohorts sugeridos por dimensão da rubrica

### Cohort D5 (Agent Concepts)
- 8 devs querem evoluir
- Formato preferido por eles: workshop hands-on (5/8) + cohort (4/8)
- Cadência: 4-6h/semana (60%)
- **Plano:** cohort de 6 semanas com 5 sessões síncronas + lab self-paced
- **Tópicos:** custom agents, MCP, A2A, handoffs, testes de agents
- **Champion candidato:** Maria Silva (já se candidatou + L3 self-perceived)

(Repetir por D2, D3, D4, D6, D7, D8 conforme demanda)

---

## 4 · Champions Network

### Ativos (já querem ser Champion sem precisar de suporte adicional) — 3 pessoas
| Nome | Email | Tópicos sugeridos | Próximo passo |
|---|---|---|---|
| Maria | maria@... | D5 Agents, D2 Copilot | Convidar para train-the-trainer |
| ...

### Com suporte (querem ser Champions se tiverem treino dedicado) — 2 pessoas
...

### Mentor candidates (se ofereceram a mentorar em L6-Q4-Q5)
| Nome | Tópico que ensina | N candidatos a mentee |
|---|---|---|
| ...

### Mentees (querem mentoria 1:1 ou peer)
...

### Referências naturais (mencionados em L6-Q2)
- "João Santos" mencionado por 4 pessoas — Champion natural não declarado, contatar
- ...

---

## 5 · Calendário sugerido de workshops (próximos 90 dias)

| Semana | Workshop | Audiência | Champion | Formato |
|---|---|---|---|---|
| W1 | Kick-off Champions Network | 5 | Você (Eng Mgr) | 2h síncrono |
| W2 | Workshop Coding Agent | 10 | Maria | 4h hands-on |
| W3 | Cohort SDD/Spec Kit kickoff | 8 | TBD | 1h síncrono |
| ...

---

## 6 · Formato e cadência preferidos pelo time

### Formatos top
1. Workshop hands-on 3-4h (X% pediram)
2. Office hours semanais (Y%)
3. Pair programming com Champion (Z%)
...

### Tempo disponível por semana (mediana)
2-4h/semana

### Cohort vs self-paced
60% cohort · 40% self-paced (recomendado: híbrido)

---

## 7 · Barreiras a remover (priorizado)

1. **Falta de tempo** ({N}/{total} mencionaram) → ação: bloquear 2h/semana no calendário do time
2. **Falta de licença Copilot** ({N}) → ação: revisar licenças com TI, target 100% até Q+1
3. **Falta de Champion** ({N}) → ação: ativar Champions Network identificados na seção 4
4. **Não sei por onde começar** ({N}) → ação: criar learning path documentado em Copilot Space compartilhado

---

## 8 · Wishlist e ideias do time (L7-Q2 a Q4)

### Workshops sugeridos pelo time (L7-Q2)
> "{quote 1}"
> "{quote 2}"
...

### Palestrantes externos sugeridos (L7-Q3)
- {nome 1}: mencionado por X
- ...

### Outras sugestões livres (L7-Q4)
> "{quote relevante}"

---

## 9 · 🔗 Conexão com outros surveys

### vs. Maturidade do team (Developer Survey - rubrica determinística)
| Dimensão | Self-perception (L2) | Rubrica medida (D-X) | Dissonância |
|---|---|---|---|
| D2 Copilot | mediana L1 | 0.80 (L1) | ✓ alinhado |
| D5 Agents | mediana L1 | 2.56 (L3) | ⚠ underconfidence! |
| D8 Security | mediana L2 | 1.92 (L2) | ✓ alinhado |
...

> **Insight:** time é mais maduro em D5 do que percebe. Pode aproveitar Champions internos para mentorar.

### vs. Capabilities do assessment principal
| Capability | Score assessment | Demanda do time | Recomendação |
|---|---|---|---|
| P1-C1 Copilot | L3 (líder) | 6 devs querem evoluir | Workshop validado pelo plano |
| P3-C5 Apps Agênticas | L1 (gap) | 8 devs querem evoluir | **Match perfeito** — priorizar |

---

## 10 · 🎯 Top 5 ações priorizadas

Ranqueadas por: impacto (n_demand) × facilidade (cohort/champion já mapeado) × alinhamento com gaps do assessment.

1. **Workshop Coding Agent (W2)** — 10 inscritos × Champion identificado × addresses P1-C1 gap
2. **Cohort SDD com Spec Kit (W3-W8)** — 8 inscritos × cobre D4 + P3-C5
3. **Champions Kickoff (W1)** — ativa rede de 5 Champions identificados
4. **Office hours quinzenal (W2+)** — atende barreira "não sei por onde começar"
5. **Revisão de licenças** (TI) — remove barreira de licença, eleva D2

---

## 11 · 📅 Próximos 30 dias

- **Semana 1:** Champions Kickoff + agendamento de workshops
- **Semana 2:** Workshop Coding Agent (Maria)
- **Semana 3:** Cohort SDD início + Office hours #1
- **Semana 4:** Retrospectiva + ajustes do plano

---

## 12 · 📋 Apêndice: respondentes (visível só para liderança)

> ⚠️ Este apêndice contém nomes/emails. **NÃO compartilhar publicamente** — só usar para convites de workshops.

| Nome | Email | Cargo | Self-perception média | Disponível? | Quer Champion? |
|---|---|---|---|---|---|
| Maria | maria@... | Tech Lead | L2.7 | 4-6h/sem | Sim ativo |
...

(N respondentes total)
```

### 10. Report in chat (PT-BR)

```
✓ Plano de capacitação → saida/plano-capacitacao-2026-05-08.md (~10 páginas)

📊 Resumo:
   • 12 respondentes IDENTIFICADOS
   • Top demand: Coding Agent (10) · SDD com Spec Kit (8) · Spaces (7)
   • Champions identificados: 3 ativos + 2 com suporte
   • Mentor candidates: 4 · Mentee candidates: 6
   • Top barreira: falta de tempo (8/12 mencionaram)

🎯 5 ações priorizadas (próximos 30 dias):
   1. Champions Kickoff (W1)
   2. Workshop Coding Agent (W2) — 10 inscritos
   3. Cohort SDD com Spec Kit (W3) — 8 inscritos
   4. Office hours quinzenal (W2+)
   5. Revisar licenças Copilot (TI)

📋 Próximo: /wizard-implementacao usa este plano em training_plan + adkar_notes + quick_wins
```

## Constraints

- Survey é **IDENTIFICADO** — pode citar nomes/emails NO RELATÓRIO mas só na seção "Apêndice — visível para liderança"
- **NÃO** envie emails automaticamente — apenas liste nomes para o líder convidar manualmente
- **NÃO** invente tópicos fora do que foi respondido
- Cross-reference com `/insights-developer-survey` e `/calcular-scores` quando ambos existirem (compara percepção vs realidade)
- Output em `saida/plano-capacitacao-<DATE>.md` apenas
- Se respondente não preencheu nome OU email, contar mas marcar como "anônimo (incompleto)" — não inventar
