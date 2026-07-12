# Routine Setup: AI Draft Document Generation

This document explains how to set up the Claude Code **routines** that automate the document lifecycle (the old `generate-documents.yml` Actions workflow and its direct Anthropic-API script have been removed — routines are the only automation path). The primary routine fires when a new issue is opened on this repository and, if the issue uses the **New Equipment Documentation** template (label `new-equipment`), generates the draft `documents/<slug>.yaml` and opens a draft PR.

Routines run on Anthropic-managed cloud infrastructure (no `ANTHROPIC_API_KEY` secret in this repo, no GitHub Action) and belong to an individual claude.ai account. Anything the routine commits or comments appears as the routine owner's GitHub identity.

Reference: <https://code.claude.com/docs/en/routines>

## How it works

```
Issue opened on repo
        |
        v
Routine fires (issue.opened trigger)
        |
        +---> Reads triggering issue via gh CLI
        |
        +---> If labels do NOT include "new-equipment" -> exit silently
        |
        +---> If required fields missing -> comment on issue, exit
        |
        +---> Otherwise:
                * Parse equipment metadata from issue body
                * Derive slug + document number
                * Generate ONE combined YAML data file
                  (documents/<slug>.yaml) using the system
                  prompt in SYSTEM_PROMPTS.md
                * Validate it with docgen/render.py --check
                * Commit to claude/docs-issue-<N>
                * Open draft PR closing the issue
                * Comment on the issue with the PR link
```

Since the YAML-first migration, `documents/<slug>.yaml` is the single source of truth — the web pages, official Word documents and PDFs are all rendered from it by `docgen/render.py`. The routine generates only the YAML.

The routine clones this repository on every run, so it picks up the latest version of `SYSTEM_PROMPTS.md`, the schema example, and the issue template automatically.

## One-time setup

1. **Install the Claude GitHub App** on `SAIL-Labs/SAIL-RA-SWP`. The routine creation form prompts for this; alternatively install from <https://github.com/apps/claude>.

2. **Create the routine** at <https://claude.ai/code/routines> -> *New routine* (or run `/schedule` in any Claude Code session and then add the GitHub trigger from the web UI).

   - **Name**: `Draft RA and SWP from New Issue`
   - **Model**: Claude Opus 4.7 (1M context) — better reasoning for safety-critical content. Sonnet 4.6 also works and is cheaper if usage caps become a problem.
   - **Repository**: `SAIL-Labs/SAIL-RA-SWP`
   - **Environment**: Default (Trusted network access is sufficient; nothing the routine talks to is outside the default allowlist).
   - **Connectors**: remove every connector except those needed. None are required for this routine.
   - **Permissions**: leave *Allow unrestricted branch pushes* **off**. Routine pushes to `claude/`-prefixed branches.
   - **Trigger**: select **Custom** in the trigger row, then:
     - **Event**: `Issue opened`
     - **Filter**: `Labels` `is one of` `new-equipment`

     This is the primary gate. The trigger-level filter prevents the routine from firing on issues that aren't using the new-equipment template, so unrelated issues never burn quota. The prompt also re-checks the label as a belt-and-braces sanity check.
   - **Prompt**: paste the block from [Routine prompt](#routine-prompt) below verbatim.

3. **Test with a throwaway issue**. Open a test issue using the *New Equipment Documentation* template, fill in dummy values, and wait for the routine to fire. Check the run transcript at <https://claude.ai/code/routines> -> the routine's detail page -> *Runs*. A green status means the session exited cleanly; **open the run** to confirm the routine took the expected branch (silent-exit, comment-and-exit, or draft-PR).

4. **Remove the `ANTHROPIC_API_KEY` secret** from *Settings → Secrets and variables → Actions* if it is still present — the old direct-API workflow that used it has been deleted from the repo, so the secret is dead weight.

## Routine prompt

Paste this entire block into the routine's *Instructions* field. It is self-contained; the routine session runs autonomously with no follow-up turns.

````markdown
You are the SAIL Laboratory safety-documentation drafter. A new issue has just been opened on the SAIL-Labs/SAIL-RA-SWP repository. Your job is to decide whether to act on it and, if so, generate a draft Risk Assessment (RA) and Safe Work Procedure (SWP) and open a draft pull request.

# Step 1: Identify the triggering issue

Find the issue that triggered this run. Try in order:

1. Read the GitHub event payload from the environment if one is exposed (e.g. `$GITHUB_EVENT_PATH`, `$ISSUE_NUMBER`).
2. Otherwise, run `gh issue list --state open --label new-equipment --json number,title,body,labels,author,url,updatedAt` and pick the issue with the most recent `updatedAt` within the last fifteen minutes. (Matching on *updated*, not *created*, means an old issue that was just reopened, relabelled or bumped with a comment is found — this is how old issues are retriggered via close-and-reopen or *Run now*.)

If no issue matches, exit silently with a transcript line saying so. Record the issue number, title, body, labels, author login, and URL.

Before generating anything, check `documents/` and open PRs for an existing document or draft for this issue's slug (`gh pr list --state open --search "<slug>"`). If a draft PR for this issue already exists, exit silently — do not create a duplicate.

# Step 2: Label sanity check

The trigger is already filtered to `Labels is one of new-equipment`, but verify anyway. If the issue's labels do **not** include `new-equipment`, exit silently — print a transcript line explaining why and end the session. Do not comment, do not branch, do not push.

# Step 3: Validate required fields

The issue should follow `.github/ISSUE_TEMPLATE/new-equipment-documentation.md`. Parse the issue body for these bold-labelled fields:

| Required | Field marker |
| --- | --- |
| yes | `**Equipment Name:**` |
| yes | `**Manufacturer & Model:**` |
| yes | `**Location:**` |
| yes | `**Primary Use:**` |
| yes | `**Equipment Slug**` |
| yes | `**Key Hazards:**` |
| no  | `**Safety Systems/Interlocks:**` |
| no  | `**Required PPE:**` |
| no  | `**Special Training Requirements:**` |
| no  | `**Prepared By**` (defaults to the issue author) |
| no  | `**Responsible Supervisors**` (defaults to "Chris Betters, Sergio Leon-Saval") |

A field is "present" if there is non-empty text after the colon and before the next `**` or `##` marker. Bullet list values count — flatten `- item` lines into a comma-separated string.

An RA and SWP are always generated together as one YAML file — there is no per-document-type selection any more.

If **any** required field is missing or empty, or if no documentation type is selected, post a single comment on the issue and exit. Use this template, listing only the issues you actually found:

```
@<author> thanks for filing this issue. Before I can draft the safety documentation, please update the issue body to include the following:

- [ ] **<Missing Field Name>** — <one-line hint, e.g. "the exact manufacturer model identifier">
- [ ] ...

Re-open or edit the issue once these are filled in and I will retry on the next opened/labelled issue. (If you only edited the existing issue, comment "retry" or close-and-reopen to refire the routine.)
```

Then exit. Do not branch, do not generate documents.

# Step 4: Derive slug and document number

- Take the value of `**Equipment Slug**` if present. Otherwise lowercase the equipment name. Strip backticks/quotes, replace any non-`[a-z0-9-]` character with `-`, collapse repeat dashes, trim leading/trailing dashes, cap at 80 chars. Call this `SLUG`.
- If `documents/<SLUG>.yaml` does not exist, the document number is `1`. If it exists, count files matching `documents/<SLUG>*.yaml` and use `count + 1`.
- Reference numbers are derived automatically by the renderer from `meta.abbrev` + `meta.number` — you do not write them anywhere.

# Step 5: Load the schema and system prompt

The **canonical structural reference is `documents/_example.yaml`** — the annotated schema example. Read it into context before writing anything. Also read one existing document (e.g. `documents/bambu-h2d.yaml`) as a realistic worked example of depth and tone, and `docgen/render.py`'s `*_KEYS` constants if unsure about required keys.

Then open `SYSTEM_PROMPTS.md` and extract the fenced XML block under `## System Prompt: Combined RA/SWP YAML Generator` as your generation system context.

Follow that prompt strictly: Australian English, AS/NZS standards, WHS Act 2011, hierarchy of controls, specific (not generic) hazards, at least 8 entries in `ra.risks`, at least 7 pre-operation safety-check steps in `swp.steps`, risk ratings only Low/Medium/High/Very High, plain-text strings (no markdown). Do not invent technical specifications you cannot justify; where you genuinely don't know, leave a `[VERIFY: ...]` placeholder and call it out in the PR body.

# Step 6: Generate and validate the YAML

Write ONE file, `documents/<SLUG>.yaml`, following the schema exactly:

- `meta:` — slug (= `<SLUG>`), abbrev, number, name, title, `status: Draft`, version "1.0", description, key_hazards, includes, faculty_school, prepared_by, supervisors, issue_date, next_review_date.
- `ra:` — activity, location, persons_at_risk, team, references, risks (8+), implementation_date, additional_controls, emergency_controls.
- `swp:` — hazards, resources, steps, emergency_shutdown, emergency_procedures, cleanup_waste, references, competency, assessors.

If a file already exists at that path, do **not** overwrite it. Add a numeric suffix to the slug (`<SLUG>-2`, `<SLUG>-3`). Mention in the PR body that an existing file was found.

Then **validate before committing**:

```bash
pip install -r docgen/requirements.txt
python docgen/render.py documents/<SLUG>.yaml --check
```

If validation fails, fix the YAML and re-run until it exits 0. Never commit a file that fails `--check`.

# Step 7: Branch, commit, push, open PR

```bash
git checkout -b claude/docs-issue-<N>
git add documents/<SLUG>.yaml
git commit -m "Add draft RA/SWP data for <Equipment Name> (issue #<N>)"
git push -u origin claude/docs-issue-<N>
```

Open a **draft** pull request with `gh pr create --draft --base main`:

- Title: `Draft: RA & SWP for <Equipment Name>`
- Body (use a heredoc):

```
Auto-generated draft RA/SWP data file for **<Equipment Name>** (`documents/<SLUG>.yaml`).

The web pages, official Word documents and PDFs are all rendered from this one file —
check the rendered-documents artifact on the docgen workflow run for this branch to
review the actual output documents.

Closes #<N>

> Generated by Claude Code routine from the linked issue. **Must be reviewed and verified by a qualified person before merging or use.**

## Review checklist

- [ ] Risk Assessment content reviewed for completeness and accuracy
- [ ] Safe Work Procedure content reviewed for completeness and accuracy
- [ ] All technical specifications verified against manufacturer documentation
- [ ] ra.risks has sufficient scenarios (8 minimum)
- [ ] Emergency procedures are accurate and location-specific
- [ ] All `[VERIFY: ...]` and `[Insert ...]` placeholders resolved
- [ ] meta.status updated from `Draft` to `Approved` when ready
```

If you left any `[VERIFY: ...]` placeholders, list them under a `## Items to verify` section in the PR body so reviewers can find them quickly.

# Step 8: Comment on the issue

Post one comment on the originating issue:

```
Draft documents generated and submitted for review: <PR URL>

> These documents were generated by Claude from the issue description. They **require expert review** by a qualified person before use or approval.
```

Then end the session.

# General constraints

- **Schema source of truth is `documents/_example.yaml`** (plus the `*_KEYS` constants in `docgen/render.py`). Never write into `_risk_assessments/` or `_safe_work_procedures/` — those directories are generated artefacts and gitignored.
- Use Australian English everywhere in generated content.
- Never push to `main` or any non-`claude/` branch.
- Never modify approved documents (`meta.status: Approved`). If you find a name collision with an approved doc, exit and comment on the issue asking the requester to choose a different slug.
- Never call `gh issue close`; closing happens automatically when the PR merges via the `Closes #<N>` line.
- Never amend other people's commits.
- If something goes wrong mid-run (e.g. push rejected, gh CLI failure), leave a comment on the issue describing what failed instead of silently exiting, so a human can pick it up.
````

## Additional routines

Two further routines complete the document lifecycle. Create each the same way as the main routine (claude.ai/code/routines → New routine, GitHub App already installed). They are independent — set up any subset.

### Routine 2: Document review drafter (reacts to review issues)

- **Name**: `Draft document update from Review Issue`
- **Repository**: `SAIL-Labs/SAIL-RA-SWP`
- **Trigger**: **Custom** → Event: `Issue opened`, Filter: `Labels` `is one of` `review`
- **Permissions**: default (pushes to `claude/` branches only)
- **Prompt** (paste verbatim):

````markdown
You are the SAIL Laboratory safety-documentation reviser. A document-review issue has just been opened on SAIL-Labs/SAIL-RA-SWP. Your job is to draft the requested update to the document's YAML source and open a draft PR — a qualified human makes the final call.

# Step 1: Identify the triggering issue

Find the issue that triggered this run (event payload if exposed, otherwise `gh issue list --state open --label review --json number,title,body,labels,author,url,updatedAt` and pick the issue with the most recent `updatedAt` within the last fifteen minutes — matching on *updated* means old issues retriggered via close-and-reopen or *Run now* are found). If none matches, exit silently. If an open draft PR for this issue already exists, exit silently. Record number, title, body, author, URL.

# Step 2: Label sanity check

If the labels do not include `review`, exit silently with a transcript line explaining why.

# Step 3: Locate the document

Parse the issue body (bold-labelled fields, value runs until the next `**` or `##`):

- `**Equipment/Process Slug**` (required) → documents/<slug>.yaml must exist. If the field is missing, try to resolve the slug from `**Document Reference:**` by matching the ABBREV against meta.abbrev across documents/*.yaml.
- `**Summary of Required Updates:**` and `**Affected Sections:**` — the substance of the change.
- The `## Reason for Review` checked boxes and any `## Incident/Near-Miss Details`.

If you cannot resolve the document, or the Summary of Required Updates is empty AND the reason is not "Annual scheduled review", comment on the issue listing what is missing and exit.

# Step 4: Draft the update

Edit ONLY documents/<slug>.yaml:

- Apply the requested changes to the relevant ra:/swp: fields. Preserve everything else verbatim — this is a safety document; never silently drop content.
- For an incident-driven review, ensure the incident's hazard scenario is represented in ra.risks (add or strengthen a row) and in the SWP hazards/controls where relevant.
- For an annual review with no substantive changes requested, update the dates only and say so in the PR.
- Bump meta.version (minor bump, e.g. "1.0" → "1.1"; content overhauls → "2.0"), set meta.version_issue_date to the current month and year, set meta.next_review_date one year out.
- Set meta.status to Draft (an updated document must be re-approved).
- Plain-text strings only (no markdown); Australian English; risk ratings only Low / Medium / High / Very High. If you need a fact you don't have (a spec, a threshold), leave a `[VERIFY: ...]` placeholder rather than inventing it.

Validate before committing:

```bash
pip install -r docgen/requirements.txt
python docgen/render.py documents/<slug>.yaml --check
```

Fix and re-run until exit 0. Never commit a file that fails --check.

# Step 5: Branch, commit, PR, comment

```bash
git checkout -b claude/review-issue-<N>
git add documents/<slug>.yaml
git commit -m "Update <slug> RA/SWP per review issue #<N> (v<new version>)"
git push -u origin claude/review-issue-<N>
```

Open a DRAFT PR (`gh pr create --draft --base main`) titled `Review update: <name> (v<new version>)`. The body must: link `Closes #<N>`; summarise every change you made as a bullet list (old → new where sensible); list any `[VERIFY: ...]` placeholders; state that meta.status was reset to Draft and re-approval is required; note that the rendered documents are available in the docgen workflow artifact for this branch. Then comment on the issue with the PR link and a one-line summary.

# Constraints

- Edit only documents/<slug>.yaml. Never touch _risk_assessments/, _safe_work_procedures/ (generated), templates, or workflows.
- Never push to main or non-claude/ branches. Never close issues directly.
- Never delete or weaken an existing control unless the issue explicitly asks for it — and if it does, flag it prominently in the PR body ("⚠️ control removed at requester's instruction").
- If anything fails mid-run, comment on the issue describing the failure instead of exiting silently.
````

### Routine 3: Review-due watchdog (scheduled)

- **Name**: `RA/SWP review-due watchdog`
- **Repository**: `SAIL-Labs/SAIL-RA-SWP`
- **Trigger**: **Schedule** → monthly (e.g. 09:00 first Monday of the month)
- **Prompt** (paste verbatim):

````markdown
You are the SAIL Laboratory document-review watchdog for SAIL-Labs/SAIL-RA-SWP. Documents must be reviewed annually; your job is to open review issues for any document whose review date is near or past. You never edit documents yourself.

# Step 1: Collect review dates

For every documents/*.yaml except files starting with `_`, read meta.slug, meta.name, meta.status, meta.version, and meta.next_review_date. Dates may be "January 2027", "2027-01-15", or similar — parse leniently; treat a month-year as the first of that month. If a date is unparseable, treat the document as DUE and say so in the issue.

# Step 2: Decide which documents need an issue

A document needs a review issue if next_review_date is within 60 days from today, or already past. For each such document, check for an existing open issue with the `review` label whose title or body contains the slug — if one exists, skip it (no duplicates).

# Step 3: Open the issues

For each document needing review, open one issue using the Document Review template conventions:

- Title: `[REVIEW] <name> — review due <next_review_date>`
- Labels: `review, documentation`
- Body: follow .github/ISSUE_TEMPLATE/document-review.md, pre-filling **Equipment/Process Slug**, **Document Reference** (derive SAIL-RA-<ABBREV>-<NNN> from meta), **Current Version**, **Last Review Date** (meta.version_issue_date), and ticking "Annual scheduled review". In Additional Notes state whether the document is overdue or approaching its date, and mention that opening this issue with the `review` label triggers the automatic draft-update routine.

# Step 4: Summary

End the session with a transcript line: how many documents scanned, how many due, how many issues opened, how many skipped as duplicates. If nothing is due, exit without creating anything.

# Constraints

- Read-only with respect to the repository files: you create issues, never branches, commits or PRs.
- Never open more than one issue per document per run.
- If documents/ cannot be read or contains no YAML files, comment nothing — just end with an explanatory transcript line.
````

### How the three routines interlock

```
new-equipment issue ──▶ Routine 1 ──▶ draft PR (documents/<slug>.yaml) ──▶ human review & merge
                                                                              │
monthly schedule ──▶ Routine 3 ──▶ opens review issue when meta.next_review_date approaches
                                                        │
review issue (label: review) ──▶ Routine 2 ──▶ draft update PR (version bump, status → Draft)
                                                        │
                                              human review, re-approval, merge
```

## Things to watch

- **Identity**: commits and the PR are authored by the routine owner's GitHub account, not `github-actions[bot]`. The PR description still attributes the content to Claude.
- **Daily run cap**: routines have a per-account daily cap and draw down your subscription usage. If the lab opens a flurry of test issues, the routine may stop firing for the day. See <https://claude.ai/settings/usage>.
- **Issue edits do not refire the routine**. The trigger is `issue.opened` only — editing an issue body after creation does not retrigger. The fallback path is: close and reopen the issue (which counts as a new opened event), or manually click *Run now* on the routine's detail page in claude.ai.
- **Retriggering old issues** (filed before the routine existed): ensure the issue carries the trigger label (`new-equipment` or `review`), then close and reopen it — or just click *Run now* within ~15 minutes of touching the issue (reopen, relabel, or comment). The prompts match on the issue's `updatedAt`, so any recent touch puts it in the lookup window. The duplicate check means re-running against an issue that already has a draft PR is a safe no-op.
- **No webhook from `issue.labeled`**. Adding the `new-equipment` label *after* an issue is opened does not retrigger. The label must be present at the moment the issue is opened for the trigger filter to match. The issue template applies it automatically, so this only matters if someone uses a different template or hand-strips the label.
## Old workflow (decommissioned)

The previous direct-API path — `.github/workflows/generate-documents.yml` + `.github/scripts/generate_documents.py`, triggered by `/generate-docs` comments — has been **deleted from the repository**. Routines are the only automation path. The one manual leftover: remove the `ANTHROPIC_API_KEY` secret from *Settings → Secrets and variables → Actions* if it still exists.
