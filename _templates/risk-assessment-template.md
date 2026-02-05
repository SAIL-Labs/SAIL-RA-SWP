---
layout: document
title: Risk Assessment - [Equipment Name]
doc_type: Risk Assessment
status: Draft
permalink: /risk-assessments/[equipment-slug]/
# Fields for auto-population on index page (update these when creating a new RA)
equipment_name: "[Equipment Name]"  # e.g., "Bambu Lab H2D Laser Edition"
reference: "SAIL-RA-[EQUIPMENT]-XXX"
version: "1.0"
description: "[Brief 1-2 sentence description of what this risk assessment covers and main hazards]"
key_hazards: "[Comma-separated list of main hazards]"  # e.g., "Laser radiation, fire risk, thermal burns"
metadata:
  reference: SAIL-RA-[EQUIPMENT]-XXX
  title: [Full Equipment/Process Name]
  version: "1.0"
  issue_date: [Month Year]
  next_review_date: [Month Year - typically 1 year from issue]
  prepared_by: [Your Name]
  supervisors: [Supervisor Names]
  faculty_school: School of Physics
related_docs:
  - title: Safe Work Procedure
    url: /safe-work-procedures/[equipment-slug]/
    description: Detailed operating procedures
show_review: true
---

Use this form to assist you to complete risk assessments for hazardous activities and processes. Any serious or ongoing hazards should be reported via RiskWare to ensure that appropriate corrective actions are tracked and completed.

<div class="metadata-table" markdown="1">

**Faculty/School:** | School of Physics
**Initial Issue Date:** | {{ page.metadata.issue_date }}
**Next Review Date:** | {{ page.metadata.next_review_date }}
**Risk Assessment Reference Number:** | {{ page.metadata.reference }}
**Risk Assessment Name:** | {{ page.metadata.title }}
**Prepared by:** | {{ page.metadata.prepared_by }}
**Responsible supervisor/s:** | {{ page.metadata.supervisors }}

</div>

<div class="activity-persons-table" markdown="1">

| **Identify the activity and the location** | **Identify who may be at risk**<br><small>This might include fellow workers, students, visitors, contractors, patients, research participants and the public.</small> |
|---|---|
| **Activity or process:**<br><br>- [List main activities]<br>- [List processes]<br>- [List operations] | **Persons at risk:**<br><br>- [List who may be affected]<br>- [e.g., Laboratory staff]<br>- [e.g., Students] |
| **Location:**<br><br>[Specific location, room number, building] | **Risk assessment team** (who was consulted?)**:**<br><br>- [Laboratory manager]<br>- [Safety officer]<br>- [Equipment users]<br>- [Subject matter experts] |

</div>

<div class="legislation-box" markdown="1">

**List of Legislation, Code of Practice, Australian Standards, Guidance Materials used to determine control measures**

- Work Health and Safety Act 2011
- Work Health and Safety Regulation 2017
- [List relevant Australian Standards - e.g., AS/NZS specific to equipment]
- [List relevant codes of practice]
- [Manufacturer documentation and manuals]
- [University WHS policies and procedures]

</div>

<div class="methodology-box" markdown="1">

**Risk Assessment Methodology**

Assessing the risk is a brainstorming exercise, which is most effectively carried out in a team environment with the people required to complete the activity or process. Most activities or processes are broken down into a variety of separate tasks. For each task, consider the hazards, the potential harm or negative outcomes and the conditions required for those negative outcomes to occur.

Whenever assessing the health and safety risks associated with a task, always consider the following primary risk factors:

- The **physical activities** required to complete the task e.g. repetitive movement, high force, physical exertion, awkward posture
- The **work environment** e.g. lighting, layout, traffic flow, ventilation, access to support (isolation)
- The **nature of the hazard itself** e.g. working with chemicals, microorganisms, radiation, use of plant and equipment, sharps, working with potentially aggressive clients, patients or research participants
- The **people involved**, e.g. level of training, supervision, experience, health, age, physical capacity.

The information gathered from the **risk assessment** process must be used to develop a **Safe Work Procedure (SWP)** or **clinical protocol** for the activity.

</div>

## Hazard Assessment Table

<div class="hazard-table-wrapper" markdown="1">
| Task or scenario | Hazard/s | Associated harm, e.g. what could go wrong? | Existing Risk Controls | Current risk rating | Any additional controls required? | Residual risk rating |
|---|---|---|---|---|---|---|
| [Describe specific task or scenario] | [Identify hazard - be specific] | - [List potential injuries/harm]<br>- [List potential consequences]<br>- [What could go wrong] | - [List existing safety features]<br>- [List engineering controls]<br>- [List admin controls] | **[High/Medium/Low/Very High]** | - [Additional safety measures needed]<br>- [Training requirements]<br>- [PPE requirements]<br>- [Procedures to implement] | **[Low/Very Low]** |
| [Next task] | [Next hazard] | - [Harm 1]<br>- [Harm 2] | - [Control 1]<br>- [Control 2] | **[Rating]** | - [Additional control 1]<br>- [Additional control 2] | **[Rating]** |

**Example rows - replace with actual hazards for your equipment:**

| Operation of [equipment] | Electrical hazards (240V) | - Electric shock<br>- Electrocution<br>- Burns | - RCD protection<br>- Earthed equipment<br>- Enclosed components | **Medium** | - Regular testing (test & tag)<br>- No wet conditions<br>- Qualified electrician for repairs<br>- Inspect power cords | **Low** |
| High-temperature operation | Thermal burns ([temperature]°C surfaces) | - Severe burns to hands, arms<br>- Skin damage | - Warning labels<br>- Limited access during operation<br>- Cool-down period | **Medium** | - Heat-resistant gloves available<br>- Cool-down procedures<br>- Training on hot surfaces | **Low** |
| General operation | Moving mechanical parts | - Crushing injuries to fingers, hands<br>- Entanglement | - Enclosed design<br>- Guards fitted<br>- Emergency stop accessible | **Low** | - Keep hands clear<br>- Training on safe operation<br>- Wait for motion to stop | **Very Low** |

</div>

## Implementation of Additional Risk Controls

| Additional controls needed | Resources required | Responsible person | Date of implementation | RiskWare Reference |
|---|---|---|---|---|
| Write the Safe Work Procedure (SWP) | Time (approx 2 hours) | Supervisor | Prior to use | N/A |
| [List each additional control identified in hazard table] | [Resources needed] | [Who is responsible] | [When it will be done] | [Reference if applicable] |
| Mandatory operator training programme | Time, training materials, subject matter expert | Laboratory Manager | Prior to use | N/A |
| Installation of [safety equipment] | [Equipment costs], installation | Facilities / Laboratory Manager | Prior to use | TBD |
| Procurement of emergency equipment ([list items]) | Equipment costs | Laboratory Manager | Prior to use | N/A |
| Establish regular inspection schedule | Time, monthly inspections | Technician | Ongoing | TBD |
| Develop sign-in/sign-out log and supervision procedures | Log book or electronic system | Laboratory Manager | Prior to use | N/A |
| [Safety testing - specify type] | Qualified technician | Facilities | Prior to use, then [frequency] | TBD |


## List emergency controls
<small>These might include how to deal with fires, spills, emergency shutdown of equipment, exposure to hazardous materials and adverse reactions or the deteriorating condition of patients/research participants in our care.</small>

<div class="emergency-box" markdown="1">

### CRITICAL: [Main Safety Concern - e.g., "Class 4 Laser Safety", "High Voltage", "Chemical Hazards"]

- [List absolute prohibitions]
- NEVER [critical safety rule]
- NEVER [critical safety rule]
- [System operates safely ONLY when all safety systems are intact and functioning]
- If any safety system fails, immediately stop use and lock out equipment

### Emergency Shutdown:

- [Describe emergency stop procedure - location of button, how to activate]
- If emergency stop fails, [backup shutdown method]
- Do not resume operation until issue resolved and equipment inspected

### [Specific Emergency Type - e.g., "Fire Emergency", "Chemical Spill", "Equipment Failure"]:

- [Step 1 - immediate action]
- [Step 2 - containment/control]
- [Step 3 - when to escalate]
- [Step 4 - evacuation criteria]
- [Step 5 - who to notify]

**Example - Fire Emergency:**
- Press emergency stop button immediately
- Equipment has [describe fire detection systems if applicable]
- Do not open chamber/doors (introduces oxygen, may worsen fire)
- Use [appropriate fire extinguisher type] if safe to do so
- If fire cannot be controlled immediately:
  - Evacuate area
  - Activate building fire alarm
  - Call emergency services (000)
  - Notify building warden

### Equipment Malfunction or Safety System Failure:

- Press emergency stop button immediately
- Isolate power if safe to do so
- Do NOT attempt to operate with damaged safety systems
- Lock out and tag equipment as defective immediately
- Report to supervisor and safety officer
- Arrange qualified technician inspection
- Equipment must NOT be used until all safety systems verified functional

### [Exposure/Injury Type - specific to equipment hazards]:

**Example - Thermal Burns:**
- Remove from heat source immediately
- Cool affected area with running cool water for 20 minutes
- Remove jewellery or tight clothing near burn (unless stuck to skin)
- Cover with clean, non-fluffy material (cling film ideal)
- Seek medical attention for serious burns (larger than 20p coin, on face/hands/joints)
- Complete first aid documentation and incident report

**Example - Chemical Exposure:**
- [Immediate first aid specific to chemical]
- Consult SDS for specific treatment
- Seek medical attention if [criteria]
- Provide SDS to medical personnel

### Emergency Contacts:

- Emergency services: 000
- University Security (after hours): [insert number]
- Supervisor: [name and number]
- Safety Officer: [name and number]
- First Aiders: [location/contact]

</div>

<div class="page-break"></div>

## REVIEW

<div class="review-table" markdown="1">

| | 1 year | 2 years | 3 years |
|---|---|---|---|
| **Scheduled review date** | | | |
| **Are control measures in place (YES/NO)** | | | |
| **Are controls eliminating or minimising the risk (YES/NO)** | | | |
| **Are there any new problems with the risk (YES/NO)** | | | |
| **Reviewed by:** | | | |
| **Actual Review date:** | | | |

</div>


## Risk Matrix

![Risk Assessment Matrix]({{ '/assets/images/RA-Matrix.png' | relative_url }})

The risk matrix defines:
- **Likelihood levels:** Rare, Unlikely, Possible, Likely, Almost Certain
- **Consequence levels:** Insignificant, Minor, Moderate, Major, Severe
- **Risk ratings:** Low, Medium, High, Very High

---

*End of Risk Assessment*
