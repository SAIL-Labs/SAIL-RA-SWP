# SAIL Laboratory Safety Documentation

GitHub Pages site for laboratory safety documentation — Risk Assessments (RAs) and Safe Work Procedures (SWPs) for SAIL Laboratory, School of Physics, University of Sydney.

**One YAML file per RA/SWP pair is the single source of truth.** From `documents/<slug>.yaml` the toolchain renders:

1. the **web pages** (Jekyll collections, published to GitHub Pages),
2. the **official USyd Word forms** (.docx via docxtpl), and
3. the **PDFs** (converted from the Word forms with LibreOffice).

The web pages, Word docs and PDFs can never drift apart, and an RA can never disagree with its paired SWP — they share one `meta:` block.

## 📁 Repository Structure

```
SAIL-RA-SWP/
├── documents/                         # ⭐ SOURCE OF TRUTH — one YAML per RA+SWP pair
│   ├── _example.yaml                  #    annotated schema reference (not rendered)
│   ├── bambu-h2d.yaml
│   ├── 3sae-cms.yaml
│   └── general-lab-safety.yaml
│
├── docgen/                            # The document generator
│   ├── render.py                      #    YAML → web md + Word .docx + PDF
│   ├── README.md                      #    authoring guide + schema documentation
│   ├── requirements.txt
│   └── templates/
│       ├── risk-assessment-template.docx    # official USyd forms (Jinja2-tagged)
│       ├── safe-work-procedure-template.docx
│       ├── ra.md.j2                   #    web page templates (mirror the Word forms)
│       └── swp.md.j2
│
├── _risk_assessments/                 # GENERATED web pages — gitignored, never edit
├── _safe_work_procedures/             # GENERATED web pages — gitignored, never edit
│
├── index.md                           # Home page (auto-populates from collections)
├── _layouts/, assets/, _config.yml    # Jekyll site chrome
│
├── SYSTEM_PROMPTS.md                  # Claude prompts for the issue-driven workflow
├── ROUTINE_SETUP.md                   # Claude Code routine setup (issue → draft PR)
└── .github/workflows/
    ├── jekyll.yml                     # deploy: generate + build + PDF + publish
    └── docgen.yml                     # PR check: validate + render all documents
```

## 🚀 Viewing the Site

Published at: <https://sail-labs.github.io/SAIL-RA-SWP/>

Run locally (regenerates pages from YAML, then serves):

```bash
./serve.sh
# open http://localhost:4000/SAIL-RA-SWP/
```

## 📝 Adding or Editing a Document

**Never edit the `.md` files in `_risk_assessments/` or `_safe_work_procedures/` — they are generated.** Edit the YAML and re-render.

### 🤖 Via GitHub issue (recommended)

1. Open an issue with the **New Equipment Documentation** template (label `new-equipment` is applied automatically).
2. The Claude Code **routine** fires on issue creation and drafts the document — see `ROUTINE_SETUP.md` for setup and for the companion review routines.
3. A draft PR appears containing `documents/<slug>.yaml`. The docgen CI check renders the actual web pages, Word docs and PDFs as a PR artifact for review.
4. A qualified person reviews, fixes placeholders, verifies specs against manufacturer documentation, flips `meta.status` to `Approved`, and merges.

### ✍️ By hand

```bash
cp documents/_example.yaml documents/my-equipment.yaml
# edit it (meta.slug must be "my-equipment"), then:
python docgen/render.py documents/my-equipment.yaml        # render web + Word
python docgen/render.py documents/my-equipment.yaml --pdf  # + PDF (needs LibreOffice)
./serve.sh                                                  # preview the site
```

First-time setup: `python3 -m venv docgen/.venv && docgen/.venv/bin/pip install -r docgen/requirements.txt` (or let `./serve.sh` do it).

The full schema is documented in [`documents/_example.yaml`](documents/_example.yaml) and [`docgen/README.md`](docgen/README.md).

### Reference numbers

Derived automatically from `meta.abbrev` + `meta.number` — never typed anywhere:

- `SAIL-RA-BAMBU-H2D-001` and `SAIL-SWP-BAMBU-H2D-001` from `abbrev: BAMBU-H2D`, `number: 1`.
- The SWP's hazard table cites the RA's reference automatically.

### Risk ratings

The four levels on the University Risk Matrix (embedded in the RA form): **Low, Medium, High, Very High**. The validator rejects anything else. Residual risk should land at Low.

## ✅ Document Workflow

1. **Create** `documents/<slug>.yaml` (issue workflow or by hand)
2. **Render + preview** locally or via the PR artifact
3. **Consult** stakeholders (users, safety officer)
4. **Review** — verify every value against manufacturer documentation
5. **Approve** — set `meta.status: Approved` and merge (qualified reviewer only)
6. **Train** users, **display** the printed PDF near the equipment
7. **Review** annually (`meta.next_review_date`) or after any incident/change

### Document statuses

- `Draft` — work in progress, shows after Approved docs on the index
- `Approved` — reviewed and approved for use

## 🎨 Styling

Site CSS lives in `assets/css/style.css` (document tables, warning boxes, badges, print styles). The generated pages use the CSS classes `metadata-table`, `activity-persons-table`, `legislation-box`, `methodology-box`, `hazard-table-wrapper`, `emergency-box`, `review-table` — defined in the web templates `docgen/templates/*.md.j2`.

## ⚠️ Important Notes

- These are **safety-critical documents**
- Always refer to the **latest approved version**
- All AI-generated content **must be reviewed by a qualified person** before approval
- Do **not** operate equipment without proper training and authorisation
- Never defeat or bypass safety systems

## 📞 Contacts

- **Supervisor:** Chris Betters
- **Safety Officer:** [Insert details]
- **Emergency Services:** 000
- **University Security:** [Insert number]

## 📄 License

These safety documents are provided for the safe operation of laboratory equipment. Unauthorised modification or use may compromise safety. All documents should be reviewed and approved by appropriate safety personnel before implementation.

---

**School of Physics | University of Sydney | SAIL Laboratory**
