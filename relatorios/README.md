# `relatorios/` — Templates Jinja2 oficiais + renderer Python (PDFs finais)

Esta pasta contém o **pipeline de geração dos 5 PDFs production-quality** — espelho fiel da plataforma web. Os templates são copiados de `app/src/report-service/templates/` (mesma versão do código de produção).

> ⚠️ **Não modifique** os arquivos `templates/` e `i18n/` — qualquer alteração quebra a paridade com a plataforma. Para personalizar branding/conteúdo, edite o `payload.json` gerado em `saida/` antes de re-renderizar.

## Estrutura

```
relatorios/
├── templates/                          ← 4 .html.j2 oficiais + CSS de print
│   ├── _components.html.j2             (componentes reutilizáveis: tabelas, badges, headers)
│   ├── _print.css                      (branding + paginação + cores L0-L4 + responsive)
│   ├── score_justification.html.j2     (PDF #1: justificativa de score + PE Readiness)
│   ├── roadmap_part_pillar.html.j2     (PDF #2/#3/#4: renderizado 3x — 1 por pillar)
│   └── roadmap_part4.html.j2           (PDF #5: implementation guide consolidado)
│
├── i18n/                               ← Strings dos 3 idiomas suportados
│   ├── en.json                         (~21 KB)
│   ├── es.json                         (~22 KB)
│   └── pt-br.json                      (~22 KB)
│
├── scripts/
│   ├── build_payload_and_render.py     ⭐ Script principal — invocado por /gerar-relatorio
│   ├── render_reports.py               (renderer puro Jinja2 + WeasyPrint)
│   └── render_smoke.py                 (smoke test do template original — referência)
│
└── sample_payload.json                 (~66 KB — schema reference + sample data Acme)
```

## Como funciona o pipeline

```
┌─ INPUTS ────────────────────────────────────────────────┐
│  respostas.json                                          │
│  saida/scores.json + gaps.json + recomendacoes.json     │
│  implementation-guide-inputs.json (opcional)             │
│  relatorios/sample_payload.json (base structure)         │
└─────────────────┬───────────────────────────────────────┘
                  ↓
   build_payload_and_render.py:
   1. Carrega sample_payload.json (estrutura completa rica)
   2. SOBRESCREVE só campos que temos dados:
      • organization, scores, capabilities, gap_analysis
      • implementation_guide_inputs (se wizard rodou)
   3. MANTÉM placeholders para narrativa que cliente não preencheu:
      • capabilities[].scoring_rationale, h1_initiatives
      • risks_per_pillar, success_metrics_per_pillar
      • Steering Committee, RACI (se wizard não rodou)
   4. Escreve saida/payload.json (debug/customização)
   5. Invoca render_reports.py
                  ↓
   render_reports.py:
   1. Carrega payload + i18n[locale] + 4 templates Jinja2
   2. Renderiza 5 templates com WeasyPrint (HTML+CSS → PDF)
   3. Output: saida/*.pdf
                  ↓
┌─ OUTPUTS (saida/) ──────────────────────────────────────┐
│  payload.json                                            │
│  score_justification.pdf       (~330 KB)                 │
│  roadmap_part_pillar_p1.pdf    (~410 KB)                 │
│  roadmap_part_pillar_p2.pdf    (~410 KB)                 │
│  roadmap_part_pillar_p3.pdf    (~410 KB)                 │
│  roadmap_part4.pdf             (~510 KB)                 │
└──────────────────────────────────────────────────────────┘
```

## Como rodar manualmente (sem Copilot)

```bash
# 1. Instalar dependências (uma vez)
python3 -m pip install --user --break-system-packages jinja2 weasyprint openpyxl
# Mac: brew install cairo pango gdk-pixbuf libffi

# 2. Pipeline completo (precisa de respostas.json + saida/scores.json+gaps.json+recomendacoes.json)
python3 relatorios/scripts/build_payload_and_render.py

# 3. OU: re-renderizar só (após editar saida/payload.json manualmente)
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida

# 4. OU: trocar locale (en / es / pt-br)
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --locale en --out saida/en
```

## Personalização

### Padrão 1 — Implementation Guide (Parte 4)
```
/wizard-implementacao    # 9 steps preenchem comitês, RACI, ADKAR, quick wins
/gerar-relatorio         # re-renderiza com Parte 4 personalizada
```

### Padrão 2 — Narrativa profunda (per capability)
```bash
# Após a primeira renderização:
code saida/payload.json   # editar campos:
                          # • capabilities[].scoring_rationale
                          # • capabilities[].h1_initiatives, h1_state_evidence
                          # • technology_resources_per_pillar
                          # • risks_per_pillar, success_metrics_per_pillar

# Re-renderizar (pula merge):
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida
```

### Padrão 3 — Mudar idioma
Edite `respostas.json::metadata.language` para `"en"`, `"es"` ou `"pt-br"` e rode `/gerar-relatorio`.

## Versão dos templates

Os templates em `templates/` espelham **`app/src/report-service/templates/`** versão do app no momento de criação do kit. Quando a plataforma evoluir os templates, atualize esta pasta copiando da source-of-truth.

## Documentação relacionada

- Algoritmo de scoring → [`../referencia/pontuacao-e-calculo.md`](../referencia/pontuacao-e-calculo.md)
- Schema do payload → veja `sample_payload.json`
- Skill que invoca → [`../.github/skills/gerar-relatorio/SKILL.md`](../.github/skills/gerar-relatorio/SKILL.md)
- PDFs exemplo → [`../referencia/exemplo-saida/`](../referencia/exemplo-saida/)
