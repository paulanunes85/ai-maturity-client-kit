# `relatorios/i18n/`

📖 **Navegação:** [🏠 Índice](../../README.md) · [« Relatórios](../README.md)

Catálogos de strings para localização dos 5 PDFs. Cada arquivo é um JSON plano `chave → tradução`.

## Conteúdo

| Arquivo | Idioma | Linhas (aprox.) |
|---|---|---|
| [`pt-br.json`](pt-br.json) | Português (Brasil) — **default** | base |
| [`en.json`](en.json) | English | base |
| [`es.json`](es.json) | Español | base |

## Como funciona

O renderer (`render_reports.py`) carrega o catálogo correspondente a `payload.locale` (`pt-br`, `en` ou `es`) e injeta uma função `t()` no contexto Jinja2:

```jinja2
<h1>{{ t('score_justification.title') }}</h1>
```

`payload.locale` é determinado por `respostas.json::metadata.language` (default: `pt-br`).

## Adicionar / alterar strings

> [!IMPORTANT]
> As 3 línguas devem ter **as mesmas chaves**. Se adicionar uma chave em `pt-br.json`, adicione também em `en.json` e `es.json` (mesmo que provisoriamente em PT — é melhor que `null`).

```bash
# Validar paridade de chaves
python3 -c "import json; a=set(json.load(open('relatorios/i18n/pt-br.json'))); b=set(json.load(open('relatorios/i18n/en.json'))); c=set(json.load(open('relatorios/i18n/es.json'))); print('faltam en:', a-b); print('faltam es:', a-c)"
```

## Convenção de chaves

Hierárquica por contexto: `<arquivo>.<seção>.<elemento>`. Exemplos:
- `score_justification.title`
- `roadmap_part_pillar.section.h1_initiatives`
- `common.priority.p0`
