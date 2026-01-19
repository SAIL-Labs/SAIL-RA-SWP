# SAIL Laboratory Safety Documentation

GitHub Pages site for safety documentation for the Bambu Lab H2D Laser Edition with 10W Class 4 laser module.

## 🔴 CLASS 4 LASER EQUIPMENT

This equipment contains a **CLASS 4 laser** - the most hazardous laser classification. 

**Mandatory training and authorisation required before use.**

## 📚 Available Documents

- **Risk Assessment** (SAIL-RA-BAMBU-H2D-001) - Comprehensive hazard identification and controls
- **Safe Work Procedure** (SAIL-SWP-BAMBU-H2D-001) - Detailed operating procedures
- **Laser Safety Guide** - Essential Class 4 laser safety information

## 🚀 Viewing the Site

Visit the published site at: `https://[your-username].github.io/[repository-name]/`

Or run locally:

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000 in your browser.

## 📝 Editing Documents

All documents are in Markdown format:

- `index.md` - Home page
- `risk-assessment.md` - Risk Assessment
- `swp.md` - Safe Work Procedure
- `laser-safety-guide.md` - Laser Safety Guide

### Document Metadata

Each document has YAML front matter with metadata:

```yaml
---
layout: document
title: Document Title
metadata:
  reference: Document Reference Number
  version: "1.0"
  issue_date: January 2026
  prepared_by: Your Name
  supervisors: Supervisor Names
---
```

## 🎨 Styling

The site uses custom CSS (`assets/css/style.css`) that mimics the LaTeX/Word template styling with:

- Blue headers (RGB 203, 216, 240)
- Professional table formatting
- Warning and danger boxes
- Print-friendly styles
- Responsive design

## 📤 Publishing to GitHub Pages

1. Push this repository to GitHub
2. Go to repository Settings → Pages
3. Under "Source", select the branch (usually `main`)
4. Save and wait a few minutes
5. Your site will be available at `https://[username].github.io/[repository-name]/`

## 🔧 Customisation

### Update Contact Information

Edit the emergency contacts table in `index.md`

### Update Logos

Add your logos to `assets/images/` and update references in `_layouts/default.html`

### Change Colours

Edit colour variables in `assets/css/style.css`:

```css
:root {
  --header-blue: rgb(203, 216, 240);  /* Change this for different header colour */
  --text-color: #333;
  --border-color: #000;
}
```

## 📋 Document Control

All safety documents must be reviewed:

- Annually
- After any incident
- When procedures change
- When equipment is modified

Update the `review_date` in document front matter.

## ⚠️ Important Notes

- These are safety-critical documents
- Always refer to the latest approved version
- Contact supervisor or safety officer with any questions
- Do not operate equipment without proper training and authorisation

## 📞 Contacts

- **Supervisor:** Chris Betters
- **Safety Officer:** [Insert details]
- **Emergency:** 000

## 📄 License

These safety documents are provided for the safe operation of laboratory equipment. 
Unauthorised modification or use may compromise safety.

---

**School of Physics | University of Sydney | SAIL Laboratory**
