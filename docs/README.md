# `docs/` — Mini-site (GitHub Pages)

📖 **Navegação:** [🏠 Índice](../README.md)

Site estático que apresenta o kit. O conteúdo da landing agora é centralizado em [`content.json`](content.json) e renderizado por [`app.js`](app.js), com três rotas públicas:

| Rota | Idioma | Shell |
| --- | --- | --- |
| `/` | PT-BR | [`index.html`](index.html) |
| `/en/` | English | [`en/index.html`](en/index.html) |
| `/es/` | Español | [`es/index.html`](es/index.html) |

## URL pública

```text
https://paulanunes85.github.io/ai-maturity-client-kit/
```

## Arquitetura

| Arquivo | Propósito |
| --- | --- |
| [`content.json`](content.json) | Fonte única dos textos PT-BR, EN e ES, incluindo hero, pipeline, cards, FAQ, skills e downloads |
| [`app.js`](app.js) | Renderer estático: carrega o JSON, seleciona idioma pela rota e monta a página |
| [`index.html`](index.html) | Shell PT-BR com autodetecção de idioma do navegador |
| [`en/index.html`](en/index.html) | Shell EN |
| [`es/index.html`](es/index.html) | Shell ES |
| [`styles.css`](styles.css) | CSS compartilhado com tokens paulasilva-ms |

## Idioma automático

A rota `/` usa o idioma do navegador para redirecionar automaticamente para `/en/` ou `/es/` quando apropriado. PT-BR continua sendo o padrão.

O seletor PT · EN · ES grava a escolha em `localStorage`, então visitas futuras respeitam a última seleção.

## Como editar conteúdo

Edite apenas [`content.json`](content.json) para alterar textos e traduções. Evite editar manualmente os três HTMLs, eles são apenas shells mínimos.

Valide o JSON antes de publicar:

```bash
python3 -m json.tool docs/content.json >/dev/null
```

## Preview local

Como o site carrega `content.json` via `fetch`, use um servidor local:

```bash
cd docs
python3 -m http.server 8000
# abrir http://localhost:8000
```

Abrir `index.html` diretamente via `file://` não é recomendado, porque navegadores bloqueiam `fetch()` de arquivos locais.

## Downloads públicos com repo privado

Sim, é possível manter o repositório privado e o site público, desde que o GitHub Pages esteja habilitado como público no plano/organização.

O detalhe importante: assets de GitHub Releases em repositório privado exigem autenticação. Por isso o workflow de Pages gera os ZIPs e os publica dentro do próprio artefato do site:

```text
https://paulanunes85.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-pt.zip
https://paulanunes85.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-en.zip
https://paulanunes85.github.io/ai-maturity-client-kit/downloads/ai-maturity-kit-es.zip
```

Esses links continuam públicos junto com o site, mesmo se o repositório voltar a ser privado.

## Deploy

O workflow [`.github/workflows/pages.yml`](../.github/workflows/pages.yml):

1. Faz checkout do repositório.
2. Gera os três ZIPs em `docs/downloads/`.
3. Faz upload da pasta `docs/` como artefato do GitHub Pages.
4. Publica o site.

Qualquer push que toque `docs/**` ou o workflow de Pages dispara novo deploy.

## Branding

Tokens MS 4 cores aplicados via CSS variables:

- `--c-blue: #00A4EF`
- `--c-green: #7FBA00`
- `--c-yellow: #FFB900`
- `--c-red: #F25022`

Logo SVG inline, Inter + JetBrains Mono via Google Fonts, e dark mode automático via `prefers-color-scheme`.
