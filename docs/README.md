# `docs/` — Mini-site (GitHub Pages)

📖 **Navegação:** [🏠 Índice](../README.md)

Site estático single-page que apresenta o kit. Publicado automaticamente via GitHub Pages quando há push em `main` que toca `docs/`.

## URL pública (após ativação)

```
https://paulanunes85.github.io/ai-maturity-client-kit/
```

## Conteúdo

| Arquivo | Propósito |
|---|---|
| [`index.html`](index.html) | Landing single-page: hero, pipeline, 3 surveys, quick start, 12 skills, FAQ, download |
| [`styles.css`](styles.css) | CSS com tokens paulasilva-ms (paleta MS 4 cores, Inter + JetBrains Mono via Google Fonts) |

## Como ativar GitHub Pages

> [!IMPORTANT]
> Ativação manual única no repo. Depois disso o deploy é automático.

1. Acesse https://github.com/paulanunes85/ai-maturity-client-kit/settings/pages
2. **Source:** selecione **GitHub Actions** (não "Deploy from a branch")
3. Faça push em qualquer arquivo de `docs/` → workflow [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) roda automaticamente
4. Site fica disponível em `https://paulanunes85.github.io/ai-maturity-client-kit/` em ~2 minutos

## Como customizar localmente

Abra `index.html` direto no navegador (não precisa servidor) — o CSS e o Google Fonts carregam via CDN.

Para preview em servidor local:
```bash
cd docs && python3 -m http.server 8000
# abrir http://localhost:8000
```

## Branding

Tokens MS 4 cores aplicados via CSS variables:
- `--c-blue: #00A4EF` (primário, links)
- `--c-green: #7FBA00` (sucesso)
- `--c-yellow: #FFB900` (atenção)
- `--c-red: #F25022` (alerta)

Logo SVG inline (sem dependência externa). Inter + JetBrains Mono via Google Fonts. Dark mode automático via `prefers-color-scheme`.

## Botão de download

O CTA "⬇ Baixar ZIP (main)" aponta para a URL nativa do GitHub:
```
https://github.com/paulanunes85/ai-maturity-client-kit/archive/refs/heads/main.zip
```

Não requer workflow extra — o ZIP é gerado on-demand pelo próprio GitHub a partir do estado atual de `main`.
