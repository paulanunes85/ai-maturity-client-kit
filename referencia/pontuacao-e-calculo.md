# Pontuação e Cálculo do Assessment de Maturidade IA

> **Documento técnico de referência** — descreve com precisão como cada resposta vira score, como capabilities/pillars/overall são agregados, regras de threshold, multi-respondente, gap analysis e PE score. Todas as fórmulas batem 1:1 com o código Rust em [`app/backend/src/scoring.rs`](../../app/backend/src/scoring.rs).

**Versão do algoritmo:** 1.0.0 · **Última auditoria do código:** 2026-05-08

---

## Índice

1. [Modelo conceitual em 3 camadas](#1-modelo-conceitual-em-3-camadas)
2. [Como cada resposta vira número](#2-como-cada-resposta-vira-número)
3. [Fórmulas oficiais](#3-fórmulas-oficiais)
4. [Tratamento de respostas faltantes](#4-tratamento-de-respostas-faltantes)
5. [Threshold de cobertura mínima](#5-threshold-de-cobertura-mínima)
6. [Multi-respondente — agregação](#6-multi-respondente--agregação)
7. [Rótulos de maturidade (mapping de score)](#7-rótulos-de-maturidade-mapping-de-score)
8. [Gap analysis e priorização](#8-gap-analysis-e-priorização)
9. [PE Score (Production Engineering Readiness)](#9-pe-score-production-engineering-readiness)
10. [Persistência (tabelas e materialização)](#10-persistência-tabelas-e-materialização)
11. [**Exemplo end-to-end — Pilar P1**](#11-exemplo-end-to-end--pilar-p1)
12. [**Exemplo end-to-end — Pilar P2**](#12-exemplo-end-to-end--pilar-p2)
13. [**Exemplo end-to-end — Pilar P3**](#13-exemplo-end-to-end--pilar-p3)
14. [Edge cases & garantias](#14-edge-cases--garantias)
15. [Glossário](#15-glossário)

---

## 1. Modelo conceitual em 3 camadas

```
┌─────────────────────────────────────────────────────────────┐
│                    OVERALL SCORE (0–4)                      │
│   = média ponderada de TODAS as capabilities (não pillars)  │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│                  PILLAR SCORE (P1, P2, P3)                  │
│        = média ponderada das capabilities do pillar         │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│                CAPABILITY SCORE (P1-C1 … P3-C9)             │
│          = média ponderada das questões da capability       │
└─────────────────────────────────────────────────────────────┘
                ▲
                │
┌─────────────────────────────────────────────────────────────┐
│              QUESTION RESPONSE (L0=0 … L4=4)                │
│       = nível selecionado pelo respondente (multi → média)  │
└─────────────────────────────────────────────────────────────┘
```

**Característica importante:** o **overall** é calculado direto sobre as capabilities (SUMPRODUCT), **não** é a média dos 3 pillar scores. Isso evita que um pilar com poucas capabilities pese igual a um com muitas.

---

## 2. Como cada resposta vira número

| Nível selecionado | Rótulo PT-BR | Valor numérico |
|---|---|---|
| L0 | Inicial | **0** |
| L1 | Em Desenvolvimento | **1** |
| L2 | Definido | **2** |
| L3 | Gerenciado | **3** |
| L4 | Otimizando | **4** |

A escala é **discreta na entrada (0–4 inteiro)** mas as agregações produzem valores **contínuos em ponto flutuante (`f64`)**, sem arredondamento. Apenas a apresentação (UI/relatório) decide a precisão visual (geralmente 2 casas decimais).

---

## 3. Fórmulas oficiais

### 3.1 Capability score
> Código de referência: [`scoring.rs:205-225`](../../app/backend/src/scoring.rs#L205)

$$
\text{capability\_score} = \frac{\sum_{q \in \text{respondidas}} (\text{nivel}_q \times \text{peso}_q)}{\sum_{q \in \text{respondidas}} \text{peso}_q}
$$

- Se nenhuma questão da capability foi respondida → `capability_score = None` (não entra nos cálculos superiores).
- Pesos default: **1.0**. Range permitido: **[0.5, 2.0]**.

### 3.2 Pillar score
> Código de referência: [`scoring.rs:227-247`](../../app/backend/src/scoring.rs#L227)

$$
\text{pillar\_score} = \frac{\sum_{c \in \text{pillar}} (\text{capability\_score}_c \times \text{peso}_c)}{\sum_{c \in \text{pillar}} \text{peso}_c}
$$

Apenas capabilities com `score = Some(_)` participam (capabilities sem nenhuma resposta são puladas).

### 3.3 Overall score
> Código de referência: [`scoring.rs:250-263`](../../app/backend/src/scoring.rs#L250)

$$
\text{overall\_score} = \frac{\sum_{c \in \text{TODAS as capabilities}} (\text{capability\_score}_c \times \text{peso}_c)}{\sum_{c \in \text{TODAS as capabilities}} \text{peso}_c}
$$

**Atenção:** SUMPRODUCT direto sobre todas as capabilities — **não** é `mean(P1, P2, P3)`.

---

## 4. Tratamento de respostas faltantes

| Situação | Comportamento |
|---|---|
| Questão não respondida | **Ignorada**. Não soma em `wsum` nem em `wtotal`. Sem penalização. |
| Capability sem nenhuma resposta | `score = None`. Não entra no pillar nem no overall. |
| Pillar sem capabilities respondidas | `pillar_score = 0.0` (caso de borda raro). |
| Overall sem capabilities respondidas | `overall_score = 0.0`. |

> **Regra de ouro:** "respondidas pesam, faltantes desaparecem". Isto incentiva o respondente a *não chutar* quando não sabe — o sistema só pune via `threshold_status`, não via score deflacionado.

---

## 5. Threshold de cobertura mínima

> Código de referência: [`scoring.rs:351-359`](../../app/backend/src/scoring.rs#L351)

| Questões aplicáveis | Status | Comportamento |
|---|---|---|
| **≥ 40** | `Ok` | Scoring normal, sem aviso. |
| **25–39** | `Warning` | Scoring calculado, mas relatório exibe banner "Resultado preliminar — confiabilidade limitada". |
| **< 25** | `Blocked` | Scoring **recusado**. API responde 422 `InsufficientData`. |

"Aplicáveis" = questões visíveis para a audience configurada do respondente (após filtro `audience`). Se um respondente é Backend, questões só de Frontend não contam.

---

## 6. Multi-respondente — agregação

> Código de referência: [`repos/scoring.rs:354-368`](../../app/backend/src/repos/scoring.rs#L354)

Quando mais de uma pessoa responde o mesmo assessment:

1. Para cada `question_id`, o sistema computa **`AVG(selected_level)`** sobre todos os respondentes que responderam aquela questão.
2. Esse valor médio (que pode ser fracionário, ex.: 2.67) entra como `nivel_q` na fórmula de capability score.
3. **Não há peso por respondente** — todo respondente vale igual.
4. **Não há estratificação por audience** — se Backend e Frontend respondem a mesma Q, a média mistura ambos.

**Exemplo:** 3 respondentes para Q1 com níveis 2, 4, 3 → `Q1 = (2+4+3)/3 = 3.0`.

---

## 7. Rótulos de maturidade (mapping de score)

> Código de referência: [`scoring.rs:361-373`](../../app/backend/src/scoring.rs#L361)

Aplicado a qualquer score (capability, pillar ou overall):

| Faixa de score | Rótulo | Cor (token) |
|---|---|---|
| `score < 0.5` | **L0 — Inicial** | `--color-l0` (vermelho) |
| `0.5 ≤ score < 1.5` | **L1 — Em Desenvolvimento** | `--color-l1` (âmbar) |
| `1.5 ≤ score < 2.5` | **L2 — Definido** | `--color-l2` (azul) |
| `2.5 ≤ score < 3.5` | **L3 — Gerenciado** | `--color-l3` (verde) |
| `score ≥ 3.5` | **L4 — Otimizando** | `--color-l4` (roxo) |

---

## 8. Gap analysis e priorização

> Código de referência: [`scoring.rs:307-349`](../../app/backend/src/scoring.rs#L307)

Para cada capability:

```
target_level   = target_overrides.get(capability_id) ou 3.0 (default L3)
gap_size       = target_level − current_score
priority_score = peso_capability × gap_size

Se gap_size ≤ 1e-9 (epsilon flutuante) → descarta (já atingiu meta)
```

### Classificação de prioridade

| `priority_score` | Rótulo | Significado |
|---|---|---|
| ≥ 2.4 | **P0** | Crítico — endereçar nos próximos 30 dias |
| ≥ 1.6 e < 2.4 | **P1** | Alto — incluir no próximo trimestre |
| ≥ 0.9 e < 1.6 | **P2** | Médio — backlog do semestre |
| < 0.9 | **P3** | Baixo — monitorar |

**Por que `weight × gap`?** Capabilities com peso 2.0 e gap 1.5 (priority_score = 3.0) são mais urgentes que peso 1.0 e gap 2.0 (priority_score = 2.0): o peso reflete impacto estratégico no overall.

---

## 9. PE Score (Production Engineering Readiness)

> Código de referência: [`scoring.rs:266-304`](../../app/backend/src/scoring.rs#L266)

Sub-score calculado **apenas com questões marcadas `pe = true`** no seed.

- Filtra → recalcula capability/pillar/overall com o subconjunto.
- Mesmo SUMPRODUCT.
- Se nenhuma questão tiver `pe = true` → retorna `None`.
- É exibido lado a lado com o overall geral, sinalizando prontidão para produção (resiliência, observabilidade, runbooks, SLOs etc.).

---

## 10. Persistência (tabelas e materialização)

> Migration de referência: [`migrations/20260417000000_initial.sql`](../../app/backend/migrations/20260417000000_initial.sql)

| Tabela | Colunas-chave | Quando é populada |
|---|---|---|
| `assessment_scores` | `overall_score`, `pe_score`, `total_applicable`, `total_answered`, `scored_at` | `POST /api/scoring/trigger` |
| `pillar_scores` | `pillar_id`, `score` | idem |
| `capability_scores` | `capability_id`, `score` (NULL se sem resposta), `weight` | idem |
| `gap_analysis` | `capability_id`, `current_score`, `target_level`, `gap_size`, `priority`, `priority_score` | idem |

`GET /api/scoring/results/{assessment_id}` lê **direto das tabelas materializadas** — não recalcula. Isso garante consistência entre relatórios e roadmaps gerados.

---

## 11. Exemplo end-to-end — Pilar P1

### Cenário
Capability **P1-C1 — Assistentes de Codificação IA** (5 questões). Avaliação respondida por **2 desenvolvedores** (R1 e R2). Todas as questões têm `weight = 1.0` (default).

### Respostas reais

| Questão | Pergunta (resumida) | R1 | R2 | **Avg** |
|---|---|---|---|---|
| `P1-C1-Q1` | Adoção de ferramentas de completação de código com IA | L3 (3) | L4 (4) | **3.5** |
| `P1-C1-Q2` | IA para revisão de código e melhoria de qualidade | L2 (2) | L3 (3) | **2.5** |
| `P1-C1-Q3` | IA para geração e manutenção de testes | L1 (1) | L2 (2) | **1.5** |
| `P1-C1-Q4` | Engenharia de prompt e gestão de templates | L2 (2) | L2 (2) | **2.0** |
| `P1-C1-Q5` | Governança e segurança das ferramentas IA | L3 (3) | L4 (4) | **3.5** |

### Passo 1 — Capability score (P1-C1)

```
wsum   = (3.5×1.0) + (2.5×1.0) + (1.5×1.0) + (2.0×1.0) + (3.5×1.0)
       = 3.5 + 2.5 + 1.5 + 2.0 + 3.5
       = 13.0

wtotal = 1.0 + 1.0 + 1.0 + 1.0 + 1.0 = 5.0

P1-C1.score = 13.0 / 5.0 = 2.60   →   Rótulo: L3 — Gerenciado
```

### Passo 2 — Pillar score (P1)

Suponha que P1-C1 é a única capability respondida do pilar P1, com `weight_capability = 1.0`:

```
ws = 2.60 × 1.0 = 2.60
wt = 1.0
P1.score = 2.60 / 1.0 = 2.60   →   Rótulo: L3 — Gerenciado
```

> Em assessment real, P1 tem 9 capabilities. O cálculo seria SUMPRODUCT sobre todas que tiverem ao menos 1 resposta.

### Passo 3 — Gap analysis

Default `target_level = 3.0`:

```
gap_size       = 3.0 − 2.60 = 0.40
priority_score = 1.0 × 0.40 = 0.40
classificação  = P3 (Baixo)   ← pois 0.40 < 0.9
```

### Passo 4 — Threshold

5 questões respondidas << 25 → **`threshold_status = Blocked`** se essa fosse a única capability avaliada. Em produção, espera-se ≥ 40 questões respondidas no assessment inteiro.

---

## 12. Exemplo end-to-end — Pilar P2

### Cenário
Capability **P2-C1 — Inteligência de Pipeline CI/CD** (6 questões). Respondida por **1 SRE** + **1 Platform Engineer**. Mistura de pesos: Q1 e Q5 com `weight = 1.5` (questões de impacto direto em DORA metrics).

### Respostas

| Questão | Pergunta (resumida) | Peso | SRE | PltEng | **Avg** |
|---|---|---:|---:|---:|---:|
| `P2-C1-Q1` | Otimização de pipeline CI/CD com IA | **1.5** | L4 (4) | L3 (3) | **3.5** |
| `P2-C1-Q2` | Self-healing builds e auto-correção | 1.0 | L2 (2) | L2 (2) | **2.0** |
| `P2-C1-Q3` | Análise preditiva de falhas | 1.0 | L1 (1) | L2 (2) | **1.5** |
| `P2-C1-Q4` | Otimização inteligente de cache | 1.0 | L2 (2) | L3 (3) | **2.5** |
| `P2-C1-Q5` | Métricas DORA e insights | **1.5** | L3 (3) | L4 (4) | **3.5** |
| `P2-C1-Q6` | Triagem automatizada de testes flaky | 1.0 | L2 (2) | L1 (1) | **1.5** |

### Passo 1 — Capability score (P2-C1)

```
wsum   = (3.5×1.5) + (2.0×1.0) + (1.5×1.0) + (2.5×1.0) + (3.5×1.5) + (1.5×1.0)
       = 5.25 + 2.0 + 1.5 + 2.5 + 5.25 + 1.5
       = 18.00

wtotal = 1.5 + 1.0 + 1.0 + 1.0 + 1.5 + 1.0 = 7.0

P2-C1.score = 18.00 / 7.0 = 2.5714…   →   Rótulo: L3 — Gerenciado
```

> **Observação:** sem os pesos extras em Q1 e Q5, a média simples seria `(3.5+2.0+1.5+2.5+3.5+1.5)/6 = 2.4167` → caía para L2. O peso 1.5 reflete que essas duas dimensões importam mais para o resultado de DevOps maduro.

### Passo 2 — Pillar score (P2) com 2 capabilities

Adicione P2-C2 (IaC) com score = 1.80, peso = 1.0:

```
ws = (2.5714 × 1.0) + (1.80 × 1.0) = 4.3714
wt = 1.0 + 1.0 = 2.0
P2.score = 4.3714 / 2.0 = 2.1857   →   Rótulo: L2 — Definido
```

### Passo 3 — Gap analysis (target customizado)

Para P2-C1, time de SRE definiu `target_level = 3.5` (acima do default):

```
gap_size       = 3.5 − 2.5714 = 0.9286
priority_score = 1.0 × 0.9286 = 0.9286
classificação  = P2 (Médio)   ← pois 0.9 ≤ 0.9286 < 1.6
```

---

## 13. Exemplo end-to-end — Pilar P3

### Cenário
Capability **P3-C5 — Aplicações Agênticas** (6 questões). Respondida por **1 Arquiteto** + **1 ML Engineer** + **1 Security**. Q1, Q3 e Q6 com `weight = 2.0` (pesos máximos — fronteira de inovação).

### Respostas

| Questão | Pergunta (resumida) | Peso | Arq | ML | Sec | **Avg** |
|---|---|---:|---:|---:|---:|---:|
| `P3-C5-Q1` | Implementação de agentes IA autônomos | **2.0** | L2 (2) | L3 (3) | L1 (1) | **2.0** |
| `P3-C5-Q2` | Coordenação multi-agente (orquestração) | 1.0 | L1 (1) | L2 (2) | L1 (1) | **1.33** |
| `P3-C5-Q3` | Frameworks de tool-use e function calling | **2.0** | L3 (3) | L4 (4) | L2 (2) | **3.0** |
| `P3-C5-Q4` | Memória persistente de agentes | 1.0 | L2 (2) | L2 (2) | L1 (1) | **1.67** |
| `P3-C5-Q5` | Avaliação contínua e safety guardrails | 1.0 | L1 (1) | L2 (2) | L3 (3) | **2.0** |
| `P3-C5-Q6` | Governança e auditoria de ações de agentes | **2.0** | L1 (1) | L1 (1) | L3 (3) | **1.67** |

### Passo 1 — Capability score (P3-C5)

```
wsum   = (2.00×2.0) + (1.33×1.0) + (3.00×2.0) + (1.67×1.0) + (2.00×1.0) + (1.67×2.0)
       = 4.00 + 1.33 + 6.00 + 1.67 + 2.00 + 3.34
       = 18.34

wtotal = 2.0 + 1.0 + 2.0 + 1.0 + 1.0 + 2.0 = 9.0

P3-C5.score = 18.34 / 9.0 = 2.0378…   →   Rótulo: L2 — Definido
```

### Passo 2 — Gap analysis (capability estratégica)

Liderança definiu `target_level = 4.0` (ambição: liderar no espaço agêntico) e capability tem `weight = 1.5`:

```
gap_size       = 4.0 − 2.0378 = 1.9622
priority_score = 1.5 × 1.9622 = 2.9433
classificação  = P0 (Crítico)   ← pois 2.9433 ≥ 2.4
```

→ Esta capability **entra no roadmap dos próximos 30 dias** com prioridade máxima.

### Passo 3 — Contribuição para overall

Se o assessment completo tem 28 capabilities ativas, P3-C5 com `score = 2.0378` e `weight = 1.5` contribui:
- Numerador overall: `+ 2.0378 × 1.5 = +3.0567`
- Denominador overall: `+ 1.5`

→ Subir P3-C5 de 2.04 para 3.5 (target prático L3) somaria `(3.5 − 2.04) × 1.5 = 2.19` ao numerador e elevaria o overall em ~`2.19 / wtotal_overall` pontos.

---

## 14. Edge cases & garantias

| Situação | Garantia |
|---|---|
| `wtotal = 0` (nenhuma questão respondida) | Retorna `None` (capability) ou `0.0` (pillar/overall). Nunca divide por zero. |
| Score acima de 4.0 | Impossível por construção — todos os níveis ∈ [0,4] e médias ponderadas preservam o range. |
| Score abaixo de 0.0 | Impossível — `selected_level ∈ [0,4]`. |
| `gap_size` negativo (já passou da meta) | Filtrado (não aparece no roadmap). |
| Multi-respondente com 0 respostas | Capability vira `None`, sem erro. |
| Respondente fora da audience | Suas respostas para questões não-aplicáveis são **ignoradas no scoring** mas armazenadas para auditoria. |
| Reprocessamento (recalcular após nova resposta) | Idempotente — `POST /api/scoring/trigger` substitui as 4 tabelas materializadas em uma transação. |

---

## 15. Glossário

| Termo | Definição |
|---|---|
| **Question** | Item de avaliação concreto. ID padrão `P[1-3]-C[1-19]-Q[1-99]`. |
| **Capability** | Subdomínio funcional. Agrupa 5–7 questões. |
| **Pillar** | Dimensão estratégica. Agrupa 9–10 capabilities. P1, P2 ou P3. |
| **Level (L0–L4)** | Maturidade de uma resposta individual. Inteiro 0–4. |
| **Score** | Resultado contínuo `f64 ∈ [0,4]` produzido por agregação. |
| **Weight** | Peso da questão (`[0.5, 2.0]`, default 1.0) ou da capability. |
| **Threshold** | Cobertura mínima de questões respondidas: 25 (warning), 40 (ok). |
| **PE flag** | Marca questões críticas para Production Engineering. Geram um sub-score paralelo. |
| **Gap** | `target − current` por capability. |
| **Priority score** | `weight × gap` que classifica capability em P0/P1/P2/P3. |
| **Audience** | Públicos-alvo da questão (developer, sre, security…). Filtra visibilidade no formulário. |
| **`threshold_status`** | `Ok` / `Warning` / `Blocked` — devolvido junto com o resultado. |

---

**Arquivos relacionados:**
- 📄 `pontuacao-e-calculo.xlsx` — planilha auditável com fórmulas SUMPRODUCT visíveis (mesmos exemplos deste doc)
- 🌐 `calculadora-pontuacao.html` — calculadora interativa standalone (selecionar respostas, ver scores ao vivo)
- 📚 `P1-…md`, `P2-…md`, `P3-…md` — perguntas reais do assessment com KPI/contexto/evidências por nível
