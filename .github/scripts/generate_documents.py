#!/usr/bin/env python3
"""
Generate draft Risk Assessment and Safe Work Procedure markdown files
from a GitHub issue body, using the Claude API with system prompts
sourced from SYSTEM_PROMPTS.md.

Required environment variables:
  ANTHROPIC_API_KEY  - Anthropic API key
  ISSUE_NUMBER       - GitHub issue number
  ISSUE_TITLE        - GitHub issue title
  ISSUE_BODY         - GitHub issue body (markdown)

Writes files:
  _risk_assessments/{slug}.md
  _safe_work_procedures/{slug}.md

Also writes to /tmp for downstream workflow steps:
  /tmp/doc_slug.txt  - equipment slug
  /tmp/doc_name.txt  - equipment name
"""

import os
import re
import sys
import glob

import anthropic


# ---------------------------------------------------------------------------
# Field parsing
# ---------------------------------------------------------------------------

def extract_field(body: str, marker: str) -> str:
    """Extract the value after a markdown bold label like **Field Name:**"""
    idx = body.find(marker)
    if idx == -1:
        return ""

    # Find the colon after the marker text
    colon_idx = body.find(":", idx + len(marker))
    if colon_idx == -1:
        return ""

    start = colon_idx + 1

    # Find where the value ends: next bold label, next ## section, or EOF
    end = len(body)
    for sentinel in ["\n**", "\n##"]:
        pos = body.find(sentinel, start)
        if pos != -1 and pos < end:
            end = pos

    value = body[start:end].strip()

    # Flatten bullet lists into a comma-separated string
    lines = []
    for line in value.split("\n"):
        line = line.strip().lstrip("-* ").strip()
        # Skip checkbox lines and empty lines
        if line and not line.startswith("[ ]") and not line.startswith("[x]"):
            lines.append(line)

    return ", ".join(lines) if lines else ""


def sanitize_slug(raw: str) -> str:
    """Convert any string into a valid lowercase hyphen-separated filename slug."""
    slug = raw.lower().strip()
    slug = re.sub(r"[`'\"]", "", slug)          # Remove quotes/backticks
    slug = re.sub(r"[^a-z0-9-]", "-", slug)    # Replace non-slug chars with dash
    slug = re.sub(r"-+", "-", slug)             # Collapse consecutive dashes
    return slug.strip("-")[:80]                 # Trim leading/trailing dashes, limit length


def slug_to_abbrev(slug: str) -> str:
    """Convert a slug like 'bambu-h2d' to an abbreviation like 'BAMBU-H2D'."""
    return slug.upper()


def get_next_ref_number(slug: str, collection_dir: str) -> str:
    """Return the next available sequential reference number (001, 002, etc.)."""
    target = os.path.join(collection_dir, f"{slug}.md")
    if not os.path.exists(target):
        return "001"
    # File already exists — count variants to determine next number
    existing = glob.glob(os.path.join(collection_dir, f"{slug}*.md"))
    return str(len(existing) + 1).zfill(3)


# ---------------------------------------------------------------------------
# System prompt extraction
# ---------------------------------------------------------------------------

def extract_system_prompt(content: str, section_title: str) -> str:
    """Extract the XML system prompt block from SYSTEM_PROMPTS.md."""
    pattern = rf"## {re.escape(section_title)}\s*\n+```xml\n(.*?)```"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        raise ValueError(f"Could not find section '{section_title}' in SYSTEM_PROMPTS.md")
    return match.group(1).strip()


# ---------------------------------------------------------------------------
# Claude API
# ---------------------------------------------------------------------------

def call_claude(client: anthropic.Anthropic, system_prompt: str, user_message: str) -> str:
    """Call the Claude API and return the generated document text."""
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=16000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


def strip_preamble(text: str) -> str:
    """Strip any conversational preamble before the YAML front matter."""
    idx = text.find("---")
    if idx == -1:
        return text
    return text[idx:]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    # Read inputs from environment variables set by the workflow
    issue_number = os.environ.get("ISSUE_NUMBER", "0")
    issue_body = os.environ.get("ISSUE_BODY", "")
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")

    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable is not set", file=sys.stderr)
        sys.exit(1)

    if not issue_body:
        print("ERROR: ISSUE_BODY is empty — cannot parse equipment details", file=sys.stderr)
        sys.exit(1)

    # ---- Parse issue body ------------------------------------------------
    equipment_name    = extract_field(issue_body, "**Equipment Name:**")
    manufacturer      = extract_field(issue_body, "**Manufacturer & Model:**")
    location          = extract_field(issue_body, "**Location:**")
    primary_use       = extract_field(issue_body, "**Primary Use:**")
    raw_slug          = extract_field(issue_body, "**Equipment Slug**")
    key_hazards       = extract_field(issue_body, "**Key Hazards:**")
    safety_systems    = extract_field(issue_body, "**Safety Systems/Interlocks:**")
    required_ppe      = extract_field(issue_body, "**Required PPE:**")
    training          = extract_field(issue_body, "**Special Training Requirements:**")

    if not equipment_name:
        print("ERROR: Could not parse Equipment Name from the issue body.", file=sys.stderr)
        print("Make sure the issue uses the new-equipment-documentation template.", file=sys.stderr)
        sys.exit(1)

    # ---- Derive slug and reference numbers --------------------------------
    slug   = sanitize_slug(raw_slug) if raw_slug else sanitize_slug(equipment_name)
    abbrev = slug_to_abbrev(slug)

    ra_num  = get_next_ref_number(slug, "_risk_assessments")
    swp_num = get_next_ref_number(slug, "_safe_work_procedures")

    ra_reference  = f"SAIL-RA-{abbrev}-{ra_num}"
    swp_reference = f"SAIL-SWP-{abbrev}-{swp_num}"

    print(f"Equipment : {equipment_name}")
    print(f"Slug      : {slug}")
    print(f"RA ref    : {ra_reference}")
    print(f"SWP ref   : {swp_reference}")

    # ---- Load system prompts from SYSTEM_PROMPTS.md ----------------------
    prompts_file = "SYSTEM_PROMPTS.md"
    if not os.path.exists(prompts_file):
        print(f"ERROR: {prompts_file} not found. Run from repository root.", file=sys.stderr)
        sys.exit(1)

    with open(prompts_file, "r") as f:
        prompts_content = f.read()

    ra_system_prompt  = extract_system_prompt(prompts_content, "System Prompt: Risk Assessment Generator")
    swp_system_prompt = extract_system_prompt(prompts_content, "System Prompt: Safe Work Procedure Generator")

    # ---- Build equipment context string ----------------------------------
    fields = {
        "Equipment Name":             equipment_name,
        "Manufacturer & Model":       manufacturer,
        "Location in Lab":            location,
        "Primary Use":                primary_use,
        "Key Hazards":                key_hazards,
        "Safety Systems/Interlocks":  safety_systems,
        "Required PPE":               required_ppe,
        "Special Training":           training,
        "File Slug":                  slug,
        "GitHub Issue":               f"#{issue_number}",
    }
    equipment_context = "\n".join(
        f"{k}: {v}" for k, v in fields.items() if v
    )

    client = anthropic.Anthropic(api_key=api_key)

    # ---- Generate Risk Assessment ----------------------------------------
    print("\nGenerating Risk Assessment (this may take a minute)...")
    ra_user_message = f"""Generate a complete Risk Assessment markdown file for the following equipment.

{equipment_context}

CRITICAL REQUIREMENTS:
- Return ONLY the complete markdown file content
- Start immediately with `---` (YAML front matter) — no preamble or explanation
- Use the exact reference number: {ra_reference}
- Set permalink to: /risk-assessments/{slug}/
- Status must be: Draft
- Include at least 8 hazard scenarios in the hazard assessment table
"""
    ra_content = strip_preamble(call_claude(client, ra_system_prompt, ra_user_message))

    # ---- Generate Safe Work Procedure ------------------------------------
    print("Generating Safe Work Procedure (this may take a minute)...")
    swp_user_message = f"""Generate a complete Safe Work Procedure markdown file for the following equipment.

{equipment_context}

CRITICAL REQUIREMENTS:
- Return ONLY the complete markdown file content
- Start immediately with `---` (YAML front matter) — no preamble or explanation
- Use the exact reference number: {swp_reference}
- Set permalink to: /safe-work-procedures/{slug}/
- Status must be: Draft
- Reference the associated Risk Assessment: {ra_reference}
- Include at least 7 mandatory pre-operation safety checks
"""
    swp_content = strip_preamble(call_claude(client, swp_system_prompt, swp_user_message))

    # ---- Write output files ----------------------------------------------
    os.makedirs("_risk_assessments", exist_ok=True)
    os.makedirs("_safe_work_procedures", exist_ok=True)

    ra_path  = f"_risk_assessments/{slug}.md"
    swp_path = f"_safe_work_procedures/{slug}.md"

    with open(ra_path, "w") as f:
        f.write(ra_content)
    print(f"Written: {ra_path}")

    with open(swp_path, "w") as f:
        f.write(swp_content)
    print(f"Written: {swp_path}")

    # ---- Write metadata for downstream workflow steps --------------------
    with open("/tmp/doc_slug.txt", "w") as f:
        f.write(slug)
    with open("/tmp/doc_name.txt", "w") as f:
        f.write(equipment_name)

    print("\nDone. Draft documents ready for review.")


if __name__ == "__main__":
    main()
