# Exemplos de outputs finais — AI Maturity Assessment Kit

> Esta pasta contém **PDFs reais gerados a partir de `respostas.json.example`** (perfil "Cliente Exemplo S.A." — 46 respostas mockadas). São o **preview exato** do que o cliente vai gerar ao rodar `/pipeline-completo` com seus próprios dados.

## 📊 Os 5 PDFs principais — Cliente Exemplo S.A. (PT-BR)

| Arquivo | Tamanho | Conteúdo |
|---|---|---|
| **[score_justification.pdf](score_justification.pdf)** | 323 KB | Justificativa de score: overall **1.99 (L2 — Definido)**, breakdown por pillar, PE Readiness com path recommendation |
| **[roadmap_part_pillar_p1.pdf](roadmap_part_pillar_p1.pdf)** | 405 KB | Pillar P1 deep-dive — 9 capabilities de Produtividade (média **2.69 L3**) |
| **[roadmap_part_pillar_p2.pdf](roadmap_part_pillar_p2.pdf)** | 407 KB | Pillar P2 deep-dive — 10 capabilities de DevOps (média **1.52 L2**) |
| **[roadmap_part_pillar_p3.pdf](roadmap_part_pillar_p3.pdf)** | 409 KB | Pillar P3 deep-dive — 9 capabilities de Plataforma (média **1.92 L2**) |
| **[roadmap_part4.pdf](roadmap_part4.pdf)** | 504 KB | Implementation Guide consolidado (Three Horizons + comitês + RACI + comms + treinamento + ADKAR + quick wins) |

**Total:** 5 PDFs · ~75 páginas equivalentes · branding limpo (sem valores monetários, sem Microsoft confidential — conforme NFR-REPORT-011).

## 🌐 Versão EN (mesmo cliente, locale en)

A subpasta [`en/`](en/) tem os mesmos 5 PDFs renderizados em inglês (mudando apenas `respostas.json::metadata.language` para `"en"`).

## 📦 Arquivos auxiliares (intermediários do pipeline)

### Outputs do assessment principal

| Arquivo | Origem | Para que serve |
|---|---|---|
| **[scores.json](scores.json)** | `/calcular-scores` | Scores brutos: overall, 3 pillars, 28 capabilities |
| **[gaps.json](gaps.json)** | `/gap-analysis` | 10 gaps ordenados por prioridade (3 P0, 0 P1, 1 P2, 6 P3) |
| **[recomendacoes.json](recomendacoes.json)** | `/recomendar-estrategias` | 6 estratégias rankeadas + tecnologias |
| **[payload.json](payload.json)** | `/gerar-relatorio` | Payload completo enviado ao Jinja2 (debug + customização) |
| **[pontuacao-preenchida-2026-05-08.xlsx](pontuacao-preenchida-2026-05-08.xlsx)** | `/preencher-planilha` | Planilha auditável com SUMPRODUCT |
| **[import-log-2026-05-08.md](import-log-2026-05-08.md)** | `/importar-respostas-excel` | Log da importação (ilustrativo) |

### ⭐ Outputs do Developer Survey (anônimo)

| Arquivo | Origem | Para que serve |
|---|---|---|
| **[insights-developer-survey-EXEMPLO.md](insights-developer-survey-EXEMPLO.md)** | `/insights-developer-survey` | Relatório completo PT-BR de insights (12 seções, ~8 KB). Gerado a partir dos 5 mocks do `survey-devs/respostas-mock-devs.json` |
| **[maturidade-developer-survey-EXEMPLO.json](maturidade-developer-survey-EXEMPLO.json)** | `/insights-developer-survey` | Maturidade calculada por rubrica determinística L0-L4 nas 7 dimensões D2-D8 |

### ⭐ Outputs do Learning & Growth Survey (identificado)

| Arquivo | Origem | Para que serve |
|---|---|---|
| **[plano-capacitacao-EXEMPLO.md](plano-capacitacao-EXEMPLO.md)** | `/plano-capacitacao` | Plano de capacitação com top 10 tópicos (inscritos pré-validados por nome+email), Champions Network, mentor pairs, calendário 90 dias |
| **[implementation-guide-inputs-EXEMPLO.json](implementation-guide-inputs-EXEMPLO.json)** | `/wizard-implementacao` Mode D | Auto-fill que extrai 6 dos 9 inputs do wizard direto do plano de capacitação |

## 🧬 Como esses PDFs foram gerados (algoritmo do `gerar-relatorio`)

```
respostas.json.example          (input do cliente — 46 respostas mockadas)
    ↓
/calcular-scores  →  saida/scores.json
    ↓
/gap-analysis     →  saida/gaps.json
    ↓
/recomendar-estrategias  →  saida/recomendacoes.json
    ↓
/gerar-relatorio invoca relatorios/scripts/build_payload_and_render.py:
  ├─ Carrega relatorios/sample_payload.json (estrutura completa, ~28 caps com narrativa rica)
  ├─ SOBRESCREVE só campos que temos dados:
  │   • organization                    ← respostas::metadata
  │   • scores.overall.weighted_avg     ← scores.json
  │   • scores.pillars[].weighted_avg   ← scores.json
  │   • capabilities[].current_score    ← scores.json (matched by id)
  │   • gap_analysis[]                  ← gaps.json (rebuilt structure)
  │   • implementation_guide_inputs.*   ← implementation-guide-inputs.json (se existir)
  ├─ MANTÉM placeholders profissionais do sample para campos sem dados:
  │   • capabilities[].scoring_rationale, h1_initiatives, evidence_collected
  │   • technology_resources_per_pillar
  │   • risks_per_pillar, success_metrics_per_pillar, next_steps_per_pillar
  │   • horizons (narrative)
  │   • executive_steering_committee, RACI, comm/training plan (se wizard não rodou)
  └─ Renderiza via render_reports.py:
      Jinja2 + i18n (pt-br/en/es) + WeasyPrint → 5 PDFs
```

## 🎯 Resultados do Cliente Exemplo S.A.

### Maturidade global

- **Overall:** **1.99** (L2 — Definido)
- **Threshold:** OK (46/158 respondidas — perfil enxuto realista)
- **Cobertura por pillar:** P1 = 13/53 · P2 = 18/59 · P3 = 15/46

### Por pillar

| Pillar | Score | Rótulo | Forte/Fraco |
|---|---|---|---|
| **P1** Produtividade | **2.69** | L3 — Gerenciado | 💪 Copilot bem adotado |
| **P2** DevOps | **1.52** | L2 — Definido | ⚠️ DevSecOps fraco |
| **P3** Plataforma | **1.92** | L2 — Definido | ⚠️ Aplicações Agênticas fracas |

### Top 3 gaps P0 (críticos)

1. **P3-C5** Aplicações Agênticas — gap 3.17 → priority 3.17 → estratégia **S6**
2. **P2-C4** DevSecOps — gap 2.75 → priority 3.30 → estratégia **S7**
3. **P2-C10** Supply Chain Security — gap 2.33 → priority 2.57 → estratégia **S7**

### Top 3 estratégias recomendadas

1. **S7** Security & Governance — priority cumulativa **5.87** (2 capabilities P0)
2. **S6** Agentic Activation — priority cumulativa **3.92** (2 capabilities P0)
3. **S5** GitHub Copilot Acceleration — priority cumulativa **3.01** (4 capabilities)

### Estratégias sem gaps relevantes

- S1 GitHub Migration · S3 App Modernization · S4 AI Applications

## 🧪 Como reproduzir (com seus dados ou mockados)

```bash
# Usar dados mockados (mesmos PDFs desta pasta)
cp respostas.json.example respostas.json

# OU usar seus dados reais (preencher manualmente)
# editar respostas.json

# Pipeline completo
/pipeline-completo
# (ou os 5 comandos individuais — ver README.md raiz)

# Outputs vão em saida/ — devem ser idênticos aos desta pasta
```

## ⚠️ Limitações conhecidas (e como contornar)

Algumas seções dos PDFs **mantém placeholders do sample_payload.json** (Acme Insurance Group) para campos onde não temos dados estruturados do cliente. Especificamente:

- `executive_steering_committee` (5 nomes do Acme — Maria Santos, James Carter…)
- `tpo`, `raci_matrix`, `communication_plan`, `training_plan`, `adkar_notes`
- `quick_wins_w1_4` / `w5_8` / `w9_12`
- Por capability: `scoring_rationale`, `h1_initiatives`, `evidence_collected`, `h2_key_enabler`, narrativa de horizons
- `technology_resources_per_pillar` detalhado (tabelas H1/H2/H3 por pillar)
- `risks_per_pillar` / `success_metrics_per_pillar` / `next_steps_per_pillar`

### Como personalizar

**Para Implementation Guide (Parte 4):**
```
/wizard-implementacao   # 9 steps preenchem tudo da Parte 4
/gerar-relatorio        # re-renderiza com dados reais
```

**Para narrativa per capability (scoring_rationale, h1_initiatives etc.):**
```bash
# Editar manualmente saida/payload.json (substituir placeholders Acme)
code saida/payload.json

# Re-renderizar (pula a etapa de merge)
python3 relatorios/scripts/render_reports.py --payload saida/payload.json --out saida
```

---

**Renderizador:** WeasyPrint 68.1 + Jinja2 · **Templates:** mesmos da plataforma de produção (`app/src/report-service/templates/`) · **Data:** 2026-05-08
