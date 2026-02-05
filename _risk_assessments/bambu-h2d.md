---
layout: document
title: Risk Assessment - Bambu Lab H2D Laser Edition
doc_type: Risk Assessment
status: Draft
permalink: /risk-assessments/bambu-h2d/
equipment_name: Bambu Lab H2D Laser Edition
reference: SAIL-RA-BAMBU-H2D-001
version: "1.0"
description: "Comprehensive risk assessment for the Bambu H2D with 10W Class 4 laser module. Covers laser radiation hazards, fire risks, thermal hazards, inhalation risks, and complete emergency procedures."
key_hazards: "Class 4 laser radiation, fire ignition, thermal burns (350°C), hazardous fumes"
metadata:
  reference: SAIL-RA-BAMBU-H2D-001
  title: Bambu Lab H2D Laser Edition with 10W Laser Module
  version: "1.0"
  issue_date: January 2026
  next_review_date: January 2027
  prepared_by: Chris Betters
  supervisors: Chris Betters, Sergio Leon-Saval
  faculty_school: School of Physics
related_docs:
  - title: Safe Work Procedure
    url: /safe-work-procedures/bambu-h2d/
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
| **Activity or process:**<br><br>- Laser engraving and cutting<br>- 3D printing (dual nozzle)<br>- Material processing (wood, acrylic, leather, etc.) | **Persons at risk:**<br><br>- Laboratory staff<br>- Research students<br>- Technicians<br>- Visitors to laboratory |
| **Location:**<br><br>Maker space / Fabrication laboratory | **Risk assessment team** (who was consulted?)**:**<br><br>- Laboratory manager<br>- Safety officer<br>- Equipment users<br>- Laser safety advisor |

</div>

<div class="legislation-box" markdown="1">

**List of Legislation, Code of Practice, Australian Standards, Guidance Materials used to determine control measures**

- AS/NZS IEC 60825.1:2014 - Safety of laser products
- AS 2211.13-1999 - Safety of industrial laser equipment
- Work Health and Safety Act 2011
- Work Health and Safety Regulation 2017
- AS/NZS 3000:2018 - Electrical installations (Wiring Rules)
- AS 1940-2017 - Storage and handling of flammable and combustible liquids
- Bambu Lab H2D Laser Safety Document and User Manual
- University WHS policies and procedures for Class 4 lasers

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
| Laser engraving and cutting operations | Class 4 laser radiation (455nm, 10W blue laser). Operates as Class 1 ONLY when all safety systems intact | - Eye damage<br>- Permanent blindness<br>- Severe skin burns<br>- Retinal injury<br>- Fire ignition | - Laser safety windows<br>- Door interlocks (front, top)<br>- Safety window interlocks<br>- Emergency stop button<br>- Auto-stop when opened | **High** | - Mandatory laser safety training<br>- NEVER defeat interlocks<br>- NEVER operate with doors/covers open<br>- Regular interlock testing<br>- Class 4 warning signage<br>- Tag out if damaged | **Low** |
| Operating with defeated or damaged safety systems | Direct exposure to Class 4 laser | - Severe eye injury<br>- Permanent blindness<br>- Severe burns<br>- Fire hazard | - Prohibition policy<br>- Equipment design prevents easy bypass | **Very High** | - ABSOLUTE PROHIBITION<br>- Disciplinary action<br>- Lock out if damaged<br>- Annual verification by qualified technician | **Low** (must not occur) |
| Laser processing of materials | Fire and ignition of materials | - Burns<br>- Fire<br>- Smoke inhalation<br>- Property damage | - 5 flame sensors<br>- AI fire detection<br>- Flame-retardant chamber<br>- Emergency stop<br>- Audible alarm | **Medium** | - NEVER leave unattended<br>- Fire extinguisher nearby (CO₂/dry powder)<br>- Clear flammable materials<br>- Emergency procedures<br>- Regular fire sensor testing | **Low** |
| High-temperature operation | Thermal burns (350°C nozzle, 65°C chamber) | - Severe burns to hands, arms | - Warning labels<br>- Limited access during operation<br>- Cool-down period | **Medium** | - Heat-resistant gloves available<br>- Cool-down procedures<br>- Training on hot surfaces | **Low** |
| Laser and cutting operations | Inhalation of fumes, smoke, particulates | - Respiratory irritation<br>- Long-term lung damage<br>- Allergic reactions | - Exhaust system fitted<br>- Air filtration capable<br>- Enclosed chamber | **Medium** | - LEV connected<br>- Air purifier recommended<br>- Respiratory protection if needed<br>- Check material SDS<br>- Regular filter maintenance | **Low** |
| General operation | Electrical hazards (240V mains) | - Electric shock<br>- Electrocution<br>- Burns | - RCD protection<br>- Earthed equipment<br>- Enclosed components | **Medium** | - Regular testing (test & tag)<br>- No wet conditions<br>- Qualified electrician for repairs<br>- Inspect power cords | **Low** |
| Material loading and operation | Moving mechanical parts (XY motion, print head) | - Crushing injuries to fingers, hands | - Enclosed design<br>- Door interlocks<br>- Emergency stop accessible | **Low** | - Keep hands clear<br>- Training on safe loading<br>- Wait for motion to stop | **Very Low** |
| Processing specific materials | Toxic fumes (acrylic, PVC, etc.) | - Respiratory damage<br>- Chemical poisoning | - Material compatibility guidance<br>- Ventilation system | **Medium** | - Prohibited materials list (PVC, polycarbonate)<br>- Pre-approval for new materials<br>- Consult SDS before use<br>- Enhanced ventilation | **Low** |
| Alarm systems | Acoustic hazards | - Hearing damage<br>- Startle response | - Audible alarm fitted | **Low** | - Appropriate volume<br>- Hearing protection if prolonged<br>- Training on alarm meaning | **Very Low** |
| Daily operation | Unattended operation | - Fire<br>- Equipment damage<br>- Delayed emergency response | - Camera monitoring<br>- Multiple safety sensors | **High** | - PROHIBITION of unattended laser operations<br>- Visual line of sight or constant camera monitoring<br>- Sign-in/sign-out procedures | **Low** |

</div>

## Implementation of Additional Risk Controls

| Additional controls needed | Resources required | Responsible person | Date of implementation | RiskWare Reference |
|---|---|---|---|---|
| Write the Safe Work Procedure (SWP) for laser operations | Time (approx 2 hours) | Supervisor | Prior to use | N/A |
| Develop Class 4 laser safety protocol and emergency procedures | Time (2 hours), laser safety advisor | Safety Officer | Prior to use | N/A |
| Annual safety interlock testing and verification by qualified technician | Qualified laser safety technician, test equipment | Laboratory Manager | Annually | TBD |
| Install prominent Class 4 laser warning signage | Warning signs compliant with AS/NZS IEC 60825.1 | Technician | Prior to use | N/A |
| Develop prohibited materials list and material approval process | Time (1 hour), manufacturer documentation | Safety Officer | Prior to use | N/A |
| Mandatory operator training programme (Class 4 laser hazards, safety systems, fire safety, emergency procedures) | Time, training materials, laser safety expert | Laboratory Manager | Prior to use | N/A |
| Installation and testing of local exhaust ventilation system | Ducting, installation, air purifier unit (recommended) | Facilities / Laboratory Manager | Prior to use | TBD |
| Procurement of emergency equipment (CO₂ fire extinguisher, first aid kit, heat-resistant gloves) | Equipment costs (approx £200) | Laboratory Manager | Prior to use | N/A |
| Establish regular inspection schedule (safety interlocks, fire sensors, electrical testing) | Time, monthly inspections | Technician | Ongoing | TBD |
| Develop sign-in/sign-out log and supervision procedures | Log book or electronic system | Laboratory Manager | Prior to use | N/A |
| Electrical safety testing (test and tag) | Qualified electrician | Facilities | Prior to use, then annually | TBD |
| Ventilation filter maintenance schedule | Replacement filters, labour | Technician | Quarterly | N/A |
| Laser safety eye examination programme (baseline and periodic) | Occupational health service | Laboratory Manager | Prior to use, then as required | TBD |


## List emergency controls
<small>These might include how to deal with fires, spills, emergency shutdown of equipment, exposure to hazardous materials and adverse reactions or the deteriorating condition of patients/research participants in our care.</small>

<div class="emergency-box" markdown="1">

### CRITICAL: Class 4 Laser Safety

- The laser module is CLASS 4 when safety systems are defeated or removed
- NEVER operate with any door, cover, or safety window open or removed
- NEVER defeat, bypass, or disable any safety interlock
- System operates as Class 1 ONLY when all safety systems are intact and functioning
- If any safety system fails, immediately stop use and lock out equipment

### Emergency Shutdown:

- Press red emergency stop button on equipment
- If button fails, isolate power at wall outlet
- Do not resume operation until issue resolved and equipment inspected

### Fire Emergency:

- Press emergency stop button immediately
- Equipment has 5 flame sensors and AI fire detection with automatic alarm
- Do not open chamber door (introduces oxygen, may worsen fire)
- Use CO₂ or dry powder fire extinguisher through access points if safe to do so
- If fire cannot be controlled immediately:
  - Evacuate area
  - Activate building fire alarm
  - Call emergency services (000)
  - Notify building warden

### Equipment Malfunction or Safety System Failure:

- Press emergency stop button immediately
- Isolate power at wall outlet if safe to do so
- Do NOT attempt to operate with damaged safety interlocks, windows, or door sensors
- Lock out and tag equipment as defective immediately
- Report to supervisor and safety officer
- Arrange qualified laser safety technician inspection
- Equipment must NOT be used until all safety systems verified functional

### Suspected Exposure to Laser Radiation (Class 4 exposure):

- Press emergency stop immediately
- If eye exposure suspected:
  - Seek IMMEDIATE medical attention at emergency department
  - Do not rub eyes
  - Close eyes or look away from bright light
  - Note time, duration, and circumstances of exposure
- Report incident immediately to supervisor and safety officer
- Complete incident report and RiskWare notification
- Equipment must be locked out and inspected before any further use
- Never look directly at laser emission point or reflected beams

### Burns from Hot Surfaces:

- Remove from heat source immediately
- Cool affected area with running cool water for 20 minutes
- Remove jewellery or tight clothing near burn (unless stuck to skin)
- Cover with clean, non-fluffy material (cling film ideal)
- Seek medical attention for serious burns (larger than 20p coin, on face/hands/joints)
- Complete first aid documentation and incident report

### Excessive Fumes or Smoke:

- Press emergency stop immediately
- If fumes are overwhelming, evacuate area
- Increase ventilation when safe (open doors/windows)
- Check exhaust system connection and function
- Check air filter status
- Review material compatibility and SDS before resuming
- Report incident to supervisor

### Emergency Contacts:

- Emergency services: 000
- University Security (after hours): [insert number]
- Supervisor: Chris Betters [insert number]
- Safety Officer: [insert name and number]
- First Aiders: [listed on notice board]

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
