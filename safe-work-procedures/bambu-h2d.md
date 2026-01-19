---
layout: document
title: Safe Work Procedure - Bambu Lab H2D
doc_type: Safe Work Procedure
status: approved
permalink: /safe-work-procedures/bambu-h2d/
metadata:
  reference: SAIL-SWP-BAMBU-H2D-001
  title: Operation of Bambu Lab H2D Laser Edition with 10W Class 4 Laser Module
  version: "1.0"
  issue_date: January 2026
  prepared_by: Chris Betters
  supervisors: Chris Betters, Sergio Leon-Saval
  review_date: January 2027
critical_warning: |
  **BEFORE OPERATING THIS EQUIPMENT:**
  
  - You MUST have completed Class 4 laser safety training
  - You MUST be assessed as competent
  - You MUST be listed on the authorised users list
  - You MUST NEVER leave equipment unattended during laser operations
  - You MUST NEVER defeat or bypass any safety system
related_docs:
  - title: Risk Assessment
    url: /risk-assessments/bambu-h2d/
    description: Hazard identification and controls
  - title: Laser Safety Guide
    url: /laser-safety-guide/
    description: Class 4 laser safety information
show_review: true
---
## SWP Title
Operation of Bambu Lab H2D Laser Edition with 10W Class 4 Laser Module

**Prepared by:** Chris Betters  
**Responsible supervisor/s:** Chris Betters, Sergio Leon-Saval

---

## List the Hazards and Risk Controls as per Risk Assessment

**Associated risk assessment reference:** SAIL-RA-BAMBU-H2D-001

### Hazards
- Class 4 laser radiation (455nm, 10W)
- Fire and ignition
- Thermal burns (350°C nozzle, 65°C chamber)
- Inhalation of fumes and particulates
- Electrical hazards (240V)
- Moving mechanical parts
- Toxic fumes from certain materials

### Risk Controls
- Laser safety windows and interlocks
- Never operate with safety systems defeated
- Never leave unattended during laser operations
- Fire detection and emergency stop
- Mandatory training and competency assessment
- Local exhaust ventilation
- Heat-resistant gloves for hot surfaces
- Material approval process

---

## List Resources Required

### Personal Protective Equipment (PPE)

- Heat-resistant gloves (for handling hot components after printing)
- Safety glasses (general workshop protection, NOT for laser - safety windows provide laser protection)
- Respiratory protection (if required based on material SDS and ventilation assessment)
- Closed-toe shoes
- Long trousers (no shorts)
- Tie back long hair

### Equipment and Materials

- Bambu Lab H2D with 10W laser module (fully functional with all safety systems verified)
- Approved materials only (wood, leather, acrylic, etc. - see approved materials list)
- Material Safety Data Sheets (SDS) for all materials to be processed
- Bambu Studio or Bambu Suite software (latest version)
- Computer with network connection
- Clean, lint-free cloths for maintenance
- Isopropyl alcohol (IPA) for cleaning

### Safety Equipment (must be present in laboratory)

- CO₂ or dry powder fire extinguisher (within 5 metres)
- First aid kit
- Emergency eyewash station (accessible)
- Emergency contact numbers displayed
- Sign-in/sign-out log book

### Ventilation

- Local exhaust ventilation (LEV) connected and operating
- Air purifier (recommended for prolonged use)
- Exhaust ducting to outside or through appropriate filtration

---

## Step by Step Instructions for Undertaking the Task

### BEFORE STARTING - CRITICAL SAFETY REQUIREMENTS

- You must have completed Class 4 laser safety training and been assessed as competent
- You must be listed on the authorised users list for this equipment
- You must never leave the equipment unattended during laser operations
- You must never defeat or bypass any safety system

### 1. PRE-OPERATION SAFETY CHECKS (MANDATORY - DO NOT SKIP)

1. **Sign in** to the equipment log book (record name, date, time, operation type)

2. **Visual inspection of laser safety windows:**
   - Check front laser safety window (green-tinted) for cracks, chips, or damage
   - Check all side panels and top cover for damage
   - If ANY damage found: DO NOT USE - lock out and report to supervisor

3. **Test door interlocks (CRITICAL):**
   - Power on the equipment
   - Navigate to settings menu and initiate a test print or laser operation
   - Slowly open the front door - laser/print head MUST stop immediately
   - Close door and repeat test with top glass cover
   - If interlocks fail: DO NOT USE - lock out and report immediately

4. **Emergency stop test:**
   - Press the red emergency stop button
   - Verify all motion stops and alarm sounds
   - Reset emergency stop by twisting clockwise

5. **Verify local exhaust ventilation (LEV):**
   - Check exhaust ducting is connected
   - Turn on LEV/air purifier
   - Verify airflow (use tissue test if needed)

6. **Check fire extinguisher:**
   - CO₂ or dry powder extinguisher present within 5 metres
   - Check pressure gauge in green zone
   - Check clear access path to extinguisher

7. **Clear work area:**
   - Remove all flammable materials from vicinity (papers, solvents, etc.)
   - Ensure clear egress path for emergency evacuation
   - Remove clutter around equipment

### 2. MATERIAL PREPARATION AND APPROVAL

8. **Check material is approved:**
   - Consult approved materials list
   - PROHIBITED: PVC, polycarbonate, materials containing chlorine or halogens
   - If material not on approved list: seek approval from supervisor before use

9. **Review material Safety Data Sheet (SDS):**
   - Check for hazardous decomposition products
   - Note any special ventilation or PPE requirements
   - Confirm fire hazards and extinguishing methods

10. **Prepare material:**
    - Ensure material is clean and dry
    - Check material dimensions fit within build volume (350 × 320 × 325 mm for 3D printing, 310 × 270 mm for laser engraving with 10W module)
    - For laser operations: ensure material is flat and securely positioned

### 3. EQUIPMENT STARTUP

11. Power on the Bambu H2D (if not already on from safety checks)
12. Allow equipment to complete startup sequence and homing
13. Check touchscreen display for any error messages
14. Verify network connection (if remote monitoring to be used)
15. Start LEV/air purifier system

### 4. PREPARE JOB FILE

16. Open Bambu Studio or Bambu Suite software on computer
17. Import or create your design file
18. **For 3D printing:**
    - Select material type and printer settings
    - Configure support structures if needed
    - Slice the model and preview toolpaths
    - Check estimated print time and material usage
19. **For laser engraving/cutting:**
    - Use BirdsEye camera to align material on bed
    - Set laser power and speed for material type (consult manufacturer guidelines)
    - Configure air assist settings
    - Preview laser path
    - Verify material will not extend outside safe area
20. Send job file to printer via network or USB

### 5. LOAD MATERIAL

21. Open front door (equipment should be idle, not during operation)
22. **For 3D printing:**
    - Clean build plate with IPA if needed
    - Install appropriate build plate (textured PEI, smooth PEI, etc.)
    - Load filament spools into AMS (if using multi-material)
    - Verify filament type matches job requirements
23. **For laser operations:**
    - Remove build plate if necessary
    - Position material on bed using alignment guides
    - Use BirdsEye camera to verify material position
    - Ensure material is flat and won't curl during processing
    - Verify material is within safe operating area
24. Close front door securely - ensure door clicks closed

### 6. START OPERATION

25. **Final check before starting:**
    - All doors and covers closed and secured
    - LEV/air purifier running
    - Emergency stop not engaged
    - Fire extinguisher accessible
    - Clear path to emergency exit

26. Select job from touchscreen or send from computer
27. Confirm job parameters on screen
28. Press start button

29. **Monitor first few minutes closely:**
    - Watch for proper adhesion (3D printing) or correct laser focus (laser operations)
    - Listen for unusual sounds
    - Watch for excessive smoke or fumes
    - Verify material not moving or curling

30. **During laser operations - MANDATORY ATTENDANCE:**
    - You MUST remain within visual line of sight OR monitor via camera continuously
    - Never leave the room during laser cutting/engraving
    - Watch for signs of fire (flames, excessive smoke, burning smell)
    - Keep emergency stop and fire extinguisher within reach
    - If you must leave for any reason: STOP the laser operation first

31. **During 3D printing operations:**
    - Check periodically for print failures
    - Can be left unattended if print-only mode (no laser)
    - Camera monitoring recommended for long prints

### 7. COMPLETION AND SHUTDOWN

32. Wait for equipment to signal job complete

33. Allow hot components to cool:
    - Nozzle: can reach 350°C - wait minimum 10 minutes
    - Chamber: can reach 65°C - wait 5 minutes
    - Build plate: wait until below 40°C (touchscreen displays temperature)

34. Open front door carefully (watch for residual heat)

35. **Remove completed work:**
    - Wear heat-resistant gloves if components still warm
    - For 3D prints: allow to cool on plate before removal
    - For laser work: carefully remove material (may have sharp edges)
    - Place in designated area for cooling/collection

36. **Clean work area** (see cleanup section below)
37. Turn off LEV/air purifier (after ensuring adequate ventilation time)
38. If last user of the day: power down equipment via touchscreen menu
39. **Sign out** in equipment log book (record time, any issues)

---

## Emergency Shutdown Procedures

### EMERGENCY STOP - Use in any of these situations:

- Fire or smoke detected
- Any safety system failure
- Equipment malfunction
- Abnormal sounds, smells, or operation
- Laser radiation suspected (door opened during operation)
- Material movement or dislodgement
- Any unsafe condition

### EMERGENCY SHUTDOWN PROCEDURE:

1. **PRESS RED EMERGENCY STOP BUTTON IMMEDIATELY**
   - Button located on front right of equipment
   - Push firmly - button will lock in depressed position
   - Audible alarm will sound
   - All motion will stop immediately

2. **If emergency stop fails or is inaccessible:**
   - Turn off power at wall outlet
   - Pull plug if necessary

3. **Assess the situation:**
   - If fire: follow fire emergency procedures (see below)
   - If injury: call for first aid assistance
   - If equipment damage: do not restart - report to supervisor
   - If safety system failure: lock out and tag equipment

4. **Do NOT restart equipment** until:
   - Emergency has been fully resolved
   - Equipment has been inspected
   - Supervisor has given approval
   - Any necessary repairs completed
   - All safety systems verified functional

5. **Complete incident report:**
   - Record time, date, and circumstances
   - Note what emergency required shutdown
   - Report to supervisor immediately
   - Complete RiskWare report if required

### RESETTING EMERGENCY STOP (only after emergency resolved):

1. Ensure all emergency conditions resolved
2. Twist emergency stop button clockwise to release
3. Button will pop up
4. Alarm will stop
5. Equipment will not automatically restart - manual restart required
6. Perform full pre-operation safety checks before resuming work

---

## Emergency Procedures for Fires, Spills or Exposure to Hazardous Substances

### FIRE EMERGENCY:

1. **PRESS EMERGENCY STOP BUTTON**

2. **DO NOT OPEN CHAMBER DOOR** (introduces oxygen, may worsen fire)

3. **If fire is small and contained inside chamber:**
   - Fire detection system will sound alarm
   - Use CO₂ or dry powder fire extinguisher through any access points
   - Direct extinguisher at base of flames
   - Use short bursts
   - If fire does not extinguish immediately, proceed to evacuation

4. **If fire cannot be controlled or spreads:**
   - Evacuate area immediately
   - Close door behind you (do not lock)
   - Activate building fire alarm
   - Call 000 (Emergency Services)
   - Notify building warden
   - Assemble at designated assembly point
   - Do not re-enter building until cleared by emergency services

5. **After fire is extinguished:**
   - Allow equipment to cool completely
   - Do not restart - lock out and tag equipment
   - Report incident to supervisor immediately
   - Complete incident report and RiskWare entry
   - Equipment must be inspected before further use

### SUSPECTED LASER RADIATION EXPOSURE:

1. **PRESS EMERGENCY STOP IMMEDIATELY**

2. **If eye exposure suspected:**
   - Do not rub eyes
   - Close eyes or look away from bright light
   - Seek IMMEDIATE medical attention at Emergency Department
   - Call 000 if severe symptoms (vision loss, severe pain)
   - Note: Class 4 laser exposure can cause permanent blindness

3. **If skin exposure (burns):**
   - Move away from laser source
   - Cool affected area with running cool water for 20 minutes
   - Cover with clean, non-fluffy material
   - Seek medical attention if severe

4. **Document incident:**
   - Record time, duration, and circumstances of exposure
   - Note which safety system(s) failed
   - Report immediately to supervisor and safety officer
   - Complete incident report and RiskWare entry

5. **Equipment must be:**
   - Locked out and tagged immediately
   - Inspected by qualified laser safety technician
   - All safety systems verified before any further use

### THERMAL BURNS (Hot Surfaces):

1. Remove from heat source immediately
2. Cool affected area with running cool water for 20 minutes
3. Remove jewellery or tight clothing near burn (unless stuck to skin)
4. Cover burn with clean, non-fluffy material (cling film is ideal)
5. **Seek medical attention if:**
   - Burn larger than 20p coin (≥5cm)
   - Burn on face, hands, feet, joints, or genitals
   - Full thickness burn (white or charred skin)
   - Blistering
   - Unsure of severity
6. Complete first aid documentation and incident report

### EXCESSIVE FUMES OR SMOKE:

1. **PRESS EMERGENCY STOP**
2. If fumes are overwhelming:
   - Evacuate area immediately
   - Do not inhale deeply
   - Get to fresh air
3. When safe to do so:
   - Increase ventilation (open doors/windows)
   - Continue running LEV/air purifier
4. If anyone experiences symptoms (difficulty breathing, dizziness, nausea):
   - Call 000 for medical assistance
   - Keep person in fresh air
   - Provide material SDS to medical personnel
5. Investigation required:
   - Check LEV system connection and function
   - Check material type (may be prohibited)
   - Review material SDS for decomposition products
   - Report to supervisor
   - Do not resume until issue resolved

### EQUIPMENT MALFUNCTION:

1. Press emergency stop
2. Isolate power if safe to do so
3. Do NOT attempt repairs yourself
4. Lock out and tag equipment
5. Report to supervisor
6. Complete incident report

### EMERGENCY CONTACTS:

- **Emergency Services:** 000
- **University Security (after hours):** [Insert number]
- **Supervisor:** Chris Betters [Insert number]
- **Safety Officer:** [Insert name and number]
- **First Aid:** [Location and contact details]
- **Nearest Emergency Department:** [Insert details]

---

## Clean Up and Waste Disposal Requirements

### AFTER EACH USE - CLEANING PROCEDURES:

#### Build chamber and surfaces:

- Allow all components to cool to room temperature before cleaning
- Remove any loose debris, dust, or residue from build chamber
- Use lint-free cloth with isopropyl alcohol (IPA) to clean:
  - Build plate
  - Laser safety windows (interior and exterior) - ensure no residue that could affect laser protection
  - Front door window
  - Any smoke/dust deposits on internal surfaces
- Do NOT use water or harsh chemicals on electronic components

#### Laser optics and air assist (after laser operations):

- Check laser lens for smoke residue or debris
- Clean if necessary using approved lens cleaning materials only
- Check air assist nozzle for blockages
- Clear any debris from air assist system

#### Exhaust system and filters:

- Check exhaust system for blockages weekly
- Inspect air filter condition
- Replace filters according to schedule (quarterly or when visibly saturated)
- Clean or replace according to manufacturer guidelines
- Document filter changes in maintenance log

#### Work area:

- Remove all materials, tools, and personal items
- Dispose of waste properly (see below)
- Wipe down surrounding benches
- Return fire extinguisher to proper location if moved
- Leave area clean and tidy for next user

### WASTE DISPOSAL:

#### 3D printing waste:

- Failed prints, support material → General waste or recycling if material is recyclable (check material type)
- Filament offcuts → Store for potential reuse or dispose in general waste
- Empty filament spools → Recycling (plastic recycling bin)

#### Laser processing waste:

- Wood/paper offcuts → General waste or composting if uncontaminated
- Acrylic offcuts → General waste (not recyclable if laser-cut due to residue)
- Leather offcuts → General waste
- Metal sheet offcuts → Metal recycling
- Any waste contaminated with hazardous materials → Consult SDS and dispose as hazardous waste if required

#### Cleaning materials:

- IPA-contaminated cloths → Allow to dry in well-ventilated area, then general waste
- Used filters → Sealed bag, then general waste (or hazardous waste if heavily contaminated)

#### Hazardous waste:

- Any material that produced toxic fumes during processing
- Contaminated cleaning materials
- Dispose via university hazardous waste system
- Label clearly and contact waste management

### MONTHLY DEEP CLEANING:

- Clean linear guides and lubricate with appropriate lubricant
- Clean lead screws and apply grease
- Vacuum chamber exhaust fan and vents
- Clean part cooling fan and air ducts
- Inspect all moving parts for wear
- Document in maintenance log

---

## References Used in the Development of This SWP

- AS/NZS IEC 60825.1:2014 - Safety of laser products
- AS 2211.13-1999 - Safety of industrial laser equipment
- Work Health and Safety Act 2011
- Work Health and Safety Regulation 2017
- AS/NZS 3000:2018 - Electrical installations (Wiring Rules)
- AS 1940-2017 - Storage and handling of flammable and combustible liquids
- Bambu Lab H2D User Manual (latest version)
- Bambu Lab H2D Laser Safety Document (wiki.bambulab.com/en/h2/laser-safety-document)
- Bambu Lab H2D Technical Specifications
- Risk Assessment SAIL-RA-BAMBU-H2D-001
- University of Sydney WHS Laser Safety Policy and Procedures
- University of Sydney WHS Fire Safety Procedures
- Material Safety Data Sheets (SDS) for approved materials

---

## Competency Required

### MANDATORY TRAINING (Must be completed before authorisation):

#### 1. Class 4 Laser Safety Training

- Understanding of laser classifications
- Class 4 laser hazards (eye damage, burns, fire)
- How safety systems work (interlocks, windows)
- Consequences of defeating safety systems
- Emergency procedures for laser exposure
- Legal responsibilities

#### 2. Equipment-Specific Training

- Bambu H2D operation (3D printing and laser functions)
- Safety system verification procedures
- Pre-operation checks
- Software operation (Bambu Studio/Suite)
- Material preparation and loading
- Emergency stop and shutdown procedures

#### 3. Fire Safety Training

- Fire extinguisher operation (CO₂ and dry powder types)
- Fire emergency procedures
- Building evacuation procedures

#### 4. Hazardous Materials Awareness

- Reading and interpreting SDS
- Prohibited materials (PVC, polycarbonate, etc.)
- Fume hazards and controls
- Material approval process

#### 5. First Aid (Basic)

- Thermal burns treatment
- When to seek medical attention
- Location of first aid equipment

### COMPETENCY ASSESSMENT:

#### Theory Assessment:

- Written test or oral examination covering:
  - Class 4 laser hazards and safety systems
  - Pre-operation safety checks
  - Emergency procedures
  - Prohibited materials
  - Equipment limitations
- Must achieve 100% on safety-critical questions
- Minimum 80% overall pass mark

#### Practical Assessment:

- Supervised practical demonstration of:
  - Complete pre-operation safety checks (including interlock testing)
  - Material preparation and approval process
  - Equipment startup procedure
  - Loading material safely
  - Starting and monitoring a job (3D print or laser operation)
  - Emergency stop activation and reset
  - Safe shutdown and cleanup
- Assessor must observe and verify competency in all areas
- Any safety-critical errors require retraining and reassessment

### ONGOING REQUIREMENTS:

- Annual refresher training on laser safety
- Retraining required if:
  - Any safety incident involving this equipment
  - Safety procedures are updated
  - Unsafe practices observed
  - Extended period of non-use (>12 months)
- Baseline eye examination recommended before authorisation
- Periodic eye examinations if frequent laser user (consult occupational health)

### RECORD KEEPING:

- Training records maintained by supervisor
- Competency assessment documented on sign-off sheet
- Authorised users list updated and displayed
- Training refresher dates tracked

---

## Staff Approved to Assess Competence for This SWP

### Authorised Assessors:

The following staff members are authorised to assess competency for operation of the Bambu Lab H2D Laser Edition:

- Chris Betters (Supervisor) - Contact: [insert details]
- Sergio Leon-Saval (Supervisor) - Contact: [insert details]
- [Additional authorised assessors to be added]

### Assessor Requirements:

To be authorised as an assessor, staff must:

- Have completed Class 4 laser safety training
- Be competent and experienced in operation of Bambu H2D
- Understand all safety systems and their verification
- Be familiar with emergency procedures
- Have authority to authorise equipment use
- Be approved by laboratory manager or safety officer

### Assessment Process:

1. Trainee completes all mandatory training modules
2. Assessor conducts theory assessment (written or oral)
3. Assessor supervises practical demonstration
4. Assessor verifies competency in all required areas
5. If competent: Assessor signs trainee off on sign-off sheet
6. If not yet competent: Additional training and practice required, then reassessment
7. Once signed off: Trainee added to authorised users list

### Authorised Users List:

- Maintained by laboratory manager
- Displayed near equipment
- Updated when new users authorised
- Reviewed annually
- Users removed if retraining required and not completed

---

## SWP Sign Off Sheet

**SWP name and version:** Operation of Bambu Lab H2D Laser Edition with 10W Class 4 Laser Module  
**Version:** 1.0 - January 2026

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

- **Annually** (by January 2027)
- After any incident involving this equipment
- When equipment is modified or upgraded
- When new hazards are identified
- When procedures change
- When Australian Standards are updated

---

*End of Safe Work Procedure*
