# `survey-devs/` — Developer Survey (anônimo, comportamental, individual)

Esta pasta contém um **survey separado** do assessment principal — focado em entender **como cada desenvolvedor usa GitHub Copilot, agentes IA, instructions files, modos do Copilot Chat, práticas (TDD/SDD), governança e segurança** no dia-a-dia. Anônimo.

> 💡 **Survey complementar a este:** depois de rodar o **survey-devs** (anônimo, mede comportamento), considere também o **[survey-learning](../survey-learning/)** (identificado, mede o que devs querem aprender). Os 2 juntos formam um diagnóstico 360° dos devs — comportamental + aspiracional.

> 🔄 **Versão 2.0 (atualizada 2026-05-08)** — terminologia atualizada com mudanças oficiais:
> - **Copilot Workspace** evoluiu para **Copilot Coding Agent** (GA set/2025)
> - **Copilot Spaces** (GA set/2025) substituiu **Knowledge Bases** (sunset nov/2025)
> - **Azure AI Foundry** renomeado para **Microsoft Foundry** + **Foundry Agent Service** GA
> - Adicionadas perguntas sobre **MCP**, **A2A protocol**, personas Agentic DevOps Microsoft (**System Designer**, **Agent Operator**), **testar agents antes de usar**, **escopo+red-lines**, **JIT permissions**.

## 📐 Diferença vs. assessment principal e survey-learning

| Aspecto | Assessment principal | Developer Survey (este) | **survey-learning** |
|---|---|---|---|
| **Audiência** | Liderança / arquitetos / Tech Leads | **Devs individuais** (qualquer cargo) | Devs individuais |
| **Anônimo?** | Não — identificado por organização | **Sim — Forms anônimo** | **Não — IDENTIFICADO (nome+email)** |
| **Foco** | Maturidade organizacional (L0-L4) | Adoção e prática individual real | **O que querem APRENDER** |
| **Escala** | Likert 5 pontos por capability | Choice/multi-choice/texto livre | Auto-percepção L0-L4 + multi |
| **Quantidade** | 158 perguntas em 28 capabilities | **75 perguntas em 9 seções** | 32 perguntas em 7 seções |
| **Tempo por respondente** | 60-90 min | **22-28 min** | 5-8 min |
| **Multi-respondente** | Possível mas não default | **Essencial** (média ≥5, ideal ≥15) | **Essencial** (>50% do time) |
| **Output** | Relatório executivo + 5 PDFs | Relatório de insights + maturidade calculada | Plano de capacitação + Champions |
| **Skills** | `/calcular-scores`, `/gerar-relatorio` etc. | `/importar-survey-devs` + `/insights-developer-survey` | [`/importar-survey-learning`](../survey-learning/) + `/plano-capacitacao` |

**Os 3 são complementares:**
- Este **survey-devs** mede COMPORTAMENTO (anônimo)
- O **[survey-learning](../survey-learning/)** mede DESEJO (identificado, complementa este)
- O **assessment principal** mede ESTRATÉGIA (liderança)
- Juntos formam diagnóstico 360°.

## 📋 As 9 seções do survey (v2.0 — atualizado 2026-05-08)

| # | Seção | Foco | Q |
|---|---|---|---|
| **S1** | Perfil | Cargo, experiência, stack, modelo de trabalho | 7 |
| **S2** | GitHub Copilot — Adoção e Modos | Licença, frequência, **Ask / Edit / Agent / Coding Agent (autônomo)**, features (incl. **Spaces**), ganho | 9 |
| **S3** | Outras ferramentas Microsoft / GitHub | **Microsoft Foundry** (ex-Azure AI Foundry), **Foundry Agent Service**, **Copilot Spaces**, **Coding Agent**, GHAS, Spec Kit, **MCP** | 7 |
| **S4** | Práticas de Desenvolvimento com IA | TDD com IA, **SDD com Spec Kit**, pair programming, refactoring, debugging, onboarding | 9 |
| **S5** | Conceitos e Estrutura de Agentes | Agente vs assistente, modos Copilot, custom agents/skills/prompts, **A2A**, handoffs, subagentes, **personas Agentic DevOps Microsoft** (System Designer / Agent Operator), **TESTAR agents antes de usar** | 11 |
| **S6** | Markdown / Memory / Instructions | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, custom instructions em **Spaces**, **Foundry Memory** | 6 |
| **S7** | Usabilidade e Best Practices | Como aprenderam (incl. MS Build / GitHub Universe), Champion, métricas DORA/DX, iterações, confiança | 9 |
| **S8** | Segurança e Governança | Política, dados sensíveis, GHAS, CodeQL, SBOM, **Microsoft Defender for DevOps**, DLP, audit, **escopo+red-lines de agents**, **JIT permissions**, treinamento | 13 |
| **S9** | Pain Points & Wishlist | Frustrações, ideias, feature requests | 4 |
| | | **TOTAL** | **75** |

## 🗂️ Arquivos nesta pasta

| Arquivo | O que é |
|---|---|
| **[INSTRUCOES-FORMS-DEVS.md](INSTRUCOES-FORMS-DEVS.md)** | Guia passo-a-passo para criar o Microsoft Forms (com configuração de anonimato + boas práticas de coleta) |
| **[perguntas-para-forms-devs.md](perguntas-para-forms-devs.md)** | As 75 perguntas formatadas para copy/paste no Forms (tipos, opções, IDs) |
| **[template-export-forms-devs.xlsx](template-export-forms-devs.xlsx)** | Excel template no formato Forms export + 5 respondentes mockados (perfis variados) |
| **[respostas-mock-devs.json](respostas-mock-devs.json)** | JSON estruturado de exemplo (para teste da skill `/insights-developer-survey`) |
| **[RUBRICA-MATURIDADE.md](RUBRICA-MATURIDADE.md)** ⭐ | **Modelo de scoring** — rubrica determinística que mapeia respostas → níveis L0-L4 em 7 dimensões. Espelha a escala do assessment principal |
| **[scripts/rubric.py](scripts/rubric.py)** | Implementação Python da rubrica (regras hardcoded por dimensão) |
| **[scripts/calcular_maturidade.py](scripts/calcular_maturidade.py)** | Script CLI que aplica a rubrica → `saida/maturidade-developer-survey-DATE.json` |

## 🚀 Fluxo de uso (3 caminhos)

### Caminho A — Microsoft Forms (recomendado para 10+ devs)

```
1. Criar Forms seguindo INSTRUCOES-FORMS-DEVS.md (~30-45 min)
2. Compartilhar link com a equipe (Slack/Teams/Email)
3. Aguardar 2 semanas (lembretes periódicos)
4. Responses → Open in Excel
5. Salvar como respostas-survey-devs.xlsx na raiz do kit-cliente/
6. /importar-survey-devs       → survey-devs/respostas-devs.json
7. /insights-developer-survey  → saida/insights-developer-survey-DATA.md
```

### Caminho B — Excel/SharePoint compartilhado (rápido para 3-5 devs)

```
1. cp survey-devs/template-export-forms-devs.xlsx respostas-survey-devs.xlsx
2. Limpar linhas de mocks (linhas 2-6)
3. Subir no SharePoint com permissão de edit
4. Cada dev preenche uma linha
5. Baixar e mover para raiz
6. /importar-survey-devs + /insights-developer-survey
```

### Caminho C — Smoke test imediato (sem coleta real)

```
1. cp survey-devs/respostas-mock-devs.json survey-devs/respostas-devs.json
2. /insights-developer-survey  → vê como será o relatório com 5 mocks
```

Útil para apresentar ao cliente "como vai ficar" antes de coletar.

## 📊 O que sai no relatório de insights

`saida/insights-developer-survey-<DATE>.md` (gerado pela skill) tem:

1. **Sumário executivo** — 3 insights + 3 gaps + maturidade percebida
2. **Demografia** (S1) — quem respondeu, distribuição
3. **Copilot adoção** (S2) — % licenças, **adoção por modo (Ask/Edit/Agent)**, features ativas, ganho percebido
4. **Ecossistema MS/GitHub** (S3) — tabela de adoção
5. **Práticas de IA + dev** (S4) — TDD, SDD, debugging, onboarding + quotes anonimizadas
6. **Conhecimento de agentes** (S5) — matriz de "conhece+usa / conhece / não conhece" para 8 conceitos
7. **Instructions files** (S6) — quem usa, mantém, atualiza
8. **Usabilidade** (S7) — Champion, métricas, confiança, iterações
9. **Segurança** (S8) — política, scanners, DLP, audit + **score de governança 0-100**
10. **Pain points** (S9) — top 5 frustrações + wishlist (quotes)
11. **Recomendações priorizadas** — quick wins, próximo trimestre, semestre
12. **Conexão com o assessment principal** — capability por capability

## 🔗 Como o survey informa o assessment principal

Se você rodou ambos:

| Capability do assessment | Sinal do survey | Validação |
|---|---|---|
| **P1-C1** Assistentes de Codificação IA | S2-Q1, Q2, Q7 | Score declarado vs. adoção real |
| **P1-C2** Plataforma de DevEx | S6-Q5, S7-Q2 | Existe ferramental compartilhado? |
| **P1-C5** Onboarding e Treinamento | S7-Q1, Q2 | Como devs aprenderam? Tem Champions? |
| **P1-C8** Medição de Produtividade | S7-Q4 | DORA/DX/SPACE realmente medidos? |
| **P2-C4** DevSecOps | S8-Q4, Q5, Q11 | Scanners ativos vs. vulns vistas |
| **P2-C10** Supply Chain | S8-Q4, Q6 | SBOM, secret scan, DLP |
| **P3-C5** Aplicações Agênticas | S5-Q3, Q6, Q9 | Custom agents, MCP — sofisticação técnica |
| **P3-C6** Identidade e Acesso | S8-Q1, Q8, Q9 | Política, DLP, audit |

> 💡 **Use case clássico:** liderança avalia P1-C1 como L3, mas survey revela 60% dos devs usa raramente — gap de adoção real, não de licença.

## 🔐 Sobre anonimato

- O Microsoft Forms tem opção "Anonymous responses" — **MARCAR é mandatório** para este survey
- Sem isso, o Forms captura email da conta MS365 do respondente (quebra anonimato)
- A skill `/importar-survey-devs` valida que colunas Email/Name estão vazias e alerta se não estiverem
- Quotes no relatório são citadas por **ID da pergunta** (ex.: "Resposta S9-Q1"), nunca por respondent_id ou cargo

## 📅 Cadência sugerida

- **Primeira vez:** antes de definir estratégia de IA na engenharia (baseline)
- **Após rollout** de Copilot Enterprise: 30 dias depois
- **Trimestralmente:** medir evolução
- **Após workshops/treinamentos:** validar absorção

## 📚 Documentação relacionada

### Outras pastas do kit
- **Survey complementar (identificado, capacitação):** [`../survey-learning/`](../survey-learning/) — Learning & Growth Survey (32 q, 5-8 min, IDENTIFICADO). Gera plano de capacitação personalizado com Champions Network e calendário de workshops. Use APÓS este Developer Survey para passar de "comportamento medido" para "plano de ação"
- **Assessment principal (organizacional):** [`../README.md`](../README.md) — 158 perguntas Likert L0-L4, leadership-driven, gera 5 PDFs production
- **Coleta multi-respondente do assessment principal:** [`../coleta/INSTRUCOES-FORMS.md`](../coleta/INSTRUCOES-FORMS.md)
- **Wizard que consolida no PDF executivo:** [`../wizard/`](../wizard/) — alimenta Parte 4 do PDF com dados deste survey + do learning survey

### Skills deste survey
- Skill que importa Excel → JSON: [`../.github/skills/importar-survey-devs/SKILL.md`](../.github/skills/importar-survey-devs/SKILL.md)
- Skill que gera relatório + maturidade: [`../.github/skills/insights-developer-survey/SKILL.md`](../.github/skills/insights-developer-survey/SKILL.md)

### Como os 3 surveys se conectam (recomendado rodar nesta ordem)

```
1. Survey-devs (anônimo, ESTE)      → mede comportamento real + maturidade calculada
2. Survey-learning (identificado)   → mede desejo + barreiras + Champions
3. Assessment principal             → liderança avalia INFORMADA pelos 2 acima
4. /wizard-implementacao            → consolida tudo
5. /gerar-relatorio                 → 5 PDFs production-quality
```

## 🔗 Fontes oficiais validadas (v2.0 — 2026-05-08)

Toda terminologia e conceitos do survey foram cruzados com documentação oficial. Use estas fontes para responder dúvidas de devs sobre o que cada termo significa:

### GitHub Copilot
- **Copilot Spaces** (GA set/2025) — <https://github.blog/changelog/2025-05-29-introducing-copilot-spaces-a-new-way-to-work-with-code-and-context/>
- **Spaces docs oficial** — <https://docs.github.com/en/copilot/concepts/context/spaces>
- **Knowledge Bases sunset → Spaces** (nov/2025) — <https://github.blog/changelog/2025-10-17-copilot-knowledge-bases-can-now-be-converted-to-copilot-spaces/>
- **Copilot Coding Agent** (sucessor do Workspace, GA set/2025) — assigna issue, abre PR sozinho

### Microsoft Foundry (ex-Azure AI Foundry)
- **Foundry Agent Service overview** — <https://learn.microsoft.com/en-us/azure/foundry/agents/overview>
- **What's new mar/2026** (MCP, A2A, multi-agent) — <https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/>
- **Connectors (1.400+ business systems)** — <https://learn.microsoft.com/en-us/connectors/azureagentservice/>

### Agentic DevOps (terminologia Microsoft)
- **DevOps Playbook for the Agentic Era** — <https://devblogs.microsoft.com/all-things-azure/agentic-devops-practices-principles-strategic-direction/>
- **Reimagining the developer lifecycle** — <https://developer.microsoft.com/blog/reimagining-every-phase-of-the-developer-lifecycle>
- **Personas (System Designer, Agent Operator)** — <https://learn.microsoft.com/en-us/azure/well-architected/ai/personas>
- **Microsoft Reactor: Agentic DevOps Live** — <https://developer.microsoft.com/en-us/reactor/series/s-1625/>
- **Azure Agentic DevOps Solutions** — <https://azure.microsoft.com/en-us/solutions/devops>

### Spec-Driven Development
- **GitHub Spec Kit** — <https://github.com/github/spec-kit>

### Aplicabilidade ao assessment principal
- O assessment de maturidade na pasta-mãe usa as 7 estratégias S1-S7 (GitHub Migration, Foundry+SRE, App Modernization, AI Apps, Copilot Acceleration, Agentic Activation, Security & Governance) — alinhadas com **Agentic DevOps** Microsoft framework.
- Os 8 profiles (full-stack, backend-api, platform-eng, security-ops, frontend, data-ml, devops-sre, legacy) cobrem os Agentic DevOps personas.
