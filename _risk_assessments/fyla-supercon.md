---
layout: document
title: Risk Assessment - Fyla Iceblink Supercontinuum Fiber Laser
doc_type: Risk Assessment
status: Draft
permalink: /risk-assessments/fyla-supercon/
equipment_name: "Fyla Iceblink Supercontinuum Fiber Laser"
reference: "SAIL-RA-FYLA-SUPERCON-001"
version: "1.0"
description: "Risk assessment for the Fyla Iceblink Supercontinuum Fiber Laser used as a broadband light source in the photonic lantern wavefront sensing setup in Room 121c, covering Class 4 laser radiation across broadband visible-to-NIR wavelengths, pulsed peak-power hazards, fibre end-face exposure, filter failure, interlock malfunction, and scattered radiation scenarios."
key_hazards: "Class 4 broadband laser radiation (visible to NIR), high peak power pulsed output, invisible near-infrared wavelengths, fibre end-face exposure, interlock defeat, reflected and scattered radiation, fire ignition"
metadata:
  reference: SAIL-RA-FYLA-SUPERCON-001
  title: Fyla Iceblink Supercontinuum Fiber Laser
  version: "1.0"
  issue_date: May 2026
  next_review_date: May 2027
  prepared_by: Claude (AI draft, awaiting expert review)
  supervisors: Chris Betters, Sergio Leon-Saval
  faculty_school: School of Physics
related_docs:
  - title: Safe Work Procedure
    url: /safe-work-procedures/fyla-supercon/
    description: Detailed operating procedures for the Fyla Iceblink Supercontinuum Fiber Laser
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
| **Activity or process:**<br><br>- Operation of Fyla Iceblink Supercontinuum Fiber Laser as a broadband light source<br>- Spectral filtering of supercontinuum output for photonic lantern wavefront sensing experiments<br>- Free-beam laser operation during alignment, fibre connection/disconnection, and maintenance<br>- Optical component adjustment and inspection in Room 121c | **Persons at risk:**<br><br>- Primary laser operator (1–3 authorised users)<br>- Other laboratory staff working in Room 121c<br>- Research students<br>- Visitors to the laboratory<br>- Persons in adjacent spaces if beam hazard exits Room 121c |
| **Location:**<br><br>Room 121c — photonic lantern wavefront sensing optical table | **Risk assessment team** (who was consulted?)**:**<br><br>- Laboratory supervisor<br>- Laser safety advisor<br>- Equipment users<br>- University WHS safety officer |

</div>

<div class="legislation-box" markdown="1">

**List of Legislation, Code of Practice, Australian Standards, Guidance Materials used to determine control measures**

- Work Health and Safety Act 2011
- Work Health and Safety Regulation 2017
- AS/NZS IEC 60825.1:2014 — Safety of laser products
- AS/NZS IEC 60825.2:2021 — Safety of optical fibre communication systems
- AS 2211.13-1999 — Safety of industrial laser equipment
- AS/NZS 3000:2018 — Electrical installations (Wiring Rules)
- AS/NZS 3760:2022 — In-service safety inspection and testing of electrical equipment
- Safe Work Australia, Code of Practice: Laser Pointer Safety
- University of Sydney WHS Laser Safety Policy and Procedures (Class 3B and Class 4 lasers)
- Fyla Iceblink Supercontinuum Fiber Laser User Manual [TODO: verify edition/revision]
- Fyla Iceblink Supercontinuum Fiber Laser Safety Documentation (Iceblink-v3.rev04.pdf)
- Laser Institute of America, ANSI Z136.1 (for reference — AS/NZS standards take precedence)

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
| Free-beam laser operation — direct or specularly reflected beam exposure to eyes during alignment, fibre work, or optical adjustment | Class 4 broadband laser radiation (approx. 450–2400 nm) [TODO: verify wavelength range and output power from manufacturer datasheet]; unenclosed beam at full output power | - Permanent retinal damage or blindness<br>- Corneal burns<br>- Cataract formation (NIR wavelengths)<br>- Severe injury from single exposure event | - Interlock system installed on laser output<br>- Authorised user requirement enforced by supervisors<br>- Laser safety training mandated before access<br>- Laser warning signage on door of Room 121c | **Very High** | - Mandatory broadband laser safety eyewear (OD-rated for full output spectrum including NIR) whenever laser output is unenclosed<br>- NEVER look directly into output fibre or any optical element in the beam path without verified beam block in place<br>- Limit persons in beam path area to those wearing appropriate eyewear<br>- Beam blocks/beam stops placed at table perimeter to contain stray beams<br>- Interlock MUST be armed and verified operational before every session | **Low** |
| NIR radiation exposure — invisible wavelengths (>700 nm) from supercontinuum output during any open-beam scenario | Near-infrared radiation (700–2400 nm component of supercontinuum); no pain reflex or aversion response at these wavelengths; eye may not detect hazard until damage has occurred | - Insidious lens and retinal damage without immediate awareness<br>- Cataract formation with chronic exposure<br>- Retinal damage including thermal burns to macula<br>- Injury may only become apparent hours or days later | - Broadband laser safety eyewear policy<br>- Laser safety training including NIR-specific hazard awareness | **High** | - Broadband laser safety eyewear MUST be rated for NIR wavelengths as well as visible output; standard visible-light safety glasses are INADEQUATE<br>- Training MUST explicitly cover the absence of aversion reflex for NIR wavelengths<br>- NEVER rely on pain or visual sensation as an indicator of safe exposure levels for this laser<br>- Verify eyewear OD rating covers full supercontinuum output range [TODO: confirm required OD values against calculated NHZ from manufacturer data] | **Low** |
| Fibre end-face exposure — disconnecting, connecting, or inspecting output fibre with laser active | Unsheathed fibre end emitting full laser power as a diverging beam; fibre outputs can emit at full power even when beam appears dim to the unaided eye (NIR component invisible) | - Severe eye injury from direct or near-field exposure<br>- Skin burns at fibre tip<br>- Insidious NIR injury if fibre disconnected without visible indication of emission | - Shutdown procedure requires laser to be off before fibre work<br>- Training covers fibre handling safety | **High** | - MANDATORY: Laser MUST be fully shut down and emission confirmed zero (e.g., via power meter or verified-off indicator) before any fibre connection, disconnection, or inspection<br>- Fibre end caps MUST be placed on all unused or disconnected connectors immediately<br>- NEVER inspect a fibre end face by looking directly at the end — always use an approved fibre inspection scope with IR-blocking filter<br>- Training to reinforce fibre-specific hazard | **Low** |
| Filter failure or removal — unfiltered broadband supercontinuum output reaching experiment or environment | Full broadband high-power supercontinuum output without spectral filtering; wavelengths normally blocked by experimental filters now present at full intensity | - Higher energy and broader wavelength exposure than normal filtered operation<br>- Enhanced risk of retinal and corneal damage<br>- Damage to sensitive optical components downstream of filter position<br>- Exposure to wavelengths for which standard broadband eyewear may not be rated | - Permanent filter installation in optical path of photonic lantern wavefront sensing setup<br>- Setup is designed to operate filtered | **High** | - Filters MUST be physically secured in optical mounts to prevent accidental removal or dislodgement (use locking screws or fixed mounts)<br>- Verify filter is correctly installed and unobstructed as part of mandatory pre-operation checks<br>- Define and document a separate written procedure for filter removal and replacement; filter changes require supervisor approval and laser shutdown<br>- Confirm eyewear OD rating is adequate for unfiltered output as a worst-case scenario | **Low** |
| Interlock defeat or malfunction — laser operates without interlock protection | Uncontrolled Class 4 beam propagation with no safety system intervention; interlock defeated by user action or malfunctions without detection | - Severe eye injury or permanent blindness<br>- Burns<br>- Risk extends to all persons in Room 121c, not just the operator | - Interlock installed by manufacturer on laser output<br>- Equipment supplied with interlock as standard | **Very High** | - ABSOLUTE PROHIBITION on defeating, bypassing, or disabling any interlock on this laser<br>- Interlock test MUST be performed as part of mandatory pre-operation checks each session (see SWP SAIL-SWP-FYLA-SUPERCON-001)<br>- If interlock malfunction is detected: IMMEDIATE lockout and tag-out of equipment; report to supervisor; equipment MUST NOT be used until verified by qualified laser safety technician<br>- Annual interlock verification by qualified laser safety technician<br>- Disciplinary action applies for any deliberate defeat | **Low (must not occur)** |
| Reflected and scattered radiation from optical components — specular reflections from lenses, mirrors, beam splitters, or polished metal | Secondary beams produced by specular reflection from optical surfaces; diffuse scatter from matte surfaces may also produce hazardous irradiance at close range for a Class 4 source | - Eye or skin exposure from secondary beams at unexpected angles<br>- Injury severity similar to direct beam exposure for specular reflections<br>- Persons outside intended beam path may be in path of reflected beam | - Enclosed optical setup reduces stray beam propagation<br>- Beam stops present on optical table | **High** | - NEVER wear watches, rings, or jewellery in the beam path area during laser operation<br>- Remove or cover all polished, reflective, or metallic objects from the optical table before operating<br>- Conduct beam path survey (trace path on diagram) before each new configuration<br>- Ensure beam stops are positioned at beam path perimeter to intercept stray reflections<br>- Training MUST include instruction on reflection hazards from Class 4 lasers | **Low** |
| High peak-power pulsed beam hazard — supercontinuum output has very high peak power relative to average power | Pulsed supercontinuum output with peak irradiance greatly exceeding CW equivalent at same average power [TODO: verify pulse duration, repetition rate, and peak power from manufacturer datasheet Iceblink-v3.rev04.pdf]; single pulse may exceed the Maximum Permissible Exposure (MPE) for eye | - Retinal damage from single pulse exposure<br>- Injury at average-power levels that would be safe for a CW laser of the same average power<br>- Standard CW laser hazard calculations may underestimate risk | - Laser safety eyewear required | **High** | - Laser safety eyewear MUST be rated for pulsed operation; confirm OD rating accounts for peak fluence per pulse, not just average irradiance [TODO: calculate required OD using peak pulse energy from manufacturer data and AS/NZS IEC 60825.1:2014]<br>- Training MUST explicitly cover the distinction between pulsed and CW laser hazard and the significance of peak power for MPE determination<br>- Any Nominal Hazard Zone (NHZ) calculation MUST use peak pulse parameters | **Low** |
| Bystander exposure — unprotected persons entering Room 121c during laser operation | Person without laser safety eyewear entering the laboratory while laser beam is active and unenclosed | - Eye injury from direct or scattered beam<br>- Particularly severe risk for persons unaware of laser hazard or unfamiliar with beam path geometry<br>- Visitors or maintenance personnel most vulnerable | - Laser safety signage on door of Room 121c | **High** | - Laser warning light or electrically interlocked door signage MUST be illuminated whenever laser output is enabled and beam is unenclosed [TODO: verify whether door interlock/warning light is installed in Room 121c or requires installation]<br>- Laser-in-use signage at eye level on Room 121c door, including instruction: "Laser operation in progress — do not enter without authorisation"<br>- Operator MUST brief any visitor before they enter while laser is operating<br>- Where operationally possible, laser beam MUST be fully enclosed when bystanders are expected in Room 121c | **Low** |
| Fire hazard — high-power beam incident on flammable materials in or near beam path | High-power laser beam or stray reflection incident on paper, fabric, plastic, optical table foam, or other combustible material present on or near the optical table | - Fire<br>- Smoke inhalation<br>- Equipment damage<br>- Laboratory fire requiring evacuation | - Beam path enclosed in permanent photonic lantern wavefront sensing optical setup<br>- Laser safety training covers fire hazard | **Medium** | - Remove all paper, fabric, plastic bags, and non-optical materials from the optical table and immediate vicinity before operating<br>- NEVER use inappropriate material (e.g., card, fabric, plastic) as a temporary beam block<br>- CO₂ fire extinguisher MUST be accessible within 5 m of Room 121c<br>- Ensure clear access to fire extinguisher and room exit at all times | **Low** |
| Electrical hazard from laser mainframe and power supply | 240 V AC mains voltage within laser chassis; internal power conditioning electronics | - Electric shock<br>- Electrocution<br>- Burns from arc flash | - Enclosed electrical components within laser chassis<br>- Earthed equipment chassis<br>- RCD protection on laboratory power circuit | **Medium** | - Regular electrical safety testing (test and tag) per AS/NZS 3760:2022 — annually minimum, or after any incident<br>- No user servicing of laser internal components; all internal repairs by qualified laser technician or authorised service agent only<br>- Keep laser clear of water and liquid spills<br>- Inspect power cord and connectors before each session; if damaged, do NOT use — report to supervisor | **Low** |
| Skin exposure to laser beam — direct or scattered beam incident on exposed skin during free-beam operations | High-power density radiation causing thermal and photochemical injury to skin; Class 4 laser radiation can ignite clothing and cause serious burns | - Burns to exposed skin<br>- Exacerbated injury if beam focused<br>- Photochemical injury at UV/short visible wavelengths if present in supercontinuum output | - Beam enclosed in optical setup during normal operation | **Medium** | - Long-sleeved laboratory coat or clothing in beam area during any free-beam operations or alignment<br>- Minimise skin exposure near beam path<br>- Beam stops in place to intercept stray beams<br>- Training on skin exposure hazards from Class 4 lasers | **Low** |
| Mechanical handling of output fibre and optical connectors — damage to fibre | Handling of fragile silica optical fibre; damaged fibre under power creates uncontrolled diverging laser emission at the damage point and sharp glass fragments | - Puncture wounds or lacerations from glass fragments<br>- Uncontrolled laser emission from damaged fibre section causing eye or skin exposure | - Careful handling practices | **Medium** | - Inspect output fibre for visible damage (kinks, cracks, discolouration) before each session; DO NOT operate with damaged fibre<br>- Minimum bend radius MUST be respected when routing fibre [TODO: verify minimum bend radius from manufacturer datasheet]<br>- Store fibre with end caps attached and in protective sleeve or coil holder when not in use<br>- Dispose of fibre offcuts safely: wrap in adhesive tape before placing in bin to prevent sharps injury<br>- Laser MUST be off during any fibre routing or connector changes | **Low** |

</div>

## Implementation of Additional Risk Controls

| Additional controls needed | Resources required | Responsible person | Date of implementation | RiskWare Reference |
|---|---|---|---|---|
| Write Safe Work Procedure (SWP) for operation of Fyla Iceblink (SAIL-SWP-FYLA-SUPERCON-001) | Time (approx. 2 hours) | Supervisor | Prior to use | N/A |
| Develop broadband laser safety eyewear procurement and OD verification procedure (confirm OD rating covers full supercontinuum output spectrum including NIR, and accounts for peak pulse fluence) | Time (2 hours); laser safety advisor; manufacturer datasheet (Iceblink-v3.rev04.pdf) | Safety Officer / Supervisor | Prior to use | TBD |
| Install laser-in-use door warning light or interlocked door sign for Room 121c | Warning light hardware (approx. $50–200); electrician if hardwired | Laboratory Manager / Facilities | Prior to any free-beam operation | TBD |
| Develop and display Nominal Hazard Zone (NHZ) calculation and diagram for Room 121c optical table (using peak pulse parameters per AS/NZS IEC 60825.1:2014) | Time (3 hours); laser safety advisor; manufacturer peak power data [TODO: verify peak power from Iceblink-v3.rev04.pdf] | Safety Officer | Prior to use | TBD |
| Annual interlock verification by qualified laser safety technician | Qualified laser technician; test equipment | Laboratory Manager | Annually (first check prior to initial use) | TBD |
| Mandatory laser operator training programme (Class 4 hazards, NIR-specific hazards, pulsed laser hazards, fibre safety, supercontinuum-specific hazards, emergency procedures) | Time; training materials; laser safety advisor | Laboratory Manager / Supervisor | Prior to use | N/A |
| Establish authorised user list for Fyla Iceblink and display near equipment in Room 121c | Time (1 hour); sign-in/sign-out log book | Supervisor | Prior to use | N/A |
| Confirm laser classification and output parameters from manufacturer documentation (wavelength range, average power, pulse duration, repetition rate, peak power, fibre connector type) | Fyla Iceblink datasheet (Iceblink-v3.rev04.pdf); contact Fyla if required | Supervisor | Prior to use — required to complete NHZ and OD calculations | N/A |
| Develop filter change and optical modification procedure (written procedure for any modification to beam path, including supervisor sign-off) | Time (1 hour) | Supervisor | Prior to any beam path changes | N/A |
| Ensure CO₂ fire extinguisher is accessible within 5 m of Room 121c | CO₂ fire extinguisher; signage | Laboratory Manager | Prior to use | N/A |
| Electrical safety testing (test and tag) of Fyla Iceblink per AS/NZS 3760:2022 | Qualified electrician; test equipment | Facilities | Prior to use, then annually | TBD |
| Develop and document beam path diagram for Room 121c photonic lantern wavefront sensing optical table (for use in pre-operation checks and bystander hazard assessment) | Time (1 hour); optical table schematic | Supervisor / Operator | Prior to use | N/A |
| Conduct baseline laser eye examination for all authorised users (recommended prior to first use of Class 4 laser) | Occupational health service / ophthalmologist | Laboratory Manager | Prior to use | TBD |

## List emergency controls
<small>These might include how to deal with fires, spills, emergency shutdown of equipment, exposure to hazardous materials and adverse reactions or the deteriorating condition of patients/research participants in our care.</small>

<div class="emergency-box" markdown="1">

### CRITICAL: Class 4 Laser Safety

- The Fyla Iceblink Supercontinuum Fiber Laser is a **Class 4 laser product** in free-beam configuration
- Supercontinuum output spans from visible to NIR (~450–2400 nm) [TODO: verify range]; **NIR wavelengths are invisible and provide no aversion warning**
- NEVER operate with interlock defeated or disabled
- NEVER look into the output fibre, any optical element in the beam path, or any reflection from optical components
- If any safety system fails, immediately shut down and lock out equipment

### Emergency Shutdown:

1. Turn laser key switch to STANDBY or OFF position immediately
2. If key switch is inaccessible: isolate power at the wall outlet supplying the laser
3. Do not resume operation until the emergency has been fully assessed and equipment inspected
4. Notify supervisor of any emergency shutdown

### Suspected Laser Radiation Exposure (Eye or Skin):

- **DO NOT PANIC — do not rub eyes**
- If eye exposure suspected:
  - Turn laser off immediately
  - Do not rub or touch eyes
  - Close eyes and avoid bright light
  - Seek **IMMEDIATE** medical attention at the nearest Emergency Department — note that injury from NIR wavelengths may not be immediately apparent; seek assessment regardless of symptoms
  - Bring this Risk Assessment and the laser datasheet (Iceblink-v3.rev04.pdf) to the ED to assist treating clinician
  - Call 000 if vision loss, severe eye pain, or loss of consciousness
- If skin burns from laser exposure:
  - Remove from laser beam immediately
  - Cool affected area with running cool water for 20 minutes
  - Cover with clean, non-fluffy material (cling film is ideal)
  - Seek medical attention for any laser burn
- Report incident immediately to supervisor
- Complete incident report and RiskWare notification
- Equipment MUST be locked out and inspected by qualified laser safety technician before any further use

### Fire Emergency:

1. Turn laser off immediately (key switch to STANDBY or OFF)
2. If fire is small and contained:
   - Use CO₂ fire extinguisher
   - Direct extinguisher at base of flames in short bursts
3. If fire cannot be controlled immediately:
   - Evacuate Room 121c
   - Close door behind you (do not lock)
   - Activate building fire alarm (pull station at nearest exit)
   - Call 000 (Emergency Services)
   - Notify building warden
   - Assemble at designated assembly point
   - Do not re-enter until cleared by emergency services
4. Do NOT restart equipment after a fire event — lock out and tag

### Equipment Malfunction or Interlock Failure:

1. Turn laser key switch to OFF or STANDBY immediately
2. If equipment cannot be safely shut down via key switch: isolate power at wall outlet
3. DO NOT attempt any repairs or bypass of safety systems
4. Lock out and tag the equipment with a "DO NOT USE — FAULT" tag
5. Report to supervisor and safety officer immediately
6. Arrange inspection by qualified laser safety technician
7. Equipment MUST NOT be used until all safety systems are verified functional

### Emergency Contacts:

- Emergency services: **000**
- University Security (after hours): [TODO: insert University of Sydney security number]
- Supervisor (Chris Betters): [TODO: insert contact number]
- Supervisor (Sergio Leon-Saval): [TODO: insert contact number]
- Safety Officer: [TODO: insert name and number]
- First Aiders: [listed on notice board in Room 121c / building corridor]
- Nearest Emergency Department: [TODO: insert nearest ED details]

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
