---
layout: document
title: Safe Work Procedure - 3SAE Combiner Manufacturing System (CMS)
doc_type: Safe Work Procedure
status: Draft
permalink: /safe-work-procedures/3sae-cms/
equipment_name: "3SAE Combiner Manufacturing System (CMS)"
reference: "SAIL-SWP-CMS-001"
version: "1.0"
description: "Detailed operating procedures for the 3SAE CMS plasma-based fibre processing system. Covers pre-operation checks, plasma operation safety, fiber handling, emergency procedures, and competency requirements."
includes: "Pre-operation safety checks, plasma system operation, fiber cleaving procedures, emergency shutdown, mandatory training requirements"
metadata:
  reference: SAIL-SWP-CMS-001
  title: Operation of 3SAE Combiner Manufacturing System (CMS)
  version: "1.0"
  issue_date: January 2026
  prepared_by: Chris Betters
  supervisors: Chris Betters, Sergio Leon-Saval
  review_date: January 2027
critical_warning: |
  **BEFORE OPERATING THIS EQUIPMENT:**

  - You MUST have completed manufacturer training and been assessed as competent
  - You MUST be listed on the authorised users list
  - You MUST complete ALL pre-operation safety checks before every session
  - You MUST maintain a 500mm exclusion zone during plasma operation
  - You MUST NEVER disable safety interlocks or protective systems
  - You MUST NEVER leave the system unattended during operation
  - You MUST NEVER touch components during or immediately after plasma operation
  - You MUST NEVER operate if any safety system appears faulty
related_docs:
  - title: Risk Assessment - 3SAE CMS
    url: /risk-assessments/3sae-cms/
    description: Hazard identification and risk controls
  - title: Manufacturer Product Information
    url: https://3sae.com/wp-content/uploads/2024/01/CMS.pdf
    description: Official 3SAE CMS specifications
show_review: true
---

## SWP Title
Operation of 3SAE Combiner Manufacturing System (CMS) for Fibre Optic Glass Processing

**Prepared by:** Chris
**Responsible supervisor/s:** [To be completed]

---

## List the Hazards and Risk Controls as per Risk Assessment

**Associated risk assessment reference:** SAIL-RA-CMS-001

### Hazards
- High-temperature plasma operation (300°C to >3000°C)
- Compressed air system at high pressure (6.2 bar / 90 psi)
- Electrical systems (dual 24V 200W power supplies)
- Optical radiation from plasma and intense lighting
- Sharp glass fibres, cleaved ends, and diamond cleaving blade
- Vacuum system operation during partial vacuum processes
- Chemical hazards from electrode materials and cleaning agents
- Ergonomic strain from precision work and prolonged operation
- Equipment complexity requiring high level of competency
- Software and control system operation

### Risk Controls
- Mandatory training and competency assessment before operation
- Complete pre-operation safety checks before every session
- Minimum 500mm exclusion zone during plasma operation
- Appropriate personal protective equipment (PPE) for all tasks
- Never operate alone as an inexperienced user (supervision required)
- Emergency stop button tested before each session
- Minimum 15-minute cooling period before accessing processing chamber
- All flammable materials removed from 1-metre radius
- Safety interlocks verified functional before operation
- Immediate reporting of any malfunctions or safety concerns
- Regular equipment inspections and maintenance
- Clear emergency procedures displayed and understood
- Authorised users list maintained and enforced

---

## List Resources Required

### Personal Protective Equipment (PPE)

- **Safety glasses (mandatory at all times):** Close-fitting design to prevent glass fragment entry; must be worn whenever handling optical fibres or operating equipment
- **Heat-resistant gloves:** Must be available and used when handling any components after plasma processing (not for use during active operation near plasma)
- **Nitrile gloves (recommended):** For handling optical fibres (provides cut protection and dexterity); mandatory when handling electrodes or cleaning chemicals
- **Laboratory coat or protective clothing:** To protect against glass fragments and potential chemical splashes
- **Closed-toe shoes (mandatory):** No open-toed footwear permitted in laboratory

### Equipment and Materials

- 3SAE Combiner Manufacturing System (CMS-01-0100)
- PC with CMS control software, monitor (23" or 40" depending on configuration)
- Optical fibres for processing (125μm to 2mm diameter as required)
- Appropriate fibre holders for diameter being processed (250μm, 400μm, 700μm, 1000μm, 1500μm, 2000μm, 2500μm)
- End cap holders if performing end cap splicing
- Electrode cleaning kit (cleaning discs provided with system)
- Spare electrode sets
- Cleaning materials for fibre preparation (isopropanol, lint-free wipes)
- Thermal inspection camera (for verifying cool-down before handling)

### Safety Equipment (must be present in laboratory)

- Fire extinguisher suitable for electrical fires (CO₂ or dry powder type) within 10 metres of equipment; location: [specify]
- First aid kit including splinter removal tools; location: [specify]
- Emergency eyewash station; location: [specify]
- Sharps disposal container for glass waste; location: within arm's reach of work area
- Emergency stop button (integrated into CMS system)
- Compressed air emergency shut-off valve; location: [specify]
- Mains power isolator for CMS; location: [specify]
- Emergency contact numbers displayed prominently
- Equipment operation logbook
- Incident report forms

### Environmental Requirements

- Compressed air supply: 6.2 bar (90 psi), 126 L/min (4.5 cfm) minimum
- Electrical supply: Dual 24V 200W power sources (mains supply with RCD protection)
- Adequate bench space: Minimum 1 metre clearance on all sides of equipment
- Adequate lighting: Minimum 500 lux at work surface
- Adequate ventilation: For heat dissipation and any electrode fumes
- Stable work surface: Capable of supporting 75 kg equipment weight
- Ambient temperature control: Equipment operates best in controlled environment

---

## Step by Step Instructions for Undertaking the Task

### BEFORE STARTING - CRITICAL SAFETY REQUIREMENTS

**STOP - Verify your authorisation:**
- Have you completed 3SAE CMS manufacturer training? **YES/NO**
- Have you passed the competency assessment? **YES/NO**
- Are you listed on the authorised users list? **YES/NO**
- If you answered NO to any of these: **DO NOT OPERATE - Contact supervisor**

**Supervision requirements for new users:**
- First 10 operations: Direct supervision by experienced user required
- Next 20 operations: Experienced user must be present in laboratory
- After 30 successful operations: May operate independently if competency maintained

### 1. PRE-OPERATION SAFETY CHECKS (MANDATORY - DO NOT SKIP)

**Complete these checks EVERY TIME before operation. If ANY check fails, DO NOT USE - lock out and report to supervisor immediately.**

1. **Sign in** to equipment logbook:
   - Record: Your name, date, time, type of operation planned
   - Review previous entries for any reported issues
   - Check that no maintenance or repair is scheduled

2. **Visual inspection of equipment exterior:**
   - Check for any visible damage to equipment housing or enclosures
   - Verify no cables or hoses are damaged, frayed, or kinked
   - Check that all cable connections are secure
   - Ensure no liquid spills or contamination on or near equipment
   - Verify work area is clean and free of clutter
   - **If ANY damage found:** DO NOT USE - lock out and report to supervisor

3. **Check exclusion zone and clearances:**
   - Verify 500mm exclusion zone around equipment is clear
   - Remove any flammable materials from 1-metre radius
   - Ensure no obstructions to emergency stop button or exit routes
   - Confirm adequate lighting for operation
   - Check that fire extinguisher is accessible

4. **Compressed air system checks:**
   - Verify compressed air supply is connected and secure
   - Check pressure gauge reads approximately 6.2 bar (90 psi)
   - Listen for any unusual hissing or air leaks
   - Inspect visible air lines for damage or kinks
   - Test emergency air shut-off valve (close and reopen to verify function)
   - **If pressure is incorrect or leaks detected:** DO NOT USE - contact facilities/supervisor

5. **Electrical system checks:**
   - Verify mains power is connected and RCD is functional (test RCD button)
   - Check that no electrical cables show damage or exposed conductors
   - Verify all equipment indicators show normal status
   - Ensure emergency power isolation switch is accessible and functional
   - **If any electrical issues detected:** DO NOT USE - contact supervisor/electrician

6. **Emergency stop button test:**
   - **CRITICAL:** Press emergency stop button to verify it functions
   - System should immediately cease all operations
   - Reset emergency stop and verify system can restart normally
   - **If emergency stop does not function correctly:** DO NOT USE - lock out and report immediately

7. **Safety interlock verification:**
   - Verify that opening chamber door during operation triggers automatic shutdown (test with system in safe idle state)
   - Check that all safety interlocks appear intact and functional
   - **If any interlock appears bypassed or faulty:** DO NOT USE - report immediately

8. **Software and control system check:**
   - Power on PC and CMS control system
   - Verify software loads without errors
   - Check that both camera views display correctly
   - Verify all system status indicators show "ready" or normal state
   - **If software errors or camera failures:** DO NOT USE - contact IT/supervisor

9. **Vision system verification:**
   - Check both orthogonal camera views are clear and focused
   - Verify telecentric lenses are clean (clean gently with lens tissue if needed)
   - Test that monitor displays both camera feeds clearly
   - Adjust monitor brightness/contrast if needed for viewing comfort
   - **If vision system not functioning:** DO NOT USE - operation requires visual monitoring

10. **Check sharps disposal and first aid readiness:**
    - Verify sharps disposal container is available and not full
    - Confirm first aid kit location and check it contains splinter removal tools
    - Note location of emergency eyewash station
    - **If safety equipment not available:** Obtain before proceeding

11. **Personal protective equipment (PPE) verification:**
    - Put on safety glasses (close-fitting type)
    - Confirm laboratory coat/protective clothing is worn
    - Verify closed-toe shoes are being worn
    - Have nitrile gloves and heat-resistant gloves readily available
    - **Never proceed without appropriate PPE**

12. **Final pre-operation check:**
    - All pre-operation checks completed satisfactorily? **YES/NO**
    - Any safety concerns or unusual observations? **Record in logbook**
    - **If any concerns:** Consult with supervisor before proceeding
    - **If all checks passed:** Proceed to operation

---

### 2. EQUIPMENT STARTUP AND INITIALISATION

13. **Power-up sequence:**
    - Ensure PC and CMS software are running
    - Verify compressed air supply is open and at correct pressure
    - Allow system to complete initialisation sequence (typically 2-3 minutes)
    - Watch for any error messages during startup
    - Verify all system diagnostics show normal operation

14. **Electrode inspection and installation (if required):**
    - **Put on nitrile gloves** before handling electrodes
    - Open electrode chamber following software prompts or manual procedures
    - Visually inspect electrodes for wear, damage, or excessive contamination
    - If electrodes appear worn (consult manufacturer guidelines for wear limits): Replace with spare set
    - Ensure electrodes are correctly positioned and secured
    - Close electrode chamber and verify secure closure
    - **Remove nitrile gloves** after electrode handling (do not contaminate other surfaces)

15. **Cooling system verification:**
    - Verify embedded electrode cooling system is functioning (check for coolant flow indicators if present)
    - Listen for coolant pump operation (should be quiet and steady)
    - Check for any coolant leaks around electrode assembly
    - **If cooling system not functioning:** DO NOT proceed - contact supervisor/manufacturer

16. **Calibration and alignment check (if required by procedure):**
    - Some processes may require alignment calibration
    - Follow software prompts for automatic alignment procedures
    - Verify pitch and yaw alignment systems are functioning correctly
    - If manual alignment needed: Use provided alignment fixtures and follow manufacturer procedures

---

### 3. FIBRE PREPARATION AND LOADING

17. **Select appropriate fibre holders:**
    - Choose fibre holders matching the diameter of fibres to be processed:
      - 250μm holders for standard single-mode fibres
      - 400μm, 700μm, 1000μm, 1500μm, 2000μm, 2500μm for larger diameter fibres
    - Install fibre holders in both left and right positioning stages
    - Ensure holders are clean and properly seated

18. **Prepare optical fibres:**
    - **Ensure safety glasses are on** before handling fibres
    - Strip fibre coating if required using appropriate stripping tool (not while in CMS)
    - Clean fibre ends with isopropanol and lint-free wipes
    - If cleaving externally before loading: Use proper cleaving technique to achieve clean end face
    - Handle fibres only by coated sections when possible
    - **Use tweezers or fibre handling tools** - avoid direct hand contact with glass sections

19. **Load fibres into holders:**
    - Carefully position fibre in left holder first
    - Secure fibre gently (avoid over-tightening which can damage fibre)
    - Load second fibre into right holder (for splicing operations)
    - For tapering operations: Load single fibre as per procedure
    - Verify fibres are properly seated and secured
    - Check alignment visually through camera system

20. **Position fibres using software control:**
    - Use X-Y-Z positioning controls to align fibres
    - Bring fibre ends into view of both camera systems
    - For fusion splicing: Align fibre cores using automatic or manual alignment
    - Achieve alignment resolution of <50nm in X and Y axes
    - Verify alignment on both orthogonal camera views before proceeding
    - **Never attempt to adjust fibre position manually while system is powered**

---

### 4. OPERATION - FUSION SPLICING

**This section covers standard fusion splicing operations. For tapering or cleaving, see sections 5 and 6.**

21. **Configure splice parameters:**
    - Select appropriate splice program from software library OR
    - Create custom splice program specifying:
      - Arc power settings (based on fibre type and diameter)
      - Arc duration
      - Pre-splice cleaning arc (if required)
      - Overlap distance
      - Push distance during splice
    - Save custom programs for repeatability
    - **Test new programs on scrap fibres before using on valuable components**

22. **Pre-splice arc cleaning (if required):**
    - Some fibre types benefit from pre-splice cleaning arc
    - Software will prompt for this step if programmed
    - Verify fibres remain aligned during cleaning arc
    - Visual inspection via camera for any debris or contamination

23. **Final pre-splice verification:**
    - **STOP - Safety verification before plasma activation:**
      - Hands clear of equipment? **YES**
      - Exclusion zone clear? **YES**
      - Fibre alignment correct? **YES**
      - Splice parameters confirmed? **YES**
      - Emergency stop accessible? **YES**
    - **If any NO answers:** Correct before proceeding

24. **Initiate fusion splice:**
    - Click "Start Splice" or equivalent command in software
    - **PLASMA WILL NOW ACTIVATE - Stand clear**
    - Monitor splice progress on both camera views
    - Watch for:
      - Smooth approach of fibre ends
      - Uniform heating and melting of glass
      - Proper fusion at interface
      - Absence of bubbles or voids
    - **Do NOT reach towards equipment during plasma operation**

25. **Post-splice monitoring:**
    - Software will automatically control:
      - Plasma power and timing
      - Fibre positioning and overlap
      - Push force during fusion
      - Cool-down period
    - Process typically completes in 10-60 seconds depending on fibre size
    - **Wait for "Splice Complete" confirmation** before proceeding

26. **Splice quality assessment:**
    - System automatically captures before/during/after images
    - Visually inspect splice on monitor for:
      - Smooth, symmetrical splice junction
      - Proper alignment (minimal core offset)
      - Absence of bubbles, voids, or cracks
      - Appropriate splice geometry
    - Use scanning function to measure splice diameter profile if needed
    - Record splice quality in logbook (accept/reject decision)

27. **Cool-down period (MANDATORY):**
    - **DO NOT touch fibres or components for minimum 15 minutes after splice**
    - Software may display temperature information
    - **Use thermal inspection camera** to verify components have cooled if immediate handling required
    - **Heat-resistant gloves** do not provide complete protection immediately after >3000°C plasma
    - Plan work to allow proper cooling time between splices

28. **Remove spliced component:**
    - After confirmed cool-down:
      - Carefully release fibre from holders
      - Use fibre handling tools (tweezers) to grip coated sections only
      - Transfer to appropriate storage or testing fixture
    - Dispose of any cleaved scrap fibres in sharps container immediately

29. **If splice is rejected:**
    - Cleave out the failed splice section
    - Prepare new fibre ends
    - Repeat alignment and splicing process
    - Document failure mode in logbook for quality tracking

---

### 5. OPERATION - FIBRE TAPERING

**Tapering operations use plasma to elongate fibre while reducing diameter. Available modes: bidirectional, single-direction, or custom table-based tapering.**

30. **Select tapering mode and parameters:**
    - **Bidirectional tapering:** For symmetric tapers up to 150mm length
    - **Single-direction tapering:** For asymmetric tapers up to 90mm length
    - **Table-based tapering:** For custom taper profiles using syntax-based programming
    - Define critical parameters:
      - Taper ratio (input diameter / output diameter)
      - Taper length
      - Pulling speed profile
      - Arc power profile
      - Hot zone width (can be expanded in partial vacuum mode)

31. **Load fibre for tapering:**
    - Secure fibre in both left and right holders with adequate length for taper
    - Ensure sufficient fibre extends beyond holders to achieve desired taper length
    - Position initial heat zone at correct starting location
    - Verify load cell feedback system is functional (shows fibre tension)

32. **Partial vacuum mode (if required):**
    - For adiabatic tapers or wide heat zone processing:
      - Verify vacuum chamber seals and O-rings are in good condition
      - Close chamber and verify seal integrity
      - Initiate vacuum pump following software procedure
      - Monitor pressure gauge during evacuation
      - Target pressure: [specify based on process requirements]
    - **Never open chamber while under vacuum**
    - Vacuum mode expands plasma heat zone up to 10x along fibre axis
    - **If unusual sounds or pressure readings:** Immediately abort and vent to atmosphere

33. **Configure taper program:**
    - Use simplified LabVIEW GUI for standard tapers OR
    - Create custom program using table-based tapering interface OR
    - Import program from MATLAB/Excel if custom algorithm developed
    - Software allows 20 adjustments per second for:
      - Fibre platform positions (left and right)
      - Heat zone location
      - Arc power settings
    - **Validate program with simulation or test run before using on valuable fibre**

34. **Initiate tapering process:**
    - **STOP - Final safety check:**
      - Fibre secured properly? **YES**
      - Taper parameters confirmed? **YES**
      - If using vacuum: Chamber sealed and pressure correct? **YES**
      - Exclusion zone clear? **YES**
    - Click "Start Taper" command
    - **PLASMA WILL ACTIVATE - Stand clear of equipment**

35. **Monitor tapering process:**
    - Watch "Hot Imaging" live view of molten glass during tapering
    - Monitor load cell feedback showing fibre tension
    - Verify smooth, controlled pulling motion
    - Watch for taper formation via camera views
    - Typical taper time: Several minutes depending on length and profile
    - **Do NOT interfere with process once started**
    - **If any abnormal behaviour observed:** Use emergency stop immediately

36. **Post-taper procedures:**
    - Process completes automatically when programmed taper profile achieved
    - Software captures images and process data
    - **Cooling period MANDATORY:** Minimum 15 minutes before handling
    - If in vacuum mode:
      - Software will prompt for controlled venting
      - Allow chamber to return to atmospheric pressure
      - Verify pressure equalised before opening chamber
    - **Use thermal camera** to verify taper has cooled sufficiently

37. **Taper quality verification:**
    - Use scanning function to measure taper diameter profile
    - Compare measured profile to target specification
    - Visual inspection for:
      - Smooth taper transition
      - Absence of modulations or stress concentrations
      - Symmetry (for bidirectional tapers)
      - Proper taper length
    - Record taper quality data in logbook
    - **If taper meets specifications:** Proceed to removal
    - **If taper is defective:** Document failure mode and repeat process

38. **Remove tapered fibre:**
    - After confirmed cool-down and quality verification
    - Carefully release fibre from holders using fibre handling tools
    - Support taper along entire length to prevent breakage
    - Transfer to appropriate storage or next processing step
    - Clean work area and dispose of scrap in sharps container

---

### 6. OPERATION - PRECISION CLEAVING

**The CMS includes in situ ultrasonic diamond-tipped cleaving capability for production of end caps, tapers, and accurate length components.**

39. **Prepare fibre for cleaving:**
    - Load fibre to be cleaved in appropriate holder
    - Position fibre so desired cleave location is in field of view
    - Use real-time scanning to identify exact cleave position
    - Achieve cleave location precision of ±12.5μm using reference marks

40. **Configure cleaving parameters:**
    - Diamond-tipped blade with piezo-based frequency and amplitude control
    - Set ultrasonic frequency and amplitude based on fibre diameter:
      - Larger fibres (up to 500μm): May require higher amplitude
      - Smaller fibres: Lower amplitude prevents shattering
    - Position semi-automated backstop for blade travel limit
    - **Verify blade is sharp and undamaged** (inspect through camera if possible)

41. **Execute cleave:**
    - **STOP - Safety check before cleaving:**
      - Safety glasses on? **YES**
      - Hands clear of cleaving zone? **YES**
      - Fibre properly positioned? **YES**
    - Initiate cleave command in software
    - Ultrasonic blade will advance to fibre, vibrate, and create cleave
    - Process typically completes in <1 second
    - **Do NOT manually interfere with cleave process**

42. **Cleave quality assessment:**
    - High-resolution camera inspection of cleaved end face
    - Good cleave characteristics:
      - Flat, perpendicular end face
      - Minimal chipping or fracture
      - Clean separation
    - **If cleave is poor quality:**
      - Adjust cleave parameters (frequency, amplitude, blade position)
      - May need to cleave back further and repeat
    - Software captures images for documentation

43. **Post-cleave handling:**
    - Cleaved fibre end is VERY SHARP
    - Use extreme care when removing cleaved component
    - Use tweezers or fibre handling tools only
    - Place cleaved scrap immediately in sharps container
    - **Never allow cleaved fibres to fall on floor or work surface**

44. **Cleaving blade maintenance:**
    - Diamond blade requires periodic replacement based on usage
    - Signs blade needs replacement:
      - Poor cleave quality despite parameter adjustments
      - Visible damage to blade tip
      - Inconsistent cleave results
    - **Blade replacement procedure:**
      - **LOCK OUT EQUIPMENT** before accessing blade
      - Use nitrile gloves when handling blade
      - Follow manufacturer procedure for safe blade removal and installation
      - Dispose of used blade in sharps container (extremely sharp)
      - Test new blade on scrap fibre before critical cleaves

---

### 7. EQUIPMENT SHUTDOWN AND POST-OPERATION PROCEDURES

45. **Prepare for shutdown:**
    - Complete any in-progress operations
    - Remove all fibres from holders
    - Collect all cleaved scrap and dispose in sharps container
    - Remove any fibre holders or fixtures that are not permanent

46. **Software shutdown sequence:**
    - Save any custom programs or process data
    - Backup critical data if required
    - Close processing software following proper exit procedure
    - **Do NOT force-quit software** - may cause data loss or system errors

47. **Plasma system shutdown:**
    - System will automatically cool down electrodes using embedded cooling
    - Allow cooling cycle to complete (typically 5-10 minutes)
    - **Do NOT power off during cooling cycle**
    - System will indicate when safe to power down

48. **Vacuum system shutdown (if used):**
    - Ensure chamber is fully vented to atmosphere
    - Verify pressure gauge shows atmospheric pressure
    - Safe to power off vacuum pump
    - Leave chamber slightly open to prevent seal damage during storage

49. **Compressed air shutdown:**
    - Close compressed air supply valve (optional - can be left on if equipment used regularly)
    - If closing air supply:
      - Allow system to depressurise naturally
      - Verify pressure gauge drops to zero
      - **Do NOT disconnect pressurised lines**

50. **Power down sequence:**
    - Shut down PC in normal manner
    - Switch off CMS main power
    - Verify all indicator lights are off
    - **Do NOT disconnect power cables while system is energised**

51. **Post-operation inspection:**
    - Visual check for any damage or issues that developed during session
    - Note any unusual behaviour in equipment logbook
    - Check work area for any dropped fibres or glass debris
    - Verify all sharps have been disposed of properly

52. **Work area cleanup:**
    - Clean all work surfaces using damp cloth (captures glass fragments)
    - **Do NOT use compressed air to clean** - will disperse glass particles
    - Dispose of cleaning materials in general waste (not sharps unless glass embedded)
    - Return all tools and accessories to designated storage
    - Ensure fire extinguisher and emergency equipment are accessible
    - Leave work area clean and ready for next user

53. **Sign out from equipment logbook:**
    - Record: End time, operations completed, component count, any issues
    - Note any maintenance needs or concerns
    - If any problems occurred:
      - **Complete incident report if safety-related**
      - **Tag equipment if not safe to use**
      - **Inform supervisor immediately of serious issues**

54. **PPE removal and hand washing:**
    - Remove and dispose of nitrile gloves if worn
    - Remove safety glasses and store properly
    - Remove laboratory coat
    - **Wash hands thoroughly** after handling fibres, electrodes, or chemicals
    - Inspect hands for any glass fragments (use magnification if needed)

---

## Emergency Shutdown Procedures

### EMERGENCY STOP - Use in ANY of these situations:

- Plasma operation appears abnormal (unusual colour, shape, sound, or behaviour)
- Smoke, fire, or burning smell detected
- Electrical sparking, arcing, or unusual sounds
- Compressed air leak or sudden pressure loss
- Vacuum chamber failure or unusual sounds from vacuum system
- Fibre breakage during processing causing unsafe condition
- Software crash or unresponsive controls
- Personal injury occurring
- Equipment damage visible or suspected
- Any situation where continued operation is unsafe

### EMERGENCY SHUTDOWN PROCEDURE:

1. **IMMEDIATELY PRESS EMERGENCY STOP BUTTON**
   - Large red button on equipment front panel
   - Pressing will immediately shut down:
     - Plasma generation
     - All motion systems
     - Processing functions
   - Emergency stop does NOT remove electrical power (use main isolator for electrical emergencies)

2. **If emergency stop button fails or is inaccessible:**
   - Turn off main power at mains isolator switch
   - Close compressed air supply at emergency shut-off valve
   - Evacuate area if situation is worsening

3. **Assess the situation:**
   - **Fire:** Follow fire emergency procedures (see below)
   - **Electrical issue:** Do not approach equipment - call electrician
   - **Compressed air failure:** Evacuate and call facilities/supervisor
   - **Personal injury:** Provide first aid and call emergency services if serious
   - **Equipment malfunction:** Assess damage and determine if area is safe

4. **DO NOT attempt to restart equipment until:**
   - Emergency condition has been completely resolved
   - Equipment has been thoroughly inspected by competent person or supervisor
   - Root cause of emergency has been identified and corrected
   - Supervisor has authorised restart in writing
   - Any necessary repairs have been completed and tested
   - All safety systems verified functional

5. **Complete incident documentation:**
   - Fill out incident report form immediately while details are fresh
   - Include: Date, time, personnel present, exact circumstances, actions taken
   - Attach photos if equipment damage occurred
   - Submit to supervisor and safety officer
   - Complete RiskWare report if required by university policy
   - Equipment may need to be locked out pending investigation

6. **Lock out and tag equipment:**
   - If equipment is not safe to use, attach lockout tag
   - Tag must state: Date, reason for lockout, who locked out, contact details
   - Only supervisor or authorised maintenance can remove lockout

### RESETTING EMERGENCY STOP (only after emergency fully resolved and authorisation obtained):

1. Verify that emergency condition has been completely addressed
2. Obtain supervisor approval to reset (document in logbook)
3. Rotate emergency stop button clockwise to release (or follow equipment-specific reset procedure)
4. System will require re-initialisation
5. **Perform complete pre-operation safety checks** before resuming any work
6. Test emergency stop button again to verify it functions correctly
7. Proceed with caution and monitor equipment closely for any recurring issues

---

## Emergency Procedures for Fires, Spills or Exposure to Hazardous Substances

### FIRE EMERGENCY:

1. **ACTIVATE EMERGENCY STOP** to shut down all CMS systems

2. **CLOSE COMPRESSED AIR SUPPLY** immediately at emergency shut-off valve

3. **If fire is SMALL (smaller than a wastebasket) and CONTAINED:**
   - Use appropriate fire extinguisher:
     - **CO₂ or Dry Powder** for electrical fires
     - **DO NOT use water** on electrical equipment
   - Aim at base of fire, sweep side to side
   - Ensure you have clear escape route behind you
   - **If fire does not extinguish immediately or grows:** Evacuate

4. **If fire is LARGE, SPREADING, or involves compressed gas:**
   - **Evacuate area immediately**
   - Close door behind you (do not lock)
   - **Activate building fire alarm** (break glass at alarm point)
   - **Call 000** (Emergency Services) from safe location
   - Provide: Location, type of fire, any hazardous materials involved
   - Evacuate to designated assembly point
   - Do not re-enter for any reason

5. **If clothing is on fire:**
   - STOP, DROP, and ROLL to smother flames
   - Use fire blanket or safety shower if available
   - Once flames out, cool burned area with water
   - Seek immediate medical attention

6. **After fire is extinguished:**
   - Do not re-enter area until declared safe by emergency services or supervisor
   - Equipment must be thoroughly inspected before any restart attempt
   - Complete incident report with detailed description of fire cause and damage
   - Review fire safety procedures and identify any improvements needed

### THERMAL BURN INJURY:

1. **Immediately move away from heat source**

2. **Cool affected area under running cold water for at least 20 minutes**
   - Use cool tap water, not ice
   - Start cooling as quickly as possible
   - Continue cooling even if pain subsides
   - Remove jewellery or constricting items before swelling occurs

3. **Do NOT:**
   - Apply ice directly to burn
   - Apply butter, oil, ointments, or "home remedies"
   - Break any blisters that form
   - Touch burn with dirty hands or materials

4. **After cooling, cover burn with:**
   - Sterile non-stick dressing from first aid kit
   - Clean plastic wrap as alternative
   - **Do NOT use fluffy materials** (cotton wool) that may stick

5. **Seek immediate medical attention for:**
   - Burns larger than a 20-cent coin (5cm diameter)
   - Burns to face, hands, feet, genitals, or major joints
   - Burns that appear deep (white, waxy, charred, or painless)
   - Burns causing severe pain or extensive blistering
   - Burns from electrical source
   - Burns from chemical contact
   - Any uncertainty about burn severity
   - **Call 000 for severe burns**

6. **For minor burns (small, superficial, not on sensitive areas):**
   - Continue cooling for 20 minutes
   - Apply sterile dressing
   - May use over-the-counter pain relief if needed
   - Monitor for signs of infection (increased pain, redness, swelling, pus)
   - Seek medical review if any concerns

7. **Complete incident documentation:**
   - Record details in equipment logbook
   - Fill out incident report form
   - Notify supervisor immediately
   - Complete RiskWare report
   - Investigate how burn occurred to prevent recurrence

### ELECTRIC SHOCK:

1. **DO NOT touch the person if they are still in contact with electrical source**
   - You may also be shocked

2. **Break the circuit:**
   - Switch off power at mains isolator, or
   - Use non-conductive material (dry wood, plastic) to move person away from source
   - **Only if safe to do so**

3. **Call 000 immediately if person is:**
   - Unconscious or not breathing
   - Showing signs of serious shock (pale, clammy, rapid pulse)
   - Burned from electrical contact

4. **If person is unconscious:**
   - Check for breathing
   - If trained in CPR and person not breathing: Commence CPR
   - Continue CPR until emergency services arrive or person recovers

5. **If person is conscious but shocked:**
   - Have them lie down and remain still
   - Keep warm with blanket if available
   - Treat any burns (see thermal burn procedure above)
   - **Seek medical attention even if person feels "fine"** - electrical shock can cause internal injuries

6. **LOCK OUT AND TAG EQUIPMENT:**
   - Equipment that delivered shock must be locked out immediately
   - Attach tag stating: "Electrical hazard - Do not use"
   - Only qualified electrician can inspect and clear equipment for use

7. **Complete incident documentation:**
   - Document exact circumstances of shock
   - Identify electrical fault that caused shock
   - Ensure equipment is repaired before any future use
   - Review electrical safety procedures

### GLASS INJURY (Cuts or Embedded Fragments):

1. **For minor cuts:**
   - Rinse wound gently with clean water
   - Apply pressure with clean cloth if bleeding
   - Once bleeding stopped: Apply sterile adhesive dressing
   - Monitor for signs of infection

2. **For EMBEDDED glass fragments:**
   - **DO NOT attempt to remove large or deep embedded glass**
   - Cover area with sterile dressing
   - Seek medical attention for professional removal
   - **DO NOT apply pressure over embedded glass**

3. **For deep cuts or severe bleeding:**
   - Apply direct pressure with clean cloth
   - Elevate injured area above heart level if possible
   - **Do NOT remove cloth if blood soaks through** - add more layers on top
   - **Call 000 if bleeding is severe or does not stop within 5-10 minutes**
   - Keep person calm and lying down
   - Monitor for signs of shock (pale, clammy, weak pulse)

4. **For EYE injuries involving glass:**
   - **DO NOT rub eye**
   - **DO NOT attempt to remove any object from eye**
   - **DO NOT apply pressure to eye**
   - Cover eye gently with sterile dressing (no pressure)
   - **Seek IMMEDIATE medical attention at emergency department**
   - **Call 000 if object embedded in eye or severe pain**
   - Cover both eyes to prevent movement (injured eye will track with healthy eye)

5. **After treatment:**
   - All glass injuries, even minor, must be reported to supervisor
   - Complete incident report
   - Investigate how glass injury occurred
   - Review handling procedures to prevent recurrence
   - Ensure sharps disposal procedures are being followed

6. **First aid supplies for glass injuries:**
   - Sterile dressings in various sizes
   - Adhesive bandages
   - Splinter removal tweezers (for tiny superficial fragments only)
   - Eye wash and eye pads
   - Clean water for rinsing wounds

### COMPRESSED AIR SYSTEM FAILURE / AIR BLAST:

1. **ACTIVATE EMERGENCY STOP**

2. **CLOSE COMPRESSED AIR SUPPLY** at emergency shut-off valve

3. **EVACUATE AREA** if loud hissing, visible high-pressure air leaks, or flying debris

4. **DO NOT approach failed air lines or fittings** - high-pressure air can cause serious injury

5. **If injury from air blast:**
   - Move to safe area away from air stream
   - **Seek IMMEDIATE medical attention for suspected air embolism:**
     - Signs: Chest pain, difficulty breathing, confusion, loss of consciousness
     - **Call 000** - air embolism is life-threatening
   - **Do NOT allow casualty to move excessively** - may worsen embolism
   - Treat any projectile injuries (embedded objects, cuts, bruises)

6. **Never use compressed air to:**
   - Clean clothing or body
   - Direct at another person
   - Blow dust or debris (creates airborne hazards)

7. **After system failure:**
   - LOCK OUT AND TAG equipment
   - Contact facilities/maintenance for pressure system inspection
   - Only qualified technician can repair and re-certify compressed air system
   - Complete incident report documenting failure mode

### VACUUM SYSTEM FAILURE:

1. **ACTIVATE EMERGENCY STOP**

2. **If catastrophic failure (implosion, explosion, or violent air inrush):**
   - **Evacuate area immediately**
   - **Call 000 if injuries present**
   - Do not re-enter until area declared safe by supervisor or emergency services

3. **If controlled venting or slow leak:**
   - Allow system to vent to atmosphere naturally
   - Monitor pressure gauge
   - Once at atmospheric pressure: Open chamber slowly
   - Inspect for damage before any further use

4. **Injuries from vacuum failure:**
   - Flying glass or debris: Treat as cuts/embedded fragments (see above)
   - Noise trauma: Seek medical review if hearing affected
   - Crush injuries: Seek immediate medical attention

5. **After vacuum system failure:**
   - LOCK OUT AND TAG equipment
   - Only qualified technician can inspect vacuum chamber and seals
   - Pressure testing may be required before return to service
   - Document failure mode in incident report

### CHEMICAL EXPOSURE (Electrode Materials or Cleaning Chemicals):

1. **Skin contact:**
   - Immediately remove contaminated clothing
   - Rinse affected area with copious running water for at least 15 minutes
   - **Do NOT use neutralising agents** unless specifically directed by SDS
   - If irritation persists: Seek medical attention
   - Bring SDS with you to medical facility

2. **Eye contact:**
   - **Immediately flush eye with water or eyewash for at least 15 minutes**
   - Hold eyelids open to ensure thorough rinsing
   - Remove contact lenses if present and easy to remove
   - **Seek immediate medical attention** after flushing
   - Bring SDS to medical facility

3. **Inhalation:**
   - Move to fresh air immediately
   - Loosen tight clothing
   - If breathing difficulty: Seek immediate medical attention
   - **Call 000 if severe respiratory distress**
   - Bring SDS to medical facility

4. **Ingestion (unlikely but possible):**
   - **Do NOT induce vomiting** unless directed by Poisons Information
   - Rinse mouth with water
   - **Call Poisons Information Centre: 13 11 26**
   - Follow their advice
   - Seek medical attention
   - Bring chemical container or SDS

5. **After chemical exposure:**
   - Complete incident report
   - Review SDS and handling procedures
   - Identify how exposure occurred and implement prevention

### SOFTWARE / CONTROL SYSTEM FAILURE:

1. **Attempt emergency stop via software interface** (if responsive)

2. **If software unresponsive:**
   - **Press physical emergency stop button**
   - **If both fail:** Turn off power at mains isolator

3. **Record any error messages or system state:**
   - Take photo of screen if possible and safe
   - Note exact sequence of events leading to failure
   - **Do NOT attempt to troubleshoot during active emergency**

4. **After system is stopped:**
   - **DO NOT attempt to restart**
   - LOCK OUT AND TAG equipment
   - Contact IT support or manufacturer technical support
   - Only qualified technician can diagnose and repair software/control issues

5. **Data preservation:**
   - If safe to do so, attempt to save any critical process data before complete shutdown
   - System logs may help diagnose software failure

6. **Complete incident report** documenting software failure and any equipment impact

### EMERGENCY CONTACTS:

- **Emergency Services:** 000
  - Police, Fire, Ambulance
  - Call for: Fires, serious injuries, life-threatening situations

- **Poisons Information Centre:** 13 11 26
  - 24/7 advice for chemical exposures and ingestions

- **University Security (after hours):** [Insert number]
  - For emergencies outside business hours
  - Can contact emergency services and key personnel

- **Supervisor:** [Name and number]
  - First point of contact for equipment issues
  - Can authorise equipment restart after emergencies

- **Safety Officer:** [Name and number]
  - For incident reporting and safety advice
  - For hazard assessments and risk management

- **First Aid Officers:** [Names and contact details / Notice board location]
  - Trained in emergency first aid
  - Can provide immediate assistance for injuries

- **Facilities Management:** [Insert number]
  - For electrical, plumbing, HVAC emergencies
  - For compressed air system issues

- **IT Support:** [Insert number]
  - For software and computer system issues
  - Can assist with data recovery

- **3SAE Technical Support:** +1 615-778-8812
  - Manufacturer support for equipment issues
  - Email: info@3sae.com
  - Available during US business hours (may have time zone delay)

---

## Clean Up and Waste Disposal Requirements

### AFTER EACH USE - CLEANING PROCEDURES:

#### Processing Chamber and Fibre Holders:

- Remove all fibre remnants from holders using tweezers
- Inspect holders for glass debris or contamination
- Wipe holders with lint-free cloth if needed
- **Do NOT use solvents on fibre holders** unless specified by manufacturer
- Return holders to designated storage

#### Electrode Cleaning (Periodic - follow manufacturer schedule):

- **Performed when:** Electrodes show visible contamination, or per manufacturer interval (typically after X hours of use)
- **Safety requirements:**
  - Equipment must be powered off and cool
  - Wear nitrile gloves
  - Perform in well-ventilated area
- **Procedure:**
  - Remove electrode assembly following manufacturer instructions
  - Use provided electrode cleaning discs
  - Clean electrode surfaces gently to remove oxidation or deposits
  - Inspect for wear (replace if worn beyond manufacturer limits)
  - Reinstall electrodes ensuring proper positioning
- **Disposal:** Used cleaning discs in general waste; worn electrodes in sharps container or per manufacturer instructions

#### Camera Lenses and Optics:

- Inspect telecentric lenses for dust or contamination
- Clean ONLY with proper lens tissue and lens cleaner
- **Never use:** Paper towel, cloth, or harsh chemicals (will scratch lenses)
- Clean gently in circular motion from centre outward
- If optics are heavily contaminated: Contact supervisor (may need professional cleaning)

#### Work Area and Benchtop:

- Remove all materials, tools, and personal items
- Wipe down work surface with damp cloth to capture glass fragments
- **Do NOT use compressed air to clean benchtop** - disperses glass particles into air and onto equipment
- Check for dropped fibres on floor or adjacent surfaces
- Leave work area clean and organised for next user

### WASTE DISPOSAL:

#### Glass Waste (Fibre Scraps, Cleaved Ends, Broken Components):

- **All glass waste goes in sharps container** - NEVER in general waste
- This includes:
  - Cleaved fibre ends
  - Failed splices or tapers
  - Broken fibres
  - Any glass fragments
- Sharps container should be:
  - Puncture-proof rigid container
  - Clearly labelled "Glass Sharps"
  - Positioned within easy reach of work area
  - Never filled beyond 3/4 full
- When full: Contact waste management for sharps container replacement

#### Electrode Waste:

- Worn electrodes: Sharps container or follow manufacturer disposal instructions
- May contain metal materials requiring specific disposal
- Contact waste management if uncertain

#### Chemical Waste (Cleaning Agents, Isopropanol, etc.):

- Small quantities of isopropanol used for fibre cleaning: Can evaporate or dispose via solvent waste
- Larger quantities or other chemicals: Use university chemical waste system
- Never pour chemicals down sink unless specifically approved
- Label all waste containers clearly
- Consult SDS for disposal requirements

#### General Waste:

- Non-contaminated packaging materials
- Paper towels (that haven't contacted glass)
- Disposable gloves (if not contaminated with chemicals)
- General laboratory waste

#### Recycling:

- Fibre spools and packaging may be recyclable
- Check with waste management for specific requirements
- Remove all labels and contamination before recycling

### PERIODIC MAINTENANCE CLEANING:

#### Weekly:

- Thorough wipe-down of equipment exterior
- Vacuum or damp-wipe floor area around equipment
- Check that all waste containers have adequate capacity
- Inspect work area organisation and storage

#### Monthly:

- Detailed cleaning of all accessible surfaces
- Inspection of air filters (if present) and cleaning if needed
- Check cable routing and organisation
- Review housekeeping procedures with all users

#### Annually (or per manufacturer schedule):

- Professional equipment cleaning and maintenance
- Inspection and cleaning of internal components by qualified technician
- Replacement of any worn or deteriorated parts
- Calibration and alignment verification

### MAINTENANCE LOG:

- Document all cleaning and maintenance activities in equipment logbook
- Record: Date, type of cleaning/maintenance, person performing, any issues noted
- Track electrode replacement and usage hours
- Schedule and track periodic maintenance tasks

---

## References Used in the Development of This SWP

- AS/NZS 60825.1:2014 - Safety of laser products
- AS/NZS 3000:2018 - Electrical installations (Wiring Rules)
- AS 2243 Series - Safety in laboratories
- AS 4343:2014 - Pressure equipment - Hazard levels
- Work Health and Safety Act 2011
- Work Health and Safety Regulation 2017
- 3SAE CMS Product Information Sheet (https://3sae.com/wp-content/uploads/2024/01/CMS.pdf)
- 3SAE CMS Operator's Manual and User Documentation
- 3SAE Combiner Manufacturing System technical specifications
- Manufacturer training materials (3SAE Technologies Inc.)
- Risk Assessment SAIL-RA-CMS-001
- University WHS policies and procedures
- Material Safety Data Sheets for all chemicals used with equipment
- Code of Practice: Managing electrical risks in the workplace

---

## Competency Required

### MANDATORY TRAINING (Must be completed before authorisation):

**All training must be documented and records maintained by supervisor.**

#### 1. Manufacturer Training Course

- **3SAE CMS Multi-day On-site Installation and Operational Training (TRN-01-0012)**
- Key learning outcomes:
  - Equipment overview and capabilities
  - Safety systems and emergency procedures
  - Control software operation (LabVIEW GUI)
  - Fusion splicing techniques and parameters
  - Fibre tapering methods (bidirectional, single-direction, table-based)
  - Precision cleaving operation
  - Electrode maintenance and replacement
  - Troubleshooting and diagnostics
  - Best practices for different fibre types and diameters
- **This training is ESSENTIAL - no substitutes**
- Training typically 2-3 days depending on applications
- Certificate of completion must be obtained

#### 2. Laboratory Safety Induction

- General laboratory safety requirements
- Emergency procedures and assembly points
- Location and use of safety equipment (fire extinguishers, eyewash, first aid)
- Chemical safety and SDS interpretation
- Incident reporting procedures
- Personal protective equipment requirements

#### 3. Fibre Optic Handling and Safety

- Optical fibre types and characteristics
- Safe handling techniques for glass fibres
- Hazards of glass fragments and cleaved ends
- Proper use of fibre handling tools
- Sharps disposal procedures
- First aid for glass injuries
- Eye protection requirements

#### 4. Electrical Safety Awareness

- Basic electrical hazards
- Lockout/tagout procedures
- RCD function and testing
- Emergency power isolation
- When to contact qualified electrician
- **Do NOT attempt electrical repairs without qualifications**

#### 5. High-Temperature Process Safety

- Thermal hazards from plasma operation
- Safe distances and exclusion zones
- Cooling time requirements
- Recognition of hot surfaces
- Thermal burn first aid
- Heat-resistant glove use and limitations

#### 6. Compressed Air and Vacuum Systems Safety

- Hazards of high-pressure systems
- Safe connection and disconnection procedures
- Pressure monitoring and relief
- Vacuum chamber operation
- Emergency shutdown procedures
- Compressed air safety (never direct at body)

### COMPETENCY ASSESSMENT:

**Competency must be formally assessed and documented before independent operation.**

#### Theory Assessment:

Written test or oral examination covering:

1. **Safety-Critical Knowledge (Must achieve 100% on these questions):**
   - Emergency stop procedure and location
   - Emergency shutdown for different emergency types
   - Thermal burn first aid procedures
   - Glass injury prevention and first aid
   - Electrical safety and when to evacuate
   - Compressed air system hazards
   - When operation must stop (red flags)
   - PPE requirements for different tasks

2. **Equipment Knowledge (Minimum 80% pass mark):**
   - CMS capabilities and specifications
   - Fusion splicing principles and parameters
   - Tapering methods and applications
   - Cleaving operation and quality assessment
   - Software interface and control functions
   - Electrode function and maintenance
   - Cooling system purpose
   - Vision system operation

3. **Procedure Knowledge (Minimum 80% pass mark):**
   - Pre-operation safety checks
   - Fibre preparation and loading
   - Splice parameter selection
   - Taper program configuration
   - Cleave positioning and execution
   - Shutdown procedures
   - Cleaning and waste disposal
   - Documentation requirements

**Failed assessment:** Review training materials, additional instruction, retest

#### Practical Assessment:

Supervised practical demonstration of competency in:

1. **Pre-Operation Procedures:**
   - Complete all safety checks correctly
   - Identify and test emergency stop
   - Verify safety equipment presence
   - Set up work area appropriately
   - Don proper PPE

2. **Basic Operation:**
   - Power up system correctly
   - Inspect and install electrodes
   - Load fibres into holders safely
   - Achieve proper fibre alignment
   - Execute a simple fusion splice
   - Assess splice quality
   - Properly shutdown system

3. **Advanced Operation (as applicable to user's role):**
   - Configure and execute taper program
   - Perform precision cleave
   - Use scanning functions
   - Operate vacuum system (if required)
   - Create custom splice/taper parameters

4. **Emergency Response:**
   - Demonstrate emergency stop activation
   - Describe appropriate response to different emergency scenarios
   - Locate and identify use of emergency equipment
   - Demonstrate understanding of when to evacuate vs. respond

5. **Housekeeping:**
   - Proper cleanup procedures
   - Correct waste disposal
   - Appropriate documentation in logbook

**Assessment Requirements:**
- Assessor must observe ALL practical elements
- Any safety-critical errors result in immediate FAIL - retraining and reassessment required
- Minor non-safety errors: Corrective instruction provided, reassessment of that element only
- All elements must be demonstrated competently before authorisation granted

### ONGOING REQUIREMENTS:

#### Refresher Training:

- **Annual refresher** required for all authorised users
- Covers:
  - Safety procedure updates
  - Any equipment modifications or new capabilities
  - Review of common errors or incidents
  - New techniques or best practices
  - Changes to Australian Standards or regulations

#### Retraining Required When:

- Any safety incident involving this equipment (immediate retraining)
- Safety procedures are updated or changed
- Equipment is significantly modified or upgraded
- Unsafe practices are observed (remedial training)
- Extended period of non-use (>6 months requires supervised refresher)
- New applications or techniques are implemented
- User requests refresher training

#### Supervision Requirements:

Based on experience level:

- **Novice users (0-10 operations):**
  - Direct supervision required at all times
  - Supervisor must be experienced CMS user
  - Supervisor present in same room, actively observing
  - Each operation reviewed with supervisor before and after

- **Intermediate users (11-30 operations):**
  - Experienced user must be present in laboratory
  - Supervisor available for consultation
  - Can perform routine operations independently with oversight
  - New or complex operations require direct supervision

- **Experienced users (31+ operations, demonstrated consistent competency):**
  - May operate independently
  - Should consult with colleagues for unusual situations
  - Responsible for mentoring and supervising novice users
  - Maintain competency through regular use (minimum monthly)

#### Medical Monitoring:

- Not routinely required for CMS operation
- Eye examinations recommended for frequent users (discuss with OH&S)
- Any health concerns affecting ability to operate safely must be reported to supervisor
- Vision requirements: Must be able to view monitor clearly and distinguish alignment on camera views

### RECORD KEEPING:

Documentation required for competency management:

1. **Training Records:**
   - Manufacturer training certificate (keep copy)
   - Laboratory safety induction completion
   - All supplementary training courses
   - Refresher training attendance
   - Maintained by supervisor, copies in personnel files

2. **Competency Assessments:**
   - Theory assessment results (written test or oral exam notes)
   - Practical assessment checklist (signed by assessor)
   - Date competency achieved
   - Any remedial training and reassessment
   - Maintained by supervisor

3. **Authorised Users List:**
   - Current list of all authorised users
   - Date authorised, authorisation level
   - Displayed prominently near equipment
   - Updated when users added or removed
   - Reviewed annually, remove inactive users

4. **Individual Operation Logs:**
   - Each user's operation count tracked in logbook
   - Helps determine supervision requirements
   - Identifies when refresher training may be beneficial
   - Reviewed during annual competency review

5. **Incident and Near-Miss Records:**
   - Any safety incidents involving specific users
   - May trigger retraining requirements
   - Pattern analysis for systemic issues
   - Maintained by safety officer

### COMPETENCY RENEWAL:

- Annual competency review by supervisor
- Considers:
  - Frequency of equipment use
  - Any incidents or near-misses
  - Refresher training completion
  - Observed work practices
  - Changes in procedures or equipment
- Supervisor may require reassessment if concerns identified
- Users who have not operated equipment in >12 months: Full reassessment required

---

## Staff Approved to Assess Competence for This SWP

### Authorised Assessors:

The following staff members are authorised to assess competency for this procedure:

- [Name 1] ([Role - e.g., Senior Research Fellow]) - Contact: [email/phone]
- [Name 2] ([Role - e.g., Laboratory Manager]) - Contact: [email/phone]
- [Additional names as appropriate]

### Assessor Requirements:

To be authorised as an assessor, staff must:

- Have completed 3SAE manufacturer training course
- Have minimum 100 successful operations on CMS (extensive experience)
- Demonstrate expert-level knowledge of all CMS functions and safety systems
- Have no significant safety incidents on record
- Understand adult learning principles and assessment techniques
- Be approved by laboratory manager AND safety officer
- Maintain current competency through regular equipment use

### Assessment Process:

1. **Trainee completes all mandatory training modules**
   - Manufacturer training (TRN-01-0012)
   - Laboratory safety induction
   - Supplementary safety training (electrical, high-temp, compressed air, etc.)
   - Trainee reviews this SWP and associated Risk Assessment thoroughly

2. **Assessor conducts theory assessment**
   - Written test or structured oral examination
   - Safety-critical questions must achieve 100%
   - General knowledge questions minimum 80%
   - If failed: Review materials, additional instruction, retest

3. **Assessor supervises practical demonstration**
   - Trainee demonstrates all required practical skills
   - Assessor uses practical assessment checklist
   - Any safety-critical errors result in immediate fail
   - Corrective instruction provided for minor errors

4. **Assessor verifies competency in all required areas**
   - Reviews theory and practical assessment results
   - Confirms all elements demonstrated satisfactorily
   - Ensures trainee understands limitations and when to seek help
   - Verifies trainee can respond appropriately to emergencies

5. **If competent: Assessor signs trainee off on sign-off sheet**
   - Assessor signature authorises trainee for operation
   - Date of authorisation recorded
   - Supervision requirements specified (based on experience level)
   - Trainee added to authorised users list

6. **If not yet competent:**
   - Specific deficiencies identified and communicated
   - Additional training and supervised practice required
   - Reassessment scheduled once trainee ready
   - May be partial reassessment (only areas that were deficient)

7. **Once signed off: Trainee added to authorised users list**
   - Name added to list displayed near equipment
   - Date authorised and authorisation level recorded
   - Supervision requirements clearly noted
   - Laboratory manager notified

### Authorised Users List Maintenance:

- **Maintained by:** Laboratory Manager
- **Displayed:** Prominently near CMS equipment (visible to all users)
- **Updated when:**
  - New users authorised (add name, date, supervision level)
  - Users move to different supervision levels (update status)
  - Users become inactive (remove or mark inactive)
  - Users require retraining (temporarily suspend if safety issue)
- **Reviewed:** Annually as part of SWP review
- **Format:**

| Name | Date Authorised | Authorisation Level | Supervision Required | Authorised By | Notes |
|------|----------------|-------------------|---------------------|---------------|-------|
| [Name] | [DD/MM/YYYY] | [Novice/Intermediate/Experienced] | [Direct/Oversight/Independent] | [Assessor Name] | [Any special conditions] |

---

## SWP Sign Off Sheet

**SWP name and version:** Operation of 3SAE Combiner Manufacturing System (CMS)  
**Version:** 1.0 - January 2026  
**Reference:** SAIL-SWP-CMS-001

**In signing this section the assessor agrees that the following persons are competent in following this SWP.**

| Name | Signature | Date Competent | Authorisation Level | Name of Assessor | Assessor Signature |
|------|-----------|----------------|-------------------|------------------|-------------------|
|      |           |                |                   |                  |                   |
|      |           |                |                   |                  |                   |
|      |           |                |                   |                  |                   |
|      |           |                |                   |                  |                   |
|      |           |                |                   |                  |                   |
|      |           |                |                   |                  |                   |
|      |           |                |                   |                  |                   |
|      |           |                |                   |                  |                   |
|      |           |                |                   |                  |                   |
|      |           |                |                   |                  |                   |

**Authorisation Levels:**
- **Novice:** Requires direct supervision (0-10 operations completed)
- **Intermediate:** Requires experienced user in laboratory (11-30 operations completed)
- **Experienced:** Approved for independent operation (31+ operations, demonstrated consistent competency)

---

## Document Review Schedule

This SWP must be reviewed:

- **Annually** (by January 2027, then annually thereafter)
- After any incident involving this equipment or process
- When equipment is modified, upgraded, or repaired
- When new hazards are identified or new information becomes available
- When procedures change or new applications are implemented
- When Australian Standards are updated or new regulations introduced
- When manufacturer issues safety bulletins or updates
- If patterns of user errors or near-misses are identified

**Review Process:**
1. Collect feedback from all users
2. Review incident reports and near-miss records
3. Check for equipment modifications or updates
4. Verify all safety controls remain effective
5. Update procedures as needed
6. Re-train all users on significant changes
7. Document review completion in equipment logbook

**Version Control:**
- Version number incremented for all changes
- Change history documented
- All users notified of updates
- Superseded versions archived (not destroyed - maintain history)

---

*End of Safe Work Procedure*

**Document Control:**
- This is a DRAFT document requiring review and approval
- All bracketed items [To be completed] must be filled in before approval
- This document must be approved by the Safety Officer and supervisors before use
- This SWP is based on Risk Assessment SAIL-RA-CMS-001
- Once approved, all authorised users must be trained on this SWP
- Users must sign the competency sign-off sheet before independent operation
- This document must be readily available to all users (printed copy near equipment, electronic copy accessible)
