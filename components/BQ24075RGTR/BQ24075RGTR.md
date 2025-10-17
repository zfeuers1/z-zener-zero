# BQ2407x Standalone 1-Cell 1.5-A Linear Battery Chargers with Power Path 

## 1 Features

- Fully compliant USB charger
- Selectable 100-mA and 500-mA maximum input current
- 100-mA Maximum current limit ensures compliance to USB-IF standard
- Input-based dynamic power management ( $\mathrm{V}_{\mathrm{IN}}$ DPM) for protection against poor USB sources
- Functional Safety-Capable (BQ24074)
- Documentation available to aid functional safety system design
- 28-V Input rating with overvoltage protection
- Integrated dynamic power path management (DPPM) function simultaneously and independently powers the system and charges the battery
- Supports up to 1.5-A charge current with current monitoring output (ISET)
- Programmable input current limit up to 1.5 A for wall adapters
- System output tracks battery voltage (BQ24072)
- Programmable termination current (BQ24074)
- Battery disconnect function with SYSOFF input (BQ24075, BQ24079)
- Programmable pre-charge and fast-charge safety timers
- Reverse current, short-circuit and thermal protection
- NTC thermistor input
- Proprietary start-up sequence limits inrush current
- Status indication - charging/done, power good
- Safety-Related Certification:
- IEC 62368-1 Certification (BQ24072)


## 2 Applications

- TWS Charging case and headphones
- Gaming accessory
- Video doorbells, IP network cameras
- Asset tracking and fleet management
- Portable medical devices


## 3 Description

The BQ2407x series of devices are integrated Li-lon linear chargers and system power path management devices targeted at space-limited portable applications. The devices operate from either a USB port or an AC adapter and support charge currents up to 1.5 A . The input voltage range with input overvoltage protection supports unregulated adapters. The USB input current limit accuracy and start up sequence allow the BQ2407x to meet USB-

IF inrush current specifications. Additionally, the input dynamic power management ( $\mathrm{V}_{\mathrm{IN}}$-DPM) prevents the charger from crashing incorrectly configured USB sources.

The BQ2407x features dynamic power path management (DPPM) that powers the system while simultaneously and independently charging the battery. The DPPM circuit reduces the charge current when the input current limit causes the system output to fall to the DPPM threshold; thus, supplying the system load at all times while monitoring the charge current separately. This feature reduces the number of charge and discharge cycles on the battery, allows for proper charge termination and enables the system to run with a defective or absent battery pack.

Device Information

| PART NUMBER ${ }^{(1)}$ | PACKAGE | BODY SIZE (NOM) |
| :-- | :-- | :-- |
| BQ24072 |  |  |
| BQ24073 | VQFN (16) | $3.00 \mathrm{~mm} \times 3.00 \mathrm{~mm}$ |
| BQ24074 |  |  |
| BQ24075 |  |  |
| BQ24079 |  |  |

(1) For all available packages, see the orderable addendum at the end of the data sheet.
![img-0.jpeg](img-0.jpeg)

Typical Application Circuit# Table of Contents 

1 Features ..... 1
2 Applications ..... 1
3 Description ..... 1
4 Revision History ..... 2
5 Description (continued) ..... 5
6 Device Comparison Table ..... 6
7 Pin Configuration and Functions ..... 7
8 Specifications ..... 10
8.1 Absolute Maximum Ratings ${ }^{(1)}$ ..... 10
8.2 ESD Ratings ..... 10
8.3 Recommended Operating Conditions ..... 10
8.4 Thermal Information ..... 11
8.5 Electrical Characteristics ..... 12
8.6 Typical Characteristics ..... 14
9 Detailed Description ..... 17
9.1 Overview ..... 17
9.2 Functional Block Diagram ..... 18
9.3 Feature Description ..... 19
9.4 Device Functional Modes ..... 31
10 Application and Implementation ..... 33
10.1 Application Information ..... 33
10.2 Typical Application ..... 33
10.3 System Examples ..... 38
11 Power Supply Recommendations ..... 39
12 Layout ..... 40
12.1 Layout Guidelines ..... 40
12.2 Layout Example ..... 41
12.3 Thermal Considerations ..... 42
13 Device and Documentation Support ..... 43
13.1 Device Support ..... 43
13.2 Receiving Notification of Documentation Updates ..... 43
13.3 Support Resources ..... 43
13.4 Trademarks ..... 43
13.5 Electrostatic Discharge Caution ..... 43
13.6 Glossary ..... 43
14 Mechanical, Packaging, and Orderable Information ..... 43

## 4 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision M (August 2019) to Revision N (October 2021) Page

- Added Functional Safety-Capable (BQ24074) to Features ..... 1
- Added Safety-Related Certification: IEC 62368-1 Certification (BQ24072) to Features ..... 1
- Changed Applications ..... 1
- Changed BQ24079T information and package in Section 6 ..... 6
- Added $\mathrm{I}_{\text {BAT(PDWN) }}$ TYP value ..... 12
- Added I $_{\text {IN }}$ TYP values ..... 12
- Added $\mathrm{I}_{\mathrm{CC}}$ TYP value ..... 12
Changes from Revision L (June 2018) to Revision M (August 2019) Page
- Changed the document title ..... 1
- Changed the Device Comparison Table ..... 6
- Deleted the Dissipation Ratings table ..... 11
- Changed $\mathrm{V}_{\text {IN-LOW }}$ To $\mathrm{V}_{\text {IN-DPM }}$ in the Functional Block Diagram ..... 18
- Changed text From: "the DPPM loop or the $\mathrm{V}_{\text {IN-(LOW) }}$ loop." To: "the DPPM loop or the $\mathrm{V}_{\text {IN-DPM }}$ loop." in the Battery Charging secton ..... 24
- Chganged text From: " input voltage has fallen to $\mathrm{V}_{\text {IN(LOW) }}$ " To: "input voltage has fallen to $\mathrm{V}_{\text {IN-DPM }}$ " in the Dynamic Charge Timers (TMR Input) scrtion ..... 27
- Changed Equation 11 ..... 42
Changes from Revision K (March 2015) to Revision L (June 2018) Page
- Deleted MARKINGS from the Device Comparison Table ..... 6
- Added the RGT0016B and RGT0016C package information to the Device Comparison Table ..... 6
- Changed the Pinout images and descriptions ..... 7
- Change description of the CE pin From: "Connect CE to a high logic level to place the battery charger in standby mode. In standby mode, ..." To ""Connect CE to a high logic level to disable battery charging. OUT is active and battery supplement mode is still available." ..... 7
- "Changed text in the third paragraph of the Power On section From: When $\mathrm{V}_{\text {OUT }}$ is above $\mathrm{V}_{\mathrm{SC}}$, ..." To: "When $\mathrm{V}_{\text {OUT }}$ is above $\mathrm{V}_{\mathrm{O}(\mathrm{SC} 1) \ldots}$ ..... 19- Changed text From: "The valid resistor range is $590 \Omega$ to $5.9 \mathrm{k} \Omega$." To: "The valid resistor range is $590 \Omega$ to 8.9 $\mathrm{k} \Omega$." in the Battery Charging section. ..... 24
- Changed From: $\mathrm{V}_{\mathrm{IN}(\mathrm{DT})}$ To: $\mathrm{V}_{\mathrm{BAT}}+\mathrm{V}_{\mathrm{IN}(\mathrm{DT})}$ in Table 9-1 ..... 28
- Changed $\mathrm{I}_{\mathrm{NTC}}$ To: $\mathrm{I}_{\mathrm{TS}}$ in Figure 9-9 ..... 29
Changes from Revision J (January 2015) to Revision K (March 2015) ..... Page
- Deleted package type code from Device Comparison Table. See the POA at the end of the data sheet. ..... 6
- Changed $\mathrm{I}_{\mathrm{CHG}}$ Battery fast charge current range MIN specification from "150 mA " to "100 mA" ..... 12
Changes from Revision I (January 2014) to Revision J (January 2015) ..... Page
- Added ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and Mechanical, Packaging, and Orderable Information section ..... 1
Changes from Revision H (December 2013) to Revision I (January 2014) ..... Page
- Changed resistor value from " $3 \mathrm{k} \Omega$ " to " $8.9 \mathrm{k} \Omega$ " in the Pin Functions table ISET Description paragraph. ..... 7
- Changed $\mathrm{R}_{\text {ISET }}$ spec MAX value from " 3000 " to " 8900 " in the Recommended Operating Conditions table. ..... 10
- Changed resistor value from " $3 \mathrm{k} \Omega$ " to " $5.9 \mathrm{k} \Omega$ " in the Battery Charging section paragraph. ..... 24
Changes from Revision G (July 2011) to Revision H (December 2013) ..... Page
- Changed $\mathrm{I}_{\mathrm{CHG}}$ Battery fast charge current range MIN specification from " 300 mA " to " 150 mA ". ..... 12
Changes from Revision F (September 2010) to Revision G (July 2011) ..... Page
- Added ESD human body model specification to Abs Maximum Ratings table. ..... 10
Changes from Revision E (August 2010) to Revision F (September 2010) ..... Page
- Changed $10 \times 45 \mathrm{~s} / \mathrm{k} \Omega$ to $10 \times 48 \mathrm{~s} / \mathrm{k} \Omega$ under section Program 6.25 hour. (TMR) ..... 34
Changes from Revision D (June 2009) to Revision E (August 2010) ..... Page
- Changed globally RT1 and RT2 to Rs and Rp. ..... 29
- Added equations 2 and 3 plus explanations and table. ..... 29
Changes from Revision C (March 2009) to Revision D (June 2009) ..... Page
- Added Device number BQ24079 ..... 1
Changes from Revision B (January 2009) to Revision C (March 2009) ..... Page
- Changed Maximum input current factor values. ..... 12
Changes from Revision A (December 2008) to Revision B (January 2009) ..... Page
- Changed $\mathrm{V}_{\text {BAT(REG) }}$ max value From 4.24 V To: 4.23 V ..... 12Changes from Revision * (September 2008) to Revision A (December 2008) ..... Page

- Changed device Features ..... 1
- Changed Description ..... 1
- Changed Typical Application Circuit ..... 1
- Changed description of $\overline{\mathrm{CHG}}$ pin ..... 7
- Changed SYSOFF Description ..... 7
- Added Figure 10-5 through Figure 8-1 ..... 14
- Changed DETAILED FUNCTIONAL DESCRIPTION section ..... 17
- Changed the Functional Block Diagram ..... 18
- Changed text in section - STATUS INDICATORS ( PGOOD, CHG) ..... 28
- Changed Table - $\overline{\text { CHG }}$ STATUS INDICATOR ..... 28
- Changed Equation 8 and Equation 9 ..... 29
- Changed APPLICATION CIRCUITS section ..... 33
- Added Using BQ24075 to Disconnect the Battery from the System, Figure 10-13 ..... 38
- Changed section - Half-Wave Adaptors ..... 39# 5 Description (continued) 

Additionally, the regulated system input enables instant system turn-on when plugged in even with a totally discharged battery. The power path management architecture also lets the battery supplement the system current requirements when the adapter cannot deliver the peak system currents, thus enabling the use of a smaller adapter.

The battery is charged in three phases: conditioning, constant current, and constant voltage. In all charge phases, an internal control loop monitors the IC junction temperature and reduces the charge current if the internal temperature threshold is exceeded. The charger power stage and charge current sense functions are fully integrated. The charger function has high accuracy current and voltage regulation loops, charge status display, and charge termination. The input current limit and charge current are programmable using external resistors.# 6 Device Comparison Table 

| PART NUMBER ${ }^{(1)(2)}$ | $\mathrm{V}_{\text {OVP }}$ | $\mathrm{V}_{\text {BAT(REG) }}$ | $\mathrm{V}_{\text {OUT(REG) }}$ | $\mathrm{V}_{\text {OPPM }}$ | TS METHOD | OPTIONAL FUNCTION | PACKAGE |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| BQ24072 | 6.6 V | 4.2 V | $\mathrm{V}_{\text {BAT }}+225 \mathrm{mV}$ | $\mathrm{V}_{\text {O(REG) }}-100 \mathrm{mV}$ | Current Based | TD | RGT0016C |
| BQ24073 | 6.6 V | 4.2 V | 4.4 V | $\mathrm{V}_{\text {O(REG) }}-100 \mathrm{mV}$ |  | TD |  |
| BQ24074 | 10.5 V | 4.2 V | 4.4 V | $\mathrm{V}_{\text {O(REG) }}-100 \mathrm{mV}$ |  | ITERM |  |
| BQ24075 | 6.6 V | 4.2 V | 5.5 V | 4.3 V |  | SYSOFF |  |
| BQ24076 | 6.6 V | 4.4 V | $\mathrm{V}_{\text {BAT }}+225 \mathrm{mV}$ | $\mathrm{V}_{\text {O(REG) }}-100 \mathrm{mV}$ |  | SYSOFF |  |
| BQ24078 | 6.6 V | 4.35 V | $\mathrm{V}_{\text {BAT }}+225 \mathrm{mV}$ | $\mathrm{V}_{\text {O(REG) }}-100 \mathrm{mV}$ |  | SYSOFF |  |
| BQ24079 | 6.6 V | 4.1 V | 5.5 V | 4.3 V |  | SYSOFF |  |
| BQ24072T | 6.6 V | 4.2 V | $\mathrm{V}_{\text {BAT }}+225 \mathrm{mV}$ | $\mathrm{V}_{\text {O(REG) }}-100 \mathrm{mV}$ | Voltage Based | TD |  |
| BQ24075T | 6.6 V | 4.2 V | 5.5 V | 4.3 V |  | SYSOFF |  |
| BQ24079T | 6.6 V | 4.1 V | 5.5 V | 4.3 V |  | SYSOFF |  |

(1) For all available packages, see the orderable addendum at the end of the data sheet
(2) This product is RoHS compatible, including a lead concentration that does not exceed $0.1 \%$ of total product weight, and is suitable for use in specified lead-free soldering processes. In addition, this product uses package materials that do not contain halogens, including bromine $(\mathrm{Br})$ or antimony $(\mathrm{Sb})$ above $0.1 \%$ of total product weight.# 7 Pin Configuration and Functions 

![img-1.jpeg](img-1.jpeg)

Figure 7-1. BQ24072, BQ24073 RGT0016B Package 16 Pins Top View
![img-2.jpeg](img-2.jpeg)

Figure 7-2. BQ24074 RGT0016B Package 16 Pins Top View![img-3.jpeg](img-3.jpeg)

Figure 7-3. BQ24075 RGT0016C Package, BQ24079 RGT0016B Package 16 Pins Top View
Table 7-1. Pin Functions

| PIN |  |  |  |  | I/O | DESCRIPTION |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| NAME | '72, '73 | '74 | '75, '79 |  |  |  |
| BAT | 2,3 | 2,3 | 2,3 | I/O | Charger Power Stage Output and Battery Voltage Sense Input. Connect BAT to the positive terminal of the battery. Bypass BAT to VSS with a $4.7-\mu \mathrm{F}$ to $47-\mu \mathrm{F}$ ceramic capacitor. |  |
| CE | 4 | 4 | 4 | I | Charge Enable Active-Low Input. Connect CE to a high logic level to disable battery charging. OUT is active and battery supplement mode is still available. Connect CE to a low logic level to enable the battery charger. CE is internally pulled down with approximately $285 \mathrm{k} \Omega$. Do not leave CE unconnected to ensure proper operation. |  |
| CHG | 9 | 9 | 9 | 0 | Open-Drain Charging Status Indication Output. CHG pulls to VSS when the battery is charging. CHG is high impedance when charging is complete and when charger is disabled. Connect CHG to the desired logic voltage rail using a $1 \mathrm{k} \Omega-100 \mathrm{k} \Omega$ resistor, or use with an LED for visual indication. |  |
| EN1 | 6 | 6 | 6 | I | Input Current Limit Configuration Inputs. Use EN1 and EN2 control the maximum input current and enable USB compliance. See Table 7-2 for the description of the operation states. EN1 and EN2 are internally pulled down with $+285 \mathrm{k} \Omega$. Do not leave EN1 or EN2 unconnected to ensure proper operation. |  |
| EN2 | 5 | 5 | 5 | I |  | Adjustable Current Limit Programming Input. Connect a $1100-\Omega$ to $8-\mathrm{k} \Omega$ resistor from ILIM to VSS to program the maximum input current (EN2=1, EN1=0). The input current includes the system load and the battery charge current. Leaving ILIM unconnected disables all charging. |
| ILIM | 12 | 12 | 12 | I |  | Input Power Connection. Connect IN to the external DC supply (AC adapter or USB port). The input operating range is 4.35 V to 6.6 V (BQ24072, BQ24073, BQ24075, and BQ24079) or 4.35 V to 10.5 V (bq24074). The input can accept voltages up to 26 V without damage but operation is suspended. Connect bypass capacitor $1 \mu \mathrm{~F}$ to $10 \mu \mathrm{~F}$ to VSS. |
| IN | 13 | 13 | 13 | I |  | Fast Charge Current Programming Input. Connect a $590-\Omega$ to $8.9-\mathrm{k} \Omega$ resistor from ISET to VSS to program the fast charge current level. Charging is disabled if ISET is left unconnected. While charging, the voltage at ISET reflects the actual charging current and can be used to monitor charge current. See Section 9.3.5.1 for more details. |
| ISET | 16 | 16 | 16 | I/O |  | Termination Current Programming Input. Connect a $0-\Omega$ to $15-\mathrm{k} \Omega$ resistor from ITERM to VSS to program the termination current. Leave ITERM unconnected to set the termination current to the default 10\% termination threshold. |
| ITERM | - | 15 | - | I |  | System Supply Output. OUT provides a regulated output when the input is below the OVP threshold and above the regulation voltage. When the input is out of the operation range, OUT is connected to $\mathrm{V}_{\mathrm{BAT}}$ except when SYSOFF is high (BQ24075 and BQ24079 only). Connect OUT to the system load. Bypass OUT to VSS with a $4.7-\mu \mathrm{F}$ to $47-\mu \mathrm{F}$ ceramic capacitor. |
| OUT | 10,11 | 10, 11 | 10, 11 | 0 |  | Open-drain Power Good Status Indication Output. PGOOD pulls to VSS when a valid input source is detected. PGOOD is high-impedance when the input power is not within specified limits. Connect PGOOD to the desired logic voltage rail using a $1-\mathrm{k} \Omega$ to $100-\mathrm{k} \Omega$ resistor, or use with an LED for visual indication. |
| PGOOD | 7 | 7 | 7 | 0 |  | System Enable Input. Connect SYSOFF high to turn off the FET connecting the battery to the system output. When an adapter is connected, charging is also disabled. Connect SYSOFF low for normal operation. SYSOFF is internally pulled up to $\mathrm{V}_{\mathrm{BAT}}$ through a large resistor (approximately $5 \mathrm{M} \Omega$ ). Do not leave SYSOFF unconnected to ensure proper operation. |Table 7-1. Pin Functions (continued)

|  PIN |  |  |  |  | DESCRIPTION  |
| --- | --- | --- | --- | --- | --- |
|  NAME | '72, '73 | '74 | '75, '79 |  |   |
|  TD | 15 | - | - | I | Termination Disable Input. Connect TD high to disable charger termination. Connect TD to VSS to enable charger termination. TD is checked during startup only and cannot be changed during operation. See the TD section in this datasheet for a description of the behavior when termination is disabled. TD is internally pulled down to VSS with approximately $285 \mathrm{k} \Omega$. Do not leave TD unconnected to ensure proper operation.  |
|  Thermal Pad | - | - | - | - | There is an internal electrical connection between the exposed thermal pad and the VSS pin of the device. The thermal pad must be connected to the same potential as the VSS pin on the printed circuit board. Do not use the thermal pad as the primary ground input for the device. VSS pin must be connected to ground at all times.  |
|  TMR | 14 | 14 | 14 | I | Timer Programming Input. TMR controls the pre-charge and fast-charge safety timers. Connect TMR to VSS to disable all safety timers. Connect a $18-\mathrm{k} \Omega$ to $72-\mathrm{k} \Omega$ resistor between TMR and VSS to program the timers a desired length. Leave TMR unconnected to set the timers to the default values.  |
|  TS | 1 | 1 | 1 | I | External NTC Thermistor Input. Connect the TS input to the NTC thermistor in the battery pack. TS monitors a $10 \mathrm{k} \Omega$ NTC thermistor. For applications that do not use the TS function, connect a $10-\mathrm{k} \Omega$ fixed resistor from TS to VSS to maintain a valid voltage level on TS.  |
|  VSS | 8 | 8 | 8 | - | Ground. Connect to the thermal pad and to the ground rail of the circuit.  |

Table 7-2. EN1/EN2 Settings

| EN2 | EN1 | MAXIMUM INPUT CURRENT INTO IN PIN |
| :--: | :--: | :-- |
| 0 | 0 | 100 mA . USB100 mode |
| 0 | 1 | 500 mA . USB500 mode |
| 1 | 0 | Set by an external resistor from ILIM to VSS |
| 1 | 1 | Standby (USB suspend mode) |# 8 Specifications 

### 8.1 Absolute Maximum Ratings ${ }^{(1)}$

over the $0^{\circ} \mathrm{C}$ to $125^{\circ} \mathrm{C}$ operating free-air temperature range (unless otherwise noted)

|  |  |  | MIN | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $V_{i}$ | Input Voltage | IN (with respect to VSS) | $-0.3$ | 28 | V |
|  |  | BAT (with respect to VSS) | $-0.3$ | 5 | V |
|  |  | OUT, EN1, EN2, CE, TS, ISET, PGOOD, CHG, ILIM, TMR, ITERM, SYSOFF, TD (with respect to VSS) | $-0.3$ | 7 | V |
| $I_{i}$ | Input Current | IN |  | 1.6 | A |
| $I_{0}$ | Output Current (Continuous) | OUT |  | 5 | A |
|  |  | BAT (Discharge mode) |  | 5 | A |
|  |  | BAT (Charging mode) |  | $1.5^{(2)}$ | A |
|  | Output Sink Current | CHG, PGOOD |  | 15 | mA |
| $T_{J}$ | Junction temperature |  | $-40$ | 150 | ${ }^{\circ} \mathrm{C}$ |
| $T_{\text {stg }}$ | Storage temperature |  | $-65$ | 150 | ${ }^{\circ} \mathrm{C}$ |

(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indicated under Section 8.3 is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. All voltage values are with respect to the network ground terminal unless otherwise noted.
(2) The IC operational charging life is reduced to 20,000 hours, when charging at 1.5 A and $125^{\circ} \mathrm{C}$. The thermal regulation feature reduces charge current if the IC's junction temperature reaches $125^{\circ} \mathrm{C}$; thus without a good thermal design the maximum programmed charge current may not be reached.

### 8.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| :--: | :--: | :--: | :--: | :--: |
| $V_{i E S D}$ | Electrostatic discharge | Human body model (HBM), per ANSI/ESDA/JEDEC JS-001 ${ }^{(1)}$ | $\pm 2000$ | V |
|  |  | Charged-device model (CDM), per JEDEC specification JESD22- <br> C101(2) | $\pm 500$ |  |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

### 8.3 Recommended Operating Conditions

|  |  |  | MIN | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $V_{i}$ | IN voltage range |  | 4.35 | 26 | V |
|  | IN operating voltage range | '72, '73, '75, '79 | 4.35 | 6.4 | V |
|  |  | '74 | 4.35 | 10.2 |  |
| $\mathrm{I}_{\text {IN }}$ | Input current, IN pin |  |  | 1.5 | A |
| $\mathrm{I}_{\text {OUT }}$ | Current, OUT pin |  |  | 4.5 | A |
| $\mathrm{I}_{\text {BAT }}$ | Current, BAT pin (Discharging) |  |  | 4.5 | A |
| $\mathrm{I}_{\text {CHG }}$ | Current, BAT pin (Charging) |  |  | $1.5^{(2)}$ | A |
| $T_{J}$ | Junction Temperature |  | $-40$ | 125 | ${ }^{\circ} \mathrm{C}$ |
| $R_{\text {ILIM }}$ | Maximum input current programming resistor |  | 1100 | 8000 | $\Omega$ |
| $R_{\text {ISET }}$ | Fast-charge current programming resistor ${ }^{(1)}$ |  | 590 | 8900 | $\Omega$ |
| $R_{\text {ITERM }}$ | Termination current programming resistor |  | 0 | 15 | $\mathrm{k} \Omega$ |
| $R_{\text {TMR }}$ | Timer programming resistor |  | 18 | 72 | $\mathrm{k} \Omega$ |

(1) Use a $1 \%$ tolerance resistor for $R_{\text {ISET }}$ to avoid issues with the $R_{\text {ISET }}$ short test when using the maximum charge current setting.
(2) The IC operational charging life is reduced to 20,000 hours, when charging at 1.5 A and $125^{\circ} \mathrm{C}$. The thermal regulation feature reduces charge current if the IC's junction temperature reaches $125^{\circ} \mathrm{C}$; thus without a good thermal design the maximum programmed charge current may not be reached.# 8.4 Thermal Information 

| THERMAL METRIC ${ }^{(1)}$ |  | BQ2407x | UNIT |
| :--: | :--: | :--: | :--: |
|  |  | RGT |  |
|  |  | 16 PINS |  |
| $R_{8, \text { IA }}$ | Junction-to-ambient thermal resistance | 44.5 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $R_{8, \text { IC(bop) }}$ | Junction-to-case (top) thermal resistance | 54.2 |  |
| $R_{8, B B}$ | Junction-to-board thermal resistance | 17.2 |  |
| $\psi_{J T}$ | Junction-to-top characterization parameter | 1.0 |  |
| $\psi_{J B}$ | Junction-to-board characterization parameter | 17.1 |  |
| $R_{8, \text { IC(bot) }}$ | Junction-to-case (bottom) thermal resistance | 3.8 |  |

(1) For more information about traditional and new thermal metrics, see the Semiconductor IC Package Thermal Metrics application report.# 8.5 Electrical Characteristics 

Over junction temperature range $\left(0^{\circ} \leq T_{J} \leq 125^{\circ} \mathrm{C}\right)$ and the recommended supply voltage range (unless otherwise noted)

|  | PARAM | TE | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| INPUT |  |  |  |  |  |  |  |
| UVLO | Undervoltage lock-out | $V_{A V} 0 \mathrm{~V} \rightarrow 4 \mathrm{~V}$ |  | 3.2 | 3.3 | 3.4 | V |
| $V_{\text {hys }}$ | Hysteresis on UVLO | $V_{A V} 4 \mathrm{~V} \rightarrow 0 \mathrm{~V}$ |  | 200 |  | 300 | mV |
| $V_{\text {IN(OT) }}$ | Input power detection threshold | Input power detected when $V_{I N}>V_{\text {BAT }}+V_{\text {IN(OT) }}$ $V_{\text {BAT }}=3.6 \mathrm{~V}, \mathrm{VIN}: 3.5 \mathrm{~V} \rightarrow 4 \mathrm{~V}$ |  | 55 | 80 | 130 | mV |
| $V_{\text {hys }}$ | Hysteresis on $V_{\text {IN(OT) }}$ | $V_{\text {BAT }}=3.6 \mathrm{~V}, V_{\text {IN }} 4 \mathrm{~V} \rightarrow 3.5 \mathrm{~V}$ |  | 20 |  |  | mV |
| $\mathrm{t}_{\text {DGL(POOOD) }}$ | Deglitch time, input power detected status | Time measured from $V_{I N}: 0 \mathrm{~V} \rightarrow 5 \mathrm{~V} 1 \mu \mathrm{~s}$ rise-time to $\mathrm{PGOOD}=\mathrm{LO}$ |  |  | 1.2 |  | ms |
| $V_{\text {OVP }}$ | Input overvoltage protection threshold | $V_{A V} 5 \mathrm{~V} \rightarrow 7 \mathrm{~V}$ | $(72,73,75,79)$ | 6.4 | 6.6 | 6.8 | V |
|  |  | $V_{A V} 5 \mathrm{~V} \rightarrow 11 \mathrm{~V}$ | (74) | 10.2 | 10.5 | 10.8 |  |
| $V_{\text {hys }}$ | Hysteresis on OVP | $V_{A V} 7 \mathrm{~V} \rightarrow 5 \mathrm{~V}$ | $(72,73,75,79)$ |  | 110 |  | mV |
|  |  | $V_{A V} 11 \mathrm{~V} \rightarrow 5 \mathrm{~V}$ | (74) |  | 175 |  |  |
| $\mathrm{t}_{\text {DGL(OVP) }}$ | Input overvoltage blanking time (OVP fault deglitch) |  |  |  | 50 |  | $\mu \mathrm{s}$ |
| $\mathrm{t}_{\text {REC }}$ | Input overvoltage recovery time | Time measured from $V_{I N}: 11 \mathrm{~V} \rightarrow 5 \mathrm{~V}$ with $1 \mu \mathrm{~s}$ fall-time to $\mathrm{PGOOD}=\mathrm{LO}$ |  |  | 1.2 |  | ms |
| ILIM, ISET SHORT-CIRCUIT DETECTION (CHECKED DURING STARTUP) |  |  |  |  |  |  |  |
| $\mathrm{t}_{\text {SC }}$ | Current source | $V_{I N}>$ UVLO and $V_{I N}>V_{\text {BAT }}+V_{\text {IN(OT) }}$ |  |  | 1.3 |  | mA |
| $V_{\text {SC }}$ |  | $V_{I N}>$ UVLO and $V_{I N}>V_{\text {BAT }}+V_{\text {IN(OT) }}$ |  |  | 520 |  | mV |
| QUIESCENT CURRENT |  |  |  |  |  |  |  |
| $\mathrm{t}_{\text {BAT(POWIN) }}$ | Sleep current into BAT pin | $\overline{\mathrm{CE}}=\mathrm{LO}$ or HI , input power not detected, No load on OUT pin, $\mathrm{T}_{\mathrm{J}}=85^{\circ} \mathrm{C}$ |  |  | 4.3 | 6.5 | $\mu \mathrm{A}$ |
| $\mathrm{t}_{\text {IN }}$ | Standby current into IN pin | EN1 $=\mathrm{HI}, \mathrm{EN} 2=\mathrm{HI}, \mathrm{V}_{\mathrm{IN}}=6 \mathrm{~V}, \mathrm{~T}_{\mathrm{J}}=85^{\circ} \mathrm{C}$ |  |  | 41.3 | 50 | $\mu \mathrm{A}$ |
|  |  | EN1 $=\mathrm{HI}, \mathrm{EN} 2=\mathrm{HI}, \mathrm{V}_{\mathrm{IN}}=10 \mathrm{~V}, \mathrm{~T}_{\mathrm{J}}=85^{\circ} \mathrm{C}$ |  |  | 99.8 | 200 |  |
| $\mathrm{t}_{\text {CC }}$ | Active supply current, IN pin | $\overline{\mathrm{CE}}=\mathrm{LO}, \mathrm{V}_{\mathrm{IN}}=6 \mathrm{~V}$, no load on OUT pin, $V_{\text {BAT }}=V_{\text {BAT(REG) }},(\mathrm{EN} 1, \mathrm{EN} 2) \neq(\mathrm{HI}, \mathrm{HI})$ |  |  | 1.1 | 1.5 | mA |
| POWER PATH |  |  |  |  |  |  |  |
| $V_{\text {DO(IN-OUT) }}$ | $V_{I N}-V_{\text {OUT }}$ | $V_{I N}=4.3 \mathrm{~V}, \mathrm{I}_{\mathrm{IN}}=1 \mathrm{~A}, V_{\text {BAT }}=4.2 \mathrm{~V}$ |  |  | 300 | 475 | mV |
| $V_{\text {DO(BAT-OUT) }}$ | $V_{\text {BAT }}-V_{\text {OUT }}$ | $\mathrm{t}_{\text {OUT }}=1 \mathrm{~A}, V_{\text {IN }}=0 \mathrm{~V}, V_{\text {BAT }}=3 \mathrm{~V}$ |  |  | 50 | 100 | mV |
| $V_{\text {O(REG) }}$ | OUT pin voltage regulation (BQ24072) | $V_{I N}>V_{\text {OUT }}+V_{\text {DO(IN-OUT) }}, V_{\text {BAT }}=3.2 \mathrm{~V}$ |  | 3.3 | 3.4 | 3.5 | V |
|  |  | $V_{I N}>V_{\text {OUT }}+V_{\text {DO(IN-OUT) }}, V_{\text {BAT }}=3.2 \mathrm{~V}$ |  | $\begin{gathered} V_{\text {BAT }}+ \\ 150 \mathrm{mV} \end{gathered}$ | $\begin{gathered} V_{\text {BAT }}+ \\ 225 \mathrm{mV} \end{gathered}$ | $\begin{gathered} V_{\text {BAT }}+ \\ 270 \mathrm{mV} \end{gathered}$ |  |
|  | OUT pin voltage regulation (BQ24073, BQ24074) | $V_{I N}>V_{\text {OUT }}+V_{\text {DO(IN-OUT) }}$ |  | 4.3 | 4.4 | 4.5 |  |
|  | OUT pin voltage regulation (BQ24075, BQ24079) | $V_{I N}>V_{\text {OUT }}+V_{\text {DO(IN-OUT) }}$ |  | 5.4 | 5.5 | 5.6 |  |
| $\mathrm{t}_{\text {IN }}$ max | Maximum input current | EN1 $=\mathrm{LO}, \mathrm{EN} 2=\mathrm{LO}$ |  | 90 | 95 | 100 | mA |
|  |  | EN1 $=\mathrm{HI}, \mathrm{EN} 2=\mathrm{LO}$ |  | 450 | 475 | 500 |  |
|  |  | EN2 $=\mathrm{HI}, \mathrm{EN} 1=\mathrm{LO}$ |  |  | $\mathrm{K}_{\text {ILIM }} / \mathrm{K}_{\text {ILIM }}$ |  | A |
| $\mathrm{K}_{\text {ILIM }}$ | Maximum input current factor | $\mathrm{I}_{\mathrm{LIM}}=500 \mathrm{~mA}$ to 1.5 A |  | 1500 | 1610 | 1720 | $A \Omega$ |
|  |  | $\mathrm{I}_{\mathrm{LIM}}=200 \mathrm{~mA}$ to 500 mA |  | 1330 | 1525 | 1720 |  |
| $\mathrm{t}_{\text {IN }}$ max | Programmable input current limit range | EN2 $=\mathrm{HI}, \mathrm{EN} 1=\mathrm{LO}, \mathrm{R}_{\text {ILIM }}=8 \mathrm{k} \Omega$ to $1.1 \mathrm{k} \Omega$ |  | 200 |  | 1500 | mA |
| $V_{\text {IN.DPM }}$ | Input voltage threshold when input current is reduced | EN2 $=\mathrm{LO}, \mathrm{EN} 1=\mathrm{X}$ |  | 4.35 | 4.5 | 4.63 | V |
| $V_{\text {DPPM }}$ | Output voltage threshold when charging current is reduced |  | $(72,73,74)$ | $\begin{gathered} V_{\text {O(REG) }}- \\ 180 \mathrm{mV} \end{gathered}$ | $\begin{gathered} V_{\text {O(REG) }}- \\ 100 \mathrm{mV} \end{gathered}$ | $\begin{gathered} V_{\text {O(REG) }}- \\ 30 \mathrm{mV} \end{gathered}$ | V |
|  |  |  | $(75,79)$ | 4.2 | 4.3 | 4.4 | V |
| $V_{\text {BSUP1 }}$ | Enter battery supplement mode | $V_{\text {BAT }}=3.6 \mathrm{~V}, R_{\text {ILIM }}=1.5 \mathrm{k} \Omega, R_{\text {LOAD }}=10 \Omega \rightarrow 2 \Omega$ |  |  | $\begin{gathered} V_{\text {OUT }} \leq V_{\text {BAT }}- \\ 40 \mathrm{mV} \end{gathered}$ |  | V |
| $V_{\text {BSUP2 }}$ | Exit battery supplement mode | $V_{\text {BAT }}=3.6 \mathrm{~V}, R_{\text {ILIM }}=1.5 \mathrm{k} \Omega, R_{\text {LOAD }}=2 \Omega \rightarrow 10 \Omega$ |  |  | $\begin{gathered} V_{\text {OUT }} \geq V_{\text {BAT }}- \\ 20 \mathrm{mV} \end{gathered}$ |  | V |
| $V_{\text {O(SC1) }}$ | Output short-circuit detection threshold, power-on | $V_{I N}>V_{\text {UVLO }}$ and $V_{I N}>V_{\text {BAT }}+V_{\text {IN(OT) }}$ |  | 0.8 | 0.9 | 1 | V |
| $V_{\text {O(SC2) }}$ | Output short-circuit detection threshold, supplement mode $V_{\text {BAT }}-V_{\text {OUT }}>V_{\text {O(SC2) }}$ indicates short-circuit | $V_{I N}>V_{\text {UVLO }}$ and $V_{I N}>V_{\text {BAT }}+V_{\text {IN(OT) }}$ |  | 200 | 250 | 300 | mV |
| $\mathrm{t}_{\text {DGL(SC2) }}$ | Deglitch time, supplement mode short circuit |  |  |  | 250 |  | $\mu \mathrm{s}$ |
| $\mathrm{t}_{\text {REC(SC2) }}$ | Recovery time, supplement mode short circuit |  |  |  | 60 |  | ms |# 8.5 Electrical Characteristics (continued) 

Over junction temperature range $\left(0^{\circ} \leq T_{J} \leq 125^{\circ} \mathrm{C}\right)$ and the recommended supply voltage range (unless otherwise noted)

| PARAMETER |  | TEST CONDITIONS |  | MIN | TYP | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| BATTERY CHARGER |  |  |  |  |  |  |  |
| $\mathrm{I}_{\text {BAT }}$ | Source current for BAT pin short-circuit detection | $\mathrm{V}_{\text {BAT }}=1.5 \mathrm{~V}$ |  | 4 | 7.5 | 11 | mA |
| $\mathrm{V}_{\text {BAT(SC) }}$ | BAT pin short-circuit detection threshold | $\mathrm{V}_{\text {BAT }}$ rising |  | 1.6 | 1.8 | 2 | V |
| $\mathrm{V}_{\text {BAT(REG) }}$ | Battery charge voltage |  | $\begin{aligned} & \text { (72, '73, '74, '75) } \\ & \text { ('79) } \end{aligned}$ | $\begin{aligned} & 4.16 \\ & 4.059 \end{aligned}$ | $\begin{aligned} & 4.20 \\ & 4.100 \end{aligned}$ | $\begin{aligned} & 4.23 \\ & 4.141 \end{aligned}$ | V |
| $\mathrm{V}_{\text {LOWV }}$ | Pre-charge to fast-charge transition threshold | $\mathrm{V}_{\mathrm{IN}}>\mathrm{V}_{\text {UVLO }}$ and $\mathrm{V}_{\mathrm{IN}}>\mathrm{V}_{\text {BAT }}+\mathrm{V}_{\text {IN(OT) }}$ |  | 2.9 | 3 | 3.1 | V |
| $\mathrm{I}_{\text {D(IL1LOWV) }}$ | Deglitch time on pre-charge to fast-charge transition |  |  |  | 25 |  | ms |
| $\mathrm{I}_{\text {D(IL2LOWV) }}$ | Deglitch time on fast-charge to pre-charge transition |  |  |  | 25 |  | ms |
| $\mathrm{I}_{\text {CHG }}$ | Battery fast charge current range | $\begin{aligned} & \mathrm{V}_{\text {BAT(REG) }}>\mathrm{V}_{\text {BAT }}>\mathrm{V}_{\text {LOWV }}, \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V} \mathrm{CE}=\mathrm{LO}, \\ & \mathrm{EN} 1=\mathrm{LO}, \mathrm{EN} 2=\mathrm{HI} \end{aligned}$ |  | 100 |  | 1500 | mA |
|  | Battery fast charge current | $\mathrm{CE}=\mathrm{LO}, \mathrm{EN} 1=\mathrm{LO}, \mathrm{EN} 2=\mathrm{HI},$ <br> $\mathrm{V}_{\text {BAT }}>\mathrm{V}_{\text {LOWV }}, \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V}, \mathrm{I}_{\mathrm{IN}} \max >\mathrm{I}_{\text {CHG }}$, no load on OUT pin, thermal loop and DPPM loop not active |  | $\mathrm{K}_{\text {ISET }} / \mathrm{R}_{\text {ISET }}$ |  |  | A |
| $\mathrm{K}_{\text {ISET }}$ | Fast charge current factor |  |  | 797 | 890 | 975 | $A \Omega$ |
| $\mathrm{I}_{\text {PRECHG }}$ | Pre-charge current |  |  | $\mathrm{K}_{\text {PRECHG }} / \mathrm{R}_{\text {ISET }}$ |  |  | A |
| $\mathrm{K}_{\text {PRECHG }}$ | Pre-charge current factor |  |  | 70 | 88 | 106 | $A \Omega$ |
| $\mathrm{I}_{\text {TERM }}$ | Termination comparator detection threshold (internally set) | $\mathrm{CE}=\mathrm{LO},(\mathrm{EN} 1, \mathrm{EN} 2) \neq(\mathrm{LO}, \mathrm{LO})$, <br> $\mathrm{V}_{\text {BAT }}>\mathrm{V}_{\text {RCH }} 1+\mathrm{I}_{\text {MAXCH }}, \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V}$, DPPM loop and thermal loop not active |  | $0.09 \times \mathrm{I}_{\mathrm{CHG}}$ | $0.1 \times \mathrm{I}_{\mathrm{CHG}}$ | $0.11 \times \mathrm{I}_{\mathrm{CHG}}$ | A |
|  |  | $\mathrm{CE}=\mathrm{LO},(\mathrm{EN} 1, \mathrm{EN} 2)=(\mathrm{LO}, \mathrm{LO})$, <br> $\mathrm{V}_{\text {BAT }}>\mathrm{V}_{\text {RCH }} 1+\mathrm{I}_{\text {MAXCH }}, \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V}$, DPPM loop and thermal loop not active |  | $0.027 \times \mathrm{I}_{\mathrm{CHG}}$ | $0.033 \times \mathrm{I}_{\mathrm{CHG}}$ | $0.040 \times \mathrm{I}_{\mathrm{CHG}}$ |  |
| $\mathrm{I}_{\text {B(AS(TERM) }}$ | Current for external termination-setting resistor | $\mathrm{V}_{\mathrm{IN}}>\mathrm{V}_{\text {UVLO }}$ and $\mathrm{V}_{\mathrm{IN}}>\mathrm{V}_{\text {BAT }}+\mathrm{V}_{\text {IN(OT) }}$ |  | 72 | 75 | 78 | $\mu \mathrm{A}$ |
| $\mathrm{I}_{\text {TERM }}$ | Termination current threshold (externally set) (BQ24074) |  |  | $\mathrm{K}_{\text {ITERM }}$ * $\mathrm{R}_{\text {ITERM }} / \mathrm{R}_{\text {ISET }}$ |  |  | A |
| $\mathrm{K}_{\text {ITERM }}$ | K Factor for termination detection threshold (externally set) (BQ24074) | USB500 or ISET mode(EN1, EN2) $\neq$ (LO, LO) $\mathrm{CE}=\mathrm{LO}, \mathrm{V}_{\text {BAT }}>\mathrm{V}_{\text {RCH }} 1+\mathrm{I}_{\text {MAXCH }}, \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V}$, DPPM loop and thermal loop not active |  | 0.0225 | 0.0300 | 0.0375 | A |
|  |  | USB100 mode (EN1, EN2) = (LO, LO), $\mathrm{CE}=\mathrm{LO}, \mathrm{V}_{\text {BAT }}>\mathrm{V}_{\text {RCH }} 1+\mathrm{I}_{\text {MAXCH }}, \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V}$, DPPM loop and thermal loop not active |  | 0.008 | 0.0100 | 0.012 |  |
| $\mathrm{I}_{\text {D(ILITERM) }}$ | Deglitch time, termination detected |  |  |  | 25 |  | ms |
| $\mathrm{V}_{\text {RCH }}$ | Recharge detection threshold | $\mathrm{V}_{\mathrm{IN}}>\mathrm{V}_{\text {UVLO }}$ and $\mathrm{V}_{\mathrm{IN}}>\mathrm{V}_{\text {BAT }}+\mathrm{V}_{\text {IN(OT) }}$ |  | $\begin{gathered} \mathrm{V}_{\text {BAT(REG) }} \\ 140 \mathrm{mV} \end{gathered}$ | $\begin{gathered} \mathrm{V}_{\text {BAT(REG) }} \\ 100 \mathrm{mV} \end{gathered}$ | $\begin{gathered} \mathrm{V}_{\text {BAT(REG) }} \\ 60 \mathrm{mV} \end{gathered}$ | V |
| $\mathrm{I}_{\text {D(IL(RCH) }}$ | Deglitch time, recharge threshold detected |  |  |  | 62.5 |  | ms |
| $\mathrm{I}_{\text {D(IL(NO-IN) }}$ | Delay time, input power loss to OUT LDO turn-off | $\mathrm{V}_{\text {BAT }}=3.6 \mathrm{~V}$. Time measured from $\mathrm{V}_{\mathrm{IN}} 5 \mathrm{~V} \rightarrow 3 \mathrm{~V} 1 \mu \mathrm{~s}$ fall-time |  |  | 20 |  | ms |
| $\mathrm{I}_{\text {BAT(SET) }}$ | Sink current for battery detection | $\mathrm{V}_{\text {BAT }}=2.5 \mathrm{~V}$ |  | 5 | 7.5 | 10 | mA |
| $\mathrm{I}_{\text {ISET }}$ | Battery detection timer | BAT high or low |  |  | 250 |  | ms |
| BATTERY CHARGING TIMERS |  |  |  |  |  |  |  |
| $\mathrm{I}_{\text {PRECHG }}$ | Pre-charge safety timer value | TMR = floating |  | 1440 | 1800 | 2160 | s |
| $\mathrm{I}_{\text {MAXCHG }}$ | Charge safety timer value | TMR = floating |  | 14400 | 18000 | 21600 | s |
| $\mathrm{I}_{\text {PRECHG }}$ | Pre-charge safety timer value | $18 \mathrm{k} \Omega<\mathrm{R}_{\text {TMR }}<72 \mathrm{k} \Omega$ |  |  | $R_{\text {TMR }} \times K_{\text {TMR }}$ |  | s |
| $\mathrm{I}_{\text {MAXCHG }}$ | Charge safety timer value | $18 \mathrm{k} \Omega<\mathrm{R}_{\text {TMR }}<72 \mathrm{k} \Omega$ |  | $10 \times R_{\text {TMR }} \times K_{\text {TMR }}$ |  |  | s |
| $\mathrm{K}_{\text {TMR }}$ | Timer factor |  |  | 36 | 48 | 60 | $\mathrm{s} / \mathrm{k} \Omega$ |
| BATTERY-PACK NTC MONITOR ${ }^{(1)}$ |  |  |  |  |  |  |  |
| $\mathrm{I}_{\text {NTC }}$ | NTC bias current | $\mathrm{V}_{\mathrm{IN}}>\mathrm{UVLO}$ and $\mathrm{V}_{\mathrm{IN}}>\mathrm{V}_{\text {BAT }}+\mathrm{V}_{\text {IN(OT) }}$ |  | 72 | 75 | 78 | $\mu \mathrm{A}$ |
| $\mathrm{V}_{\text {HOT }}$ | High temperature trip point | Battery charging, $\mathrm{V}_{\text {TS }}$ Falling |  | 270 | 300 | 330 | mV |
| $\mathrm{V}_{\text {HYS(HOT) }}$ | Hysteresis on high trip point | Battery charging, $\mathrm{V}_{\text {TS }}$ Rising from $\mathrm{V}_{\text {HOT }}$ |  |  | 30 |  | mV |
| $\mathrm{V}_{\text {COLD }}$ | Low temperature trip point | Battery charging, $\mathrm{V}_{\text {TS }}$ Rising |  | 2000 | 2100 | 2200 | mV |
| $\mathrm{V}_{\text {HYS(COLD) }}$ | Hysteresis on low trip point | Battery charging, $\mathrm{V}_{\text {TS }}$ Falling from $\mathrm{V}_{\text {COLD }}$ |  |  | 300 |  | mV |
| $\mathrm{I}_{\text {D(IL(TS) }}$ | Deglitch time, pack temperature fault detection | TS fault detected to charger disable |  |  | 50 |  | ms |
| $\mathrm{V}_{\text {D(IL(TS) }}$ | TS function disable threshold (BQ24072, BQ24073) | TS unconnected |  |  | $\mathrm{V}_{\mathrm{IN}}-200 \mathrm{mV}$ |  | V |
| THERMAL REGULATION |  |  |  |  |  |  |  |
| $\mathrm{T}_{\text {J(RED) }}$ | Temperature regulation limit |  |  |  | 125 |  | ${ }^{\circ} \mathrm{C}$ |
| $\mathrm{T}_{\text {J(OFF) }}$ | Thermal shutdown temperature | $\mathrm{T}_{\mathrm{J}}$ Rising |  |  | 155 |  | ${ }^{\circ} \mathrm{C}$ |
| $\mathrm{T}_{\text {J(OFF-HYS) }}$ | Thermal shutdown hysteresis |  |  |  | 20 |  | ${ }^{\circ} \mathrm{C}$ |# 8.5 Electrical Characteristics (continued) 

Over junction temperature range $\left(0^{\circ} \leq T_{J} \leq 125^{\circ} \mathrm{C}\right)$ and the recommended supply voltage range (unless otherwise noted)

| PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| LOGIC LEVELS ON EN1, EN2, CE, SYSOFF, TD |  |  |  |  |  |  |
| $V_{I L}$ | Logic LOW input voltage |  | 0 |  | 0.4 | V |
| $V_{A 1}$ | Logic HIGH input voltage |  | 1.4 |  | 6 | V |
| $I_{I L}$ | Input sink current | $V_{I L}=0 \mathrm{~V}$ |  |  | 1 | $\mu \mathrm{A}$ |
| $I_{A 1}$ | Input source current | $V_{A 1}=1.4 \mathrm{~V}$ |  |  | 10 | $\mu \mathrm{A}$ |
| LOGIC LEVELS ON PGOOD, CHG |  |  |  |  |  |  |
| $V_{O L}$ | Output LOW voltage | $I_{0 \text { INK }}=5 \mathrm{~mA}$ |  |  | 0.4 | V |

(1) These numbers set trip points of $0^{\circ} \mathrm{C}$ and $50^{\circ} \mathrm{C}$ while charging, with $3^{\circ} \mathrm{C}$ hysteresis on the trip points, with a Vishay Type 2 curve NTC with an R25 of $10 \mathrm{k} \Omega$.

### 8.6 Typical Characteristics

$V_{I N}=6 \mathrm{~V}, \mathrm{EN} 1=1, \mathrm{EN} 2=0$, BQ24073 application circuit, $\mathrm{T}_{\mathrm{A}}=25^{\circ} \mathrm{C}$, unless otherwise noted.
![img-4.jpeg](img-4.jpeg)

Figure 8-1. Thermal Regulation
![img-5.jpeg](img-5.jpeg)

Figure 8-3. Dropout Voltage vs Temperature No Input Supply
![img-6.jpeg](img-6.jpeg)

Figure 8-2. Dropout Voltage vs Temperature
![img-7.jpeg](img-7.jpeg)

Figure 8-4. BQ24072 Output Regulation Voltage vs Battery Voltage# 8.6 Typical Characteristics (continued) 

$V_{I N}=6 \mathrm{~V}, \mathrm{EN} 1=1, \mathrm{EN} 2=0, B Q 24073$ application circuit, $T_{A}=25^{\circ} \mathrm{C}$, unless otherwise noted.
![img-8.jpeg](img-8.jpeg)

Figure 8-5. BQ24072 Output Regulation Voltage vs Temperature
![img-9.jpeg](img-9.jpeg)

Figure 8-7. BQ24075, BQ24079 Output Regulation Voltage vs Temperature
![img-10.jpeg](img-10.jpeg)

Figure 8-9. BQ24072/ 73/ 75/ 79 Overvoltage Protection Threshold vs Temperature
![img-11.jpeg](img-11.jpeg)

Figure 8-6. BQ24073/ 74 Output Regulation Voltage vs Temperature
![img-12.jpeg](img-12.jpeg)

Figure 8-8. BAT Regulation Voltage vs Temperature
![img-13.jpeg](img-13.jpeg)

Figure 8-10. BQ24074 Overvoltage Protection Threshold vs Temperature# 8.6 Typical Characteristics (continued) 

$\mathrm{V}_{\mathrm{IN}}=6 \mathrm{~V}, \mathrm{EN} 1=1, \mathrm{EN} 2=0, \mathrm{~BQ} 24073$ application circuit, $\mathrm{T}_{\mathrm{A}}=25^{\circ} \mathrm{C}$, unless otherwise noted.
![img-14.jpeg](img-14.jpeg)

Figure 8-11. BQ24074 Input Current Limit vs Input Voltage
![img-15.jpeg](img-15.jpeg)

Figure 8-13. Fastcharge Current vs Battery Voltage
![img-16.jpeg](img-16.jpeg)

Figure 8-12. Fastcharge Current vs Battery Voltage
![img-17.jpeg](img-17.jpeg)

Figure 8-14. Precharge Current vs Battery Voltage
![img-18.jpeg](img-18.jpeg)

Figure 8-15. Precharge Current vs Battery Voltage# 9 Detailed Description 

### 9.1 Overview

The BQ2407x devices are integrated Li-lon linear chargers and system power path management devices targeted at space-limited portable applications. The device powers the system while simultaneously and independently charging the battery. This feature reduces the number of charge and discharge cycles on the battery, allows for proper charge termination and enables the system to run with a defective or absent battery pack. This feature also allows instant system turn-on even with a totally discharged battery. The input power source for charging the battery and running the system can be an AC adapter or a USB port. The devices feature Dynamic Power Path Management (DPPM), which shares the source current between the system and battery charging, and automatically reduces the charging current if the system load increases. When charging from a USB port, the input dynamic power management ( $\mathrm{V}_{\text {IN-DPM }}$ ) circuit reduces the input current if the input voltage falls below a threshold, thus preventing the USB port from crashing. The power-path architecture also permits the battery to supplement the system current requirements when the adapter cannot deliver the peak system currents.# 9.2 Functional Block Diagram 

![img-19.jpeg](img-19.jpeg)# 9.3 Feature Description 

### 9.3.1 Undervoltage Lockout (UVLO)

The BQ2407X family remains in power down mode when the input voltage at the IN pin is below the undervoltage threshold (UVLO).

During the power down mode the host commands at the control inputs ( $\overline{\mathrm{CE}}, \mathrm{EN} 1$ and EN2) are ignored. The Q1 FET connected between IN and OUT pins is off, and the status outputs $\overline{\mathrm{CHG}}$ and $\overline{\text { PGOOD }}$ are high impedance. The Q2 FET that connects BAT to OUT is ON. (If SYSOFF is high, Q2 is off). During power down mode, the $\mathrm{V}_{\text {OUT(SC2) }}$ circuitry is active and monitors for overload conditions on OUT.

### 9.3.2 Power On

When $\mathrm{V}_{\mathrm{IN}}$ exceeds the UVLO threshold, the BQ2407x powers up. While $\mathrm{V}_{\mathrm{IN}}$ is below $\mathrm{V}_{\mathrm{BAT}}+\mathrm{V}_{\mathrm{IN}(\mathrm{DT})}$, the host commands at the control inputs ( $\overline{\mathrm{CE}}, \mathrm{EN} 1$ and EN2) are ignored. The Q1 FET connected between IN and OUT pins is off, and the status outputs $\overline{\mathrm{CHG}}$ and $\overline{\text { PGOOD }}$ are high impedance. The Q2 FET that connects BAT to OUT is ON. (If SYSOFF is high, Q2 is off). During this mode, the $\mathrm{V}_{\text {OUT(SC2) }}$ circuitry is active and monitors for overload conditions on OUT.
Once $\mathrm{V}_{\mathrm{IN}}$ rises above $\mathrm{V}_{\mathrm{BAT}}+\mathrm{V}_{\mathrm{IN}(\mathrm{DT})}$, PGOOD is driven low to indicate the valid power status and the $\overline{\mathrm{CE}}$, EN1, and EN2 inputs are read. The device enters standby mode if (EN1 = EN2 = HI) or if an input overvoltage condition occurs. In standby mode, Q1 is OFF and Q2 is ON so OUT is connected to the battery input. (If SYSOFF is high, FET Q2 is off). During this mode, the $\mathrm{V}_{\text {OUT(SC2) }}$ circuitry is active and monitors for overload conditions on OUT.
When the input voltage at IN is within the valid range: $\mathrm{V}_{\mathrm{IN}}>$ UVLO AND $\mathrm{V}_{\mathrm{IN}}>\mathrm{V}_{\mathrm{BAT}}+\mathrm{V}_{\mathrm{IN}(\mathrm{DT})}$ AND $\mathrm{V}_{\mathrm{IN}}<\mathrm{V}_{\mathrm{OVP}}$, and the EN1 and EN2 pins indicate that the USB suspend mode is not enabled [(EN1, EN2) \# (HI, HI)] all internal timers and other circuit blocks are activated. The device then checks for short-circuits at the ISET and ILIM pins. If no short conditions exists, the device switches on the input FET Q1 with a 100 mA current limit to checks for a short circuit at OUT. When $\mathrm{V}_{\text {OUT }}$ is above $\mathrm{V}_{\mathrm{O}(\mathrm{SC} 1)}$, the FET Q1 switches to the current limit threshold set by EN1, EN2 and $R_{\text {ILIM }}$ and the device enters into the normal operation. During normal operation, the system is powered by the input source ( Q 1 is regulating), and the device continuously monitors the status of $\overline{\mathrm{CE}}, \mathrm{EN} 1$ and EN2 as well as the input voltage conditions.![img-20.jpeg](img-20.jpeg)

Figure 9-1. Startup Flow Diagram# 9.3.3 Overvoltage Protection (OVP) 

The BQ2407x accepts inputs up to 28 V without damage. Additionally, an overvoltage protection (OVP) circuit is implemented that shuts off the internal LDO and discontinues charging when $\mathrm{V}_{\mathrm{IN}}>\mathrm{V}_{\mathrm{OVP}}$ for a period long than $t_{\text {DGL(OVP) }}$. When in OVP, the system output (OUT) is connected to the battery and $\overline{P G O O D}$ is high impedance. Once the OVP condition is removed, a new power on sequence starts (see Section 9.3.2). The safety timers are reset and a new charge cycle will be indicated by the $\overline{\mathrm{CHG}}$ output.

### 9.3.4 Dynamic Power Path Management

The BQ2407x features an OUT output that powers the external load connected to the battery. This output is active whenever a source is connected to IN or BAT. The following sections discuss the behavior of OUT with a source connected to IN to charge the battery and a battery source only.

### 9.3.4.1 Input Source Connected (ADAPTER or USB)

With a source connected, the dynamic power path management (DPPM) circuitry of the BQ2407x monitors the input current continuously. The OUT output for the BQ24073/ 74/ 75/ 79 is regulated to a fixed voltage ( $\mathrm{V}_{\mathrm{O}(\mathrm{REG})}$ ). For the BQ24072, OUT is regulated to 200 mV above the voltage at BAT. When the BAT voltage falls below 3.2 V , OUT is clamped to 3.4 V . This allows for proper startup of the system load even with a discharged battery. The current into IN is shared between charging the battery and powering the system load at OUT. The BQ2407x has internal selectable current limits of 100 mA (USB100) and 500 mA (USB500) for charging from USB ports, as well as a resistor-programmable input current limit.

The BQ2407x is USB IF compliant for the inrush current testing. The USB specification allows up to $10 \mu \mathrm{~F}$ to be hard started, which establishes $50 \mu \mathrm{C}$ as the maximum inrush charge value when exceeding 100 mA . The input current limit for the BQ2407x prevents the input current from exceeding this limit, even with system capacitances greater than $10 \mu \mathrm{~F}$. The input capacitance to the device must be selected small enough to prevent a violation $(<10 \mu \mathrm{~F})$, as this current is not limited. Figure 9-2 demonstrates the start-up of the BQ2407x and compares it to the USB-IF specification.
![img-21.jpeg](img-21.jpeg)

Figure 9-2. USB-IF Inrush Current Test
The input current limit selection is controlled by the state of the EN1 and EN2 pins as shown in the EN1/EN2 Settings table in Section 7. When using the resistor-programmable current limit, the input current limit is set by the value of the resistor connected from the ILIM pin to VSS, and is given by the equation:

$$
\mathrm{I}_{\mathrm{IN}-\mathrm{MAX}}=\mathrm{K}_{\mathrm{ILIM}} / \mathrm{R}_{\mathrm{ILIM}}
$$

The input current limit is adjustable up to 1.5 A . The valid resistor range is $1.1 \mathrm{k} \Omega$ to $8 \mathrm{k} \Omega$.When the IN source is connected, priority is given to the system load. The DPPM and Battery Supplement modes are used to maintain the system load. Figure 9-4 and Figure 9-5 illustrate examples of the DPPM and supplement modes. These modes are explained in detail in the following sections.

# 9.3.4.1.1 Input DPM Mode ( $\mathrm{V}_{\text {IN }}$-DPM) 

The BQ2407x utilizes the $\mathrm{V}_{\mathrm{IN}}$-DPM mode for operation from current-limited USB ports. When EN1 and EN2 are configured for USB100 (EN2=0, EN1=0) or USB500 (EN2=0, EN1=1) modes, the input voltage is monitored. If $\mathrm{V}_{\mathrm{IN}}$ falls to $\mathrm{V}_{\text {IN-DPM }}$, the input current limit is reduced to prevent the input voltage from falling further. This prevents the BQ2407x from crashing poorly designed or incorrectly configured USB sources. Figure 9-3 shows the $\mathrm{V}_{\mathrm{IN}}$-DPM behavior to a current limited source. In this figure, the input source has a $400-\mathrm{mA}$ current limit and the device is in USB500 mode (EN1=1, EN2=0).
![img-22.jpeg](img-22.jpeg)

Figure 9-3. $\mathrm{V}_{\text {IN }}$-DPM Waveform

### 9.3.4.1.2 DPPM Mode

When the sum of the charging and system load currents exceeds the maximum input current (programmed with EN1, EN2, and ILIM pins), the voltage at OUT decreases. Once the voltage on the OUT pin falls to $\mathrm{V}_{\text {DPPM }}$, the BQ2407x enters DPPM mode. In this mode, the charging current is reduced as the OUT current increases in order to maintain the system output. Battery termination is disabled while in DPPM mode.

### 9.3.4.1.3 Battery Supplement Mode

While in DPPM mode, if the charging current falls to zero and the system load current increases beyond the programmed input current limit, the voltage at OUT reduces further. When the OUT voltage drops below the $\mathrm{V}_{\text {BSUP1 }}$ threshold, the battery supplements the system load. The battery stops supplementing the system load when the voltage at OUT rises above the $\mathrm{V}_{\text {BSUP2 }}$ threshold.
During supplement mode, the battery supplement current is not regulated (BAT-FET is fully on), however there is a short circuit protection circuit built in. Figure 10-6 demonstrates supplement mode. If during battery supplement mode, the voltage at OUT drops $\mathrm{V}_{\mathrm{O}(\mathrm{SC} 2)}$ below the BAT voltage, the OUT output is turned off if the overload exists after $\mathrm{t}_{\mathrm{DGL}(\mathrm{SC} 2)}$. The short circuit recovery timer then starts counting. After $\mathrm{t}_{\mathrm{REC}(\mathrm{SC} 2)}$, OUT turns on and attempts to restart. If the short circuit remains, OUT is turned off and the counter restarts. Battery termination is disabled while in supplement mode.![img-23.jpeg](img-23.jpeg)

Figure 9-4. BQ24072 DPPM and Battery Supplement Modes ( $\mathrm{V}_{\text {OREG }}=\mathrm{V}_{\mathrm{BAT}}+225 \mathrm{mV}, \mathrm{V}_{\mathrm{BAT}}=3.6 \mathrm{~V}$ )![img-24.jpeg](img-24.jpeg)

Figure 9-5. BQ24073 DPPM and Battery Supplement Modes ( $\mathrm{V}_{\text {OREG }}=4.4 \mathrm{~V}, \mathrm{~V}_{\text {BAT }}=3.6 \mathrm{~V}$ )

# 9.3.4.2 Input Source Not Connected 

When no source is connected to the IN input, OUT is powered strictly from the battery. During this mode the current into OUT is not regulated, similar to Battery Supplement Mode, however the short circuit circuitry is active. If the OUT voltage falls below the BAT voltage by 250 mV for longer than $t_{\text {DGL(SC2) }}$, OUT is turned off. The short circuit recovery timer then starts counting. After $t_{\text {REC(SC2) }}$, OUT turns on and attempts to restart. If the short circuit remains, OUT is turned off and the counter restarts. This ON/OFF cycle continues until the overload condition is removed.

### 9.3.5 Battery Charging

Set $\overline{\mathrm{CE}}$ low to initiate battery charging. First, the device checks for a short-circuit on the BAT pin by sourcing $\mathrm{I}_{\text {BAT(SC) }}$ to the battery and monitoring the voltage. When the BAT voltage exceeds $\mathrm{V}_{\text {BAT(SC) }}$, the battery charging continues. The battery is charged in three phases: conditioning pre-charge, constant current fast charge (current regulation) and a constant voltage tapering (voltage regulation). In all charge phases, an internal control loop monitors the IC junction temperature and reduces the charge current if an internal temperature threshold is exceeded.

Figure 9-6 illustrates a normal Li-lon charge cycle using the BQ2407x:![img-25.jpeg](img-25.jpeg)

Figure 9-6. Typical Charge Cycle
In the pre-charge phase, the battery is charged at with the pre-charge current ( $\mathrm{I}_{\text {PRECHG }}$ ). Once the battery voltage crosses the $\mathrm{V}_{\mathrm{LOWV}}$ threshold, the battery is charged with the fast-charge current ( $\mathrm{I}_{\mathrm{CHG}}$ ). As the battery voltage reaches $\mathrm{V}_{\mathrm{BAT}(\mathrm{REG})}$, the battery is held at a constant voltage of $\mathrm{V}_{\mathrm{BAT}(\mathrm{REG})}$ and the charge current tapers off as the battery approaches full charge. When the battery current reaches $\mathrm{I}_{\text {TERM }}$, the $\overline{\mathrm{CHG}}$ pin indicates charging done by going high-impedance.

Note that termination detection is disabled whenever the charge rate is reduced because of the actions of the thermal loop, the DPPM loop or the $\mathrm{V}_{\text {IN-DPM }}$ loop.
The value of the fast-charge current is set by the resistor connected from the ISET pin to VSS, and is given by the equation:

$$
\mathrm{I}_{\mathrm{CHG}}=\mathrm{K}_{\mathrm{ISET}} / \mathrm{R}_{\mathrm{ISET}}
$$

The charge current limit is adjustable up to 1.5 A . The valid resistor range is $590 \Omega$ to $8.9 \mathrm{k} \Omega$. If $\mathrm{I}_{\mathrm{CHG}}$ is programmed as greater than the input current limit, the battery will not charge at the rate of $\mathrm{I}_{\mathrm{CHG}}$, but at the slower rate of $\mathrm{I}_{\mathrm{IN}(\mathrm{MAX})}$ (minus the load current on the OUT pin, if any). In this case, the charger timers will be proportionately slowed down.

# 9.3.5.1 Charge Current Translator 

When the charger is enabled, internal circuits generate a current proportional to the charge current at the ISET input. The current out of ISET is $1 / 400( \pm 10 \%)$ of the charge current. This current, when applied to the external charge current programming resistor, $\mathrm{R}_{\text {ISET }}$, generates an analog voltage that can be monitored by an external host to calculate the current sourced from BAT.

$$
\mathrm{V}_{\text {ISET }}=\mathrm{I}_{\text {CHARGE }} / 400 \times \mathrm{R}_{\text {ISET }}
$$![img-26.jpeg](img-26.jpeg)

Figure 9-7. Battery Charging Flow Diagram# 9.3.5.2 Adjustable Termination Threshold (ITERM Input, BQ24074) 

The termination current threshold in the BQ24074 is user-programmable. Set the termination current by connecting a resistor from ITERM to VSS. For USB100 mode (EN1 = EN2 = Low), the termination current value is calculated as:

$$
\mathrm{I}_{\text {TERM }}=0.01 \times \mathrm{R}_{\text {ITERM }} / \mathrm{R}_{\text {ISET }}
$$

In the other input current limit modes (EN1 $\neq$ EN2), the termination current value is calculated as:

$$
\mathrm{I}_{\text {TERM }}=0.03 \times \mathrm{R}_{\text {ITERM }} / \mathrm{R}_{\text {ISET }}
$$

The termination current is programmable up to $50 \%$ of the fastcharge current. The $R_{\text {ITERM }}$ resistor must be less than $15 \mathrm{k} \Omega$. Leave ITERM unconnected to select the default internally set termination current.

### 9.3.5.3 Termination Disable (TD Input, BQ24072, BQ24073)

The BQ24072 and BQ24073 contain a TD input that allows termination to be enabled/ disabled. Connect TD to a logic high to disable charge termination. When termination is disabled, the device goes through the pre-charge, fast-charge and CV phases, then remains in the CV phase. During the CV phase, the charger maintains the output voltage at BAT equal to $\mathrm{V}_{\mathrm{BAT}(\mathrm{REG})}$, and charging current does not terminate. The charge current is set by $\mathrm{I}_{\mathrm{CHG}}$ or $\mathrm{I}_{\mathrm{IN}} \max$, whichever is less. Battery detection is not performed. The $\overline{\mathrm{CHG}}$ output is high impedance once the current falls below $\mathrm{I}_{\text {TERM }}$ and does not go low until the input power or $\overline{\mathrm{CE}}$ are toggled. When termination is disabled, the pre-charge and fast-charge safety timers are also disabled. Battery pack temperature sensing (TS pin functionality) is disabled if the TD pin is high and the TS pin is unconnected or pulled up to $\mathrm{V}_{\mathrm{IN}}$.

### 9.3.5.4 Battery Detection and Recharge

The BQ2407x automatically detects if a battery is connected or removed. Once a charge cycle is complete, the battery voltage is monitored. When the battery voltage falls below $\mathrm{V}_{\mathrm{RCH}}$, the battery detection routine is run. During battery detection, current $\left(\mathrm{I}_{\mathrm{BAT}(\mathrm{DET})}\right)$ is pulled from the battery for a duration $\mathrm{t}_{\mathrm{DET}}$ to see if the voltage on BAT falls below $\mathrm{V}_{\text {LOWV }}$. If not, charging begins. If it does, then it indicates that the battery is missing or the protector is open. Next, the precharge current is applied for $\mathrm{t}_{\mathrm{DET}}$ to close the protector if possible. If $\mathrm{V}_{\mathrm{BAT}}<\mathrm{V}_{\mathrm{RCH}}$, then the protector closed and charging is initiated. If $\mathrm{V}_{\mathrm{BAT}}>\mathrm{V}_{\mathrm{RCH}}$, then the battery is determined to be missing and the detection routine continues.

### 9.3.5.5 Battery Disconnect (SYSOFF Input, BQ24075, BQ24079)

The BQ24075 and BQ24079 feature a SYSOFF input that allows the user to turn the FET Q2 off and disconnect the battery from the OUT pin. This is useful for disconnecting the system load from the battery, factory programming where the battery is not installed or for host side impedance track fuel gauging, such as bq27500, where the battery open circuit voltage level must be detected before the battery charges or discharges. The /CHG output remains low when SYSOFF is high. Connect SYSOFF to VSS, to turn Q2 on for normal operation. SYSOFF is internally pulled to VBAT through $\sim 5 \mathrm{M} \Omega$ resistor.

### 9.3.5.6 Dynamic Charge Timers (TMR Input)

The BQ2407x devices contain internal safety timers for the pre-charge and fast-charge phases to prevent potential damage to the battery and the system. The timers begin at the start of the respective charge cycles. The timer values are programmed by connecting a resistor from TMR to VSS. The resistor value is calculated using the following equation:

$$
\begin{aligned}
& \mathrm{t}_{\text {PRECHG }}=\mathrm{K}_{\text {TMR }} \times \mathrm{R}_{\text {TMR }} \\
& \mathrm{t}_{\text {MAXCHG }}=10 \times \mathrm{K}_{\text {TMR }} \times \mathrm{R}_{\text {TMR }}
\end{aligned}
$$

Leave TMR unconnected to select the internal default timers. Disable the timers by connecting TMR to VSS.
Reset the timers by toggling the CE pin, or by toggling EN1, EN2 pin to put the device in and out of USB suspend mode (EN1 = HI, EN2 = HI).Note that timers are suspended when the device is in thermal shutdown, and the timers are slowed proportionally to the charge current when the device enters thermal regulation. For the BQ24072 and BQ24073, the timers are disabled when TD is connected to a high logic level.
During the fast charge phase, several events increase the timer durations.

- The system load current activates the DPPM loop which reduces the available charging current
- The input current is reduced because the input voltage has fallen to $\mathrm{V}_{\text {IN-DPM }}$
- The device has entered thermal regulation because the IC junction temperature has exceeded $\mathrm{T}_{\mathrm{J}(\text { REG })}$

During each of these events, the internal timers are slowed down proportionately to the reduction in charging current. For example, if the charging current is reduced by half for two minutes, the timer clock is reduced to half the frequency and the counter counts half as fast resulting in only one minute of "counting" time.
If the pre charge timer expires before the battery voltage reaches $\mathrm{V}_{\text {LOWV }}$, the BQ2407x indicates a fault condition. Additionally, if the battery current does not fall to $\mathrm{I}_{\text {TERM }}$ before the fast charge timer expires, a fault is indicated. The $\overline{\mathrm{CHG}}$ output flashes at approximately 2 Hz to indicate a fault condition. The fault condition is cleared by toggling $\overline{\mathrm{CE}}$ or the input power, entering/ exiting USB suspend mode, or an OVP event.

# 9.3.5.7 Status Indicators ( $\overline{P G O O D}, \overline{C H G}$ ) 

The BQ2407x contains two open-drain outputs that signal its status. The $\overline{P G O O D}$ output signals when a valid input source is connected. $\overline{P G O O D}$ is low when $\left(\mathrm{V}_{\mathrm{BAT}}+\mathrm{V}_{\mathrm{IN}(\mathrm{DT})}\right)<\mathrm{V}_{\mathrm{IN}}<\mathrm{V}_{\text {OVP }}$. When the input voltage is outside of this range, $\overline{P G O O D}$ is high impedance.

The charge cycle after power-up, CE going low, or exiting OVP is indicated with the $\overline{\mathrm{CHG}}$ pin on (low - LED on), whereas all refresh (subsequent) charges will result in the $\overline{\mathrm{CHG}}$ pin off (open - LED off). In addition, the $\overline{\mathrm{CHG}}$ signals timer faults by flashing at approximately 2 Hz .

Table 9-1. $\overline{P G O O D}$ Status Indicator

| INPUT STATE | PGOOD OUTPUT |
| :--: | :--: |
| $\mathrm{V}_{\text {IN }}<\mathrm{V}_{\text {UVLO }}$ | High-impedance |
| $\mathrm{V}_{\text {UVLO }}<\mathrm{V}_{\text {IN }}<\mathrm{V}_{\text {BAT }}+\mathrm{V}_{\text {IN(DT) }}$ | High-impedance |
| $\mathrm{V}_{\text {BAT }}+\mathrm{V}_{\text {IN(DT) }}<\mathrm{V}_{\text {IN }}<\mathrm{V}_{\text {OVP }}$ | Low |
| $\mathrm{V}_{\text {IN }}>\mathrm{V}_{\text {OVP }}$ | High-impedance |

Table 9-2. $\overline{\text { CHG }}$ Status Indicator

| CHARGE STATE | CHG OUTPUT |
| :--: | :--: |
| Charging | Low (for first charge cycle) |
| Charging suspended by thermal loop |  |
| Safety timers expired | Flashing at 2 Hz |
| Charging done | High-impedance |
| Recharging after termination |  |
| IC disabled or no valid input power |  |
| Battery absent |  |

### 9.3.5.8 Thermal Regulation and Thermal Shutdown

The BQ2407x contain a thermal regulation loop that monitors the die temperature. If the temperature exceeds $\mathrm{T}_{\mathrm{J}(\text { REG })}$, the device automatically reduces the charging current to prevent the die temperature from increasing further. In some cases, the die temperature continues to rise despite the operation of the thermal loop, particularly under high VIN and heavy OUT system load conditions. Under these conditions, if the die temperature increases to $\mathrm{T}_{\mathrm{J}(\text { OFF })}$, the input FET Q1 is turned OFF. FET Q2 is turned ON to ensure that the battery still powers the load on OUT. Once the device die temperature cools by $\mathrm{T}_{\mathrm{J}(\text { OFF-HYS)}}$, the input FET Q1 is turned on and the device returns to thermal regulation. Continuous overtemperature conditions result in a "hiccup" mode. During thermal regulation, the safety timers are slowed down proportionately to the reduction in current limit.Note that this feature monitors the die temperature of the BQ2407x. This is not synonymous with ambient temperature. Self heating exists due to the power dissipated in the IC because of the linear nature of the battery charging algorithm and the LDO associated with OUT. A modified charge cycle with the thermal loop active is shown in Figure 9-8. Battery termination is disabled during thermal regulation.
![img-27.jpeg](img-27.jpeg)

Figure 9-8. Charge Cycle Modified by Thermal Loop

# 9.3.6 Battery Pack Temperature Monitoring 

The BQ2407x features an external battery pack temperature monitoring input. The TS input connects to the NTC thermistor in the battery pack to monitor battery temperature and prevent dangerous over-temperature conditions. During charging, $\mathrm{I}_{\mathrm{NTC}}$ is sourced to TS and the voltage at TS is continuously monitored. If, at any time, the voltage at TS is outside of the operating range ( $\mathrm{V}_{\text {COLD }}$ to $\mathrm{V}_{\text {HOT }}$ ), charging is suspended. The timers maintain their values but suspend counting. When the voltage measured at TS returns to within the operation window, charging is resumed and the timers continue counting. When charging is suspended due to a battery pack temperature fault, the $\overline{\mathrm{CHG}}$ pin remains low and continues to indicate charging.
For the BQ24072 and BQ24073, battery pack temperature sensing is disabled when termination is disabled (TD $=$ High) and the voltage at TS is greater than $\mathrm{V}_{\text {DIS(TS) }}$. For applications that do not require the TS monitoring function, connect a $10-\mathrm{k} \Omega$ resistor from TS to VSS to set the TS voltage at a valid level and maintain charging.The allowed temperature range for 103AT-2 type thermistor is $0^{\circ} \mathrm{C}$ to $50^{\circ} \mathrm{C}$. However, the user may increase the range by adding two external resistors. See Figure 9-9 for the circuit details. The values for Rs and Rp are calculated using the following equations:

$$
\begin{aligned}
& \mathrm{Rs}=\frac{-\left(\mathrm{R}_{\mathrm{TH}}+\mathrm{R}_{\mathrm{TC}}\right) \pm \sqrt{\left(\mathrm{R}_{\mathrm{TH}}+\mathrm{R}_{\mathrm{TC}}\right)^{2}-4\left\{\mathrm{R}_{\mathrm{TH}} \times \mathrm{R}_{\mathrm{TC}}+\frac{\mathrm{V}_{\mathrm{H}} \times \mathrm{V}_{\mathrm{C}}}{\left(\mathrm{~V}_{\mathrm{H}}-\mathrm{V}_{\mathrm{C}}\right) \times \mathrm{I}_{\mathrm{TS}}} \times\left(\mathrm{R}_{\mathrm{TC}}-\mathrm{R}_{\mathrm{TH}}\right)\right\}}\right\}}{2} \\
& \mathrm{Rp}=\frac{\mathrm{V}_{\mathrm{H}} \times\left(\mathrm{R}_{\mathrm{TH}}+\mathrm{R}_{\mathrm{S}}\right)}{\mathrm{I}_{\mathrm{TS}} \times\left(\mathrm{R}_{\mathrm{TH}}+\mathrm{R}_{\mathrm{S}}\right)-\mathrm{V}_{\mathrm{H}}}
\end{aligned}
$$

where

- $\mathrm{R}_{\mathrm{TH}}$ : Thermistor Hot Trip Value found in thermistor data sheet
- $\mathrm{R}_{\mathrm{TC}}$ : Thermistor Cold Trip Value found in thermistor data sheet
- $\mathrm{V}_{\mathrm{H}}$ : IC's Hot Trip Threshold $=0.3 \mathrm{~V}$ nominal
- $\mathrm{V}_{\mathrm{C}}$ : IC's Cold Trip Threshold $=2.1 \mathrm{~V}$ nominal
- $\mathrm{I}_{\text {TS }}$ : IC's Output Current Bias $=75 \mu \mathrm{~A}$ nominal
- NTC Thermsitor Semitec 103AT-4

Rs and Rp 1\% values were chosen closest to calculated values in Table 9-3.
Table 9-3. Calculated Values

| COLD TEMP RESISTANCE AND <br> TRIP THRESHOLD; $\boldsymbol{\Omega}\left({ }^{\circ} \mathbf{C}\right)$ | HOT TEMP RESISTANCE AND <br> TRIP THRESHOLD; $\boldsymbol{\Omega}\left({ }^{\circ} \mathbf{C}\right)$ | EXTERNAL BIAS RESISTOR, <br> $\mathbf{R s}(\boldsymbol{\Omega})$ | EXTERNAL BIAS RESISTOR, <br> $\mathbf{R p}(\boldsymbol{\Omega})$ |
| :--: | :--: | :--: | :--: |
| $28000(-0.6)$ | $4000(51)$ | 0 | $\infty$ |
| $28480(-1)$ | $3536(55)$ | 487 | 845000 |
| $28480(-1)$ | $3021(60)$ | 1000 | 549000 |
| $33890(-5)$ | $4026(51)$ | 76.8 | 158000 |
| $33890(-5)$ | $3536(55)$ | 576 | 150000 |
| $33890(-5)$ | $3021(60)$ | 1100 | 140000 |

RHOT and RCOLD are the thermistor resistance at the desired hot and cold temperatures, respectively. The temperature window cannot be tightened more than using only the thermistor connected to TS, it can only be extended.
![img-28.jpeg](img-28.jpeg)

Figure 9-9. Extended TS Pin Thresholds# 9.4 Device Functional Modes 

### 9.4.1 Sleep Mode

When the input is between UVLO and $\mathrm{V}_{\mathrm{IN}(\mathrm{DT})}$, the device enters sleep mode. After entering sleep mode for $>20$ mS the internal FET connection between the IN and OUT pin is disabled and pulling the input to ground will not discharge the battery, other than the leakage on the BAT pin. If one has a full $1000-\mathrm{mAHr}$ battery and the leakage is $10 \mu \mathrm{~A}$, then it would take $1000 \mathrm{mAHr} / 10 \mu \mathrm{~A}=100000$ hours ( 11.4 years) to discharge the battery. The self-discharge of the battery is typically five times higher than this.

### 9.4.2 Explanation of Deglitch Times and Comparator Hysteresis

## Note

Figure 9-10 to Figure 9-14 are not to scale.
![img-29.jpeg](img-29.jpeg)

Figure 9-10. Power-Up, Power-Down, Power Good Indication
![img-30.jpeg](img-30.jpeg)

Figure 9-11. Precharge to Fast-Charge, Fast- to Pre-Charge Transition - $\mathbf{t}_{\text {DGL1(LOWV) }}$, $\mathbf{t}_{\text {DGL2(LOWV) }}$![img-31.jpeg](img-31.jpeg)

Figure 9-12. Recharge $-t_{\text {DGL(RCH) }}$
![img-32.jpeg](img-32.jpeg)

Figure 9-13. OUT Short-Circuit - Supplement Mode
![img-33.jpeg](img-33.jpeg)

Figure 9-14. Battery Pack Temperature Sensing - TS Pin. Battery Temperature Increasing# 10 Application and Implementation 

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

### 10.1 Application Information

The BQ2407x devices power the system while simultaneously and independently charging the battery. The input power source for charging the battery and running the system can be an AC adapter or a USB port. The devices feature dynamic power-path management (DPPM), which shares the source current between the system and battery charging and automatically reduces the charging current if the system load increases. When charging from a USB port, the input dynamic power management (VIN-DPM) circuit reduces the input current limit if the input voltage falls below a threshold, preventing the USB port from crashing. The power-path architecture also permits the battery to supplement the system current requirements when the adapter cannot deliver the peak system currents.

The BQ2407x is configurable to be host controlled for selecting different input current limits based on the input source connected, or a fully stand alone device for applications that do not support multiple types of input sources.

### 10.2 Typical Application

$\mathrm{V}_{\mathrm{IN}}=$ UVLO to $\mathrm{V}_{\mathrm{OVP}}, \mathrm{I}_{\text {FASTCHG }}=800 \mathrm{~mA}, \mathrm{I}_{\mathrm{IN}(\mathrm{MAX})}=1.3 \mathrm{~A}$, Battery Temperature Charge Range $=0^{\circ} \mathrm{C}$ to $50^{\circ} \mathrm{C}$, 6.25 -hour Fastcharge Safety Timer
![img-34.jpeg](img-34.jpeg)

Figure 10-1. Using BQ24072/ BQ24073 in a Host-Controlled Charger Application# 10.2.1 Design Requirements 

- Supply voltage $=5 \mathrm{~V}$
- Fast charge current of approximately 800 mA ; ISET - pin 16
- Input Current Limit =1.3 A; ILIM - pin 12
- Termination Current Threshold = 110 mA; ITERM - pin 15 (BQ24074 only)
- Safety timer duration, Fast-Charge $=6.25$ hours; TMR - pin 14
- TS - Battery Temperature Sense $=10 \mathrm{k} \Omega$ NTC (103AT-2)


### 10.2.2 Detailed Design Procedure

### 10.2.2.1 BQ2407x Charger Design Example

See Figure 10-1 to Figure 10-13 for Schematics of the Design Example.

### 10.2.2.1.1 Termination Disable (TD) (BQ24072, BQ24073 only)

Connect TD high to disable termination. Connect TD low to enable termination.

### 10.2.2.1.2 System ON/OFF (SYSOFF) (BQ24075 or BQ24079 only)

Connect SYSOFF high to disconnect the battery from the system load. Connect SYSOFF low for normal operation

### 10.2.2.2 Calculations

### 10.2.2.2.1 Program the Fast Charge Current (ISET):

$R_{\text {ISET }}=K_{\text {ISET }} / I_{\text {CHG }}$
$\mathrm{K}_{\text {ISET }}=890 \mathrm{~A} \Omega$ from the electrical characteristics table.
$R_{\text {ISET }}=890 \mathrm{~A} \Omega / 0.8 \mathrm{~A}=1.1125 \mathrm{k} \Omega$
Select the closest standard value, which for this case is $1.13 \mathrm{k} \Omega$. Connect this resistor between ISET (pin 16) and $\mathrm{V}_{\mathrm{SS}}$.

### 10.2.2.2.2 Program the Input Current Limit (ILIM)

$R_{\text {ILIM }}=K_{\text {ILIM }} / I_{\text {I_MAX }}$
$\mathrm{K}_{\text {ILIM }}=1550 \mathrm{~A} \Omega$ from the electrical characteristics table.
$R_{\text {ISET }}=1550 \mathrm{~A} \Omega / 1.3 \mathrm{~A}=1.192 \mathrm{k} \Omega$
Select the closest standard value, which for this case is $1.18 \mathrm{k} \Omega$. Connect this resistor between ILIM (pin 12) and $\mathrm{V}_{\mathrm{SS}}$.

### 10.2.2.2.3 Program the Termination Current Threshold ( $\mathrm{I}_{\text {TERM }}$ ) (BQ24074 only)

$R_{\text {ITERM }}=I_{\text {TERM }} \times R_{\text {ISET }} / 0.030$
$R_{\text {ISET }}=1.13 \mathrm{k} \Omega$ from the above calculation.
$R_{\text {ITERM }}=110 \mathrm{~mA} \times 1.13 \mathrm{k} \Omega / 0.030=4.143 \mathrm{k} \Omega$
Select the closest standard value, which for this case is $4.12 \mathrm{k} \Omega$. Connect this resistor between ITERM (pin 15) and $\mathrm{V}_{\mathrm{SS}}$. Note that when in USB100 mode (EN1 $=$ EN2 $=\mathrm{V}_{\mathrm{SS}}$ ), the termination threshold is $1 / 3$ of the normal threshold.

### 10.2.2.2.4 Program 6.25-hour Fast-Charge Safety Timer (TMR)

$R_{\text {TMR }}=t_{\text {MAXCHG }} /\left(10 \times K_{\text {TMR }}\right)$
$\mathrm{K}_{\text {TMR }}=48 \mathrm{~s} / \mathrm{k} \Omega$ from the electrical characteristics table.
$R_{\text {TMR }}=(6.25 \mathrm{hr} \times 3600 \mathrm{~s} / \mathrm{hr}) /(10 \times 48 \mathrm{~s} / \mathrm{k} \Omega)=46.8 \mathrm{k} \Omega$
Select the closest standard value, which for this case is $46.4 \mathrm{k} \Omega$. Connect this resistor between TMR (pin 14) and $\mathrm{V}_{\mathrm{SS}}$.# 10.2.2.3 TS Function 

Use a $10-\mathrm{k} \Omega$ NTC thermistor in the battery pack (103AT-2). For applications that do not require the TS monitoring function, connect a $10-\mathrm{k} \Omega$ resistor from TS to VSS to set the TS voltage at a valid level and maintain charging.

### 10.2.2.4 CHG and PGOOD

LED Status: Connect a $1.5-\mathrm{k} \Omega$ resistor in series with a LED between OUT and $\overline{\mathrm{CHG}}$ to indicate charging status. Connect a $1.5-\mathrm{k} \Omega$ resistor in series with a LED between OUT and $\overline{\text { PGOOD }}$ to indicate when a valid input source is connected.

Processor Monitoring Status: Connect a pullup resistor (on the order of $100 \mathrm{k} \Omega$ ) between the power rail of the processor and $\overline{\mathrm{CHG}}$ and $\overline{\text { PGOOD. }}$

### 10.2.2.5 Selecting IN, OUT, and BAT Pin Capacitors

In most applications, all that is needed is a high-frequency decoupling capacitor (ceramic) on the power pin, input, output and battery pins. Using the values shown on the application diagram, is recommended. After evaluation of these voltage signals with real system operational conditions, one can determine if capacitance values can be adjusted toward the minimum recommended values (DC load application) or higher values for fast high amplitude pulsed load applications. Note if designed high input voltage sources (bad adaptors or wrong adaptors), the capacitor needs to be rated appropriately. Ceramic capacitors are tested to $2 x$ their rated values so a $16-\mathrm{V}$ capacitor may be adequate for a $30-\mathrm{V}$ transient (verify tested rating with capacitor manufacturer).# 10.2.3 Application Curves 

![img-35.jpeg](img-35.jpeg)

Figure 10-2. Adapter Plug-In Battery Connected
![img-36.jpeg](img-36.jpeg)

Figure 10-4. Battery Detection Battery Removed
![img-37.jpeg](img-37.jpeg)

Figure 10-6. Entering and Exiting Battery Supplement Mode BQ24074
![img-38.jpeg](img-38.jpeg)

Figure 10-3. Battery Detection Battery Inserted
![img-39.jpeg](img-39.jpeg)

$$
\mathrm{R}_{\mathrm{LOAD}}=20 \Omega \text { to } 9 \Omega
$$

Figure 10-5. Entering and Exiting DPPM Mode
![img-40.jpeg](img-40.jpeg)

$$
\mathrm{R}_{\mathrm{LOAD}}=20 \Omega \text { to } 4.5 \Omega
$$

Figure 10-7. Entering and Exiting Battery Supplement Mode BQ24072![img-41.jpeg](img-41.jpeg)

Figure 10-8. Charger ON/OFF Using CE
![img-42.jpeg](img-42.jpeg)

Figure 10-10. System ON/OFF With Input Connected $\mathrm{V}_{\mathrm{IN}}=6 \mathrm{~V}$ BQ24075, BQ24079
![img-43.jpeg](img-43.jpeg)

Figure 10-9. OVP Fault
![img-44.jpeg](img-44.jpeg)

Figure 10-11. System ON/OFF With Input Not Connected $\mathrm{V}_{\mathrm{IN}}=0 \mathrm{~V}$ BQ24075, BQ24079# 10.3 System Examples 

### 10.3.1 Standalone Charger

$V_{\text {IN }}=$ UVLO to $V_{\text {OVP }}, I_{\text {FASTCHG }}=800 \mathrm{~mA}, I_{\text {IN(MAX) }}=1.3 \mathrm{~A}, I_{\text {TERM }}=110 \mathrm{~mA}$, Battery Temperature Charge Range $=0^{\circ} \mathrm{C}$ to $50^{\circ} \mathrm{C}$, Safety Timers disabled.
![img-45.jpeg](img-45.jpeg)

Figure 10-12. Using BQ24074 in a Standalone Charger Application

### 10.3.2 Disconnecting the Battery From the System

$V_{\text {IN }}=$ UVLO to $V_{\text {OVP }}, I_{\text {FASTCHG }}=800 \mathrm{~mA}, I_{\text {IN(MAX) }}=1.3 \mathrm{~A}$, Battery Temperature Charge Range $=0^{\circ} \mathrm{C}$ to $50^{\circ} \mathrm{C}$, 6.25 hour Fastcharge Safety Timer.
![img-46.jpeg](img-46.jpeg)

Figure 10-13. Using BQ24075 or BQ24079 to Disconnect the Battery From the System# 11 Power Supply Recommendations 

Some adapters implement a half rectifier topology, which causes the adapter output voltage to fall below the battery voltage during part of the cycle. To enable operation with adapters under those conditions, the BQ2407x family keeps the charger on for at least 20 msec (typical) after the input power puts the part in sleep mode. This feature enables use of external adapters using 50 Hz networks. The input must not drop below the UVLO voltage for the charger to work properly. Thus, the battery voltage should be above the UVLO to help prevent the input from dropping out. Additional input capacitance may be needed.# 12 Layout 

### 12.1 Layout Guidelines

- To obtain optimal performance, the decoupling capacitor from IN to GND (thermal pad) and the output filter capacitors from OUT to GND (thermal pad) should be placed as close as possible to the BQ2407x, with short trace runs to both IN, OUT and GND (thermal pad).
- All low-current GND connections should be kept separate from the high-current charge or discharge paths from the battery. Use a single-point ground technique incorporating both the small signal ground path and the power ground path.
- The high current charge paths into IN pin and from the OUT pin must be sized appropriately for the maximum charge current in order to avoid voltage drops in these traces
- The BQ2407x family is packaged in a thermally enhanced MLP package. The package includes a thermal pad to provide an effective thermal contact between the IC and the printed circuit board (PCB); this thermal pad is also the main ground connection for the device. Connect the thermal pad to the PCB ground connection. Full PCB design guidelines for this package are provided in the QFN/SON PCB Attachment Application Note.# 12.2 Layout Example 

![img-47.jpeg](img-47.jpeg)

Figure 12-1. Layout Schematic# 12.3 Thermal Considerations 

The BQ24072/3/4/5 family is packaged in a thermally enhanced MLP package. The package includes a thermal pad to provide an effective thermal contact between the IC and the printed circuit board (PCB). The power pad should be directly connected to the $\mathrm{V}_{\mathrm{SS}}$ pin. Full PCB design guidelines for this package are provided in the QFN/SON PCB Attachment Application Note. The most common measure of package thermal performance is thermal impedance ( $\theta_{\mathrm{JA}}$ ) measured (or modeled) from the chip junction to the air surrounding the package surface (ambient). The mathematical expression for $\theta_{\mathrm{JA}}$ is:

$$
\theta_{\mathrm{JA}}=\left(\mathrm{T}_{\mathrm{J}}-\mathrm{T}\right) / \mathrm{P}
$$

where

- $\mathrm{T}_{\mathrm{J}}=$ chip junction temperature
- $\mathrm{T}=$ ambient temperature
- $\mathrm{P}=$ device power dissipation

Factors that can influence the measurement and calculation of $\theta_{\text {JA }}$ include:

- Whether or not the device is board mounted
- Trace size, composition, thickness, and geometry
- Orientation of the device (horizontal or vertical)
- Volume of the ambient air surrounding the device under test and airflow
- Whether other surfaces are in close proximity to the device being tested

Due to the charge profile of Li-Ion batteries the maximum power dissipation is typically seen at the beginning of the charge cycle when the battery voltage is at its lowest. Typically after fast charge begins the pack voltage increases to $\$ 3.4 \mathrm{~V}$ within the first 2 minutes. The thermal time constant of the assembly typically takes a few minutes to heat up so when doing maximum power dissipation calculations, 3.4 V is a good minimum voltage to use. This is verified, with the system and a fully discharged battery, by plotting temperature on the bottom of the PCB under the IC (pad should have multiple vias), the charge current and the battery voltage as a function of time. The fast charge current will start to taper off if the part goes into thermal regulation.

The device power dissipation, $P$, is a function of the charge rate and the voltage drop across the internal PowerFET. It can be calculated from the following equation when a battery pack is being charged :

$$
P=\left[V_{(I N)}-V_{(O U T)}\right] \times\left[I_{(O U T)}+I_{(B A T)}\right]+\left[V_{(O U T)}-V_{(B A T)}\right] \times I_{(B A T)}
$$

The thermal loop feature reduces the charge current to limit excessive IC junction temperature. It is recommended that the design not run in thermal regulation for typical operating conditions (nominal input voltage and nominal ambient temperatures) and use the feature for non typical situations such as hot environments or higher than normal input source voltage. With that said, the IC will still perform as described, if the thermal loop is always active.# 13 Device and Documentation Support 

### 13.1 Device Support

### 13.1.1 Third-Party Products Disclaimer

TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

### 13.2 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Subscribe to updates to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

### 13.3 Support Resources

TI E2E ${ }^{\text {TM }}$ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

### 13.4 Trademarks

TI E2E ${ }^{\text {TM }}$ is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.

### 13.5 Electrostatic Discharge Caution

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

### 13.6 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

## 14 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.# PACKAGE OPTION ADDENDUM

|  Orderable part number | Status
(1) | Material type
(2) | Package | Pins | Package qty | Carrier | RoHS
(3) | Lead finish/
Ball material
(4) | MSL rating/
Peak reflow
(5) | Op temp ( ${ }^{\circ} \mathrm{C}$ ) | Part marking
(6)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  BQ24072RGTR | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CKP  |
|  BQ24072RGTR.A | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CKP  |
|  BQ24072RGTR.B | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CKP  |
|  BQ24072RGTRG4 | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CKP  |
|  BQ24072RGTRG4.A | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CKP  |
|  BQ24072RGTRG4.B | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CKP  |
|  BQ24072RGTT | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CKP  |
|  BQ24072RGTT.A | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CKP  |
|  BQ24072RGTT.B | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CKP  |
|  BQ24073RGTR | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-1-260C-UNLIM | $-40$ to 85 | CKQ  |
|  BQ24073RGTR.A | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-1-260C-UNLIM | $-40$ to 85 | CKQ  |
|  BQ24073RGTR.B | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-1-260C-UNLIM | $-40$ to 85 | CKQ  |
|  BQ24073RGTRG4 | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-1-260C-UNLIM | $-40$ to 85 | CKQ  |
|  BQ24073RGTRG4.A | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-1-260C-UNLIM | $-40$ to 85 | CKQ  |
|  BQ24073RGTRG4.B | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-1-260C-UNLIM | $-40$ to 85 | CKQ  |
|  BQ24073RGTT | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | Call TI | Nipdau | Level-2-260C-1 YEAR | $-40$ to 85  |
|  BQ24073RGTT.A | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | Call TI | Nipdau | Level-2-260C-1 YEAR | $-40$ to 85  |
|  BQ24073RGTT.B | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | Call TI | Nipdau | Level-2-260C-1 YEAR | $-40$ to 85  |
|  BQ24073RGTTG4 | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | Call TI | Nipdau | Level-2-260C-1 YEAR | $-40$ to 85  |
|  BQ24074RGTR | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | (BZF, NXK)  |
|  BQ24074RGTR.A | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | (BZF, NXK)  |
|  BQ24074RGTR.B | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | (BZF, NXK)  |
|  BQ24074RGTRG4 | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | (BZF, NXK)  |
|  BQ24074RGTT | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | (BZF, NXK)  |
|  BQ24074RGTT.A | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | (BZF, NXK)  |
|  BQ24074RGTT.B | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | (BZF, NXK)  |
|  BQ24075RGTR | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CDU  |
|  BQ24075RGTR.A | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CDU  |
|  BQ24075RGTR.B | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CDU  ||  Orderable part number | Status
(1) | Material type
(2) | Package | Pins | Package qty | Carrier | RoHS
(3) | Lead finish/
Ball material
(4) | MSL rating/
Peak reflow
(5) | Op temp ( ${ }^{\circ} \mathrm{C}$ ) | Part marking
(6)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  BQ24075RGTRG4 | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CDU  |
|  BQ24075RGTRG4.A | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CDU  |
|  BQ24075RGTRG4.B | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CDU  |
|  BQ24075RGTT | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CDU  |
|  BQ24075RGTT.A | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CDU  |
|  BQ24075RGTT.B | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | CDU  |
|  BQ24079RGTR | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | ODI  |
|  BQ24079RGTR.B | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | ODI  |
|  BQ24079RGTRG4 | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | ODI  |
|  BQ24079RGTRG4.B | Active | Production | VQFN (RGT) | 16 | 3000 | LARGE T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | ODI  |
|  BQ24079RGTT | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | ODI  |
|  BQ24079RGTT.B | Active | Production | VQFN (RGT) | 16 | 250 | SMALL T\&R | Yes | NIPDAU | Level-2-260C-1 YEAR | $-40$ to 85 | ODI  |

${ }^{(1)}$ Status: For more details on status, see our product life cycle. ${ }^{(2)}$ Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind. ${ }^{(3)}$ RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition. ${ }^{(4)}$ Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width. ${ }^{(5)}$ MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board. ${ }^{(6)}$ Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "-" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

# OTHER QUALIFIED VERSIONS OF BQ24075 : 

- Automotive : BQ24075-Q1

NOTE: Qualified Version Definitions:

- Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects# TAPE AND REEL INFORMATION 

![img-48.jpeg](img-48.jpeg)

TAPE DIMENSIONS
![img-49.jpeg](img-49.jpeg)

| A0 | Dimension designed to accommodate the component width |
| :-- | :-- |
| B0 | Dimension designed to accommodate the component length |
| K0 | Dimension designed to accommodate the component thickness |
| W | Overall width of the carrier tape |
| P1 | Pitch between successive cavity centers |

QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE
![img-50.jpeg](img-50.jpeg)
*All dimensions are nominal

| Device | Package <br> Type | Package <br> Drawing | Pins | SPQ | Reel <br> Diameter <br> (mm) | Reel <br> Width <br> W1 (mm) | A0 <br> (mm) | B0 <br> (mm) | K0 <br> (mm) | P1 <br> (mm) | W <br> (mm) | Pin1 <br> Quadrant |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| BQ24072RGTR | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24072RGTRG4 | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24072RGTT | VQFN | RGT | 16 | 250 | 180.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24073RGTR | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24073RGTR | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24073RGTRG4 | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24073RGTT | VQFN | RGT | 16 | 250 | 180.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24074RGTR | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24074RGTT | VQFN | RGT | 16 | 250 | 180.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24075RGTR | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24075RGTRG4 | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24075RGTT | VQFN | RGT | 16 | 250 | 180.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24079RGTR | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24079RGTRG4 | VQFN | RGT | 16 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| BQ24079RGTT | VQFN | RGT | 16 | 250 | 180.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |# **PACKAGE MATERIALS INFORMATION**

![img-51.jpeg](img-51.jpeg)

|  *All dimensions are nominal | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  **Device** |  |  |  |  |  |  |   |
|  BQ24072RGTR | VQFN | RGT | 16 | 3000 | 346.0 | 346.0 | 33.0  |
|  BQ24072RGTRG4 | VQFN | RGT | 16 | 3000 | 346.0 | 346.0 | 33.0  |
|  BQ24072RGTT | VQFN | RGT | 16 | 250 | 210.0 | 185.0 | 35.0  |
|  BQ24073RGTR | VQFN | RGT | 16 | 3000 | 367.0 | 367.0 | 35.0  |
|  BQ24073RGTR | VQFN | RGT | 16 | 3000 | 346.0 | 346.0 | 33.0  |
|  BQ24073RGTRG4 | VQFN | RGT | 16 | 3000 | 367.0 | 367.0 | 35.0  |
|  BQ24073RGTT | VQFN | RGT | 16 | 250 | 210.0 | 185.0 | 35.0  |
|  BQ24074RGTR | VQFN | RGT | 16 | 3000 | 346.0 | 346.0 | 33.0  |
|  BQ24074RGTT | VQFN | RGT | 16 | 250 | 210.0 | 185.0 | 35.0  |
|  BQ24075RGTR | VQFN | RGT | 16 | 3000 | 346.0 | 346.0 | 33.0  |
|  BQ24075RGTRG4 | VQFN | RGT | 16 | 3000 | 346.0 | 346.0 | 33.0  |
|  BQ24075RGTT | VQFN | RGT | 16 | 250 | 210.0 | 185.0 | 35.0  |
|  BQ24079RGTR | VQFN | RGT | 16 | 3000 | 346.0 | 346.0 | 33.0  |
|  BQ24079RGTRG4 | VQFN | RGT | 16 | 3000 | 346.0 | 346.0 | 33.0  |
|  BQ24079RGTT | VQFN | RGT | 16 | 250 | 210.0 | 185.0 | 35.0  |![img-52.jpeg](img-52.jpeg)

Images above are just a representation of the package family, actual package may vary. Refer to the product data sheet for package details.![img-53.jpeg](img-53.jpeg)

| SIDE WALL <br> METAL THICKNESS <br> DIM A |  |
| :--: | :--: |
| OPTION 1 | OPTION 2 |
| 0.1 | 0.2 |

![img-54.jpeg](img-54.jpeg)

NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.![img-55.jpeg](img-55.jpeg)

NOTES: (continued)
4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown on this view. It is recommended that vias under paste be filled, plugged or tented.![img-56.jpeg](img-56.jpeg)

SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL
EXPOSED PAD 17:
85\% PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE SCALE:25X

NOTES: (continued)
6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.# IMPORTANT NOTICE AND DISCLAIMER 

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.
These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.
TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.
TI objects to and rejects any additional or different terms you may have proposed.
Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265
Copyright © 2025, Texas Instruments Incorporated