# docgen — one YAML → web pages + Word documents + PDFs

Renders each combined data file in `documents/` into a paired **Risk Assessment** and
**Safe Work Procedure** in three forms:

- **Web**: Jekyll markdown into `_risk_assessments/` and `_safe_work_procedures/`
  (generated, gitignored) via the Jinja2 templates `templates/{ra,swp}.md.j2`.
- **Word**: the official University of Sydney forms via
  [docxtpl](https://docxtpl.readthedocs.io/) (Jinja2 inside `.docx`).
- **PDF**: converted from the Word output with headless LibreOffice.

An RA always pairs with an SWP. The shared header (references, title, dates, preparer,
supervisors) lives once in the `meta:` block, so the pair **cannot drift out of sync**.

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python render.py --all                       # web + Word for every documents/*.yaml
python render.py ../documents/foo.yaml       # one pair
python render.py --all --pdf                 # + PDFs (needs LibreOffice: brew install --cask libreoffice)
python render.py --all --check               # validate + dry-run render, write nothing
```

Output goes to `_risk_assessments/`, `_safe_work_procedures/` (web) and
`docgen/out/{docx,pdfs}/` (documents). Filenames match the site's download-button URLs
(`<reference>.pdf`, e.g. `RA-A28-SAIL-218G-3sae-cms.pdf` — the buttons build URLs
from `page.reference`).

## The data file

One file per document pair, three sections — see
[`documents/_example.yaml`](../documents/_example.yaml) for every field annotated:

| Section | Purpose |
| --- | --- |
| `meta:` | slug, building + rooms (→ derived references), name, title, status, version, dates, preparer, supervisors, index-card text |
| `ra:`   | activity, location, people, legislation, risk table, implementation actions, emergency controls |
| `swp:`  | hazard/control rows, resources, steps, emergency shutdown & procedures, cleanup, references, competency, assessors |

The required-key lists live in the `*_KEYS` constants at the top of `render.py` — the
templates and those constants must be kept in lock-step.

### Derived fields (never typed)

- `RA-{building}-SAIL-{rooms}-{slug}` / `SWP-{building}-SAIL-{rooms}-{slug}`
  from `meta.building` + optional `meta.rooms` (joined with `_`; segment omitted
  when no rooms are listed) + `meta.slug`.
- The SWP hazard rows cite the RA reference automatically.
- `meta.key_hazards` defaults to the first line of each risk's hazards.

### Risk ratings

Exactly the four labels on the RA form's embedded Risk Matrix:

> **Low** · **Medium** · **High** · **Very High**

(Case-insensitive match; anything else — including "Critical" and "Very Low" — is
rejected.) Residual risk should land at Low.

### Multi-line content

Use YAML block scalars; newlines become real line breaks in Word (`docxtpl.Listing`)
and `<br>` on the web. Prefix lines with `- ` for dash lists inside table cells:

```yaml
controls: |-
  - Interlocked enclosure
  - Laser safety eyewear
  - Trained users only
```

Strings are **plain text** — markdown (`**`, `##`) would render literally in the Word
form. Use CAPS for emphasis (NEVER, MUST, MANDATORY).

## Validation

Before rendering, `render.py` checks: all three sections and every required key
present; list-typed fields are lists; slug format and slug↔filename match; status is
Draft/Approved; at least one risk row and one hazard row; every rating is a valid
Risk-Matrix value. Every problem is reported at once and the exit code is non-zero
(CI-friendly). Rendering uses `jinja2.StrictUndefined`, so a placeholder the data
doesn't supply is a hard error, not a blank cell.

## Templates

`templates/risk-assessment-template.docx` and `templates/safe-work-procedure-template.docx`
are the marked-up USyd forms; `templates/{ra,swp}.md.j2` are the matching web-page
templates. All four mirror the same section structure.

> ⚠️ **Editing the .docx templates in Word:** if you re-type a `{{ … }}` / `{% … %}`
> tag, Word may split it across runs and docxtpl will fail to parse it. After any
> template edit, run `python render.py --all --check` — a clean pass means the tags are
> intact. The RA template contains a footnote in the "additional controls" header and
> the embedded Risk Matrix image on the last page; don't delete those. The two static
> implementation-table rows (write SWP, training) are deliberate boilerplate.

## CI

- `.github/workflows/docgen.yml` — on PRs/branches touching `documents/**` or
  `docgen/**`: validates and renders everything, uploads a `rendered-documents`
  artifact for review.
- `.github/workflows/jekyll.yml` — on push to main: generates pages, builds the site,
  renders Word + PDF, and publishes them at `/docx/…` and `/pdfs/…` on the live site.
