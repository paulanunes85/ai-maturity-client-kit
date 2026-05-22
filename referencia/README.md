# `referencia/` — Documentação técnica e exemplos

Esta pasta contém **documentação read-only**: algoritmo oficial, descrição das 158 questões, planilha auditável, calculadora interativa e exemplos finais de output.

## Arquivos

### 📊 Documentação do algoritmo de scoring

| Arquivo | O que é |
|---|---|
| **[pontuacao-e-calculo.md](pontuacao-e-calculo.md)** | Referência oficial em PT-BR — todas as fórmulas (capability/pillar/overall), threshold (25/40), multi-respondente, gap analysis (P0-P3), mapping rótulos, edge cases, glossário. **Espelha 1:1** o código `app/backend/src/scoring.rs` |
| **[pontuacao-e-calculo.xlsx](pontuacao-e-calculo.xlsx)** | Planilha Excel auditável com 5 abas: Como ler, Exemplo P1, Exemplo P2, Exemplo P3, Resumo. Fórmulas SUMPRODUCT visíveis célula por célula |
| **[calculadora-pontuacao.html](calculadora-pontuacao.html)** | Calculadora interativa standalone (Tailwind + JavaScript) — 17 questões reais (1 capability por pillar), edite níveis e pesos, vê scores recalculando ao vivo. Abre no browser |

### 📚 Documentação das 158 questões

| Arquivo | Conteúdo |
|---|---|
| **[P1-produtividade-do-desenvolvedor.md](P1-produtividade-do-desenvolvedor.md)** | 53 questões do P1 com: KPI, contexto (o que mede / por que importa), descrição completa de cada nível L0-L4 com evidências esperadas |
| **[P2-ciclo-de-vida-devops.md](P2-ciclo-de-vida-devops.md)** | 59 questões do P2 (mesmo formato) |
| **[P3-plataforma-de-aplicações.md](P3-plataforma-de-aplicações.md)** | 46 questões do P3 (mesmo formato) |

### 🎯 Exemplos finais (output do pipeline)

| Pasta | O que é |
|---|---|
| **[exemplo-saida/](exemplo-saida/)** | **5 PDFs reais** + JSONs intermediários gerados a partir de `respostas.json.example` (Cliente Exemplo S.A.). Inclui versão PT-BR (raiz) e EN (`exemplo-saida/en/`). É o **preview exato** do que o cliente vai gerar. Tem README detalhado dentro. |

## Quando usar cada arquivo

- **Quer entender como os scores são calculados?** → `pontuacao-e-calculo.md`
- **Cliente perguntou "como esse score saiu?" e quer ver fórmula?** → abra `pontuacao-e-calculo.xlsx` no Excel
- **Quer brincar com diferentes respostas e ver scores ao vivo?** → abra `calculadora-pontuacao.html` no browser
- **Vai responder uma questão e tem dúvida sobre o que cada nível significa?** → consulte `P1/P2/P3-…md` (mais detalhe que os HTMLs visuais em `formularios/`)
- **Quer ver "como vai ficar o relatório final"?** → abra os PDFs em `exemplo-saida/`

## ⚠️ Importante

**Não modifique** nenhum arquivo desta pasta — eles são **read-only** (referência técnica que deve permanecer canônica). Se precisar customizar para seu cliente, copie para outro lugar e edite a cópia.

A única exceção: a subpasta `exemplo-saida/` pode ser regenerada rodando o pipeline com `respostas.json.example`.
