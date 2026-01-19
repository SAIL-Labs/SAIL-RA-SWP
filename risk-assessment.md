---
layout: document
title: Risk Assessment - Bambu Lab H2D Laser Edition
doc_type: Risk Assessment
status: approved
permalink: /risk-assessment/
metadata:
  reference: SAIL-RA-BAMBU-H2D-001
  title: Bambu Lab H2D Laser Edition with 10W Laser Module
  version: "1.0"
  issue_date: January 2026
  prepared_by: Chris Betters
  supervisors: Chris Betters, Sergio Leon-Saval
  review_date: January 2027
critical_warning: |
  **CLASS 4 LASER HAZARD**
  
  The Bambu Lab H2D uses a **CLASS 4 laser module** (455nm, 10W blue laser). This is the highest and most dangerous laser classification.
  
  - **Class 4 lasers can cause:** Immediate permanent eye damage and blindness, severe skin burns, fire ignition, hazardous reflections from any surface
  - **The system operates as Class 1 (safe) ONLY when:** All laser safety windows are intact, all door interlocks are functioning, all safety systems are enabled, the enclosure is fully closed during operation
  
  **NEVER defeat, bypass, or disable ANY safety system.**
related_docs:
  - title: Safe Work Procedure
    url: /swp/
    description: Detailed operating procedures
  - title: Laser Safety Guide
    url: /laser-safety-guide/
    description: Class 4 laser safety information
show_review: true
---
  - Laser engraving and cutting
  - 3D printing (dual nozzle)
  - Material processing (wood, acrylic, leather, etc.)

**Location:** Maker space / Fabrication laboratory

### Persons at risk:

- Laboratory staff
- Research students
- Technicians
- Visitors to laboratory

### Risk assessment team (who was consulted?):

- Laboratory manager
- Safety officer
- Equipment users
- Laser safety advisor

---

## List of Legislation, Code of Practice, Australian Standards, Guidance Materials

- AS/NZS IEC 60825.1:2014 - Safety of laser products
- AS 2211.13-1999 - Safety of industrial laser equipment
- Work Health and Safety Act 2011
- Work Health and Safety Regulation 2017
- AS/NZS 3000:2018 - Electrical installations (Wiring Rules)
- AS 1940-2017 - Storage and handling of flammable and combustible liquids
- Bambu Lab H2D Laser Safety Document and User Manual
- University WHS policies and procedures for Class 4 lasers

---

## Risk Assessment Methodology

Assessing the risk is a brainstorming exercise, which is most effectively carried out in a team environment with the people required to complete the activity or process. Most activities or processes are broken down into a variety of separate tasks. For each task, consider the hazards, the potential harm or negative outcomes and the conditions required for those negative outcomes to occur.

Whenever assessing the health and safety risks associated with a task, always consider the following primary risk factors:

- The **physical activities** required to complete the task e.g. repetitive movement, high force, physical exertion, awkward posture
- The **work environment** e.g. lighting, layout, traffic flow, ventilation, access to support (isolation)
- The **nature of the hazard itself** e.g. working with chemicals, microorganisms, radiation, use of plant and equipment, sharps, working with potentially aggressive clients, patients or research participants
- The **people involved**, e.g. level of training, supervision, experience, health, age, physical capacity.

The information gathered from the **risk assessment** process must be used to develop a **Safe Work Procedure (SWP)** or **clinical protocol** for the activity.

---

## Hazard Assessment Table

### Task 1: Laser engraving and cutting operations

**Hazard/s:** Class 4 laser radiation (455nm, 10W blue laser). Operates as Class 1 ONLY when all safety systems intact

**Associated harm:**
- Eye damage
- Permanent blindness
- Severe skin burns
- Retinal injury
- Fire ignition

**Existing Risk Controls:**
- Laser safety windows
- Door interlocks (front, top)
- Safety window interlocks
- Emergency stop button
- Auto-stop when opened

**Current risk rating:** High

**Additional controls required:**
- Mandatory laser safety training
- NEVER defeat interlocks
- NEVER operate with doors/covers open
- Regular interlock testing
- Class 4 warning signage
- Tag out if damaged

**Residual risk rating:** Low

---

### Task 2: Operating with defeated or damaged safety systems

**Hazard/s:** Direct exposure to Class 4 laser

**Associated harm:**
- Severe eye injury
- Permanent blindness
- Severe burns
- Fire hazard

**Existing Risk Controls:**
- Prohibition policy
- Equipment design prevents easy bypass

**Current risk rating:** Very High

**Additional controls required:**
- ABSOLUTE PROHIBITION
- Disciplinary action
- Lock out if damaged
- Annual verification by qualified technician

**Residual risk rating:** Low (must not occur)

---

### Task 3: Laser processing of materials

**Hazard/s:** Fire and ignition of materials

**Associated harm:**
- Burns
- Fire
- Smoke inhalation
- Property damage

**Existing Risk Controls:**
- 5 flame sensors
- AI fire detection
- Flame-retardant chamber
- Emergency stop
- Audible alarm

**Current risk rating:** Medium

**Additional controls required:**
- NEVER leave unattended
- Fire extinguisher nearby (CO₂/dry powder)
- Clear flammable materials
- Emergency procedures
- Regular fire sensor testing

**Residual risk rating:** Low

---

### Task 4: High-temperature operation

**Hazard/s:** Thermal burns (350°C nozzle, 65°C chamber)

**Associated harm:** Severe burns to hands, arms

**Existing Risk Controls:**
- Warning labels
- Limited access during operation
- Cool-down period

**Current risk rating:** Medium

**Additional controls required:**
- Heat-resistant gloves available
- Cool-down procedures
- Training on hot surfaces

**Residual risk rating:** Low

---

### Task 5: Laser and cutting operations

**Hazard/s:** Inhalation of fumes, smoke, particulates

**Associated harm:**
- Respiratory irritation
- Long-term lung damage
- Allergic reactions

**Existing Risk Controls:**
- Exhaust system fitted
- Air filtration capable
- Enclosed chamber

**Current risk rating:** Medium

**Additional controls required:**
- LEV connected
- Air purifier recommended
- Respiratory protection if needed
- Check material SDS
- Regular filter maintenance

**Residual risk rating:** Low

---

### Task 6: General operation

**Hazard/s:** Electrical hazards (240V mains)

**Associated harm:**
- Electric shock
- Electrocution
- Burns

**Existing Risk Controls:**
- RCD protection
- Earthed equipment
- Enclosed components

**Current risk rating:** Medium

**Additional controls required:**
- Regular testing (test & tag)
- No wet conditions
- Qualified electrician for repairs
- Inspect power cords

**Residual risk rating:** Low

---

### Task 7: Material loading and operation

**Hazard/s:** Moving mechanical parts (XY motion, print head)

**Associated harm:** Crushing injuries to fingers, hands

**Existing Risk Controls:**
- Enclosed design
- Door interlocks
- Emergency stop accessible

**Current risk rating:** Low

**Additional controls required:**
- Keep hands clear
- Training on safe loading
- Wait for motion to stop

**Residual risk rating:** Very Low

---

### Task 8: Processing specific materials

**Hazard/s:** Toxic fumes (acrylic, PVC, etc.)

**Associated harm:**
- Respiratory damage
- Chemical poisoning

**Existing Risk Controls:**
- Material compatibility guidance
- Ventilation system

**Current risk rating:** Medium

**Additional controls required:**
- Prohibited materials list (PVC, polycarbonate)
- Pre-approval for new materials
- Consult SDS before use
- Enhanced ventilation

**Residual risk rating:** Low

---

### Task 9: Alarm systems

**Hazard/s:** Acoustic hazards

**Associated harm:**
- Hearing damage
- Startle response

**Existing Risk Controls:** Audible alarm fitted

**Current risk rating:** Low

**Additional controls required:**
- Appropriate volume
- Hearing protection if prolonged
- Training on alarm meaning

**Residual risk rating:** Very Low

---

### Task 10: Daily operation

**Hazard/s:** Unattended operation

**Associated harm:**
- Fire
- Equipment damage
- Delayed emergency response

**Existing Risk Controls:**
- Camera monitoring
- Multiple safety sensors

**Current risk rating:** High

**Additional controls required:**
- PROHIBITION of unattended laser operations
- Visual line of sight or constant camera monitoring
- Sign-in/sign-out procedures

**Residual risk rating:** Low

---

## Implementation of Additional Risk Controls

| Additional controls needed | Resources required | Responsible person | Date of implementation | RiskWare Reference |
|---------------------------|-------------------|-------------------|----------------------|-------------------|
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

---

## List Emergency Controls

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

---

## REVIEW

| Scheduled review date | 1 year | 2 years | 3 years |
|----------------------|---------|---------|---------|
| Are control measures in place (YES/NO) | | | |
| Are controls eliminating or minimising the risk (YES/NO) | | | |
| Are there any new problems with the risk (YES/NO) | | | |
| Reviewed by: | | | |
| Actual Review date: | | | |

---

## Risk Matrix

*[Insert your organisation's risk matrix here]*

The risk matrix should define:
- Likelihood levels (Rare, Unlikely, Possible, Likely, Almost Certain)
- Consequence levels (Insignificant, Minor, Moderate, Major, Severe)
- Risk ratings (Low, Medium, High, Very High)

---

*End of Risk Assessment*
