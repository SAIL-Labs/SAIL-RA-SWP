# Site Architecture Documentation

## One YAML → web + Word + PDF

Every RA/SWP pair is defined by a single data file, `documents/<slug>.yaml`, with three sections:

| Section | Contents | Used by |
| --- | --- | --- |
| `meta:` | slug, abbrev, number, name, title, status, version, dates, preparer, supervisors, index-card text | **both** documents |
| `ra:` | activity, location, people, legislation, risk table, implementation actions, emergency controls | Risk Assessment |
| `swp:` | hazards/controls, resources, steps, emergency procedures, cleanup, competency, assessors | Safe Work Procedure |

`docgen/render.py` renders each YAML into:

1. `_risk_assessments/<slug>.md` + `_safe_work_procedures/<slug>.md` — Jekyll pages (**generated, gitignored — never edit**), via the Jinja2 templates `docgen/templates/{ra,swp}.md.j2`;
2. `docgen/out/docx/**/SAIL-{RA,SWP}-<slug>.docx` — the official USyd Word forms, via docxtpl and the tagged templates `docgen/templates/*.docx`;
3. `docgen/out/pdfs/**/SAIL-{RA,SWP}-<slug>.pdf` — converted from the Word docs by headless LibreOffice (`--pdf`).

The full schema is documented inline in [`documents/_example.yaml`](documents/_example.yaml); required keys are enforced by the `*_KEYS` constants in `docgen/render.py`.

## How the Index Page Auto-Populates

The front page (`index.md`) displays all documents without manual editing:

1. **Jekyll collections** (`_config.yml`): `_risk_assessments/` and `_safe_work_procedures/`.
2. Jekyll finds every markdown file the generator wrote into those directories.
3. `index.md` loops the collections with Liquid, splitting by `status` (`Approved` cards first, then `Draft`), sorting each group by `equipment_name`.

The generator emits all card fields into the front matter automatically from `meta:` — `equipment_name` (from `meta.name`), `reference` (derived), `version`, `description`, `key_hazards` (RA; defaults to the risk table's hazards) and `includes` (SWP).

## Reference Numbers

Derived — never typed:

```
meta.abbrev: BAMBU-H2D     ┐
meta.number: 1             ┴→  SAIL-RA-BAMBU-H2D-001  and  SAIL-SWP-BAMBU-H2D-001
```

`abbrev` defaults to `slug` uppercased; override it when the historical reference differs (e.g. `3sae-cms` uses `CMS`). The SWP's hazard rows cite the RA reference automatically.

## Risk Ratings

The University Risk Matrix embedded in the RA form defines exactly four levels: **Low, Medium, High, Very High**. The validator rejects anything else (no "Critical", no "Very Low"). Residual risk should land at Low.

## File Naming Convention

- YAML: `documents/<slug>.yaml`, where `<slug>` = `meta.slug` (lowercase, hyphen-separated — enforced).
- Permalinks: `/risk-assessments/<slug>/` and `/safe-work-procedures/<slug>/` (emitted automatically).
- Downloads: `/pdfs/<collection>/SAIL-{RA|SWP}-<slug>.pdf` and `/docx/<collection>/SAIL-{RA|SWP}-<slug>.docx` — the "Download PDF"/"Download Word" buttons in `_layouts/default.html` build these URLs from the page slug.

## Testing Locally

```bash
./serve.sh                                   # regenerates pages + serves with livereload
# or piecemeal:
docgen/.venv/bin/python docgen/render.py --all --web   # after editing a YAML
docgen/.venv/bin/python docgen/render.py --all --pdf   # Word + PDF (needs LibreOffice)
```

View at http://localhost:4000/SAIL-RA-SWP/ (note the baseurl).

## CI Pipelines

- **`docgen.yml`** (PRs/branches touching `documents/**` or `docgen/**`): validates every YAML, renders web + Word + PDF, uploads everything as a `rendered-documents` artifact for reviewers.
- **`jekyll.yml`** (push to main): regenerates pages, builds the site, renders Word + PDF, publishes them under `/docx/` and `/pdfs/` in the Pages artifact, deploys.

## Troubleshooting

- **Validation error** (`missing required key`, `not a valid risk rating`): fix the YAML — the error lists every problem with its path (`ra.risks[3].residual_rating`).
- **Template render error / UndefinedError**: a required value is missing, or someone re-typed a Jinja tag inside a Word template and Word split it across runs — see "Editing templates in Word" in `docgen/README.md`.
- **Document not on the index**: did the generator run? (`./serve.sh` runs it; a bare `jekyll serve` does not.) Check `meta.status` is exactly `Draft` or `Approved` (case-sensitive).
- **Stale page**: `bundle exec jekyll clean`, then re-run `./serve.sh`.

## Benefits

- RA and SWP can never disagree — shared `meta:` block
- Web, Word and PDF can never drift — single source, one renderer
- Strict validation before anything renders (required keys, rating vocabulary, slug format)
- PR artifacts show reviewers the real documents a data change produces
