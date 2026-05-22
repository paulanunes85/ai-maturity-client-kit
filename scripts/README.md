# `scripts/` — Utilitários do kit

📖 **Navegação:** [🏠 Índice](../README.md)

Scripts auxiliares de manutenção e validação do kit (não invocados pelo cliente final no fluxo normal — são para contribuidores).

## Conteúdo

| Arquivo | Propósito |
|---|---|
| [`smoke_test.py`](smoke_test.py) | Teste end-to-end automatizado: copia `respostas.json.example` → roda `build_payload_and_render.py --no-render` → valida shape do `payload.json` → restaura workspace. Stdlib puro (sem pytest). |

## Como usar

```bash
make smoke          # assessment only
make smoke-cross    # + cross-survey enrichment (developer + learning surveys)

# ou direto:
python3 scripts/smoke_test.py
python3 scripts/smoke_test.py --with-cross-survey
```

> [!TIP]
> Rode `make smoke` antes de abrir PR que toca o pipeline (`relatorios/scripts/*.py` ou qualquer SKILL.md em `.github/skills/`).
