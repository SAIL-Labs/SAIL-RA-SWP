#!/usr/bin/env python3
"""Render a paired Risk Assessment (RA) and Safe Work Procedure (SWP) from one YAML file.

One combined YAML file per document pair (``meta:`` + ``ra:`` + ``swp:``) is the single
source of truth in ``documents/``. From it this script renders:

- **Web**: Jekyll markdown into ``_risk_assessments/<slug>.md`` and
  ``_safe_work_procedures/<slug>.md`` (both dirs are generated artefacts, gitignored).
- **Word**: the official USyd .docx forms via docxtpl (Jinja2-in-.docx) into
  ``docgen/out/docx/…``.
- **PDF**: from the Word output via headless LibreOffice (``--pdf``) into
  ``docgen/out/pdfs/…`` — filenames match the site's download-button URLs.

Because the shared header lives once in ``meta:``, the RA and its paired SWP stay in
sync by construction.

Usage
-----
    python docgen/render.py --all                 # web + docx for every documents/*.yaml
    python docgen/render.py documents/foo.yaml    # one pair
    python docgen/render.py --all --pdf           # also convert docx -> pdf (needs soffice)
    python docgen/render.py --all --check         # validate + dry-run render, write nothing

The script validates the data before rendering (required keys, rating values against the
template's own risk matrix, list-typed fields) and renders with ``jinja2.StrictUndefined``
so any placeholder missing from the data fails loudly rather than rendering blank.
"""
from __future__ import annotations

import argparse
import copy
import shutil
import subprocess
import sys
from pathlib import Path

import yaml
from docxtpl import DocxTemplate, Listing
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from jinja2.exceptions import TemplateError

DOCGEN_DIR = Path(__file__).resolve().parent
SITE_ROOT = DOCGEN_DIR.parent
DOCUMENTS_DIR = SITE_ROOT / "documents"

# ---------------------------------------------------------------------------
# Contract — kept in lock-step with the two .docx templates and the two .md.j2
# web templates in templates/. The placeholder map was extracted from the
# templates themselves; if you edit a template's tags, update the matching
# entry here (and vice versa).
# ---------------------------------------------------------------------------

# The four risk-rating levels are the ONLY values that appear in the template's
# embedded Risk Matrix image (Low=green, Medium=yellow, High=orange, Very High=red).
# NOT "Critical" and NOT a five-level "Very Low" scale — those are wrong for this form.
ALLOWED_RATINGS = ("Low", "Medium", "High", "Very High")
ALLOWED_STATUS = ("Draft", "Approved")

META_KEYS = [
    "slug", "building", "name", "title", "status", "version", "version_issue_date",
    "description", "faculty_school", "prepared_by", "supervisors",
    "issue_date", "next_review_date",
]
META_OPTIONAL_KEYS = ["rooms", "key_hazards", "includes"]
META_LIST_KEYS = ["supervisors", "rooms"]

RA_KEYS = [
    "activity", "location", "persons_at_risk", "team", "references",
    "risks", "implementation_date", "additional_controls", "emergency_controls",
]
RA_LIST_KEYS = ["persons_at_risk", "team", "references", "risks",
                "additional_controls", "emergency_controls"]
RISK_KEYS = ["task", "hazards", "harm", "controls",
             "current_rating", "additional_controls", "residual_rating"]
RA_ADDL_CONTROL_KEYS = ["control", "resources", "responsible", "date", "riskware_ref"]

SWP_KEYS = [
    "hazards", "resources", "steps",
    "emergency_shutdown", "emergency_procedures", "cleanup_waste",
    "references", "competency", "assessors",
]
SWP_LIST_KEYS = ["hazards", "resources", "steps", "emergency_shutdown",
                 "emergency_procedures", "cleanup_waste", "references",
                 "competency", "assessors"]
SWP_HAZARD_KEYS = ["hazard", "controls"]

WORD_TEMPLATES = {
    "ra": "risk-assessment-template.docx",
    "swp": "safe-work-procedure-template.docx",
}
WEB_TEMPLATES = {"ra": "ra.md.j2", "swp": "swp.md.j2"}


class ValidationError(Exception):
    """Raised with a list of all data problems found, so the user fixes them in one pass."""


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def _require(section: dict, keys: list[str], where: str, errors: list[str]) -> None:
    if not isinstance(section, dict):
        errors.append(f"{where}: expected a mapping, got {type(section).__name__}")
        return
    for k in keys:
        if k not in section:
            errors.append(f"{where}: missing required key '{k}'")


def _require_list(section: dict, keys: list[str], where: str, errors: list[str]) -> None:
    for k in keys:
        if k in section and not isinstance(section[k], list):
            errors.append(f"{where}.{k}: expected a list, got {type(section[k]).__name__}")


def _check_rating(value, where: str, errors: list[str]) -> None:
    if value is None or str(value).strip() == "":
        errors.append(f"{where}: rating is empty (expected one of {', '.join(ALLOWED_RATINGS)})")
        return
    canonical = {r.lower(): r for r in ALLOWED_RATINGS}
    if str(value).strip().lower() not in canonical:
        errors.append(
            f"{where}: '{value}' is not a valid risk rating "
            f"(expected one of {', '.join(ALLOWED_RATINGS)} — these are the labels on the template's Risk Matrix)"
        )


def validate(data: dict, source: str = "") -> None:
    """Validate the combined data dict; raise ValidationError listing every problem."""
    errors: list[str] = []

    for top in ("meta", "ra", "swp"):
        if top not in data or not isinstance(data.get(top), dict):
            errors.append(f"top level: missing or malformed '{top}:' section")
    if errors:
        raise ValidationError("\n".join(f"  - {e}" for e in errors))

    meta, ra, swp = data["meta"], data["ra"], data["swp"]

    # --- meta ---
    _require(meta, META_KEYS, "meta", errors)
    _require_list(meta, META_LIST_KEYS, "meta", errors)
    slug = str(meta.get("slug", "")).strip()
    if slug and not all(c.islower() or c.isdigit() or c == "-" for c in slug):
        errors.append(f"meta.slug: '{slug}' must be lowercase letters, digits and dashes only")
    if source and slug and Path(source).stem != slug and not Path(source).stem.startswith("_"):
        errors.append(f"meta.slug: '{slug}' must match the YAML filename ('{Path(source).stem}')")
    building = str(meta.get("building", "")).strip()
    if "building" in meta and (not building or any(c.isspace() for c in building)):
        errors.append(f"meta.building: '{meta.get('building')}' must be a non-empty code with no spaces (e.g. A28)")
    rooms = meta.get("rooms")
    for i, room in enumerate(rooms if isinstance(rooms, list) else []):
        r = str(room).strip()
        if not r or any(c.isspace() for c in r):
            errors.append(f"meta.rooms[{i}]: '{room}' must be a non-empty room number with no spaces (e.g. 218G)")
    if meta.get("status") not in ALLOWED_STATUS:
        errors.append(f"meta.status: '{meta.get('status')}' must be one of {', '.join(ALLOWED_STATUS)}")

    # --- ra ---
    _require(ra, RA_KEYS, "ra", errors)
    _require_list(ra, RA_LIST_KEYS, "ra", errors)
    for i, risk in enumerate(ra.get("risks") or []):
        where = f"ra.risks[{i}]"
        _require(risk, RISK_KEYS, where, errors)
        if isinstance(risk, dict):
            _check_rating(risk.get("current_rating"), f"{where}.current_rating", errors)
            _check_rating(risk.get("residual_rating"), f"{where}.residual_rating", errors)
    if not (ra.get("risks") or []):
        errors.append("ra.risks: at least one risk row is required")
    for i, ctrl in enumerate(ra.get("additional_controls") or []):
        _require(ctrl, RA_ADDL_CONTROL_KEYS, f"ra.additional_controls[{i}]", errors)

    # --- swp ---
    _require(swp, SWP_KEYS, "swp", errors)
    _require_list(swp, SWP_LIST_KEYS, "swp", errors)
    for i, haz in enumerate(swp.get("hazards") or []):
        _require(haz, SWP_HAZARD_KEYS, f"swp.hazards[{i}]", errors)
    if not (swp.get("hazards") or []):
        errors.append("swp.hazards: at least one hazard row is required")
    for k in ("version", "version_issue_date"):
        if k in swp:
            errors.append(f"swp.{k}: moved to meta.{k} — remove it from swp:")

    if errors:
        raise ValidationError("\n".join(f"  - {e}" for e in errors))


# ---------------------------------------------------------------------------
# Context derivation
# ---------------------------------------------------------------------------

def derive(data: dict) -> dict:
    """Return a deep-copied context with derived fields filled in.

    - meta.ra_reference / meta.swp_reference as
      {RA|SWP}-{building}-SAIL-{rooms "_"-joined, omitted if none}-{slug}
    - meta.reference = ra_reference (the Word RA header and the SWP per-hazard
      "Associated risk assessment reference" rows both use this tag)
    - swp.version / swp.version_issue_date mapped from meta (Word SWP tags)
    - meta.key_hazards defaulted from the first line of each risk's hazards
    """
    ctx = copy.deepcopy(data)
    meta, ra, swp = ctx["meta"], ctx["ra"], ctx["swp"]

    building = str(meta["building"]).strip()
    rooms = "_".join(str(r).strip() for r in (meta.get("rooms") or []))
    core = "-".join(p for p in (building, "SAIL", rooms, meta["slug"]) if p)
    meta["ra_reference"] = f"RA-{core}"
    meta["swp_reference"] = f"SWP-{core}"
    meta["reference"] = meta["ra_reference"]

    swp["version"] = meta["version"]
    swp["version_issue_date"] = meta["version_issue_date"]

    if not meta.get("key_hazards"):
        seen: list[str] = []
        for r in ra.get("risks", []):
            first = str(r.get("hazards", "")).split("\n")[0].strip().rstrip(".")
            if first and first not in seen:
                seen.append(first)
        meta["key_hazards"] = ", ".join(seen)
    if not meta.get("includes"):
        meta["includes"] = ("Hazards and controls, resources, step-by-step instructions, "
                            "emergency procedures, cleanup, competency requirements")
    return ctx


# ---------------------------------------------------------------------------
# Word rendering
# ---------------------------------------------------------------------------

def _wrap_multiline(value):
    """Recursively wrap any string containing newlines in docxtpl.Listing so that
    '\\n' renders as a real Word line break inside a cell/paragraph (plain Jinja does
    not translate '\\n' to <w:br/>). Non-string / newline-free values pass through."""
    if isinstance(value, str):
        return Listing(value) if "\n" in value else value
    if isinstance(value, list):
        return [_wrap_multiline(v) for v in value]
    if isinstance(value, dict):
        return {k: _wrap_multiline(v) for k, v in value.items()}
    return value


def render_word(ctx: dict, templates_dir: Path, out_dir: Path, dry_run: bool = False) -> list[Path]:
    meta = ctx["meta"]
    word_ctx = _wrap_multiline(ctx)
    env = Environment(undefined=StrictUndefined, autoescape=False)
    jobs = [
        (WORD_TEMPLATES["ra"], out_dir / "docx" / "risk-assessments" / f"{meta['ra_reference']}.docx"),
        (WORD_TEMPLATES["swp"], out_dir / "docx" / "safe-work-procedures" / f"{meta['swp_reference']}.docx"),
    ]
    written: list[Path] = []
    for template_name, out_path in jobs:
        template_path = templates_dir / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"template not found: {template_path}")
        tpl = DocxTemplate(str(template_path))
        tpl.render(word_ctx, jinja_env=env)  # render even on --check: catches tag errors
        if not dry_run:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            tpl.save(str(out_path))
            written.append(out_path)
    return written


# ---------------------------------------------------------------------------
# Web rendering
# ---------------------------------------------------------------------------

def _filter_br(value) -> str:
    """Newlines -> <br> so one multiline YAML string works on web and in Word."""
    return str(value).replace("\n", "<br>")


def _filter_cell(value) -> str:
    """Make a YAML string safe inside a markdown table cell."""
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def _filter_bullets(value) -> str:
    """Render a list as dash bullets inside a table cell."""
    return "<br>".join(f"- {_filter_cell(v)}" for v in value)


def _web_env(templates_dir: Path) -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        undefined=StrictUndefined,
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["br"] = _filter_br
    env.filters["cell"] = _filter_cell
    env.filters["bullets"] = _filter_bullets
    return env


def _front_matter(ctx: dict, kind: str) -> dict:
    meta = ctx["meta"]
    common = {
        "layout": "document",
        "doc_type": "Risk Assessment" if kind == "ra" else "Safe Work Procedure",
        "status": meta["status"],
        "equipment_name": meta["name"],
        "version": str(meta["version"]),
        "description": meta["description"],
        "show_review": True,
    }
    md = {
        "title": meta["title"],
        "version": str(meta["version"]),
        "issue_date": meta["issue_date"],
        "next_review_date": meta["next_review_date"],
        "prepared_by": meta["prepared_by"],
        "supervisors": ", ".join(meta["supervisors"]),
        "faculty_school": meta["faculty_school"],
    }
    slug = meta["slug"]
    if kind == "ra":
        return {
            **common,
            "title": f"Risk Assessment - {meta['name']}",
            "permalink": f"/risk-assessments/{slug}/",
            "reference": meta["ra_reference"],
            "key_hazards": meta["key_hazards"],
            "metadata": {"reference": meta["ra_reference"], **md},
            "related_docs": [{
                "title": "Safe Work Procedure",
                "url": f"/safe-work-procedures/{slug}/",
                "description": "Detailed operating procedures",
            }],
        }
    return {
        **common,
        "title": f"Safe Work Procedure - {meta['name']}",
        "permalink": f"/safe-work-procedures/{slug}/",
        "reference": meta["swp_reference"],
        "includes": meta["includes"],
        "metadata": {"reference": meta["swp_reference"], **md},
        "related_docs": [{
            "title": "Risk Assessment",
            "url": f"/risk-assessments/{slug}/",
            "description": "Hazard identification and controls",
        }],
    }


def render_web(ctx: dict, templates_dir: Path, site_root: Path, dry_run: bool = False) -> list[Path]:
    slug = ctx["meta"]["slug"]
    env = _web_env(templates_dir)
    jobs = [
        ("ra", site_root / "_risk_assessments" / f"{slug}.md"),
        ("swp", site_root / "_safe_work_procedures" / f"{slug}.md"),
    ]
    written: list[Path] = []
    for kind, out_path in jobs:
        body = env.get_template(WEB_TEMPLATES[kind]).render(ctx)
        fm = yaml.safe_dump(_front_matter(ctx, kind), sort_keys=False,
                            allow_unicode=True, width=1000)
        banner = (f"<!-- GENERATED from documents/{slug}.yaml — DO NOT EDIT.\n"
                  f"     Regenerate with: python docgen/render.py --all -->\n")
        content = f"---\n{fm}---\n\n{banner}\n{body}"
        if not dry_run:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            written.append(out_path)
    return written


# ---------------------------------------------------------------------------
# PDF conversion (LibreOffice)
# ---------------------------------------------------------------------------

def _find_soffice() -> str:
    for candidate in ("soffice", "libreoffice"):
        path = shutil.which(candidate)
        if path:
            return path
    raise FileNotFoundError(
        "LibreOffice not found (need 'soffice' on PATH). "
        "macOS: brew install --cask libreoffice; Ubuntu: apt-get install libreoffice-writer"
    )


def render_pdf(docx_paths: list[Path], out_dir: Path) -> list[Path]:
    """Convert rendered .docx files to PDF, mirroring the docx/ tree under pdfs/."""
    soffice = _find_soffice()
    written: list[Path] = []
    for docx in docx_paths:
        # docx/<collection>/NAME.docx -> pdfs/<collection>/NAME.pdf
        pdf_dir = out_dir / "pdfs" / docx.parent.name
        pdf_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [soffice, "--headless", "--convert-to", "pdf",
             "--outdir", str(pdf_dir), str(docx)],
            check=True, capture_output=True, timeout=180,
        )
        pdf = pdf_dir / (docx.stem + ".pdf")
        if not pdf.exists():
            raise RuntimeError(f"LibreOffice did not produce {pdf}")
        written.append(pdf)
    return written


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def load_data(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: top-level YAML must be a mapping with meta/ra/swp sections")
    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render paired RA + SWP (web markdown, Word .docx, PDF) from combined YAML data files.",
    )
    parser.add_argument("data", nargs="*", type=Path,
                        help="YAML file(s) to render (or use --all)")
    parser.add_argument("--all", action="store_true",
                        help=f"render every YAML in {DOCUMENTS_DIR.relative_to(SITE_ROOT)}/ (files starting with _ are skipped)")
    parser.add_argument("--web", action="store_true", help="render web markdown only")
    parser.add_argument("--docx", action="store_true", help="render Word .docx only")
    parser.add_argument("--pdf", action="store_true",
                        help="also convert .docx to PDF via LibreOffice (implies --docx)")
    parser.add_argument("--check", action="store_true",
                        help="validate and dry-run render everything; write nothing")
    parser.add_argument("-o", "--out-dir", type=Path, default=DOCGEN_DIR / "out",
                        help="output directory for docx/ and pdfs/ (default: docgen/out)")
    parser.add_argument("--site-root", type=Path, default=SITE_ROOT,
                        help="repo root that holds the _*/ collection dirs (default: parent of docgen/)")
    parser.add_argument("--templates-dir", type=Path, default=DOCGEN_DIR / "templates",
                        help="directory holding the .docx and .md.j2 templates")
    args = parser.parse_args(argv)

    files = list(args.data)
    if args.all:
        files += sorted(p for p in DOCUMENTS_DIR.glob("*.yaml") if not p.name.startswith("_"))
    if not files:
        parser.error("no input files — pass YAML paths or --all")

    # default: web + docx (pdf only when asked)
    do_web = args.web or not (args.web or args.docx or args.pdf)
    do_docx = args.docx or args.pdf or not (args.web or args.docx or args.pdf)

    failures = 0
    all_docx: list[Path] = []
    for path in files:
        try:
            data = load_data(path)
            validate(data, source=str(path))
            ctx = derive(data)
            written: list[Path] = []
            if do_web:
                written += render_web(ctx, args.templates_dir, args.site_root, dry_run=args.check)
            if do_docx:
                docx = render_word(ctx, args.templates_dir, args.out_dir, dry_run=args.check)
                written += docx
                all_docx += docx
            label = "OK (dry run)" if args.check else "OK"
            print(f"{path}: {label}")
            for p in written:
                print(f"  -> {p}")
        except ValidationError as exc:
            print(f"{path}: validation failed\n{exc}", file=sys.stderr)
            failures += 1
        except TemplateError as exc:
            print(f"{path}: template render error ({type(exc).__name__}): {exc}\n"
                  "  A required value may be missing from the data, or a template tag may be "
                  "split across Word runs.", file=sys.stderr)
            failures += 1
        except (FileNotFoundError, yaml.YAMLError) as exc:
            print(f"{path}: {exc}", file=sys.stderr)
            failures += 1

    if args.pdf and not args.check and all_docx and failures == 0:
        try:
            for pdf in render_pdf(all_docx, args.out_dir):
                print(f"  -> {pdf}")
        except (FileNotFoundError, RuntimeError, subprocess.SubprocessError) as exc:
            print(f"PDF conversion failed: {exc}", file=sys.stderr)
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
