# Assessment de Maturidade IA — Pilar P2: Ciclo de Vida DevOps

> Mede a maturidade de pipelines, infraestrutura como código, observabilidade, DevSecOps, releases, testes, incidentes e segurança da cadeia de suprimentos.

## Visão geral

- **Pilar:** `P2` — Ciclo de Vida DevOps
- **Capacidades (capabilities):** 10
- **Questões totais:** 59
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

## Capacidades do pilar P2

- **P2-C1** — Inteligência de Pipeline CI/CD (6 questões)
- **P2-C2** — Infraestrutura como Código (6 questões)
- **P2-C3** — Observabilidade e Monitoramento (6 questões)
- **P2-C4** — Integração de Segurança (DevSecOps) (6 questões)
- **P2-C5** — Estratégias de Release e Implantação (6 questões)
- **P2-C6** — Automação de Testes (7 questões)
- **P2-C7** — Gestão de Incidentes e SRE (7 questões)
- **P2-C8** — Gestão de Artefatos e Pacotes (5 questões)
- **P2-C9** — Gestão de Mudanças e GitOps (5 questões)
- **P2-C10** — Segurança de Dependências e Cadeia de Suprimentos (5 questões)

---

## P2-C1 — Inteligência de Pipeline CI/CD

**6 questões neste capability.**

### P2-C1-Q1 — Quão maduro é seu pipeline CI/CD em termos de automação e integração de IA?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `Deployment frequency per week`

**Contexto**

- **O que mede (what):** Measures the automation level and intelligence of CI/CD pipelines.
- **Por que importa (why):** Mature CI/CD pipelines enable teams to deploy 200x more frequently with 3x lower change failure rate (DORA research).

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Manual builds and deployments. No CI/CD pipeline. Deployments happen weekly or less frequently. | • No CI/CD pipeline<br>• Manual build process<br>• Weekly or less deployments |
| **L1** | Em Desenvolvimento | Basic CI pipeline with automated builds and unit tests. Manual deployment process. Deployment frequency: weekly. | • CI pipeline configured<br>• Automated unit tests<br>• Manual deployments weekly |
| **L2** | Definido | Full CI/CD pipeline with automated testing, staging deployment, and manual production promotion. Deployment frequency: daily. | • Automated staging deployment<br>• Manual prod promotion<br>• Daily production deployments cadence |
| **L3** | Gerenciado | Intelligent CI/CD: auto-scaling test suites, smart test selection (run only affected tests), canary deployments. Multiple deployments per day. | • Smart test selection<br>• Canary deployment config<br>• Multiple daily deployments<br>• Test impact analysis |
| **L4** | Otimizando | AI-optimized pipeline: predictive build failures, auto-remediation of flaky tests, ML-driven canary analysis, self-healing deployments. | • Predictive failure model<br>• Automated remediation scripts deployed<br>• ML canary analysis<br>• Self-healing deployment docs |

---

### P2-C1-Q2 — Em que medida Inteligência de Pipeline CI/CD (pipeline-as-code everywhere) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% pipelines as code`

**Contexto**

- **O que mede (what):** All pipelines live next to code as versioned YAML/HCL.
- **Por que importa (why):** Pipeline-as-code is auditable, reviewable, and reproducible.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem pipeline-as-code everywhere implementado. As equipes operam sem esta capacidade. | • No pipeline-as-code everywhere deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de pipeline-as-code everywhere com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | pipeline-as-code everywhere adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | pipeline-as-code everywhere padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | pipeline-as-code everywhere é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q3 — Em que medida Inteligência de Pipeline CI/CD (build caching and artifact reuse) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% cache hit ratio`

**Contexto**

- **O que mede (what):** Remote build caches and content-addressed artifacts reduce build time.
- **Por que importa (why):** Caching cuts CI time by 40-70% and reduces cloud spend.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem build caching and artifact reuse implementado. As equipes operam sem esta capacidade. | • No build caching and artifact reuse deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de build caching and artifact reuse com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | build caching and artifact reuse adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | build caching and artifact reuse padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | build caching and artifact reuse é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q4 — Em que medida Inteligência de Pipeline CI/CD (trunk-based development) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `branches >7 days old`

**Contexto**

- **O que mede (what):** Short-lived branches merged to trunk multiple times a day.
- **Por que importa (why):** Trunk-based dev reduces merge hell and enables continuous delivery.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem trunk-based development implementado. As equipes operam sem esta capacidade. | • No trunk-based development deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de trunk-based development com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | trunk-based development adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | trunk-based development padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | trunk-based development é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q5 — Em que medida Inteligência de Pipeline CI/CD (deployment frequency) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `deploys per day`

**Contexto**

- **O que mede (what):** Elite DORA teams deploy many times per day to production.
- **Por que importa (why):** High deploy frequency correlates with low change fail rate.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem deployment frequency implementado. As equipes operam sem esta capacidade. | • No deployment frequency deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de deployment frequency com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | deployment frequency adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | deployment frequency padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | deployment frequency é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C1-Q6 — Em que medida Inteligência de Pipeline CI/CD (feature flags for progressive delivery) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `flags used per release`

**Contexto**

- **O que mede (what):** Feature flags decouple deployment from release.
- **Por que importa (why):** Flags enable dark launches, canary rollouts, and fast rollback.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem feature flags for progressive delivery implementado. As equipes operam sem esta capacidade. | • No feature flags for progressive delivery deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de feature flags for progressive delivery com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | feature flags for progressive delivery adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | feature flags for progressive delivery padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | feature flags for progressive delivery é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C2 — Infraestrutura como Código

**6 questões neste capability.**

### P2-C2-Q1 — Qual porcentagem de sua infraestrutura é gerenciada por código?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança, qa-test
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `% infrastructure as code`

**Contexto**

- **O que mede (what):** Measures the extent to which infrastructure provisioning and management is codified and version-controlled.
- **Por que importa (why):** IaC reduces provisioning errors by 90% and enables infrastructure changes to be reviewed, tested, and audited like application code.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | All infrastructure provisioned manually via cloud console or CLI commands. No version control for infra. | • Manual provisioning only<br>• No IaC files in repos<br>• Console-based management workflow |
| **L1** | Em Desenvolvimento | Some infrastructure defined in code (<30%). Mix of manual and automated provisioning. Scripts not version controlled consistently. | • <30% IaC coverage<br>• Mixed manual and automated processes<br>• Inconsistent version control |
| **L2** | Definido | 50-75% of infrastructure defined in code. IaC modules for common patterns. PR-based review for infra changes. | • 50-75% IaC coverage<br>• Reusable IaC modules<br>• PR-based infra review |
| **L3** | Gerenciado | >90% of infrastructure as code. Drift detection enabled. Policy-as-code enforcement. Self-service provisioning via templates. | • >90% IaC coverage<br>• Drift detection reports<br>• Policy-as-code rules enforced<br>• Self-service templates published |
| **L4** | Otimizando | 100% IaC with AI-generated infrastructure recommendations. Auto-remediation of drift. Cost optimization suggestions. Predictive scaling. | • 100% IaC coverage<br>• AI infra recommendations<br>• Automated drift remediation enabled<br>• Predictive scaling config |

---

### P2-C2-Q2 — Em que medida Infraestrutura como Código (Terraform/Bicep-based IaC) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% infra as code`

**Contexto**

- **O que mede (what):** All long-lived infra is declared as code.
- **Por que importa (why):** IaC eliminates snowflake servers and enables reproducible environments.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem terraform/bicep-based iac implementado. As equipes operam sem esta capacidade. | • No Terraform/Bicep-based IaC deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de terraform/bicep-based iac com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | Terraform/Bicep-based IaC adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | Terraform/Bicep-based IaC padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | Terraform/Bicep-based IaC é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q3 — Em que medida Infraestrutura como Código (module and pattern library) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% resources via modules`

**Contexto**

- **O que mede (what):** A shared module library encodes opinionated security and networking.
- **Por que importa (why):** Modules enforce standards and reduce per-team cognitive load.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem module and pattern library implementado. As equipes operam sem esta capacidade. | • No module and pattern library deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de module and pattern library com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | module and pattern library adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | module and pattern library padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | module and pattern library é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q4 — Em que medida Infraestrutura como Código (GitOps for config drift) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% envs drift-detected`

**Contexto**

- **O que mede (what):** GitOps controllers reconcile cluster and cloud state to Git.
- **Por que importa (why):** GitOps eliminates drift and makes Git the single source of truth.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem gitops for config drift implementado. As equipes operam sem esta capacidade. | • No GitOps for config drift deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de gitops for config drift com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | GitOps for config drift adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | GitOps for config drift padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | GitOps for config drift é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q5 — Em que medida Infraestrutura como Código (policy-as-code (OPA/Conftest)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `policies enforced in PR`

**Contexto**

- **O que mede (what):** Policies are evaluated on IaC changes before merge.
- **Por que importa (why):** Policy-as-code shifts governance left and scales security review.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem policy-as-code (opa/conftest) implementado. As equipes operam sem esta capacidade. | • No policy-as-code (OPA/Conftest) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de policy-as-code (opa/conftest) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | policy-as-code (OPA/Conftest) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | policy-as-code (OPA/Conftest) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | policy-as-code (OPA/Conftest) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C2-Q6 — Em que medida Infraestrutura como Código (ephemeral environment per PR) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `PR envs spun up`

**Contexto**

- **O que mede (what):** Every PR gets an ephemeral environment for integration testing.
- **Por que importa (why):** Ephemeral envs find bugs earlier and speed up review.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ephemeral environment per pr implementado. As equipes operam sem esta capacidade. | • No ephemeral environment per PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de ephemeral environment per pr com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | ephemeral environment per PR adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | ephemeral environment per PR padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | ephemeral environment per PR é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C3 — Observabilidade e Monitoramento

**6 questões neste capability.**

### P2-C3-Q1 — Quão abrangente é sua stack de observabilidade (logs, métricas, traces)?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Sim
- **KPI principal:** `MTTR in minutes`

**Contexto**

- **O que mede (what):** Measures the maturity of the observability stack including logging, metrics, and distributed tracing.
- **Por que importa (why):** Comprehensive observability reduces MTTR from hours to minutes and enables proactive issue detection.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Minimal logging. No centralized monitoring. Issues discovered by users reporting them. | • No centralized logging<br>• No monitoring dashboards<br>• User-reported issues only |
| **L1** | Em Desenvolvimento | Centralized logging (ELK/CloudWatch). Basic uptime monitoring. MTTR >60 minutes. | • Centralized log platform<br>• Basic uptime checks<br>• MTTR >60 minutes |
| **L2** | Definido | Structured logging, application metrics (Prometheus/Datadog), basic alerting. MTTR 30-60 minutes. | • Structured JSON logging<br>• Application metrics dashboard<br>• MTTR 30-60 minutes |
| **L3** | Gerenciado | Full observability: distributed tracing, correlated logs-metrics-traces, SLO-based alerting. MTTR <15 minutes. | • Distributed tracing enabled<br>• Correlated observability stack deployed<br>• SLO-based alerts configured<br>• MTTR <15 minutes |
| **L4** | Otimizando | AI-powered observability: anomaly detection, predictive alerting, auto-correlation of incidents, suggested remediation. MTTR <5 minutes. | • AI anomaly detection<br>• Predictive alerting enabled<br>• Automated incident correlation enabled<br>• MTTR <5 minutes |

---

### P2-C3-Q2 — Em que medida Observabilidade e Monitoramento (structured logging w/ correlation IDs) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services emitting structured logs`

**Contexto**

- **O que mede (what):** All logs follow a schema and carry trace/correlation IDs.
- **Por que importa (why):** Structured logs are searchable, aggregatable, and machine-readable.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem structured logging w/ correlation ids implementado. As equipes operam sem esta capacidade. | • No structured logging w/ correlation IDs deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de structured logging w/ correlation ids com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | structured logging w/ correlation IDs adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | structured logging w/ correlation IDs padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | structured logging w/ correlation IDs é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q3 — Em que medida Observabilidade e Monitoramento (distributed tracing (OpenTelemetry)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services instrumented`

**Contexto**

- **O que mede (what):** OTEL SDKs emit traces across service boundaries.
- **Por que importa (why):** Distributed tracing reveals latency contributors across microservices.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem distributed tracing (opentelemetry) implementado. As equipes operam sem esta capacidade. | • No distributed tracing (OpenTelemetry) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de distributed tracing (opentelemetry) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | distributed tracing (OpenTelemetry) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | distributed tracing (OpenTelemetry) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | distributed tracing (OpenTelemetry) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q4 — Em que medida Observabilidade e Monitoramento (SLOs and error budgets) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with SLOs`

**Contexto**

- **O que mede (what):** Service-level objectives with error budgets drive reliability decisions.
- **Por que importa (why):** SLOs align engineering priorities with user experience.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem slos and error budgets implementado. As equipes operam sem esta capacidade. | • No SLOs and error budgets deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de slos and error budgets com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SLOs and error budgets adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | SLOs and error budgets padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | SLOs and error budgets é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q5 — Em que medida Observabilidade e Monitoramento (synthetic monitoring) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `journeys monitored`

**Contexto**

- **O que mede (what):** Synthetic probes exercise critical user journeys continuously.
- **Por que importa (why):** Synthetics catch regressions before users do.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem synthetic monitoring implementado. As equipes operam sem esta capacidade. | • No synthetic monitoring deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de synthetic monitoring com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | synthetic monitoring adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | synthetic monitoring padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | synthetic monitoring é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C3-Q6 — Em que medida Observabilidade e Monitoramento (anomaly detection with ML) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `alerts auto-triaged`

**Contexto**

- **O que mede (what):** ML models detect anomalies and suppress noise.
- **Por que importa (why):** ML-based detection reduces alert fatigue and speeds response.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem anomaly detection with ml implementado. As equipes operam sem esta capacidade. | • No anomaly detection with ML deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de anomaly detection with ml com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | anomaly detection with ML adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | anomaly detection with ML padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | anomaly detection with ML é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C4 — Integração de Segurança (DevSecOps)

**6 questões neste capability.**

### P2-C4-Q1 — Quão integrada está a segurança no seu pipeline de desenvolvimento e implantação?

**Metadados**

- **Público-alvo:** Segurança, devops, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% vulnerabilities caught pre-prod`

**Contexto**

- **O que mede (what):** Measures the integration of security practices into the development lifecycle (shift-left security).
- **Por que importa (why):** Fixing vulnerabilities in production costs 30x more than catching them in development. DevSecOps reduces security incidents by 50%.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Security reviewed only before release. No automated scanning. Vulnerabilities found in production. | • No automated security scanning<br>• Pre-release only reviews<br>• Production vulnerability incidents |
| **L1** | Em Desenvolvimento | Basic dependency scanning in CI (Dependabot/Snyk). Manual security review for critical features. | • Dependency scanning configured<br>• Manual security reviews<br>• No SAST or DAST scanning |
| **L2** | Definido | SAST and dependency scanning in CI pipeline. Security requirements in definition of done. >50% vulnerabilities caught pre-production. | • SAST in CI pipeline<br>• Security in DoD<br>• >50% pre-prod catch rate |
| **L3** | Gerenciado | Full DevSecOps: SAST, DAST, SCA, container scanning, secret detection. Security gates block deployment. >80% pre-prod catch rate. | • SAST, DAST, SCA, and container scanning<br>• Secret detection enabled<br>• >80% pre-prod catch rate |
| **L4** | Otimizando | AI-powered security: automated threat modeling, predictive vulnerability detection, auto-patching of known CVEs, runtime protection. >95% pre-prod catch rate. | • Automated threat modeling<br>• Predictive vulnerability detection<br>• Automated patching pipeline enabled<br>• >95% pre-prod catch rate |

---

### P2-C4-Q2 — Em que medida Integração de Segurança (DevSecOps) (SAST in every pipeline) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos with SAST`

**Contexto**

- **O que mede (what):** Static analysis scans every PR for vulnerabilities.
- **Por que importa (why):** SAST finds bugs cheaply at authoring time.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sast in every pipeline implementado. As equipes operam sem esta capacidade. | • No SAST in every pipeline deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de sast in every pipeline com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SAST in every pipeline adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | SAST in every pipeline padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | SAST in every pipeline é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q3 — Em que medida Integração de Segurança (DevSecOps) (SCA and dependency review) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos with SCA`

**Contexto**

- **O que mede (what):** Software composition analysis flags vulnerable dependencies.
- **Por que importa (why):** Known-vuln dependencies are a top attack vector.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sca and dependency review implementado. As equipes operam sem esta capacidade. | • No SCA and dependency review deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de sca and dependency review com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SCA and dependency review adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | SCA and dependency review padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | SCA and dependency review é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q4 — Em que medida Integração de Segurança (DevSecOps) (secret scanning and push protection) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `secrets blocked per month`

**Contexto**

- **O que mede (what):** Secrets are detected pre-commit and blocked from push.
- **Por que importa (why):** Leaked secrets are the #1 source of breach in cloud environments.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem secret scanning and push protection implementado. As equipes operam sem esta capacidade. | • No secret scanning and push protection deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de secret scanning and push protection com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | secret scanning and push protection adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | secret scanning and push protection padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | secret scanning and push protection é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q5 — Em que medida Integração de Segurança (DevSecOps) (DAST and API security testing) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops, qa-test
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% APIs DAST-tested`

**Contexto**

- **O que mede (what):** Dynamic testing exercises the running app for runtime vulns.
- **Por que importa (why):** DAST catches issues SAST cannot (auth, logic, configuration).

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem dast and api security testing implementado. As equipes operam sem esta capacidade. | • No DAST and API security testing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de dast and api security testing com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | DAST and API security testing adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | DAST and API security testing padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | DAST and API security testing é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C4-Q6 — Em que medida Integração de Segurança (DevSecOps) (security champions program) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `champions per 20 devs`

**Contexto**

- **O que mede (what):** Every team has a security champion trained and resourced.
- **Por que importa (why):** Champions scale security expertise into every team.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem security champions program implementado. As equipes operam sem esta capacidade. | • No security champions program deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de security champions program com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | security champions program adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | security champions program padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | security champions program é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C5 — Estratégias de Release e Implantação

**6 questões neste capability.**

### P2-C5-Q1 — Em que medida Estratégias de Release e Implantação (blue/green or canary deploys) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with canary`

**Contexto**

- **O que mede (what):** Canary or blue/green deploys reduce blast radius.
- **Por que importa (why):** Progressive rollout catches issues before full exposure.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem blue/green or canary deploys implementado. As equipes operam sem esta capacidade. | • No blue/green or canary deploys deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de blue/green or canary deploys com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | blue/green or canary deploys adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | blue/green or canary deploys padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | blue/green or canary deploys é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q2 — Em que medida Estratégias de Release e Implantação (automated rollback) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median rollback time`

**Contexto**

- **O que mede (what):** SLO breach or error spike triggers automatic rollback.
- **Por que importa (why):** Automated rollback limits user impact when deploys go wrong.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem automated rollback implementado. As equipes operam sem esta capacidade. | • No automated rollback deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de automated rollback com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | automated rollback adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | automated rollback padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | automated rollback é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q3 — Em que medida Estratégias de Release e Implantação (feature flag platform) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Arquiteto
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `flags in active use`

**Contexto**

- **O que mede (what):** A flag platform supports progressive exposure and experiments.
- **Por que importa (why):** Flags decouple deploy from release.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem feature flag platform implementado. As equipes operam sem esta capacidade. | • No feature flag platform deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de feature flag platform com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | feature flag platform adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | feature flag platform padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | feature flag platform é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q4 — Em que medida Estratégias de Release e Implantação (release coordination via ChatOps) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% releases using ChatOps`

**Contexto**

- **O que mede (what):** Releases are coordinated through a chat bot with approvals.
- **Por que importa (why):** ChatOps creates an audit trail and reduces handoff errors.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem release coordination via chatops implementado. As equipes operam sem esta capacidade. | • No release coordination via ChatOps deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de release coordination via chatops com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | release coordination via ChatOps adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | release coordination via ChatOps padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | release coordination via ChatOps é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q5 — Em que medida Estratégias de Release e Implantação (progressive delivery across regions) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `regions rolled out per release`

**Contexto**

- **O que mede (what):** Releases ripple across regions with automated health checks.
- **Por que importa (why):** Multi-region rollout contains regional failures.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem progressive delivery across regions implementado. As equipes operam sem esta capacidade. | • No progressive delivery across regions deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de progressive delivery across regions com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | progressive delivery across regions adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | progressive delivery across regions padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | progressive delivery across regions é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C5-Q6 — Em que medida Estratégias de Release e Implantação (release metrics dashboard) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% releases meeting SLO`

**Contexto**

- **O que mede (what):** Deployment success and SLO impact are tracked per release.
- **Por que importa (why):** Data-driven release retros drive continuous improvement.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem release metrics dashboard implementado. As equipes operam sem esta capacidade. | • No release metrics dashboard deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de release metrics dashboard com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | release metrics dashboard adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | release metrics dashboard padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | release metrics dashboard é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C6 — Automação de Testes

**7 questões neste capability.**

### P2-C6-Q1 — Em que medida Automação de Testes (unit test coverage targets) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos >80% coverage`

**Contexto**

- **O que mede (what):** Every repo has a measurable coverage target.
- **Por que importa (why):** Coverage is a useful proxy when combined with mutation testing.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem unit test coverage targets implementado. As equipes operam sem esta capacidade. | • No unit test coverage targets deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de unit test coverage targets com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | unit test coverage targets adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | unit test coverage targets padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | unit test coverage targets é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q2 — Em que medida Automação de Testes (integration test suites) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `integration tests in CI`

**Contexto**

- **O que mede (what):** Integration tests exercise real service boundaries.
- **Por que importa (why):** Integration tests catch wiring bugs that units cannot.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem integration test suites implementado. As equipes operam sem esta capacidade. | • No integration test suites deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de integration test suites com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | integration test suites adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | integration test suites padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | integration test suites é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q3 — Em que medida Automação de Testes (end-to-end / journey tests) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `critical journeys automated`

**Contexto**

- **O que mede (what):** Critical user journeys run automatically on every deploy.
- **Por que importa (why):** E2E tests protect revenue-critical flows.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem end-to-end / journey tests implementado. As equipes operam sem esta capacidade. | • No end-to-end / journey tests deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de end-to-end / journey tests com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | end-to-end / journey tests adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | end-to-end / journey tests padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | end-to-end / journey tests é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q4 — Em que medida Automação de Testes (contract testing) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% service pairs with contract tests`

**Contexto**

- **O que mede (what):** Consumer-driven contract tests catch API breakage.
- **Por que importa (why):** Contract tests protect microservice compatibility.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem contract testing implementado. As equipes operam sem esta capacidade. | • No contract testing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de contract testing com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | contract testing adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | contract testing padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | contract testing é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q5 — Em que medida Automação de Testes (AI-assisted test generation) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% tests AI-generated`

**Contexto**

- **O que mede (what):** AI proposes tests for new and changed code.
- **Por que importa (why):** AI-generated tests raise the floor on coverage.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem ai-assisted test generation implementado. As equipes operam sem esta capacidade. | • No AI-assisted test generation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de ai-assisted test generation com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | AI-assisted test generation adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | AI-assisted test generation padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | AI-assisted test generation é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q6 — Em que medida Automação de Testes (flaky-test detection & quarantine) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `flaky test rate`

**Contexto**

- **O que mede (what):** Flaky tests are auto-quarantined and triaged.
- **Por que importa (why):** Flaky tests erode trust; detection restores it.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem flaky-test detection & quarantine implementado. As equipes operam sem esta capacidade. | • No flaky-test detection & quarantine deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de flaky-test detection & quarantine com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | flaky-test detection & quarantine adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | flaky-test detection & quarantine padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | flaky-test detection & quarantine é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C6-Q7 — Em que medida Automação de Testes (mutation testing) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** qa-test, Desenvolvedor, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `mutation score of critical modules`

**Contexto**

- **O que mede (what):** Mutation testing validates the quality of the test suite.
- **Por que importa (why):** Mutation scores reveal whether tests actually catch bugs.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem mutation testing implementado. As equipes operam sem esta capacidade. | • No mutation testing deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de mutation testing com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | mutation testing adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | mutation testing padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | mutation testing é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C7 — Gestão de Incidentes e SRE

**7 questões neste capability.**

### P2-C7-Q1 — Em que medida Gestão de Incidentes e SRE (on-call rotation with tooling) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services with on-call`

**Contexto**

- **O que mede (what):** Every prod service has a named on-call rotation.
- **Por que importa (why):** Clear ownership is the foundation of reliability.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem on-call rotation with tooling implementado. As equipes operam sem esta capacidade. | • No on-call rotation with tooling deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de on-call rotation with tooling com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | on-call rotation with tooling adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | on-call rotation with tooling padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | on-call rotation with tooling é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q2 — Em que medida Gestão de Incidentes e SRE (blameless postmortems) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% incidents with postmortem`

**Contexto**

- **O que mede (what):** Postmortems focus on systems, not people.
- **Por que importa (why):** Blameless culture unlocks honest learning.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem blameless postmortems implementado. As equipes operam sem esta capacidade. | • No blameless postmortems deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de blameless postmortems com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | blameless postmortems adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | blameless postmortems padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | blameless postmortems é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q3 — Em que medida Gestão de Incidentes e SRE (error budget policy) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Segurança, product-owner
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% services using error budgets`

**Contexto**

- **O que mede (what):** Error budgets gate feature work vs reliability work.
- **Por que importa (why):** Error budgets make reliability a shared business decision.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem error budget policy implementado. As equipes operam sem esta capacidade. | • No error budget policy deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de error budget policy com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | error budget policy adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | error budget policy padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | error budget policy é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q4 — Em que medida Gestão de Incidentes e SRE (chaos engineering) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `gamedays per quarter`

**Contexto**

- **O que mede (what):** Controlled fault injection exercises resilience.
- **Por que importa (why):** Chaos engineering builds confidence in recovery.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem chaos engineering implementado. As equipes operam sem esta capacidade. | • No chaos engineering deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de chaos engineering com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | chaos engineering adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | chaos engineering padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | chaos engineering é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q5 — Em que medida Gestão de Incidentes e SRE (incident commander role) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% major incidents with IC`

**Contexto**

- **O que mede (what):** An incident commander coordinates response.
- **Por que importa (why):** A single coordinator reduces confusion during incidents.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem incident commander role implementado. As equipes operam sem esta capacidade. | • No incident commander role deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de incident commander role com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | incident commander role adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | incident commander role padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | incident commander role é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q6 — Em que medida Gestão de Incidentes e SRE (SRE-dev partnership model) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, engineering-leader, data-ai
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% teams with SRE partner`

**Contexto**

- **O que mede (what):** SRE and dev teams collaborate on reliability roadmaps.
- **Por que importa (why):** Embedded partnership beats gatekeeping.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sre-dev partnership model implementado. As equipes operam sem esta capacidade. | • No SRE-dev partnership model deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de sre-dev partnership model com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SRE-dev partnership model adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | SRE-dev partnership model padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | SRE-dev partnership model é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C7-Q7 — Em que medida Gestão de Incidentes e SRE (runbook automation) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% incidents with runbook run`

**Contexto**

- **O que mede (what):** Runbook steps are codified and executed automatically.
- **Por que importa (why):** Runbook automation shrinks MTTR and reduces human error.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem runbook automation implementado. As equipes operam sem esta capacidade. | • No runbook automation deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de runbook automation com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | runbook automation adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | runbook automation padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | runbook automation é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C8 — Gestão de Artefatos e Pacotes

**5 questões neste capability.**

### P2-C8-Q1 — Em que medida Gestão de Artefatos e Pacotes (internal package registry) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% packages via registry`

**Contexto**

- **O que mede (what):** Internal registry hosts all packages; no public-only deps.
- **Por que importa (why):** A registry enables auditing and availability controls.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem internal package registry implementado. As equipes operam sem esta capacidade. | • No internal package registry deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de internal package registry com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | internal package registry adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | internal package registry padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | internal package registry é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q2 — Em que medida Gestão de Artefatos e Pacotes (SBOM for every build) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% builds with SBOM`

**Contexto**

- **O que mede (what):** Each build generates a software bill of materials.
- **Por que importa (why):** SBOMs are now a regulatory and security requirement.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem sbom for every build implementado. As equipes operam sem esta capacidade. | • No SBOM for every build deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de sbom for every build com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | SBOM for every build adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | SBOM for every build padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | SBOM for every build é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q3 — Em que medida Gestão de Artefatos e Pacotes (artifact signing (SLSA)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% artifacts signed`

**Contexto**

- **O que mede (what):** Artifacts are signed and verified on deploy.
- **Por que importa (why):** Signing prevents supply-chain tampering.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem artifact signing (slsa) implementado. As equipes operam sem esta capacidade. | • No artifact signing (SLSA) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de artifact signing (slsa) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | artifact signing (SLSA) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | artifact signing (SLSA) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | artifact signing (SLSA) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q4 — Em que medida Gestão de Artefatos e Pacotes (vulnerability scanning of artifacts) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% artifacts scanned`

**Contexto**

- **O que mede (what):** Every artifact is scanned before deployment.
- **Por que importa (why):** Pre-deploy scanning blocks known-bad artifacts.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem vulnerability scanning of artifacts implementado. As equipes operam sem esta capacidade. | • No vulnerability scanning of artifacts deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de vulnerability scanning of artifacts com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | vulnerability scanning of artifacts adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | vulnerability scanning of artifacts padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | vulnerability scanning of artifacts é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C8-Q5 — Em que medida Gestão de Artefatos e Pacotes (retention & promotion policies) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `artifacts promoted via policy`

**Contexto**

- **O que mede (what):** Artifacts move through dev→stage→prod with policy gates.
- **Por que importa (why):** Promotion policies tie deploys to provenance.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem retention & promotion policies implementado. As equipes operam sem esta capacidade. | • No retention & promotion policies deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de retention & promotion policies com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | retention & promotion policies adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | retention & promotion policies padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | retention & promotion policies é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C9 — Gestão de Mudanças e GitOps

**5 questões neste capability.**

### P2-C9-Q1 — Em que medida Gestão de Mudanças e GitOps (GitOps controllers in prod) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% clusters on GitOps`

**Contexto**

- **O que mede (what):** Cluster state is reconciled from Git by a controller.
- **Por que importa (why):** GitOps makes change traceable, auditable, and reversible.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem gitops controllers in prod implementado. As equipes operam sem esta capacidade. | • No GitOps controllers in prod deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de gitops controllers in prod com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | GitOps controllers in prod adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | GitOps controllers in prod padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | GitOps controllers in prod é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q2 — Em que medida Gestão de Mudanças e GitOps (automated change tickets) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% changes ticketed automatically`

**Contexto**

- **O que mede (what):** Change records are created from PRs automatically.
- **Por que importa (why):** Automation keeps records accurate without slowing delivery.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem automated change tickets implementado. As equipes operam sem esta capacidade. | • No automated change tickets deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de automated change tickets com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | automated change tickets adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | automated change tickets padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | automated change tickets é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q3 — Em que medida Gestão de Mudanças e GitOps (approvals in PR (not tickets)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% approvals in PR`

**Contexto**

- **O que mede (what):** Change approvals happen in code review, not separate tickets.
- **Por que importa (why):** Approval-as-code cuts cycle time while keeping audit trail.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem approvals in pr (not tickets) implementado. As equipes operam sem esta capacidade. | • No approvals in PR (not tickets) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de approvals in pr (not tickets) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | approvals in PR (not tickets) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | approvals in PR (not tickets) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | approvals in PR (not tickets) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q4 — Em que medida Gestão de Mudanças e GitOps (environment promotion via PR) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% envs promoted via PR`

**Contexto**

- **O que mede (what):** Moving from stage to prod is a PR, not a click.
- **Por que importa (why):** PR-based promotion inherits review and rollback.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem environment promotion via pr implementado. As equipes operam sem esta capacidade. | • No environment promotion via PR deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de environment promotion via pr com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | environment promotion via PR adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | environment promotion via PR padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | environment promotion via PR é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C9-Q5 — Em que medida Gestão de Mudanças e GitOps (compliance evidence auto-collected) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** devops, Engenheiro de Plataforma, Segurança
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `controls automated`

**Contexto**

- **O que mede (what):** Evidence for SOC2/ISO is gathered automatically from CI.
- **Por que importa (why):** Auto-evidence turns audits into a side effect of normal work.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem compliance evidence auto-collected implementado. As equipes operam sem esta capacidade. | • No compliance evidence auto-collected deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de compliance evidence auto-collected com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | compliance evidence auto-collected adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | compliance evidence auto-collected padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | compliance evidence auto-collected é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

## P2-C10 — Segurança de Dependências e Cadeia de Suprimentos

**5 questões neste capability.**

### P2-C10-Q1 — Em que medida Segurança de Dependências e Cadeia de Suprimentos (dependabot or renovate on every repo) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% repos auto-updated`

**Contexto**

- **O que mede (what):** Dependabot or Renovate opens PRs for outdated deps.
- **Por que importa (why):** Automated updates keep CVE window short.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem dependabot or renovate on every repo implementado. As equipes operam sem esta capacidade. | • No dependabot or renovate on every repo deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de dependabot or renovate on every repo com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | dependabot or renovate on every repo adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | dependabot or renovate on every repo padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | dependabot or renovate on every repo é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q2 — Em que medida Segurança de Dependências e Cadeia de Suprimentos (allow-list registries only) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `% deps from allow-listed source`

**Contexto**

- **O que mede (what):** Proxy registries filter packages from trusted sources.
- **Por que importa (why):** Proxying blocks typosquatting and malicious packages.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem allow-list registries only implementado. As equipes operam sem esta capacidade. | • No allow-list registries only deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de allow-list registries only com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | allow-list registries only adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | allow-list registries only padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | allow-list registries only é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q3 — Em que medida Segurança de Dependências e Cadeia de Suprimentos (build provenance (SLSA level)) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `SLSA level reached`

**Contexto**

- **O que mede (what):** Builds carry verifiable provenance metadata.
- **Por que importa (why):** Provenance is the foundation of supply-chain trust.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem build provenance (slsa level) implementado. As equipes operam sem esta capacidade. | • No build provenance (SLSA level) deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de build provenance (slsa level) com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | build provenance (SLSA level) adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | build provenance (SLSA level) padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | build provenance (SLSA level) é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q4 — Em que medida Segurança de Dependências e Cadeia de Suprimentos (critical dep response playbook) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `median time to patch critical`

**Contexto**

- **O que mede (what):** A playbook handles Log4Shell-class events.
- **Por que importa (why):** Preparation beats improvisation in a zero-day.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem critical dep response playbook implementado. As equipes operam sem esta capacidade. | • No critical dep response playbook deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de critical dep response playbook com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | critical dep response playbook adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | critical dep response playbook padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | critical dep response playbook é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---

### P2-C10-Q5 — Em que medida Segurança de Dependências e Cadeia de Suprimentos (vendor/OSS risk reviews) foi adotado entre as equipes?

**Metadados**

- **Público-alvo:** Segurança, devops
- **Peso:** 1.0
- **Professional Edition:** Não
- **KPI principal:** `critical vendors reviewed/year`

**Contexto**

- **O que mede (what):** High-risk vendors and OSS dependencies are reviewed annually.
- **Por que importa (why):** Review surfaces risk before it becomes an incident.

**Formato da resposta**

Escala Likert de 5 níveis (L0–L4). Selecione **um** nível que melhor descreve a sua organização hoje. Adicione evidência textual e/ou anexos (PDF, DOCX, XLSX, PNG, JPEG — até 10 MB).

**Níveis e evidências esperadas**

| Nível | Rótulo | Descrição | Evidências sugeridas |
|---|---|---|---|
| **L0** | Inicial | Sem vendor/oss risk reviews implementado. As equipes operam sem esta capacidade. | • No vendor/OSS risk reviews deployed<br>• No documented policy<br>• No owner assigned |
| **L1** | Em Desenvolvimento | Implementação piloto de vendor/oss risk reviews com <10% de cobertura de equipes e uso ad-hoc. | • Pilot program documentation<br>• <10% team coverage<br>• No formal policy |
| **L2** | Definido | vendor/OSS risk reviews adotado por 25-50% das equipes com diretrizes básicas e treinamento. | • Adoption 25-50% rate measured<br>• Usage guidelines published<br>• Onboarding materials exist |
| **L3** | Gerenciado | vendor/OSS risk reviews padronizado em >75% das equipes com resultados medidos e governança. | • >75% adoption rate measured<br>• KPIs tracked monthly<br>• Governance reviews in place |
| **L4** | Otimizando | vendor/OSS risk reviews é otimizado, automatizado e continuamente melhorado com insights baseados em dados. | • >95% adoption rate measured<br>• Automated telemetry feedback loops<br>• Continuous improvement program |

---


## Como esta seção é pontuada

- Cada questão recebe um valor numérico do nível selecionado: L0=0, L1=1, L2=2, L3=3, L4=4.
- A pontuação da capacidade é a média ponderada das questões (peso default = 1.0; questões com peso 1.5 ou 2.0 contam mais).
- A pontuação do pilar **P2** é a média das 10 capacidades.
- O resultado é exibido em escala 0–4 e convertido para % de maturidade (nível / 4 × 100).

## Glossário rápido

- **Pillar:** dimensão estratégica de maturidade.
- **Capability:** subdomínio funcional dentro de um pilar.
- **Question:** item de avaliação concreto, ID padrão `P[1-3]-C[1-19]-Q[1-99]`.
- **Level (L0–L4):** ponto na escala Likert de maturidade.
- **KPI:** indicador-chave que valida objetivamente o nível declarado.
- **Evidence:** prova qualitativa (texto) ou quantitativa (anexo) que sustenta a resposta.
