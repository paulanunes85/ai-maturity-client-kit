# Brand Voice (paulasilva-ms)

Voz unificada do design system. Todo conteúdo escrito sob identidade Microsoft segue estas regras.

## Três pilares

1. **Pedagógico sem condescendência.** Explique como se ensinasse engenheiro inteligente que não viu este tópico específico. Não fale como se fosse iniciante precisando de hand-holding.
2. **Provocativo por dado, não por hype.** Faça afirmações que desafiam suposições, mas embase cada afirmação com número, citação ou cenário concreto. Nunca use superlativo vago.
3. **Pessoal com cicatrizes nomeadas.** Referencie modos de falha reais que você viu. Não fale em abstração quando pode falar de experiência.

## Vocabulário banido (nunca use em nenhum output)

| Banido | Por que | Alternativa |
|---|---|---|
| `AI-powered` | Filler de marketing | Descreva o que a IA faz |
| `revolutionary` | Auto-elogio sem prova | Descreva a mudança concreta |
| `game-changer` | Clichê | Diga o que mudou e por quê importa |
| `next-generation` | Sinal vazio | Dê a versão ou a nova capability |
| `world-class` | Auto-elogio | Cite o benchmark |
| `best-in-class` | Auto-elogio | Cite o benchmark |
| `cutting-edge` | Vago | Nomeie a técnica específica |
| `this changes everything` | Hipérbole | Liste o que muda e o que não muda |
| `the future is here` | Hype | Descreva o estado presente |
| `obviously` | Implica que leitor é burro | Apenas afirme |
| `as everyone knows` | Idem | Apenas afirme |
| `synergy` | Vazio | Descreva a interação específica |
| `leverage` (verbo) | Filler | `use`, `apply`, `build on` |
| `circle back` | Filler corporativo | `revisit`, `come back to` |
| `low-hanging fruit` | Clichê | Nomeie a oportunidade |
| `I am no expert but...` | Falsa modéstia | Apenas afirme |
| `just sharing my humble thoughts` | Idem | Idem |

## Pontuação

- ❌ **Sem em-dashes** (`—`). Use vírgula, ponto, dois-pontos ou ponto-e-vírgula.
- ❌ **Sem en-dashes** (`–`) em ranges. Use hífen com espaços (`08:00 - 12:00`) ou "to" / "a".
- ❌ **Sem espaço duplo** após ponto. Espaço simples.
- ✅ **Vírgula serial** (Oxford). "Specs, agents, and humans in the loop."

## Tom por audiência

| Audiência | Tom | Exemplo de abertura |
|---|---|---|
| Executiva (board, VP) | Conciso, números primeiro, ações claras | "3 capabilities em P0. Ação imediata: investir 8 FTE em S7 (Security)." |
| Tech Lead / Arquiteto | Trade-offs explícitos, citações técnicas | "Foundry Agent Service GA traz MCP nativo. Trade-off: vendor lock-in vs. integração rápida." |
| Desenvolvedor | Concreto, código quando útil, jargão OK | "Custom agent em `.github/agents/*.agent.md`. Frontmatter `tools:`, `handoffs:`. Ver paulasilva-ms showcase." |
| Cliente externo | Pedagógico, sem siglas internas | "AI Maturity Assessment é uma avaliação em 158 perguntas que mede 28 capabilities organizacionais." |

## Padrões de citação

- Microsoft-first: cite docs.microsoft.com, learn.microsoft.com, github.blog antes de outras fontes.
- Sempre dê a URL completa.
- Cite com data quando relevante (ex.: "GA setembro 2025").
- Para conceitos do paulasilva-ms DS, referencie o caminho da skill (`.github/skills/paulasilva-ms/references/X.md`).
