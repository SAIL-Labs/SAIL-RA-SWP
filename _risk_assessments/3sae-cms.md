---
layout: document
title: Risk Assessment - 3SAE Combiner Manufacturing System (CMS)
doc_type: Risk Assessment
status: Draft
permalink: /risk-assessments/3sae-cms/
equipment_name: "3SAE Combiner Manufacturing System (CMS)"
reference: "SAIL-RA-CMS-001"
version: "1.0"
description: "Risk assessment for the 3SAE CMS fibre optic processing system utilizing thermally stabilized plasma technology (>3000°C). Covers extreme thermal hazards, high-pressure gas systems, electrical hazards, optical radiation, and sharp materials."
key_hazards: "High-temperature plasma (>3000°C), compressed air (90 psi), electrical hazards, optical radiation, sharp glass fibres, vacuum system"
metadata:
  reference: SAIL-RA-CMS-001
  title: 3SAE Combiner Manufacturing System (CMS) - Fibre Optic Glass Processing
  version: "1.0"
  issue_date: January 2026
  prepared_by: Chris Betters
  supervisors: Chris Betters, Sergio Leon-Saval
  review_date: January 2027
critical_warning: |
  **CRITICAL SAFETY WARNING - HIGH TEMPERATURE PLASMA SYSTEM**

  The 3SAE CMS utilises thermally stabilised plasma technology that operates at temperatures exceeding 3000°C. This system presents extreme thermal hazards, high-pressure gas hazards, electrical hazards, and optical radiation risks.

  - **Key hazards:** High-temperature plasma (>3000°C), compressed air system (90 psi), electrical systems (24V 200W), ultrasonic cleaving blade, optical radiation, sharp glass fibres, vacuum system
  - **Safety requirements:** Mandatory training and competency assessment before operation, continuous supervision for inexperienced users, compliance with all safety interlocks, appropriate PPE for all tasks

  **NEVER disable safety interlocks or protective systems.**
  **NEVER operate without appropriate thermal and eye protection.**
  **NEVER leave the system unattended during operation.**
  **NEVER attempt to touch or inspect components during or immediately after plasma operation.**
related_docs:
  - title: Safe Work Procedure - 3SAE CMS
    url: /safe-work-procedures/3sae-cms/
    description: Detailed operating procedures for the CMS
  - title: Manufacturer Documentation
    url: https://3sae.com/wp-content/uploads/2024/01/CMS.pdf
    description: Official product information sheet
show_review: true
---

## Activity, Process, or Equipment Name

3SAE Combiner Manufacturing System (CMS) - Fibre Optic Glass Processing System

**Reference Number:** SAIL-RA-CMS-001

### Purpose/use:

- Fusion splicing of optical fibres (125μm to 2mm diameter)
- Fibre optic tapering for combiners and mode-field adapters
- Precision cleaving of optical fibres and components up to 500μm diameter
- Production of multi-kilowatt class optical components
- Manufacturing of photonic crystal fibre assemblies
- Research and development of custom fibre optic assemblies

**Location:** 218G SAIL Nexus Lab

### Persons at risk:

- Laboratory staff operating the CMS
- Research students and postgraduate researchers
- Technical support personnel
- Maintenance technicians
- Visitors to the laboratory (when equipment is operational)

### Risk assessment team (who was consulted?):

- Laboratory manager
- Safety officer
- Equipment users and operators
- Manufacturer documentation review
- Technical specifications analysis

---

## List of Legislation, Code of Practice, Australian Standards, Guidance Materials

- AS/NZS 60825.1:2014 - Safety of laser products
- AS/NZS 3000:2018 - Electrical installations (Wiring Rules)
- AS/NZS 4804:2001 - Occupational health and safety management systems
- AS 1940:2017 - The storage and handling of flammable and combustible liquids
- AS 2243 Series - Safety in laboratories
- Work Health and Safety Act 2011
- Work Health and Safety Regulation 2017
- AS 4343:2014 - Pressure equipment - Hazard levels
- AS 1210:2010 - Pressure vessels
- Manufacturer's documentation (3SAE Technologies Inc.)
- CMS Product Information Sheet and User Manual
- University WHS policies and procedures

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

### Task 1: High-Temperature Plasma Operation (Ring of Fire® Technology)

**Hazard/s:** Thermally Stabilised Plasma operating at temperatures from 300°C to >3000°C for fusion splicing, tapering, and glass processing operations.

**Associated harm:**
- Severe thermal burns from contact with plasma, heated components, or processed fibres
- Eye injury from intense visible and infrared radiation from plasma
- Fire ignition if flammable materials are present near plasma zone
- Heat stress from prolonged operation in proximity to heat source
- Thermal damage to skin from radiant heat exposure
- Secondary burns from heated electrode assemblies and processing chambers
- Ignition of combustible materials (paper, solvents, packaging materials)

**Existing Risk Controls:**
- Enclosed processing chamber with controlled access during operation
- Integrated cooling system for Ring of Fire® electrodes and electrical components
- Automatic shut-off systems and emergency stop functionality
- Two orthogonal camera systems allowing remote viewing of process
- Manufacturer-designed thermal barriers and shielding
- Clear operational protocols specifying minimum safe distances
- Warning labels on equipment indicating hot surfaces
- Plasma operates within enclosed chamber, not exposed to operator
- Load cell feedback system for process monitoring without physical contact

**Current risk rating:** Medium

**Additional controls required:**
- Mandatory completion of manufacturer-provided training before operation
- Supervised operation for all users until competency demonstrated
- Annual thermal safety audit of equipment and enclosure integrity
- Prohibition of leaving system unattended during plasma operation
- Automatic plasma shut-off if chamber is opened during operation (interlock verification)

**Residual risk rating:** Low

---

### Task 2: Compressed Air System Operation

**Hazard/s:** High-pressure compressed air system operating at 6.2 bar (90 psi) with flow rate of 126 L/min (~4.5 cfm).

**Associated harm:**
- Projectile hazards from disconnected or failed air lines
- Air embolism if compressed air contacts broken skin or body orifices
- Eye injury from airborne particles propelled by compressed air
- Hearing damage from sudden pressure releases or air leaks
- Equipment damage from over-pressurisation
- Rapid decompression injuries if partial vacuum system fails catastrophically
- Whiplash injuries from flailing disconnected air hoses

**Existing Risk Controls:**
- Manufacturer-specified pressure regulator and relief valves
- Industrial-grade compressed air fittings and hoses
- Pressure gauges for monitoring system pressure
- Air filtration system to remove particulates and moisture
- Specified air quality requirements in manufacturer documentation
- Equipment designed to operate within specified pressure range
- Built-in pressure monitoring systems

**Current risk rating:** Medium

**Additional controls required:**
- Monthly visual inspection of all air lines, fittings, and connections for wear or damage
- Pressure testing of air supply system annually by qualified technician
- All air line connections must use proper industrial quick-disconnect fittings
- Air line routing must prevent trip hazards and protect from damage
- "High Pressure Air" warning labels at connection points
- Procedure for safe depressurisation before maintenance
- Training on safe compressed air practices including prohibition of using air for cleaning clothing or skin
- Eye protection mandatory when working with compressed air systems
- Annual testing of pressure relief valves
- Secondary pressure regulator if facility air supply exceeds equipment requirements

**Residual risk rating:** Low

---

### Task 3: Electrical Hazards

**Hazard/s:** Dual 24V 200W power supplies and electrical components within the system including electrode power systems, vision systems, and control electronics.

**Associated harm:**
- Electric shock from contact with live electrical components
- Electrical burns from short circuits or component failure
- Fire from electrical faults or overheating
- Equipment damage from power surges or incorrect supply
- Secondary injuries from startle response to electric shock
- Arc flash during maintenance if residual charge present

**Existing Risk Controls:**
- Manufacturer-designed electrical safety systems
- 24V operation reduces shock severity compared to mains voltage
- Enclosed electrical components within equipment housing
- Proper earthing and electrical isolation as per design
- Circuit protection and fusing built into system
- Electrical interconnection cables provided by manufacturer
- CE/relevant certification compliance for electrical safety

**Current risk rating:** Medium

**Additional controls required:**
- Annual electrical safety inspection by qualified electrician
- Residual current device (RCD) protection on mains supply to equipment
- "Electrical Hazard" warning labels on access panels
- Lockout/tagout procedures for any maintenance requiring access to electrical components
- Only qualified electrical personnel authorised to access internal electrical systems
- Immediate shutdown and reporting of any unusual electrical behaviour (sparking, burning smell, tripped breakers)
- Dedicated power circuit for CMS to prevent overloading
- Emergency shutdown procedure prominently displayed
- Testing of earth continuity during annual inspection
- Regular inspection of equipment for signs of electrical overheating or damage
- Documented procedure for safe de-energisation before any internal access

**Residual risk rating:** Low

---

### Task 4: Optical Radiation and Vision System Hazards

**Hazard/s:** Intense visible and infrared radiation from plasma, bright illumination from vision system, and direct viewing of molten glass during processing.

**Associated harm:**
- Eye strain and fatigue from prolonged viewing of bright processes
- Potential retinal damage from intense plasma radiation
- Flash blindness from sudden bright emissions
- Long-term eye damage from repeated exposure to intense light
- Headaches and discomfort from monitor viewing for extended periods
- Temporary vision impairment affecting ability to perform other tasks safely

**Existing Risk Controls:**
- Indirect viewing via camera systems rather than direct observation
- Two orthogonal 5MP cameras with telecentric lenses provide remote viewing
- "Hot Imaging" provides live viewing with appropriate exposure compensation
- Automatic exposure control prevents over or under-exposure of vision system
- 23-inch (or 40-inch with upgrade) monitor for viewing at safe distance
- Processing occurs within chamber, not in direct line of sight
- Vision system designed to handle brightness of plasma without damage

**Current risk rating:** Medium

**Additional controls required:**
- Mandatory pre-operation verification that vision system is functioning correctly
- Prohibition of direct viewing of plasma or molten glass
- Monitor positioned to minimise screen glare and at appropriate height for ergonomic viewing
- Regular breaks during extended operation sessions (minimum 5-minute break every hour)
- Adjustment of monitor brightness to comfortable level for ambient lighting conditions
- Room lighting sufficient to prevent excessive monitor brightness contrast
- Safety glasses with appropriate plasma viewing filters available if direct inspection required (maintenance only)
- Annual vision system calibration and safety assessment
- Documented procedure for what to do if vision system fails during operation (emergency stop)
- Alternative viewing method available if primary system fails
- Immediate reporting of any vision system malfunctions
- Eye examinations recommended for frequent users as part of health surveillance

**Residual risk rating:** Low

---

### Task 5: Sharp Objects and Glass Fibre Handling

**Hazard/s:** Handling of optical fibres, cleaved glass ends, diamond-tipped ultrasonic cleaving blade, broken or scrap fibres, and sharp glass edges.

**Associated harm:**
- Puncture wounds and lacerations from sharp glass fibre ends
- Glass fibre fragments embedded in skin (difficult to see and remove)
- Eye injuries from glass splinters or fragments
- Cuts from diamond cleaving blade during blade changes or maintenance
- Infection from contaminated glass penetrating skin
- Injuries from broken glass components during handling or disposal

**Existing Risk Controls:**
- Integrated cleaver with blade enclosed during operation
- Precision handling systems reduce direct hand contact with fibres
- Fibre holders and fixtures position fibres securely
- Automatic alignment reduces need for manual fibre manipulation
- Manufacturer-designed fibre handling accessories (holders for different diameters)
- Controlled cleaving process reduces random glass shard generation
- Ultrasonic cleaver with controlled operation parameters

**Current risk rating:** Medium

**Additional controls required:**
- Safety glasses mandatory at all times when handling optical fibres
- Close-fitting safety glasses to prevent entry of glass fragments
- Designated sharps disposal containers positioned within easy reach of work area
- Nitrile gloves recommended for handling fibres (provides some cut protection while maintaining dexterity)
- No hand contact with freshly cleaved fibre ends
- Tweezers or fibre handling tools must be used for positioning small components
- Work surface with contrasting colour to improve visibility of glass fragments
- Immediate cleanup of any broken fibres or glass debris using sticky tape or damp cloth (not hands)
- Regular inspection and replacement of diamond cleaving blade per manufacturer schedule
- Lockout procedure when accessing cleaver blade for replacement
- Training on safe fibre handling techniques and first aid for glass injuries
- First aid kit with splinter removal tools available
- Regular workspace cleaning to remove accumulated glass debris
- Warning signs indicating sharp materials hazard
- Magnification available for inspection of fibre handling areas for fragments
- Documented procedure for safe disposal of scrap fibres and glass waste

**Residual risk rating:** Low

---

### Task 6: Vacuum System Operation

**Hazard/s:** Partial vacuum operation capability for adiabatic tapering and specialised processing modes.

**Associated harm:**
- Implosion hazard if vacuum chamber fails structurally
- Rapid inrush of air if seal fails during vacuum operation
- Crush injuries to fingers or hands if caught in vacuum seal mechanisms
- Inhalation of particles if vacuum system draws in contaminated air upon seal breach
- Secondary injuries from sudden pressure equalisation (noise, flying components)

**Existing Risk Controls:**
- Manufacturer-designed vacuum chamber with appropriate pressure rating
- Controlled evacuation and venting procedures built into system
- Pressure monitoring and control systems
- Emergency pressure relief mechanisms
- Chamber designed to withstand operating vacuum levels
- Interlocked systems prevent chamber opening under vacuum

**Current risk rating:** Medium

**Additional controls required:**
- Pre-operation inspection of vacuum chamber seals and O-rings
- Maintenance schedule for vacuum pump and sealing systems
- Immediate shutdown if unusual sounds or pressure readings detected
- Hands and fingers clear of all sealing surfaces before vacuum initiation
- Prohibition of opening chamber until fully vented to atmospheric pressure
- Pressure gauge verification before each vacuum operation
- Annual pressure testing of vacuum chamber by competent person
- Documented procedure for emergency venting
- Training on vacuum system operation and emergency procedures
- Vacuum pump exhaust directed away from operator breathing zone
- Regular inspection of chamber viewing windows for cracks or damage
- Replacement schedule for seals and gaskets

**Residual risk rating:** Low

---

### Task 7: Chemical Hazards from Electrodes and Processing

**Hazard/s:** Electrode materials, potential contamination from electrode wear, cleaning chemicals for electrode maintenance, and any chemicals used in fibre preparation or cleaning.

**Associated harm:**
- Skin irritation or allergic reactions from electrode materials or metal dust
- Inhalation of particulates from electrode wear or cleaning
- Eye irritation from cleaning chemicals
- Chemical burns from improper use of cleaning agents
- Long-term health effects from repeated exposure to metal particulates
- Fire or explosion from incompatible chemical mixing

**Existing Risk Controls:**
- Embedded electrode cooling system minimises oxidation and contamination
- Thermally Stabilised Plasma operation reduces electrode wear compared to conventional systems
- Manufacturer documentation specifies electrode materials and handling
- Enclosed processing area limits airborne particulate spread
- Electrode cleaning performed outside of operating chamber
- Spare electrode sets provided with system

**Current risk rating:** Low

**Additional controls required:**
- Safety Data Sheets (SDS) available for all chemicals used with equipment
- Nitrile gloves worn when handling electrodes or performing cleaning
- Electrode cleaning performed in well-ventilated area or fume hood
- Eye protection during electrode handling and cleaning
- Designated electrode cleaning area with appropriate spill containment
- Electrode disposal via appropriate waste stream (not general waste)
- Training on safe handling of electrode materials
- Respiratory protection assessment if electrode material particulates are generated
- Prohibition of eating, drinking, or applying cosmetics in areas where electrode handling occurs
- Hand washing required after electrode handling
- Regular housekeeping to prevent accumulation of electrode material dust
- Documented procedure for spill response for any cleaning chemicals
- Chemical inventory maintained and reviewed annually

**Residual risk rating:** Very Low

---

### Task 8: Ergonomic and Musculoskeletal Hazards

**Hazard/s:** Prolonged seated work at computer monitor, repetitive precise movements, sustained awkward postures during fibre alignment and loading, and extended periods of concentration.

**Associated harm:**
- Eye strain and visual fatigue from monitor work and precision tasks
- Neck and shoulder pain from sustained postures
- Back pain from prolonged sitting
- Wrist and hand strain from repetitive precision movements
- Mental fatigue from sustained concentration on critical tasks
- Headaches from prolonged near-focus work

**Existing Risk Controls:**
- Adjustable workstation with standard CMS package (upgrade includes ergonomic cart)
- Monitor viewing at appropriate distance via camera systems (no need for extreme close-up work)
- Precision automated alignment reduces manual manipulation requirements
- Orthogonal camera views reduce need for awkward viewing angles

**Current risk rating:** Low

**Additional controls required:**
- Ergonomic workstation assessment and setup for each regular user
- Adjustable chair with lumbar support provided
- Monitor positioned at eye level and appropriate distance (50-70cm)
- Regular micro-breaks during precision work (30 seconds every 10-15 minutes)
- Task rotation where possible to vary physical demands
- Maximum continuous operation time without breaks: 1 hour
- Training on proper posture and ergonomic setup
- Workstation setup checklist completed before extended sessions
- Adequate task lighting to reduce eye strain without creating monitor glare
- Consider upgrade to workstation cart package (CMS-01-0150) for improved ergonomics
- Stretching exercises guidance for operators
- Reporting procedure for any musculoskeletal discomfort
- Periodic ergonomic reviews for frequent users

**Residual risk rating:** Very Low

---

### Task 9: Training and Competency Requirements

**Hazard/s:** Operation of complex, high-hazard equipment by inadequately trained or supervised personnel.

**Associated harm:**
- All hazards listed above are significantly increased if operators lack proper training
- Equipment damage from incorrect operation
- Injury to self or others from not understanding emergency procedures
- Production of unsafe or poor-quality components
- Inability to recognise and respond to abnormal operating conditions

**Existing Risk Controls:**
- Detailed operator's manual provided with equipment
- Multi-day on-site installation and operational training available (TRN-01-0012)
- Complex system requiring demonstrated competency
- PC with all necessary software and documentation included

**Current risk rating:** High (for untrained users)

**Additional controls required:**
- Mandatory completion of manufacturer training before independent operation
- Competency assessment must be completed and documented before authorisation
- Authorised users list maintained and displayed near equipment
- Graduated training program: observation → supervised operation → independent operation
- Minimum supervision requirements for new users (defined in SWP)
- Theory assessment covering safety-critical knowledge
- Practical assessment demonstrating safe operation and emergency response
- Refresher training annually or after 6 months of non-use
- Retraining required after any safety incident or procedure changes
- Documented training records for all operators
- Induction briefing for any visitors or observers covering hazards and emergency procedures
- Prohibition of operation outside authorised users list
- Clear signage indicating training requirement
- Training must include all hazard categories and emergency procedures

**Residual risk rating:** Low (for trained and authorised users)

---

### Task 10: Software and Control System Hazards

**Hazard/s:** Software malfunctions, incorrect programming of tapering or splicing processes, control system failures, and human-computer interface errors.

**Associated harm:**
- Uncontrolled equipment operation from software errors
- Component damage from incorrect process parameters
- Safety system bypass from software faults
- Operator confusion from unclear interface leading to errors
- Inability to execute emergency stop if software freezes
- Loss of critical safety data or process monitoring
- Repetitive strain from poorly designed user interface

**Existing Risk Controls:**
- LabVIEW-based GUI designed for simplified operation
- Table-based tapering software provides process control with preview capability
- Automatic process capture and documentation
- Multiple software interfaces available (including MATLAB, Excel for custom programs)
- PC with all necessary software pre-installed and configured
- Manufacturer software updates and support

**Current risk rating:** Medium

**Additional controls required:**
- Training must include software operation and common error messages
- Emergency stop remains functional regardless of software state (hardware-based)
- Software version control and change management procedures
- Validation of custom programs before use on actual components
- Test runs with dummy components before processing valuable materials
- Regular software backups and system restore points
- Procedure for software failure during operation (safe shutdown process)
- Documentation of all custom programs with safety parameter limits
- User access controls to prevent unauthorised software changes
- Annual software functionality testing including emergency stop interface
- Prohibition of using software from untrusted sources
- Documented process for reporting software issues
- Redundant control (physical emergency stop) independent of software

**Residual risk rating:** Low

---

### Task 11: General Laboratory Safety and Housekeeping

**Hazard/s:** Cluttered work area, spills, trip hazards from cables and air lines, inadequate lighting, poor ventilation, and general laboratory hazards.

**Associated harm:**
- Trips and falls causing injury
- Inability to access emergency equipment or exits
- Increased risk of contamination or cross-contamination
- Fire hazards from combustible materials near heat sources
- Electrical hazards from cable damage
- Delayed emergency response due to obstructed access

**Existing Risk Controls:**
- Defined equipment footprint (71cm W × 56cm D × 43cm H)
- Specified weight (~75 kg) allows for stable positioning
- Necessary cables and connections provided by manufacturer
- Equipment designed for laboratory bench installation

**Current risk rating:** Low

**Additional controls required:**
- Defined equipment location with adequate clearance on all sides (minimum 1 metre)
- Cable management system to prevent trip hazards
- Regular housekeeping schedule (daily cleanup, weekly deep clean)
- Clear access to emergency stop, fire extinguisher, and exits at all times
- Adequate bench space for component staging and handling
- Non-slip matting if floor surface is smooth
- Adequate lighting for precision work (minimum 500 lux at work surface)
- Ventilation adequate for heat dissipation and any fumes
- Storage system for electrodes, fibre holders, and accessories
- Spill kit appropriate for any chemicals used
- Clear labelling of all gas lines, electrical connections, and controls
- Daily pre-operation area inspection checklist
- Immediate cleanup of any spills or broken components
- Fire extinguisher (suitable for electrical fires) within 10 metres
- Monthly safety inspection of work area and equipment surrounds
- Prohibition of food and drink in equipment operation area

**Residual risk rating:** Very Low

---

## Implementation of Additional Risk Controls

| Additional controls needed | Resources required | Responsible person | Date of implementation | RiskWare Reference |
|---------------------------|-------------------|-------------------|----------------------|-------------------|
| Manufacturer training completion | Training course booking, travel costs if off-site | Laboratory Manager | Prior to equipment use | N/A |
| Competency assessment program | Assessment tools, time for practical evaluation | Supervisor/Trainer | Prior to equipment use | N/A |
| Authorised users list creation and display | Signage, documentation system | Laboratory Manager | Prior to equipment use | N/A |
| RCD installation on power supply | Qualified electrician, RCD unit | Facilities/Safety Officer | Prior to equipment use | N/A |
| Annual electrical safety inspection schedule | Qualified electrician, budget allocation | Laboratory Manager | Within 12 months of installation | N/A |
| Thermal inspection camera procurement | Budget for camera purchase | Laboratory Manager | Prior to first use | N/A |
| Sharps disposal containers | Appropriate containers, waste contract | Laboratory Manager | Prior to equipment use | N/A |
| SDS collection for all chemicals | Contact manufacturers, file system | Laboratory Staff | Prior to equipment use | N/A |
| Ergonomic workstation setup | Adjustable chair, assessment tool | OH&S Coordinator | Prior to regular use | N/A |
| Emergency shutdown procedure signage | Sign design and printing | Safety Officer | Prior to equipment use | N/A |
| Exclusion zone markings | Floor tape, warning signs | Laboratory Staff | Prior to equipment use | N/A |
| First aid kit with splinter removal tools | First aid supplies | First Aid Officer | Prior to equipment use | N/A |
| Vacuum system inspection procedure | Procedure documentation | Laboratory Manager | Prior to vacuum operation | N/A |
| Compressed air line inspection schedule | Inspection checklist | Laboratory Manager | Prior to equipment use | N/A |
| Software validation and backup procedures | IT support, documentation | IT/Laboratory Manager | Prior to equipment use | N/A |

---

## List Emergency Controls

### Emergency Shutdown:

1. **Press EMERGENCY STOP button** (location to be identified on equipment and documented in SWP)
2. **Close compressed air supply** using emergency shut-off valve
3. **If emergency stop fails:** Switch off power at mains isolator
4. **Do NOT attempt to restart** until:
   - Emergency condition has been fully resolved
   - Equipment has been inspected by competent person
   - Supervisor has authorised restart
   - Any necessary repairs have been completed

**Do not restart if:**
- Equipment damage is visible
- Unusual sounds, smells, or visual signs were present during emergency
- Cause of emergency is not fully understood
- Any safety system appears compromised

### Fire Emergency:

1. **Activate emergency stop** to shut down all systems
2. **Close compressed air supply** immediately
3. **If fire is small and contained:**
   - Use appropriate fire extinguisher (CO₂ or dry powder for electrical fires)
   - Ensure you have clear escape route
   - Do not fight fire if it threatens your safety
4. **If fire is spreading or involves stored compressed gases:**
   - Evacuate area immediately
   - Activate building fire alarm
   - Call 000 (Emergency Services)
   - Evacuate to assembly point
5. **After fire is extinguished:**
   - Do not re-enter area until declared safe by emergency services
   - Equipment must be inspected before any restart attempt
   - Complete incident report

### Thermal Burn Injury:

1. **Immediately cool affected area** under running cold water for at least 20 minutes
2. **Remove jewellery or constricting items** before swelling occurs
3. **Do NOT apply ice, ointments, or home remedies**
4. **Cover burn with sterile non-stick dressing** after cooling
5. **Seek immediate medical attention** for:
   - Burns larger than a 20-cent coin
   - Burns to face, hands, feet, genitals, or major joints
   - Full thickness burns (white, waxy, or charred appearance)
   - Any burn causing severe pain or blistering
6. **For chemical burns:** Flush with copious water and seek immediate medical attention
7. **Complete incident report** and inform supervisor

### Electric Shock:

1. **Do NOT touch the person** if they are still in contact with electrical source
2. **Switch off power** at mains or remove person using non-conductive material (dry wood, plastic)
3. **Call 000** immediately if person is unconscious or not breathing
4. **If trained in CPR,** commence if required
5. **If conscious but shocked:** Have person lie down and stay still
6. **Treat any burns** as per thermal burn procedure above
7. **Seek medical attention** for all electric shock incidents
8. **Equipment must be tagged out** and inspected before any restart
9. **Complete incident report**

### Glass Injury (Cuts or Embedded Fragments):

1. **Do NOT attempt to remove embedded glass** - seek medical attention
2. **For minor cuts:**
   - Clean wound gently with clean water
   - Apply sterile dressing
   - Seek medical attention if bleeding does not stop
3. **For eye injuries:**
   - Do NOT rub eye
   - Do NOT attempt to remove any object from eye
   - Cover eye with sterile dressing without pressure
   - Seek immediate medical attention
4. **For deep cuts or significant bleeding:**
   - Apply direct pressure with clean cloth
   - Elevate injured area if possible
   - Call 000 if bleeding is severe
5. **All glass injuries must be reported** to supervisor
6. **Complete incident report**

### Compressed Air System Failure:

1. **Activate emergency stop**
2. **Close compressed air supply** at emergency shut-off valve
3. **Evacuate area** if loud hissing or visible air leaks present
4. **Do NOT approach failed air lines or fittings**
5. **If injury from air blast:**
   - Move to safe area
   - Seek immediate medical attention for suspected air embolism (chest pain, difficulty breathing, confusion)
   - Treat any projectile injuries
6. **Lock out and tag equipment**
7. **Contact maintenance** for pressure system inspection
8. **Complete incident report**

### Vacuum System Failure:

1. **Activate emergency stop**
2. **Vent vacuum chamber** using controlled venting procedure (if safe to do so)
3. **If catastrophic failure (implosion or explosion):**
   - Evacuate area immediately
   - Call emergency services if injuries present
   - Do not re-enter until area declared safe
4. **If rapid inrush of air:**
   - Check for injuries from flying debris or noise trauma
   - Seek medical attention as required
5. **Lock out and tag equipment**
6. **Complete incident report**
7. **Equipment must be inspected** by qualified technician before any restart

### Software/Control System Failure:

1. **Attempt emergency stop** via software interface
2. **If software unresponsive:** Use physical emergency stop button
3. **If both fail:** Switch off power at mains
4. **Record error messages or system state** if safe to do so
5. **Do NOT attempt to restart** until IT/technical support has assessed
6. **Lock out and tag equipment**
7. **Complete incident report**
8. **Contact manufacturer technical support** for software issues

### Emergency Contacts:

- **Emergency Services:** 000
- **University Security (after hours):** 9351 3333
- **Supervisor:** Sergio Leon-Saval 
- **Safety Officer:** Chris Betters
- **First Aid Officers:** Christopher Hoffmann (Rm227)

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

### Likelihood Levels

- **Rare:** May occur only in exceptional circumstances (< 5% chance)
- **Unlikely:** Could occur at some time (5-25% chance)
- **Possible:** Might occur at some time (25-50% chance)
- **Likely:** Will probably occur in most circumstances (50-75% chance)
- **Almost Certain:** Expected to occur in most circumstances (> 75% chance)

### Consequence Levels

- **Insignificant:** No injuries, minimal financial loss
- **Minor:** First aid treatment, minor financial loss
- **Moderate:** Medical treatment required, moderate financial loss
- **Major:** Extensive injuries, major financial loss, significant time loss
- **Severe:** Death or permanent disability, huge financial loss

### Risk Rating Matrix

|                    | **Insignificant** | **Minor** | **Moderate** | **Major** | **Severe** |
|-------------------|-------------------|-----------|--------------|-----------|------------|
| **Almost Certain** | Medium            | High      | Very High    | Very High | Very High  |
| **Likely**        | Low               | Medium    | High         | Very High | Very High  |
| **Possible**      | Low               | Medium    | Medium       | High      | Very High  |
| **Unlikely**      | Very Low          | Low       | Medium       | Medium    | High       |
| **Rare**          | Very Low          | Very Low  | Low          | Medium    | High       |

### Risk Control Actions

- **Very High Risk:** Immediate action required. Activity should not proceed.
- **High Risk:** Senior management attention needed. Detailed planning required.
- **Medium Risk:** Management responsibility must be specified. Monitoring required.
- **Low Risk:** Manage by routine procedures. Periodic review.
- **Very Low Risk:** Accept risk. Monitor periodically.

---

*End of Risk Assessment*

**Document Control:**
- This is a DRAFT document requiring review and approval
- All bracketed items [To be completed] must be filled in before approval
- This document must be approved by the Safety Officer before equipment operation commences
- Once approved, this RA must be used to develop the Safe Work Procedure (SWP)
- Annual review is mandatory, or sooner if equipment or processes change
