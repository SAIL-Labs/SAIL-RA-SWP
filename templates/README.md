---
layout: default
title: Safety Documentation Templates
permalink: /templates/
---

# Safety Documentation Templates

This page provides templates for creating new Risk Assessments and Safe Work Procedures for laboratory equipment and processes.

---

## Available Templates

### [Risk Assessment Template](risk-assessment-template/)

Use this template to create a comprehensive risk assessment for new equipment or processes. The template includes:

- Metadata and document control information
- Hazard identification sections
- Risk rating methodology
- Control measures
- Emergency procedures
- Review schedule

**When to use:** Before introducing any new equipment, process, or significant modification to existing procedures.

<a href="risk-assessment-template/" class="metadata-badge">View Risk Assessment Template →</a>

---

### [Safe Work Procedure Template](safe-work-procedure-template/)

Use this template to create detailed step-by-step operating procedures. The template includes:

- Pre-operation safety checks
- Required resources and PPE
- Step-by-step operating instructions
- Emergency shutdown procedures
- Cleanup and waste disposal
- Competency requirements and sign-off sheet

**When to use:** For all equipment and processes identified in risk assessments requiring formal operating procedures.

<a href="safe-work-procedure-template/" class="metadata-badge">View Safe Work Procedure Template →</a>

---

## How to Use These Templates

### 1. Download or Copy the Template

- Navigate to the template you need (links above)
- Copy the markdown content
- Create a new file in the appropriate directory:
  - Risk Assessments: `risk-assessments/[equipment-name].md`
  - Safe Work Procedures: `safe-work-procedures/[equipment-name].md`

### 2. Complete the Template

Replace all placeholder text (shown in `[square brackets]`) with your specific information:

- `[Equipment Name]` → Actual equipment name
- `[equipment-slug]` → URL-friendly name (e.g., "bambu-h2d")
- `[Your Name]` → Your actual name
- `[Month Year]` → Actual dates
- All other bracketed placeholders throughout the document

### 3. Customize for Your Equipment

- Add or remove tasks/hazards as needed
- Expand sections relevant to your specific equipment
- Include equipment-specific warnings and procedures
- Add photos or diagrams if helpful

### 4. Consult with Stakeholders

Before finalizing your document, consult with:

- Equipment users
- Safety officer
- Laboratory manager
- Subject matter experts
- Manufacturer documentation

### 5. Review and Approval

- Submit completed document to supervisor for review
- Address any feedback or required changes
- Obtain formal approval from safety officer
- Update document status from "draft" to "approved"

### 6. Implementation

Once approved:

- Add the document to the main [index page](/)
- Display near the relevant equipment
- Provide training to all users
- Maintain authorised users list
- Schedule annual review

---

## Template Fields Explanation

### Metadata Section

The YAML front matter at the top of each template contains important metadata:

```yaml
metadata:
  reference: SAIL-[TYPE]-[EQUIPMENT]-XXX
  title: [Full descriptive title]
  version: "1.0"
  issue_date: [Month Year]
  prepared_by: [Your Name]
  supervisors: [Supervisor Names]
  review_date: [Month Year]
```

**Reference Number Format:**
- `SAIL` = SAIL Laboratory
- `RA` or `SWP` = Document type
- `[EQUIPMENT]` = Short equipment identifier (e.g., BAMBU-H2D)
- `XXX` = Sequential number (001, 002, etc.)

**Example:** `SAIL-RA-LASER-001` for the first laser-related risk assessment

### Permalink

Set the permalink to match your filename:

```yaml
permalink: /risk-assessments/[equipment-slug]/
```

The `[equipment-slug]` should be:
- All lowercase
- Hyphen-separated
- URL-friendly
- Match your filename (without .md extension)

**Example:** For "Bambu Lab H2D", use `bambu-h2d`

### Status

Documents can have these statuses:

- `draft` - Work in progress, not yet approved
- `approved` - Reviewed and approved for use
- `archived` - Superseded by newer version

---

## Best Practices

### Writing Risk Assessments

1. **Be Specific:** Clearly identify each hazard and its associated harm
2. **Use Risk Matrix:** Consistently apply your organization's risk rating system
3. **Control Hierarchy:** Follow the hierarchy of controls (elimination, substitution, engineering, administrative, PPE)
4. **Be Realistic:** Assess actual risks, not theoretical worst-case scenarios
5. **Involve Users:** Consult people who actually operate the equipment

### Writing Safe Work Procedures

1. **Step-by-Step:** Break complex operations into clear, sequential steps
2. **Safety First:** Lead with pre-operation safety checks
3. **Be Precise:** Don't assume knowledge - specify exactly what to do
4. **Emergency Focus:** Make emergency procedures prominent and clear
5. **Test It:** Have someone unfamiliar with the equipment try following the SWP

### Document Control

1. **Version Control:** Increment version numbers for all changes
2. **Track Changes:** Document what changed in each version
3. **Regular Reviews:** Schedule and complete annual reviews
4. **Accessible:** Make documents easily accessible to all users
5. **Training:** Ensure all users are trained on current procedures

---

## Need Help?

If you need assistance creating safety documentation:

- Contact your supervisor
- Consult with the safety officer
- Review existing approved documents as examples
- Refer to manufacturer safety documentation
- Check relevant Australian Standards

---

<div class="info-box">
<p><strong>Remember:</strong> Safety documentation is only effective if it's used. Make sure your documents are:</p>
<ul>
<li>Clear and easy to understand</li>
<li>Readily accessible to users</li>
<li>Regularly reviewed and updated</li>
<li>Incorporated into training programs</li>
</ul>
</div>
