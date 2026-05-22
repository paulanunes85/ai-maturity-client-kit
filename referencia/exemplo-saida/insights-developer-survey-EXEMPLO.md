<!-- paulasilva-ms identity: Paula Silva | Software Global Black Belt · paulasilva@microsoft.com -->
<!-- paulasilva-ms Design System v1.7.0 -->

# Developer Survey — Relatório de Insights

**Data:** 2026-05-08  ·  **Respondentes:** 5 (anônimos)  ·  **Versão da rubrica:** 1.0
**Autor:** Paula Silva | Software Global Black Belt  ·  **Contato:** paulasilva@microsoft.com

---

## 1 · Sumário Executivo

### 🎯 Maturidade IA do Time (rubrica determinística)

> **Overall: 2.22 (L2 — Definido)**
> Baseado em 5 respondentes, 7 dimensões, escala L0-L4 (mesma do assessment principal)

| Dimensão | Score | Rótulo | % devs em L3+L4 |
|---|---|---|---|
| D2 Copilot Adoption | **0.80** | L1 — Em Desenvolvimento | 0% |
| D3 MS/GH Tooling Breadth | **2.40** | L2 — Definido | 80% |
| D4 AI Dev Practices | **2.68** | L3 — Gerenciado | 80% |
| D5 Agent Concepts Mastery | **2.56** | L3 — Gerenciado | 80% |
| D6 Instructions Maturity | **2.31** | L2 — Definido | 40% |
| D7 Best Practices | **2.91** | L3 — Gerenciado | 60% |
| D8 Security & Governance | **1.92** | L2 — Definido | 20% |

### 🏆 3 dimensões mais fortes
- **D7** Best Practices — score **2.91** (L3 — Gerenciado)
- **D4** AI Dev Practices — score **2.68** (L3 — Gerenciado)
- **D5** Agent Concepts Mastery — score **2.56** (L3 — Gerenciado)

### ⚠️ 3 maiores gaps (oportunidades de roadmap)
- 🔴 **D2** Copilot Adoption — score **0.80** (L1 — Em Desenvolvimento)
- 🔴 **D8** Security & Governance — score **1.92** (L2 — Definido)
- 🔴 **D6** Instructions Maturity — score **2.31** (L2 — Definido)

### 💡 3 insights principais
1. **Underutilization de Coding Agent:** apenas 20% conhece/usa Coding Agent autônomo (S2-Q3) — tópico de workshop urgente

---

## 2 · Demografia (S1)

### Distribuição por cargo
| Cargo | N | % |
|---|---|---|
| Full-Stack | 2 | 40% |
| Architect | 1 | 20% |
| Outro | 1 | 20% |
| Data Engineer / ML Engineer | 1 | 20% |

---

## 3 · GitHub Copilot — Adoção e Modos (S2)

### Cobertura de licenças (S2-Q1)
| Tipo | N | % |
|---|---|---|
| Sim — Copilot Pro (individual) | 2 | 40% |
| Tenho licença mas não uso | 1 | 20% |
| Sim — Copilot Enterprise | 1 | 20% |
| Sim — Copilot Business | 1 | 20% |

### Frequência de uso (S2-Q2)
| Frequência | N | % |
|---|---|---|
| Diariamente (várias horas) | 2 | 40% |
| Semanal | 2 | 40% |
| Nunca | 1 | 20% |

### 🆕 Modos do Copilot Chat usados (S2-Q3, multi-select)
| Modo | N usuários | % devs |
|---|---|---|
| Ask (responder perguntas) | 3 | 60% |
| Edit (edição multi-arquivo no IDE) | 2 | 40% |
| Plan / Vision | 2 | 40% |
| Agent (autônomo no IDE, executa tasks) | 2 | 40% |
| Não uso o Chat — só completion inline | 2 | 40% |
| Copilot Coding Agent (autônomo no GitHub.com — assigna issue, abre PR sozinho) | 1 | 20% |

### Features ativas (S2-Q5, multi-select) — Top 8
| Feature | N | % devs |
|---|---|---|
| Copilot Coding Agent (tarefas autônomas) | 2 | 40% |
| Inline code completion | 2 | 40% |
| Pull Request review (Copilot review) | 2 | 40% |
| Pull Request descriptions automáticas | 2 | 40% |
| Slash commands no Chat (/explain, /fix, /tests) | 2 | 40% |
| Copilot CLI (gh copilot) | 2 | 40% |
| Copilot Spaces (contexto compartilhado: repos + docs + custom instructions) | 1 | 20% |
| Chat (perguntas no IDE) | 1 | 20% |

### Ganho de produtividade percebido (S2-Q7)
| Faixa | N | % |
|---|---|---|
| Neutro (sem ganho) | 2 | 40% |
| +10-20% | 1 | 20% |
| Não sei medir | 1 | 20% |
| Negativo (atrapalha) | 1 | 20% |

---

## 4 · Outras ferramentas Microsoft / GitHub AI (S3)

### Adoção (S3-Q1, multi-select)
| Ferramenta | N usuários | % devs |
|---|---|---|
| Azure OpenAI Service (direto via API) | 2 | 40% |
| Microsoft 365 Copilot | 2 | 40% |
| GitHub Advanced Security (GHAS) | 2 | 40% |
| Visual Studio com Copilot avançado | 2 | 40% |
| GitHub Copilot Coding Agent (autônomo) | 2 | 40% |
| GitHub Copilot Spaces | 1 | 20% |
| Nenhuma das acima | 1 | 20% |
| GitHub Models (playground multi-LLM) | 1 | 20% |
| Microsoft Foundry (ex-Azure AI Foundry) | 1 | 20% |
| GitHub Actions com Copilot integration | 1 | 20% |

---

## 5 · Práticas de Desenvolvimento com IA (S4)

### TDD com IA (S4-Q1)
| Frequência | N | % |
|---|---|---|
| Às vezes | 2 | 40% |
| Sempre que possível | 2 | 40% |
| Frequentemente | 1 | 20% |

### SDD (Spec-Driven Development) (S4-Q2)
| Conhecimento | N | % |
|---|---|---|
| Uso ativamente (com Spec Kit ou similar) | 3 | 60% |
| Já testei em alguns projetos | 2 | 40% |

---

## 6 · Conceitos de Agentes (S5)

### Conhecimento por conceito
| Conceito | Distribuição |
|---|---|
| **S5-Q1** AI agent | Sim — vagamente=2, Sim — explico claramente=2, Não sei a diferença=1 |
| **S5-Q3** Custom agents (.agent.md) | Já criei=2, Já usei mas não criei=2, Não sabia que era possível=1 |
| **S5-Q4** Skills (SKILL.md) | Conheço e uso=4, Conheço mas não uso=1 |
| **S5-Q5** Prompt files (.prompt.md) | Sim — uma ou duas=3, Sim — várias=2 |
| **S5-Q6** A2A protocol | Conheço o conceito=2, Não conheço=2, Uso (ex.: Foundry A2A Tool)=1 |
| **S5-Q9** Personas Agentic DevOps | Não conheço=3, Conheço o conceito=1, Sim — adoto explicitamente=1 |

**Insight:** apenas 60% conhece MCP — conceitos avançados (A2A, handoffs, subagentes, personas) são desconhecidos pela maioria. Oportunidade de workshop técnico.

---

## 7 · Markdown / Memory / Instructions (S6)

### Arquivos de instruções usados (S6-Q1, multi)
| Arquivo | N usuários | % |
|---|---|---|
| .github/instructions/*.instructions.md | 4 | 80% |
| .github/copilot-instructions.md | 3 | 60% |
| Custom instructions em Copilot Spaces | 2 | 40% |
| AGENTS.md | 2 | 40% |
| CLAUDE.md (raiz do projeto) | 1 | 20% |

---

## 8 · Usabilidade e Best Practices (S7)

### Champions no time (S7-Q2)
| Resposta | N | % |
|---|---|---|
| Sim — eu sou | 3 | 60% |
| Não, mas precisava ter | 1 | 20% |
| Sim — outra pessoa | 1 | 20% |

### Métricas de produtividade (S7-Q4, multi)
| Framework | N | % |
|---|---|---|
| SPACE framework | 5 | 100% |
| Métricas de adoção do Copilot (active users) | 4 | 80% |
| DX index (developer experience) | 4 | 80% |
| DORA metrics (lead time, deployment freq, MTTR, change failure) | 3 | 60% |
| Self-report periódico (survey) | 2 | 40% |

---

## 9 · 🔒 Segurança e Governança (S8)

### Política documentada (S8-Q1)
| Resposta | N | % |
|---|---|---|
| Sim — mas pouco clara | 3 | 60% |
| Política informal (sem documento) | 1 | 20% |
| Sim — política formal e clara | 1 | 20% |

### Ferramentas de segurança ativas (S8-Q4, multi)
| Ferramenta | N | % |
|---|---|---|
| Dependabot / dependency review | 3 | 60% |
| SBOM (Software Bill of Materials) | 2 | 40% |
| Secret scanning | 2 | 40% |
| Microsoft Defender for Cloud | 1 | 20% |
| Nenhuma | 1 | 20% |
| CodeQL scanning | 1 | 20% |
| Snyk / SonarQube / outro SAST | 1 | 20% |
| Microsoft Defender for DevOps | 1 | 20% |
| GitHub Advanced Security (GHAS) | 1 | 20% |

---

## 10 · Pain Points & Wishlist (S9, anonimizadas)

---

## 11 · 🎯 Recomendações Priorizadas

| Prioridade | Ação | Justificativa |
|---|---|---|
| 🟠 P1 | Workshop de Coding Agent (autônomo no GitHub.com) | apenas 20% conhece |

> 💡 Para plano de capacitação detalhado com Champions, cohorts e calendário, rode também o **Learning & Growth Survey** (`survey-learning/`) e a skill `/plano-capacitacao`.

---

## 12 · 🔗 Conexão com Assessment de Maturidade

Se você rodou o assessment principal, compare:

| Dimensão (survey) | Capability (assessment) | Validar |
|---|---|---|
| **D2** Copilot Adoption | P1-C1 Assistentes IA | Score declarado vs. adoção real |
| **D3** MS/GH Tooling | P3-C3, P3-C5 | Sofisticação técnica |
| **D4** AI Dev Practices | P1-C2, P1-C8 | Práticas estruturadas |
| **D5** Agent Concepts | P3-C5 | Conhecimento avançado |
| **D6** Instructions | P1-C7 | Manutenção contexto IA |
| **D7** Best Practices | P1-C5, P1-C8 | Cultura de adoção |
| **D8** Security & Governance | P2-C4, P2-C10 | Governance real |

> **Padrão clássico:** liderança avalia P1-C1 como L3, mas survey D2 mostra L1 → **dissonância** entre estratégia e prática.

---

*Relatório gerado pela skill `/insights-developer-survey` · Rubrica determinística v1.0 · 2026-05-08*


---

<sub>**Paula Silva** | Software Global Black Belt · paulasilva@microsoft.com</sub>  
<sub>Building the future of software development with AI and Agentic DevOps</sub>  
<sub>Identidade visual: paulasilva-ms Design System v1.7.0 · ver `referencia/branding/`</sub>
