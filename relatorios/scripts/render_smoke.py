#!/usr/bin/env python3
"""
Smoke test harness for the Final Report templates.

Loads the sample fixture + i18n strings, renders each template through Jinja2 +
WeasyPrint, and validates the NFR-REPORT-011 content-stripping policy against
the rendered PDF text.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from weasyprint import HTML, CSS

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "templates"
I18N = ROOT / "i18n"
FIXTURES = ROOT / "fixtures"
OUT = ROOT / "rendered"
OUT.mkdir(exist_ok=True)


# ─── i18n helpers ────────────────────────────────────────────────
def load_locale(locale: str) -> dict[str, str]:
    return json.loads((I18N / f"{locale}.json").read_text())


def make_t_filter(strings: dict[str, str]):
    """Returns a `t()` template function that supports {placeholder} substitution."""
    pattern = re.compile(r"\{(\w+)\}")

    def t(key: str, **kwargs) -> str:
        s = strings.get(key, f"⟨{key}⟩")  # show missing keys clearly
        if kwargs:
            return pattern.sub(lambda m: str(kwargs.get(m.group(1), m.group(0))), s)
        return s

    return t


# ─── Renderer ────────────────────────────────────────────────────
def render(template_name: str, payload: dict[str, Any], extra_ctx: dict | None = None,
           out_label: str | None = None) -> bytes:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=True,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    locale = payload.get("locale", "en")
    strings = load_locale(locale)
    t = make_t_filter(strings)
    env.globals["t"] = t  # callable in templates
    env.filters["t"] = t  # also as filter

    template = env.get_template(template_name)
    ctx = {**payload, **(extra_ctx or {})}
    html_str = template.render(**ctx)

    # Persist rendered HTML for inspection — use the same label as PDF so
    # multiple variants (per pillar) don't overwrite each other.
    label = out_label or template_name.replace(".html.j2", "")
    html_path = OUT / f"{label}.html"
    html_path.write_text(html_str)

    css_path = TEMPLATES / "_print.css"
    pdf_bytes = HTML(string=html_str, base_url=str(TEMPLATES)).write_pdf(
        stylesheets=[CSS(filename=str(css_path))]
    )
    return pdf_bytes


# ─── Content lint per NFR-REPORT-011 ─────────────────────────────
FORBIDDEN_TOKENS = [
    r"\$\d",                               # $1, $1M, $150K — any digit after $
    r"\bUSD\b",
    r"R\$",
    r"€\d",
    r"Microsoft Confidential",
    r"Microsoft Latam GBB",
    r"paulasilva@microsoft\.com",
]


def lint_content(pdf_bytes: bytes, label: str) -> list[str]:
    """Content scan against forbidden tokens per NFR-REPORT-011.

    Scans only the rendered HTML (the source of truth for visible content).
    Scanning compressed PDF byte streams produces false positives because
    PDF object/xref tables contain arbitrary byte sequences.
    """
    html_path = OUT / f"{label}.html"
    if not html_path.exists():
        return [f"  ✗ HTML not found at {html_path}"]
    text_corpus = html_path.read_text(errors="replace")

    violations = []
    for pattern in FORBIDDEN_TOKENS:
        for m in re.finditer(pattern, text_corpus):
            ctx = text_corpus[max(0, m.start() - 30):m.start() + 50]
            violations.append(f"  ✗ {pattern!r} matched: ...{ctx!r}...")
    return violations


# ─── Main ────────────────────────────────────────────────────────
def main() -> int:
    payload_path = FIXTURES / "sample_payload.json"
    payload = json.loads(payload_path.read_text())
    print(f"Loaded payload: {payload_path}  ({payload_path.stat().st_size:,} bytes)")
    print(f"  organization: {payload['organization']['name']}")
    print(f"  capabilities: {len(payload['capabilities'])}")
    print(f"  pillars     : {len(payload['scores']['pillars'])}")
    print(f"  horizons    : {len(payload['horizons'])}")
    print()

    targets = [
        ("score_justification.html.j2", {}),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P1"}),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P2"}),
        ("roadmap_part_pillar.html.j2", {"pillar_focus": "P3"}),
        ("roadmap_part4.html.j2", {}),
    ]

    overall_ok = True

    for tmpl, extra in targets:
        label_suffix = ""
        if "pillar_focus" in extra:
            label_suffix = f"_{extra['pillar_focus'].lower()}"
        out_label = tmpl.replace(".html.j2", "") + label_suffix
        print(f"━━━ Rendering {tmpl} {extra} ━━━")
        try:
            pdf_bytes = render(tmpl, payload, extra, out_label=out_label)
        except Exception as e:
            print(f"  ✗ FAILED: {type(e).__name__}: {e}")
            overall_ok = False
            continue

        out_path = OUT / f"{out_label}.pdf"
        out_path.write_bytes(pdf_bytes)
        print(f"  ✓ {out_path.name}: {len(pdf_bytes):,} bytes")

        # Lint per NFR-REPORT-011
        violations = lint_content(pdf_bytes, out_label)
        if violations:
            print(f"  ✗ Content lint failed for {out_label}:")
            for v in violations:
                print(v)
            overall_ok = False
        else:
            print(f"  ✓ Content lint passed (no forbidden tokens)")
        print()

    print("─" * 60)
    if overall_ok:
        print("✓ ALL TEMPLATES RENDERED + LINT PASSED")
        return 0
    else:
        print("✗ FAILURES")
        return 1


if __name__ == "__main__":
    sys.exit(main())
