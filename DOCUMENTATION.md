# Auto-Population Documentation

## How the Index Page Auto-Populates

The front page (`index.md`) automatically displays all Risk Assessments and Safe Work Procedures without manual editing. This is achieved through Jekyll's collection system.

### How It Works

1. **Jekyll Collections**: The site uses two collections defined in `_config.yml`:
   - `_risk_assessments/` - All risk assessment documents
   - `_safe_work_procedures/` - All safe work procedure documents

2. **Automatic Detection**: Jekyll automatically finds all markdown files in these directories

3. **Front Matter Fields**: Each document's YAML front matter includes metadata that appears on the index page

4. **Liquid Templating**: The index page uses Liquid code to loop through collections and display cards

### Required Front Matter Fields

For a document to appear correctly on the index page, include these fields in the YAML front matter:

#### Risk Assessments

```yaml
---
layout: document
title: Risk Assessment - [Equipment Name]
doc_type: Risk Assessment
status: Approved  # or "Draft"
permalink: /risk-assessments/equipment-slug/
equipment_name: "[Equipment Name]"  # Required for card title
reference: "SAIL-RA-EQUIPMENT-XXX"  # Required for display
version: "1.0"  # Required for display
description: "[Brief description for card]"  # Optional but recommended
key_hazards: "[Comma-separated hazards]"  # Optional but recommended
---
```

#### Safe Work Procedures

```yaml
---
layout: document
title: Safe Work Procedure - [Equipment Name]
doc_type: Safe Work Procedure
status: Approved  # or "Draft"
permalink: /safe-work-procedures/equipment-slug/
equipment_name: "[Equipment Name]"  # Required for card title
reference: "SAIL-SWP-EQUIPMENT-XXX"  # Required for display
version: "1.0"  # Required for display
description: "[Brief description for card]"  # Optional but recommended
includes: "[What the procedure includes]"  # Optional but recommended
---
```

### Document Status and Ordering

**Status Sorting:**
- Approved documents appear first
- Draft documents appear after approved ones
- Within each status group, documents are sorted alphabetically by `equipment_name`

**Valid Status Values:**
- `Approved` - Fully approved and ready for use
- `Draft` - Work in progress or under review

### Adding a New Document

1. **Copy the template:**
   ```bash
   cp _templates/risk-assessment-template.md _risk_assessments/my-equipment.md
   # or
   cp _templates/safe-work-procedure-template.md _safe_work_procedures/my-equipment.md
   ```

2. **Update the front matter:**
   - Change `equipment_name` to the actual equipment name
   - Update `reference` with the correct document number
   - Fill in `description` and `key_hazards` (or `includes` for SWPs)
   - Update `permalink` to match the filename
   - Set `status` to "Draft" initially

3. **Complete the document content:**
   - Fill in all sections
   - Replace all `[placeholder text]`
   - Follow the template structure

4. **The document will automatically appear on the index page** when you commit and push

5. **Change status to "Approved"** when the document is reviewed and approved

### File Naming Convention

**Files should be named:**
- Lowercase
- Hyphen-separated
- Match the permalink
- Example: `bambu-h2d.md` for `/risk-assessments/bambu-h2d/`

### Testing Locally

```bash
# Start Jekyll server
bundle exec jekyll serve

# View at http://localhost:4000/SAIL-RA-SWP/
```

The index page will automatically show all documents in the collections.

### Troubleshooting

**Document not appearing?**
1. Check the file is in the correct directory (`_risk_assessments/` or `_safe_work_procedures/`)
2. Verify the front matter has valid YAML syntax (proper indentation, quotes)
3. Ensure required fields are present: `equipment_name`, `reference`, `version`, `status`
4. Check that `status` is exactly "Approved" or "Draft" (case-sensitive)
5. Restart Jekyll server: `Ctrl+C` then `bundle exec jekyll serve`

**Document showing but looks wrong?**
1. Verify `equipment_name` is set (used for card title)
2. Check `description` and `key_hazards`/`includes` are filled in
3. Ensure `reference` and `version` are correct

**Sorting wrong?**
- Documents are sorted by status (Approved first) then alphabetically by `equipment_name`
- Check `equipment_name` spelling if order seems wrong

### No Manual Index Updates Needed

**You never need to edit `index.md` to add documents!**

Just create the markdown file in the appropriate collection folder with correct front matter, and it will automatically appear.

### Example: Adding CMS 3SAE Documentation

1. Create files:
   ```bash
   touch _risk_assessments/3sae-cms.md
   touch _safe_work_procedures/3sae-cms.md
   ```

2. Add front matter to `_risk_assessments/3sae-cms.md`:
   ```yaml
   ---
   layout: document
   title: Risk Assessment - CMS 3SAE Electron Microscope
   doc_type: Risk Assessment
   status: Draft
   permalink: /risk-assessments/3sae-cms/
   equipment_name: "CMS 3SAE Electron Microscope"
   reference: "SAIL-RA-3SAE-CMS-001"
   version: "1.0"
   description: "Risk assessment for the CMS 3SAE scanning electron microscope covering electron beam hazards, X-ray radiation, vacuum systems, and chemical safety."
   key_hazards: "X-ray radiation, electron beam, vacuum hazards, hazardous chemicals"
   metadata:
     reference: SAIL-RA-3SAE-CMS-001
     title: CMS 3SAE Electron Microscope
     version: "1.0"
     issue_date: February 2026
     prepared_by: Chris Betters
     supervisors: Chris Betters, Sergio Leon-Saval
     review_date: February 2027
   ---
   ```

3. Complete the document content

4. Commit and push - document automatically appears on index page!

### Benefits

✅ No manual index maintenance
✅ Consistent formatting
✅ Automatic sorting (Approved first, then alphabetical)
✅ Easy to add new documents
✅ Reduces errors and omissions
✅ Always up-to-date

### Related Files

- `/index.md` - Front page with auto-population code
- `/_config.yml` - Collection definitions
- `/_templates/risk-assessment-template.md` - RA template with all required fields
- `/_templates/safe-work-procedure-template.md` - SWP template with all required fields
