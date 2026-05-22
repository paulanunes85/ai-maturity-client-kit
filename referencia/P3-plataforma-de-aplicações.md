# Assessment de Maturidade IA — Pilar P3: Plataforma de Aplicações

> Mede a sofisticação da plataforma — arquitetura cloud-native, APIs, IA, dados, agentes, identidade, multi-cloud, performance e FinOps.

## Visão geral

- **Pilar:** `P3` — Plataforma de Aplicações
- **Capacidades (capabilities):** 9
- **Questões totais:** 46
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

## Capacidades do pilar P3

- **P3-C1** — Arquitetura Cloud-Native (5 questões)
- **P3-C2** — Gestão de APIs (5 questões)
- **P3-C3** — Desenvolvimento de Aplicações IA (5 questões)
- **P3-C4** — Plataforma de Dados e Lakehouse (5 questões)
- **P3-C5** — Aplicações Agênticas (6 questões)
- **P3-C6** — Gestão de Identidades e Acessos (5 questões)
- **P3-C7** — Multi-Cloud e Portabilidade (5 questões)
- **P3-C8** — Desempenho e Escalabilidade (5 questões)
- **P3-C9** — FinOps e Otimização de Custos (5 questões)

---

## P3-C1 — Arquitetura Cloud-Native

**5 questões neste capability.**

### P3-C1-Q1 — Qual é a maturidade da adoção de arquitetura cloud-native?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `% workloads containerized`

**Contexto**

- **O que mede (what):** Measures adoption of cloud-native patterns including containerization, orchestration, and service decomposition.
- **Por que importa (why):** Cloud-native architectures enable 10x faster scaling, 99.99% availability, and 50% infrastructure cost reduction.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Monolithic applications deployed on VMs or bare metal. No containerization. | • No container adoption<br>• VM-based deployment topology<br>• Monolithic architecture in use |
| **L1** | Em Desenvolvimento | Some applications containerized (<30%). Docker used for development but not production. | • <30% containerized rate measured<br>• Docker in dev only<br>• No orchestration platform |
| **L2** | Definido | 50-70% of workloads containerized. Kubernetes or container orchestration in production. Basic microservice decomposition. | • 50-70% containerized rate measured<br>• K8s in production<br>• Some microservices deployed |
| **L3** | Gerenciado | >85% workloads cloud-native. Service mesh, GitOps deployment, automated scaling. Well-defined service boundaries. | • >85% cloud-native rate measured<br>• Service mesh deployed<br>• GitOps workflow adopted<br>• Automated scaling rules configured |
| **L4** | Otimizando | Full cloud-native with AI-optimized resource allocation, predictive auto-scaling, self-healing infrastructure, and serverless where appropriate. | • AI resource optimization<br>• Predictive automated scaling enabled<br>• Self-healing infrastructure enabled<br>• Serverless platform adoption |

---

### P3-C1-Q2 — Em que medida Arquitetura Nativa da Nuvem (container adoption) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% workloads containerized`

**Contexto**

- **O que mede (what):** Workloads run as containers on Kubernetes or managed platforms.
- **Por que importa (why):** Containers enable density, portability, and declarative deploys.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem container adoption implementado. As equipes operam sem esta capacidade. | • No container adoption deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de container adoption com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | container adoption adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | container adoption padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | container adoption é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C1-Q3 — Em que medida Arquitetura Nativa da Nuvem (service mesh / zero trust networking) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services on mesh`

**Contexto**

- **O que mede (what):** Service mesh handles mTLS, retries, and traffic shaping.
- **Por que importa (why):** Mesh moves reliability and security out of app code.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem service mesh / zero trust networking implementado. As equipes operam sem esta capacidade. | • No service mesh / zero trust networking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de service mesh / zero trust networking com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | service mesh / zero trust networking adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | service mesh / zero trust networking padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | service mesh / zero trust networking é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C1-Q4 — Em que medida Arquitetura Nativa da Nuvem (event-driven architecture) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% flows async`

**Contexto**

- **O que mede (what):** Events and queues decouple services for resilience and scale.
- **Por que importa (why):** EDA enables loose coupling and graceful degradation.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem event-driven architecture implementado. As equipes operam sem esta capacidade. | • No event-driven architecture deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de event-driven architecture com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | event-driven architecture adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | event-driven architecture padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | event-driven architecture é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C1-Q5 — Em que medida Arquitetura Nativa da Nuvem (managed services preference) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% managed vs self-hosted`

**Contexto**

- **O que mede (what):** Prefer managed databases, queues, and caches over self-operated.
- **Por que importa (why):** Managed services shift ops burden to the cloud provider.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem managed services preference implementado. As equipes operam sem esta capacidade. | • No managed services preference deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de managed services preference com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | managed services preference adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | managed services preference padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | managed services preference é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C2 — Gestão de APIs

**5 questões neste capability.**

### P3-C2-Q1 — Quão madura é sua estratégia de gestão de APIs?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor, engineering-leader, Segurança
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `% APIs with OpenAPI spec`

**Contexto**

- **O que mede (what):** Measures the maturity of API design, documentation, versioning, and governance practices.
- **Por que importa (why):** Well-managed APIs reduce integration time by 70% and enable partner ecosystem growth.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | No API standards. APIs designed ad-hoc. No documentation beyond source code. | • No API standards<br>• Ad-hoc API design<br>• No API documentation |
| **L1** | Em Desenvolvimento | Some APIs have basic documentation. No versioning strategy. Inconsistent error handling. | • Basic API docs exist<br>• No versioning policy<br>• Inconsistent error formats |
| **L2** | Definido | OpenAPI specs for >50% of APIs. API design guidelines documented. Versioning strategy defined. | • >50% APIs with OpenAPI<br>• Design guidelines doc<br>• API versioning strategy documented |
| **L3** | Gerenciado | API gateway with centralized management. >80% APIs documented. Rate limiting, auth, and monitoring standardized. API lifecycle management. | • API gateway deployed<br>• >80% documented rate measured<br>• Standardized auth/rate limiting |
| **L4** | Otimizando | AI-powered API management: auto-generated docs from code, anomaly detection on API traffic, predictive capacity planning, automated backward compatibility checks. | • Auto-generated API docs<br>• Traffic anomaly detection<br>• Predictive capacity planning<br>• Auto compatibility checks |

---

### P3-C2-Q2 — Em que medida Gestão de APIs (API gateway for all external APIs) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% APIs behind gateway`

**Contexto**

- **O que mede (what):** Gateway handles auth, rate limiting, and observability.
- **Por que importa (why):** A gateway centralizes cross-cutting API concerns.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem api gateway for all external apis implementado. As equipes operam sem esta capacidade. | • No API gateway for all external APIs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de api gateway for all external apis com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | API gateway for all external APIs adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | API gateway for all external APIs padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | API gateway for all external APIs é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C2-Q3 — Em que medida Gestão de APIs (OpenAPI contracts) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% APIs with spec`

**Contexto**

- **O que mede (what):** Every API has a machine-readable contract.
- **Por que importa (why):** Contracts enable codegen, mock servers, and compatibility testing.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem openapi contracts implementado. As equipes operam sem esta capacidade. | • No OpenAPI contracts deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de openapi contracts com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | OpenAPI contracts adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | OpenAPI contracts padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | OpenAPI contracts é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C2-Q4 — Em que medida Gestão de APIs (versioning & deprecation policy) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `deprecated APIs retired on time`

**Contexto**

- **O que mede (what):** Explicit versioning and deprecation schedules.
- **Por que importa (why):** Clear policy preserves customer trust and avoids breakage.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem versioning & deprecation policy implementado. As equipes operam sem esta capacidade. | • No versioning & deprecation policy deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de versioning & deprecation policy com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | versioning & deprecation policy adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | versioning & deprecation policy padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | versioning & deprecation policy é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C2-Q5 — Em que medida Gestão de APIs (developer portal with self-serve keys) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Desenvolvedor
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `time-to-first-call`

**Contexto**

- **O que mede (what):** Self-service key issuance and interactive docs.
- **Por que importa (why):** Dev portals accelerate partner integration.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem developer portal with self-serve keys implementado. As equipes operam sem esta capacidade. | • No developer portal with self-serve keys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de developer portal with self-serve keys com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | developer portal with self-serve keys adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | developer portal with self-serve keys padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | developer portal with self-serve keys é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C3 — Desenvolvimento de Aplicações IA

**5 questões neste capability.**

### P3-C3-Q1 — Quão madura é a capacidade da sua organização de construir e implantar aplicações com IA?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `# AI features in production`

**Contexto**

- **O que mede (what):** Measures the organization's capability to develop, deploy, and maintain AI-powered application features.
- **Por que importa (why):** Organizations with mature AI application development ship AI features 5x faster and with 3x fewer production incidents.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | No AI features in production applications. No team capability for AI development. | • No AI features deployed<br>• No ML/AI engineering skills<br>• No AI development tools |
| **L1** | Em Desenvolvimento | Experimenting with AI APIs (OpenAI, Azure AI) in 1-2 applications. No MLOps practices. | • 1-2 AI experiments<br>• Direct API integration<br>• No MLOps tooling in place |
| **L2** | Definido | 3-5 AI-powered features in production. Basic prompt engineering practices. RAG pattern for knowledge retrieval. | • 3-5 AI features live<br>• Prompt engineering guidelines<br>• RAG implementation deployed |
| **L3** | Gerenciado | Standardized AI development framework. Model evaluation pipeline. Prompt versioning and A/B testing. >10 AI features in production. | • AI dev framework docs<br>• Model evaluation pipeline<br>• Prompt versioning workflow<br>• >10 AI features |
| **L4** | Otimizando | AI-native applications with autonomous agents, multi-model orchestration, continuous model evaluation, and automated prompt optimization. AI features are core to product. | • Autonomous agent deployments<br>• Multi-model orchestration enabled<br>• Continuous model eval<br>• Automated prompt optimization |

---

### P3-C3-Q2 — Em que medida Desenvolvimento de Aplicações de IA (LLM application frameworks) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% AI apps on framework`

**Contexto**

- **O que mede (what):** Teams use frameworks (LangChain, Semantic Kernel) for LLM apps.
- **Por que importa (why):** Frameworks accelerate RAG, agents, and evaluation patterns.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem llm application frameworks implementado. As equipes operam sem esta capacidade. | • No LLM application frameworks deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de llm application frameworks com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | LLM application frameworks adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | LLM application frameworks padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | LLM application frameworks é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C3-Q3 — Em que medida Desenvolvimento de Aplicações de IA (evaluation harness for AI) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `evals per release`

**Contexto**

- **O que mede (what):** Automated evals run on every model or prompt change.
- **Por que importa (why):** AI evals catch regressions that unit tests cannot.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem evaluation harness for ai implementado. As equipes operam sem esta capacidade. | • No evaluation harness for AI deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de evaluation harness for ai com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | evaluation harness for AI adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | evaluation harness for AI padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | evaluation harness for AI é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C3-Q4 — Em que medida Desenvolvimento de Aplicações de IA (vector database / RAG platform) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `RAG apps in prod`

**Contexto**

- **O que mede (what):** A shared vector store/RAG platform serves multiple apps.
- **Por que importa (why):** Centralized RAG reduces duplicated work across teams.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem vector database / rag platform implementado. As equipes operam sem esta capacidade. | • No vector database / RAG platform deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de vector database / rag platform com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | vector database / RAG platform adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | vector database / RAG platform padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | vector database / RAG platform é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C3-Q5 — Em que medida Desenvolvimento de Aplicações de IA (responsible AI / safety filters) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Desenvolvedor, Arquiteto, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% AI apps with guardrails`

**Contexto**

- **O que mede (what):** All AI apps integrate content safety and audit logging.
- **Por que importa (why):** Responsible AI is table stakes; retrofitting is expensive.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem responsible ai / safety filters implementado. As equipes operam sem esta capacidade. | • No responsible AI / safety filters deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de responsible ai / safety filters com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | responsible AI / safety filters adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | responsible AI / safety filters padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | responsible AI / safety filters é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C4 — Plataforma de Dados e Lakehouse

**5 questões neste capability.**

### P3-C4-Q1 — Em que medida Plataforma de Dados e Lakehouse (lakehouse or data platform in use) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% data in platform`

**Contexto**

- **O que mede (what):** A lakehouse unifies structured and unstructured data.
- **Por que importa (why):** Lakehouses combine warehouse performance with lake flexibility.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem lakehouse or data platform in use implementado. As equipes operam sem esta capacidade. | • No lakehouse or data platform in use deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de lakehouse or data platform in use com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | lakehouse or data platform in use adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | lakehouse or data platform in use padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | lakehouse or data platform in use é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q2 — Em que medida Plataforma de Dados e Lakehouse (data contracts between producers & consumers) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% pipelines with contracts`

**Contexto**

- **O que mede (what):** Data contracts declare schema and quality guarantees.
- **Por que importa (why):** Contracts prevent silent breakage between teams.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem data contracts between producers & consumers implementado. As equipes operam sem esta capacidade. | • No data contracts between producers & consumers deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de data contracts between producers & consumers com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | data contracts between producers & consumers adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | data contracts between producers & consumers padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | data contracts between producers & consumers é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q3 — Em que medida Plataforma de Dados e Lakehouse (catalog and lineage tracking) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% datasets cataloged`

**Contexto**

- **O que mede (what):** Every dataset has ownership, lineage, and quality metadata.
- **Por que importa (why):** Catalogs accelerate discovery and investigations.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem catalog and lineage tracking implementado. As equipes operam sem esta capacidade. | • No catalog and lineage tracking deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de catalog and lineage tracking com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | catalog and lineage tracking adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | catalog and lineage tracking padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | catalog and lineage tracking é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q4 — Em que medida Plataforma de Dados e Lakehouse (self-service analytics) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% decisions using data`

**Contexto**

- **O que mede (what):** Business users query data themselves via governed tools.
- **Por que importa (why):** Self-service shifts the bottleneck off the data team.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem self-service analytics implementado. As equipes operam sem esta capacidade. | • No self-service analytics deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de self-service analytics com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | self-service analytics adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | self-service analytics padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | self-service analytics é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C4-Q5 — Em que medida Plataforma de Dados e Lakehouse (real-time streaming ingestion) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% use-cases real-time`

**Contexto**

- **O que mede (what):** Streaming is available for time-sensitive use cases.
- **Por que importa (why):** Real-time data enables fresher AI and operational decisions.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem real-time streaming ingestion implementado. As equipes operam sem esta capacidade. | • No real-time streaming ingestion deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de real-time streaming ingestion com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | real-time streaming ingestion adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | real-time streaming ingestion padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | real-time streaming ingestion é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C5 — Aplicações Agênticas

**6 questões neste capability.**

### P3-C5-Q1 — Em que medida Aplicações Agênticas (agents with tool-use in prod) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `agents in production`

**Contexto**

- **O que mede (what):** Agents call tools and APIs to perform multi-step work.
- **Por que importa (why):** Agentic workflows automate complex tasks humans used to route.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem agents with tool-use in prod implementado. As equipes operam sem esta capacidade. | • No agents with tool-use in prod deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de agents with tool-use in prod com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | agents with tool-use in prod adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | agents with tool-use in prod padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | agents with tool-use in prod é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q2 — Em que medida Aplicações Agênticas (orchestration framework (Semantic Kernel, etc)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% agents on framework`

**Contexto**

- **O que mede (what):** Agents are built on a standard orchestration runtime.
- **Por que importa (why):** Standard runtimes reduce per-agent engineering cost.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem orchestration framework (semantic kernel, etc) implementado. As equipes operam sem esta capacidade. | • No orchestration framework (Semantic Kernel, etc) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de orchestration framework (semantic kernel, etc) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | orchestration framework (Semantic Kernel, etc) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | orchestration framework (Semantic Kernel, etc) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | orchestration framework (Semantic Kernel, etc) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q3 — Em que medida Aplicações Agênticas (evaluation and safety for agents) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `eval scenarios per agent`

**Contexto**

- **O que mede (what):** Agents are evaluated for safety, cost, and task completion.
- **Por que importa (why):** Agent evaluation is different from LLM evaluation.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem evaluation and safety for agents implementado. As equipes operam sem esta capacidade. | • No evaluation and safety for agents deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de evaluation and safety for agents com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | evaluation and safety for agents adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | evaluation and safety for agents padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | evaluation and safety for agents é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q4 — Em que medida Aplicações Agênticas (tool/action registry) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `tools available to agents`

**Contexto**

- **O que mede (what):** A governed registry lists tools agents may call.
- **Por que importa (why):** A registry controls blast radius and enables auditing.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem tool/action registry implementado. As equipes operam sem esta capacidade. | • No tool/action registry deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de tool/action registry com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | tool/action registry adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | tool/action registry padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | tool/action registry é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q5 — Em que medida Aplicações Agênticas (human-in-the-loop controls) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% agents with HITL`

**Contexto**

- **O que mede (what):** High-stakes actions require human confirmation.
- **Por que importa (why):** HITL lets teams ship agents safely while learning.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem human-in-the-loop controls implementado. As equipes operam sem esta capacidade. | • No human-in-the-loop controls deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de human-in-the-loop controls com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | human-in-the-loop controls adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | human-in-the-loop controls padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | human-in-the-loop controls é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C5-Q6 — Em que medida Aplicações Agênticas (agent cost and latency telemetry) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** data-ai, Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `p95 agent step latency`

**Contexto**

- **O que mede (what):** Agent performance and cost are tracked per step.
- **Por que importa (why):** Telemetry is required to run agents profitably at scale.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem agent cost and latency telemetry implementado. As equipes operam sem esta capacidade. | • No agent cost and latency telemetry deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de agent cost and latency telemetry com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | agent cost and latency telemetry adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | agent cost and latency telemetry padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | agent cost and latency telemetry é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C6 — Gestão de Identidades e Acessos

**5 questões neste capability.**

### P3-C6-Q1 — Em que medida Gestão de Identidades e Acessos (SSO for all apps) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% apps behind SSO`

**Contexto**

- **O que mede (what):** All apps authenticate via central SSO.
- **Por que importa (why):** SSO is the foundation of user lifecycle and revocation.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sso for all apps implementado. As equipes operam sem esta capacidade. | • No SSO for all apps deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de sso for all apps com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SSO for all apps adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | SSO for all apps padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | SSO for all apps é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q2 — Em que medida Gestão de Identidades e Acessos (workload identity (no long-lived secrets)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% workloads using WI`

**Contexto**

- **O que mede (what):** Workloads use managed identity, not static keys.
- **Por que importa (why):** Managed identities eliminate an entire class of leak.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem workload identity (no long-lived secrets) implementado. As equipes operam sem esta capacidade. | • No workload identity (no long-lived secrets) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de workload identity (no long-lived secrets) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | workload identity (no long-lived secrets) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | workload identity (no long-lived secrets) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | workload identity (no long-lived secrets) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q3 — Em que medida Gestão de Identidades e Acessos (least-privilege with JIT elevation) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% access through JIT`

**Contexto**

- **O que mede (what):** Standing admin is replaced by just-in-time elevation.
- **Por que importa (why):** JIT dramatically reduces blast radius of compromised accounts.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem least-privilege with jit elevation implementado. As equipes operam sem esta capacidade. | • No least-privilege with JIT elevation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de least-privilege with jit elevation com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | least-privilege with JIT elevation adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | least-privilege with JIT elevation padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | least-privilege with JIT elevation é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q4 — Em que medida Gestão de Identidades e Acessos (conditional access policies) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% sessions policy-evaluated`

**Contexto**

- **O que mede (what):** Access is granted based on device, location, and risk.
- **Por que importa (why):** Conditional access adapts security to context.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem conditional access policies implementado. As equipes operam sem esta capacidade. | • No conditional access policies deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de conditional access policies com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | conditional access policies adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | conditional access policies padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | conditional access policies é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C6-Q5 — Em que medida Gestão de Identidades e Acessos (access reviews and audit) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `access reviews per year`

**Contexto**

- **O que mede (what):** Access is reviewed at least quarterly and logged.
- **Por que importa (why):** Reviews prevent access drift from acquisitions and reorgs.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem access reviews and audit implementado. As equipes operam sem esta capacidade. | • No access reviews and audit deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de access reviews and audit com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | access reviews and audit adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | access reviews and audit padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | access reviews and audit é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C7 — Multi-Cloud e Portabilidade

**5 questões neste capability.**

### P3-C7-Q1 — Em que medida Multi-Cloud e Portabilidade (container-based workloads for portability) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% workloads portable`

**Contexto**

- **O que mede (what):** Workloads run in containers on any cloud.
- **Por que importa (why):** Portability is a hedge against lock-in and outages.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem container-based workloads for portability implementado. As equipes operam sem esta capacidade. | • No container-based workloads for portability deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de container-based workloads for portability com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | container-based workloads for portability adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | container-based workloads for portability padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | container-based workloads for portability é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q2 — Em que medida Multi-Cloud e Portabilidade (abstracted data tier (Postgres, etc)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% data on portable engines`

**Contexto**

- **O que mede (what):** Data services use open standards (Postgres, MySQL).
- **Por que importa (why):** Open engines keep migration costs bounded.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem abstracted data tier (postgres, etc) implementado. As equipes operam sem esta capacidade. | • No abstracted data tier (Postgres, etc) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de abstracted data tier (postgres, etc) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | abstracted data tier (Postgres, etc) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | abstracted data tier (Postgres, etc) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | abstracted data tier (Postgres, etc) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q3 — Em que medida Multi-Cloud e Portabilidade (multi-region deployment capability) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services multi-region`

**Contexto**

- **O que mede (what):** Services can run active-active across regions.
- **Por que importa (why):** Multi-region capability is required for DR and compliance.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem multi-region deployment capability implementado. As equipes operam sem esta capacidade. | • No multi-region deployment capability deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de multi-region deployment capability com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | multi-region deployment capability adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | multi-region deployment capability padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | multi-region deployment capability é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q4 — Em que medida Multi-Cloud e Portabilidade (cloud-agnostic IaC modules) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% modules cloud-agnostic`

**Contexto**

- **O que mede (what):** IaC modules abstract provider specifics where sensible.
- **Por que importa (why):** Thoughtful abstraction limits porting pain.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem cloud-agnostic iac modules implementado. As equipes operam sem esta capacidade. | • No cloud-agnostic IaC modules deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de cloud-agnostic iac modules com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | cloud-agnostic IaC modules adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | cloud-agnostic IaC modules padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | cloud-agnostic IaC modules é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C7-Q5 — Em que medida Multi-Cloud e Portabilidade (disaster recovery drills) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Arquiteto, Engenheiro de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `DR drills per year`

**Contexto**

- **O que mede (what):** Annual DR drills validate recovery time and process.
- **Por que importa (why):** Untested DR is not DR.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem disaster recovery drills implementado. As equipes operam sem esta capacidade. | • No disaster recovery drills deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de disaster recovery drills com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | disaster recovery drills adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | disaster recovery drills padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | disaster recovery drills é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C8 — Desempenho e Escalabilidade

**5 questões neste capability.**

### P3-C8-Q1 — Em que medida Desempenho e Escalabilidade (performance budgets per service) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with perf budget`

**Contexto**

- **O que mede (what):** Services declare latency and throughput budgets.
- **Por que importa (why):** Budgets turn performance into a first-class requirement.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem performance budgets per service implementado. As equipes operam sem esta capacidade. | • No performance budgets per service deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de performance budgets per service com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | performance budgets per service adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | performance budgets per service padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | performance budgets per service é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q2 — Em que medida Desempenho e Escalabilidade (load/stress testing in CI) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services load-tested`

**Contexto**

- **O que mede (what):** Load tests run on every release candidate.
- **Por que importa (why):** Catching regressions in CI beats catching them in prod.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem load/stress testing in ci implementado. As equipes operam sem esta capacidade. | • No load/stress testing in CI deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de load/stress testing in ci com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | load/stress testing in CI adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | load/stress testing in CI padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | load/stress testing in CI é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q3 — Em que medida Desempenho e Escalabilidade (autoscaling based on real demand) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services autoscaled`

**Contexto**

- **O que mede (what):** Services autoscale on CPU, latency, or queue depth.
- **Por que importa (why):** Autoscaling matches cost to demand.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem autoscaling based on real demand implementado. As equipes operam sem esta capacidade. | • No autoscaling based on real demand deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de autoscaling based on real demand com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | autoscaling based on real demand adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | autoscaling based on real demand padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | autoscaling based on real demand é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q4 — Em que medida Desempenho e Escalabilidade (profiling in production) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services continuously profiled`

**Contexto**

- **O que mede (what):** Always-on profiling (e.g., pyroscope, parca) runs in prod.
- **Por que importa (why):** Prod profiling surfaces bottlenecks real users hit.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem profiling in production implementado. As equipes operam sem esta capacidade. | • No profiling in production deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de profiling in production com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | profiling in production adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | profiling in production padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | profiling in production é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C8-Q5 — Em que medida Desempenho e Escalabilidade (capacity planning cadence) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `capacity reviews per year`

**Contexto**

- **O que mede (what):** Capacity is reviewed with growth projections.
- **Por que importa (why):** Planning prevents painful migrations at peak load.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem capacity planning cadence implementado. As equipes operam sem esta capacidade. | • No capacity planning cadence deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de capacity planning cadence com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | capacity planning cadence adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | capacity planning cadence padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | capacity planning cadence é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P3-C9 — FinOps e Otimização de Custos

**5 questões neste capability.**

### P3-C9-Q1 — Em que medida FinOps e Otimização de Custos (cost allocation & showback) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% cost tagged to team`

**Contexto**

- **O que mede (what):** Every resource is tagged and attributed to a team.
- **Por que importa (why):** Showback creates ownership for cost.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem cost allocation & showback implementado. As equipes operam sem esta capacidade. | • No cost allocation & showback deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de cost allocation & showback com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | cost allocation & showback adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | cost allocation & showback padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | cost allocation & showback é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q2 — Em que medida FinOps e Otimização de Custos (committed use / savings plans) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% eligible spend committed`

**Contexto**

- **O que mede (what):** Commit spend is used where usage is predictable.
- **Por que importa (why):** Commitments cut spend 20-50% at minimal risk.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem committed use / savings plans implementado. As equipes operam sem esta capacidade. | • No committed use / savings plans deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de committed use / savings plans com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | committed use / savings plans adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | committed use / savings plans padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | committed use / savings plans é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q3 — Em que medida FinOps e Otimização de Custos (idle and unused resource cleanup) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `$/month saved by cleanup`

**Contexto**

- **O que mede (what):** Automation flags and removes idle resources.
- **Por que importa (why):** Cleanup is the highest-leverage FinOps activity.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem idle and unused resource cleanup implementado. As equipes operam sem esta capacidade. | • No idle and unused resource cleanup deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de idle and unused resource cleanup com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | idle and unused resource cleanup adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | idle and unused resource cleanup padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | idle and unused resource cleanup é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q4 — Em que medida FinOps e Otimização de Custos (rightsizing recommendations) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% rightsizing applied`

**Contexto**

- **O que mede (what):** Automated recommendations drive continuous rightsizing.
- **Por que importa (why):** Rightsizing closes the gap between provisioned and needed.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem rightsizing recommendations implementado. As equipes operam sem esta capacidade. | • No rightsizing recommendations deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de rightsizing recommendations com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | rightsizing recommendations adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | rightsizing recommendations padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | rightsizing recommendations é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P3-C9-Q5 — Em que medida FinOps e Otimização de Custos (unit economics per product) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** product-owner, engineering-leader, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% products with $/user`

**Contexto**

- **O que mede (what):** Products track cost per user, request, or transaction.
- **Por que importa (why):** Unit economics align engineering and business decisions.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem unit economics per product implementado. As equipes operam sem esta capacidade. | • No unit economics per product deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de unit economics per product com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | unit economics per product adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | unit economics per product padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | unit economics per product é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## Como esta seção é pontuada

- Cada questão recebe um valor numérico do nível selecionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- A pontuação da capacidade é a média ponderada das questões (peso default = 1.0; questões com peso 1.5 ou 2.0 contam mais).
- A pontuação do pilar **P3** é a média das 9 capacidades.
- O resultado é exibido em escala 0–4 e convertido para % de maturidade (nível / 4 × 100).

## Glossário rápido

- **Pillar:** dimensão estratégica de maturidade.
- **Capability:** subdomínio funcional dentro de um pilar.
- **Question:** item de avaliação concreto, ID padrão `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0–L4):** ponto na escala Likert de maturidade.
- **KPI:** indicador-chave que valida objetivamente o nível declarado.
- **Evidence:** prova qualitativa (texto) ou quantitativa (anexo) que sustenta a resposta.
