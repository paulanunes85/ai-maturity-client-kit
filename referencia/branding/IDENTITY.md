# Identidade visual paulasilva-ms (Microsoft)

Identidade aplicada aos artefatos visuais deste kit. Forka o design system [paulasilva-ms](../../../../.github/skills/paulasilva-ms/) v1.7.0.

## Strings canônicas (use exatamente)

```text
Author name:     Paula Silva
Role (formal):   Software Global Black Belt
Role (full):     Paula Silva, Software Global Black Belt
Meta-bar form:   Paula Silva | Software Global Black Belt
Contact:         paulasilva@microsoft.com
Tagline (EN):    Building the future of software development with AI and Agentic DevOps
```

A função é **Software Global Black Belt** (não "GBB Americas", não "Microsoft Global Black Belt", não abreviado). Não tem organização, não tem região.

O contato é **email apenas**. Sem LinkedIn público, sem GitHub, sem website em material Microsoft.

A tagline é **inglês apenas** em material MS. Não traduzir.

## Paleta de logo (4 cores Microsoft oficiais)

| Token | Hex | Uso |
|---|---|---|
| `--c-blue-500` | `#00A4EF` | Accent default, botões primários, links |
| `--c-green-500` | `#7FBA00` | Sucesso, confirmação, métricas positivas |
| `--c-yellow-500` | `#FFB900` | Atenção, destaque |
| `--c-red-500` | `#F25022` | Erro, gap crítico, alerta |

Cada cor tem variantes `-50` (muito claro, fundo), `-100` (claro), `-700` (escuro, texto). Veja [`tokens-paulasilva-ms.css`](tokens-paulasilva-ms.css).

## Logo SVG (inline, nunca link externo)

22px (chrome bar):

```html
<svg viewBox="0 0 1914 1062" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="paulasilva" style="width:22px;height:auto;flex-shrink:0;">
  <title>paulasilva</title>
  <path fill="#F25022" d="M532 131 L36 462 L13 497 L13 560 L23 582 L48 604 L521 923 L539 926 L539 699 L547 680 L314 530 L527 395 L551 371 L558 347 L558 155 L547 135 Z"/>
  <path fill="#7FBA00" d="M551 681 L542 693 L540 700 L540 917 L546 930 L558 940 L571 943 L778 943 L788 941 L798 935 L809 910 L809 702 L807 694 L799 682 L784 674 L566 674 Z"/>
  <path fill="#FFB900" d="M1390 16 L1208 13 L1184 23 L1171 38 L768 1009 L768 1026 L778 1038 L957 1042 L975 1037 L995 1017 L1346 179 L1349 145 L1367 129 L1401 47 L1402 31 Z"/>
  <path fill="#00A4EF" d="M1369 131 L1350 149 L1349 355 L1354 369 L1385 399 L1592 528 L1373 667 L1354 688 L1349 703 L1349 907 L1361 924 L1377 926 L1871 595 L1893 563 L1894 501 L1885 477 L1863 456 L1398 142 Z"/>
</svg>
```

## Chrome bar (topo de qualquer HTML standalone)

```html
<div class="deck-brand">
  <!-- 22px logo SVG aqui -->
  <span class="deck-brand__text">Paula Silva | Software Global Black Belt</span>
</div>
```

```css
.deck-brand {
  position: fixed; top: 16px; left: 32px; z-index: 50;
  display: flex; align-items: center; gap: 12px;
}
.deck-brand__text {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink-3);
}
```

## Tipografia

- **Sans:** Inter (carregar de Google Fonts ou CDN)
- **Mono:** JetBrains Mono (carregar de Google Fonts)

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

## Forbidden patterns (revisar antes de publicar)

- ❌ Em-dashes (`—`). Use vírgula, ponto, dois-pontos ou ponto-e-vírgula.
- ❌ En-dashes (`–`) em ranges. Use hífen com espaços (`08:00 - 12:00`) ou "to" / "a".
- ❌ Vocabulário banido: ver [`VOICE.md`](VOICE.md).
- ❌ Cores fora da paleta MS sem token explícito.
- ❌ Logo com cores diferentes das 4 oficiais (`#F25022 / #7FBA00 / #FFB900 / #00A4EF`).
- ❌ "Microsoft GBB Americas", "MS Global Black Belt", abreviações de role.
- ❌ Adicionar LinkedIn, GitHub, website ao contato. Email apenas.

## Como usar nos artefatos do kit

1. Os 4 HTMLs interativos do kit já carregam `tokens-paulasilva-ms.css`:
   - [`../calculadora-pontuacao.html`](../calculadora-pontuacao.html)
   - [`../../formularios/P1-produtividade-do-desenvolvedor.html`](../../formularios/P1-produtividade-do-desenvolvedor.html)
   - [`../../formularios/P2-ciclo-de-vida-devops.html`](../../formularios/P2-ciclo-de-vida-devops.html)
   - [`../../formularios/P3-plataforma-de-aplicações.html`](../../formularios/P3-plataforma-de-aplicações.html)
   - [`../../wizard/implementation-guide-wizard.html`](../../wizard/implementation-guide-wizard.html)

2. Os PDFs Jinja2 (`relatorios/templates/*.html.j2` + `_print.css`) **mantêm a paleta oficial da plataforma** (não foram alterados). Branding MS aplica-se aos HTMLs standalone do kit, não aos PDFs production.

3. Para criar novo HTML alinhado:
   - Carregue Inter + JetBrains Mono via Google Fonts
   - `<link rel="stylesheet" href="referencia/branding/tokens-paulasilva-ms.css">` (relativo)
   - Use tokens (`var(--c-blue-500)`, `var(--accent)`, `var(--ink)`, etc.)
   - Adicione chrome bar com logo + meta-text

## Referência completa

Para detalhe completo do design system (showcase, deck patterns, simulações, layouts), veja a skill canônica:

- [`/Users/paulasilva/Documents/ai-maturuty-client-platform/.github/skills/paulasilva-ms/`](../../../../.github/skills/paulasilva-ms/)
- `references/identity.md` — strings canônicas + logo
- `references/voice.md` — vocabulário banido + tom
- `references/components.md` — componentes (cards, badges, tables)
- `references/playbook.md` — pattern de playbook multi-página
- `assets/showcase.html` — visual reference de todos os patterns
