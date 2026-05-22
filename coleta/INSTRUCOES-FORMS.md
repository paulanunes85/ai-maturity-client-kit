# Como criar o Microsoft Forms para o AI Maturity Assessment

📖 **Navegação:** [🏠 Índice](../README.md) · [« Guia passo-a-passo](../GUIA-PASSO-A-PASSO.md) · Você está aqui · [» Survey-devs](../survey-devs/INSTRUCOES-FORMS-DEVS.md)

> [!TIP]
> Este guia mostra **3 caminhos** para criar e usar o Microsoft Forms com as 158 questões. Escolha o que melhor se encaixa no tempo disponível e perfil técnico da equipe.

---

## ⚖️ Comparação rápida dos 3 caminhos

| Caminho | Tempo de setup | Esforço | Quando usar |
|---|---|---|---|
| **A. Forms manual completo** | 4–6 horas | Alto (criar 158 perguntas) | Você quer experiência Forms 100% nativa, com seções e branding |
| **B. Forms enxuto (1 capability piloto)** | 30 minutos | Baixo | PoC ou validação com poucos respondentes antes de escalar |
| **C. Direto no Excel/SharePoint** ⭐ | 5 minutos | Mínimo | **Recomendado** — usa o template Excel que já vem no kit, evita 4h de criação |

---

## 🅰️ Caminho A — Forms manual completo (158 perguntas)

### Passo 1 · Criar o Forms

1. Acesse https://forms.office.com (login com sua conta Microsoft 365)
2. Clique em **+ New Form**
3. Título: `AI Maturity Assessment - <Nome da sua organização>`
4. Subtítulo (opcional):
   ```
   Avaliação de maturidade IA em 3 pillars: Produtividade, DevOps e Plataforma.
   158 questões com escala L0-L4. Tempo estimado: 45-90 minutos.
   Suas respostas são confidenciais e usadas apenas para gerar o roadmap.
   ```

### Passo 2 · Configurar 3 seções

Adicione 3 seções (botão **+ Add new** → ícone de seção):

| Seção | Título | Subtítulo sugerido |
|---|---|---|
| 1 | **Pilar P1 — Produtividade do Desenvolvedor** | 53 questões em 9 capabilities |
| 2 | **Pilar P2 — Ciclo de Vida DevOps** | 59 questões em 10 capabilities |
| 3 | **Pilar P3 — Plataforma de Aplicações** | 46 questões em 9 capabilities |

### Passo 3 · Adicionar as 158 questões

Para cada questão, adicione **2 elementos** no Forms:

1. **Choice (single answer)** com a pergunta + as 6 opções de nível
2. **Long Text** (opcional) para evidência

Use o documento [`perguntas-para-forms.md`](perguntas-para-forms.md) como fonte de copy/paste — ele tem as 158 perguntas formatadas com IDs (`P1-C1-Q1`, etc.) e o texto completo.

#### Opções fixas para TODAS as questões (cole idênticas)

```
L0 — Inicial — Sem prática estabelecida
L1 — Em Desenvolvimento — Pilotos isolados (<25%)
L2 — Definido — Cobertura 25-50% com diretrizes
L3 — Gerenciado — >75% com métricas de impacto
L4 — Otimizando — Universal (>95%) com automação contínua
NA — Não sei / Não se aplica
```

> ⚠️ **CRÍTICO:** o prefixo `L0`, `L1`, ..., `L4`, `NA` deve estar **literalmente no início** de cada opção. A skill de importação usa esse prefixo para mapear de volta para o número (0–4 ou null). Não traduza, não reformate.

#### Formato do título de cada pergunta

```
P1-C1-Q1: <texto da pergunta>
```

> ⚠️ **IMPORTANTE:** o ID (`P1-C1-Q1`) deve estar **literalmente no início** do título da pergunta, seguido de `:`. Exemplo de [`perguntas-para-forms.md`](perguntas-para-forms.md):
>
> `P1-C1-Q1: Em que medida sua organização utiliza ferramentas de completação de código com IA (ex. GitHub Copilot)?`

#### Formato do campo de evidência

```
Evidência (P1-C1-Q1)
```

Tipo: **Long Text**, opcional (não marcar como required).

### Passo 4 · Configurar permissões

1. Botão **Settings** (engrenagem) no canto superior direito
2. **Who can fill out this form**:
   - **Only people in my organization** — recomendado se for uso interno
   - **Anyone with the link** — se for cross-empresa (consultoria)
3. **One response per person** — desabilitado (queremos múltiplos para agregar)
4. **Email notification of each response** — opcional

### Passo 5 · Compartilhar

1. Botão **Send/Collect responses**
2. Copiar o link
3. Compartilhar via Email/Teams/SharePoint com a equipe

### Passo 6 · Exportar respostas

Quando tiver respostas suficientes (recomendado: ≥3 respondentes para reduzir viés):

1. Aba **Responses**
2. Botão **Open in Excel**
3. Salvar o arquivo como **`respostas-forms.xlsx`**
4. Mover para a raiz do `kit-cliente/`

### Passo 7 · Importar no kit

No VS Code, abra o Copilot Chat (modo **Agent**) e digite:

```
/importar-respostas-excel
```

A skill:
- Detecta o `respostas-forms.xlsx` automaticamente
- Faz backup do `respostas.json` atual
- Agrega múltiplos respondentes via média por questão
- Sobrescreve `respostas.json`
- Gera `saida/import-log-<DATA>.md`

Depois rode `/pipeline-completo` normalmente.

---

## 🅱️ Caminho B — Forms enxuto (1 capability piloto)

Para **validar o fluxo end-to-end** antes de investir na criação completa.

### Passo 1 · Escolher 1 capability

Escolha 1 capability com 5-7 questões. Sugestão: **P1-C1 (Assistentes de Codificação IA)** — é o tema mais "quente" e vai gerar boa discussão na equipe.

### Passo 2 · Criar o Forms só com essas 5 questões

Mesmo processo do Caminho A, mas com apenas **5 perguntas** em vez de 158. Tempo: 15-30 min.

### Passo 3 · Coletar 3-5 respostas

Compartilhe com seu time imediato (não com toda a empresa). Tempo: 1-2 dias.

### Passo 4 · Importar e rodar

Como o `respostas.json` vai ter só 5 questões respondidas, o **threshold ficará em BLOCKED** (precisa ≥25). Mas:
- Você valida que o fluxo Forms → Excel → respostas.json funciona
- Você vê como aparece no relatório uma capability com dados reais

Para gerar relatório útil, complete manualmente o resto via `respostas.json` ou expanda o Forms.

---

## 🅲 Caminho C — Direto no Excel/SharePoint ⭐ (RECOMENDADO)

Pula o Forms e usa o **template Excel** que já vem no kit.

### Passo 1 · Pegar o template

O kit vem com [`coleta/template-export-forms.xlsx`](template-export-forms.xlsx). Esse arquivo:
- Tem o **mesmo formato** que o Forms exportaria
- Já tem as 158 colunas de pergunta + 158 de evidência
- Vem com **3 respondentes mockados** como exemplo (você pode apagar e substituir)

### Passo 2 · Subir no SharePoint/OneDrive

1. Limpar as 3 linhas de respondentes mockados (linhas 2, 3, 4) — manter só o header
2. Renomear: `respostas-forms.xlsx` (ou outro nome)
3. **SharePoint:** subir na library do projeto, gerar link "Anyone with the link can edit"
4. **OneDrive:** subir e compartilhar editar
5. **Teams:** anexar no canal e fixar

### Passo 3 · Cada respondente preenche uma linha

Compartilhe instruções:

```
Olá equipe!

Por favor preencham UMA linha por pessoa neste arquivo:
<link do SharePoint>

Para cada uma das 158 colunas de pergunta:
- Selecione um nível L0-L4 (ou deixe em branco se "não sabe")
- O texto deve começar com o código (ex.: "L3 — Gerenciado")
- Use a coluna de Evidência logo à direita para descrever ferramenta/cobertura/métrica

Tempo estimado: 45-90 min. Pode pausar e voltar.

Dúvidas? Consultem os documentos em referencia/P*.md (no kit-cliente).
```

### Passo 4 · Baixar o Excel

Quando todos preencherem:
1. SharePoint → arquivo → **Download a Copy**
2. Renomear para **`respostas-forms.xlsx`**
3. Mover para a raiz do `kit-cliente/`

### Passo 5 · Importar e rodar

```
/importar-respostas-excel
/pipeline-completo
```

---

## 🆚 Forms vs Excel direto — qual escolher?

| Critério | Microsoft Forms | Excel/SharePoint |
|---|---|---|
| **Tempo de setup** | 4-6h (criar 158 perguntas) | 5 min (template pronto) |
| **UX para o respondente** | Mobile-friendly, 1 pergunta por vez | Planilha (intimidante para não-técnicos) |
| **Validação de dados** | Fixa (Choice = só 6 opções) | Frágil (pessoa pode digitar qualquer coisa) |
| **Multi-respondente** | Nativo | Manual (1 linha por pessoa) |
| **Edição posterior** | Difícil (cada submit é final) | Fácil (qualquer um pode mudar a qualquer hora) |
| **Audit trail** | Nativo (timestamp por submit) | SharePoint version history |
| **Custo de licença** | Microsoft 365 padrão | Microsoft 365 padrão |
| **Integração com kit** | Idêntica (`/importar-respostas-excel`) | Idêntica |

**Recomendação prática:**
- **PoC / Time pequeno (3-5 pessoas):** Excel direto (Caminho C)
- **Roll-out organização (10+ respondentes):** Forms (Caminho A)
- **Cliente exigente / branding profissional:** Forms (Caminho A)

---

## 🔄 Outros formatos suportados pela skill

A skill `/importar-respostas-excel` aceita qualquer Excel/CSV cujo header de pergunta comece com `P[1-3]-C\d+-Q\d+:`. Isso inclui:

- ✅ **Microsoft Forms** export (formato oficial)
- ✅ **Google Forms** export (Sheets → Download as .xlsx)
- ✅ **Excel/SharePoint** custom (template do kit ou seu próprio)
- ✅ **CSV** (se renomear para .xlsx ou converter)
- ⚠️ **Typeform** — funciona se ajustar headers para ter os IDs

---

## 💡 Dicas práticas

### Dica 1 · Comece com 1 pillar
Não tente coletar respostas dos 3 pillars ao mesmo tempo. Comece pelo P1 (Produtividade) que é o mais tangível para devs. Depois P2 (DevOps) com SREs. Depois P3 (Plataforma) com arquitetos.

### Dica 2 · Pré-preenchimento por entrevista
Em vez de mandar o link e esperar, faça uma **entrevista de 1h por respondente** preenchendo junto. Você captura nuances melhor e gera evidências mais ricas.

### Dica 3 · Treine antes de soltar
Faça um **kick-off de 30 min** explicando:
- O que é o assessment
- Como L0-L4 são definidos
- Por que evidência importa
- Quanto tempo vai levar
- Quando vão receber o relatório

### Dica 4 · Rode ciclos curtos
Não espere 100% de respostas para rodar `/pipeline-completo`. Rode com 25 (WARNING), depois 50 (OK), depois 100. A cada ciclo, o relatório melhora e você captura mais conversas.

### Dica 5 · Versionamento
Toda vez que importar, a skill cria `respostas.json.backup-<timestamp>`. Guarde esses backups — eles são seu **histórico de evolução** entre rodadas do assessment.

---

## 🆘 Troubleshooting

| Problema | Diagnóstico | Solução |
|---|---|---|
| Skill não detecta `respostas-forms.xlsx` | Arquivo não está na raiz | Mover para `kit-cliente/respostas-forms.xlsx` (não em coleta/) |
| "Nenhum header reconhecido" | Headers do Excel não começam com `P1-C1-Q1:` etc. | Editar headers manualmente para incluir IDs no início |
| Respondente apareceu duplicado | Forms permite múltiplas submissões da mesma pessoa | Editar Excel manualmente para deletar linha duplicada antes de importar |
| Levels viraram texto | Forms exportou opção SEM o prefixo `L0/L1/...` | Reconstituir Forms incluindo os prefixos no início de cada Choice option |
| Excel tem 158 colunas mas só 90 questões reconhecidas | Headers truncados pelo Forms (limite de 4000 chars) | Encurtar o texto das perguntas no Forms (manter só o ID + frase resumida) |

---

## 📚 Referências

- **Lista completa das 158 perguntas formatadas para Forms:** [`perguntas-para-forms.md`](perguntas-para-forms.md)
- **Template Excel pronto (3 respondentes mockados):** [`template-export-forms.xlsx`](template-export-forms.xlsx)
- **Skill de importação:** [`../.github/skills/importar-respostas-excel/SKILL.md`](../.github/skills/importar-respostas-excel/SKILL.md)
- **Algoritmo de agregação multi-respondente:** [`../referencia/pontuacao-e-calculo.md`](../referencia/pontuacao-e-calculo.md) seção 6

---

**Versão:** 1.0 · **Data:** 2026-05-08

---

## Continuar a leitura

| ← ANTERIOR | PRÓXIMO → |
|:---|---:|
| **[Guia passo-a-passo](../GUIA-PASSO-A-PASSO.md)** | **[Developer Survey (anônimo)](../survey-devs/INSTRUCOES-FORMS-DEVS.md)** |
| Do zero ao PDF executivo em 60–90 min. | 75 perguntas anônimas sobre Copilot, agentes, governança, MCP / A2A. |

↑ [Voltar ao Índice do kit](../README.md)
