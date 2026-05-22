# Perguntas para Microsoft Forms — Learning & Growth Survey

> **Survey IDENTIFICADO** (nome + email) de 32 perguntas em 7 seções. Tempo estimado: **5-8 min**. Foca em o que devs querem APRENDER + formato preferido + barreiras + Champions.

**Diferente dos surveys anteriores:**
- Assessment principal: maturidade organizacional (Likert L0-L4)
- Developer Survey: comportamento real anônimo
- **Este Learning Survey: roadmap de capacitação IDENTIFICADO** (precisa nome+email para convidar para workshops)

## Como criar o Forms

1. Acesse <https://forms.office.com> → **+ New Form**
2. Título: `Learning & Growth IA — O que você quer aprender nos próximos 6 meses?`
3. Subtítulo:
   ```
   Survey de 5-8 min sobre seu plano de capacitação em IA.
   IDENTIFICADO (precisamos nome+email para te convidar para os workshops certos).
   Resultado: plano de capacitação personalizado + cohorts + Champions Network.
   ```
4. **Settings** (⚙️):
   - ☐ **Anonymous responses** (DESMARCADO — survey identificado)
   - ☑ **Only people in my organization** (recomendado)
   - ☑ **One response per person** (1 por dev)
   - ☑ **Accept responses**
   - ☑ Email notification of each response (você acompanha em tempo real)
5. Adicione 7 seções (uma por L1..L7):
   - **L1 — Identificação** (4 perguntas)
   - **L2 — Auto-percepção de maturidade IA** (7 perguntas)
   - **L3 — Onde quer crescer (priorização pessoal)** (2 perguntas)
   - **L4 — Tópicos específicos que quer aprender** (5 perguntas)
   - **L5 — Formato e cadência preferidos** (4 perguntas)
   - **L6 — Champions e mentoria** (5 perguntas)
   - **L7 — Barreiras e Wishlist** (5 perguntas)

6. Para cada pergunta abaixo:
   - **`choice`** → Choice (Single answer)
   - **`multi`** → Choice (Multiple answers)
   - **`text`** → Long Text
   - **`text-short`** → Short Text (1 linha)

7. **TÍTULO** começa SEMPRE com o ID + dois pontos. Exemplo:
   ```
   L4-Q1: Quais tópicos de GitHub Copilot você quer dominar?
   ```
8. **Required**: marque L1-Q1 (nome) e L1-Q2 (email) como required. Demais opcionais.
9. Compartilhe via **Send → Link** com TODOS os devs da empresa
10. Quando tiver respostas: **Responses → Open in Excel** → renomeie para `respostas-survey-learning.xlsx` → mova para raiz do `kit-cliente/`

---

## L1 — Identificação

_Survey IDENTIFICADO — vamos usar seu nome/email para CONVIDAR você para os workshops/cohorts certos. Não compartilhamos respostas individuais publicamente._

_4 perguntas nesta seção._

### Pergunta `L1-Q1` — _Short Text (1 linha)_

> **L1-Q1: Seu nome completo:**

### Pergunta `L1-Q2` — _Short Text (1 linha)_

> **L1-Q2: Email corporativo (para convites de workshops):**

### Pergunta `L1-Q3` — _Choice (single answer)_

> **L1-Q3: Cargo:**

Opções:
- Desenvolvedor Backend
- Desenvolvedor Frontend
- Full-Stack
- SRE / Platform Engineer
- Data Engineer / ML Engineer
- Architect
- Tech Lead
- Engineering Manager
- QA / SDET
- DevOps / DevEx
- Outro

### Pergunta `L1-Q4` — _Choice (single answer)_

> **L1-Q4: Time / Squad:**

Opções:
- [Lista a customizar pela org]
- Outro / não pertenço a um squad fixo

---

## L2 — Auto-percepção de maturidade IA

_Avalie sua confiança HOJE em cada uma das 7 dimensões da rubrica de maturidade. Honestidade conta — quanto mais real, melhor o plano._

_7 perguntas nesta seção._

### Pergunta `L2-Q1` — _Choice (single answer)_

> **L2-Q1: **D2 — Copilot Adoption** (modos Ask/Edit/Agent/Coding Agent, features, ganho mensurado): qual seu nível?**

Opções:
- L0 — Nunca usei ou não conheço
- L1 — Sei o básico (inline completion)
- L2 — Uso Ask/Edit no dia-a-dia
- L3 — Uso Agent + Spaces, mensuro ganho
- L4 — Domino Coding Agent autônomo, prompt library do time

### Pergunta `L2-Q2` — _Choice (single answer)_

> **L2-Q2: **D3 — Microsoft/GitHub Tooling** (Foundry, Spaces, Coding Agent, MCP, Spec Kit, GHAS): qual seu nível?**

Opções:
- L0 — Não conheço o ecossistema
- L1 — Conheço de nome
- L2 — Uso 2-3 ferramentas básicas
- L3 — Uso 4+ ferramentas avançadas
- L4 — Domino o ecossistema completo (incl. Foundry/MCP)

### Pergunta `L2-Q3` — _Choice (single answer)_

> **L2-Q3: **D4 — AI Dev Practices** (TDD com IA, SDD, pair programming, debugging com IA): qual seu nível?**

Opções:
- L0 — Nenhuma prática estruturada
- L1 — Uso IA pontualmente
- L2 — TDD ou SDD ocasional
- L3 — Trato IA como pair em várias fases
- L4 — Pair programmer mindset completo + SDD com Spec Kit

### Pergunta `L2-Q4` — _Choice (single answer)_

> **L2-Q4: **D5 — Agent Concepts** (custom agents, skills, prompts, MCP, A2A, handoffs, subagentes, personas Agentic DevOps): qual seu nível?**

Opções:
- L0 — Não sei o que é um agente
- L1 — Conheço só o básico
- L2 — Conheço modos do Copilot
- L3 — Já criei custom agents/skills/prompts
- L4 — Domino MCP, A2A, subagentes, testo agents

### Pergunta `L2-Q5` — _Choice (single answer)_

> **L2-Q5: **D6 — Instructions / Memory** (copilot-instructions.md, AGENTS.md, CLAUDE.md, Spaces, prompt library): qual seu nível?**

Opções:
- L0 — Não uso instructions files
- L1 — Tenho 1 arquivo básico
- L2 — Uso e atualizo ocasionalmente
- L3 — Time mantém ativamente
- L4 — Prompt library compartilhada + Spaces colaborativos

### Pergunta `L2-Q6` — _Choice (single answer)_

> **L2-Q6: **D7 — Best Practices** (Champion, métricas DORA/DX, comunidade, compartilha prompts): qual seu nível?**

Opções:
- L0 — Não tenho cultura de IA estruturada
- L1 — Auto-aprendizado isolado
- L2 — Tenho Champion no time
- L3 — Mensuro DORA/DX + compartilho com colegas
- L4 — Comunidade ativa + revisão regular de adoção

### Pergunta `L2-Q7` — _Choice (single answer)_

> **L2-Q7: **D8 — Security & Governance** (política IA, GHAS, SBOM, JIT permissions, red-lines de agents, audit): qual seu nível?**

Opções:
- L0 — Sem política, sem ferramentas
- L1 — Política informal
- L2 — GHAS ativo + política básica
- L3 — Scanners obrigatórios + SBOM + treinamento
- L4 — JIT permissions + red-lines docs + audit revisado

---

## L3 — Onde quer crescer (priorização pessoal)

_Pensando nos próximos 6 meses, em que dimensões você MAIS quer evoluir?_

_2 perguntas nesta seção._

### Pergunta `L3-Q1` — _Choice (multiple answers)_

> **L3-Q1: Selecione as **3 dimensões PRIORITÁRIAS** para você crescer nos próximos 6 meses (escolha exatamente 3):**

Opções:
- D2 — Copilot Adoption (modos avançados, Coding Agent)
- D3 — MS/GitHub Tooling (Foundry, Spaces, Spec Kit, MCP)
- D4 — AI Dev Practices (TDD com IA, SDD)
- D5 — Agent Concepts (custom agents, MCP, A2A)
- D6 — Instructions / Memory (instructions files, prompt library)
- D7 — Best Practices (DORA, comunidade, mentoria)
- D8 — Security & Governance (GHAS, SBOM, red-lines)

### Pergunta `L3-Q2` — _Long Text (resposta livre)_

> **L3-Q2: Por que escolheu essas 3 dimensões? (1-2 frases — opcional mas ajuda muito)**

---

## L4 — Tópicos específicos que quer aprender

_Marque TODOS os tópicos que você gostaria de aprender ou aprofundar._

_5 perguntas nesta seção._

### Pergunta `L4-Q1` — _Choice (multiple answers)_

> **L4-Q1: Quais tópicos de **GitHub Copilot** você quer dominar?**

Opções:
- Modo Ask (perguntas eficazes)
- Modo Edit (edição multi-arquivo)
- Modo Agent (autônomo no IDE)
- Coding Agent (autônomo no GitHub.com — assigna issue, abre PR)
- Copilot Spaces (contexto compartilhado)
- PR review com Copilot
- Test generation
- Slash commands (/explain, /fix, /tests)
- Copilot CLI
- Já domino tudo isso

### Pergunta `L4-Q2` — _Choice (multiple answers)_

> **L4-Q2: Quais tópicos de **Microsoft Foundry / Azure AI** você quer aprender?**

Opções:
- Microsoft Foundry — visão geral
- Foundry Agent Service (criar agentes)
- Azure OpenAI Service (API direta)
- Embeddings + RAG
- MCP (Model Context Protocol) + Foundry MCP server
- A2A (Agent-to-Agent) protocol
- Multi-agent orchestration
- Connectors (Dynamics, SAP, SharePoint)
- Foundry Memory (long-term context)
- Não tenho interesse em Foundry hoje

### Pergunta `L4-Q3` — _Choice (multiple answers)_

> **L4-Q3: Quais tópicos de **práticas com IA** você quer aprender?**

Opções:
- TDD com IA (test-first com Copilot)
- SDD com Spec Kit (Spec-Driven Development)
- Prompt engineering (técnicas avançadas)
- Pair programming com IA (mindset + práticas)
- Refactoring com IA
- Code review com IA antes de PR
- Debugging assistido por IA
- Onboarding em projeto novo com IA + Spaces
- Documentação automática

### Pergunta `L4-Q4` — _Choice (multiple answers)_

> **L4-Q4: Quais tópicos de **agentes e primitives** você quer aprender?**

Opções:
- Criar custom agents (.agent.md)
- Criar custom skills (SKILL.md)
- Criar prompt files (.prompt.md)
- Configurar custom MCP server
- Subagentes (delegação)
- Handoffs entre agentes
- Personas Agentic DevOps (System Designer, Agent Operator)
- Testar agents (test suites para prompts/skills)
- Guardrails / red-lines de agents

### Pergunta `L4-Q5` — _Choice (multiple answers)_

> **L4-Q5: Quais tópicos de **segurança e governança** você quer aprender?**

Opções:
- GitHub Advanced Security (CodeQL, secret scan)
- SBOM (Software Bill of Materials)
- Microsoft Defender for DevOps / Cloud
- DLP para prompts de IA
- JIT permissions para agentes
- Audit logs de IA + análise
- Política de uso de IA (templates)
- Vulnerabilidades comuns em código gerado por IA
- Compliance / LGPD / GDPR + IA

---

## L5 — Formato e cadência preferidos

_Como você aprende melhor?_

_4 perguntas nesta seção._

### Pergunta `L5-Q1` — _Choice (multiple answers)_

> **L5-Q1: Quais formatos de aprendizado funcionam melhor para você?**

Opções:
- Workshop hands-on presencial/remoto (3-4h)
- Workshop curto (1h, sandwich seminar)
- Curso online self-paced (Coursera, Pluralsight, MS Learn)
- Pair programming com Champion
- Office hours semanais (dúvidas livres)
- Vídeos curtos (YouTube, Microsoft Learn)
- Podcast
- Book club / paper club
- Hackathon interno
- Show & tell de colegas
- Documentação escrita + tentativa-e-erro

### Pergunta `L5-Q2` — _Choice (single answer)_

> **L5-Q2: Quanto tempo por SEMANA você dedicaria a aprender IA/Copilot?**

Opções:
- < 1h/semana
- 1-2h/semana
- 2-4h/semana
- 4-6h/semana
- Mais de 6h/semana

### Pergunta `L5-Q3` — _Choice (multiple answers)_

> **L5-Q3: Que horário/dia funciona melhor para workshops síncronos?**

Opções:
- Manhã de quarta/quinta
- Tarde de quarta/quinta
- Sexta tarde (low-stress)
- Almoço (lunch & learn)
- Após expediente (com hora extra)
- Não consigo síncrono — só self-paced

### Pergunta `L5-Q4` — _Choice (single answer)_

> **L5-Q4: Prefere cohorts (grupo fixo aprendendo junto) ou self-paced (no seu ritmo)?**

Opções:
- Cohort (grupo fixo, mais accountability)
- Self-paced (meu ritmo, mais flexibilidade)
- Híbrido (módulos self-paced + sessões síncronas)
- Não tenho preferência

---

## L6 — Champions e mentoria

_Sobre comunidade interna e mentoria._

_5 perguntas nesta seção._

### Pergunta `L6-Q1` — _Choice (single answer)_

> **L6-Q1: Você se candidataria como **Champion de IA** no seu time/empresa (ajudar outros, organizar workshops)?**

Opções:
- Sim — quero ser Champion ativo
- Sim — mas só se tiver suporte/treino dedicado
- Talvez — preciso pensar
- Não tenho interesse hoje

### Pergunta `L6-Q2` — _Long Text (resposta livre)_

> **L6-Q2: Quem no seu time/empresa você considera **referência em IA** hoje? (nome opcional, ajuda a mapear champions naturais)**

### Pergunta `L6-Q3` — _Choice (single answer)_

> **L6-Q3: Você gostaria de mentoria 1:1 com alguém mais experiente em IA?**

Opções:
- Sim — mentor sênior em IA
- Sim — peer mentoring (mesmo nível, troca mútua)
- Não — prefiro auto-aprendizado
- Outro (especifique no campo livre)

### Pergunta `L6-Q4` — _Choice (single answer)_

> **L6-Q4: Você se ofereceria para mentorar/ensinar OUTRAS pessoas em algum tópico?**

Opções:
- Sim — em vários tópicos
- Sim — em 1 tópico específico
- Talvez — depende do tópico
- Não me sinto pronto

### Pergunta `L6-Q5` — _Long Text (resposta livre)_

> **L6-Q5: Se respondeu sim à anterior, em QUE tópico(s) você se sentiria confortável mentorando?**

---

## L7 — Barreiras e Wishlist

_O que te impede de aprender mais? E que workshop você gostaria de organizar/atender?_

_5 perguntas nesta seção._

### Pergunta `L7-Q1` — _Choice (multiple answers)_

> **L7-Q1: Quais BARREIRAS te impedem de aprender mais sobre IA hoje?**

Opções:
- Falta de tempo (sprint pressure)
- Falta de licença Copilot
- Falta de licença para Foundry / Azure AI
- Falta de espaço para experimentar (sandbox / repo de teste)
- Falta de treinamento estruturado
- Falta de Champion no time
- Política de segurança bloqueia testes
- Não sei por onde começar
- Não vejo prioridade clara da liderança
- Falta de orçamento para cursos pagos
- Tudo bem — sem barreiras significativas

### Pergunta `L7-Q2` — _Long Text (resposta livre)_

> **L7-Q2: Que **workshop interno** você gostaria que existisse (mesmo se for ambicioso)?**

### Pergunta `L7-Q3` — _Long Text (resposta livre)_

> **L7-Q3: Que **palestrante externo** (interno/parceiro/comunidade) você gostaria de trazer?**

### Pergunta `L7-Q4` — _Long Text (resposta livre)_

> **L7-Q4: Algo mais que queira compartilhar sobre seu desejo de aprendizado em IA?**

### Pergunta `L7-Q5` — _Choice (single answer)_

> **L7-Q5: Você quer receber o **plano de capacitação consolidado** (resultado deste survey) por email?**

Opções:
- Sim — quero ver o plano e os workshops sugeridos
- Não, obrigado

---

## Resumo
- **7 seções**
- **32 perguntas** (15 choice + 9 multi + 8 text)
- **Tempo:** 5-8 min
- **Identificado** (precisa nome + email)

## Próximos passos

1. Coletar respostas (1-2 semanas, lembrar 1×/semana)
2. Exportar Excel → renomear `respostas-survey-learning.xlsx` → mover para raiz do kit
3. No Copilot Chat (modo Agent):
   ```
   /importar-survey-learning
   /plano-capacitacao
   ```
4. Receber plano de capacitação priorizado em `saida/plano-capacitacao-DATA.md`
