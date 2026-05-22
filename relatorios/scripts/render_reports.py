#!/usr/bin/env python3
"""Render the 5 client-ready PDF reports for AI Maturity Assessment.

Renders Jinja2 templates → HTML → WeasyPrint → PDF.

Inputs:
  - templates/  (5 .html.j2 files + _print.css)
  - i18n/       (en.json, es.json, pt-br.json)
  - <payload>   (default: sample_payload.json — adapt to your data)

Outputs (in --out dir, default ../../referencia/exemplo-saida/):
  - score_justification.pdf
  - roadmap_part_pillar_p1.pdf
  - roadmap_part_pillar_p2.pdf
  - roadmap_part_pillar_p3.pdf
  - roadmap_part4.pdf

Usage:
  python3 render_reports.py                            # uses sample_payload.json
  python3 render_reports.py --payload other.json       # custom payload
  python3 render_reports.py --out /path/to/output      # custom output
  python3 render_reports.py --locale pt-br             # render PT-BR
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from weasyprint import HTML, CSS

ROOT = Path(__file__).resolve().parent.parent  # kit-cliente/relatorios/
TEMPLATES = ROOT / "templates"
I18N = ROOT / "i18n"


def load_locale(locale: str) -> dict[str, str]:
    return json.loads((I18N / f"{locale}.json").read_text(encoding="utf-8"))


def make_t(strings: dict[str, str]):
    pat = re.compile(r"\{(\w+)\}")
    def t(key: str, **kw) -> str:
        s = strings.get(key, f"⟨{key}⟩")
        return pat.sub(lambda m: str(kw.get(m.group(1), m.group(0))), s) if kw else s
    return t


def render(template_name: str, payload: dict, extra_ctx: dict | None, out_dir: Path, label: str) -> Path:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=True,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    locale = payload.get("locale", "en")
    strings = load_locale(locale)
    t = make_t(strings)
    env.globals["t"] = t
    env.filters["t"] = t

    template = env.get_template(template_name)
    ctx = {**payload, **(extra_ctx or {})}
    html_str = template.render(**ctx)

    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / f"{label}.html"
    html_path.write_text(html_str, encoding="utf-8")

    css_path = TEMPLATES / "_print.css"
    pdf_bytes = HTML(string=html_str, base_url=str(TEMPLATES)).write_pdf(
        stylesheets=[CSS(filename=str(css_path))]
    )
    pdf_path = out_dir / f"{label}.pdf"
    pdf_path.write_bytes(pdf_bytes)
    return pdf_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--payload", default=str(ROOT / "sample_payload.json"))
    ap.add_argument("--out", default=str(ROOT.parent / "referencia/exemplo-saida"))
    ap.add_argument("--locale", default=None, help="override payload.locale")
    args = ap.parse_args()

    payload_path = Path(args.payload)
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    if args.locale:
        payload["locale"] = args.locale

    out_dir = Path(args.out)

    print(f"Payload:  {payload_path}  ({payload_path.stat().st_size:,} bytes)")
    print(f"Locale:   {payload.get('locale', 'en')}")
    print(f"Org:      {payload.get('organization', {}).get('name', '?')}")
    print(f"Out dir:  {out_dir}")
    print()

    targets = [
        ("score_justification.html.j2", {}, "score_justification"),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P1"}, "roadmap_part_pillar_p1"),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P2"}, "roadmap_part_pillar_p2"),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P3"}, "roadmap_part_pillar_p3"),
        ("roadmap_part4.html.j2", {}, "roadmap_part4"),
    ]

    ok = True
    for tmpl, extra, label in targets:
        try:
            pdf_path = render(tmpl, payload, extra, out_dir, label)
            print(f"  ✓ {pdf_path.name}: {pdf_path.stat().st_size:,} bytes")
        except Exception as e:
            print(f"  ✗ {label}: {type(e).__name__}: {e}")
            ok = False

    print()
    if ok:
        print(f"✓ Todos os 5 PDFs gerados em {out_dir}")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
