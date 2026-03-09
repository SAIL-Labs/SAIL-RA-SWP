# SAIL Laboratory Safety Documentation

GitHub Pages site for laboratory safety documentation including Risk Assessments and Safe Work Procedures.

## 📁 Repository Structure

```
SAIL-RA-SWP/
├── index.md                           # Home page with auto-populating document lists
├── laser-safety-guide.md              # Class 4 laser safety guide
├── DOCUMENTATION.md                   # Auto-population documentation
├── CLAUDE_PROMPT.md                   # User prompts for Claude assistance
├── SYSTEM_PROMPTS.md                  # System prompts for Claude Projects/API
│
├── _risk_assessments/                 # Risk Assessment documents (auto-indexed)
│   ├── bambu-h2d.md                  # Bambu H2D Risk Assessment
│   └── 3sae-cms.md                   # 3SAE CMS Risk Assessment
│
├── _safe_work_procedures/             # Safe Work Procedure documents (auto-indexed)
│   ├── bambu-h2d.md                  # Bambu H2D SWP
│   └── 3sae-cms.md                   # 3SAE CMS SWP
│
├── _templates/                        # Templates for new documents
│   ├── README.md                     # Template usage guide
│   ├── risk-assessment-template.md   # RA template
│   └── safe-work-procedure-template.md # SWP template
│
├── .github/                           # GitHub templates and guides
│   ├── ISSUE_TEMPLATE/               # Issue templates
│   │   ├── new-equipment-documentation.md
│   │   ├── document-review.md
│   │   ├── safety-concern.md
│   │   ├── website-improvement.md
│   │   └── config.yml
│   ├── pull_request_template.md      # PR template
│   └── CONTRIBUTING.md               # Contribution guide
│
├── _layouts/                          # Jekyll layouts
│   ├── default.html                  # Main layout with navigation
│   └── document.html                 # Document-specific layout
│
├── assets/                            # CSS and other assets
│   └── css/
│       └── style.css                 # Custom styling
│
└── _config.yml                        # Jekyll configuration with collections
```

## 🚀 Viewing the Site

Visit the published site at: `https://[your-username].github.io/[repository-name]/`

Or run locally:

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000 in your browser.

## 📝 Adding New Documents

### ✨ Auto-Population Feature

**The index page automatically populates with new documents!** You no longer need to manually edit `index.md` to add new Risk Assessments or Safe Work Procedures.

Just create a document in the appropriate collection folder with the required front matter fields, and it will automatically appear on the front page.

For detailed information, see [DOCUMENTATION.md](DOCUMENTATION.md)

### Adding a New Risk Assessment

1. Copy the template:
   ```bash
   cp _templates/risk-assessment-template.md _risk_assessments/[equipment-name].md
   ```

2. Edit the new file and update the front matter:
   ```yaml
   equipment_name: "[Equipment Name]"
   reference: "SAIL-RA-EQUIPMENT-XXX"
   version: "1.0"
   status: "Draft"  # Change to "Approved" when ready
   description: "[Brief description for the index card]"
   key_hazards: "[Main hazards]"
   permalink: /risk-assessments/[equipment-name]/
   ```

3. Replace all `[placeholders]` with your information

4. **That's it!** The document will automatically appear on the index page when you commit and push

### Adding a New Safe Work Procedure

1. Copy the template:
   ```bash
   cp _templates/safe-work-procedure-template.md _safe_work_procedures/[equipment-name].md
   ```

2. Edit the new file and update the front matter:
   ```yaml
   equipment_name: "[Equipment Name]"
   reference: "SAIL-SWP-EQUIPMENT-XXX"
   version: "1.0"
   status: "Draft"  # Change to "Approved" when ready
   description: "[Brief description for the index card]"
   includes: "[What the procedure covers]"
   permalink: /safe-work-procedures/[equipment-name]/
   ```

3. Replace all `[placeholders]` with your information

4. **That's it!** The document will automatically appear on the index page when you commit and push

### 🤖 Automated AI Document Generation (Recommended)

The fastest way to create new documents is via the GitHub Issues workflow:

1. **Open an issue** using the "New Equipment Documentation" template — fill in equipment name, manufacturer, location, hazards, PPE, and the equipment slug (e.g., `fume-hood`)
2. **A lab member with write access** reviews the issue and comments `/generate-docs`
3. **GitHub Actions** calls the Claude AI API automatically and opens a **draft PR** containing both the RA and SWP

The PR links back to the issue and includes a review checklist. Once the documents have been reviewed and all placeholder values verified against manufacturer specs, change `status: Draft` to `status: Approved` in the front matter and merge.

**One-time setup required:** Add `ANTHROPIC_API_KEY` to the repository's GitHub Actions secrets (Settings → Secrets and variables → Actions → New repository secret). Contact the repository owner if you need access.

**Important:** All AI-generated content must be reviewed by a qualified person. Never approve documents without verifying technical specifications against manufacturer documentation.

### Manually Using Claude AI to Fill Templates

You can also use Claude interactively. See:
- **[SYSTEM_PROMPTS.md](SYSTEM_PROMPTS.md)** - System prompts for Claude Projects or API integration

These prompts guide Claude to:
- Generate equipment-specific Risk Assessments with proper hazard analysis
- Create detailed Safe Work Procedures with step-by-step instructions
- Review documents for completeness and compliance
- Use Australian standards and terminology
- Follow the SAIL template format exactly

### Template Structure

Each document template includes:

**Risk Assessment Template:**
- Document metadata (reference number, version, dates)
- Critical safety warnings
- Hazard identification tables
- Risk ratings and controls
- Emergency procedures
- Review schedule

**Safe Work Procedure Template:**
- Document metadata
- Required resources and PPE
- Step-by-step operating instructions
- Pre-operation safety checks
- Emergency shutdown procedures
- Cleanup and waste disposal
- Competency requirements and sign-off sheet

## 📋 Document Metadata

Each document has YAML front matter with metadata:

```yaml
---
layout: document
title: [Document Title]
doc_type: [Risk Assessment or Safe Work Procedure]
status: [draft, approved, or archived]
permalink: /[category]/[document-name]/
metadata:
  reference: SAIL-[TYPE]-[EQUIPMENT]-XXX
  title: [Full Descriptive Title]
  version: "1.0"
  issue_date: [Month Year]
  prepared_by: [Your Name]
  supervisors: [Supervisor Names]
  review_date: [Month Year]
critical_warning: |
  [Critical safety information displayed prominently]
related_docs:
  - title: [Related Document]
    url: /[path]/
    description: [Brief description]
show_review: true
---
```

### Reference Number Format

- `SAIL` = SAIL Laboratory
- `RA` = Risk Assessment
- `SWP` = Safe Work Procedure
- `[EQUIPMENT]` = Short equipment identifier (e.g., BAMBU-H2D, LASER-001)
- `XXX` = Sequential number (001, 002, etc.)

**Examples:**
- `SAIL-RA-BAMBU-H2D-001` - First Bambu H2D Risk Assessment
- `SAIL-SWP-BAMBU-H2D-001` - First Bambu H2D Safe Work Procedure

## 🎨 Styling

The site uses custom CSS (`assets/css/style.css`) with:

- Blue headers (RGB 203, 216, 240) matching LaTeX/Word templates
- Professional table formatting
- Color-coded warning and info boxes
- Document metadata badges
- Print-friendly styles
- Responsive design for mobile/tablet

### Warning Boxes

```html
<div class="danger-box">
  <h3>⚠️ CRITICAL WARNING ⚠️</h3>
  <p>Critical safety information</p>
</div>

<div class="warning-box">
  <h3>⚠️ Warning</h3>
  <p>Important safety information</p>
</div>

<div class="info-box">
  <h3>ℹ️ Information</h3>
  <p>Helpful information</p>
</div>
```

## 📤 Publishing to GitHub Pages

1. Push this repository to GitHub
2. Go to repository Settings → Pages
3. Under "Source", select the branch (usually `main`)
4. Save and wait a few minutes
5. Your site will be available at `https://[username].github.io/[repository-name]/`

## 🔧 Customization

### Update Contact Information

Edit the emergency contacts table in `index.md`:

```markdown
| Emergency Type | Contact | Number |
|---------------|---------|---------|
| **Emergency Services** | Fire, Medical, Police | **000** |
| **Supervisor** | Chris Betters | [Insert number] |
```

### Update Navigation

Edit `_layouts/default.html` to modify the navigation menu:

```html
<nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/#risk-assessments">Risk Assessments</a></li>
    <li><a href="/#safe-work-procedures-swps">Safe Work Procedures</a></li>
    <li><a href="/laser-safety-guide">Resources</a></li>
  </ul>
</nav>
```

### Change Colors

Edit color variables in `assets/css/style.css`:

```css
:root {
  --header-blue: rgb(203, 216, 240);
  --text-color: #333;
  --border-color: #000;
}
```

## 📋 Document Control

All safety documents must be reviewed:

- **Annually** at minimum
- After any incident or near-miss
- When procedures change
- When equipment is modified
- When new hazards are identified

Update the `review_date` in document front matter when reviewed.

### Document Statuses

- `draft` - Work in progress, not yet approved
- `approved` - Reviewed and approved for use
- `archived` - Superseded by newer version

## ✅ Document Workflow

1. **Create** new document from template
2. **Complete** all sections, replacing placeholders
3. **Consult** with stakeholders (users, safety officer, etc.)
4. **Review** for accuracy and completeness
5. **Approve** by supervisor and safety officer
6. **Publish** by updating status to "approved"
7. **Add** to index.md document list
8. **Train** all users on the new/updated procedure
9. **Display** near relevant equipment
10. **Review** annually or as needed

## ⚠️ Important Notes

- These are **safety-critical documents**
- Always refer to the **latest approved version**
- Contact supervisor or safety officer with any questions
- Do **not** operate equipment without proper training and authorization
- Complete all mandatory pre-operation safety checks
- Never defeat or bypass safety systems

## 📞 Contacts

- **Supervisor:** Chris Betters
- **Safety Officer:** [Insert details]
- **Emergency Services:** 000
- **University Security:** [Insert number]

## 🔴 Current Equipment

### Bambu Lab H2D Laser Edition

**CLASS 4 LASER EQUIPMENT** - Most hazardous laser classification

Documents available:
- [Risk Assessment](risk-assessments/bambu-h2d.md) (SAIL-RA-BAMBU-H2D-001)
- [Safe Work Procedure](safe-work-procedures/bambu-h2d.md) (SAIL-SWP-BAMBU-H2D-001)
- [Laser Safety Guide](laser-safety-guide.md)

**Mandatory training and authorization required before use.**

## 📄 License

These safety documents are provided for the safe operation of laboratory equipment. Unauthorized modification or use may compromise safety. All documents should be reviewed and approved by appropriate safety personnel before implementation.

---

**School of Physics | University of Sydney | SAIL Laboratory**
