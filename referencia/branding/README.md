# `referencia/branding/` — Identidade visual paulasilva-ms (Microsoft)

Esta pasta contém os assets de branding aplicados aos artefatos visuais standalone deste kit (HTMLs interativos). Forka o design system canônico [paulasilva-ms v1.7.0](../../../../.github/skills/paulasilva-ms/).

## Arquivos

| Arquivo | Para que serve |
|---|---|
| **[tokens-paulasilva-ms.css](tokens-paulasilva-ms.css)** | Design tokens canônicos: paleta Microsoft 4 cores (#F25022, #7FBA00, #FFB900, #00A4EF), neutros, dark mode, accent classes (.acc-blue, .acc-green, .acc-yellow, .acc-red), tipografia (Inter + JetBrains Mono) |
| **[IDENTITY.md](IDENTITY.md)** | Strings canônicas (nome, role, contato), logo SVG inline, chrome bar, padrões obrigatórios |
| **[VOICE.md](VOICE.md)** | Pilares de voz, vocabulário banido, regras de pontuação, tom por audiência |

## Onde o branding está aplicado

### ✅ Aplicado nos HTMLs standalone do kit

Os seguintes arquivos carregam `tokens-paulasilva-ms.css` e mostram o chrome bar:

- [`../calculadora-pontuacao.html`](../calculadora-pontuacao.html) — calculadora interativa
- [`../../formularios/P1-produtividade-do-desenvolvedor.html`](../../formularios/P1-produtividade-do-desenvolvedor.html)
- [`../../formularios/P2-ciclo-de-vida-devops.html`](../../formularios/P2-ciclo-de-vida-devops.html)
- [`../../formularios/P3-plataforma-de-aplicações.html`](../../formularios/P3-plataforma-de-aplicações.html)
- [`../../wizard/implementation-guide-wizard.html`](../../wizard/implementation-guide-wizard.html)

### ❌ NÃO aplicado nos PDFs Jinja2

Os 5 PDFs production-quality (`relatorios/templates/*.html.j2` + `_print.css`) **mantêm a paleta oficial da plataforma** (espelho fiel de `app/src/report-service/templates/`). Branding paulasilva-ms aplica-se aos HTMLs do kit, não aos PDFs.

Razão: os PDFs são entregáveis production que precisam ser idênticos à futura plataforma web. Modificar o CSS deles quebraria essa paridade.

## Atribuição (todo HTML novo deste kit deve ter)

```
Paula Silva | Software Global Black Belt
paulasilva@microsoft.com
```

Sem LinkedIn, sem GitHub, sem website. Email apenas.

## Como criar novo HTML alinhado

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../referencia/branding/tokens-paulasilva-ms.css">
  <style>
    body { font-family: var(--font-sans); color: var(--ink); background: var(--bg); }
    h1 { color: var(--accent-ink); }
    .card { background: var(--paper); border: 1px solid var(--rule); }
  </style>
</head>
<body>
  <div class="deck-brand">
    <!-- 22px logo SVG (copiar de IDENTITY.md) -->
    <span class="deck-brand__text">Paula Silva | Software Global Black Belt</span>
  </div>
  <!-- conteúdo aqui -->
</body>
</html>
```

## Skill canônica completa

Para showcase visual completo, deck patterns, simulações, layouts de playbook multi-página:

- Caminho: [`/Users/paulasilva/Documents/ai-maturuty-client-platform/.github/skills/paulasilva-ms/`](../../../../.github/skills/paulasilva-ms/)
- `assets/showcase.html` abre no browser e mostra todos os componentes
- `references/components.md` documenta cards, badges, tables, buttons
- `references/playbook.md` documenta pattern de playbook multi-página
- `references/pdf-generation.md` documenta deck → PDF via Playwright

Quando precisar criar novo deck, playbook ou material formal Microsoft fora deste kit, invoque a skill `paulasilva-ms` no Copilot Chat.
