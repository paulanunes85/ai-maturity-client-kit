# `relatorios/templates/`

📖 **Navegação:** [🏠 Índice](../../README.md) · [« Relatórios](../README.md)

Templates Jinja2 dos **5 PDFs** que o cliente recebe. **Não modifique** sem coordenação — mirroram exatamente os templates da plataforma web (`app/src/report-service/templates/`).

## Conteúdo

| Arquivo | Renderiza | Tamanho aprox. |
|---|---|---|
| [`score_justification.html.j2`](score_justification.html.j2) | `score_justification.pdf` — Justificativa executiva + PE Readiness + recomendação de caminho | ~330 KB |
| [`roadmap_part_pillar.html.j2`](roadmap_part_pillar.html.j2) | Renderizado **3 vezes** (P1/P2/P3) → `roadmap_part_pillar_p{1,2,3}.pdf` — Deep-dive por pilar | ~410 KB cada |
| [`roadmap_part4.html.j2`](roadmap_part4.html.j2) | `roadmap_part4.pdf` — Implementation Guide consolidado (Steering Committee, RACI, ADKAR, Quick Wins) | ~510 KB |
| [`_components.html.j2`](_components.html.j2) | Macros compartilhados (cards, badges, score meters, gauges) — incluído nos 3 templates acima | — |
| [`_print.css`](_print.css) | CSS de print com `@page` rules, paleta MS 4 cores via `:root`, tipografia Inter + JetBrains Mono | — |

## Como personalizar

> [!CAUTION]
> Editar os `.html.j2` aqui **afeta TODOS os clientes** que usarem o kit. Para customização por cliente, edite `saida/payload.json` e re-renderize com `render_reports.py`.

Se quiser realmente alterar o template:
1. Trabalhe em uma branch
2. Rode `make smoke` antes de commitar
3. Compare visualmente: `python3 relatorios/scripts/build_payload_and_render.py` vs PDFs em `referencia/exemplo-saida/`

## Variáveis-chave consumidas

Cada template espera campos específicos de `payload.json`. Para o schema completo, veja:
- [`../sample_payload.json`](../sample_payload.json) — exemplo populado
- [`../scripts/build_payload_and_render.py`](../scripts/build_payload_and_render.py) — código que monta o payload

## i18n

Strings localizáveis vivem em [`../i18n/`](../i18n/) (`en.json`, `es.json`, `pt-br.json`). Os templates leem via `{{ t('chave') }}`.
