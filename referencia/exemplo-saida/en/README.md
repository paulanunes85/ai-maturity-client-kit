# `referencia/exemplo-saida/en/`

📖 **Navegação:** [🏠 Índice](../../../README.md) · [« Exemplo-saída](../README.md)

Versão **em inglês** dos 5 PDFs de referência gerados a partir de `respostas.json.example` (Cliente Exemplo S.A., locale forçado para `en`).

## Conteúdo

| Arquivo | Descrição |
|---|---|
| `score_justification.pdf` | Score Justification — Acme/Cliente Exemplo |
| `roadmap_part_pillar_p1.pdf` | Productivity pillar deep-dive |
| `roadmap_part_pillar_p2.pdf` | DevOps pillar deep-dive |
| `roadmap_part_pillar_p3.pdf` | Platform pillar deep-dive |
| `roadmap_part4.pdf` | Implementation Guide consolidated |

## Quando usar

- Mostrar ao cliente final como **vão ficar os PDFs em inglês** (se ele optar por `language: "en"` no `respostas.json::metadata`)
- Validar visualmente que o template `roadmap_part_pillar.html.j2` lida bem com strings mais longas (inglês tende a expandir vs. PT-BR)

> [!NOTE]
> Os PDFs em PT-BR (default) ficam no diretório pai: [`../`](../).

## Como regerar

```bash
# editar respostas.json.example, mudar "language": "en"
cp respostas.json.example respostas.json
python3 relatorios/scripts/build_payload_and_render.py
# mover saida/*.pdf para referencia/exemplo-saida/en/
```
