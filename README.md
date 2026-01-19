# SAIL Laboratory Safety Documentation

GitHub Pages site for laboratory safety documentation including Risk Assessments and Safe Work Procedures.

## 📁 Repository Structure

```
filesghpages/
├── index.md                           # Home page with document lists
├── laser-safety-guide.md              # Class 4 laser safety guide
│
├── risk-assessments/                  # Risk Assessment documents
│   └── bambu-h2d.md                  # Bambu H2D Risk Assessment
│
├── safe-work-procedures/              # Safe Work Procedure documents
│   └── bambu-h2d.md                  # Bambu H2D SWP
│
├── templates/                         # Templates for new documents
│   ├── README.md                     # Template usage guide
│   ├── risk-assessment-template.md   # RA template
│   └── safe-work-procedure-template.md # SWP template
│
├── _layouts/                          # Jekyll layouts
│   ├── default.html                  # Main layout with navigation
│   └── document.html                 # Document-specific layout
│
├── assets/                            # CSS and other assets
│   └── css/
│       └── style.css                 # Custom styling
│
└── _config.yml                        # Jekyll configuration
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

### Adding a New Risk Assessment

1. Copy the template:
   ```bash
   cp templates/risk-assessment-template.md risk-assessments/[equipment-name].md
   ```

2. Edit the new file and replace all `[placeholders]` with your information

3. Update the permalink:
   ```yaml
   permalink: /risk-assessments/[equipment-name]/
   ```

4. Add the document to `index.md` under the Risk Assessments section

### Adding a New Safe Work Procedure

1. Copy the template:
   ```bash
   cp templates/safe-work-procedure-template.md safe-work-procedures/[equipment-name].md
   ```

2. Edit the new file and replace all `[placeholders]` with your information

3. Update the permalink:
   ```yaml
   permalink: /safe-work-procedures/[equipment-name]/
   ```

4. Add the document to `index.md` under the Safe Work Procedures section

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
