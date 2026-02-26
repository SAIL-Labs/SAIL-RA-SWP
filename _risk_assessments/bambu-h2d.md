---
layout: document
title: Risk Assessment - Bambu Lab H2D Laser Edition
doc_type: Risk Assessment
status: draft
permalink: /risk-assessments/bambu-h2d/
equipment_name: "Bambu Lab H2D Laser Edition"
reference: "SAIL-RA-BAMBU-H2D-001"
version: "1.1"
description: "Risk assessment for the Bambu Lab H2D 3D printer with 10W Class 4 laser module, covering laser radiation, thermal, electrical, mechanical, fire, and airborne emission hazards (UFPs and VOCs) from FDM printing and laser operations."
key_hazards: "Class 4 laser radiation, fire risk, thermal burns, ultrafine particle emissions, volatile organic compounds, toxic fumes"
metadata:
  reference: SAIL-RA-BAMBU-H2D-001
  title: Bambu Lab H2D Laser Edition with 10W Laser Module
  version: "1.1"
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
| **Activity or process:**<br><br>- 3D printing (FDM, dual nozzle, up to 350°C)<br>- Laser engraving and cutting (Class 4, 455nm, 10W)<br>- Material processing (wood, acrylic, leather, etc.)<br>- Handling of printed parts and waste material | **Persons at risk:**<br><br>- Laboratory staff<br>- Research students<br>- Technicians<br>- Visitors to laboratory<br>- Occupants of adjacent areas (airborne emissions) |
| **Location:**<br><br>Maker space / Fabrication laboratory | **Risk assessment team** (who was consulted?)**:**<br><br>- Laboratory manager<br>- Safety officer<br>- Equipment users<br>- Laser safety advisor |

</div>

<div class="legislation-box" markdown="1">

**List of Legislation, Code of Practice, Australian Standards, Guidance Materials used to determine control measures**

- Work Health and Safety Act 2011
- Work Health and Safety Regulation 2017
- AS/NZS IEC 60825.1:2014 -- Safety of laser products
- AS 2211.13-1999 -- Safety of industrial laser equipment
- AS/NZS 3000:2018 -- Electrical installations (Wiring Rules)
- AS 1940-2017 -- Storage and handling of flammable and combustible liquids
- AS 1668.2-2012 -- The use of ventilation and airconditioning in buildings, Part 2: Mechanical ventilation in buildings
- Safe Work Australia, Workplace Exposure Standards for Airborne Contaminants (2024)
- Bambu Lab H2D Laser Safety Document and User Manual
- University WHS policies and procedures for Class 4 lasers
- US EPA, "EPA Researchers Continue to Study the Emissions of 3D Printers" (2025)
- "Exposure hazards of particles and VOCs emitted from material extrusion 3D printing" (2023), *Environment International*
- "A global evaluation of exposure to pollutants in 3D printing" (2025), *Journal of Hazardous Materials Advances*

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
| High-temperature operation | Thermal burns (350°C nozzle, 65°C chamber) | - Severe burns to hands, arms<br>- Skin damage from contact with nozzle, heat bed, or chamber walls | - Warning labels<br>- Limited access during operation<br>- Cool-down period | **Medium** | - Heat-resistant gloves available<br>- Cool-down procedures<br>- Training on hot surfaces | **Low** |
| 3D printing with any filament type (PLA, PETG, ABS, ASA, nylon, etc.) | Ultrafine particle (UFP) emissions. All FDM filaments emit particles smaller than 100 nm at rates of approximately 10⁸ to 10¹² particles/min. Published research has detected trace metals (Cr, As, Pb, Cd, Co) in particulate fraction | - Deep lung penetration of respirable UFPs<br>- Respiratory inflammation and reduced lung function<br>- Increased asthma risk<br>- Chronic respiratory disease with repeated exposure<br>- US EPA characterises exposure profile as comparable to traffic-related air pollution | - Fully enclosed build chamber contains emissions during printing<br>- Internal activated carbon filter (recirculates chamber air; active by default for ABS, ASA, PC, PA; bypasses for PLA, PETG)<br>- Bambu Lab Smoke Purifier connected to exhaust: G4 pre-filter, F8 filter, activated carbon (1200 mg/g adsorption capacity), HEPA H13 (captures 99% of particles ≥0.3 µm)<br>- Fresh air supply to printer room | **Medium** | - Complete mechanical extraction upgrade for printer room to provide adequate air changes per hour<br>- Keep enclosure closed during printing and allow cooling before opening to prevent burst release of accumulated particles<br>- Enable internal carbon filter for ALL filament types, not just high-temperature materials<br>- Avoid extended occupancy of printer room during long prints until extraction upgrade complete<br>- Regular cleaning of printer internals (fans, chamber surfaces) to remove deposited particulate<br>- Consider VOC/PM2.5 monitor to verify extraction effectiveness | **Low** |
| 3D printing with lower-emission filaments (PLA, PETG) | Volatile organic compound (VOC) emissions. PLA emits lactide and methyl methacrylate. PETG emits ethylbenzene (IARC Group 2B -- possibly carcinogenic) | - Eye, nose and throat irritation<br>- Headaches, coughing, nausea<br>- Potential carcinogenic risk from ethylbenzene (PETG) with chronic exposure<br>- Total VOC concentrations may exceed indoor air quality guidelines in poorly ventilated settings | - Fully enclosed build chamber<br>- Bambu Lab Smoke Purifier with activated carbon stage addresses VOCs in exhaust path<br>- Fresh air supply to printer room | **Medium** | - Preferential use of PLA and PETG where material properties allow<br>- Ensure Smoke Purifier is connected and operating for every print<br>- Complete room extraction upgrade<br>- Replace activated carbon filters per manufacturer schedule (adsorption capacity degrades over time)<br>- Monitor for symptoms of irritation during printing | **Low** |
| 3D printing with higher-emission filaments (ABS, ASA, nylon, PC, composites) | Elevated VOC emissions. ABS/ASA emit styrene (IARC Group 2B), formaldehyde (IARC Group 1 -- carcinogenic), and acetaldehyde at 3-4x the rate of PLA. Nylon emits caprolactam (respiratory irritant). High-temperature composites (PC, PPS) produce significantly increased emissions at elevated extrusion temperatures | - Respiratory damage and chronic lung disease<br>- Carcinogenic risk from styrene and formaldehyde exposure<br>- Eye, nose and throat irritation<br>- Headaches, nausea, dizziness<br>- Sensitisation and allergic reactions<br>- Potential for exceeding workplace exposure standards in poorly ventilated rooms | - Fully enclosed build chamber<br>- Internal activated carbon filter active by default for these filament types<br>- Bambu Lab Smoke Purifier with activated carbon and HEPA H13 in exhaust path<br>- Fresh air supply to printer room | **High** | - Use ABS/ASA/nylon/PC ONLY when specifically required by application; default to PLA or PETG<br>- Room extraction system MUST be operational before printing with these materials<br>- NEVER open enclosure during printing with high-emission filaments<br>- Supervisor pre-approval required for ABS, ASA, PC, PPS, and composite filaments<br>- Consult SDS for specific filament before use<br>- Limit concurrent prints with high-emission materials<br>- Avoid extended occupancy of printer room during and immediately after printing<br>- Clean printer internals after ABS printing (deposits sticky residue on fans and internal surfaces)<br>- Respiratory protection (P2/N95 minimum) if extraction is inadequate or under maintenance | **Low** |
| Laser cutting and engraving materials | Fumes, smoke and particulates from thermal decomposition of materials by laser | - Respiratory irritation and damage<br>- Eye irritation<br>- Toxic gas exposure (varies by material)<br>- Long-term lung damage | - Exhaust system fitted<br>- Air filtration via Smoke Purifier<br>- Enclosed chamber | **Medium** | - LEV connected and verified operational before laser use<br>- Consult material SDS before laser processing<br>- Use only approved materials (see prohibited list)<br>- Respiratory protection available if required<br>- Regular filter maintenance | **Low** |
| Processing prohibited or unknown materials (laser or 3D printing) | Toxic fumes from incompatible materials. PVC releases hydrochloric acid gas. Polycarbonate produces bisphenol A. Unknown materials may produce unpredictable toxic decomposition products | - Severe respiratory damage<br>- Chemical poisoning<br>- Hydrochloric acid burns to airways (PVC)<br>- Endocrine disruption (polycarbonate) | - Material compatibility guidance from manufacturer<br>- Ventilation system | **High** | - PROHIBITED materials list enforced: PVC, vinyl, polycarbonate (laser), chlorinated plastics, materials of unknown composition<br>- Pre-approval process for any new material not on approved list<br>- Consult SDS before use of any unfamiliar material<br>- Enhanced ventilation for all material processing<br>- Prohibited list displayed at equipment | **Low** |
| General operation | Electrical hazards (240V mains) | - Electric shock<br>- Electrocution<br>- Burns | - RCD protection<br>- Earthed equipment<br>- Enclosed components | **Medium** | - Regular testing (test & tag)<br>- No wet conditions<br>- Qualified electrician for repairs<br>- Inspect power cords | **Low** |
| Material loading and operation | Moving mechanical parts (XY gantry, print head, toolhead change mechanism) | - Crushing injuries to fingers, hands<br>- Entanglement | - Enclosed design<br>- Door interlocks<br>- Emergency stop accessible | **Low** | - Keep hands clear during operation<br>- Training on safe loading procedure<br>- Wait for all motion to stop before opening doors | **Very Low** |
| Alarm systems | Acoustic hazards from fire detection alarm and error alerts | - Hearing discomfort<br>- Startle response | - Audible alarm fitted | **Low** | - Appropriate alarm volume setting<br>- Training on alarm meaning and response<br>- Hearing protection available if prolonged exposure during fault condition | **Very Low** |
| Unattended operation (3D printing) | Extended unattended prints with potential for fire, equipment failure, or emission accumulation | - Fire with delayed response<br>- Equipment damage<br>- UFP/VOC accumulation in occupied room<br>- Delayed emergency response | - Camera monitoring capability<br>- 5 flame sensors and AI fire detection<br>- Enclosed chamber<br>- Smoke Purifier filtration | **High** | - PROHIBITION of unattended laser operations (laser must have operator present at all times)<br>- 3D print operations: remote camera monitoring acceptable if flame detection and auto-stop verified functional<br>- Sign-in/sign-out procedures<br>- Ensure extraction and filtration running for duration of print<br>- Room should not be continuously occupied during long unattended prints unless extraction verified adequate | **Low** |

</div>

## Implementation of Additional Risk Controls

| Additional controls needed | Resources required | Responsible person | Date of implementation | RiskWare Reference |
|---|---|---|---|---|
| Write the Safe Work Procedure (SWP) for laser and 3D printing operations | Time (approx 3 hours) | Supervisor | Prior to use | N/A |
| Develop Class 4 laser safety protocol and emergency procedures | Time (2 hours), laser safety advisor | Safety Officer | Prior to use | N/A |
| Annual safety interlock testing and verification by qualified technician | Qualified laser safety technician, test equipment | Laboratory Manager | Annually | TBD |
| Install prominent Class 4 laser warning signage | Warning signs compliant with AS/NZS IEC 60825.1 | Technician | Prior to use | N/A |
| Develop prohibited materials list and material approval process (laser and 3D printing) | Time (1 hour), manufacturer documentation, SDS review | Safety Officer | Prior to use | N/A |
| Mandatory operator training programme (Class 4 laser hazards, safety systems, 3D printing emissions awareness, fire safety, emergency procedures) | Time, training materials, laser safety expert | Laboratory Manager | Prior to use | N/A |
| Complete mechanical extraction upgrade for printer room | Ducting, extraction fan, installation, commissioning | Facilities / Laboratory Manager | Prior to use of high-emission filaments | TBD |
| Procurement of emergency equipment (CO₂ fire extinguisher, first aid kit, heat-resistant gloves) | Equipment costs (approx $300) | Laboratory Manager | Prior to use | N/A |
| Establish regular inspection schedule (safety interlocks, fire sensors, electrical testing, filter condition) | Time, monthly inspections | Technician | Ongoing | TBD |
| Develop sign-in/sign-out log and supervision procedures | Log book or electronic system | Laboratory Manager | Prior to use | N/A |
| Electrical safety testing (test and tag) | Qualified electrician | Facilities | Prior to use, then annually | TBD |
| Smoke Purifier and internal filter maintenance schedule (activated carbon and HEPA replacement) | Replacement filters, labour | Technician | Per manufacturer schedule (check quarterly) | N/A |
| Develop filament selection and approval policy (default to PLA/PETG; supervisor approval for ABS/ASA/nylon/PC) | Time (1 hour), manufacturer data | Supervisor | Prior to use | N/A |
| Procure VOC/PM2.5 monitor for printer room | Air quality monitor (approx $200-500) | Laboratory Manager | After extraction upgrade | N/A |
| Laser safety eye examination programme (baseline and periodic) | Occupational health service | Laboratory Manager | Prior to use, then as required | TBD |
| Develop 3D printing emissions awareness training module | Time (2 hours), published research references | Safety Officer | Prior to use | N/A |
| Display prohibited materials list and filament risk profile at equipment | Printed signage | Technician | Prior to use | N/A |


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

### Excessive Fumes, Smoke, or Respiratory Irritation (3D Printing or Laser Operations):

- Press emergency stop button immediately to halt the print or laser operation
- If experiencing respiratory irritation, headache, nausea, or eye irritation: leave the room immediately and move to fresh air
- If fumes are overwhelming or visible smoke is present: evacuate the area
- Do NOT open the printer enclosure while fumes are present (allows burst release of accumulated emissions)
- Once room is clear of personnel:
  - Increase ventilation (open doors and windows if safe to do so)
  - Allow Smoke Purifier and extraction system to clear remaining airborne contaminants
  - Do not re-enter until air has cleared (minimum 15 minutes with ventilation running)
- Investigate cause before resuming:
  - Verify Smoke Purifier is connected and operational
  - Check extraction system is functioning
  - Check filter condition (may be saturated)
  - Verify correct filament type was used (check for prohibited materials)
  - Review print temperature settings (excessive temperature increases all emissions)
- If symptoms persist after leaving the room, seek medical attention
- Report incident to supervisor
- Complete incident report if medical attention sought or if caused by equipment malfunction

### Burns from Hot Surfaces:

- Remove from heat source immediately
- Cool affected area with running cool water for 20 minutes
- Remove jewellery or tight clothing near burn (unless stuck to skin)
- Cover with clean, non-fluffy material (cling film ideal)
- Seek medical attention for serious burns (larger than a 5 cm diameter area, on face/hands/joints)
- Complete first aid documentation and incident report

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