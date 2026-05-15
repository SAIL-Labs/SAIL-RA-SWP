---
layout: document
title: Safe Work Procedure - Fyla Iceblink Supercontinuum Fiber Laser
doc_type: Safe Work Procedure
status: Draft
permalink: /safe-work-procedures/fyla-supercon/
equipment_name: "Fyla Iceblink Supercontinuum Fiber Laser"
reference: "SAIL-SWP-FYLA-SUPERCON-001"
version: "1.0"
description: "Safe work procedure for operation of the Fyla Iceblink Supercontinuum Fiber Laser as a filtered broadband light source in the photonic lantern wavefront sensing setup in Room 121c, including mandatory pre-operation safety checks, interlock verification, laser startup and shutdown, emergency procedures, and competency requirements."
includes: "Mandatory safety checks, interlock testing, fibre handling procedures, emergency procedures, cleanup protocols, competency and training requirements"
metadata:
  reference: SAIL-SWP-FYLA-SUPERCON-001
  title: Operation of Fyla Iceblink Supercontinuum Fiber Laser in Photonic Lantern Wavefront Sensing Setup
  version: "1.0"
  issue_date: May 2026
  next_review_date: May 2027
  prepared_by: Claude (AI draft, awaiting expert review)
  supervisors: Chris Betters, Sergio Leon-Saval
  faculty_school: School of Physics
related_docs:
  - title: Risk Assessment
    url: /risk-assessments/fyla-supercon/
    description: Hazard identification and risk controls for the Fyla Iceblink Supercontinuum Fiber Laser
show_review: true
---

## SWP Title

Operation of Fyla Iceblink Supercontinuum Fiber Laser in Photonic Lantern Wavefront Sensing Setup

**Prepared by:** Claude (AI draft, awaiting expert review)
**Responsible supervisor/s:** Chris Betters, Sergio Leon-Saval

---

## List the Hazards and Risk Controls as per Risk Assessment

**Associated risk assessment reference:** SAIL-RA-FYLA-SUPERCON-001

### Hazards

- Class 4 broadband laser radiation (visible to NIR, approx. 450–2400 nm) [TODO: verify wavelength range]
- Invisible near-infrared (NIR) radiation without aversion reflex
- High peak power pulsed output
- Fibre end-face exposure (disconnection or inspection under power)
- Filter failure or removal causing unfiltered broadband exposure
- Interlock defeat or malfunction
- Reflected and scattered radiation from optical components
- Bystander exposure from unprotected persons entering Room 121c
- Fire from high-power beam on flammable materials
- Electrical hazard from laser mainframe (240 V AC)

### Risk Controls

- Broadband laser safety eyewear (OD-rated for full output spectrum including NIR) MUST be worn during all free-beam operations
- Interlock MUST be armed and tested before every session
- Laser MUST be fully shut down before any fibre connection, disconnection, or inspection
- Beam path enclosed in photonic lantern optical setup during normal operation
- Filters physically secured in optical mounts; verified before each session
- Laser warning signage on Room 121c door; laser-in-use indicator when beam is active and unenclosed
- Authorised users list enforced; mandatory Class 4 laser safety training before access
- No jewellery or reflective items in beam path area
- CO₂ fire extinguisher within 5 m of Room 121c
- Annual interlock verification by qualified laser safety technician

---

## List Resources Required

### Personal Protective Equipment (PPE)

- **Broadband laser safety eyewear** — rated for the full supercontinuum output spectrum including NIR wavelengths; OD value MUST account for peak pulse irradiance [TODO: specify exact eyewear model, wavelength range covered, and OD values after NHZ calculation]
- Long-sleeved laboratory coat or clothing during any free-beam operations
- Closed-toe shoes (standard laboratory requirement)

### Equipment and Materials

- Fyla Iceblink Supercontinuum Fiber Laser (key, power cord, and chassis fully intact)
- Photonic lantern wavefront sensing optical setup in Room 121c
- Optical power meter or calibrated detector for verifying laser output and confirming shutdown
- Fibre end caps (for all disconnected fibre connectors)
- Equipment log book

### Safety Equipment (must be present in Room 121c before operating)

- CO₂ fire extinguisher within 5 m — pressure gauge in green zone
- First aid kit accessible
- Emergency contact numbers displayed on notice board
- Laser-in-use warning sign for Room 121c door
- Beam stops at optical table perimeter

### Ventilation

- Normal laboratory ventilation adequate for this equipment (no significant fume hazard)

---

## Step by Step Instructions for Undertaking the Task

### BEFORE STARTING — CRITICAL SAFETY REQUIREMENTS

- You MUST have completed Class 4 laser safety training (including NIR and pulsed laser hazard modules) and been assessed as competent before using this equipment
- You MUST be listed on the authorised users list for the Fyla Iceblink in Room 121c
- You MUST NEVER defeat, bypass, or disable the interlock on this laser under any circumstances
- You MUST NEVER look into the output fibre or any optical element in the beam path
- You MUST NEVER connect or disconnect fibre connectors while the laser is active

---

### 1. PRE-OPERATION SAFETY CHECKS (MANDATORY — DO NOT SKIP)

**If ANY check fails: DO NOT USE — lock out equipment, attach a "DO NOT USE — FAULT" tag, and report to supervisor immediately.**

1. **Sign in** to the equipment log book: record your name, date, time, and planned operation.

2. **Verify no unauthorised persons** are in Room 121c, or brief anyone present on the laser hazard and confirm they will not enter the beam path area without appropriate eyewear.

3. **Check laser safety signage** is displayed on the Room 121c door. Confirm the laser-in-use warning sign is available and ready to be placed when operation commences.

4. **Inspect laser safety eyewear:**
   - Confirm eyewear is rated for the full supercontinuum output spectrum including NIR [TODO: verify required OD values]
   - Check for scratches, cracks, or damage to the optical filter element
   - If any damage is found: DO NOT USE — report and replace before proceeding

5. **Verify beam enclosure integrity:**
   - Inspect all enclosure panels and covers on the photonic lantern wavefront sensing optical setup
   - Confirm there are no gaps, open ports, or dislodged covers in the beam path
   - Confirm all beam stops are in their correct positions at the optical table perimeter

6. **Verify output filter installation:**
   - Confirm the spectral filter is correctly seated in its mount in the optical path
   - Confirm locking screws or retention mechanism are engaged
   - DO NOT proceed if filter is missing, misaligned, or appears damaged

7. **Check for reflective objects in beam path area:**
   - Remove or cover all watches, rings, and jewellery before operating
   - Remove all non-optical metallic, polished, or reflective items from the optical table surface
   - Remove paper, fabric, plastics, and other flammable materials from the optical table

8. **Test interlock function (CRITICAL):**
   - Power on the laser to standby mode [TODO: verify exact procedure for entering standby without enabling emission — refer to Iceblink-v3.rev04.pdf]
   - Initiate test sequence to verify interlock: trigger the interlock (e.g., open the designated interlock circuit) while laser is enabled
   - Confirm laser emission ceases immediately when interlock is triggered
   - Reset interlock and verify emission resumes on command
   - If interlock fails to interrupt emission: IMMEDIATELY shut down laser, lock out, and report to supervisor — DO NOT USE

9. **Check fire extinguisher:**
   - CO₂ fire extinguisher is present and accessible within 5 m of Room 121c
   - Pressure gauge is in the green zone
   - Access path to extinguisher is unobstructed

10. **Confirm no unauthorised modifications** to the optical setup since the last session (check against beam path diagram if available). Report any unexpected changes to supervisor before proceeding.

---

### 2. LASER STARTUP

11. Confirm laser key switch is in the OFF or STANDBY position before connecting power.

12. Turn ON the main power switch at the rear of the Fyla Iceblink chassis [TODO: verify power switch location from Iceblink-v3.rev04.pdf].

13. Allow the laser to complete its self-test and initialisation sequence. Wait for the front panel display to indicate ready or standby status [TODO: verify display messages and startup duration from manufacturer manual].

14. Check the front panel display for any fault, warning, or error messages. If any fault message is present: DO NOT enable laser emission — consult manufacturer documentation for fault meaning and report to supervisor.

15. Insert the laser key and turn to the STANDBY position [TODO: verify key switch positions and labelling from Iceblink-v3.rev04.pdf].

16. Verify the interlock indicator shows ARMED/ACTIVE status on the front panel [TODO: confirm indicator label and appearance from manual].

17. Set the power/attenuation control to the minimum output level before enabling emission.

18. Place the laser-in-use warning sign on the Room 121c door.

19. **Don laser safety eyewear** — MUST be worn before enabling laser emission.

20. Enable laser emission by turning key to the ENABLE or ON position [TODO: verify key position labelling from Iceblink-v3.rev04.pdf].

21. Verify emission indicator is illuminated on the front panel.

22. Confirm laser output is reaching the photonic lantern wavefront sensing setup as expected (e.g., via calibrated detector or known test measurement) without approaching any unenclosed beam path elements.

23. Gradually increase laser power to the required operating level for the experiment. Record the operating power in the log book.

---

### 3. OPERATION

24. Confirm beam enclosure is intact and no free-beam elements of the optical path are accessible to unprotected persons.

25. **During operation:**
    - Remain within Room 121c or ensure the laser-in-use sign is clearly visible and the interlock is armed if briefly leaving the room
    - NEVER leave the laser operating in an unlocked room with no occupant when the beam path is unenclosed
    - Monitor for any unusual sounds, smells, or visible changes to the laser output (e.g., mode instability, unexpected brightness changes)
    - If any anomaly is observed: shut down laser immediately and investigate before resuming

26. **During any optical alignment or adjustment (free-beam operations):**
    - Ensure laser safety eyewear is on before the beam path is opened
    - Reduce laser output power to the minimum level required for alignment tasks
    - Use alignment tools (e.g., beam profiler card or IR sensor card) to locate and verify the beam path — NEVER use your eye directly
    - Ensure all bystanders have appropriate eyewear or are outside Room 121c
    - Laser-in-use sign MUST be on the door whenever the beam path is unenclosed

27. Record any significant observations, settings changes, or anomalies in the log book.

---

### 4. COMPLETION AND SHUTDOWN

28. Reduce laser output power to the minimum setting.

29. Turn the key switch to STANDBY position to disable laser emission [TODO: verify key position from manufacturer manual].

30. Confirm emission has ceased using the panel indicator and, where possible, verify with a power meter at the output.

31. Allow a brief warm-down period as specified in manufacturer documentation [TODO: verify recommended warm-down procedure from Iceblink-v3.rev04.pdf].

32. Turn the main power switch to OFF.

33. **Remove the laser key** from the key switch and store securely (key must remain with the authorised user or be returned to designated secure storage).

34. Replace fibre end caps on any disconnected or exposed fibre connectors.

35. Remove the laser-in-use warning sign from the Room 121c door.

36. **Sign out** in the equipment log book — record shutdown time and note any issues, anomalies, or maintenance required.

---

## Emergency Shutdown Procedures

### USE EMERGENCY SHUTDOWN IN ANY OF THESE SITUATIONS:

- Fire or smoke detected in Room 121c or on the optical table
- Any safety system failure (interlock malfunction, enclosure breach)
- Equipment malfunction, abnormal noise, smell, or behaviour from laser
- Suspected laser radiation exposure (eye or skin)
- Any unsafe condition or unexpected beam behaviour
- Power outage or electrical fault

### EMERGENCY SHUTDOWN PROCEDURE:

1. **Turn the laser key switch immediately to OFF or STANDBY** — this is the primary and fastest shutdown method.

2. **If the key switch is inaccessible or ineffective:**
   - Turn off the main power switch at the rear of the laser chassis
   - As a last resort, isolate power at the wall outlet supplying the laser

3. **Assess the situation:**
   - If fire: follow the fire emergency procedure (see below)
   - If laser radiation exposure suspected: follow the laser exposure emergency procedure
   - If equipment malfunction: lock out and tag; do NOT restart
   - If interlock failure: lock out and tag; do NOT restart; notify supervisor

4. **DO NOT restart the laser** until:
   - The emergency has been fully resolved and documented
   - Equipment has been inspected (by qualified laser safety technician if safety systems were involved)
   - Supervisor has given written approval to resume
   - All safety systems have been verified functional

5. **Complete an incident report:**
   - Record time, date, and circumstances in the log book
   - Report to supervisor immediately
   - Complete a RiskWare entry if required (any incident involving potential laser exposure, fire, or equipment malfunction)

### RESETTING AFTER EMERGENCY SHUTDOWN (only after emergency fully resolved):

1. Confirm all emergency conditions are resolved and equipment is safe
2. Perform a full set of pre-operation safety checks (Section 1 of this SWP)
3. Obtain supervisor approval before resuming operation
4. Restart the laser following the startup procedure (Section 2 of this SWP)

---

## Emergency Procedures for Fires, Laser Exposure, and Equipment Malfunction

### SUSPECTED LASER RADIATION EXPOSURE (EYE OR SKIN):

1. **Turn laser off immediately** (key switch to OFF or STANDBY)

2. **If eye exposure suspected:**
   - Do NOT rub eyes
   - Close eyes or look away from all bright light sources
   - Seek **IMMEDIATE** medical attention at the Emergency Department — **do not delay even if no immediate symptoms; NIR wavelengths can cause damage that is not immediately apparent**
   - Call 000 if there is vision loss, severe eye pain, or inability to function
   - Bring the Fyla Iceblink Safety Documentation (Iceblink-v3.rev04.pdf) and this Risk Assessment to the treating clinician to describe the laser type, wavelength range, and output characteristics
   - Note and report: time of exposure, duration, which part of the setup was involved, whether eyewear was worn

3. **If skin burns from laser radiation:**
   - Move away from the laser and beam path area
   - Cool the affected area with running cool water for a minimum of 20 minutes
   - Remove jewellery or tight clothing near the burn (unless stuck to skin)
   - Cover with clean, non-fluffy material (cling film is ideal)
   - Seek medical attention for any laser-caused burn

4. **Immediately after any exposure event:**
   - Report to supervisor
   - Lock out and tag the laser
   - Complete incident report and RiskWare entry
   - Equipment must be inspected by qualified laser safety technician before further use

### FIRE EMERGENCY:

1. Turn laser key switch to OFF or STANDBY immediately

2. If fire is small and contained on the optical table:
   - Use the CO₂ fire extinguisher (direct at base of flames in short bursts)
   - Do not introduce water to the optical table (electrical components present)

3. If fire cannot be controlled immediately, or is spreading:
   - Evacuate Room 121c
   - Close the door behind you (do not lock)
   - Activate building fire alarm (pull station at nearest exit)
   - Call 000 (Emergency Services)
   - Notify building warden
   - Assemble at designated assembly point
   - Do not re-enter until cleared by emergency services

4. After any fire event:
   - Lock out and tag the laser — DO NOT restart
   - Report to supervisor immediately
   - Complete incident report and RiskWare entry

### EQUIPMENT MALFUNCTION:

1. Turn laser key switch to OFF or STANDBY
2. If unable to shut down safely via key switch: isolate power at wall outlet
3. DO NOT attempt any repairs or internal inspection of the laser yourself
4. Lock out and tag equipment: "DO NOT USE — FAULT"
5. Report to supervisor immediately with a description of the malfunction
6. Arrange inspection by qualified laser safety technician or authorised Fyla service agent
7. Complete incident report

### EMERGENCY CONTACTS:

- **Emergency services:** 000
- **University Security (after hours):** [TODO: insert University of Sydney security number]
- **Supervisor (Chris Betters):** [TODO: insert contact number]
- **Supervisor (Sergio Leon-Saval):** [TODO: insert contact number]
- **Safety Officer:** [TODO: insert name and contact number]
- **First Aiders:** [listed on notice board in Room 121c / building corridor]
- **Nearest Emergency Department:** [TODO: insert nearest ED name and address]

---

## Clean Up and Waste Disposal Requirements

### AFTER EACH SESSION:

1. Confirm laser is shut down and key removed (refer to shutdown procedure, steps 28–36).

2. Replace all fibre end caps on disconnected or exposed connectors.

3. Return all tools, measurement equipment, and personal items to designated storage locations.

4. Remove the laser-in-use sign from the Room 121c door.

5. Remove and safely store laser safety eyewear (in case, not on the optical table).

6. Inspect the optical table for any dropped or misplaced items; clear the table of non-optical materials.

### WASTE DISPOSAL:

- **Used fibre offcuts:** wrap in adhesive tape before placing in the general waste bin to prevent sharps injury
- **Damaged or expired laser safety eyewear:** dispose of via university equipment disposal process; do not reuse damaged eyewear
- **General laboratory waste:** follow standard laboratory waste procedures for Room 121c
- **Electrical or electronic components:** do not dispose of in general waste; contact laboratory manager for electronic waste disposal

### PERIODIC MAINTENANCE:

- Inspect output fibre for damage at least monthly; replace if any kinks, cracks, or discolouration observed
- Clean laser chassis exterior and optical table area as required
- Document any maintenance performed in the equipment log book
- Report any concerns about laser performance or optical output stability to supervisor

---

## References Used in the Development of This SWP

- AS/NZS IEC 60825.1:2014 — Safety of laser products
- AS/NZS IEC 60825.2:2021 — Safety of optical fibre communication systems
- AS 2211.13-1999 — Safety of industrial laser equipment
- Work Health and Safety Act 2011
- Work Health and Safety Regulation 2017
- AS/NZS 3760:2022 — In-service safety inspection and testing of electrical equipment
- Fyla Iceblink Supercontinuum Fiber Laser User Manual [TODO: verify edition/revision]
- Fyla Iceblink Safety Documentation (Iceblink-v3.rev04.pdf)
- Risk Assessment SAIL-RA-FYLA-SUPERCON-001
- University of Sydney WHS Laser Safety Policy and Procedures

---

## Competency Required

### MANDATORY TRAINING (must be completed and assessed before authorisation to operate):

#### 1. Class 4 Laser Safety Training

- Laser classifications and what Class 4 means in practice
- Mechanism of laser eye and skin injury
- NIR-specific hazards: why invisible wavelengths are particularly dangerous, absence of aversion reflex
- Pulsed laser hazards: distinction between average power and peak power for exposure limits
- How the interlock system functions and why defeating interlocks is prohibited
- Legal and personal responsibilities under the WHS Act 2011

#### 2. Supercontinuum Laser and Fibre Laser Specific Training

- Supercontinuum generation: what makes these lasers unique (broadband output, pulsed nature, high peak power)
- Understanding the Fyla Iceblink front panel, key switch, indicators, and controls
- Output fibre safety: why disconnection under power is prohibited; how to inspect and handle fibres safely
- Filter system in the photonic lantern wavefront sensing setup: what the filters do, how to verify they are installed, what to do if a filter is missing or damaged
- Beam path geometry in Room 121c: where the beam travels, location of beam stops, and where reflections may occur

#### 3. Pre-Operation Safety Check Procedure

- Step-by-step walk-through of all mandatory pre-operation safety checks in this SWP
- How to test the interlock correctly
- What to do if any check fails

#### 4. Emergency Procedures

- Emergency shutdown procedure (laser key switch and alternative methods)
- Laser radiation exposure response: eye and skin, with emphasis on seeking immediate medical attention
- Fire emergency procedure for Room 121c
- Who to call and when

#### 5. Laboratory Safety (University of Sydney Requirements)

- Reading and interpreting Safety Data Sheets (SDS)
- Use of CO₂ fire extinguisher
- Building evacuation procedures
- Incident reporting via RiskWare

### COMPETENCY ASSESSMENT:

#### Theory Assessment:

- Written or oral examination covering:
  - Class 4 laser hazards including NIR and pulsed laser distinctions
  - Interlock function and prohibition on defeat
  - Mandatory pre-operation safety checks
  - Correct emergency procedures (laser exposure, fire, malfunction)
  - Fibre handling safety
- **100% pass required on all safety-critical questions**
- Minimum 80% overall pass mark

#### Practical Assessment:

Assessor must observe the trainee independently demonstrate, in Room 121c with the Fyla Iceblink:

1. All mandatory pre-operation safety checks in correct sequence, including interlock test
2. Correct laser startup procedure (from key-off to emission enabled)
3. Identification and correct use of broadband laser safety eyewear
4. Correct shutdown procedure
5. Correct response to a simulated interlock failure (shut down, lock out, notify)
6. Location and operation of CO₂ fire extinguisher
7. Completion of equipment log book entry

Any safety-critical error during practical assessment requires retraining and reassessment before authorisation.

### ONGOING REQUIREMENTS:

- Annual refresher training in laser safety
- Retraining required if:
  - Any safety incident involving this equipment
  - Safety procedures are updated or equipment is modified
  - Unsafe practices are observed
  - No laser use for more than 12 consecutive months
- Baseline eye examination recommended before first authorised use of any Class 4 laser (consult occupational health or ophthalmologist)
- Periodic eye examination if regular Class 4 laser user (consult occupational health for frequency)

### RECORD KEEPING:

- All training records maintained by supervisor in personnel file
- Competency assessment documented on SWP Sign Off Sheet (below)
- Authorised users list updated, displayed near equipment in Room 121c, and reviewed annually
- Refresher training dates tracked and upcoming dates notified to users

---

## Staff Approved to Assess Competence for This SWP

### Authorised Assessors:

The following staff are authorised to assess competency for operation of the Fyla Iceblink Supercontinuum Fiber Laser:

- Chris Betters (Supervisor) — Contact: [TODO: insert details]
- Sergio Leon-Saval (Supervisor) — Contact: [TODO: insert details]
- [Additional authorised assessors to be added by supervisor]

### Assessor Requirements:

To be authorised as an assessor, staff must:

- Hold a current Class 4 laser safety qualification or equivalent recognised training
- Be experienced and competent in operation of the Fyla Iceblink and the Room 121c optical setup
- Understand all safety systems, interlock function, and fibre handling procedures
- Be familiar with all emergency procedures in this SWP
- Have authority to authorise equipment access (i.e., be a supervisor or laboratory manager)
- Have approval from the laboratory manager or safety officer to assess competency

### Assessment Process:

1. Trainee completes all mandatory training modules
2. Assessor conducts theory assessment (written or oral)
3. Assessor supervises and evaluates practical demonstration in Room 121c
4. Assessor confirms competency in all required areas
5. If competent: Assessor and trainee sign the SWP Sign Off Sheet; trainee added to authorised users list
6. If not yet competent: identify gaps, provide additional training and practice, then conduct reassessment
7. Authorised users list updated and displayed

---

## SWP Sign Off Sheet

**SWP name and version:** Operation of Fyla Iceblink Supercontinuum Fiber Laser in Photonic Lantern Wavefront Sensing Setup — Version 1.0 — May 2026

**In signing this section the assessor agrees that the following persons are competent in following this SWP.**

| Name | Signature | Date Competent | Name of Assessor/Authoriser | Assessor/Authoriser Signature |
|------|-----------|----------------|------------------------------|-------------------------------|
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |
|      |           |                |                              |                               |

---

## Document Review Schedule

This SWP must be reviewed:

- **Annually** (by May 2027)
- After any safety incident involving this equipment
- When the laser, optical setup, or operational procedures are modified or upgraded
- When new hazards are identified
- When relevant Australian Standards are updated
- When University of Sydney WHS laser safety policy is updated

---

*End of Safe Work Procedure*
