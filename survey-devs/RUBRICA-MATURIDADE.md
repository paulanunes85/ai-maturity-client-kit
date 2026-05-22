# Rubrica de Maturidade IA — Developer Survey

> **Modelo determinístico** que mapeia respostas do survey para níveis L0-L4 em **7 dimensões**, espelhando a escala do assessment principal de maturidade. Score por time (sem scores individuais no relatório, preserva anonimato).

**Versão da rubrica:** 1.0 · **Data:** 2026-05-08
**Implementação:** [`scripts/rubric.py`](scripts/rubric.py) · **Executor:** [`scripts/calcular_maturidade.py`](scripts/calcular_maturidade.py)

---

## 🎯 Princípios

1. **Determinística** — mesma resposta sempre produz o mesmo nível. Sem LLM, sem aleatoriedade.
2. **Auditável** — cada regra documentada neste arquivo, código replica 1:1.
3. **Conservadora** — na dúvida, desce o nível (evita inflar maturidade declarada).
4. **Anônimo** — calcula por respondente individualmente, mas **só agregados** saem no relatório (média, distribuição).
5. **Espelho do assessment principal** — usa a mesma escala L0-L4 (Inicial → Otimizando) para comparação direta.

## 🧭 Escala (igual ao assessment principal)

| Faixa | Rótulo | Descrição |
|---|---|---|
| `< 0.5` | **L0 — Inicial** | Sem prática, sem conhecimento, sem ferramenta |
| `[0.5, 1.5)` | **L1 — Em Desenvolvimento** | Adoção pontual, conhecimento básico |
| `[1.5, 2.5)` | **L2 — Definido** | Uso regular, conhece conceitos chave |
| `[2.5, 3.5)` | **L3 — Gerenciado** | Adoção ampla, conhece avançados, mede impacto |
| `≥ 3.5` | **L4 — Otimizando** | Domínio completo, cria primitivos, otimização contínua |

## 📊 As 7 dimensões

| ID | Dimensão | Vem de | O que mede |
|---|---|---|---|
| **D2** | **Copilot Adoption** | S2 (9 q) | Frequência + breadth de modos + features + ganho mensurado |
| **D3** | **MS/GH Tooling Breadth** | S3 (7 q) | Quantas ferramentas avançadas (Foundry, Spaces, Coding Agent, MCP, Spec Kit) usa |
| **D4** | **AI Dev Practices** | S4 (9 q) | TDD com IA, SDD, pair programming, debugging, onboarding |
| **D5** | **Agent Concepts Mastery** | S5 (11 q) | Conhecimento de 9 conceitos chave + criação de primitives + testes |
| **D6** | **Instructions Maturity** | S6 (6 q) | Uso de instructions files, manutenção, prompt library compartilhada |
| **D7** | **Best Practices** | S7 (9 q) | Champion, métricas DORA/DX, comunidade, compartilhamento |
| **D8** | **Security & Governance** | S8 (13 q) | Política, GHAS, scanners, SBOM, JIT, red-lines, audit, treinamento |

> **Excluídas do score:** S1 (perfil — só categoriza) e S9 (texto livre — vira quotes).

## ⚖️ Regras detalhadas por dimensão

### D2 — Copilot Adoption

| Resposta-chave | Sinaliza |
|---|---|
| `S2-Q1: Não tenho licença` OR `Tenho mas não uso` | **Hard L0** |
| `S2-Q2: Nunca` | **Hard L0** |
| `S2-Q2: Raramente` | L1 |
| `S2-Q2: Diariamente` + `S2-Q5: 2+ features` + `S2-Q3: 1+ modo` | **L2** |
| Acima + `S2-Q3: usa Agent ou Coding Agent` + `S2-Q5: 4+ features` + ganho positivo | **L3** |
| Acima + `S2-Q3: Coding Agent` + `S2-Q5: Spaces` + `S2-Q7: ganho >40%` + `S2-Q5: 5+ features` | **L4** |

### D3 — MS/GH Tooling Breadth

Score ponto-a-ponto: `n_tools (S3-Q1) + advanced_signals (S3-Q3, Q4, Q6, Q2)`

- `n_tools` = quantas ferramentas marcadas em S3-Q1 (excluindo "Nenhuma")
- `advanced_signals` = +1 para cada:
  - Coding Agent: "Uso ativamente"
  - Spaces: "Uso e crio"
  - MCP: "Uso servidores" ou "Configurei custom"
  - Foundry usado para "MCP", "multi-agent" ou "agentes autônomos"

**Mapping:**
- `score ≥ 8` → **L4** (5+ ferramentas + 3+ sinais avançados)
- `score 5-7` → **L3**
- `score 3-4` → **L2**
- `score 1-2` → **L1**
- `score 0` → **L0**

### D4 — AI Dev Practices

Soma ponderada (max ~10 pontos), mapeada para 0-4:

| Pergunta | Sinal | Pontos |
|---|---|---|
| `S4-Q1` TDD com IA | "Sempre" | +2 |
|  | "Frequentemente" | +1.5 |
|  | "Não sei TDD" | -1 |
| `S4-Q2` SDD | "Uso ativamente" | +2 |
|  | "Já testei" | +1 |
|  | "Nunca ouvi falar" | -0.5 |
| `S4-Q3` Momentos consulta IA (multi) | n_momentos × 0.4 (cap 2.0) | até +2 |
| `S4-Q4` Pair programmer mindset | "Trato como par" | +1.5 |
|  | "Às vezes" | +0.5 |
| `S4-Q5` Refactoring | "Toda semana" | +1 |
| `S4-Q7` Debugging primeiro com IA | "Pergunto Copilot" | +0.5 |
| `S4-Q8` Onboarding com IA | "Sempre" | +1 |

**Mapping:** `score / 10 × 4` → arredondado.

### D5 — Agent Concepts Mastery

3 componentes:

**(a) Coverage de 9 conceitos** (60% do peso): para cada um, +1.0 se "uso/explico", senão 0:
- S5-Q1 AI agent
- S5-Q2 Modos Copilot
- S5-Q3 Custom agents
- S5-Q4 Skills
- S5-Q5 Prompt files
- S5-Q6 A2A
- S5-Q7 Handoffs
- S5-Q8 Subagentes
- S5-Q9 Personas Agentic DevOps

**(b) Primitives criados (S5-Q11 multi)** (25% do peso): n_primitivos × 0.25 (cap 1.0)

**(c) Testes de agents (S5-Q10)** (15% do peso):
- "Sempre — test suite" → +1.0
- "Frequentemente" → +0.5
- "Não crio agents" → 0 (neutro)

**Fórmula:** `(coverage × 0.6 × 4) + min(n_primitivos × 0.25, 1.0) + (test_bonus × 0.36)`. Cap em 4.0.

**Cobertura mínima:** se `<5` perguntas respondidas → retorna `None` (não scored).

### D6 — Instructions Maturity

| Pergunta | Sinal | Pontos |
|---|---|---|
| `S6-Q1` Files (multi) | "Nenhum" ou vazio | **Hard L0** |
|  | 4+ tipos | +2 |
|  | 2-3 tipos | +1.5 |
|  | 1 tipo | +1 |
| `S6-Q2` Maintainer | "Time inteiro contribui" | +2 |
|  | "1-2 dedicadas" | +1.5 |
|  | "Ninguém mantém" / "Não temos" | -1 |
| `S6-Q3` Update freq | "Toda semana" | +1 |
|  | "Mensalmente" | +0.7 |
|  | "Nunca" | -0.5 |
| `S6-Q4` Content (multi) | n_tipos × 0.3 (cap 2.0) | até +2 |
| `S6-Q5` Library shared | "Copilot Space" / "repo dedicado" | +1 |
|  | "Não compartilhamos" | -0.5 |

**Mapping:** `score / 9 × 4`.

### D7 — Best Practices

| Pergunta | Sinal | Pontos |
|---|---|---|
| `S7-Q1` Learning sources (multi) | n_fontes × 0.3 (cap 1.5) | até +1.5 |
| `S7-Q2` Champion | "Sim — eu sou" / "outra pessoa" | +1.5 |
|  | "Cada um se vira" | -0.5 |
| `S7-Q3` Internal channel | ">5 mensagens/sem" | +1 |
|  | "pouco ativo" | +0.5 |
| `S7-Q4` Métricas (multi) | DORA/DX/SPACE/Copilot count × 0.5 (cap 2.0) | até +2 |
|  | "Não medimos" | -1 |
| `S7-Q5` Iterações | "1ª tentativa" / "2-3" | +1 |
|  | "7+" | -0.5 |
| `S7-Q9` Compartilha prompts | "Frequentemente" | +1 |
|  | "Nunca" | -0.5 |

**Mapping:** `score / 8 × 4`.

### D8 — Security & Governance (CRÍTICO — conservadora)

Maior número de regras + penalizações por red flags:

| Pergunta | Sinal | Pontos |
|---|---|---|
| `S8-Q1` Política + `S8-Q4` (Sec tools) | "Não temos política" + "Nenhuma ferramenta" | **Hard L0** |
| `S8-Q1` | "formal e clara" | +2 |
|  | "pouco clara" | +1 |
|  | "informal" | +0.5 |
| `S8-Q2` Sabe dados sensíveis | "Sei claramente" | +1 |
| `S8-Q3` Forbidden (multi) | n_tipos × 0.2 (cap 1.0) | até +1 |
|  | "Nenhuma restrição" | -1 |
| `S8-Q4` Sec tools (multi) | n_tools × 0.3 (cap 2.0) | até +2 |
| `S8-Q5` Code scan no PR | "gate obrigatório" | +1 |
| `S8-Q6` SBOM | "automatizado" | +0.5 |
| `S8-Q7` Review formal IA | "obrigatório humano + scanner" | +1 |
| `S8-Q8` Red-lines de agents | "Sempre" | +1 |
| `S8-Q9` JIT permissions | "JIT obrigatório" | +1 |
| `S8-Q10` DLP | "bloqueia" | +0.5 |
| `S8-Q11` Audit | "ativos e revisados" | +0.5 |
| `S8-Q12` Treinamento | "obrigatório anual" | +0.5 |

**Mapping:** `score / 12 × 4`.

## 🧮 Score overall do respondente

```
overall = média(D2..D8)  # apenas dimensões com score != None
```

## 🧮 Agregação para o time

```
team_score(D) = média(D em todos os respondentes)  # ignora None
team_overall  = média(overall de todos os respondentes)
distribuição(D) = % de respondentes em cada L0-L4
```

## 📤 Output

`saida/maturidade-developer-survey-<DATE>.json`:

```jsonc
{
  "metadata": {
    "computed_at": "2026-05-08T12:00:00Z",
    "n_respondents": 12,
    "rubric_version": "1.0 (deterministic)",
    "anonymous": true,
    "scope": "team aggregate (no individual scores in output)"
  },
  "team_overall": {
    "score": 2.22,
    "label": "L2 — Definido",
    "respondents_with_overall": 12
  },
  "dimensions": {
    "D2": {
      "name": "Copilot Adoption",
      "team_score": 0.80,
      "label": "L1 — Em Desenvolvimento",
      "respondents_with_score": 12,
      "distribution_count": {"L0": 5, "L1": 5, "L2": 2, "L3": 0, "L4": 0},
      "distribution_pct": {"L0": 41.7, "L1": 41.7, "L2": 16.7, "L3": 0, "L4": 0}
    },
    "D3": {...}, "D4": {...}, "D5": {...},
    "D6": {...}, "D7": {...}, "D8": {...}
  },
  "ranking": {
    "top": [["D7", "Best Practices", 2.91], ...],
    "bottom": [["D2", "Copilot Adoption", 0.80], ...]
  }
}
```

## 🔄 Como rodar

### Via skill no Copilot Chat

```
/insights-developer-survey   # invoca o script automaticamente
```

### Via CLI

```bash
python3 survey-devs/scripts/calcular_maturidade.py
# Output:
#   - saida/maturidade-developer-survey-DATE.json
#   - resumo no stdout (overall + tabela por dimensão + ranking)
```

## 🔗 Cross-reference com o assessment principal

A maturidade individual (do survey) **alimenta e valida** as capabilities do assessment organizacional:

| Dimensão do survey | Capability do assessment | O que validar |
|---|---|---|
| **D2** Copilot Adoption | `P1-C1` Assistentes de Codificação IA | Score declarado vs. adoção real declarada por devs |
| **D3** MS/GH Tooling | `P3-C3` Aplicações IA + `P3-C5` Apps Agênticas | Sofisticação técnica em IA |
| **D4** AI Dev Practices | `P1-C2` DevEx + `P1-C8` Métricas Produtividade | Práticas estruturadas |
| **D5** Agent Concepts | `P3-C5` Apps Agênticas | Conhecimento avançado |
| **D6** Instructions | `P1-C7` Documentação automatizada | Manutenção de contexto IA |
| **D7** Best Practices | `P1-C5` Onboarding + `P1-C8` Métricas | Cultura de adoção |
| **D8** Security & Governance | `P2-C4` DevSecOps + `P2-C10` Supply Chain | Governance real |

> 💡 **Padrão clássico:** liderança avalia P1-C1 como L3, mas survey D2 mostra L1 (60% dos devs raramente usa) → **dissonância** entre estratégia e prática. A skill `/insights-developer-survey` destaca isso na seção 12 do relatório.

## 📊 Calibração e revisão da rubrica

Esta é a **versão 1.0**. Recomendado revisar trimestralmente baseado em:

- Casos onde score parece sub/super-estimado (calibrar pesos)
- Mudanças no ecossistema (ex.: Copilot lança modo novo → adicionar em S2-Q3 + atualizar D2)
- Feedback de respondentes ("essa pergunta era ambígua")

**Como propor mudança:**
1. Editar `scripts/rubric.py` com a regra atualizada
2. Documentar o porquê neste arquivo
3. Incrementar `RUBRIC_VERSION` e re-rodar com dados anteriores para comparar

## 🔐 Política de anonimato no scoring

A rubrica calcula score POR respondente individualmente, mas o output JSON e o relatório:

- ✅ Mostram **scores agregados do time** (média, distribuição %)
- ✅ Mostram **distribuição por nível** (% devs em cada L0-L4)
- ❌ NÃO mostram score por respondent_id
- ❌ NÃO mostram cargo/perfil junto com score (agregação por cargo só se ≥3 devs do mesmo cargo)

Isso preserva o pacto de anonimato do survey enquanto permite insights úteis ao time.
