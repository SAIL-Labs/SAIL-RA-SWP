# Claude Prompt for Safety Documentation Generation

Use this prompt when asking Claude to help fill in Risk Assessment or Safe Work Procedure templates.

---

## For Risk Assessment Generation

```
I need help creating a Risk Assessment for [EQUIPMENT NAME] using the SAIL Laboratory template format.

EQUIPMENT INFORMATION:
- Equipment name: [Full equipment name and model]
- Manufacturer: [Manufacturer name]
- Primary use: [What the equipment is used for]
- Location: [Where it will be located]
- Manufacturer documentation: [Attach or link to manuals, datasheets, safety documents]

CONTEXT:
- This is for the School of Physics, University of Sydney
- The risk assessment must comply with Australian WHS standards
- It will be used by laboratory staff, research students, and technicians
- Prepared by: [Your name]
- Supervisors: [Supervisor names]

HAZARDS TO CONSIDER:
[List any known hazards or concerns about this equipment, e.g.:]
- High temperature surfaces (specify temperatures)
- Electrical hazards (specify voltage)
- Moving parts
- Chemical exposure
- Radiation (specify type)
- Fire risk
- Noise
- [Any other specific hazards]

SAFETY SYSTEMS:
[Describe existing safety features:]
- Interlocks
- Emergency stops
- Guards/barriers
- Alarms
- Ventilation
- [Other safety features]

REQUIREMENTS:
Please help me complete the Risk Assessment template by:

1. Filling in all metadata (reference number format: SAIL-RA-[EQUIPMENT]-001, dates, etc.)

2. Completing the Activity and Persons at Risk table with:
   - Specific activities/processes for this equipment
   - Who may be at risk
   - Risk assessment team members to consult

3. Identifying relevant Australian Standards and legislation for this equipment type

4. Creating a comprehensive Hazard Assessment Table with:
   - Each task/scenario broken down separately
   - Specific hazards (not generic)
   - Realistic potential harms
   - Existing controls already on the equipment
   - Current risk ratings (using High/Medium/Low/Very High)
   - Additional controls needed to reduce risk
   - Residual risk ratings after controls implemented

5. Completing the Implementation of Additional Controls table with:
   - Specific, actionable control measures
   - Resource requirements
   - Responsible persons
   - Implementation dates
   - RiskWare references where applicable

6. Writing comprehensive emergency procedures covering:
   - Critical safety warnings specific to this equipment
   - Emergency shutdown procedures (step-by-step)
   - Fire emergency response
   - Equipment malfunction response
   - Exposure/injury first aid (specific to hazards)
   - Emergency contacts

IMPORTANT REQUIREMENTS:
- Be specific, not generic (e.g., "350°C nozzle" not "hot surfaces")
- Use Australian terminology and standards
- Follow hierarchy of controls (elimination, substitution, engineering, admin, PPE)
- Consider realistic scenarios, not just worst-case
- Risk ratings should reflect actual likelihood and consequence
- Emergency procedures must be actionable and clear
- Include all necessary PPE and training requirements

Please generate the content section by section, ensuring all [placeholders] are replaced with specific, accurate information for this equipment.
```

---

## For Safe Work Procedure Generation

```
I need help creating a Safe Work Procedure (SWP) for [EQUIPMENT NAME] using the SAIL Laboratory template format.

EQUIPMENT INFORMATION:
- Equipment name: [Full equipment name and model]
- Manufacturer: [Manufacturer name]
- Primary functions: [What operations it performs]
- Location: [Where it will be located]
- Manufacturer documentation: [Attach or link to user manuals, operation guides]
- Associated Risk Assessment: SAIL-RA-[EQUIPMENT]-XXX

CONTEXT:
- This is for the School of Physics, University of Sydney
- The SWP will be used by trained operators (staff and students)
- Must align with the Risk Assessment SAIL-RA-[EQUIPMENT]-XXX
- Prepared by: [Your name]
- Supervisors: [Supervisor names]

OPERATION OVERVIEW:
[Describe how the equipment is typically used:]
- Normal operating procedures
- Typical materials/workpieces processed
- Duration of typical operations
- Frequency of use
- Whether operations can be unattended

HAZARDS (from Risk Assessment):
[List main hazards that the procedure must address:]
- [Hazard 1]
- [Hazard 2]
- [Hazard 3]

SAFETY SYSTEMS:
[Describe safety features that operators must check/use:]
- Interlocks (describe what they protect)
- Emergency stops (location and function)
- Guards/barriers
- Warning alarms
- Ventilation/exhaust systems
- [Other safety features]

REQUIRED PPE:
- [List PPE required]
- [Specify when each PPE item is needed]

REQUIREMENTS:
Please help me complete the Safe Work Procedure template by:

1. Filling in all metadata (reference SAIL-SWP-[EQUIPMENT]-001, dates, etc.)

2. Listing hazards and risk controls from the associated Risk Assessment

3. Detailing all resources required:
   - Complete PPE list with specific types (not just "gloves" but "heat-resistant gloves rated to 200°C")
   - All equipment, materials, and consumables needed
   - Safety equipment that must be present (fire extinguisher type, first aid, etc.)
   - Environmental controls (ventilation, temperature, etc.)

4. Writing comprehensive step-by-step instructions including:

   **Pre-operation safety checks (MANDATORY):**
   - Sign-in procedure
   - Visual inspection steps (what to look for)
   - Safety system testing (exactly how to test each interlock/emergency stop)
   - Ventilation/environmental checks
   - Emergency equipment checks
   - Work area clearance

   **Material preparation:**
   - How to verify materials are approved
   - SDS requirements
   - Material preparation steps

   **Equipment startup:**
   - Exact power-on sequence
   - Initialization steps
   - What to check on displays/interfaces

   **Operation procedures:**
   - Job/program preparation
   - Material loading (safe methods)
   - Starting operation (final checks, start procedure)
   - Monitoring during operation
   - Attendance requirements (must attend vs. can leave)
   - What to watch for during operation

   **Completion and shutdown:**
   - How to know operation is complete
   - Cool-down requirements (temperatures, times)
   - Safe removal of work
   - Cleaning procedures
   - Shutdown steps
   - Sign-out procedure

5. Writing detailed emergency procedures:
   - When to use emergency stop (specific scenarios)
   - How to activate emergency stop (exact location and method)
   - What happens when activated
   - Alternative shutdown if emergency stop fails
   - How to reset after emergency
   - Fire emergency (specific to this equipment)
   - Equipment malfunction response
   - Injury/exposure first aid
   - Who to contact

6. Specifying cleanup and waste disposal:
   - After-use cleaning (what, how, with what materials)
   - Component-specific cleaning
   - Waste types generated
   - How to dispose of each waste type
   - Periodic maintenance cleaning

7. Defining competency requirements:
   - Mandatory training modules (specific topics)
   - Theory assessment criteria
   - Practical assessment tasks
   - Pass marks
   - Ongoing requirements (refresher training, retraining triggers)
   - Record keeping

8. Listing staff approved to assess competence:
   - Who can assess
   - Assessor requirements
   - Assessment process
   - Sign-off procedures

IMPORTANT REQUIREMENTS:
- Instructions must be numbered and sequential
- Each step must be actionable (specific verbs: press, check, verify, etc.)
- Use exact equipment terminology (button names, menu items, etc.)
- Include specific values (temperatures, times, distances)
- Safety-critical steps must be emphasized (NEVER, MUST, MANDATORY)
- Emergency procedures must be unambiguous
- Competency requirements must be measurable
- No generic placeholders - all information must be specific to this equipment

TONE AND STYLE:
- Use active voice ("Press the button" not "The button should be pressed")
- Use imperative mood (commands: "Check the interlock")
- Be direct and concise
- Use bullet points for lists, numbered steps for procedures
- Bold or capitalize critical safety information
- Assume the reader is competent but needs clear guidance

Please generate the SWP content section by section, ensuring:
- All [placeholders] are replaced with equipment-specific information
- Procedures are detailed enough to follow without prior knowledge
- Safety checks are comprehensive and testable
- Emergency procedures are clear and actionable
```

---

## Example Usage

### Starting a conversation with Claude:

**For Risk Assessment:**
```
[Paste the Risk Assessment prompt above]

I'm creating a risk assessment for a [EQUIPMENT]. Here's the information:

EQUIPMENT INFORMATION:
- Equipment name: XYZ Model 5000 Laser Cutter
- Manufacturer: LaserCorp Industries
- Primary use: Cutting and engraving wood, acrylic, and leather
- Location: Room 301, Maker Space
- Manufacturer documentation: [attach PDF or provide link]

HAZARDS TO CONSIDER:
- Class 2 laser (1000nm, 50W)
- Fire risk from combustible materials
- High temperature surfaces (nozzle reaches 200°C)
- Fumes from cutting materials
- Moving gantry system
- Electrical (240V AC)

SAFETY SYSTEMS:
- Laser interlock on door
- Emergency stop button (front right)
- Flame detection sensors
- Enclosed cutting chamber
- Exhaust port for ventilation

Please help me complete the Risk Assessment using the SAIL template format.
```

**For Safe Work Procedure:**
```
[Paste the Safe Work Procedure prompt above]

I'm creating an SWP for a [EQUIPMENT]. Here's the information:

EQUIPMENT INFORMATION:
- Equipment name: XYZ Model 5000 Laser Cutter
- Manufacturer: LaserCorp Industries
- Primary functions: Laser cutting and engraving
- Location: Room 301, Maker Space
- Associated Risk Assessment: SAIL-RA-LASER-001

OPERATION OVERVIEW:
- Used for cutting wood, acrylic, leather up to 10mm thick
- Typical jobs take 10-120 minutes
- Used daily by multiple researchers
- MUST be attended during operation due to fire risk
- Controlled via touchscreen and computer software

[Include all other required information...]

Please help me complete the Safe Work Procedure using the SAIL template format.
```

---

## Tips for Best Results

### 1. Provide Complete Information
- Attach or link to manufacturer documentation
- Include technical specifications
- Describe actual operating procedures you use
- List all known hazards and safety features

### 2. Be Specific About Context
- Who will use this equipment? (experience level)
- What training do they already have?
- What are the typical use cases?
- What materials/processes are involved?

### 3. Iterate and Refine
- Review Claude's initial output
- Ask for revisions: "Make the emergency shutdown procedure more detailed"
- Add information Claude might have missed: "Also include procedures for material jams"
- Request specific risk ratings: "Is 'Medium' risk appropriate for the thermal hazard?"

### 4. Verify Technical Accuracy
- Check all temperature, voltage, power ratings against manufacturer specs
- Verify emergency procedures match equipment design
- Confirm Australian Standards references are current
- Ensure risk ratings align with WHS guidelines

### 5. Ask Claude to Explain
- "Why did you rate this hazard as 'High'?"
- "What additional controls would reduce this to 'Low'?"
- "What Australian Standard applies to this type of equipment?"

### 6. Request Formatting Help
- "Format this as a markdown table"
- "Add more detail to the pre-operation checks section"
- "Break this down into numbered sub-steps"

---

## Follow-up Prompts for Refinement

**If output is too generic:**
```
This is too generic. Please revise with:
- Specific temperatures, voltages, dimensions from the [equipment] specs
- Exact button names and locations from the user manual
- Specific materials we'll be processing (wood, acrylic, leather)
- Actual safety features on this model (not generic equipment)
```

**To add missing hazards:**
```
You missed an important hazard: [describe hazard]
Please add a row to the Hazard Assessment Table covering:
- Task: [when this hazard occurs]
- Hazard: [specific hazard]
- Potential harm: [what could go wrong]
- Existing controls: [what's already on the equipment]
- Additional controls needed: [what we should implement]
```

**To improve emergency procedures:**
```
The emergency shutdown procedure needs more detail. Please revise to include:
- Exact location of emergency stop button (e.g., "front right corner, red mushroom button")
- What happens when pressed (e.g., "all motion stops immediately, laser shuts off, alarm sounds")
- How to reset (e.g., "twist button clockwise to release")
- What to check before restarting
- Alternative shutdown if emergency stop fails
```

**To refine risk ratings:**
```
I think the risk rating for [hazard] should be [different rating] because [reason].
Please revise the hazard table entry and explain your reasoning for the risk rating using the likelihood and consequence levels from the risk matrix.
```

**To improve step-by-step instructions:**
```
The operating procedure needs more detail. For each step, please include:
- Exactly what button/control to use (name from manual)
- What should happen (expected result)
- What to check/verify
- What to do if it doesn't work as expected

Make it detailed enough that someone trained but unfamiliar with this specific model could follow it.
```

---

## Quality Checklist

Before finalizing the document, verify:

**Risk Assessment:**
- [ ] All [placeholders] replaced with specific information
- [ ] Equipment name, model, manufacturer correct
- [ ] Reference number follows format: SAIL-RA-[EQUIPMENT]-001
- [ ] Dates are realistic and properly formatted
- [ ] Relevant Australian Standards listed
- [ ] Each hazard has its own row in the table
- [ ] Risk ratings use correct terms (High/Medium/Low/Very High)
- [ ] Additional controls are specific and actionable
- [ ] Implementation table has resources, responsibilities, dates
- [ ] Emergency procedures are equipment-specific
- [ ] Emergency contacts section has all required entries

**Safe Work Procedure:**
- [ ] All [placeholders] replaced with specific information
- [ ] Reference number follows format: SAIL-SWP-[EQUIPMENT]-001
- [ ] Links to correct Risk Assessment
- [ ] PPE list is complete and specific
- [ ] Pre-operation checks are comprehensive and testable
- [ ] Each procedure step is numbered and actionable
- [ ] Equipment-specific terminology used (not generic)
- [ ] Emergency procedures reference exact locations
- [ ] Cleanup procedures cover all components
- [ ] Competency requirements are measurable
- [ ] Sign-off sheet is included
- [ ] Review schedule is defined

---

## Document Versions and Updates

When updating an existing document:

```
I need to update an existing [Risk Assessment/Safe Work Procedure] for [EQUIPMENT].

CURRENT DOCUMENT: SAIL-[RA/SWP]-[EQUIPMENT]-XXX Version [X.X]

REASON FOR UPDATE:
- [ ] Annual review
- [ ] Equipment modification: [describe change]
- [ ] New hazard identified: [describe hazard]
- [ ] Procedure change: [describe change]
- [ ] Incident/near-miss: [describe incident]

CHANGES NEEDED:
[Describe what needs to be updated]

Please help me:
1. Update the version number to [X.X]
2. Update the issue date to [current month/year]
3. Update the review date to [one year from now]
4. Make the following specific changes: [list changes]
5. Ensure the document remains consistent throughout

Maintain the existing structure and formatting, only changing the specific sections that need updating.
```

---

## Notes

- These prompts are designed for use with Claude (Anthropic's AI assistant)
- Always review AI-generated content with subject matter experts
- Verify all technical specifications against manufacturer documentation
- Have safety officer review before finalizing
- Remember: AI can help draft, but humans must verify safety-critical information
- Keep manufacturer documentation handy for reference during generation
- Consider using Claude Projects to maintain context across multiple documents for the same equipment

---

**Last updated:** February 2026
**Maintained by:** SAIL Laboratory, School of Physics, University of Sydney
