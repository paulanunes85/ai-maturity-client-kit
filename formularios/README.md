# `formularios/` — HTMLs visuais das 158 questões (referência offline)

Esta pasta contém **3 arquivos HTML standalone** (um por pillar) com todas as 158 questões do assessment formatadas como aparecem na plataforma web. Útil para **consultar visualmente** durante o preenchimento do `respostas.json` ou para apresentar/discutir as questões em workshops.

## Arquivos

| Arquivo | Pillar | Capabilities | Questões |
|---|---|---|---|
| **[P1-produtividade-do-desenvolvedor.html](P1-produtividade-do-desenvolvedor.html)** | P1 — Produtividade do Desenvolvedor | 9 | 53 |
| **[P2-ciclo-de-vida-devops.html](P2-ciclo-de-vida-devops.html)** | P2 — Ciclo de Vida DevOps | 10 | 59 |
| **[P3-plataforma-de-aplicações.html](P3-plataforma-de-aplicações.html)** | P3 — Plataforma de Aplicações | 9 | 46 |

## Como usar

1. Duplo clique em qualquer arquivo `.html` para abrir no navegador (não precisa servidor)
2. Cada questão mostra:
   - **ID** (`P1-C1-Q1`, etc.) — use para mapear no `respostas.json`
   - **Texto** da pergunta em PT-BR
   - **5 opções de nível** (L0 a L4) com descrição e cor
   - **KPI** sugerido (em inglês — termo técnico universal)
   - **Contexto** (o que mede / por que importa)
   - **Evidências** esperadas por nível

3. Para preencher `respostas.json`:
   - Identifique o ID da questão no HTML
   - Vá no `respostas.json` (raiz do kit) e procure esse ID
   - Marque o `level` (0-4) e adicione `evidence` (texto descritivo)

## Observação importante

Estes HTMLs são **visualização offline** — não capturam respostas. Para coleta interativa (clicar e salvar), use:
- **Microsoft Forms** (ver `coleta/INSTRUCOES-FORMS.md`)
- **Wizard React** quando a plataforma web estiver pronta
- **Edição manual** do `respostas.json` (formato JSON estruturado)

## Documentação técnica das questões

Para descrição detalhada das 158 questões com KPI/contexto/evidências por nível, veja os MD em [`../referencia/`](../referencia/):
- `referencia/P1-produtividade-do-desenvolvedor.md`
- `referencia/P2-ciclo-de-vida-devops.md`
- `referencia/P3-plataforma-de-aplicações.md`
