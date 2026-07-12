#!/usr/bin/env python3
"""
Generate a draft combined RA/SWP YAML data file from a GitHub issue body,
using the Claude API with the system prompt sourced from SYSTEM_PROMPTS.md.

Since the YAML-first migration, ONE file drives everything: the web pages,
Word documents and PDFs are all rendered from documents/{slug}.yaml by
docgen/render.py. This script writes that file and validates it renders.

Required environment variables:
  ANTHROPIC_API_KEY  - Anthropic API key
  ISSUE_NUMBER       - GitHub issue number
  ISSUE_TITLE        - GitHub issue title
  ISSUE_BODY         - GitHub issue body (markdown)

Writes files:
  documents/{slug}.yaml

Also writes to /tmp for downstream workflow steps:
  /tmp/doc_slug.txt  - equipment slug
  /tmp/doc_name.txt  - equipment name
"""

import glob
import os
import re
import subprocess
import sys

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


def get_next_number(slug: str) -> int:
    """Return the next available sequential document number for this slug."""
    if not os.path.exists(f"documents/{slug}.yaml"):
        return 1
    # File already exists — count variants to determine next number
    return len(glob.glob(f"documents/{slug}*.yaml")) + 1


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
        model="claude-sonnet-5",
        max_tokens=32000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


def strip_to_yaml(text: str) -> str:
    """Strip any conversational preamble or code fences around the YAML body."""
    text = text.strip()
    # Remove a wrapping ```yaml ... ``` / ``` ... ``` fence if present
    fence = re.match(r"^```[a-zA-Z]*\n(.*?)\n?```\s*$", text, re.DOTALL)
    if fence:
        text = fence.group(1).strip()
    # Drop anything before the meta: top-level key
    idx = text.find("meta:")
    if idx > 0:
        text = text[idx:]
    return text + ("\n" if not text.endswith("\n") else "")


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

    # ---- Derive slug and document number ----------------------------------
    slug   = sanitize_slug(raw_slug) if raw_slug else sanitize_slug(equipment_name)
    number = get_next_number(slug)

    print(f"Equipment : {equipment_name}")
    print(f"Slug      : {slug}")
    print(f"Number    : {number:03d}")

    # ---- Load system prompt from SYSTEM_PROMPTS.md ------------------------
    prompts_file = "SYSTEM_PROMPTS.md"
    if not os.path.exists(prompts_file):
        print(f"ERROR: {prompts_file} not found. Run from repository root.", file=sys.stderr)
        sys.exit(1)

    with open(prompts_file, "r") as f:
        prompts_content = f.read()

    system_prompt = extract_system_prompt(
        prompts_content, "Combined RA/SWP YAML Generator")

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
        "Slug (use as meta.slug)":    slug,
        "Number (use as meta.number)": str(number),
        "GitHub Issue":               f"#{issue_number}",
    }
    equipment_context = "\n".join(
        f"{k}: {v}" for k, v in fields.items() if v
    )

    client = anthropic.Anthropic(api_key=api_key)

    # ---- Generate the combined YAML ---------------------------------------
    print("\nGenerating combined RA/SWP YAML (this may take a minute)...")
    user_message = f"""Generate the combined RA/SWP YAML data file for the following equipment.

{equipment_context}

CRITICAL REQUIREMENTS:
- Return ONLY the YAML document — no preamble, no markdown fences
- meta.slug must be exactly: {slug}
- meta.number must be exactly: {number}
- meta.status must be: Draft
- Include at least 8 entries in ra.risks
- Include at least 7 pre-operation safety check steps in swp.steps
"""
    yaml_content = strip_to_yaml(call_claude(client, system_prompt, user_message))

    # ---- Write output file -------------------------------------------------
    os.makedirs("documents", exist_ok=True)
    doc_path = f"documents/{slug}.yaml"
    header = (f"# Generated from GitHub issue #{issue_number} — DRAFT, requires expert review.\n"
              f"# This file is the single source of truth: web pages, Word documents and PDFs\n"
              f"# are all rendered from it by docgen/render.py.\n")
    with open(doc_path, "w") as f:
        f.write(header + yaml_content)
    print(f"Written: {doc_path}")

    # ---- Validate: the file must render cleanly ----------------------------
    print("\nValidating with docgen/render.py --check ...")
    result = subprocess.run(
        [sys.executable, "docgen/render.py", doc_path, "--check"],
        capture_output=True, text=True,
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        print("ERROR: generated YAML failed validation — not opening a PR.", file=sys.stderr)
        sys.exit(1)

    # ---- Write metadata for downstream workflow steps --------------------
    with open("/tmp/doc_slug.txt", "w") as f:
        f.write(slug)
    with open("/tmp/doc_name.txt", "w") as f:
        f.write(equipment_name)

    print("\nDone. Draft document data ready for review.")


if __name__ == "__main__":
    main()
