---
title: "Safe Work Procedure: Fyla Iceblink Supercontinuum Fiber Laser"
reference: SAIL-SWP-FYLA-SUPERCON-001
permalink: /safe-work-procedures/fyla-supercon/
status: Draft
version: "1.0"
date_created: 2025-01-01
date_reviewed: 2025-01-01
date_next_review: 2026-01-01
equipment: Fyla Iceblink Supercontinuum Fiber Laser
manufacturer: Fyla
model: Iceblink
location: Photonic Lantern Wavefront Sensing Setup, School of Physics, University of Sydney
github_issue: 1
associated_risk_assessment: SAIL-RA-FYLA-SUPERCON-001
prepared_by: "[Lab Safety Officer]"
approved_by: "[Supervisor / Lab Manager]"
tags:
  - laser
  - supercontinuum
  - fiber-laser
  - photonics
  - class-3b-or-4
---

# Safe Work Procedure: Fyla Iceblink Supercontinuum Fiber Laser

**SWP Reference:** SAIL-SWP-FYLA-SUPERCON-001
**Associated Risk Assessment:** SAIL-RA-FYLA-SUPERCON-001
**Status:** Draft
**Version:** 1.0
**Location:** Photonic Lantern Wavefront Sensing Setup, School of Physics, University of Sydney

| Prepared By | Role | Date |
|---|---|---|
| [Name] | [Role] | [Date] |

| Supervisor / Approver | Role | Date |
|---|---|---|
| [Name] | [Role / Title] | [Date] |
| [Name] | [Role / Title] | [Date] |

---

## 1. Hazards and Risk Controls Summary

The following hazards have been identified in the associated Risk Assessment (SAIL-RA-FYLA-SUPERCON-001). All controls described below MUST be applied before and during operation.

| # | Hazard | Risk | Primary Control | Secondary Control |
|---|---|---|---|---|
| H1 | Direct or reflected laser beam contact with eyes | Permanent eye injury / blindness | Laser safety eyewear rated for supercontinuum output spectrum (≈400–2400 nm, or as specified for filtered output) | Optical enclosure; beam stops during alignment |
| H2 | Direct or reflected laser beam contact with skin | Burns | Laser safety eyewear; minimise exposed skin; enclosure | Written alignment procedure; reduce power during alignment |
| H3 | Supercontinuum output in free-beam configuration | High irradiance over broad spectral range; eye/skin hazard | Interlock system engaged; appropriate OD-rated eyewear for full output spectrum | Enclosure of beam path |
| H4 | Inadvertent interlock bypass or enclosure breach | Uncontrolled laser exposure | Interlock tested before each use; enclosure integrity verified | Posted warnings; restricted access during operation |
| H5 | Filtered output — residual hazardous wavelengths | Underestimation of hazard if filter selection is incorrect | Confirm filter OD and spectral range matches intended use; verify with power meter | OD calculations reviewed by supervisor before use with new filter |
| H6 | Electrical hazard — mains power and laser controller | Electrocution | Do not open laser unit enclosure; only authorised service personnel access internal components | Inspect power cables before use |
| H7 | Trip/slip hazard from fibre and power cables | Musculoskeletal injury | Route all cables along bench edges and secure with cable ties; post warning signage | Maintain clear walkways |
| H8 | Fire from laser interaction with flammable materials | Fire/burns | Remove flammable materials from beam path and immediate area | Fire extinguisher (CO₂) accessible within lab |

---

## 2. Resources Required

### 2.1 Personal Protective Equipment (PPE)

| Item | Specification | When Required |
|---|---|---|
| Laser safety eyewear | OD rated for the full supercontinuum output spectrum (≈400–2400 nm) OR rated for the specific filtered wavelength range in use; consult supervisor for OD calculation | MANDATORY whenever the beam path is open (free-beam operation) or the enclosure is open |
| Lab coat / long-sleeved clothing | Natural fibre (cotton preferred) | At all times in lab |
| Closed-toe shoes | Any | At all times in lab |
| Laser safety eyewear for visitors | As above; visitor pairs must be kept at lab entry | Required for any person entering the lab while laser is operating in free-beam configuration |

> **NOTE:** When the beam is fully enclosed and all enclosure panels are confirmed closed and interlocked, laser safety eyewear may be removed at the discretion of the responsible operator, in line with the risk assessment. When in doubt, **wear eyewear**.

### 2.2 Equipment and Consumables

- Fyla Iceblink Supercontinuum Fiber Laser unit and controller
- Single-mode or applicable delivery fibre (as installed in the photonic lantern wavefront sensing setup)
- Optical filters appropriate to the experiment (confirm OD and spectral transmission with supervisor before use)
- Optical power meter and appropriate detector head (for output verification)
- Beam block / beam dump rated for the laser power
- Alignment tools (irises, card holders — use fluorescent alignment cards, not unprotected hands or eyes)
- Lens cleaning materials (if required for optics in the beam path)

### 2.3 Safety Equipment

- Laser safety eyewear (operator and visitor pairs) — stored at lab entry
- CO₂ fire extinguisher — located at [specify exact location in lab, e.g., "east wall near exit door"]
- First aid kit — located at [specify location, e.g., "corridor outside lab, Room [XXX]"]
- Emergency eyewash station — located at [specify location]
- Laser hazard warning sign (posted on lab door and activated when laser is operational)
- "Laser in Use — Do Not Enter" illuminated warning sign or equivalent (activated at laser controller keyswitch)

### 2.4 Ventilation

- Standard laboratory ventilation is sufficient for normal operation of this laser.
- No fume extraction is required for laser operation alone.
- If chemical samples or coatings are being exposed to the laser output, assess additional ventilation requirements separately and consult the relevant SDS.

---

## 3. Step-by-Step Instructions

> **IMPORTANT:** These instructions apply to operation of the Fyla Iceblink Supercontinuum Fiber Laser in the Photonic Lantern Wavefront Sensing Setup at the School of Physics, University of Sydney. The laser is used in a filtered configuration delivered via optical fibre. Free-beam sections of the optical path require eyewear and must be enclosed wherever practicable.
>
> **Reference the Fyla Iceblink User Manual (Iceblink-v3.rev04.pdf) for full technical specifications.** This SWP does not replace the manufacturer's manual; it supplements it with site-specific safety requirements.

---

### 3.1 Before Starting — Critical Safety Requirements

1. **Confirm you hold current laser operator certification** issued by the University of Sydney (or equivalent recognised by the School of Physics Safety Officer). Do NOT operate this laser without certification.

2. **Confirm you have read and understood** this SWP (SAIL-SWP-FYLA-SUPERCON-001) and the associated Risk Assessment (SAIL-RA-FYLA-SUPERCON-001) prior to commencing work.

3. **Confirm the experiment has been approved** by your supervisor, including:
   - The specific optical filter(s) to be used and their verified OD and spectral range.
   - Whether operation is free-beam or fully enclosed.
   - The maximum output power setting permitted for this session.

4. **Obtain the correct laser safety eyewear** from the storage location at the lab entry. Confirm the eyewear is rated for the wavelength range and power level applicable to the current configuration (filtered or unfiltered spectrum). If uncertain, **stop and consult your supervisor before proceeding**.

5. **Post the "Laser in Use" warning sign** on the outside of the lab door and ensure the door is closed.

6. **Communicate your intent to operate** to others working in the shared space. Confirm no other person is present in the laser area without appropriate eyewear.

---

### 3.2 Pre-Operation Safety Checks (MANDATORY — DO NOT SKIP)

> **If ANY of the following checks fails: DO NOT USE THE LASER. Lock out the controller (remove key), post an "Out of Service" notice, and report the fault to the Laboratory Manager or Supervisor immediately.**

Perform all checks in order and record the outcome in the laboratory logbook.

1. **Sign in to the laboratory logbook.** Record: date, time, your name, experiment description, laser power settings to be used, and filter configuration.

2. **Inspect the Fyla Iceblink laser unit and controller for visible damage.**
   - Check the unit casing for cracks, burn marks, or signs of impact.
   - Check the mains power cable for cuts, fraying, exposed conductors, or damaged plugs.
   - Check the fibre delivery cable for kinks, sharp bends, crushing, or connector damage.
   - **Expected result:** No visible damage on any component. If damage is found, do not power on.

3. **Inspect the optical bench and beam path for obstructions and hazards.**
   - Confirm all flammable materials (paper, cloth, solvents) are removed from within 300 mm of the beam path and any optical component.
   - Confirm all retroreflective or highly specular objects (jewellery, watch faces, metal tools) are removed from the beam path area.
   - Confirm the beam dump / beam block is correctly positioned at the beam terminus.
   - **Expected result:** Clear, unobstructed beam path with rated beam dump in place.

4. **Verify the optical enclosure integrity** (if operating in enclosed configuration).
   - Inspect all enclosure panels, lids, and covers along the full beam path for correct seating.
   - Confirm all enclosure clips, screws, or fasteners are engaged.
   - Confirm there are no gaps greater than the minimum safe aperture for the output power in use.
   - **Expected result:** Fully sealed enclosure with no open apertures.

5. **Verify the interlock system is functional** (required for free-beam sections; see Section 3.4, Step 5 for full test procedure).
   - Confirm the interlock cable is connected to the Fyla Iceblink controller interlock port.
   - Confirm the interlock is connected to any enclosure panels or doors covering the beam path, as installed.
   - If operating in free-beam configuration without enclosure interlock: confirm laser safety eyewear is worn by ALL persons in the room and restricted access is enforced. Document this in the logbook.
   - **Expected result:** Interlock circuit is closed (controller indicates "Interlock OK" or equivalent status indication per the Fyla Iceblink User Manual); or, for free-beam operation, eyewear confirmed on all occupants.

6. **Confirm optical filter(s) are correctly installed and verified.**
   - Identify each filter by its marked specification (part number, centre wavelength, OD, or bandpass range).
   - Confirm the filter specification matches the supervisor-approved configuration recorded in the logbook.
   - Confirm the filter is correctly seated in its mount and oriented in the correct direction (if directional).
   - **Expected result:** Approved filter(s) installed and confirmed as specified. Do not operate with unidentified or unapproved filters.

7. **Verify laser safety eyewear condition and rating.**
   - Inspect lenses for scratches, cracks, or degradation that could reduce optical density.
   - Confirm the OD marking on the frame matches the required protection for this configuration.
   - Confirm eyewear fits correctly and provides full coverage without gaps.
   - **Expected result:** Eyewear is undamaged, correctly rated, and fits properly. Replace damaged eyewear before operating.

8. **Confirm the emergency stop / keyswitch is in the OFF position** before connecting to mains power.
   - The Fyla Iceblink controller keyswitch must be in the **OFF / STANDBY** position.
   - **Expected result:** Keyswitch is in the OFF position; laser emission indicator is not lit.

9. **Verify the power meter / detector is available and functional** for output power verification after startup.
   - Power on the power meter and select the appropriate detector head for the filtered wavelength range.
   - Zero the power meter.
   - **Expected result:** Power meter powers on and zeroes correctly. If the power meter is faulty, do not proceed — output power cannot be verified.

10. **Confirm laboratory access control is active.**
    - Confirm the "Laser in Use" sign is illuminated or posted on the lab door.
    - Confirm the lab door is closed.
    - Confirm only authorised and briefed personnel are present.
    - **Expected result:** Lab is secured, warning posted, and only qualified personnel present.

> **Record the outcome of all checks in the laboratory logbook before proceeding.**

---

### 3.3 Material Preparation and Approval

1. **Confirm experimental approval with your supervisor** before commencing, specifically:
   - The maximum output power setting (in mW) and repetition rate or pulse mode setting to be used.
   - The specific filter configuration and its verified OD values across the full supercontinuum spectrum.
   - Whether alignment will require brief free-beam access and the approved procedure for doing so.

2. **Calculate and confirm the Nominal Ocular Hazard Distance (NOHD)** for the current filter and power configuration if operating with any free-beam section. Use the values from the associated Risk Assessment (SAIL-RA-FYLA-SUPERCON-001) or request a supervisor review for non-standard configurations.

3. **Confirm the beam dump rating** is appropriate for the maximum output power in use. Check the beam dump manufacturer's maximum power rating and confirm it exceeds the Fyla Iceblink maximum output for the current configuration.

4. **Prepare alignment aids** (fluorescent alignment cards, IR detector cards if applicable) and place them in accessible locations. **NEVER use unprotected eyes, hands, or skin to locate or verify a laser beam.**

---

### 3.4 Equipment Startup

1. **Don laser safety eyewear** rated for the supercontinuum output spectrum (or filtered output, as confirmed in pre-operation checks). Eyewear MUST be worn before the laser controller is powered on.

2. **Connect the Fyla Iceblink controller to mains power** at the power board or wall outlet. Confirm the mains indicator on the controller illuminates.

3. **Power on the Fyla Iceblink controller** using the main power switch (refer to Iceblink-v3.rev04.pdf, Section [Controller Operation], for the exact switch location and label). Allow the controller to complete its boot sequence.
   - **Expected result:** Controller display or status LEDs indicate STANDBY or READY state with no fault codes.
   - If a fault code is displayed, refer to the Fyla Iceblink User Manual fault code table. Do not proceed until the fault is resolved.

4. **Verify the interlock status** on the controller display or status indicator.
   - Navigate to the status display per the Fyla Iceblink User Manual.
   - **Expected result:** Interlock status reads "OK", "Closed", or equivalent (not "FAULT" or "OPEN").
   - If the interlock status reads as open or faulted: identify and resolve the cause before proceeding. Do not bypass the interlock.

5. **Test the interlock system** (MANDATORY for each session involving free-beam sections):
   - With the controller in STANDBY (key ON, emission OFF), deliberately open or disconnect the interlock circuit (e.g., open the enclosure panel connected to the interlock).
   - **Expected result:** Controller interlock status changes to FAULT/OPEN and the laser is inhibited from emission.
   - Close or reconnect the interlock circuit.
   - **Expected result:** Controller interlock status returns to OK/CLOSED.
   - Record the result in the laboratory logbook.

6. **Insert the keyswitch and rotate to the ON position** (refer to Iceblink-v3.rev04.pdf for exact keyswitch location and operation). The keyswitch must remain under the control of the responsible operator at all times during the session.
   - **Expected result:** Controller transitions from STANDBY to ENABLED/ARMED state. The laser emission warning indicator activates.

7. **Set the laser output parameters** to the approved values for this session:
   - Set output power to the minimum level required for the experiment (do not exceed the supervisor-approved maximum).
   - Set repetition rate, pulse width, or CW mode as required per the experimental protocol and as permitted in the Fyla Iceblink User Manual.
   - **Do not enable emission at this stage.**

---

### 3.5 Prepare Job / Operation

1. **Configure the optical setup** for the experiment:
   - Confirm the delivery fibre is correctly connected to the Fyla Iceblink fibre output port. Inspect the fibre connector ferrule and the port for contamination or damage before mating.
   - Tighten or latch the fibre connector as specified in the Fyla Iceblink User Manual. Do not overtighten.
   - Confirm filters are installed in the correct position in the beam path (as verified in pre-operation checks).

2. **Confirm the beam path is unobstructed** from the fibre output through to the beam dump, by visual inspection along the bench. Do not lean over the beam path.

3. **Confirm the photonic lantern wavefront sensing setup** is in the correct configuration for the experiment and that all downstream optical components are aligned and secured.

4. **Set the power meter detector** at the appropriate measurement point to allow output power verification after enabling emission. Do not position the detector in a location requiring the operator to reach over or into the beam path to read it.

5. **Conduct a final verbal or visual check** with all persons in the lab:
   - Announce: "Laser going live — confirm eyewear on."
   - Confirm all occupants confirm eyewear is correctly worn before enabling emission.

---

### 3.6 Load Material / Workpiece

> *This laser is used as a fixed light source in the photonic lantern wavefront sensing optical setup. There is no separate workpiece loading step. If test samples or optical components are being placed in the beam path as part of the experiment, apply the following steps.*

1. **Power the laser to STANDBY (emission OFF)** before placing any optical element, sample, or component into the beam path.

2. **Mount the component or sample** in its holder. Confirm it is mechanically stable and will not shift during operation.

3. **Confirm the component is approved** for use at the current laser power and wavelength range (check manufacturer's damage threshold specifications).

4. **Close all enclosure panels** after mounting. Confirm interlock status returns to OK before re-enabling emission.

---

### 3.7 Start Operation

1. **Perform a final safety check** immediately before enabling emission:
   - Eyewear on: **Yes / No** (record in logbook)
   - Interlock OK: **Yes / No** (record in logbook)
   - Enclosure closed: **Yes / No** (record in logbook)
   - Lab door closed: **Yes / No** (record in logbook)
   - All occupants confirmed: **Yes / No** (record in logbook)

2. **Enable laser emission** using the emission enable control on the Fyla Iceblink controller (refer to Iceblink-v3.rev04.pdf for the exact control label and location — typically a dedicated "EMISSION ON" button or equivalent).
   - **Expected result:** Emission indicator illuminates on the controller; laser output begins at the set power level.

3. **Immediately verify output power** using the power meter:
   - Read the output power at the measurement point.
   - Confirm the reading is within the expected range for the set power level and filter configuration.
   - **If output power is significantly higher than expected: immediately press EMISSION OFF and investigate before re-enabling.**

4. **Monitor the laser and optical setup continuously** during operation. Do not leave the laser unattended while emission is active.
   - Check for any unexpected beam scatter, reflections, or fluorescence from optical components.
   - Check for any unusual sounds from the laser controller (fan noise change, alarms).
   - Check the fibre cable for heating at the connector or along its length.

5. **If an unexpected event occurs** (unusual beam behaviour, component failure, equipment alarm, or any doubt about safety): press the EMISSION OFF control immediately, then assess the situation. Do not re-enable emission until the cause is identified and resolved.

6. **Record the start time, power setting, and filter configuration** in the laboratory logbook.

---

### 3.8 Completion and Shutdown

1. **Disable laser emission** using the emission enable control on the Fyla Iceblink controller (press "EMISSION OFF" or equivalent). Confirm the emission indicator extinguishes.

2. **Record the end time and any observations** in the laboratory logbook.

3. **Rotate the keyswitch to the OFF position** and remove the key. Store the key in the designated location (as defined by the Laboratory Manager).

4. **Power down the Fyla Iceblink controller** using the main power switch.

5. **Disconnect from mains power** if this is the last session of the day or if the equipment will be unattended.

6. **Do not disconnect the delivery fibre** unless specifically required by the experiment and approved by the supervisor. If disconnection is required:
   - Confirm emission is OFF and controller is powered down before disconnecting.
   - Cap the fibre connector and the laser output port immediately after disconnection to prevent contamination.

7. **Remove laser safety eyewear** only after confirming the controller is powered down and the keyswitch is removed.

8. **Clear the beam path area**: remove any alignment aids, tools, or temporary components used during the session.

9. **Clean up the work area** (see Section 8 — Clean Up and Waste Disposal Requirements).

10. **Sign out in the laboratory logbook**: record completion time and any faults, anomalies, or maintenance required.

11. **Remove the "Laser in Use" warning sign** from the lab door once operation is complete and the laser is fully shut down.

---

## 4. Emergency Shutdown Procedures

### 4.1 Emergency Stop — Immediate Laser Shutdown

**Location of emergency stop / emission off:** The primary emission stop is the **EMISSION OFF control on the Fyla Iceblink controller front panel** (refer to Iceblink-v3.rev04.pdf for exact button label, colour, and location).

**To perform emergency shutdown:**

1. **Press the EMISSION OFF control** on the Fyla Iceblink controller. Laser emission ceases immediately.
   - **Expected result:** Emission indicator extinguishes; laser output stops.

2. **Rotate the keyswitch to OFF** and remove the key.

3. **Power down the controller** using the main power switch if safe to do so.

4. **Disconnect from mains power** at the power board if the situation requires full power isolation.

5. **If the emission off control is inaccessible or fails to stop emission:**
   - Disconnect the mains power supply at the wall outlet or power board immediately.
   - Do not reach across the beam path to access the controller.

6. **Do not re-enable the laser** until the cause of the emergency has been identified, documented, and resolved with the supervisor.

### 4.2 Interlock Fault

1. If the controller displays an interlock fault during operation, **the laser will automatically inhibit emission**.
2. Confirm emission has ceased (emission indicator off, power meter reads zero).
3. Identify the cause of the interlock fault:
   - Check that all enclosure panels are fully closed and fastened.
   - Check that the interlock cable is fully connected to the controller interlock port.
4. **Do not bypass or defeat the interlock under any circumstances.**
5. If the interlock fault cannot be resolved, report to the Laboratory Manager and do not operate the laser.

---

## 5. Emergency Procedures

### 5.1 Eye Exposure to Laser Radiation

1. **Immediately press EMISSION OFF** on the Fyla Iceblink controller to stop laser emission.
2. **Do not rub the affected eye(s).**
3. **Call for assistance** — do not attempt to self-treat a laser eye injury.
4. **Call 000 (Emergency Services) immediately.** Laser eye injuries are medical emergencies requiring specialist ophthalmological assessment.
5. **Contact the University of Sydney Security and Emergency:** [Insert University Emergency Number — typically 02 9351 3333 or internal extension].
6. **Contact the supervisor or Laboratory Manager** at [insert supervisor name and contact number].
7. **Keep the affected person calm and still** until emergency services arrive. Do not allow them to move around the lab unassisted.
8. **Record the laser parameters** (wavelength/filter, power setting, exposure duration if known) and provide this information to emergency services.
9. **Do not leave the affected person alone.**
10. **Complete a University of Sydney incident report** as soon as practicable after the emergency.

### 5.2 Skin Exposure or Burns

1. **Press EMISSION OFF** on the Fyla Iceblink controller immediately.
2. **For minor burns (superficial redness only):** cool the area with running water for 20 minutes. Do not apply ice. Seek medical assessment.
3. **For serious burns:** call 000 immediately. Do not remove clothing adhered to the burn. Keep the person still and warm until emergency services arrive.
4. **Contact the supervisor or Laboratory Manager** and complete an incident report.

### 5.3 Fire

1. **Press EMISSION OFF** on the Fyla Iceblink controller and power down the controller immediately.
2. **If the fire is small and contained** (e.g., smouldering material in the beam path):
   - Use the CO₂ fire extinguisher located at [specify location].
   - Apply CO₂ to the base of the fire using a sweeping motion.
   - **Never use water on electrical equipment.**
3. **If the fire is growing or cannot be immediately controlled:**
   - **Activate the nearest fire alarm pull station.**
   - **Evacuate the laboratory immediately** via the nearest exit: [specify primary and secondary exit routes].
   - Close doors behind you — do not lock.
   - Call 000 and report the fire.
   - Do not re-enter the laboratory.
4. **Notify the Laboratory Manager and University Safety Office** as soon as it is safe to do so.

### 5.4 Fibre Damage or Laser System Malfunction

1. **Press EMISSION OFF** on the Fyla Iceblink controller immediately.
2. **Rotate keyswitch to OFF** and power down the controller.
3. **Do not handle a damaged delivery fibre** — broken fibre ends may emit hazardous radiation and the fibre tip may cause puncture wounds.
4. If the fibre is visibly broken or the controller displays a fault code that cannot be resolved by consulting the Fyla Iceblink User Manual: **do not attempt to operate the laser**.
5. **Isolate the equipment** (lock out at mains if required) and post an "Out of Service" notice.
6. **Report the fault to the Laboratory Manager** for assessment and manufacturer-authorised servicing.

### 5.5 Unauthorised Entry During Operation

1. **If a person without appropriate eyewear enters the lab during active free-beam operation:**
   - Immediately announce: "STOP — laser in use — do not move."
   - **Press EMISSION OFF** on the controller.
   - Direct the person to stop and close their eyes until emission is confirmed off.
2. Confirm emission is off before allowing the person to move freely.
3. Brief the person on the laser hazard and the requirement for eyewear before re-enabling emission.
4. Report the incident to the Laboratory Manager and complete an incident report.

---

## 6. Emergency Contacts

| Contact | Name | Phone |
|---|---|---|
| Emergency Services (Ambulance / Fire / Police) | — | **000** |
| University of Sydney Security and Emergency | — | **[02 9351 3333 or internal XXX]** |
| Laboratory Manager | [Name] | [Phone / Extension] |
| Supervisor | [Name] | [Phone / Extension] |
| School of Physics Safety Officer | [Name] | [Phone / Extension] |
| Poisons Information Centre (non-emergency) | — | **13 11 26** |

---

## 7. Clean Up and Waste Disposal Requirements

### 7.1 Routine Clean Up After Each Session

1. **Confirm laser emission is OFF and the controller is powered down** before commencing any clean-up activities.

2. **Inspect the optical bench** for any debris, dust, or contamination that may have accumulated on optical surfaces.

3. **Clean optical components** (lenses, filters, mirrors) only if required and only using approved lens tissue and optical cleaning fluid. Follow the "drag and drop" method; do not rub optical surfaces in a circular motion. Dispose of used lens tissue in general waste.

4. **Inspect the fibre connector** end faces for contamination if the fibre was connected or disconnected during the session. Clean using an approved fibre cleaning tool (e.g., fibre cleaning swab or click cleaner). Dispose of used cleaning swabs in general waste.

5. **Remove and store** any alignment aids, beam blocks, or test components used during the session.

6. **Return all tools** to their designated storage locations.

7. **Leave the optical bench in the standard operating configuration** or in the supervisor-specified state for the next session.

### 7.2 Waste Types and Disposal

| Waste Type | Description | Disposal Method |
|---|---|---|
| Lens tissue / optical cleaning materials | Solvent-contaminated if IPA used | If contaminated with isopropanol (IPA): allow to evaporate fully in a fume cupboard before disposal in general waste. Quantities of >250 mL of IPA: dispose as chemical waste. |
| Fibre cleaning swabs | Contaminated with fibre cleaning solvent | Allow solvent to evaporate, dispose in general waste. |
| Damaged fibre sections | Silica glass fibre fragments | **Hazardous — puncture risk.** Seal in a rigid container (e.g., plastic bottle with lid) labelled "Broken Glass — Silica Fibre". Dispose in sharps/glass waste stream as directed by University waste management. |
| Damaged optical filters | Glass / coated optical elements | Broken glass: seal in rigid container, dispose in glass waste stream. Intact damaged filters: consult supervisor for special optical material disposal. |
| Worn or degraded laser safety eyewear | Plastic / polycarbonate lens | Dispose in general waste. Remove from service and record disposal in equipment register. |
| Packaging and cardboard | Consumable packaging | General recycling. |

> **Hazardous Waste:** If any chemical reagents, solvents, or coated materials are used in conjunction with this laser, consult the relevant SDS and the University of Sydney hazardous waste disposal procedure. Do not mix chemical waste streams.

---

## 8. References

1. Fyla Iceblink Supercontinuum Fiber Laser User Manual, v3.rev04 — [Iceblink-v3.rev04.pdf, available from Fyla website: https://fyla.com/laser/iceblink-supercontinuum-fiber-laser/]
2. SAIL-RA-FYLA-SUPERCON-001 — Risk Assessment: Fyla Iceblink Supercontinuum Fiber Laser, School of Physics, University of Sydney
3. Australian Radiation Protection and Nuclear Safety Agency (ARPANSA) — Radiation Protection Standard for Occupational Exposure to Laser Radiation (RPS 12)
4. Safe Work Australia — Code of Practice: Labelling of Workplace Hazardous Chemicals
5. University of Sydney Work Health and Safety Policy — [Insert current University WHS Policy reference]
6. University of Sydney Laser Safety Policy / Laser Safety Guidelines — [Insert reference if applicable]
7. AS/NZS IEC 60825.1:2023 — Safety of laser products, Part 1: Equipment classification and requirements
8. University of Sydney Laser Operator Certification Program — [Insert reference / link]
9. University of Sydney Hazardous Waste Disposal Procedure — [Insert reference]

---

## 9. Competency Required

### 9.1 Mandatory Pre-Requisite Training

All operators MUST have completed the following before operating the Fyla Iceblink Supercontinuum Fiber Laser:

| # | Training Requirement | Provider | Evidence Required |
|---|---|---|---|
| 1 | University of Sydney Laser Operator Certification | School of Physics / University Safety | Current certification card or certificate |
| 2 | Laser Safety Induction (including laser classes, NOHD, OD calculations, biological effects of laser radiation) | School of Physics Safety Officer or equivalent | Induction record in training register |
| 3 | Equipment-specific induction: Fyla Iceblink (covering controller operation, interlock, fibre handling, filter use) | Approved Assessor (see Section 10) | Induction record in training register |
| 4 | Read and signed acknowledgement of this SWP (SAIL-SWP-FYLA-SUPERCON-001) and Risk Assessment (SAIL-RA-FYLA-SUPERCON-001) | Self-certified, witnessed by supervisor | Signed SWP sign-off sheet (Section 11) |
| 5 | Familiarity with Fyla Iceblink User Manual (Iceblink-v3.rev04.pdf) | Self-study | Confirmed during practical assessment |

### 9.2 Theory Assessment

Before unsupervised operation, the operator must demonstrate understanding of the following topics by passing a verbal or written assessment (minimum pass mark: **80%**):

- Laser classification system and the classification of the Fyla Iceblink
- Biological effects of supercontinuum laser radiation on eyes and skin across the full output spectrum
- Correct selection and verification of laser safety eyewear OD for a given power and wavelength range
- Function and testing of the interlock system on the Fyla Iceblink
- Role and verification of optical filters in reducing hazard
- Emergency shutdown procedure for the Fyla Iceblink
- Emergency procedure for laser eye exposure
- Correct fibre handling and connector cleaning procedures
- University WHS incident reporting requirements

### 9.3 Practical Assessment

Before unsupervised operation, the operator must demonstrate the following practical tasks to the satisfaction of an Approved Assessor:

1. Correctly don and verify laser safety eyewear appropriate to the setup.
2. Complete all 10 mandatory pre-operation safety checks in the correct order without prompting.
3. Correctly test the interlock system and interpret the controller status indication.
4. Safely power on the Fyla Iceblink controller, set approved output parameters, and enable emission.
5. Verify laser output power using a power meter.
6. Perform a safe, controlled shutdown of the Fyla Iceblink.
7. Correctly connect and disconnect the delivery fibre, including inspection and cleaning of the connector end face.
8. Describe the correct response to a laser eye exposure emergency without prompting.
9. Locate and correctly use the CO₂ fire extinguisher (demonstration, not live fire).
10. Complete a logbook entry for a simulated session (start, operation, shutdown, and anomaly recording).

### 9.4 Ongoing Competency Requirements

| Requirement | Frequency | Action if Not Met |
|---|---|---|
| Laser Operator Certification renewal | As required by University policy (typically annual or biennial) | Certification lapses: operator may not use laser until recertified |
| SWP review and re-acknowledgement | On each document revision or at minimum every 2 years | Operator must re-read and re-sign the updated SWP before next use |
| Practical refresher / re-assessment | If operator has not used the laser for more than 12 months | Supervised re-induction session with Approved Assessor before unsupervised operation resumes |
| Incident-triggered retraining | Following any safety incident or near-miss involving this laser | Full re-assessment (theory and practical) before return to unsupervised operation |

### 9.5 Retraining Triggers

An operator MUST undergo retraining before resuming unsupervised operation if:

- They have been involved in a laser safety incident or near-miss on any laser system.
- They have not operated a laser for more than 12 consecutive months.
- The equipment configuration (power level, filter set, beam path) has changed significantly from that covered in their original assessment.
- Their Laser Operator Certification has lapsed.
- The SWP has been substantially revised and the assessor determines retraining is required.

### 9.6 Training Records

- All training, inductions, and assessments must be recorded in the School of Physics training register [insert register location/link].
- Operators must retain a copy of their current Laser Operator Certification and be able to produce it on request.
- Assessors must record practical assessment outcomes and sign the assessment record.

---

## 10. Staff Approved to Assess Competence

> The following persons are approved to conduct practical and theory assessments for this equipment. Only persons listed here may sign off new operators for unsupervised use.

| Name | Position | Contact | Date Approved |
|---|---|---|---|
| [Name] | [Position] | [Email / Phone] | [Date] |
| [Name] | [Position] | [Email / Phone] | [Date] |

> **To be added to this list**, a staff member must: hold current Laser Operator Certification, have demonstrated competency on the Fyla Iceblink for a minimum of [e.g., 6 months], and be approved by the School of Physics Safety Officer and Laboratory Manager.

---

## 11. SWP Sign-Off Sheet

> All operators must read this Safe Work Procedure and the associated Risk Assessment (SAIL-RA-FYLA-SUPERCON-001) before operating the Fyla Iceblink Supercontinuum Fiber Laser. Sign below to confirm you have read, understood, and will comply with all requirements. This sheet must be retained by the Laboratory Manager.

| # | Full Name (Print) | Signature | Date | Supervisor / Assessor Name | Assessor Signature |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |

*Additional sign-off sheets available from the Laboratory Manager.*

---

## 12. Document Review Schedule

| Review Event | Details |
|---|---|
| **Scheduled Review Frequency** | Every **2 years** from date of approval, or earlier if triggered by an incident, equipment change, or regulatory update |
| **Next Scheduled Review Date** | [Date — 2 years from approval date] |
| **Review Trigger Events** | Laser safety incident or near-miss; change to laser configuration, power, or filter set; change in University WHS policy or Australian laser safety standards; change in laboratory layout affecting emergency egress or equipment location |
| **Review Responsibility** | Laboratory Manager in consultation with School of Physics Safety Officer and supervising academic |
| **Review Process** | Reviewer confirms alignment with current Risk Assessment; confirms all contact details and room locations are current; consults with approved assessors; submits revised document for approval via SAIL documentation system |

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 1.0 | [Date] | [Name] | Initial draft |
| | | | |

---

*This Safe Work Procedure is a controlled document. The current version is available at: [https://your-sail-site/safe-work-procedures/fyla-supercon/](https://your-sail-site/safe-work-procedures/fyla-supercon/). Printed copies are uncontrolled. Verify you are using the current version before commencing work.*

*For queries regarding this document, contact the Laboratory Manager or School of Physics Safety Officer.*
```