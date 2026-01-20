# Contributing to SAIL Laboratory Safety Documentation

Thank you for contributing to the SAIL Laboratory Safety Documentation Portal. Safety documentation is critical for protecting laboratory users, so please follow these guidelines carefully.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Creating Safety Documents](#creating-safety-documents)
- [Updating Safety Documents](#updating-safety-documents)
- [Website Improvements](#website-improvements)
- [Review Process](#review-process)
- [Style Guide](#style-guide)

## Code of Conduct

- **Safety First:** Never compromise on safety for convenience or speed
- **Accuracy:** Ensure all information is technically accurate and up-to-date
- **Clarity:** Write clearly for all users, including those new to the equipment
- **Collaboration:** Consult with equipment users and safety officers
- **Respect:** Be professional and constructive in all interactions

## Getting Started

1. **Read Existing Documentation:** Familiarize yourself with approved documents
2. **Review Templates:** Understand the structure in `_templates/`
3. **Check Issues:** See if your contribution relates to an existing issue
4. **Create an Issue:** For new documents or major changes, create an issue first
5. **Fork and Branch:** Work in a feature branch with a descriptive name

### Branch Naming Convention

- `new-doc/equipment-name` - New safety documentation
- `update/doc-reference` - Updates to existing documents
- `fix/issue-description` - Bug fixes
- `feature/description` - Website features
- `review/doc-reference-v2` - Document reviews

## Types of Contributions

### 1. New Safety Documents

**When:** Adding documentation for new equipment or processes

**Process:**
1. Create an issue using "New Equipment Documentation" template
2. Copy the appropriate template from `_templates/`
3. Complete all sections thoroughly
4. Consult with equipment users and safety officer
5. Submit PR when draft is ready for review

**Required Approvals:**
- Equipment users
- Laboratory supervisor
- Safety officer (for high-risk equipment)

### 2. Document Updates

**When:** Annual reviews, incident responses, or procedure changes

**Process:**
1. Create an issue using "Document Review" template
2. Increment version number
3. Document changes clearly
4. Update review dates
5. Submit PR with change summary

**Required Approvals:**
- Laboratory supervisor
- Safety officer (if safety-critical changes)

### 3. Safety Concerns

**When:** Reporting hazards, near-misses, or documentation gaps

**Process:**
1. **Immediate hazards:** Call 000 and notify supervisor directly
2. Create issue using "Safety Concern" template
3. Include all relevant details
4. Tag equipment/lock out if needed
5. Follow up on corrective actions

### 4. Website Improvements

**When:** Fixing bugs, improving UX, or adding features

**Process:**
1. Create issue using "Website Improvement" template
2. Test changes locally
3. Verify print layout
4. Check accessibility
5. Submit PR with screenshots

## Creating Safety Documents

### Step-by-Step Guide

#### 1. Prepare

- [ ] Review manufacturer documentation
- [ ] Consult with equipment users
- [ ] Identify similar equipment for reference
- [ ] List known hazards
- [ ] Understand safety systems

#### 2. Draft Document

- [ ] Copy appropriate template
- [ ] Create file: `_risk_assessments/equipment-slug.md` or `_safe_work_procedures/equipment-slug.md`
- [ ] Set correct permalink
- [ ] Complete metadata section
- [ ] Fill all required sections
- [ ] Replace ALL placeholder text

#### 3. Content Requirements

**Risk Assessments Must Include:**
- Complete hazard identification
- Risk ratings (before and after controls)
- Control measures following hierarchy of controls
- Emergency procedures
- PPE requirements
- Related documents

**Safe Work Procedures Must Include:**
- Pre-operation safety checks
- Step-by-step instructions
- Emergency shutdown procedures
- Cleanup procedures
- Competency requirements
- Sign-off sheet

#### 4. Quality Checks

- [ ] All placeholders `[like this]` replaced
- [ ] Hazards specific to equipment (not generic)
- [ ] Procedures tested with actual equipment
- [ ] Emergency contacts verified
- [ ] Links work correctly
- [ ] Document renders correctly
- [ ] Prints correctly on A4

#### 5. Review

- [ ] Self-review against checklist
- [ ] Peer review by equipment user
- [ ] Supervisor review
- [ ] Safety officer review (if required)
- [ ] Address all feedback
- [ ] Obtain approvals

## Updating Safety Documents

### When to Update

**Mandatory:**
- Annual review date reached
- After any incident or near-miss
- Equipment modification
- New hazard identified
- Procedure change

**Optional:**
- User feedback suggests improvements
- Clarity improvements
- Formatting updates
- Related document updates

### Update Process

1. **Increment Version:**
   - Minor updates: 1.0 → 1.1
   - Major changes: 1.x → 2.0

2. **Track Changes:**
   - Document what changed and why
   - Update issue date
   - Set new review date (typically +1 year)

3. **Review Scope:**
   - Complete review for major changes
   - Targeted review for minor updates
   - Safety officer review if safety-critical

## Website Improvements

### Development Setup

```bash
# Clone repository
git clone [repository-url]
cd SAIL-RA-SWP

# Install Jekyll (if not installed)
gem install bundler jekyll

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# View at http://localhost:4000/SAIL-RA-SWP/
```

### Testing Requirements

Before submitting PR, verify:

1. **Functionality:**
   - [ ] No console errors
   - [ ] All links work
   - [ ] Forms function correctly
   - [ ] Navigation works

2. **Compatibility:**
   - [ ] Chrome/Edge
   - [ ] Firefox
   - [ ] Safari
   - [ ] Mobile browsers

3. **Print Layout:**
   - [ ] Documents print correctly
   - [ ] Page breaks appropriate
   - [ ] Headers/footers correct
   - [ ] A4 paper size

4. **Accessibility:**
   - [ ] Semantic HTML
   - [ ] Alt text on images
   - [ ] Keyboard navigation
   - [ ] Color contrast

## Review Process

### For Contributors

1. **Self-Review:** Complete all checklists
2. **Submit PR:** Use pull request template
3. **Respond to Feedback:** Address reviewer comments promptly
4. **Update as Needed:** Make requested changes
5. **Final Approval:** Wait for all required approvals

### For Reviewers

**Review Checklist:**
- [ ] Content technically accurate
- [ ] Safety requirements complete
- [ ] Procedures clear and unambiguous
- [ ] Hazards properly identified
- [ ] Controls adequate and realistic
- [ ] Emergency procedures clear
- [ ] Formatting consistent
- [ ] Links functional
- [ ] Metadata complete
- [ ] Version control correct

**Approval Authority:**
- Draft documents: Laboratory supervisor
- Approved documents: Safety officer
- Website changes: Repository maintainer

## Style Guide

### Document Writing

**Do:**
- ✅ Use active voice ("Check the interlock")
- ✅ Be specific ("Heat to 350°C")
- ✅ Use numbered steps for procedures
- ✅ Include warnings before steps
- ✅ Define acronyms on first use

**Don't:**
- ❌ Use passive voice ("The interlock should be checked")
- ❌ Be vague ("Heat sufficiently")
- ❌ Mix instructions with explanations
- ❌ Assume prior knowledge
- ❌ Use unexplained jargon

### Formatting

- Use markdown formatting consistently
- Tables for structured data
- Lists for multiple items
- Boxes for warnings/critical info
- Bold for emphasis (sparingly)

### Naming Conventions

**Files:**
- `equipment-name.md` (lowercase, hyphens)
- `bambu-h2d.md` not `Bambu_H2D.md`

**References:**
- `SAIL-RA-EQUIPMENT-001` (uppercase)
- `SAIL-SWP-BAMBU-H2D-001`

**Permalinks:**
- `/risk-assessments/equipment-name/`
- `/safe-work-procedures/equipment-name/`

## Questions?

- Check existing documentation for examples
- Review templates in `_templates/`
- Contact laboratory supervisor
- Create an issue for clarification

---

## Quick Reference

### Creating New Document

```bash
# 1. Create issue (GitHub)
# 2. Copy template
cp _templates/risk-assessment-template.md _risk_assessments/my-equipment.md

# 3. Edit file, replace ALL placeholders
# 4. Test locally
bundle exec jekyll serve

# 5. Create PR
git checkout -b new-doc/my-equipment
git add .
git commit -m "Add risk assessment for My Equipment"
git push origin new-doc/my-equipment
```

### Document Status Flow

```
Draft → Under Review → Approved → Published → [Annual Review] → Updated
```

### Priority Levels

- **P0 Critical:** Safety issues, immediate action required
- **P1 High:** Important safety updates, address within 1 week
- **P2 Medium:** Improvements, address within 1 month
- **P3 Low:** Minor updates, address in next review cycle

---

Thank you for contributing to laboratory safety! 🔬⚗️🛡️
