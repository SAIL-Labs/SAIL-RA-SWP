---
name: Document Review
about: Schedule or request review of existing safety documentation. Updates are made in the document's YAML source file (documents/<slug>.yaml) — a draft PR with the proposed changes can be generated automatically.
title: '[REVIEW] '
labels: 'review, documentation'
assignees: ''
---

<!--
Reviews are applied to the document's single source file, documents/<slug>.yaml —
the web pages, Word documents and PDFs all regenerate from it. Keep the bold field
labels exactly as they are; they are parsed programmatically.
-->

## Document to Review

**Equipment/Process Slug** *(the documents/<slug>.yaml filename — e.g. `bambu-h2d`)*:

**Document Reference:** (e.g., SAIL-RA-BAMBU-H2D-001)

**Current Version:**

**Last Review Date:**

## Reason for Review

- [ ] Annual scheduled review
- [ ] After incident/near-miss
- [ ] Equipment modification
- [ ] New hazard identified
- [ ] Procedure change
- [ ] User feedback
- [ ] Other:

## Proposed Changes

**Summary of Required Updates:**


**Affected Sections:**
-

## Review Process

**Stakeholders to Consult:**
- [ ] Equipment users
- [ ] Safety officer
- [ ] Supervisor
- [ ] Manufacturer documentation
- [ ] Other:

**Target Completion Date:**

## Incident/Near-Miss Details (if applicable)

**Date:**

**Description:**


**Immediate Actions Taken:**


## Additional Notes

<!--
After the changes are merged, remember: meta.version bumped, meta.version_issue_date
and meta.next_review_date updated, and the REVIEW table on the printed RA completed
by hand at the physical review.
-->
