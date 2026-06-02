# Kit AI Maturity Assessment · Edición Español

> Kit de autoservicio para ejecutar la Evaluación de Madurez en IA con GitHub Copilot.
> **3 encuestas complementarias · 5 PDFs production-quality · plan de capacitación personalizado.**

[![Open in VS Code](https://img.shields.io/badge/Abrir%20en-VS%20Code-007ACC?logo=visualstudiocode)](https://github.com/paulanunes85/ai-maturity-client-kit)
[![Sitio](https://img.shields.io/badge/sitio-paulanunes85.github.io-00A4EF)](https://paulanunes85.github.io/ai-maturity-client-kit/es/)
[![Descargar ZIP](https://img.shields.io/badge/descargar-ES%20kit.zip-7FBA00)](https://paulanunes85.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-es.zip)

---

## Qué es este kit

Un **kit autocontenido** para ejecutar una evaluación end-to-end de madurez en IA **sin depender de una plataforma web**. Incluye:

- **Framework de 158 preguntas** organizado en 3 pilares × 28 capabilities × 7 estrategias
- **3 encuestas complementarias**: Assessment organizacional + Developer Survey anónima + Learning & Growth Survey identificada
- **12 skills custom de Copilot Chat + 1 prompt + 1 agente concierge** que orquestan el pipeline completo
- **5 PDFs ejecutivos** renderizados con branding paulasilva-ms (paleta Microsoft 4 colores) — ya localizados en ES vía `relatorios/i18n/es.json`
- **Hoja Excel auditable** con fórmulas SUMPRODUCT nativas
- **Plan de capacitación** con nombres + emails de inscritos

## ⚠ Nota importante sobre idioma

El ZIP en Español sigue una separación deliberada de idioma:

1. **Los archivos de customización de Copilot se mantienen en Inglés** — `.github/copilot-instructions.md`, `.github/agents/`, `.github/prompts/` y `.github/skills/` son el runtime del agente y se comparten intencionalmente en todos los paquetes de idioma.
2. **La documentación orientada al cliente está en Español** — `README.md`, `PASO-A-PASO.md`, `INSTRUCCIONES-FORMS.md` y `PACKAGE-LANGUAGE-NOTES.md` quedan en la raíz del ZIP.
3. **Los activos runtime compartidos son neutrales al idioma** — JSONs, scripts, templates, workbooks e IDs de scoring se reutilizan. Los IDs canónicos de preguntas y algunos nombres internos permanecen en Portugués cuando el framework de scoring y el mapeo de plataforma lo requieren.
4. **Los PDFs se renderizan en Español** vía `relatorios/i18n/es.json` — define `report_lang: "es"` en `respostas.json` y los 5 PDFs salen en Español.

Si necesitas el framework JSON totalmente traducido, abre un issue: <https://github.com/paulanunes85/ai-maturity-client-kit/issues/new>

## Inicio rápido

```bash
# 1. Clona el repo
git clone https://github.com/paulanunes85/ai-maturity-client-kit.git
cd ai-maturity-client-kit

# 2. Valida prerequisitos
make smoke

# 3. Copia los datos de ejemplo y ejecuta el pipeline completo
cp respostas.json.example respostas.json

# Abre VS Code, en Copilot Chat (modo Agent):
#   @ai-maturity-assistant
# o:
#   /pipeline-completo
```

Los resultados aparecen en `saida/` (5 PDFs + scores.json + gaps.json + recomendacoes.json + Excel auditable).

## Las 3 encuestas

| Encuesta | Audiencia | Preguntas | Tiempo | Output |
| --- | --- | --- | --- | --- |
| 🅰️ **AI Maturity Assessment** | Liderazgo / org | 158 | 60-90 min | 5 PDFs ejecutivos |
| 🅱️ **Developer Survey** | Devs anónimos | 75 | 22-28 min/dev | Insights comportamentales + madurez L0-L4 por dimensión |
| 🅲 **Learning & Growth** | Devs identificados | 32 | 5-8 min/dev | Roadmap de capacitación con listas de inscritos |

Orden recomendado para consultoría seria: **B (anónimo) → C (identificado) → A (liderazgo)**. Cada encuesta informa la siguiente; el agente concierge cruza resultados automáticamente.

## Pipeline en una línea

```text
INPUT (respostas.json o Forms .xlsx)
  → /calcular-scores          (SUMPRODUCT 3 capas)
  → /gap-analysis             (prioridades P0 / P1 / P2 / P3)
  → /recomendar-estrategias   (S1 a S7 + tecnologías)
  → /wizard-implementacao     (9 inputs para PDF Parte 4)
  → /gerar-relatorio          (Jinja2 + WeasyPrint)
OUTPUT (5 PDFs + XLSX auditable)
```

## Qué está traducido en este folder

| Archivo | Estado |
| --- | --- |
| [README.md](README.md) | ✅ Traducido |
| [GUIA-PASSO-A-PASSO.md](../GUIA-PASSO-A-PASSO.md) | ✅ Traducido como `PASO-A-PASO.md` |
| [INSTRUCOES-FORMS.md](../coleta/INSTRUCOES-FORMS.md) | ✅ Traducido como `INSTRUCCIONES-FORMS.md` |
| Customizaciones Copilot bajo `.github/` | ✅ Incluidas, intencionalmente en Inglés |
| JSONs, scripts, templates y workbooks compartidos | ✅ Incluidos como activos runtime |
| PDFs de reporte | ✅ Ya en ES vía `relatorios/i18n/es.json` |

## Continuar leyendo

| ⬅ Anterior | Siguiente ➡ |
| :--- | ---: |
| [🏠 Sitio principal (multi-idioma)](https://paulanunes85.github.io/ai-maturity-client-kit/) | [📘 Paso a paso detallado](PASO-A-PASO.md) |

---

**Paula Silva** — Software Global Black Belt | [paulasilva@microsoft.com](mailto:paulasilva@microsoft.com)
*Building the future of software development with AI and Agentic DevOps*
