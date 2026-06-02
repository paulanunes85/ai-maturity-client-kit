#!/usr/bin/env python3
"""Build per-language ZIP packages for the AI Maturity client kit.

Packaging rule:
- Copilot customization files under .github/ stay in English in every package.
- Client-facing documentation in each package must match the selected language.
- Shared scripts, templates, JSON schemas, workbooks, and renderers are reused.
"""

from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMMON_EXCLUDED_PARTS = {
    ".git",
    ".mypy_cache",
    "__pycache__",
    "dist",
    "build",
    "saida",
}

COMMON_EXCLUDED_NAMES = {
    ".DS_Store",
    "Thumbs.db",
}

GENERATED_OR_CLIENT_INPUTS = {
    "respostas.json",
    "implementation-guide-inputs.json",
    "respostas-forms.xlsx",
    "respostas-survey-devs.xlsx",
    "respostas-survey-learning.xlsx",
    "survey-devs/respostas-devs.json",
    "survey-learning/respostas-learning.json",
}

COPILOT_CUSTOMIZATION_ROOTS = [
    ".github/copilot-instructions.md",
    ".github/agents",
    ".github/prompts",
    ".github/skills",
]

SHARED_RUNTIME_ROOTS = [
    "framework.json",
    "respostas.json.example",
    "Makefile",
    "scripts",
    "relatorios/templates",
    "relatorios/scripts",
    "relatorios/i18n",
    "relatorios/sample_payload.json",
    "coleta/template-export-forms.xlsx",
    "survey-devs/scripts",
    "survey-devs/respostas-mock-devs.json",
    "survey-devs/template-export-forms-devs.xlsx",
    "survey-learning/scripts",
    "survey-learning/respostas-mock-learning.json",
    "survey-learning/template-export-forms-learning.xlsx",
    "wizard/scripts",
    "wizard/implementation-guide-inputs.template.json",
    "referencia/pontuacao-e-calculo.xlsx",
]

LANGUAGE_DOCS = {
    "pt": [],
    "en": [
        ("kit-en/README.md", "README.md"),
        ("kit-en/STEP-BY-STEP.md", "STEP-BY-STEP.md"),
        ("kit-en/FORMS-INSTRUCTIONS.md", "FORMS-INSTRUCTIONS.md"),
    ],
    "es": [
        ("kit-es/README.md", "README.md"),
        ("kit-es/PASO-A-PASO.md", "PASO-A-PASO.md"),
        ("kit-es/INSTRUCCIONES-FORMS.md", "INSTRUCCIONES-FORMS.md"),
    ],
}

LANGUAGE_NOTES = {
        "pt": """# Notas de idioma do pacote PT-BR

- Documentacao de cliente: Portugues (Brasil).
- Arquivos de customizacao do Copilot em `.github/`: mantidos em ingles
    por design, para economizar contexto e melhorar compatibilidade.
- Arquivos JSON, scripts, templates e workbooks sao recursos executaveis
    ou estruturados compartilhados.
""",
        "en": """# Language Notes for the English Package

- Client-facing documentation: English.
- Copilot customization files in `.github/`: intentionally kept in English
    across every language package.
- Shared JSON files, scripts, templates, and workbooks are executable or
    structured assets reused by all languages.
- Canonical question IDs and some internal field names remain in Portuguese
    where required by the scoring framework and production platform mapping.
""",
        "es": """# Notas de idioma del paquete Espanol

- Documentacion orientada al cliente: Espanol.
- Archivos de customizacion de Copilot en `.github/`: se mantienen en ingles
    intencionalmente en todos los paquetes.
- JSONs, scripts, templates y workbooks compartidos son activos ejecutables
    o estructurados reutilizados por todos los idiomas.
- IDs canonicos de preguntas y algunos nombres internos permanecen en Portugues
    cuando el framework de scoring y el mapeo de plataforma lo requieren.
""",
}

ARCHIVE_NAMES = {
    "pt": "ai-maturity-kit-pt.zip",
    "en": "ai-maturity-kit-en.zip",
    "es": "ai-maturity-kit-es.zip",
}


def normalized(path: Path) -> str:
    return path.as_posix()


def is_common_excluded(rel: str) -> bool:
    parts = set(Path(rel).parts)
    if parts & COMMON_EXCLUDED_PARTS:
        return True
    if Path(rel).name in COMMON_EXCLUDED_NAMES:
        return True
    if rel.startswith(".github/workflows/"):
        return True
    if rel.startswith("docs/downloads/"):
        return True
    if rel in GENERATED_OR_CLIENT_INPUTS:
        return True
    return False


def should_include_runtime_file(rel: str) -> bool:
    if is_common_excluded(rel):
        return False
    path = Path(rel)
    if path.suffix.lower() == ".md":
        return rel.startswith(".github/")
    if path.suffix.lower() in {".html", ".htm"}:
        return rel.startswith("relatorios/templates/")
    return True


def add_file(
    zf: zipfile.ZipFile,
    source_rel: str,
    dest_rel: str | None = None,
) -> None:
    source = ROOT / source_rel
    if not source.exists() or not source.is_file():
        return
    arcname = dest_rel or source_rel
    if arcname in zf.NameToInfo:
        return
    zf.write(source, arcname)


def iter_source_files(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    return sorted(path for path in source.rglob("*") if path.is_file())


def should_add_tree_file(rel: str, runtime_filter: bool) -> bool:
    if runtime_filter and not should_include_runtime_file(rel):
        return False
    return not is_common_excluded(rel)


def destination_for(
    file_path: Path,
    source: Path,
    dest_rel: str | None,
) -> str:
    if not dest_rel:
        return normalized(file_path.relative_to(ROOT))
    if source.is_file():
        return dest_rel
    return normalized(Path(dest_rel) / file_path.relative_to(source))


def add_tree(
    zf: zipfile.ZipFile,
    source_rel: str,
    dest_rel: str | None = None,
    *,
    runtime_filter: bool = False,
) -> None:
    source = ROOT / source_rel
    if not source.exists():
        return

    for file_path in iter_source_files(source):
        rel = normalized(file_path.relative_to(ROOT))
        if not should_add_tree_file(rel, runtime_filter):
            continue
        dest = destination_for(file_path, source, dest_rel)
        if dest in zf.NameToInfo:
            continue
        zf.write(file_path, dest)


def add_copilot_customizations(zf: zipfile.ZipFile) -> None:
    for root in COPILOT_CUSTOMIZATION_ROOTS:
        add_tree(zf, root)


def add_shared_runtime(zf: zipfile.ZipFile) -> None:
    for root in SHARED_RUNTIME_ROOTS:
        add_tree(zf, root, runtime_filter=True)


def add_reference_examples(zf: zipfile.ZipFile, lang: str) -> None:
    # JSON examples are language-neutral structured outputs.
    for source in [
        "referencia/exemplo-saida/scores.json",
        "referencia/exemplo-saida/gaps.json",
        "referencia/exemplo-saida/recomendacoes.json",
        "referencia/exemplo-saida/payload.json",
        "referencia/exemplo-saida/maturidade-developer-survey-EXEMPLO.json",
        "referencia/exemplo-saida/implementation-guide-inputs-EXEMPLO.json",
    ]:
        add_file(zf, source)

    if lang == "pt":
        example_dir = ROOT / "referencia/exemplo-saida"
        for file_path in sorted(example_dir.glob("*.pdf")):
            add_file(zf, normalized(file_path.relative_to(ROOT)))
        add_file(
            zf,
            "referencia/exemplo-saida/pontuacao-preenchida-2026-05-08.xlsx",
        )
        add_file(zf, "referencia/exemplo-saida/README.md")
        add_file(
            zf,
            "referencia/exemplo-saida/insights-developer-survey-EXEMPLO.md",
        )
        add_file(zf, "referencia/exemplo-saida/plano-capacitacao-EXEMPLO.md")
    elif lang == "en":
        add_tree(zf, "referencia/exemplo-saida/en", runtime_filter=False)


def add_pt_documentation(zf: zipfile.ZipFile) -> None:
    excluded_prefixes = (
        ".github/",
        ".git/",
        "docs/",
        "kit-en/",
        "kit-es/",
        "saida/",
        "dist/",
    )
    for file_path in sorted(ROOT.rglob("*.md")):
        rel = normalized(file_path.relative_to(ROOT))
        if rel.startswith(excluded_prefixes) or is_common_excluded(rel):
            continue
        add_file(zf, rel)

    # PT-BR visual guides are intentionally included only in the PT package.
    add_tree(zf, "formularios", runtime_filter=False)
    add_file(zf, "wizard/implementation-guide-wizard.html")
    add_file(zf, "referencia/calculadora-pontuacao.html")


def add_localized_docs(zf: zipfile.ZipFile, lang: str) -> None:
    if lang == "pt":
        add_pt_documentation(zf)
    for source, dest in LANGUAGE_DOCS[lang]:
        add_file(zf, source, dest)
    zf.writestr("PACKAGE-LANGUAGE-NOTES.md", LANGUAGE_NOTES[lang])


def build_archive(lang: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = output_dir / ARCHIVE_NAMES[lang]
    if archive_path.exists():
        archive_path.unlink()

    with zipfile.ZipFile(
        archive_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as zf:
        add_copilot_customizations(zf)
        add_shared_runtime(zf)
        add_reference_examples(zf, lang)
        add_localized_docs(zf, lang)

    return archive_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build PT, EN, and ES language kit ZIPs."
    )
    parser.add_argument(
        "--out",
        default="dist",
        help="Output directory for generated ZIP files.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Delete the output directory before building.",
    )
    args = parser.parse_args()

    output_dir = (ROOT / args.out).resolve()
    if args.clean and output_dir.exists():
        shutil.rmtree(output_dir)

    archives = [build_archive(lang, output_dir) for lang in ("pt", "en", "es")]
    for archive in archives:
        size_mb = archive.stat().st_size / (1024 * 1024)
        try:
            display_path = archive.relative_to(ROOT)
        except ValueError:
            display_path = archive
        print(f"{display_path} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
