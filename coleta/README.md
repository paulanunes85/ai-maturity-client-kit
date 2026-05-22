# `coleta/` — Coletar respostas via Microsoft Forms ou Excel multi-respondente

Esta pasta tem tudo para o cliente coletar respostas de **3 ou mais pessoas** via Microsoft Forms (ou planilha Excel/SharePoint compartilhada). A skill `/importar-respostas-excel` consome o output e gera `respostas.json` agregado (média por questão).

## Arquivos

| Arquivo | O que é |
|---|---|
| **[INSTRUCOES-FORMS.md](INSTRUCOES-FORMS.md)** | Guia passo-a-passo dos 3 caminhos: Forms manual completo, Forms enxuto piloto, Excel/SharePoint direto |
| **[perguntas-para-forms.md](perguntas-para-forms.md)** | As 158 perguntas formatadas para copy/paste no Microsoft Forms (estrutura por pillar/capability) |
| **[template-export-forms.xlsx](template-export-forms.xlsx)** | Excel template no formato exato do Forms export — 158 colunas pergunta + 158 evidência + 3 respondentes mockados para teste |

## Quando usar cada arquivo

- **Vai criar Microsoft Forms manual?** → leia `INSTRUCOES-FORMS.md` (Caminho A) + abra `perguntas-para-forms.md` ao lado para copy/paste
- **Vai usar Excel/SharePoint direto (mais rápido)?** → leia `INSTRUCOES-FORMS.md` (Caminho C) + use `template-export-forms.xlsx` como base
- **Quer testar a skill `/importar-respostas-excel` agora?** → renomeie `template-export-forms.xlsx` → `respostas-forms.xlsx`, mova para a raiz do kit, rode a skill (ela detecta automaticamente)

## Próximo passo

Depois de coletar (Forms ou Excel), você terá um arquivo `respostas-forms.xlsx`. Mova para a raiz do `kit-cliente/` e rode no Copilot Chat:

```
/importar-respostas-excel
```

Ou simplesmente:

```
@ai-maturity-assistant
```

— o concierge detecta o arquivo e te conduz.
