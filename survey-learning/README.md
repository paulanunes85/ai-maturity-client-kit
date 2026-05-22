# `survey-learning/` — Learning & Growth Survey (identificado, capacitação)

**Terceiro pilar do kit:** depois de medir maturidade organizacional (assessment) e comportamento real (survey-devs), este survey gera o **roadmap de capacitação personalizado** — workshops, cohorts, Champions Network, mentoria. **Identificado** (nome+email) para poder convidar as pessoas certas.

## 📐 Diferença vs. outros surveys

| Aspecto | Assessment principal | Developer Survey | **Learning Survey** |
|---|---|---|---|
| **Audiência** | Liderança | Devs anônimos | **Devs identificados** |
| **Anônimo?** | Não | Sim | **Não — precisa nome+email** |
| **Foco** | Maturidade L0-L4 organizacional | Comportamento real (% adoção) | **O que querem APRENDER** |
| **Tempo por respondente** | 60-90 min | 22-28 min | **5-8 min** |
| **Quantidade de perguntas** | 158 | 75 | **32** |
| **Output** | 5 PDFs production | Insights + maturidade calculada | **Plano de capacitação acionável** |
| **Skills** | `/calcular-scores`, `/gerar-relatorio` | `/importar-survey-devs`, `/insights-developer-survey` | `/importar-survey-learning`, `/plano-capacitacao` |

**Os 3 são complementares** — rodar os 3 dá visão 360°:

```
Assessment (estratégia da liderança)
         ↓
Survey-devs (realidade comportamental anônima)
         ↓
Learning Survey (desejo de evolução identificado)
         ↓
WIZARD-IMPLEMENTACAO (consolida em Implementation Guide PDF)
```

## 📋 As 7 seções

| # | Seção | Foco | Q |
|---|---|---|---|
| **L1** | Identificação | Nome, email, cargo, time | 4 |
| **L2** | Auto-percepção de maturidade | Auto-avaliação L0-L4 nas 7 dimensões D2-D8 (rubrica) | 7 |
| **L3** | Onde quer crescer | Top 3 dimensões prioritárias (próximos 6 meses) | 2 |
| **L4** | Tópicos específicos | Copilot, Foundry, práticas (TDD/SDD), agents, segurança | 5 |
| **L5** | Formato e cadência | Workshop, cohort vs self-paced, horários, tempo/semana | 4 |
| **L6** | Champions e mentoria | Quer ser Champion? Mentoria? Quem é referência? | 5 |
| **L7** | Barreiras e Wishlist | O que impede + workshops + palestrantes desejados | 5 |
| | | **TOTAL** | **32** |

## 🗂️ Arquivos nesta pasta

| Arquivo | O que é |
|---|---|
| **[INSTRUCOES-FORMS-LEARNING.md](INSTRUCOES-FORMS-LEARNING.md)** | Como criar o Microsoft Forms IDENTIFICADO (com configuração + boas práticas + uso ético dos dados) |
| **[perguntas-para-forms-learning.md](perguntas-para-forms-learning.md)** | As 32 perguntas formatadas para copy/paste no Forms |
| **[template-export-forms-learning.xlsx](template-export-forms-learning.xlsx)** | Excel template + 5 respondentes mockados (Maria, João, Ana, Pedro, Sofia) |
| **[respostas-mock-learning.json](respostas-mock-learning.json)** | JSON estruturado de exemplo |

## 🚀 Fluxo de uso

```
1. Criar Forms seguindo INSTRUCOES-FORMS-LEARNING.md (~30 min)
2. Compartilhar link com TODOS os devs (Slack/Teams/Email)
3. Aguardar 2 semanas (lembretes em D+7 e D+12)
4. Responses → Open in Excel
5. Salvar como respostas-survey-learning.xlsx na raiz do kit
6. /importar-survey-learning   → survey-learning/respostas-learning.json
7. /plano-capacitacao          → saida/plano-capacitacao-DATA.md
```

## 🧪 Como testar / smoke test (sem coletar respostas reais)

Antes de criar o Forms para os devs, valide o pipeline com os 5 respondentes mockados:

### Modo A — Via Copilot Chat (recomendado)

```bash
# Da raiz do kit-cliente:
cp survey-learning/respostas-mock-learning.json survey-learning/respostas-learning.json
```

No Copilot Chat (modo Agent):
```
/plano-capacitacao
```

Em ~30 segundos você terá `saida/plano-capacitacao-2026-05-08.md` gerado a partir dos mocks (Maria, João, Ana, Pedro, Sofia). Permite ver "como vai ficar" antes de coletar dados reais.

### Modo B — Via @ai-maturity-assistant (concierge)

```
@ai-maturity-assistant
```

Escolha **[C] Learning & Growth Survey** quando o agente perguntar. Ele vai oferecer 3 opções e a `[C] Smoke test imediato com mocks` faz o atalho automaticamente.

### Modo C — Simulando ciclo completo via Excel mock

Para validar end-to-end (incluindo a skill `/importar-survey-learning`):

```bash
# Renomeie o template para o que a skill espera detectar
cp survey-learning/template-export-forms-learning.xlsx respostas-survey-learning.xlsx

# No Copilot Chat:
/importar-survey-learning      # parseia o Excel mock → respostas-learning.json
/plano-capacitacao             # gera plano dos 5 mocks identificados
```

Depois limpe o estado:
```bash
rm respostas-survey-learning.xlsx survey-learning/respostas-learning.json
```

### O que validar no smoke test

Após `/plano-capacitacao`, abra `saida/plano-capacitacao-DATA.md` e confirme:

- [ ] Sumário executivo mostra 5 respondentes
- [ ] Top 10 tópicos demandados aparecem com **nome + email** dos inscritos (Maria, João, Ana, Pedro, Sofia)
- [ ] Champions Network: Maria + João + Sofia listados como "ativos" (consistente com mocks)
- [ ] Calendário 90 dias gerado (workshops sequenciados)
- [ ] Apêndice tem tabela de respondentes (visível para liderança)

Se algum desses falta → reporte como bug da skill `/plano-capacitacao` (não do mock).

## 📊 O que sai no plano de capacitação

`saida/plano-capacitacao-<DATE>.md` (gerado pela skill) tem **12 seções**:

1. **Sumário Executivo** — maturidade percebida + top 3 dimensões prioritárias + Champions identificados + 3 quick wins
2. **Top 10 tópicos demandados** — com lista de inscritos pré-validados (nome+email)
3. **Cohorts sugeridos por dimensão D2-D8** — com Champions, formato, cadência
4. **Champions Network** — 3 tiers (ativos, com suporte, maybe) + mentor pairs + referências naturais
5. **Calendário de workshops próximos 90 dias** — semana × workshop × audiência × Champion
6. **Formato e cadência preferidos** — agregado do time
7. **Barreiras a remover** — priorizado
8. **Wishlist do time** — workshops, palestrantes, ideias livres
9. **Conexão com outros surveys** — comparação self-perception (L2) vs rubrica medida (D2-D8) vs assessment principal
10. **Top 5 ações priorizadas** — impacto × facilidade × alinhamento com gaps
11. **Próximos 30 dias** — cronograma semana a semana
12. **Apêndice — respondentes (visível só para liderança)** — tabela com todos os respondentes

## 🔗 Conexão com outros surveys e wizard

### ⭐ Mode D — Auto-fill do wizard

Após `/plano-capacitacao` gerar `saida/plano-capacitacao-DATA.md`, ao rodar `/wizard-implementacao` o Copilot Agent **detecta automaticamente** este plano e oferece **Mode D — Auto-fill** que preenche **6 dos 9 inputs do wizard** automaticamente:

```
saida/plano-capacitacao.md
    ↓ alimenta automaticamente (Mode D)
.github/skills/wizard-implementacao  (Parte 4 do PDF)
    ↓ campos populados:
- executive_steering_committee  ← Champions Network "ativos"
- communication_plan            ← Calendário sugerido
- training_plan                 ← Cohorts por dimensão
- adkar_notes                   ← Workshops top 5 (Knowledge stage)
- quick_wins_w1_4               ← Calendário 30 dias
- quick_wins_w5_8               ← Calendário semanas 5-8
- quick_wins_w9_12              ← Calendário semanas 9-12

Você só preenche manualmente: TPO + RACI Matrix
```

**Economia estimada do Mode D:** 30-45 min de wizard manual + dados REAIS do seu time (não placeholders do sample Acme).

**Como invocar Mode D:** simplesmente rode `/wizard-implementacao` depois de `/plano-capacitacao`. O agente oferece automaticamente.

## 🔐 Sobre identificação (não anonimato)

- Microsoft Forms tem opção "Anonymous responses" — para este survey, deve ficar **DESMARCADA**
- Devs precisam saber que é identificado AO RESPONDER (transparência)
- Liderança se compromete a usar dados SÓ para capacitação (não performance review)
- Plano consolidado é compartilhado com toda a equipe (transparência)
- Apêndice com nomes/emails é "visível para liderança" no relatório — não compartilhar publicamente

## 📅 Cadência sugerida

- **Primeira vez:** após estabelecer baseline com assessment + survey-devs
- **A cada 6 meses:** medir evolução do desejo + comparar com maturidade real
- **Após eventos grandes** (rollout Copilot, mudança de stack, novo Champion): re-rodar para realinhar plano

## 📚 Documentação relacionada

- **Skill que importa Excel → JSON:** [`../.github/skills/importar-survey-learning/SKILL.md`](../.github/skills/importar-survey-learning/SKILL.md)
- **Skill que gera plano:** [`../.github/skills/plano-capacitacao/SKILL.md`](../.github/skills/plano-capacitacao/SKILL.md)
- **Survey complementar (anônimo):** [`../survey-devs/`](../survey-devs/)
- **Wizard que consome o plano:** [`../wizard/`](../wizard/) (alimenta Parte 4 do PDF)
- **Assessment principal:** ver [`../README.md`](../README.md)

## 🔗 Fontes para tópicos cobertos no survey

Os tópicos de aprendizagem listados em L4 vêm das mesmas fontes oficiais validadas no Developer Survey:

- **GitHub Copilot** (modos, Spaces, Coding Agent): docs.github.com/copilot
- **Microsoft Foundry**: learn.microsoft.com/azure/foundry
- **MCP / A2A**: protocols + Foundry support (mar/2026)
- **Spec Kit (SDD)**: github.com/github/spec-kit
- **Agentic DevOps personas**: learn.microsoft.com/azure/well-architected/ai/personas
- **GHAS, CodeQL, SBOM, Defender**: GitHub Advanced Security + Microsoft Defender for DevOps docs
