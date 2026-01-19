# Quick Start Guide

## What Changed?

Your GitHub Pages site has been reorganized with:

1. **Fixed folder structure** - Folders now use underscore prefix (`_risk_assessments`, `_safe_work_procedures`, `_templates`) so Jekyll properly builds them as collections
2. **Professional header with logo placeholders** - Ready for you to add actual logos
3. **Modern landing page** - index.md now has a hero section, card-based layout, and better visual hierarchy

## Current Structure

```
filesghpages/
├── _risk_assessments/          # Risk Assessment documents
│   └── bambu-h2d.md
├── _safe_work_procedures/      # Safe Work Procedure documents
│   └── bambu-h2d.md
├── _templates/                  # Templates for new documents
│   ├── README.md               # Template usage guide
│   ├── risk-assessment-template.md
│   └── safe-work-procedure-template.md
├── _layouts/                    # Jekyll layouts
│   ├── default.html            # Main layout with header/nav/footer
│   └── document.html           # Document-specific layout
├── assets/
│   ├── css/style.css           # Updated with landing page styles
│   ├── sail-logo.pdf           # Your logo (PDF)
│   └── usyd-logo.pdf           # University logo (PDF)
└── index.md                     # Modern landing page
```

## Adding Actual Logos

The header currently has placeholder text. To add your actual logos:

### Option 1: Convert PDFs to Images

```bash
# Convert PDFs to PNG (requires ImageMagick or similar)
convert -density 300 assets/sail-logo.pdf assets/images/sail-logo.png
convert -density 300 assets/usyd-logo.pdf assets/images/usyd-logo.png
```

Then update `_layouts/default.html`:

```html
<div class="logo-left">
  <img src="{{ '/assets/images/usyd-logo.png' | relative_url }}" alt="University of Sydney" style="max-height: 80px;">
</div>
<div class="logo-right">
  <img src="{{ '/assets/images/sail-logo.png' | relative_url }}" alt="SAIL Laboratory" style="max-height: 80px;">
</div>
```

### Option 2: Keep Text Placeholders

The current setup works fine with text - it's clean and professional. You can customize the text in `_layouts/default.html` around line 14-27.

## Testing Locally

```bash
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000

## Adding New Documents

### New Risk Assessment

1. Copy template:
   ```bash
   cp _templates/risk-assessment-template.md _risk_assessments/new-equipment.md
   ```

2. Edit `_risk_assessments/new-equipment.md`:
   - Replace all `[placeholders]` with actual information
   - Update `permalink: /risk-assessments/new-equipment/`

3. Add to `index.md`:
   ```html
   <div class="document-card">
     <h3>Your Equipment Name</h3>
     <div class="card-meta">
       <strong>Reference:</strong> SAIL-RA-XXX-001 | <strong>Version:</strong> 1.0 | <strong>Status:</strong> <span class="metadata-badge status-approved">Approved</span>
     </div>
     <p>Description of the risk assessment...</p>
     <a href="/risk-assessments/new-equipment/" class="cta-button">View Risk Assessment →</a>
   </div>
   ```

### New Safe Work Procedure

Same process, just use the SWP template and folder.

## Key Features

### Landing Page
- **Hero section** with gradient background
- **Card-based layout** for documents (hover effects)
- **Feature grid** for resources and quick reference
- **Responsive design** - works on mobile, tablet, desktop

### Header
- **Three-column layout**: Left logo | Center title | Right logo
- **Navigation bar** with active state highlighting
- **Fully responsive** - stacks on mobile

### Document Cards
- Professional cards with metadata
- Hover animation (lifts up on hover)
- Clear call-to-action buttons
- Easy to add more documents

## Publishing to GitHub Pages

1. Commit all changes:
   ```bash
   git add .
   git commit -m "Reorganized site with collections and modern landing page"
   git push
   ```

2. Enable GitHub Pages:
   - Go to repository Settings → Pages
   - Source: Deploy from branch `main`
   - Save

3. Site will be live at: `https://[username].github.io/[repo-name]/`

## Customization

### Change Colors

Edit `assets/css/style.css`:

```css
:root {
  --header-blue: rgb(203, 216, 240);  /* Header background */
  --text-color: #333;                 /* Main text */
  --link-color: #0066cc;              /* Links and buttons */
}

.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  /* Change gradient colors here */
}
```

### Change Header Title

Edit `_layouts/default.html` around line 19-21:

```html
<div class="header-title">
  <h1>Your Laboratory Name</h1>
  <p class="subtitle">Your Subtitle</p>
</div>
```

## Common Issues

### Collections not building?

Make sure folder names start with underscore:
- ✅ `_risk_assessments/`
- ❌ `risk-assessments/`

### Links not working?

Check `permalink` in frontmatter matches folder structure:
```yaml
permalink: /risk-assessments/document-name/
```

### Styles not loading?

Clear Jekyll cache and rebuild:
```bash
bundle exec jekyll clean
bundle exec jekyll serve
```

## Next Steps

1. Convert your logos to PNG/SVG and add them to the header
2. Add more equipment documents using the templates
3. Customize colors to match your branding
4. Update contact information in index.md
5. Test thoroughly before publishing

---

Need help? Check `README.md` for detailed documentation or `_templates/README.md` for template usage guide.
