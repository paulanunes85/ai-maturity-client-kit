# Como criar o Microsoft Forms para o Developer Survey

📖 **Navegação:** [🏠 Índice](../README.md) · [« Coleta principal](../coleta/INSTRUCOES-FORMS.md) · Você está aqui · [» Learning Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.md)

> [!IMPORTANT]
> Survey **anônimo** de **75 perguntas** em 9 seções para entender como os desenvolvedores da sua organização usam GitHub Copilot, modos do Copilot Chat (Ask/Edit/Agent/**Coding Agent**), **Copilot Spaces**, **Microsoft Foundry**, agentes IA + **MCP / A2A**, instructions files, práticas (TDD/SDD com Spec Kit), **personas Agentic DevOps** (System Designer / Agent Operator), governança e segurança (incl. **JIT permissions** e **escopo+red-lines de agents**). Tempo estimado por respondente: **22-28 min**.

**Versão 2.0 (2026-05-08)** — termos atualizados com docs oficiais Microsoft/GitHub mais recentes.

**Diferente do assessment principal** (Likert L0-L4 organizacional). Este é **comportamental individual** — quanto mais devs respondem, mais rica a foto.

---

## 🎯 Quando usar este survey

- ✅ Antes de definir estratégia de adoção de IA na engenharia
- ✅ Após rollout de GitHub Copilot para medir adoção real
- ✅ Como input para o `/wizard-implementacao` (Implementation Guide do assessment principal)
- ✅ Trimestralmente para acompanhar evolução cultural
- ✅ Antes de workshops de Copilot/AI para identificar gaps

---

## 🔐 Anonimato — CRÍTICO

Este survey é **anônimo por design**:
- ❌ Não pedimos nome, email, ID corporativo
- ✅ Coletamos só: cargo, tempo de experiência, padrões de uso, opiniões
- ✅ Devs respondem com mais honestidade quando sabem que é anônimo
- ⚠️ No Microsoft Forms, **MARCAR "Anonymous responses"** nas Settings (sem isso, ele captura email da conta MS365)

---

## 📋 Os 9 temas cobertos (v2.0)

| # | Seção | Foco | Perguntas |
|---|---|---|---|
| **S1** | Perfil do respondente | Cargo, experiência, stack, modelo de trabalho | 7 |
| **S2** | GitHub Copilot — Adoção e Modos | Licença, frequência, **Ask / Edit / Agent / Coding Agent (autônomo)**, features (incl. **Spaces**), ganho | 9 |
| **S3** | Outras ferramentas Microsoft / GitHub AI | **Microsoft Foundry** (ex-Azure AI Foundry), **Foundry Agent Service**, **Copilot Spaces**, **Coding Agent**, GHAS, **Spec Kit**, **MCP** | 7 |
| **S4** | Práticas de Desenvolvimento com IA | **TDD com IA**, **SDD com Spec Kit**, pair programming, refactoring, debugging, onboarding | 9 |
| **S5** | Conceitos e Estrutura de Agentes | Agente vs assistente, modos Copilot, **custom agents/skills/prompts**, **A2A**, handoffs, subagentes, **personas Agentic DevOps** (System Designer / Agent Operator), **TESTAR agents antes de usar** | 11 |
| **S6** | Markdown / Memory / Instructions | `copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, custom instructions em **Spaces**, **Foundry Memory** | 6 |
| **S7** | Usabilidade e Best Practices | Como aprendeu (incl. MS Build / GitHub Universe), Champion, métricas DORA/DX, iterações, confiança | 9 |
| **S8** | Segurança e Governança | Política de IA, dados sensíveis, GHAS, CodeQL, SBOM, **Microsoft Defender for DevOps**, DLP, audit, **escopo+red-lines de agents**, **JIT permissions**, treinamento | 13 |
| **S9** | Pain Points & Wishlist | Frustrações, ideias, feature requests | 4 |
| | | **TOTAL** | **75** |

---

## 🛠️ Como criar o Forms (passo a passo)

### Passo 1 · Criar o formulário

1. Acesse <https://forms.office.com>
2. Clique em **+ New Form**
3. Título sugerido: `Developer Survey — Como minha equipe usa GitHub & IA hoje`
4. Subtítulo (cole isso):

```
Survey ANÔNIMO (20-25 min) sobre suas práticas com GitHub Copilot,
modos do Copilot Chat (Ask/Edit/Agent), agentes IA, instructions files,
melhores práticas de IA + Dev e segurança.

Suas respostas vão alimentar o roadmap de adoção de IA no time.
NÃO pedimos nome ou email — apenas cargo, tempo de experiência e padrões.

Tempo estimado: 20-25 min.
```

### Passo 2 · ⚠️ CONFIGURAR ANONIMATO

**Settings (engrenagem ⚙️ no canto superior direito):**

| Setting | Valor |
|---|---|
| **Anonymous responses** | ☑ **MARCADO** (CRÍTICO — sem isso captura email!) |
| **Who can respond** | "Anyone with the link" (se cross-org) ou "Only people in my organization" |
| **One response per person** | ☐ DESMARCADO (queremos múltiplos) |
| **Accept responses** | ☑ MARCADO |
| **Email notification** | ☑ MARCADO (opcional — você é avisado a cada resposta) |
| **Customize thank you message** | "Obrigado! Suas respostas estão sendo agregadas com as do time." |

> 🔍 **Como confirmar anonimato:** após criar, abra o link em janela anônima. Se NÃO aparecer "Logged in as [seu email]" no topo, está anônimo.

### Passo 3 · Criar 9 seções

No Forms, botão **+ Add new** → ícone de seção (ou "Add section"):

```
Section 1: S1 — Perfil do respondente            (7 questões)
Section 2: S2 — GitHub Copilot                   (9 questões)
Section 3: S3 — Outras ferramentas Microsoft/GH  (7 questões)
Section 4: S4 — Práticas de Desenvolvimento     (9 questões)
Section 5: S5 — Conceitos de Agentes             (11 questões)
Section 6: S6 — Markdown / Instructions          (6 questões)
Section 7: S7 — Usabilidade                      (9 questões)
Section 8: S8 — Segurança e Governança          (13 questões)
Section 9: S9 — Pain Points & Wishlist           (4 questões)
```

### Passo 4 · Adicionar as 75 perguntas

Use o documento [`perguntas-para-forms-devs.md`](perguntas-para-forms-devs.md) como **fonte de copy/paste**. Cada pergunta tem:
- **Tipo** (`choice`, `multi`, `text`)
- **ID** (`S2-Q1`, `S5-Q3`, etc.)
- **Texto da pergunta**
- **Opções** (para choice/multi)

**Para cada pergunta no Forms:**

1. Tipo:
   - `choice` (Single answer) → **Choice** com "Multiple answers" DESMARCADO
   - `multi` (Multiple answers) → **Choice** com "Multiple answers" MARCADO
   - `text` (Long Text) → **Long answer**

2. **TÍTULO da pergunta DEVE começar com o ID + dois pontos**:
   ```
   S2-Q1: Você tem licença GitHub Copilot ativa?
   ```
   > ⚠️ **CRÍTICO:** o ID é usado pela skill `/importar-survey-devs` para mapear de volta ao schema. Não remova nem altere o formato `SX-QY:`.

3. **Opções** (para choice/multi): cole as opções listadas no MD, **uma por linha**, na ordem.

4. **Required**: marque como required apenas as 7 perguntas de Perfil (S1-Q1 a S1-Q7). Demais opcionais (devs podem pular).

### Passo 5 · Compartilhar

1. Botão **+ Send / Collect responses** no topo
2. Escolher **Link** (não Email — quebra anonimato)
3. Copiar URL
4. Compartilhar via:
   - **Slack/Teams:** canal #engineering ou #copilot-users
   - **Email para todos os devs:** "Survey anônimo de 20 min — sua opinião conta"
   - **All-hands:** projetar QR code da URL para devs scanearem
5. **Deadline sugerido:** 2 semanas. Lembrar 1× por semana.

### Passo 6 · Acompanhar respostas

- Aba **Responses** mostra contagem em tempo real
- Recomendado: **mínimo 5 respondentes**, ideal **15+** para insights ricos
- Se baixa adesão: 1-on-1 com líderes para incentivar

### Passo 7 · Exportar quando tiver respostas suficientes

1. Aba **Responses** → botão **Open in Excel**
2. Salve o arquivo como **`respostas-survey-devs.xlsx`**
3. Mova para a **raiz do `kit-cliente/`** (não dentro de `survey-devs/`)
4. **Anonimato confirmado:** as colunas D (Email) e E (Name) devem estar vazias

### Passo 8 · Analisar com o kit

No Copilot Chat (modo Agent):

```
/importar-survey-devs
```

A skill:
- Detecta `respostas-survey-devs.xlsx`
- Parseia 75 perguntas × N respondentes
- Gera `survey-devs/respostas-devs.json`
- Gera `saida/import-survey-log-<DATE>.md`

Depois:

```
/insights-developer-survey
```

Gera relatório agregado em `saida/insights-developer-survey-<DATE>.md` com:
- Distribuição de cargos
- Top 5 features mais usadas do Copilot
- % adoção por modo (Ask/Edit/Agent/Workspace)
- Conhecimento de conceitos (agentes, MCP, handoffs)
- Maturidade de instructions files
- Gaps de governança e segurança
- Citations de pain points (anonimizados)
- Recomendações priorizadas para roadmap

---

## 🅱️ Caminho alternativo — Excel/SharePoint direto (sem Forms)

Mais rápido se a equipe é pequena (3-5 devs) e técnica.

1. Abra `survey-devs/template-export-forms-devs.xlsx`
2. Apague as 5 linhas de respondentes mockados (linhas 2-6) — manter linha 1 (headers)
3. Salve como `respostas-survey-devs.xlsx` e suba no SharePoint com link "Anyone can edit"
4. Cada dev preenche **uma linha** com suas respostas (texto livre nas células de resposta)
5. Quando todos preencherem: baixe → mova para raiz do kit → `/importar-survey-devs`

**Trade-off:** menos visual que Forms, mas zero setup. Adequado para times técnicos.

---

## 💡 Boas práticas da coleta

### Lance com contexto
Não jogue o link no Slack sem contexto. Crie momento:

> "Pessoal, antes de definirmos a estratégia de IA na engenharia para o próximo trimestre, queremos ouvir como vocês usam IA hoje. Survey anônimo de 20-25 min com 75 perguntas (Copilot, agentes, segurança…). Suas respostas vão diretamente no roadmap. Link: <URL>. Deadline: 2 semanas."

### Garanta anonimato (de verdade)
- Confirme que Settings → Anonymous está MARCADO
- Não force login MS365 (caso compartilhe externamente)
- No relatório agregado nunca cite respondentes específicos — só padrões

### Lembre periodicamente
- D+3: lembrete suave no canal
- D+7: recap "X respostas até agora, faltam Y dias"
- D+10: 1-on-1 com líderes para empurrar
- D+14: deadline final + começa análise

### Compartilhe os insights
Devs respondem mais um próximo survey se virem que o anterior gerou ação. Após `/insights-developer-survey`:
- Apresente em all-hands
- Gere quick wins (workshop, prompt library, etc.)
- Trimestralmente repita para medir evolução

---

## 🆘 Troubleshooting

| Problema | Diagnóstico | Solução |
|---|---|---|
| Skill não detecta arquivo | Não está na raiz | Mover `respostas-survey-devs.xlsx` para `kit-cliente/` (raiz) |
| Skill diz "0 respondentes" | Email/Name não vazios mas perguntas vazias | Verificar se respondentes preencheram pelo menos 1 pergunta |
| Headers não reconhecidos | Falta "SX-QY:" no início | Editar headers manualmente para incluir o ID |
| Aparece email no Excel | Anonymity OFF | Reconfigurar Forms → Settings → Anonymous Responses ON e re-enviar |
| Pouca adesão (< 5 respostas) | Lançamento sem contexto | Re-lance com mensagem do líder, deadline, propósito |

---

## 📚 Referências

- **As 75 perguntas formatadas:** [`perguntas-para-forms-devs.md`](perguntas-para-forms-devs.md)
- **Template Excel pronto (5 mocks):** [`template-export-forms-devs.xlsx`](template-export-forms-devs.xlsx)
- **JSON estruturado de exemplo:** [`respostas-mock-devs.json`](respostas-mock-devs.json)
- **Skill de import:** [`../.github/skills/importar-survey-devs/SKILL.md`](../.github/skills/importar-survey-devs/SKILL.md)
- **Skill de insights:** [`../.github/skills/insights-developer-survey/SKILL.md`](../.github/skills/insights-developer-survey/SKILL.md)
- **Relação com o assessment principal:** este survey COMPLEMENTA o assessment de maturidade. Os insights aqui informam as questões P1-C1, P1-C5, P1-C8 (Copilot, Onboarding, Métricas) e a governança em P2-C4 / P3-C6.

---

**Versão:** 1.0 · **Data:** 2026-05-08

---

## Continuar a leitura

| ← ANTERIOR | PRÓXIMO → |
|:---|---:|
| **[Coleta do assessment principal](../coleta/INSTRUCOES-FORMS.md)** | **[Learning & Growth Survey](../survey-learning/INSTRUCOES-FORMS-LEARNING.md)** |
| 3 caminhos para coletar as 158 perguntas do assessment via Forms / Excel. | 32 perguntas identificadas: plano de capacitação com Champions e workshops. |

↑ [Voltar ao Índice do kit](../README.md)
