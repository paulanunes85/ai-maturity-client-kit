# Assessment de Maturidade IA — Pilar P1: Produtividade do Desenvolvedor

> Mede o quanto a engenharia adota IA para acelerar o ciclo de codificação, documentação, revisão, onboarding e colaboração interna.

## Visão geral

- **Pilar:** `P1` — Produtividade do Desenvolvedor
- **Capacidades (capabilities):** 9
- **Questões totais:** 53
- **Escala:** Likert L0–L4 (Inicial → Otimizando)
- **Idioma da pergunta:** Português (Brasil)
- **Idioma de KPI/contexto/evidência:** Inglês (termos técnicos universais)
- **Resposta esperada por questão:** 1 nível selecionado + texto de evidência (mín. recomendado 80 caracteres) + anexo opcional

## Como interpretar a escala

| Nível | Rótulo | Significado |
|---|---|---|
| **L0** | Inicial | Sem prática estabelecida; ações ad-hoc, sem ferramenta ou política. |
| **L1** | Em Desenvolvimento | Pilotos isolados, cobertura <25%, sem governança. |
| **L2** | Definido | Adoção em 25–50% das equipes, com diretrizes e treinamento básico. |
| **L3** | Gerenciado | Cobertura >75% com métricas de impacto e bibliotecas/templates compartilhados. |
| **L4** | Otimizando | Cobertura quase universal (>95%), automação, ajuste fino, melhoria contínua mensurada. |

## Tipos de informação coletada por questão

Cada questão captura simultaneamente **três tipos de dado**:

1. **Quantitativo (KPI):** uma métrica numérica explícita (ex.: % desenvolvedores ativos, MTTR, lead time, taxa de cobertura). Use o KPI sugerido para padronizar comparação entre equipes.

2. **Qualitativo (descrição do nível):** o respondente seleciona o nível L0–L4 cuja descrição melhor representa a realidade observada hoje (não a aspiracional).

3. **Evidência (texto + anexos):** prova documental — link de pipeline, screenshot de dashboard, política, runbook, contrato de licenças, métrica exportada. Quanto mais específica, maior a qualidade da evidência (escala: nenhuma → mínima → adequada → detalhada → exemplar).

## Critérios de qualidade da evidência

- **Mínima (<80 caracteres):** texto genérico, sem nome de ferramenta, métrica ou link.
- **Adequada (80–250):** menciona ferramenta + cobertura/escopo aproximado.
- **Detalhada (250–500):** inclui métrica numérica + link/anexo + período de medição.
- **Exemplar (>500 ou múltiplos anexos):** múltiplas fontes corroborantes, série temporal, comparativo antes/depois.

## Capacidades do pilar P1

- **P1-C1** — Assistentes de Codificação IA (5 questões)
- **P1-C2** — Plataforma de Experiência do Desenvolvedor (6 questões)
- **P1-C3** — Gestão do Conhecimento (6 questões)
- **P1-C4** — Automação de Revisão de Código (7 questões)
- **P1-C5** — Onboarding e Treinamento de Desenvolvedores (7 questões)
- **P1-C6** — Inner Source e Colaboração (6 questões)
- **P1-C7** — Automação de Documentação (5 questões)
- **P1-C8** — Medição de Produtividade do Desenvolvedor (6 questões)
- **P1-C9** — Automação de Ambientes e Espaços de Trabalho (5 questões)

---

## P1-C1 — Assistentes de Codificação IA

**5 questões neste capability.**

### P1-C1-Q1 — Em que medida sua organização utiliza ferramentas de completação de código com IA (ex. GitHub Copilot)?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% developers using AI completion`

**Contexto**

- **O que mede (what):** Measures adoption of AI-powered code completion and suggestion tools across the development team.
- **Por que importa (why):** AI coding assistants can increase developer velocity by 30-55% on routine coding tasks, reducing time-to-market.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ferramentas de IA de codificação implementadas. Todo o código é escrito manualmente sem assistência de IA. | • No AI tool licenses<br>• No AI tool policies<br>• Manual-only coding workflows |
| **L1** | Em Desenvolvimento | Implementação piloto de assistente de codificação IA para <10% dos desenvolvedores. Uso ad-hoc sem diretrizes. | • Pilot program documentation<br>• < 10% license allocation<br>• No usage policy defined |
| **L2** | Definido | Assistente de codificação IA implantado para 25-50% dos desenvolvedores com diretrizes de uso e treinamento básico. | • 25-50% license coverage<br>• Written usage guidelines<br>• Completion training materials |
| **L3** | Gerenciado | Assistente de codificação IA implantado para >75% dos desenvolvedores com ganhos de produtividade medidos >15% e bibliotecas de prompts. | • >75% active users<br>• Productivity metrics showing >15% gain<br>• Shared prompt library repository |
| **L4** | Otimizando | Assistente de codificação IA universal (>95%) com ajuste fino de modelo personalizado e melhoria de velocidade medida >30%. | • >95% daily active usage<br>• Custom model fine-tuning config<br>• Measured >30% velocity improvement<br>• Automated suggestion quality tracking |

---

### P1-C1-Q2 — Quão efetivamente sua equipe aproveita IA para revisão de código e melhoria de qualidade?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% PRs with AI review`

**Contexto**

- **O que mede (what):** Measures use of AI in code review processes to catch bugs, suggest improvements, and enforce standards.
- **Por que importa (why):** AI-assisted code review reduces review time by 40% and catches 20% more defects than manual-only review.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem participação de IA em revisão de código. Todas as revisões são revisões manuais entre pares. | • Manual-only review process<br>• No AI review tools<br>• No automated quality gates |
| **L1** | Em Desenvolvimento | Linting básico e ferramentas de análise estática em CI. Sem sugestões de revisão impulsadas por IA. | • CI linting configuration<br>• Static analysis tool setup<br>• No AI review bot configured |
| **L2** | Definido | Bot de revisão com IA configurado em 30-60% dos repositórios, fornecendo sugestões automatizadas de código. | • AI review bot on 30-60% of repos<br>• PR suggestion examples<br>• Review bot configuration docs |
| **L3** | Gerenciado | Revisão com IA integrada em >80% dos repositórios com regras personalizadas alinhadas aos padrões da equipe. | • >80% repo coverage<br>• Custom rule configuration<br>• Measured >25% review cycle reduction |
| **L4** | Otimizando | IA realiza primeira revisão em todos os PRs, aprovando automaticamente mudanças de baixo risco e escalando as críticas. | • 100% PR AI first-pass<br>• Auto-approval policy documented<br>• Risk classification model<br>• >50% cycle time reduction |

---

### P1-C1-Q3 — Como sua organização mede e rastreia o impacto das ferramentas de codificação IA na produtividade?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 0.8
- **Professional Edition:** Não
- **KPI principal:** `Productivity measurement maturity`

**Contexto**

- **O que mede (what):** Measures the organization's ability to quantify the value of AI coding tools.
- **Por que importa (why):** Without measurement, organizations cannot justify AI tool investment or optimize adoption strategies.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem medição do impacto das ferramentas de IA. Sem métricas de produtividade base capturadas. | • No DORA metrics<br>• No productivity dashboards<br>• No AI tool usage tracking |
| **L1** | Em Desenvolvimento | Feedback anedótico de desenvolvedores sobre a utilidade de ferramentas de IA. Sem medição quantitativa. | • Developer survey results<br>• Informal feedback collection<br>• No quantitative data |
| **L2** | Definido | Métricas DORA básicas rastreadas (frequência de implantação, tempo de entrega). Análise de uso de ferramentas de IA disponível. | • DORA metrics dashboard<br>• Monthly usage analytics report<br>• Baseline measurements established |
| **L3** | Gerenciado | Métricas abrangentes de produtividade do desenvolvedor incluindo medidas específicas de IA: taxa de aceitação, tempo economizado. | • >40% suggestion acceptance rate<br>• >20% time-to-merge improvement<br>• Defect density trend analysis |
| **L4** | Otimizando | Plataforma de inteligência de produtividade em tempo real correlacionando o uso de ferramentas de IA com resultados de negócio. | • Real-time productivity dashboard<br>• Automated ROI reports<br>• Business outcome correlation analysis<br>• Per-team optimization recommendations |

---

### P1-C1-Q4 — Qual nível de capacidades de testes assistidos por IA sua organização emprega?

**Metadados**

- **Público-alvo:** Desenvolvedor, qa-test, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% test coverage from AI generation`

**Contexto**

- **O que mede (what):** Measures use of AI to generate, maintain, and optimize test suites.
- **Por que importa (why):** AI-generated tests can increase coverage from 40% to 80% in weeks, catching regressions that manual tests miss.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Todos os testes escritos manualmente. Cobertura de testes inferior a 40% na maioria dos projetos. | • Manual test writing only<br>• <40% average coverage<br>• No AI test generation tools |
| **L1** | Em Desenvolvimento | Uso ocasional de IA para gerar esqueletos de testes unitários. A cobertura permanece abaixo de 50%. | • Ad-hoc AI test generation<br>• <50% coverage rate measured<br>• No systematic approach |
| **L2** | Definido | Geração de testes com IA integrada no fluxo de desenvolvimento para 30-50% do novo código. Cobertura >60%. | • AI test generation in 30-50% of new code<br>• 60% coverage gates in CI<br>• Test generation guidelines |
| **L3** | Gerenciado | IA gera >70% de testes unitários com revisão humana. Cobertura >75%. IA identifica casos extremos. | • >70% AI-generated tests<br>• >75% coverage across projects<br>• Edge case suggestion examples |
| **L4** | Otimizando | Otimização de testes impulsionada por IA: gera suites de regressão automaticamente, identifica testes instáveis, otimiza cobertura. | • >85% coverage rate measured<br>• <5% flaky test rate<br>• Automated regression suite generation<br>• Mutation testing integration |

---

### P1-C1-Q5 — Como sua organização governa o código gerado por IA em termos de segurança e conformidade?

**Metadados**

- **Público-alvo:** Desenvolvedor, Segurança, product-owner, qa-test
- **Peso:** 1.1
- **Professional Edition:** Não
- **KPI principal:** `AI code governance maturity`

**Contexto**

- **O que mede (what):** Measures policies and controls around AI-generated code quality, security, and IP compliance.
- **Por que importa (why):** Without governance, AI-generated code can introduce vulnerabilities, license violations, and compliance risks.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem governança sobre código gerado por IA. Nenhuma política existe. Desenvolvedores usam ferramentas de IA sem restrições. | • No AI code policy<br>• No security scanning of AI code<br>• No license compliance checks |
| **L1** | Em Desenvolvimento | Política básica existe proibindo uso de IA em módulos sensíveis à segurança. Sem automação. | • Written AI usage policy<br>• Security-sensitive module list<br>• No automated enforcement |
| **L2** | Definido | Código gerado por IA passa por análise de segurança padrão (SAST/DAST). Verificação de conformidade de licenças em CI. | • SAST/DAST pipeline includes AI code<br>• License compliance scanning<br>• Policy enforcement in CI |
| **L3** | Gerenciado | Portões de qualidade de código dedicados para IA: varredura de vulnerabilidades, auditoria de licenças, revisão de qualidade de código. | • AI-specific quality gates<br>• Code provenance tracking<br>• <2% security flag rate<br>• Quarterly audit reports |
| **L4** | Otimizando | Governança de código IA em tempo real: cada sugestão varrida antes de exibir, licenças bloqueadas e métricas de qualidade rastreadas. | • Pre-display content scanning enabled<br>• Auto-rejection of blocked licenses<br>• Zero unreviewed AI code policy<br>• Compliance certification achieved |

---

## P1-C2 — Plataforma de Experiência do Desenvolvedor

**6 questões neste capability.**

### P1-C2-Q1 — Quão maduro é seu portal ou plataforma interna para desenvolvedores?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `Developer portal adoption %`

**Contexto**

- **O que mede (what):** Measures the maturity of centralized developer portal for service catalog, docs, and self-service.
- **Por que importa (why):** A mature developer portal reduces onboarding time by 60% and eliminates context-switching between tools.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | No developer portal. Documentation scattered across wikis, Slack, and email. | • No centralized portal<br>• Documentation in multiple tools<br>• No service catalog |
| **L1** | Em Desenvolvimento | Basic wiki or Confluence space with some documentation. No service catalog or self-service capabilities. | • Central wiki exists<br>• Some API docs<br>• No service catalog |
| **L2** | Definido | Developer portal deployed (Backstage or similar) with service catalog covering >50% of services. Basic documentation templates. | • >50% services cataloged<br>• Portal deployment docs<br>• Documentation templates published |
| **L3** | Gerenciado | Developer portal covers >80% of services with self-service scaffolding, automated API docs, and integrated CI/CD status. Onboarding time reduced >40%. | • >80% service coverage<br>• Self-service scaffolding tooling<br>• >40% onboarding time reduction |
| **L4** | Otimizando | AI-powered developer portal: natural language search across all docs, auto-generated architecture diagrams, predictive issue detection. >95% developer satisfaction. | • AI-powered search enabled<br>• Auto-generated architecture diagrams<br>• >95% satisfaction score<br>• Predictive issue detection |

---

### P1-C2-Q2 — Quão efetivamente suas equipes usam ambientes de desenvolvimento padronizados?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma
- **Peso:** 0.9
- **Professional Edition:** Sim
- **KPI principal:** `Environment setup time (minutes)`

**Contexto**

- **O que mede (what):** Measures standardization of development environments across teams.
- **Por que importa (why):** Standardized environments eliminate 'works on my machine' issues and reduce setup time from days to minutes.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Each developer maintains their own environment setup. No standardization. Setup takes >4 hours for new team members. | • No environment standardization<br>• Setup time >4 hours<br>• Manual dependency installation |
| **L1** | Em Desenvolvimento | README with setup instructions. Some teams use Docker for local development. Setup time 1-4 hours. | • README setup guide<br>• Some Docker usage<br>• 1-4 hour setup time |
| **L2** | Definido | Docker Compose or devcontainer for >50% of projects. Setup time <30 minutes. Shared configurations. | • >50% projects with containers<br>• <30 min setup time<br>• Shared dev configs |
| **L3** | Gerenciado | Standardized devcontainers for >80% of projects. Cloud-based dev environments available (Codespaces). Setup time <10 minutes. | • >80% devcontainer coverage<br>• Cloud dev environment available<br>• <10 min setup time |
| **L4** | Otimizando | One-click ephemeral dev environments with AI-configured dependencies. Zero manual setup. Environment parity with production guaranteed. | • One-click environment creation<br>• Zero manual setup steps<br>• Production parity verification documented<br>• AI dependency configuration |

---

### P1-C2-Q3 — Em que medida Plataforma de Experiência do Desenvolvedor (self-service IDP) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `Self-service catalog coverage`

**Contexto**

- **O que mede (what):** Internal developer platform (IDP) provides paved paths with self-service provisioning.
- **Por que importa (why):** IDPs reduce cognitive load and accelerate onboarding by 50-70%.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem self-service idp implementado. As equipes operam sem esta capacidade. | • No self-service IDP deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de self-service idp com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | self-service IDP adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | self-service IDP padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | self-service IDP é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q4 — Em que medida Plataforma de Experiência do Desenvolvedor (golden paths and templates) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services from templates`

**Contexto**

- **O que mede (what):** Golden-path templates encode opinionated defaults for new services.
- **Por que importa (why):** Standard templates reduce time-to-first-commit and enforce security baselines.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem golden paths and templates implementado. As equipes operam sem esta capacidade. | • No golden paths and templates deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de golden paths and templates com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | golden paths and templates adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | golden paths and templates padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | golden paths and templates é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q5 — Em que medida Plataforma de Experiência do Desenvolvedor (developer portal) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `Portal MAU (monthly active users)`

**Contexto**

- **O que mede (what):** A developer portal centralizes docs, APIs, and service catalog.
- **Por que importa (why):** A single pane of glass reduces context switching and improves discovery.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem developer portal implementado. As equipes operam sem esta capacidade. | • No developer portal deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de developer portal com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | developer portal adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | developer portal padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | developer portal é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C2-Q6 — Em que medida Plataforma de Experiência do Desenvolvedor (paved road policy enforcement) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Segurança, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `services on paved road`

**Contexto**

- **O que mede (what):** Platform policies are codified so teams must opt-out explicitly.
- **Por que importa (why):** Policy-as-code turns governance into an enabler, not a blocker.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem paved road policy enforcement implementado. As equipes operam sem esta capacidade. | • No paved road policy enforcement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de paved road policy enforcement com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | paved road policy enforcement adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | paved road policy enforcement padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | paved road policy enforcement é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C3 — Gestão do Conhecimento

**6 questões neste capability.**

### P1-C3-Q1 — Quão efetivamente sua organização captura e compartilha conhecimento de desenvolvimento?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `Knowledge retrieval success rate %`

**Contexto**

- **O que mede (what):** Measures how well development knowledge is captured, organized, and accessible.
- **Por que importa (why):** Poor knowledge management causes 20% of developer time wasted searching for information or reinventing solutions.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Knowledge lives in individual developers' heads. No documentation culture. High bus-factor risk. | • No documentation policy<br>• Knowledge in individuals<br>• High bus-factor risk |
| **L1** | Em Desenvolvimento | Basic documentation exists for critical systems. Knowledge sharing through ad-hoc meetings and Slack threads. | • Some critical system docs<br>• Ad-hoc knowledge sharing<br>• Slack-based Q&A channel |
| **L2** | Definido | Structured documentation in central wiki. Regular tech talks or knowledge sharing sessions. Decision records for major changes. | • Central wiki with structure<br>• Regular tech talks<br>• ADR practice established |
| **L3** | Gerenciado | Searchable knowledge base covering >70% of systems. AI-assisted documentation generation. Automated runbooks for common issues. | • >70% system documentation<br>• AI-assisted doc generation<br>• Automated runbooks published |
| **L4** | Otimizando | AI-powered knowledge graph linking code, docs, incidents, and decisions. Natural language queries return contextual answers. Knowledge freshness auto-monitored. | • Knowledge graph implementation<br>• NL query interface<br>• Automated freshness monitoring enabled<br>• Contextual answer system |

---

### P1-C3-Q2 — Em que medida Gestão do Conhecimento (semantic code search) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos indexed`

**Contexto**

- **O que mede (what):** Organization-wide semantic search across repos, docs, and chats.
- **Por que importa (why):** Semantic search cuts duplicate work by making prior solutions discoverable.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem semantic code search implementado. As equipes operam sem esta capacidade. | • No semantic code search deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de semantic code search com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | semantic code search adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | semantic code search padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | semantic code search é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q3 — Em que medida Gestão do Conhecimento (RAG-based docs assistant) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `queries per developer/month`

**Contexto**

- **O que mede (what):** LLM-backed assistant answers dev questions from internal knowledge base.
- **Por que importa (why):** RAG assistants reduce interrupt load on senior engineers.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem rag-based docs assistant implementado. As equipes operam sem esta capacidade. | • No RAG-based docs assistant deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de rag-based docs assistant com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | RAG-based docs assistant adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | RAG-based docs assistant padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | RAG-based docs assistant é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q4 — Em que medida Gestão do Conhecimento (runbook and playbook coverage) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% critical services with runbook`

**Contexto**

- **O que mede (what):** Automated runbooks capture operational knowledge.
- **Por que importa (why):** Documented runbooks shorten MTTR and enable on-call rotation.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem runbook and playbook coverage implementado. As equipes operam sem esta capacidade. | • No runbook and playbook coverage deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de runbook and playbook coverage com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | runbook and playbook coverage adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | runbook and playbook coverage padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | runbook and playbook coverage é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q5 — Em que medida Gestão do Conhecimento (ADR (architecture decision records)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with ADRs`

**Contexto**

- **O que mede (what):** Architecture decisions are captured as ADRs in the repo.
- **Por que importa (why):** ADRs preserve institutional memory beyond individuals.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem adr (architecture decision records) implementado. As equipes operam sem esta capacidade. | • No ADR (architecture decision records) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de adr (architecture decision records) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | ADR (architecture decision records) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | ADR (architecture decision records) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | ADR (architecture decision records) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C3-Q6 — Em que medida Gestão do Conhecimento (learning content & curated paths) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `completions per quarter`

**Contexto**

- **O que mede (what):** Curated learning paths tied to role and career ladder.
- **Por que importa (why):** Structured learning reduces ramp time and improves retention.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem learning content & curated paths implementado. As equipes operam sem esta capacidade. | • No learning content & curated paths deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de learning content & curated paths com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | learning content & curated paths adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | learning content & curated paths padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | learning content & curated paths é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C4 — Automação de Revisão de Código

**7 questões neste capability.**

### P1-C4-Q1 — Em que medida Automação de Revisão de Código (AI reviewer bot on every PR) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% PRs AI-reviewed`

**Contexto**

- **O que mede (what):** A bot posts AI-generated review comments on every PR.
- **Por que importa (why):** AI reviewers catch issues before humans look at the code.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ai reviewer bot on every pr implementado. As equipes operam sem esta capacidade. | • No AI reviewer bot on every PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de ai reviewer bot on every pr com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | AI reviewer bot on every PR adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | AI reviewer bot on every PR padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | AI reviewer bot on every PR é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q2 — Em que medida Automação de Revisão de Código (static linting and style auto-fix) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `lint violations per kLOC`

**Contexto**

- **O que mede (what):** Linters and formatters run automatically on every commit.
- **Por que importa (why):** Automated style removes bikeshedding from reviews.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem static linting and style auto-fix implementado. As equipes operam sem esta capacidade. | • No static linting and style auto-fix deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de static linting and style auto-fix com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | static linting and style auto-fix adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | static linting and style auto-fix padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | static linting and style auto-fix é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q3 — Em que medida Automação de Revisão de Código (automated security review) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `critical findings per PR`

**Contexto**

- **O que mede (what):** SAST comments inline on the PR diff.
- **Por que importa (why):** Inline findings are fixed 10x faster than backlog items.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem automated security review implementado. As equipes operam sem esta capacidade. | • No automated security review deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de automated security review com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | automated security review adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | automated security review padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | automated security review é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q4 — Em que medida Automação de Revisão de Código (required-reviewer rules) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% PRs meeting review rule`

**Contexto**

- **O que mede (what):** CODEOWNERS enforces domain-expert review per path.
- **Por que importa (why):** Right reviewer + right code = better catches.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem required-reviewer rules implementado. As equipes operam sem esta capacidade. | • No required-reviewer rules deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de required-reviewer rules com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | required-reviewer rules adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | required-reviewer rules padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | required-reviewer rules é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q5 — Em que medida Automação de Revisão de Código (review SLA tracking) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median PR cycle time`

**Contexto**

- **O que mede (what):** PR cycle time is measured and targeted.
- **Por que importa (why):** Fast review cycles keep developers in flow.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem review sla tracking implementado. As equipes operam sem esta capacidade. | • No review SLA tracking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de review sla tracking com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | review SLA tracking adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | review SLA tracking padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | review SLA tracking é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q6 — Em que medida Automação de Revisão de Código (change size enforcement) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median PR size (LoC)`

**Contexto**

- **O que mede (what):** Pre-commit hooks encourage small PRs.
- **Por que importa (why):** Small PRs get better reviews and merge faster.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem change size enforcement implementado. As equipes operam sem esta capacidade. | • No change size enforcement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de change size enforcement com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | change size enforcement adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | change size enforcement padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | change size enforcement é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C4-Q7 — Em que medida Automação de Revisão de Código (reviewer load balancing) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `review load balance index`

**Contexto**

- **O que mede (what):** Reviewer assignment balances load across the team.
- **Por que importa (why):** Balanced review load prevents burnout of top reviewers.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem reviewer load balancing implementado. As equipes operam sem esta capacidade. | • No reviewer load balancing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de reviewer load balancing com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | reviewer load balancing adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | reviewer load balancing padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | reviewer load balancing é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C5 — Onboarding e Treinamento de Desenvolvedores

**7 questões neste capability.**

### P1-C5-Q1 — Em que medida Onboarding e Treinamento de Desenvolvedores (codespaces/dev containers for instant env) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `time-to-first-commit (hours)`

**Contexto**

- **O que mede (what):** Cloud dev envs are ready in minutes.
- **Por que importa (why):** Fast env setup unblocks new hires on day one.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem codespaces/dev containers for instant env implementado. As equipes operam sem esta capacidade. | • No codespaces/dev containers for instant env deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de codespaces/dev containers for instant env com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | codespaces/dev containers for instant env adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | codespaces/dev containers for instant env padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | codespaces/dev containers for instant env é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q2 — Em que medida Onboarding e Treinamento de Desenvolvedores (structured onboarding playbook) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% new hires completing onboarding`

**Contexto**

- **O que mede (what):** A documented 30/60/90-day onboarding plan per role.
- **Por que importa (why):** Structured onboarding reduces ramp time by 30-50%.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem structured onboarding playbook implementado. As equipes operam sem esta capacidade. | • No structured onboarding playbook deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de structured onboarding playbook com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | structured onboarding playbook adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | structured onboarding playbook padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | structured onboarding playbook é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q3 — Em que medida Onboarding e Treinamento de Desenvolvedores (mentor pairing program) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `mentor:mentee ratio`

**Contexto**

- **O que mede (what):** Every new hire gets a senior mentor for 90 days.
- **Por que importa (why):** Mentoring shortens ramp and boosts retention.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem mentor pairing program implementado. As equipes operam sem esta capacidade. | • No mentor pairing program deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de mentor pairing program com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | mentor pairing program adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | mentor pairing program padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | mentor pairing program é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q4 — Em que medida Onboarding e Treinamento de Desenvolvedores (hands-on curriculum & kata) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `katas completed per hire`

**Contexto**

- **O que mede (what):** Role-specific coding kata produce demonstrable skill.
- **Por que importa (why):** Deliberate practice builds skill faster than reading.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem hands-on curriculum & kata implementado. As equipes operam sem esta capacidade. | • No hands-on curriculum & kata deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de hands-on curriculum & kata com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | hands-on curriculum & kata adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | hands-on curriculum & kata padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | hands-on curriculum & kata é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q5 — Em que medida Onboarding e Treinamento de Desenvolvedores (shadow on-call rotation) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `new hires who shadowed on-call`

**Contexto**

- **O que mede (what):** New hires shadow on-call to learn operational context.
- **Por que importa (why):** Operational context is the fastest way to understand the system.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem shadow on-call rotation implementado. As equipes operam sem esta capacidade. | • No shadow on-call rotation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de shadow on-call rotation com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | shadow on-call rotation adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | shadow on-call rotation padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | shadow on-call rotation é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q6 — Em que medida Onboarding e Treinamento de Desenvolvedores (onboarding feedback loop) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `NPS from new hires`

**Contexto**

- **O que mede (what):** New hires rate onboarding; results drive improvements.
- **Por que importa (why):** Feedback loops turn onboarding into a continuously improving product.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem onboarding feedback loop implementado. As equipes operam sem esta capacidade. | • No onboarding feedback loop deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de onboarding feedback loop com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | onboarding feedback loop adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | onboarding feedback loop padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | onboarding feedback loop é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C5-Q7 — Em que medida Onboarding e Treinamento de Desenvolvedores (ramp-time measurement) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median ramp-time to first deploy`

**Contexto**

- **O que mede (what):** Time-to-first-deploy is measured and improved for new hires.
- **Por que importa (why):** Measuring ramp turns onboarding improvements into ROI.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ramp-time measurement implementado. As equipes operam sem esta capacidade. | • No ramp-time measurement deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de ramp-time measurement com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | ramp-time measurement adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | ramp-time measurement padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | ramp-time measurement é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C6 — Inner Source e Colaboração

**6 questões neste capability.**

### P1-C6-Q1 — Em que medida Inner Source e Colaboração (internal repos with open contribution) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos open to all devs`

**Contexto**

- **O que mede (what):** Repos inside the org welcome PRs from other teams.
- **Por que importa (why):** Inner source breaks silos and increases reuse.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem internal repos with open contribution implementado. As equipes operam sem esta capacidade. | • No internal repos with open contribution deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de internal repos with open contribution com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | internal repos with open contribution adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | internal repos with open contribution padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | internal repos with open contribution é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q2 — Em que medida Inner Source e Colaboração (CONTRIBUTING.md standards) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos with CONTRIBUTING`

**Contexto**

- **O que mede (what):** Every repo documents how to contribute and review.
- **Por que importa (why):** Clear contribution norms lower friction for cross-team work.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem contributing.md standards implementado. As equipes operam sem esta capacidade. | • No CONTRIBUTING.md standards deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de contributing.md standards com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | CONTRIBUTING.md standards adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | CONTRIBUTING.md standards padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | CONTRIBUTING.md standards é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q3 — Em que medida Inner Source e Colaboração (inner-source discovery portal) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `cross-team PRs per month`

**Contexto**

- **O que mede (what):** A portal indexes inner-source projects seeking contributions.
- **Por que importa (why):** Discovery drives participation.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem inner-source discovery portal implementado. As equipes operam sem esta capacidade. | • No inner-source discovery portal deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de inner-source discovery portal com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | inner-source discovery portal adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | inner-source discovery portal padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | inner-source discovery portal é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q4 — Em que medida Inner Source e Colaboração (good-first-issue labeling) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `GFI issues closed per month`

**Contexto**

- **O que mede (what):** Starter issues help newcomers contribute confidently.
- **Por que importa (why):** Labeling lowers the bar for first-time contributors.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem good-first-issue labeling implementado. As equipes operam sem esta capacidade. | • No good-first-issue labeling deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de good-first-issue labeling com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | good-first-issue labeling adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | good-first-issue labeling padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | good-first-issue labeling é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q5 — Em que medida Inner Source e Colaboração (cross-team design reviews) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `reviews per quarter`

**Contexto**

- **O que mede (what):** Design docs are reviewed by multiple teams.
- **Por que importa (why):** Cross-team review catches assumptions and shares patterns.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem cross-team design reviews implementado. As equipes operam sem esta capacidade. | • No cross-team design reviews deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de cross-team design reviews com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | cross-team design reviews adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | cross-team design reviews padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | cross-team design reviews é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C6-Q6 — Em que medida Inner Source e Colaboração (community of practice) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, engineering-leader
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `CoP active members`

**Contexto**

- **O que mede (what):** Guilds and CoPs build horizontal expertise.
- **Por que importa (why):** CoPs accelerate learning and de-risk hiring gaps.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem community of practice implementado. As equipes operam sem esta capacidade. | • No community of practice deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de community of practice com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | community of practice adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | community of practice padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | community of practice é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C7 — Automação de Documentação

**5 questões neste capability.**

### P1-C7-Q1 — Em que medida Automação de Documentação (docs-as-code in Git) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with docs in repo`

**Contexto**

- **O que mede (what):** Docs live with code and are reviewed in PRs.
- **Por que importa (why):** Docs-as-code prevents docs from rotting away from source.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem docs-as-code in git implementado. As equipes operam sem esta capacidade. | • No docs-as-code in Git deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de docs-as-code in git com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | docs-as-code in Git adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | docs-as-code in Git padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | docs-as-code in Git é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q2 — Em que medida Automação de Documentação (auto-generated API reference) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% APIs with generated docs`

**Contexto**

- **O que mede (what):** API reference is generated from OpenAPI or source.
- **Por que importa (why):** Generated docs are always up to date.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem auto-generated api reference implementado. As equipes operam sem esta capacidade. | • No auto-generated API reference deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de auto-generated api reference com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | auto-generated API reference adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | auto-generated API reference padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | auto-generated API reference é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q3 — Em que medida Automação de Documentação (AI-assisted doc drafting) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% PRs with AI doc suggestions`

**Contexto**

- **O que mede (what):** AI suggests README and doc updates from code diffs.
- **Por que importa (why):** AI drafts raise the floor on documentation quality.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ai-assisted doc drafting implementado. As equipes operam sem esta capacidade. | • No AI-assisted doc drafting deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de ai-assisted doc drafting com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | AI-assisted doc drafting adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | AI-assisted doc drafting padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | AI-assisted doc drafting é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q4 — Em que medida Automação de Documentação (doc quality linting) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `broken-link count`

**Contexto**

- **O que mede (what):** Link checks and style linters run in CI.
- **Por que importa (why):** Automated checks keep docs trustworthy.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem doc quality linting implementado. As equipes operam sem esta capacidade. | • No doc quality linting deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de doc quality linting com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | doc quality linting adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | doc quality linting padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | doc quality linting é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C7-Q5 — Em que medida Automação de Documentação (docs analytics) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `top unanswered queries`

**Contexto**

- **O que mede (what):** Search analytics reveal what users cannot find.
- **Por que importa (why):** Analytics turn docs into a data-driven product.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem docs analytics implementado. As equipes operam sem esta capacidade. | • No docs analytics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de docs analytics com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | docs analytics adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | docs analytics padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | docs analytics é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C8 — Medição de Produtividade do Desenvolvedor

**6 questões neste capability.**

### P1-C8-Q1 — Em que medida Medição de Produtividade do Desenvolvedor (DORA four key metrics) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `deploys/day, lead time, CFR, MTTR`

**Contexto**

- **O que mede (what):** Deployment frequency, lead time, change fail rate, MTTR are tracked.
- **Por que importa (why):** DORA metrics correlate with business outcomes.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem dora four key metrics implementado. As equipes operam sem esta capacidade. | • No DORA four key metrics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de dora four key metrics com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | DORA four key metrics adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | DORA four key metrics padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | DORA four key metrics é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q2 — Em que medida Medição de Produtividade do Desenvolvedor (developer experience surveys) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `DX survey NPS`

**Contexto**

- **O que mede (what):** Quarterly surveys measure developer satisfaction.
- **Por que importa (why):** DX surveys surface friction that metrics miss.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem developer experience surveys implementado. As equipes operam sem esta capacidade. | • No developer experience surveys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de developer experience surveys com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | developer experience surveys adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | developer experience surveys padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | developer experience surveys é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q3 — Em que medida Medição de Produtividade do Desenvolvedor (build/test feedback loop time) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `p95 CI duration`

**Contexto**

- **O que mede (what):** CI provides signal within 10 minutes for typical PRs.
- **Por que importa (why):** Fast feedback keeps developers in flow.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem build/test feedback loop time implementado. As equipes operam sem esta capacidade. | • No build/test feedback loop time deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de build/test feedback loop time com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | build/test feedback loop time adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | build/test feedback loop time padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | build/test feedback loop time é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q4 — Em que medida Medição de Produtividade do Desenvolvedor (SPACE framework adoption) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `SPACE dimensions tracked`

**Contexto**

- **O que mede (what):** Teams track Satisfaction, Performance, Activity, Communication, Efficiency.
- **Por que importa (why):** SPACE balances quantitative and qualitative signals.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem space framework adoption implementado. As equipes operam sem esta capacidade. | • No SPACE framework adoption deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de space framework adoption com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SPACE framework adoption adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | SPACE framework adoption padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | SPACE framework adoption é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q5 — Em que medida Medição de Produtividade do Desenvolvedor (flow vs friction dashboards) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% teams viewing dashboard monthly`

**Contexto**

- **O que mede (what):** Leaders and teams see productivity data side by side.
- **Por que importa (why):** Shared data aligns improvements across teams.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem flow vs friction dashboards implementado. As equipes operam sem esta capacidade. | • No flow vs friction dashboards deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de flow vs friction dashboards com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | flow vs friction dashboards adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | flow vs friction dashboards padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | flow vs friction dashboards é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C8-Q6 — Em que medida Medição de Produtividade do Desenvolvedor (quarterly productivity OKRs) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% teams hitting DX OKRs`

**Contexto**

- **O que mede (what):** DX improvements are tracked as OKRs.
- **Por que importa (why):** OKRs make productivity a first-class investment.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem quarterly productivity okrs implementado. As equipes operam sem esta capacidade. | • No quarterly productivity OKRs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de quarterly productivity okrs com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | quarterly productivity OKRs adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | quarterly productivity OKRs padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | quarterly productivity OKRs é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P1-C9 — Automação de Ambientes e Espaços de Trabalho

**5 questões neste capability.**

### P1-C9-Q1 — Em que medida Automação de Ambientes e Espaços de Trabalho (reproducible local envs (devcontainers)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos with devcontainer`

**Contexto**

- **O que mede (what):** Every repo ships a devcontainer or Nix shell.
- **Por que importa (why):** Reproducible envs eliminate 'works on my machine' failures.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem reproducible local envs (devcontainers) implementado. As equipes operam sem esta capacidade. | • No reproducible local envs (devcontainers) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de reproducible local envs (devcontainers) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | reproducible local envs (devcontainers) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | reproducible local envs (devcontainers) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | reproducible local envs (devcontainers) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q2 — Em que medida Automação de Ambientes e Espaços de Trabalho (cloud workspaces (Codespaces/Gitpod)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% devs using cloud workspace`

**Contexto**

- **O que mede (what):** Cloud workspaces are the default dev env.
- **Por que importa (why):** Cloud workspaces make env setup instant and consistent.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem cloud workspaces (codespaces/gitpod) implementado. As equipes operam sem esta capacidade. | • No cloud workspaces (Codespaces/Gitpod) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de cloud workspaces (codespaces/gitpod) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | cloud workspaces (Codespaces/Gitpod) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | cloud workspaces (Codespaces/Gitpod) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | cloud workspaces (Codespaces/Gitpod) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q3 — Em que medida Automação de Ambientes e Espaços de Trabalho (tool and SDK version pinning) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `tools pinned per repo`

**Contexto**

- **O que mede (what):** Language and tool versions are pinned and lockfiles committed.
- **Por que importa (why):** Pinned versions keep builds reproducible across machines.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem tool and sdk version pinning implementado. As equipes operam sem esta capacidade. | • No tool and SDK version pinning deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de tool and sdk version pinning com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | tool and SDK version pinning adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | tool and SDK version pinning padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | tool and SDK version pinning é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q4 — Em que medida Automação de Ambientes e Espaços de Trabalho (on-demand test data) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `time to get fresh test data`

**Contexto**

- **O que mede (what):** Developers can reset or provision realistic test data on demand.
- **Por que importa (why):** Fresh data unblocks testing and debugging.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem on-demand test data implementado. As equipes operam sem esta capacidade. | • No on-demand test data deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de on-demand test data com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | on-demand test data adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | on-demand test data padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | on-demand test data é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P1-C9-Q5 — Em que medida Automação de Ambientes e Espaços de Trabalho (workspace telemetry & health) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Desenvolvedor, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% workspaces healthy`

**Contexto**

- **O que mede (what):** Workspace telemetry reveals setup failures and tool crashes.
- **Por que importa (why):** Telemetry lets platform teams fix friction proactively.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem workspace telemetry & health implementado. As equipes operam sem esta capacidade. | • No workspace telemetry & health deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de workspace telemetry & health com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | workspace telemetry & health adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | workspace telemetry & health padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | workspace telemetry & health é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## Como esta seção é pontuada

- Cada questão recebe um valor numérico do nível selecionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- A pontuação da capacidade é a média ponderada das questões (peso default = 1.0; questões com peso 1.5 ou 2.0 contam mais).
- A pontuação do pilar **P1** é a média das 9 capacidades.
- O resultado é exibido em escala 0–4 e convertido para % de maturidade (nível / 4 × 100).

## Glossário rápido

- **Pillar:** dimensão estratégica de maturidade.
- **Capability:** subdomínio funcional dentro de um pilar.
- **Question:** item de avaliação concreto, ID padrão `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0–L4):** ponto na escala Likert de maturidade.
- **KPI:** indicador-chave que valida objetivamente o nível declarado.
- **Evidence:** prova qualitativa (texto) ou quantitativa (anexo) que sustenta a resposta.
