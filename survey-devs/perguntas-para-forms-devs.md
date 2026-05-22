# Perguntas para Microsoft Forms — Developer Survey (GitHub + IA)

> 75 perguntas em 9 seções. Tempo estimado para preencher: **20-25 min**. ANÔNIMO — não pedimos nome ou email do respondente.

## Como criar o Forms

1. Acesse https://forms.office.com → **+ New Form**
2. Título sugerido: `Developer Survey — Como minha equipe usa GitHub & IA hoje`
3. Subtítulo:
   ```
   Survey anônimo (15-25 min) sobre suas práticas com GitHub Copilot,
   modos do Copilot Chat (Ask/Edit/Agent), agentes IA, instructions files,
   melhores práticas de IA + Dev e segurança.
   Suas respostas vão alimentar o roadmap de adoção de IA no time.
   ```
4. **Settings** (⚙️):
   - ☑ **Anonymous responses** (CRÍTICO — deixar marcado)
   - ☑ One response per person: **DESMARCADO** (queremos múltiplos)
   - ☑ Accept responses
5. Adicione **9 seções** (botão `+ Add new` → ícone de seção):
   - **S1 — Perfil do respondente** (7 perguntas)
   - **S2 — GitHub Copilot — Adoção e Modos** (9 perguntas)
   - **S3 — Outras ferramentas Microsoft / GitHub AI** (7 perguntas)
   - **S4 — Práticas de Desenvolvimento com IA** (9 perguntas)
   - **S5 — Conceitos e Estrutura de Agentes** (11 perguntas)
   - **S6 — Markdown / Memory / Instructions** (6 perguntas)
   - **S7 — Usabilidade e Best Practices** (9 perguntas)
   - **S8 — Segurança e Governança** (13 perguntas)
   - **S9 — Pain Points & Wishlist** (4 perguntas)

6. Para cada pergunta abaixo, adicione no Forms o tipo correspondente:
   - **`choice`** → Choice (Single answer)
   - **`multi`** → Choice (Multiple answers / checkboxes)
   - **`text`** → Long Text

7. **TÍTULO** de cada pergunta deve começar com o ID + dois pontos. Exemplo:
   ```
   S2-Q1: Você tem licença GitHub Copilot ativa?
   ```
   > ⚠️ O ID é usado pela skill `/importar-survey-devs` para mapear de volta. NÃO REMOVA.

8. Compartilhe via **+ Send / Collect responses** → copiar link → enviar via Slack/Teams/email

9. Quando tiver respostas, **Responses → Open in Excel** → renomear para `respostas-survey-devs.xlsx` → mover para a raiz do `kit-cliente/`

---

## S1 — Perfil do respondente

_Perguntas básicas sobre você e seu contexto. Anônimo — não pediremos nome ou email._

_7 perguntas nesta seção._

### Pergunta `S1-Q1` — _Choice (single answer)_

> **S1-Q1: Qual seu cargo atual?**

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

### Pergunta `S1-Q2` — _Choice (single answer)_

> **S1-Q2: Tempo total como desenvolvedor?**

Opções:
- < 2 anos
- 2-5 anos
- 6-10 anos
- 11-15 anos
- > 15 anos

### Pergunta `S1-Q3` — _Choice (single answer)_

> **S1-Q3: Há quanto tempo usa IA no desenvolvimento (Copilot, Cursor, Claude Code, etc.)?**

Opções:
- Nunca usei
- < 3 meses
- 3-12 meses
- 1-2 anos
- > 2 anos

### Pergunta `S1-Q4` — _Choice (multiple answers)_

> **S1-Q4: Linguagens principais que você usa no dia-a-dia?**

Opções:
- TypeScript / JavaScript
- Python
- C# / .NET
- Java / Kotlin
- Go
- Rust
- C++
- Ruby
- PHP
- Swift
- SQL (foco principal)
- Outra

### Pergunta `S1-Q5` — _Choice (single answer)_

> **S1-Q5: Quantas horas por dia você passa codando (em média)?**

Opções:
- < 2h
- 2-4h
- 4-6h
- 6-8h
- > 8h

### Pergunta `S1-Q6` — _Choice (single answer)_

> **S1-Q6: Qual o tamanho do seu squad / time imediato?**

Opções:
- Sou solo
- 2-4 pessoas
- 5-9 pessoas
- 10-15 pessoas
- > 15 pessoas

### Pergunta `S1-Q7` — _Choice (single answer)_

> **S1-Q7: Modelo de trabalho?**

Opções:
- Remoto 100%
- Híbrido (1-2 dias presencial)
- Híbrido (3-4 dias)
- Presencial 100%

---

## S2 — GitHub Copilot — Adoção e Modos

_Foco no GitHub Copilot. Inclui os modos atuais (Ask, Edit, Agent) + Coding Agent autônomo (sucessor do Workspace, GA set/2025) e Spaces (contexto compartilhado, GA set/2025, substituiu Knowledge Bases)._

_9 perguntas nesta seção._

### Pergunta `S2-Q1` — _Choice (single answer)_

> **S2-Q1: Você tem licença GitHub Copilot ativa?**

Opções:
- Sim — Copilot Enterprise
- Sim — Copilot Business
- Sim — Copilot Pro+ (individual)
- Sim — Copilot Pro (individual)
- Sim — Copilot Free
- Tenho licença mas não uso
- Não tenho licença

### Pergunta `S2-Q2` — _Choice (single answer)_

> **S2-Q2: Frequência de uso do Copilot?**

Opções:
- Diariamente (várias horas)
- Diariamente (esporádico)
- Semanal
- Raramente
- Nunca

### Pergunta `S2-Q3` — _Choice (multiple answers)_

> **S2-Q3: Quais MODOS do Copilot Chat você usa? (selecione todos que se aplicam)**

Opções:
- Ask (responder perguntas)
- Edit (edição multi-arquivo no IDE)
- Agent (autônomo no IDE, executa tasks)
- Copilot Coding Agent (autônomo no GitHub.com — assigna issue, abre PR sozinho)
- Plan / Vision
- Não uso o Chat — só completion inline
- Não conheço esses modos

### Pergunta `S2-Q4` — _Choice (single answer)_

> **S2-Q4: Qual MODO você usa MAIS no dia-a-dia?**

Opções:
- Ask
- Edit
- Agent (no IDE)
- Coding Agent (autônomo no GitHub)
- Plan / Vision
- Só completion inline
- Não sei a diferença

### Pergunta `S2-Q5` — _Choice (multiple answers)_

> **S2-Q5: Quais features do Copilot você usa?**

Opções:
- Inline code completion
- Chat (perguntas no IDE)
- Pull Request descriptions automáticas
- Pull Request review (Copilot review)
- Test generation
- Documentation generation
- Issue resolution (Coding Agent assigna issue)
- Slash commands no Chat (/explain, /fix, /tests)
- Copilot Spaces (contexto compartilhado: repos + docs + custom instructions)
- Copilot Coding Agent (tarefas autônomas)
- Copilot CLI (gh copilot)

### Pergunta `S2-Q6` — _Choice (multiple answers)_

> **S2-Q6: Onde você usa Copilot?**

Opções:
- VS Code
- Visual Studio
- JetBrains (IntelliJ, PyCharm, etc.)
- Neovim
- Xcode
- GitHub.com (web)
- GitHub Mobile
- GitHub Codespaces
- CLI (gh copilot)

### Pergunta `S2-Q7` — _Choice (single answer)_

> **S2-Q7: Ganho de produtividade percebido com Copilot?**

Opções:
- Negativo (atrapalha)
- Neutro (sem ganho)
- +10-20%
- +20-40%
- +40-60%
- +60% ou mais
- Não sei medir

### Pergunta `S2-Q8` — _Choice (multiple answers)_

> **S2-Q8: Para QUE TAREFAS o Copilot mais te ajuda?**

Opções:
- Boilerplate / código repetitivo
- Refactoring
- Escrever testes
- Aprender API/lib nova
- Debugging
- Explicar código legado
- Documentação
- SQL / queries complexas
- Regex
- Tradução entre linguagens
- Onboarding em projeto novo

### Pergunta `S2-Q9` — _Long Text (resposta livre)_

> **S2-Q9: Em quais tarefas o Copilot NÃO te ajuda (ou atrapalha)?**

---

## S3 — Outras ferramentas Microsoft / GitHub AI

_Ecossistema Microsoft Foundry (ex-Azure AI Foundry) e features avançadas do GitHub._

_7 perguntas nesta seção._

### Pergunta `S3-Q1` — _Choice (multiple answers)_

> **S3-Q1: Quais outras ferramentas Microsoft / GitHub AI você USA hoje?**

Opções:
- Microsoft Foundry (ex-Azure AI Foundry)
- Foundry Agent Service (GA — built on OpenAI Responses API)
- Azure OpenAI Service (direto via API)
- Microsoft 365 Copilot
- GitHub Copilot Spaces
- GitHub Copilot Coding Agent (autônomo)
- GitHub Codespaces
- GitHub Models (playground multi-LLM)
- GitHub Advanced Security (GHAS)
- GitHub Actions com Copilot integration
- Visual Studio com Copilot avançado
- Nenhuma das acima

### Pergunta `S3-Q2` — _Choice (multiple answers)_

> **S3-Q2: Para QUE você usa Microsoft Foundry / Azure OpenAI (se usa)?**

Opções:
- PoC / experimentação
- Feature de produto em produção
- Embeddings / RAG
- Foundry Agent Service para agentes autônomos
- Multi-agent orchestration via MCP
- Fine-tuning
- Connectors (Dynamics, SAP, SharePoint, etc.)
- Não uso

### Pergunta `S3-Q3` — _Choice (single answer)_

> **S3-Q3: Conhece o GitHub Copilot Coding Agent (sucessor do Workspace, GA set/2025 — assigna issue e abre PR sozinho)?**

Opções:
- Uso ativamente em produção
- Já testei mas não uso recorrente
- Conheço mas nunca usei
- Não conheço

### Pergunta `S3-Q4` — _Choice (single answer)_

> **S3-Q4: Conhece Copilot Spaces (contexto compartilhado — substituiu Knowledge Bases)?**

Opções:
- Uso e crio Spaces para meu time
- Uso Spaces criados por outros
- Conheço mas não uso
- Não conheço

### Pergunta `S3-Q5` — _Choice (single answer)_

> **S3-Q5: Conhece o GitHub Spec Kit (github/spec-kit) para Spec-Driven Development?**

Opções:
- Uso
- Conheço mas não uso
- Não conheço

### Pergunta `S3-Q6` — _Choice (single answer)_

> **S3-Q6: Conhece MCP (Model Context Protocol) — padrão para agentes consumirem tools/contexto?**

Opções:
- Uso servidores MCP no meu workflow
- Configurei algum MCP server custom
- Conheço o conceito
- Não conheço

### Pergunta `S3-Q7` — _Choice (single answer)_

> **S3-Q7: Já usou GitHub Models para testar diferentes LLMs (gpt-4o, claude, llama, etc.)?**

Opções:
- Uso recorrente
- Já testei
- Não conheço

---

## S4 — Práticas de Desenvolvimento com IA

_Como você incorpora IA no seu fluxo: TDD, SDD (Spec-Driven Development), pair programming com IA, etc._

_9 perguntas nesta seção._

### Pergunta `S4-Q1` — _Choice (single answer)_

> **S4-Q1: Você pratica TDD (Test-Driven Development) com IA — escrever teste primeiro com Copilot?**

Opções:
- Sempre que possível
- Frequentemente
- Às vezes
- Raramente
- Nunca
- Não sei o que é TDD

### Pergunta `S4-Q2` — _Choice (single answer)_

> **S4-Q2: Você pratica SDD (Spec-Driven Development) — escrever spec → IA gera código?**

Opções:
- Uso ativamente (com Spec Kit ou similar)
- Já testei em alguns projetos
- Conheço o conceito mas não uso
- Nunca ouvi falar

### Pergunta `S4-Q3` — _Choice (multiple answers)_

> **S4-Q3: Em QUE momentos você consulta IA durante o coding?**

Opções:
- Antes de começar (planejar arquitetura)
- Durante (autocomplete + perguntas)
- Após implementar (review/refactor)
- Quando trava (debugging)
- Para escrever testes
- Para escrever docs
- Para code review do meu próprio PR

### Pergunta `S4-Q4` — _Choice (single answer)_

> **S4-Q4: Considera o Copilot/agente IA como um 'pair programmer'?**

Opções:
- Sim — trato como par
- Às vezes (depende da tarefa)
- Não — só ferramenta de autocompletar
- Não uso de forma estruturada

### Pergunta `S4-Q5` — _Choice (single answer)_

> **S4-Q5: Frequência: você refatora código com ajuda de IA?**

Opções:
- Toda semana
- Algumas vezes por mês
- Raramente
- Nunca

### Pergunta `S4-Q6` — _Choice (single answer)_

> **S4-Q6: Quem mantém a documentação do código no seu time?**

Opções:
- IA gera e o time revisa
- Devs escrevem manualmente, IA ajuda às vezes
- Time mantém manualmente, sem IA
- Documentação está abandonada

### Pergunta `S4-Q7` — _Choice (single answer)_

> **S4-Q7: Quando você tem um bug difícil, sua primeira ação é?**

Opções:
- Pergunto ao Copilot Chat / Claude / outro AI
- Procuro nos logs / debugger
- Pergunto a colega humano
- Stack Overflow / documentação
- Depende do bug

### Pergunta `S4-Q8` — _Choice (single answer)_

> **S4-Q8: Onboarding em projeto novo — você usa IA (com Copilot Spaces ou similar) para entender a base de código?**

Opções:
- Sempre — primeira coisa que faço
- Frequentemente
- Às vezes
- Não — leio README e código manualmente

### Pergunta `S4-Q9` — _Long Text (resposta livre)_

> **S4-Q9: Descreva 1 prática concreta com IA que MUDOU sua produtividade nos últimos 6 meses:**

---

## S5 — Conceitos e Estrutura de Agentes

_Verifica conhecimento e uso de agentes IA estruturados, incluindo personas Agentic DevOps da Microsoft (System Designer / Agent Operator) e práticas de teste/governança de agentes._

_11 perguntas nesta seção._

### Pergunta `S5-Q1` — _Choice (single answer)_

> **S5-Q1: Você sabe o que é um 'AI agent' (autônomo, vs. assistente reativo)?**

Opções:
- Sim — explico claramente
- Sim — vagamente
- Não sei a diferença
- Não conheço o termo

### Pergunta `S5-Q2` — _Choice (single answer)_

> **S5-Q2: Sabe diferença entre Ask, Edit, Agent e Coding Agent (modos do Copilot)?**

Opções:
- Sim — uso conscientemente
- Mais ou menos
- Não sei a diferença

### Pergunta `S5-Q3` — _Choice (single answer)_

> **S5-Q3: Já criou ou usou um custom agent (.github/agents/*.agent.md ou equivalente Claude/Cursor)?**

Opções:
- Já criei
- Já usei mas não criei
- Sei que existem mas nunca usei
- Não sabia que era possível

### Pergunta `S5-Q4` — _Choice (single answer)_

> **S5-Q4: Você conhece o conceito de 'skill' (SKILL.md ou equivalente — bloco reutilizável de instruções)?**

Opções:
- Conheço e uso
- Conheço mas não uso
- Não conheço

### Pergunta `S5-Q5` — _Choice (single answer)_

> **S5-Q5: Já criou prompt files (.prompt.md em .github/prompts/)?**

Opções:
- Sim — várias
- Sim — uma ou duas
- Não, mas planejo
- Não conheço

### Pergunta `S5-Q6` — _Choice (single answer)_

> **S5-Q6: Conhece A2A (Agent-to-Agent protocol) — agentes comunicando entre si?**

Opções:
- Uso (ex.: Foundry A2A Tool)
- Conheço o conceito
- Não conheço

### Pergunta `S5-Q7` — _Choice (single answer)_

> **S5-Q7: Conhece handoffs entre agentes (agente A passa contexto para agente B)?**

Opções:
- Uso
- Conheço o conceito
- Não conheço

### Pergunta `S5-Q8` — _Choice (single answer)_

> **S5-Q8: Conhece subagentes (agente principal delega tarefas para sub-agentes especializados)?**

Opções:
- Uso
- Conheço o conceito
- Não conheço

### Pergunta `S5-Q9` — _Choice (single answer)_

> **S5-Q9: Conhece as personas Agentic DevOps Microsoft: 'System Designer' (define specs/constraints) e 'Agent Operator' (orquestra agents)?**

Opções:
- Sim — adoto explicitamente
- Conheço o conceito
- Não conheço

### Pergunta `S5-Q10` — _Choice (single answer)_

> **S5-Q10: Você TESTA seus custom agents/prompts/skills antes de usar em código real?**

Opções:
- Sempre — tenho test suite para meus agents
- Frequentemente — manual mas sistemático
- Às vezes — só sanity check
- Raramente / nunca
- Não crio agents/prompts/skills

### Pergunta `S5-Q11` — _Choice (multiple answers)_

> **S5-Q11: Quais primitivos você JÁ CRIOU para uso pessoal/team?**

Opções:
- Custom prompts (.prompt.md)
- Custom skills (SKILL.md)
- Custom agents (.agent.md)
- Custom MCP server
- Instructions files (copilot-instructions.md / AGENTS.md / CLAUDE.md)
- Spaces compartilhados
- Nenhum dos acima

---

## S6 — Markdown / Memory / Instructions

_Sobre arquivos de configuração que ensinam o agente sobre seu projeto._

_6 perguntas nesta seção._

### Pergunta `S6-Q1` — _Choice (multiple answers)_

> **S6-Q1: Quais arquivos de instruções você USA hoje?**

Opções:
- .github/copilot-instructions.md
- .github/instructions/*.instructions.md
- AGENTS.md
- CLAUDE.md (raiz do projeto)
- .cursorrules
- Custom instructions em Copilot Spaces
- Nenhum

### Pergunta `S6-Q2` — _Choice (single answer)_

> **S6-Q2: Quem mantém o(s) arquivo(s) de instruções no seu projeto?**

Opções:
- Time inteiro contribui
- 1-2 pessoas dedicadas
- Eu mantenho sozinho
- Ninguém mantém — está desatualizado
- Não temos

### Pergunta `S6-Q3` — _Choice (single answer)_

> **S6-Q3: Frequência de update desses arquivos?**

Opções:
- Toda semana
- Mensalmente
- Trimestralmente
- Quando algo quebra
- Nunca atualizo

### Pergunta `S6-Q4` — _Choice (multiple answers)_

> **S6-Q4: O QUE você inclui nos arquivos de instruções?**

Opções:
- Code style / convenções do projeto
- Domain knowledge (regras de negócio)
- Stack / ferramentas
- Forbidden patterns (o que NÃO fazer)
- Examples (good vs bad code)
- Estrutura de pastas / arquitetura
- Comandos comuns (test, build, deploy)
- Não tenho instruções

### Pergunta `S6-Q5` — _Choice (single answer)_

> **S6-Q5: Tem prompt library compartilhada com seu time (repo ou Copilot Space dedicado)?**

Opções:
- Sim — Copilot Space compartilhado
- Sim — repo dedicado
- Sim — wiki/Confluence
- Cada um mantém o seu
- Não compartilhamos prompts

### Pergunta `S6-Q6` — _Choice (single answer)_

> **S6-Q6: Usa memory persistente do agente (Foundry Memory, Claude memory, Copilot memory)?**

Opções:
- Uso ativamente
- Já testei
- Não conheço

---

## S7 — Usabilidade e Best Practices

_Como você (e o time) aprende e melhora o uso de IA._

_9 perguntas nesta seção._

### Pergunta `S7-Q1` — _Choice (multiple answers)_

> **S7-Q1: Como você APRENDEU a usar Copilot/IA no dev?**

Opções:
- Auto-aprendizado (tentativa e erro)
- Workshop interno da empresa
- Documentação oficial
- Vídeos do YouTube
- Curso online (Coursera, Udemy, MS Learn)
- Champion no time
- Eventos / conferências (Microsoft Build, GitHub Universe)
- Comunidades / Discord / Slack

### Pergunta `S7-Q2` — _Choice (single answer)_

> **S7-Q2: Existe um 'AI/Copilot Champion' no seu time/empresa (alguém que ajuda os outros)?**

Opções:
- Sim — eu sou
- Sim — outra pessoa
- Não, mas precisava ter
- Não — cada um se vira

### Pergunta `S7-Q3` — _Choice (single answer)_

> **S7-Q3: Tem canal/comunidade interna para discutir uso de IA na engenharia?**

Opções:
- Sim — ativo (>5 mensagens/semana)
- Sim — pouco ativo
- Não temos canal dedicado
- Não sei

### Pergunta `S7-Q4` — _Choice (multiple answers)_

> **S7-Q4: Sua organização MEDE produtividade do dev de forma estruturada?**

Opções:
- DORA metrics (lead time, deployment freq, MTTR, change failure)
- DX index (developer experience)
- SPACE framework
- Métricas de adoção do Copilot (active users)
- Self-report periódico (survey)
- Não medimos formalmente

### Pergunta `S7-Q5` — _Choice (single answer)_

> **S7-Q5: Quantas iterações típicas em um prompt antes de você ter o resultado bom?**

Opções:
- Acerta na 1ª tentativa
- 2-3 iterações
- 4-6 iterações
- 7+ iterações (frequente)

### Pergunta `S7-Q6` — _Choice (single answer)_

> **S7-Q6: Você confia no código gerado por IA o suficiente para mergeá-lo SEM revisar linha-a-linha?**

Opções:
- Nunca — sempre reviso
- Para mudanças triviais (sim)
- Frequentemente (confio)
- Quase sempre

### Pergunta `S7-Q7` — _Choice (single answer)_

> **S7-Q7: Frequência com que você detecta 'hallucinations' (IA inventa API/método inexistente)?**

Opções:
- Diariamente
- Semanalmente
- Raramente
- Quase nunca

### Pergunta `S7-Q8` — _Choice (single answer)_

> **S7-Q8: Desde que adotou IA, sente que está APRENDENDO mais ou menos sobre engenharia?**

Opções:
- Aprendendo MUITO MAIS (IA acelera)
- Um pouco mais
- Mais ou menos igual
- Aprendendo MENOS (dependência)
- Não sei avaliar

### Pergunta `S7-Q9` — _Choice (single answer)_

> **S7-Q9: Você compartilha bons prompts/exemplos de uso com colegas (em Spaces, Slack, Confluence)?**

Opções:
- Frequentemente — em canal compartilhado
- Às vezes — pessoalmente
- Raramente
- Nunca

---

## S8 — Segurança e Governança

_Práticas de segurança no uso de IA + governança de agentes (escopo, red-lines, JIT permissions, audit)._

_13 perguntas nesta seção._

### Pergunta `S8-Q1` — _Choice (single answer)_

> **S8-Q1: Sua organização tem POLÍTICA DOCUMENTADA de uso de IA na engenharia?**

Opções:
- Sim — política formal e clara
- Sim — mas pouco clara
- Política informal (sem documento)
- Não temos política
- Não sei

### Pergunta `S8-Q2` — _Choice (single answer)_

> **S8-Q2: Você sabe QUAIS DADOS PODEM ir para LLMs externas (Copilot, ChatGPT)?**

Opções:
- Sei claramente o que pode e o que NÃO pode
- Tenho ideia geral
- Vagamente
- Não sei

### Pergunta `S8-Q3` — _Choice (multiple answers)_

> **S8-Q3: Quais tipos de dados você JAMAIS coloca em prompts de IA externa?**

Opções:
- PII / dados pessoais de clientes
- Secrets / API keys / tokens
- Código de IP estratégico
- Dados financeiros
- Dados de saúde
- Nenhuma restrição (não temos política)

### Pergunta `S8-Q4` — _Choice (multiple answers)_

> **S8-Q4: Quais ferramentas de SEGURANÇA estão ativas no seu repo?**

Opções:
- GitHub Advanced Security (GHAS)
- CodeQL scanning
- Secret scanning
- Dependabot / dependency review
- SBOM (Software Bill of Materials)
- Microsoft Defender for DevOps
- Microsoft Defender for Cloud
- Snyk / SonarQube / outro SAST
- Nenhuma

### Pergunta `S8-Q5` — _Choice (single answer)_

> **S8-Q5: Code Scanning roda em código GERADO por IA (no PR ou no IDE)?**

Opções:
- Sim — gate obrigatório no PR
- Sim — opcional
- Roda mas não bloqueia
- Não roda

### Pergunta `S8-Q6` — _Choice (single answer)_

> **S8-Q6: Sua org gera SBOM dos serviços críticos?**

Opções:
- Sim — automatizado
- Sim — manual quando solicitado
- Não geramos
- Não sei

### Pergunta `S8-Q7` — _Choice (single answer)_

> **S8-Q7: Existe processo formal de REVIEW para código gerado por IA antes de merge?**

Opções:
- Sim — review obrigatório por outro humano + scanner
- Review humano obrigatório (sem scanner extra)
- Review opcional
- Não temos processo

### Pergunta `S8-Q8` — _Choice (single answer)_

> **S8-Q8: Quando você cria/usa um custom agent, define ESCOPO e RED-LINES explícitos (ex.: 'agent não pode aprovar próprio PR')?**

Opções:
- Sempre — escopo + red-lines documentados
- Frequentemente
- Às vezes
- Raramente / nunca
- Não crio/uso custom agents

### Pergunta `S8-Q9` — _Choice (single answer)_

> **S8-Q9: Sua org tem permissões JIT (Just-In-Time) para agents — vs. permissões persistentes?**

Opções:
- Sim — JIT obrigatório para agents
- Sim — opcional
- Não temos JIT
- Não sei

### Pergunta `S8-Q10` — _Choice (single answer)_

> **S8-Q10: Sua org tem DLP (Data Loss Prevention) configurado para evitar dados sensíveis em prompts?**

Opções:
- Sim — bloqueia ativamente
- Sim — alerta mas não bloqueia
- Não temos
- Não sei

### Pergunta `S8-Q11` — _Choice (single answer)_

> **S8-Q11: Sua org tem AUDIT LOGS de uso do Copilot/agentes IA — incluindo decisões autônomas de agents?**

Opções:
- Sim — logs ativos e revisados
- Logs ativos mas não revisados
- Não temos
- Não sei

### Pergunta `S8-Q12` — _Choice (single answer)_

> **S8-Q12: Já recebeu TREINAMENTO formal de segurança no uso de IA?**

Opções:
- Sim — treinamento obrigatório anual
- Sim — uma vez (no onboarding)
- Não recebi treinamento
- Não sei

### Pergunta `S8-Q13` — _Choice (single answer)_

> **S8-Q13: Frequência: você já viu Copilot/IA sugerir código com vulnerabilidade óbvia (SQL injection, XSS, hardcoded secrets, etc.)?**

Opções:
- Diariamente
- Semanalmente
- Mensalmente
- Quase nunca

---

## S9 — Pain Points & Wishlist

_Suas ideias e frustrações. Texto livre — fique à vontade._

_4 perguntas nesta seção._

### Pergunta `S9-Q1` — _Long Text (resposta livre)_

> **S9-Q1: O QUE MAIS te frustra hoje no uso de IA no seu dia-a-dia de engenharia?**

### Pergunta `S9-Q2` — _Long Text (resposta livre)_

> **S9-Q2: Que MUDANÇA na ferramenta/processo dobraria sua produtividade?**

### Pergunta `S9-Q3` — _Long Text (resposta livre)_

> **S9-Q3: Que feature/ferramenta Microsoft/GitHub você gostaria que existisse (ou conhecesse melhor)?**

### Pergunta `S9-Q4` — _Choice (single answer)_

> **S9-Q4: Você gostaria de receber a versão consolidada deste survey (insights agregados de toda a equipe)?**

Opções:
- Sim — quero ver
- Não, obrigado

---

## Resumo final

- **9 seções** (1 por tema)
- **75 perguntas** (55 choice + 15 multi + 5 long text)
- **Tempo estimado:** 20-25 min (rascunho rápido em 10 min)
- **Respostas esperadas:** quanto mais devs, melhor — mínimo 5, ideal 15+

## Próximos passos

1. Após coletar respostas, **Responses → Open in Excel** no Microsoft Forms
2. Renomeie o Excel para `respostas-survey-devs.xlsx`
3. Mova para a raiz do `kit-cliente/`
4. No Copilot Chat (modo Agent): `/importar-survey-devs`
5. Depois: `/insights-developer-survey` para gerar relatório consolidado
