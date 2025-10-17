# TPS63070 2-V to 16-V Buck-Boost Converter With 3.6-A Switch Current 

## 1 Features

- Input Voltage Range: 2.0 V to 16 V
- Output Voltage Range: 2.5 V to 9 V
- Up to 95\% Efficiency
- +/- 1\% dc accuracy in PWM mode
- $+3 \%$ / -1\% dc accuracy in PFM mode
- 2 A Output Current in Buck Mode
- 2 A Output Current in Boost Mode (VIN = 4 V; Vout = 5 V)
- Precise ENABLE input allows
- user defined undervoltage lockout
- exact sequencing
- Automatic Transition Between Step Down and Boost Mode
- Typical Device Quiescent Current: $50 \mu \mathrm{~A}$
- Fixed and Adjustable Output Voltage Options
- Output Discharge Option
- Power Save Mode for Improved Efficiency at Low Output Power
- Forced Fixed Frequency Operation at 2.4 MHz and Synchronization Option
- Power Good Output
- VSEL simply allows output voltage change
- Load Disconnect During Shutdown
- Overtemperature Protection
- Input / Output Overvoltage Protection
- Available in QFN Package

Simplified Schematic
![img-0.jpeg](img-0.jpeg)

## 2 Applications

- Dual Li-lon Applications
- Industrial Metering Equipment
- DSC's and Camcorders
- Notebook Computers
- Ultra Mobile PC's and Mobile Internet Devices
- Personal Medical Products


## 3 Description

The TPS6307x is a high efficiency, low quiescent current buck-boost converter suitable for applications where the input voltage can be higher or lower than the output voltage. Output currents can go as high as 2 A in boost mode and in buck mode. The buck-boost converter is based on a fixed frequency, pulse-widthmodulation (PWM) controller using synchronous rectification to obtain maximum efficiency. At low load currents, the converter enters Power Save Mode to maintain high efficiency over a wide load current range. The converter can be disabled to minimize battery drain. During shutdown, the load is disconnected from the battery. The device is available in a $2.5 \mathrm{~mm} \times 3 \mathrm{~mm}$ QFN package.

Device Information ${ }^{(1)}$

| PART NUMBER | PACKAGE | BODY SIZE (NOM) |
| :-- | :--: | :--: |
| TPS63070 | VQFN | $2.5 \mathrm{~mm} \times 3 \mathrm{~mm}$ |
| TPS630701 | VQFN | $2.5 \mathrm{~mm} \times 3 \mathrm{~mm}$ |
| TPS630702 | VQFN | $2.5 \mathrm{~mm} \times 3 \mathrm{~mm}$ |

(1) For all available packages, see the orderable addendum at the end of the datasheet.

Efficiency vs Output Current; Vo $=5 \mathrm{~V}$
![img-1.jpeg](img-1.jpeg)# Table of Contents 

1 Features ..... 1
2 Applications ..... 1
3 Description ..... 1
4 Revision History ..... 2
5 Device Comparison Table ..... 3
6 Pin Configuration and Functions ..... 3
7 Specifications ..... 4
7.1 Absolute Maximum Ratings ..... 4
7.2 ESD Ratings ..... 4
7.3 Recommended Operating Conditions ..... 4
7.4 Thermal Information ..... 5
7.5 Electrical Characteristics ..... 6
7.6 Typical Characteristics ..... 8
8 Detailed Description ..... 9
8.1 Overview ..... 9
8.2 Functional Block Diagram TPS63070 ..... 9
8.3 Functional Block Diagram TPS630701 ..... 10
8.4 Feature Description ..... 10
8.5 Device Functional Modes ..... 14
9 Application and Implementation ..... 16
9.1 Application Information ..... 16
9.2 Typical Application for adjustable version ..... 16
9.3 Typical Application for Fixed Voltage Version ..... 26
10 Power Supply Recommendations ..... 31
10.1 Thermal Information ..... 31
11 Layout ..... 32
11.1 Layout Guidelines ..... 32
11.2 Layout Example ..... 32
12 Device and Documentation Support ..... 33
12.1 Device Support ..... 33
12.2 Related Links ..... 33
12.3 Receiving Notification of Documentation Updates ..... 33
12.4 Community Resources ..... 33
12.5 Trademarks ..... 33
12.6 Electrostatic Discharge Caution ..... 33
12.7 Glossary ..... 33
13 Mechanical, Packaging, and Orderable Information ..... 34

## 4 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

## Changes from Revision A (August 2016) to Revision B

- Added Various minor editorial updates and corrections ..... 1
- Added TPS630702 Variant ..... 1
- Added TPS630702 Variant with "output discharge=on" option ..... 3
- Added TPS630702 VOUT info ..... 7
- Added TPS630702 VFB info at 3 instances ..... 7
- Added Parameter Name ROD to output discharge resistance row ..... 7
- Added Link to TechNote SLVAE62 ..... 13
- Added more descriptive text for better understanding ..... 15
- Changed Description of Discharge Feature, reflecting TPS630702 ..... 15
- Changed description of output voltage programming to match EC table ..... 17
- Added table of content for application curves ..... 20
- Added TPS630702 Variant ..... 33
Changes from Original (June 2016) to Revision A ..... Page
- Added full Production Data ..... 1# 5 Device Comparison Table 

| Device Number | Features | Output Voltage | Marking |
| :--: | :--: | :--: | :--: |
| TPS63070 | output discharge $=$ off | adjustable | 3070 |
| TPS630701 | output discharge $=$ off | fixed 5 V | 0701 |
| TPS630702 | output discharge $=$ on | adjustable | 0702 |

## 6 Pin Configuration and Functions

![img-2.jpeg](img-2.jpeg)

Pin Functions

| PIN |  | I/O | DESCRIPTION |
| :--: | :--: | :--: | :--: |
| NAME | NO. |  | Enable input. Pull high to enable the device, pull low to disable the device. |
| EN | 14 | I | Voltage feedback of adjustable versions, must be connected to VOUT on fixed output voltage versions |
| FB | 5 | I | Voltage feedback of adjustable versions, must be connected to VOUT on fixed output voltage versions |
| GND | 4 |  | Control / logic ground |
| L1 | 11 | I | Connection for Inductor |
| L2 | 9 | I | Connection for Inductor |
| PS/SYNC | 1 | I | Pull to low for forced PWM, pull high for PWM/PFM (power save) mode. Apply a clock signal to synchronize to an external frequency. |
| PG | 2 | 0 | Open drain power good output |
| PGND | 10 |  | Power ground |
| VIN | 12,13 | I | Supply voltage for power stage |
| VOUT | 7,8 | 0 | Buck-boost converter output |
| VAUX | 3 | 0 | Connection for Capacitor of internal voltage regulator. This pin must not be loaded externally. |
| VSEL | 15 | I | Voltage scaling input. A high level on this pin enables a transistor which pulls pin FB2 to GND. |
| FB2 | 6 | 0 | Voltage scaling output. Connect a resistor from FB to FB2 to change the voltage divider ratio on the feedback pin. A logic high level on VSEL will change the output voltage to a higher value. Leave the pin open or connect to GND if not used. |# 7 Specifications 

### 7.1 Absolute Maximum Ratings

over operating junction temperature range (unless otherwise noted) ${ }^{(1)}$

|  |  | MIN | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: |
| Voltage range | VIN, PS/SYNC, EN, VSEL | $-0.3$ | 20 | V |
|  | L1 | $-0.3$ | 20 | V |
|  | L1 (transient for $t<10 \mathrm{~ns})^{(2)}$ | $-3$ | 25 | V |
|  | L2, PG, VOUT, FB | $-0.3$ | 12 | V |
|  | L2 (transient for $t<10 \mathrm{~ns})^{(2)}$ | $-3$ | 15 | V |
|  | AUX | $-0.3$ | 7 | V |
|  | FB2 | $-0.3$ | 3 | V |
| Operating junction temperature, $T_{j}$ |  | $-40$ | 150 | ${ }^{\circ} \mathrm{C}$ |
| Storage temperature range, $\mathrm{T}_{\text {stg }}$ |  | $-65$ | 150 | ${ }^{\circ} \mathrm{C}$ |

(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) While switching

### 7.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| :--: | :--: | :--: | :--: | :--: |
| $\mathrm{V}_{\text {(ESD) }}$ | Electrostatic discharge | Human body model (HBM), per ANSI/ESDA/JEDEC JS-001, all pins ${ }^{(1)}$ | $\pm 2000$ | V |
|  |  | Charged device model (CDM), per JEDEC specification JESD22-C101, all pins ${ }^{(2)}$ | $\pm 500$ |  |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

### 7.3 Recommended Operating Conditions

over operating junction temperature range (unless otherwise noted)

|  | MIN | NOM | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: |
| Supply voltage at VIN | 2.0 |  | 16 | V |
| Output Voltage | 2.5 |  | 9 | V |
| Effective Inductance | 0.7 | 1.5 | 2.8 | $\mu \mathrm{H}$ |
| Capacitance connected to VIN pin | 4.7 | 10 |  | $\mu \mathrm{F}$ |
| Capacitance connected to VAUX pin |  | 100 |  | nF |
| Total capacitance connected to VOUT pin ${ }^{(1)}$ | 15 | 47 | 470 | $\mu \mathrm{F}$ |
| duty cycle in buck mode over recommended operating conditions | 30 |  |  | \% |
| duty cycle in buck mode over recommended operating conditions but effective output capacitance Cout,eff $\geq 40 \mathrm{uF}$; effective inductance L,eff $=0.7 \mu \mathrm{H}$ to 1.8 uH | 20 |  |  | \% |
| Operating junction temperature range, $T_{J}$ | $-40$ |  | 125 | ${ }^{\circ} \mathrm{C}$ |

(1) Due to the dc bias effect of ceramic capacitors, the effective capacitance is lower than the nominal value when a voltage is applied. This is why the capacitance is specified to allow the selection of the minimal capacitor required with the dc bias effect for this type of capacitor in mind. The capacitance range given above is for the nominal inductance of $1.5 \mu \mathrm{H}$. Please also see the detailed design procedure in the application section about the ratio of inductance and minimum output capacitance.# 7.4 Thermal Information 

| THERMAL METRIC ${ }^{(1)}$ |  | TPS63070x |  |
| :--: | :--: | :--: | :--: |
|  |  | VQFN | UNIT |
|  |  | 13 PINS |  |
| $R_{i \text { i }}$ | Junction-to-ambient thermal resistance | 63 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $R_{i \text { iJ }}$ (top) | Junction-to-case (top) thermal resistance | 42 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $R_{i J B}$ | Junction-to-board thermal resistance | 13 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $\eta_{J T}$ | Junction-to-top characterization parameter | 2.4 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $\eta_{J B}$ | Junction-to-board characterization parameter | 13 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $R_{i J C(b o t)}$ | Junction-to-case (bottom) thermal resistance | n/a | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |

(1) For more information about traditional and new thermal metrics, see the IC Package Thermal Metrics application report, SPRA953.# 7.5 Electrical Characteristics 

over VIN $=2 \mathrm{~V}$ to $16 \mathrm{~V} ; \mathrm{Tj}=-40^{\circ} \mathrm{C}$ to $125^{\circ} \mathrm{C}$; typical values are at $\mathrm{Tj}=25^{\circ} \mathrm{C}$ (unless otherwise noted)

| PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| SUPPLY |  |  |  |  |  |  |
| VIN | Input voltage range | once started; Vout $\geq 3.0 \mathrm{~V}$ | 2.0 |  | 16 | V |
| VIN | Input voltage range | for start-up; Vout $<3.0 \mathrm{~V}$ | 3.0 |  | 16 | V |
| IOUT | Output current | during operation with either VIN $\geq 4.5 \mathrm{~V}$ or VOUT $\geq 4.5 \mathrm{~V}$ and the boost factor (VOUT/VIN) $\leq 1$ |  |  | 2 | A |
| $\mathrm{I}_{\mathrm{Q}}$ | Quiescent current | into VIN; IOUT $=0 \mathrm{~mA}$, $\mathrm{V}_{\mathrm{EN}}=\mathrm{VIN}=6 \mathrm{~V}, \mathrm{PFM}$ VOUT $=5 \mathrm{~V} ; \mathrm{Tj}=-40^{\circ} \mathrm{C}$ to $85^{\circ} \mathrm{C}$ | 54 |  | 103 | $\mu \mathrm{A}$ |
| $\mathrm{I}_{\mathrm{Q}}$ | Quiescent current | into VIN; IOUT $=0 \mathrm{~mA}$, $\mathrm{V}_{\mathrm{EN}}=\mathrm{VIN}=6 \mathrm{~V}, \mathrm{PFM}$ VOUT $=5 \mathrm{~V} ; \mathrm{Tj}=-40^{\circ} \mathrm{C}$ to $125^{\circ} \mathrm{C}$ |  |  | 133 | $\mu \mathrm{A}$ |
| $\mathrm{I}_{\mathrm{Q}}$ | Quiescent current | into VOUT; IOUT $=0 \mathrm{~mA}$, $\mathrm{V}_{\mathrm{EN}}=\mathrm{VIN}=6 \mathrm{~V}, \mathrm{VOUT}=5 \mathrm{~V}, \mathrm{PFM}$ $\mathrm{Tj}=-40^{\circ} \mathrm{C}$ to $85^{\circ} \mathrm{C}$ | 5 |  | 9 | $\mu \mathrm{A}$ |
| $\mathrm{I}_{\mathrm{Q}}$ | Quiescent current | into VOUT; IOUT $=0 \mathrm{~mA}$, $\mathrm{V}_{\mathrm{EN}}=\mathrm{VIN}=6 \mathrm{~V}, \mathrm{VOUT}=5 \mathrm{~V}, \mathrm{PFM}$ $\mathrm{Tj}=-40^{\circ} \mathrm{C}$ to $125^{\circ} \mathrm{C}$ |  |  | 17 | $\mu \mathrm{A}$ |
| $\mathrm{I}_{\mathrm{SD}}$ | Shutdown current | $\begin{aligned} & \mathrm{V}_{\mathrm{EN}}=0 \mathrm{~V} ; \mathrm{Tj}=-40^{\circ} \mathrm{C} \text { to } 85^{\circ} \mathrm{C} ; \\ & \mathrm{VIN}=5 \mathrm{~V} \end{aligned}$ | 2 |  | 12 | $\mu \mathrm{A}$ |
| $\mathrm{I}_{\mathrm{SD}}$ | Shutdown current | $\mathrm{V}_{\mathrm{EN}}=0 \mathrm{~V} ; \mathrm{Tj}=-40^{\circ} \mathrm{C}$ to $85^{\circ} \mathrm{C}$ |  |  | 26 | $\mu \mathrm{A}$ |
| $\mathrm{V}_{\text {UVLO }}$ | Undervoltage lockout threshold | VIN voltage falling | 1.7 | 1.85 | 1.95 | V |
| $\mathrm{V}_{\text {UVLO,TH }}$ | Undervoltage lockout hysteresis | VIN voltage rising | 525 | 850 |  | mV |
| $\mathrm{T}_{\mathrm{SD}}$ | Thermal shutdown |  |  | 160 |  | ${ }^{\circ} \mathrm{C}$ |
| $\mathrm{T}_{\mathrm{SD}}$ | Thermal shutdown hysteresis |  |  | 20 |  | ${ }^{\circ} \mathrm{C}$ |
| LOGIC SIGNALS: EN, PS/SYNC, PG, VSEL |  |  |  |  |  |  |
| $\mathrm{V}_{\text {THR }}$ | Threshold Voltage rising edge for EN pin and PS/SYNC used for PWM/PFM mode change |  | 0.77 | 0.8 | 0.83 | V |
| $\mathrm{V}_{\text {THF }}$ | Threshold Voltage falling edge for EN pin and PS/SYNC used for PWM/PFM mode change |  | 0.67 | 0.7 | 0.73 | V |
| $\mathrm{V}_{\mathrm{IL}}$ | VSEL low level input voltage; PS/SYNC low level input voltage when used for synchronization |  |  |  | 0.3 | V |
| $\mathrm{V}_{\mathrm{IH}}$ | VSEL high level input voltage; PS/SYNC high level input voltage when used for synchronization |  | 1.1 |  |  | V |
|  | EN, PS/SYNC, VSEL input current |  |  |  | 0.2 | $\mu \mathrm{A}$ |
| $\mathrm{V}_{\mathrm{OL}}$ | PG output low voltage | $\mathrm{I}_{\mathrm{PG}}=-1 \mathrm{~mA}$ |  |  | 0.4 | V |
| $\mathrm{I}_{\text {LKG }}$ | PG output leakage current | PG pin high impedance; $\mathrm{V}_{\mathrm{PG}}=5 \mathrm{~V}$ |  |  | 0.2 | $\mu \mathrm{A}$ |
| $\mathrm{I}_{\mathrm{PG}}$ | PG sink current |  |  |  | 1 | mA |
| $\mathrm{V}_{\text {TH_PG }}$ | Power Good Threshold Voltage, rising Vout |  | 94.5 | 96 | 98.5 | $\%$ |
| $\mathrm{V}_{\text {TH_PG }}$ | Power Good Threshold Voltage, falling Vout |  | 90 | 92 | 94.5 | $\%$ |# Electrical Characteristics (continued) 

over VIN $=2 \mathrm{~V}$ to $16 \mathrm{~V} ; \mathrm{Tj}=-40^{\circ} \mathrm{C}$ to $125^{\circ} \mathrm{C}$; typical values are at $\mathrm{Tj}=25^{\circ} \mathrm{C}$ (unless otherwise noted)

| PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| OUTPUT |  |  |  |  |  |  |
| VOUT | TPS63070/TPS630702 output voltage range ${ }^{11)}$ |  | 2.5 |  | 9 | V |
| VOUT | TPS630701 output voltage |  | 5.0 |  |  | V |
| $\mathrm{V}_{\mathrm{FB}}$ | TPS63070/TPS630702 feedback voltage | PS/SYNC = VIN | 800 |  |  | mV |
|  | feedback impedance | for fixed voltage versions | 1.5 |  |  | $\mathrm{M} \Omega$ |
|  | feedback leakage | for adjustable version; VFB $=0.8 \mathrm{~V}$ |  |  | 100 | nA |
| $\mathrm{V}_{\mathrm{FB}}$ | TPS63070/TPS630702 feedback voltage accuracy | PS/SYNC = GND (PWM mode) | $-1$ |  | 1 | \% |
| VOUT | TPS630701 output voltage accuracy | PS/SYNC = GND (PWM mode) | $-1$ |  | 1 | \% |
| $\mathrm{V}_{\mathrm{FB}}$ | TPS63070/TPS630702 feedback voltage accuracy | PS/SYNC = VIN (PFM mode); VIN $\geq 3 \mathrm{~V}$ | $-1$ |  | 3 | \% |
| VOUT | TPS630701 output voltage accuracy | PS/SYNC = VIN (PFM mode); <br> VIN $\geq 3 \mathrm{~V}$ | $-1$ |  | 3 | \% |
| $t_{\text {SW }}$ | Oscillator frequency |  | 2100 | 2400 | 2700 | kHz |
|  | Frequency range for synchronization |  | 2100 |  | 2800 | kHz |
| $\operatorname{IIN}, \max$ | Average, positive input current limit | $\begin{aligned} & \mathrm{VIN}=5.0 \mathrm{~V} ; \mathrm{VOUT}=6.5 \mathrm{~V} ; \\ & \mathrm{Tj}=0^{\circ} \mathrm{C} \text { to } 125^{\circ} \mathrm{C} \end{aligned}$ | 3050 | 3600 | 4150 | mA |
| $\operatorname{IIN}, \max$ | Average, negative input current limit | $\begin{aligned} & \mathrm{VIN}=5.0 \mathrm{~V} ; \mathrm{VOUT}=6.5 \mathrm{~V} ; \\ & \mathrm{Tj}=0^{\circ} \mathrm{C} \text { to } 125^{\circ} \mathrm{C} \end{aligned}$ | 1100 | 1800 |  | mA |
| $\begin{aligned} & \mathrm{R}_{\mathrm{DS}(\mathrm{ON})} \\ & \text { BUCK } \end{aligned}$ | High side switch on resistance | VIN $=5 \mathrm{~V}$ | 50 |  | 80 | $\mathrm{m} \Omega$ |
|  | Low side switch on resistance | VIN $=5 \mathrm{~V}$ | 100 |  | 160 | $\mathrm{m} \Omega$ |
| $\mathrm{R}_{\text {DS(ON) }}$ <br> BOOST | High side switch on resistance | VIN $=5 \mathrm{~V}$ | 40 |  | 70 | $\mathrm{m} \Omega$ |
|  | Low side switch on resistance | VIN $=5 \mathrm{~V}$ | 80 |  | 125 | $\mathrm{m} \Omega$ |
| $\begin{aligned} & \mathrm{R}_{\mathrm{DS}(\mathrm{ON})} \\ & \mathrm{FB} 2 \end{aligned}$ | FB2 resistance to GND with VSEL = high |  | 25 |  | 100 | $\Omega$ |
| $t_{\text {LKG }}$ | Input leakage current into FB2 with VSEL=low | VFB $=$ VFB2 $=0.8 \mathrm{~V}$ |  |  | 100 | nA |
|  | FB2 sink current |  |  |  | 100 | $\mu \mathrm{A}$ |
|  | Line regulation | Power Save Mode disabled | 0.07 |  |  | $\% / \mathrm{V}$ |
|  | Load regulation | Power Save Mode disabled | 0.2 |  |  | \%/A |
| $\mathrm{V}_{\text {AUX }}$ | Maximum bias voltage | VIN $\geq$ VOUT; VIN $<6 \mathrm{~V}$ | VIN - 0.3 |  | 7 | V |
|  |  | VIN < VOUT | $\begin{gathered} \text { VOUT - } \\ 0.3 \end{gathered}$ |  | 7 | V |
| $R_{O D}$ | Output discharge resistance (only in TPS630702) | VIN $=5 \mathrm{~V} ;$ VOUT $=5 \mathrm{~V}$ | 200 |  |  | $\Omega$ |
| $t_{\text {delay }}$ | Start-up delay | time from $\mathrm{EN}=\mathrm{V}_{\mathrm{IN}}$ to device starts switching | 70 |  |  | $\mu \mathrm{s}$ |
| $t_{\text {SS }}$ | soft-start time | time to ramp from 5\% to 95\% of Vout; buck mode; VIN $=7.2 \mathrm{~V}$, Vout $=3.3 \mathrm{~V}$, lout $=500 \mathrm{~mA}$ | 400 |  |  | $\mu \mathrm{s}$ |
|  |  | time to ramp from 5\% to 95\% of Vout; boost mode; VIN $=3.0 \mathrm{~V}$, Vout $=3.3 \mathrm{~V}$, lout $=250 \mathrm{~mA}$ | 850 |  |  | $\mu \mathrm{s}$ |

(1) Please observe the minimum duty cycle in buck mode# 7.6 Typical Characteristics 

![img-3.jpeg](img-3.jpeg)# 8 Detailed Description 

### 8.1 Overview

The TPS6307x use 4 internal N-channel MOSFETs to maintain synchronous power conversion at all possible operating conditions. This enables the device to keep high efficiency over a wide input voltage and output power range. To regulate the output voltage at all possible input voltage conditions, the device automatically switches from buck operation to boost operation and back as required by the configuration. It always uses one active switch, one rectifying switch, one switch on, and one switch held off. Therefore, it operates as a buck converter when the input voltage is higher than the output voltage, and as a boost converter when the input voltage is lower than the output voltage. There is no mode of operation in which all 4 switches are switching. The RMS current through the switches and the inductor is kept at a minimum, to minimize switching and conduction losses. For the remaining 2 switches, one is kept on and the other is kept off, thus causing no switching losses. Controlling the switches this way allows the converter to always keep high efficiency over the complete input voltage range. The device provides a seamless transition from buck to boost or from boost to buck operation.

### 8.2 Functional Block Diagram TPS63070

![img-4.jpeg](img-4.jpeg)

Figure 5. Functional Block Diagram# 8.3 Functional Block Diagram TPS630701 

![img-5.jpeg](img-5.jpeg)

Figure 6. Functional Block Diagram

### 8.4 Feature Description

### 8.4.1 Control Loop Description

The controller circuit of the device is based on an average current mode topology. The average inductor current is regulated by a fast current regulator loop which is controlled by a voltage control loop.
The non inverting input of the transconductance amplifier gmv can be assumed to be constant. The output of gmv defines the average inductor current. The inductor current is reconstructed by measuring the current through the high side buck MOSFET. This current corresponds exactly to the inductor current in boost mode. In buck mode, the current is measured during the on-time of the same MOSFET. During the off-time, the current is reconstructed internally starting from the peak value reached at the end of the on-time cycle. The average current is then compared to the desired value and the difference, or current error, is amplified and compared to the sawtooth ramp of either the Buck or the Boost. Depending on which of the two ramps is crossed by the signal, either the Buck MOSFETs or the Boost MOSFETs are activated. When the input voltage is close to the output voltage, one buck cycle is followed by a boost cycle. In this condition, not more than three cycle in a row of the same mode are allowed. This control method in the buck-boost region ensures a robust control and the highest efficiency.
For an input voltage above 9 V , and Vout below 2.2 V , the switching frequency is reduced by a factor of 2 to keep the minimum on-time at a reasonable value. For short circuit protection, at an output voltage below 1.2 V , the low side input FET and the high side output FET are not actively switched but their back-gate diode used for conduction.
TPS6307x also contains a negative current limit. This allows the inductor current to reverse and flow from the output to the input. This is required for forced PWM operation at low output current but also for applications that require a fairly high current from the output to the input like TEC (thermo electric cooling) applications where the TEC cell is placed between input and output of the converter,# Feature Description (continued) 

![img-6.jpeg](img-6.jpeg)

Figure 7. Average Current Mode Control

### 8.4.2 Precise Enable

The enable pin of the TPS63070 is not just a simple digital input but compares the voltage applied to a fixed threshold of 0.8 V for a rising voltage. This allows to drive the pin by a slowly changing voltage and enables the use of an external RC network to achieve a precise power-up delay. The enable input threshold for a falling edge is typically 100 mV lower than the rising edge threshold. The TPS63070 starts operation when the rising threshold is exceeded. For proper operation, the EN pin must be terminated and must not be left floating. Pulling the EN pin low forces the device into shutdown. In this mode, the internal high side and low side MOSFETs are turned off and the entire internal-control circuitry is switched off. The enable pin can also be used with an external voltage divider to set a user-defined minimum supply voltage.
It is recommended to not connect EN directly to VIN but use a resistor in series in the range of $1 \mathrm{k} \Omega$ to $1 \mathrm{M} \Omega$. If several inputs like EN and PS/SYNC are connected to VIN, the resistor can be shared. No resistor is required if the pin is driven from an analog or digital signal rather than a supply voltage.

### 8.4.3 Power Good

The device has a built in power good output that indicates whether the output voltage has reached its nominal value. The PG signal is generated based on the status of the output voltage monitor. The power good circuit operates as long as the converter is enabled and VIN is above the undervoltage lockout threshold.
If the output voltage has not reached the regulated condition, the PG pin is held low. When the regulated condition is reached, PG is high impedance.
The PG output needs an external pull-up resistor. This resistor can be pulled to any voltage up to the maximum output voltage rating.

Table 1. Power Good Status

| EN | output voltage status | PG |
| :--: | :--: | :--: |
| low | output off | low |
| high | output voltage above power good threshold | high impedance |
| high | output voltage below power good threshold, in thermal shutdown or input / output overvoltage protection active | low |# 8.4.4 Soft Start 

To minimize inrush current during start up, the device has a soft start. When the EN pin is set high, after a thermal shutdown or after the undervoltage lockout threshold is exceeded, a soft-start cycle is started and the input current is ramped until the output voltage reaches regulation. The device ramps up the output voltage in a controlled manner, even if a large capacitor is connected at the output. During soft-start, as long as the output voltage is below the power good threshold, the input current limit is reduced to typically 1 A . The soft-start time is defined by the current limit during the soft-start phase along with the load current, output capacitance and the input to output voltage ratio.

### 8.4.5 PS/SYNC

The PS/SYNC pin has two functions:

- switching between forced PWM mode and power save mode
- synchronizing to an external clock applied at pin PS/SYNC

When PS/SYNC is set high, the device operates in power save mode at low output current. For an average inductor current above a certain threshold the device switches to forced PWM mode. The automatic switch-over from PFM to PWM and vice versa is done such that the efficiency is kept at the maximum possible level. It is not based on a fixed threshold but at a current that depends on input voltage and output voltage to keep the efficiency at the maximum possible level.
The power save mode is disabled when PS/SYNC is set low. The device then operates in forced fixed frequency PWM mode independent of the output current.
TPS6307x can be synchronized to an external clock applied at pin PS/SYNC. Details about the voltage level and frequency range can be found in the electrical characteristics. When an external clock is detected, TPS6307x switches from internal clock or power save mode to fixed frequency operation based on the external clock frequency. When the external clock is removed, TPS6307x switches back to internal clock or power save mode depending on the average inductor current and status of the PS/SYNC pin. The PS/SYNC pin has two parallel input stages, a slow one with the precise threshold for PWM/PFM mode change and a fast digital input stage for an external clock signal for synchronization.
It is recommended to not connect PS/SYNC directly to VIN but use a resistor in series in the range of $1 \mathrm{k} \Omega$ to $1 \mathrm{M} \Omega$. If several inputs like EN and PS/SYNC are connected to VIN, the resistor can be shared. No resistor is required if the pin is driven from an analog or digital signal rather than a supply voltage.

### 8.4.6 Short Circuit Protection

The TPS6307x provides short circuit protection to protect itself and the application. When the output voltage is below 1.2 V , the back-gate diodes of the low side input FET and high side output FET are used for rectification. For an input voltage above 9 V and an output voltage below 2.2 V , the switching frequency is scaled to $1 / 2$ of its nominal value.# 8.4.7 VSEL and FB2 pins 

The VSEL pin allows to dynamically select between two different output voltages on the adjustable version. The voltage is set by a resistor that is connected between the FB and the FB2 pin. FB2 is connected to GND if VSEL = high. FB2 is high impedance if VSEL= low. The transition speed during a voltage change is defined by the loop bandwidth of the device and can be adjusted by adding a feed-forward capacitor in parallel to R1.
![img-7.jpeg](img-7.jpeg)

Figure 8. Typical Application using VSEL
The resistor values for the feedback divider and FB2 are in the $50-500 \mathrm{k} \Omega$ range. R3 is calculated as follows:
$R 3=\frac{V o 1 \times R 1 \times R 2^{2}}{(V o 2-V o 1)(R 1 \times R 2+R 2^{2})}$ for $V o 2>V o 1$
For more details on how to use VSEL see Technote SLVAE62.

### 8.4.8 Overvoltage Protection

TPS6307x has a built in over-voltage protection which limits the output voltage. The voltage is internally sensed on the VOUT pin. In case the voltage on the feedback pin is not set correctly or the connection is open, this limits the output voltage to a value that protects the output stage from a too high voltage by limiting it to a internally set value.

Input over-voltage protection forces PFM mode to make sure the device is protected against boosting from the output to the input. This may happen if there is a large capacitor charged above the nominal voltage on the output and the supply on the input is removed. In PWM mode, the device is able to provide current from the output to the input causing a rise in the input voltage. In PFM mode, the current to the input is blocked so the input voltage can not rise. The input over-voltage protection does not protect the device from a too high voltage applied to the input but just from operating such that the device itself causes a rise of the input voltage above critical levels. Both over-voltage sensors are de-glitched by approximately $1 \mu \mathrm{~s}$.

### 8.4.9 Undervoltage Lockout

When the input voltage drops, the undervoltage lockout prevents mis-operation by switching off the device. The converter starts operation when the input voltage exceeds the threshold by a hysteresis of typically 850 mV . This relatively large hysteresis is needed to allow operation down to $2-\mathrm{V}$ of supply voltage for the case when the output voltage is up at $3-\mathrm{V}$ or above but restrict start-up for the case when the output voltage is zero. For start-up when the output voltage has not yet ramped, the rising UVLO threshold was set to a level that allows to start TPS63070 at a supply voltage where the load does not demand much load current.

### 8.4.10 Overtemperature Protection

The junction temperature (Tj) of the device is monitored by an internal temperature sensor. When Tj exceeds the thermal shutdown temperature, the device goes into thermal shutdown. The power stage is turned off and PG goes low. When Tj decreases below the hysteresis amount, the converter resumes normal operation, beginning with a Soft Start cycle. To avoid unstable conditions, a hysteresis of typically $20^{\circ} \mathrm{C}$ is implemented on the thermal shutdown temperature. In addition, the thermal shutdown is debounced by approximately $10 \mu \mathrm{~s}$.# 8.5 Device Functional Modes 

### 8.5.1 Power Save Mode

Depending on the load current, in order to provide the best efficiency over the complete load range, the device works in PWM mode at an inductor current of approximately 650 mA or higher. At lighter load, the device switches automatically in to Power Save Mode to reduce power consumption and extend battery life. The PFM/PWM pin can be used to select between the two different operation modes. To enable Power Save Mode, the PFM/PWM pin must be set high.
During Power Save Mode, the part operates with a reduced switching frequency and supply current to maintain high efficiency. The output voltage is monitored by a comparator for the threshold "comp low" and "comp high" at every clock cycle. When the device enters Power Save Mode, the converter stops operating and the output voltage drops. The slope of the output voltage depends on the load and the output capacitance. When the output voltage reaches the comp low threshold, at the next clock cycle the device ramps up the output voltage again by starting operation. Operation can last for one or several pulses until the "comp high" threshold is reached. At the next PFM cycle, if the inductor current is still lower than about 650 mA , the device switches off again and the same operation is repeated. Instead, if at the next PFM cycle, the inductor current is above approximately 650 mA , the device automatically switches to PWM mode.
In order to keep high efficiency in PFM mode, there is only a comparator active to keep the output voltage regulated. The AC ripple in this condition is increased, compared to the voltage in PWM mode. The amplitude of this voltage ripple typically is 50 mV pk-pk, with $22 \mu \mathrm{~F}$ effective capacitance. In order to avoid a critical voltage drop when switching from 0 A to full load, the output voltage in PFM is typically $1 \%$ above the nominal value in PWM. This allows the converter to operate with a small output capacitor and still have a low absolute voltage drop during heavy load transients.
Power Save Mode can be disabled by programming the PFM/PWM pin low.
![img-8.jpeg](img-8.jpeg)

Figure 9. Dynamic Voltage Positioning

### 8.5.2 Current Limit

it is possible to calculate the output current in the different conditions in boost mode using Equation 2 and Equation 3 and in buck mode using Equation 4 and Equation 5.

$$
\begin{array}{ll}
\text { Duty Cycle Boost } & D=\frac{V_{\text {OUT }}-V_{\text {IN }}}{V_{\text {OUT }}} \\
\text { Output Current Boost } & I_{\text {OUT }}=\eta \times I_{\text {IN }}(1-D) \\
\text { Duty Cycle Buck } & D=\frac{V_{\text {OUT }}}{V_{\text {IN }}} \\
\text { Output Current Buck } & I_{\text {OUT }}=\left(\eta \times I_{\text {IN }}\right) / D
\end{array}
$$# Device Functional Modes (continued) 

With,
$\eta=$ Estimated converter efficiency (use the number from the efficiency curves or 0.90 as an assumption)
$I_{I N}=$ Minimum average input current
The maximum output current TPS63070 can provide, can directly be seen from the graphs "Maximum Load Current vs Input Voltage" for different output voltages at (Figure 43, Figure 20 and Figure 22 ). The start-up current is lower because the current limit is set to typically 1 A to limit the inrush current at start-up as long as the power good signal is low. Please see the typical start-up current graphs at Figure 42, Figure 19 and Figure 21. Once the power good comparator indicates "power good", the current limit is set to its nominal value as given in the electrical characteristics.

### 8.5.3 Output Discharge Function (TPS630702 only)

To make sure the load applied at TPS630702 is powered up from 0 V once TPS630702 is enabled, the device features an internal discharge resistor for the output capacitor. The discharge function is enabled as soon as the device is disabled, in thermal shutdown or in undervoltage lockout. The minimum supply voltage required for the discharge function to remain active when enabled is approximately 2 V . The discharge function is only active after the device has been enabled at least once after supply voltage was applied. This feature is only enabled in TPS630702 and it is the only difference between TPS63070 and TPS630702.# 9 Application and Implementation 

## NOTE

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

### 9.1 Application Information

The TPS6307x is a high efficiency, low quiescent current buck-boost converter suitable for applications where the input voltage can be higher or lower than the output voltage. The TPS63070 is internally supplied from the higher of the input voltage or output voltage. For proper operation either one or both need to have a voltage of 3.0 V or above but must not exceed their maximum rating.

### 9.2 Typical Application for adjustable version

![img-9.jpeg](img-9.jpeg)

Figure 10. Typical Application For Adjustable Version

### 9.2.1 Design Requirements

The design guidelines provide a component selection to operate the device within the recommended operating conditions. The input and output capacitors have been split into a small 0603 size capacitor close to the device pins and 0805 size capacitors to get the required capacitance.

Table 2. Bill of Materials

| REFERENCE | DESCRIPTION | VALUE | MANUFACTURER |
| :--: | :--: | :--: | :--: |
| IC | TPS63070RNM |  | Texas Instruments |
| L | XFL4020-152ME | $1.5 \mu \mathrm{H}$ | Coilcraft |
| CIN | GRM21BC71E106ME11L | $2 \times 10 \mu \mathrm{~F} / 25 \mathrm{~V} /$ <br> X7S / 0805 | Murata |
| C1 | TMK107BBJ106MA-T | $10 \mu \mathrm{~F} / 25 \mathrm{~V} / \mathrm{X} 5 \mathrm{R} /$ <br> 0603 | Taiyo Yuden |
| COUT | GRM21BC81C226ME44L | $3 \times 22 \mu \mathrm{~F} / 16 \mathrm{~V} /$ <br> X6S / 0805 | Murata |
| C4 | TMK107BBJ106MA-T | $10 \mu \mathrm{~F} / 25 \mathrm{~V} / \mathrm{X} 5 \mathrm{R} /$ <br> 0603 | Taiyo Yuden |Table 2. Bill of Materials (continued)

| REFERENCE | DESCRIPTION | VALUE | MANUFACTURER |
| :--: | :--: | :--: | :--: |
| CVAUX | TMK105B7104MV-FR | $100 \mathrm{nF} / 25 \mathrm{~V} / \mathrm{X} 7 \mathrm{R} /$ <br> 0402 | Taiyo Yuden |
| R1, R2 | Metal Film Resistor ; 1\% | depending on desired <br> output voltage |  |
| R4 | Metal Film Resistor ; 1\% | $100 \mathrm{k} \Omega$ |  |

# 9.2.2 Detailed Design Procedure 

The TPS6307x series of buck-boost converter has internal loop compensation. Therefore, the external L-C filter has to be selected according to the internal compensation. It's important to consider that the effective inductance, due to inductor tolerance and current derating can vary between $20 \%$ and $-30 \%$. The same for the capacitance of the output filter: the effective capacitance can vary between $+20 \%$ and $-80 \%$ of the specified datasheet value, due to capacitor tolerance and bias voltage. For this reason, Output Filter Selection shows the nominal capacitance and inductance value allowed. The effective capacitance of the adjustable version TPS63070 on the output (in $\mu \mathrm{F}$ ) needs to be at least 10 times higher than the effective inductance (in $\mu \mathrm{H}$ ) to ensure a good transient response and stable operation.

Table 3. Output Filter Selection

| INDUCTOR <br> VALUE $[\mu \mathrm{H}]^{(1)}$ | OUTPUT CAPACITOR VALUE $[\mu \mathrm{F}]^{(2)}$ |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  | 22 | 47 | 68 | 100 |
| 1.0 |  | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| 1.5 |  | $\sqrt{ }^{(3)}$ | $\checkmark$ | $\checkmark$ |
| 2.2 |  |  | $\checkmark$ | $\checkmark$ |

(1) Inductor tolerance and current de-rating is anticipated. The effective inductance can vary by $+20 \%$ and $-30 \%$.
(2) Capacitance tolerance and bias voltage de-rating of $+20 \%$ and $-50 \%$ is anticipated. For capacitors with larger dc bias effect, a larger nominal value needs to be selected.
(3) Typical application. Other check marks indicates recommended filter combinations

### 9.2.2.1 Programming The Output Voltage

While the output voltage of the TPS63070 is adjustable, the TPS630701 is set to a fixed voltage. For fixed output versions, the FB pin must be connected to the output directly. The adjustable version can be programmed for output voltages from 2.5 V to 9 V by using a resistive divider from VOUT to GND. The voltage at the FB pin $\left(V_{\text {REF }}\right)$ is regulated to 800 mV . The value of the output voltage is set by the selection of the resistive divider from Equation 6. It is recommended to choose resistor values which allow a current of at least $2 u A$, meaning the value of R2 shouldn't exceed $400 \mathrm{k} \Omega$. Lower resistor values are recommended for highest accuracy and most robust design.

$$
R_{1}=R_{2}\left(\frac{V_{\text {OUT }}}{0.8 \mathrm{~V}}-1\right)
$$

Table 4. Typical Resistor Values

| Output Voltage | R1 | R2 |
| :--: | :--: | :--: |
| 3.3 V | $470 \mathrm{k} \Omega$ | $150 \mathrm{k} \Omega$ |
| 5.0 V | $680 \mathrm{k} \Omega$ | $130 \mathrm{k} \Omega$ |
| 5.3 V | $560 \mathrm{k} \Omega$ | $100 \mathrm{k} \Omega$ |
| 5.5 V | $300 \mathrm{k} \Omega$ | $51 \mathrm{k} \Omega$ |
| 6.5 V | $360 \mathrm{k} \Omega$ | $51 \mathrm{k} \Omega$ |
| 9 V | $402 \mathrm{k} \Omega$ | $39 \mathrm{k} \Omega$ |# 9.2.2.2 Inductor Selection 

For high efficiencies, the inductor should have a low dc resistance to minimize conduction losses. Especially at high switching frequencies, the core material has a higher impact on efficiency. When using small chip inductors, the efficiency is reduced mainly due to higher inductor core losses. This needs to be considered when selecting the appropriate inductor. The inductor value determines the inductor ripple current. The larger the inductor value, the smaller the inductor ripple current and the lower the conduction losses of the converter. Conversely, larger inductor values cause a slower load transient response. To avoid saturation of the inductor, the peak current for the inductor in steady state operation is calculated using Equation 8. Only the equation which defines the switch current in boost mode is shown, because this provides the highest value of current and represents the critical current value for selecting the right inductor.

$$
\begin{aligned}
& \text { Duty Cycle Boost } \quad \mathrm{D}=\frac{\mathrm{V}_{\text {OUT }}-\mathrm{V}_{\mathrm{IN}}}{\mathrm{~V}_{\text {OUT }}} \\
& \mathrm{I}_{\text {PEAK }}=\frac{\text { lout }}{\eta \times(1-\mathrm{D})}+\frac{\text { Vin } \times \mathrm{D}}{2 \times f \times \mathrm{L}}
\end{aligned}
$$

Where,
$\mathrm{D}=$ Duty Cycle in Boost mode
$\mathrm{f}=$ Converter switching frequency (typical 2.4 MHz )
$\mathrm{L}=$ Selected inductor value
$\eta=$ Estimated converter efficiency (use the number from the efficiency curves or 0.90 as an assumption)
Note: The calculation must be done for the minimum input voltage which is possible to have in boost mode
Calculating the maximum inductor current using the actual operating conditions gives the minimum saturation current of the inductor needed. It is recommended to choose an inductor with a saturation current $20 \%$ higher than the value calculated from Equation 8. The following inductors are recommended for use:

Table 5. Inductor Selection

| INDUCTOR VALUE | COMPONENT SUPPLIER ${ }^{(1)}$ | SIZE (LxWxH/mm) | Isat/DCR |
| :--: | :--: | :--: | :--: |
| $1.2 \mu \mathrm{H}$ | Coilcraft, XFL4015-122ME | $4 \times 4 \times 1.5$ | $4.5 \mathrm{~A} / 18.8 \mathrm{~m} \Omega$ |
| $1.5 \mu \mathrm{H}$ | Coilcraft, XFL4020-152ME | $4 \times 4 \times 2.1$ | $4.6 \mathrm{~A} / 14.4 \mathrm{~m} \Omega$ |
| $1.0 \mu \mathrm{H}$ | Coilcraft, XFL4020-102ME | $4 \times 4 \times 2.1$ | $5.4 \mathrm{~A} / 10.8 \mathrm{~m} \Omega$ |
| $1 \mu \mathrm{H}$ | Murata, 1277AS-H-1R0M | $3.2 \times 2.5 \times 1.2$ | $3.7 \mathrm{~A} / 45 \mathrm{~m} \Omega$ |

(1) See Third-party Products Disclaimer

The inductor value also affects the stability of the feedback loop. In particular the boost transfer function exhibits a right half-plane zero. The frequency of the right half plane zero is inverse proportional to the inductor value and the load current. This means the higher the value of the inductance and load current, the more the right half plane zero is moved to a lower frequency. This degrades the phase margin of the feedback loop. It is recommended to choose the inductor's value in order to have the frequency of the right half plane zero $>400$ kHz . The frequency of the RHPZ is calculated using Equation 9.

$$
f_{\text {RHPZ }}=\frac{(1-\mathrm{D})^{2} \times \text { Vout }}{2 \pi \times \text { lout } \times \mathrm{L}}
$$

With,
$\mathrm{D}=$ Duty Cycle in Boost mode
Note: The calculation must be done for the minimum input voltage which is possible to have in boost mode
If the operating conditions results in a frequency of the RHPZ of less than 400 kHz , more output capacitance should be added to reduce the cross over frequency. The RHPZ moves to lowest frequency at lowest input voltage (highest boost factor) and largest output current. Device stability should therefore be observed mainly under these worst case operating conditions.# 9.2.2.3 Capacitor Selection 

### 9.2.2.3.1 Input Capacitor

It is recommended to use a combination of capacitors on the input. A small size ceramic capacitor as close as possible from the VIN pin to GND to block high frequency noise and a larger one in parallel for the required capacitance on for good transient behavior of the regulator. X5R or X7R ceramic capacitor are recommended. The input capacitor needs to be large enough to avoid supply voltage dips shorter than 5us as the undervoltage lockout circuitry needs time to react.

### 9.2.2.3.2 Output Capacitor

Same as the input, the output capacitor should be a combination of capacitors optimized for suppressing high frequency noise and a larger capacitor for low output voltage ripple and stable operation. The use of small X5R or X7R ceramic capacitors placed as close as possible to the VOUT and GND pins of the IC is recommended. A 0603 size capacitor close to the pins of the IC and as many 0805 capacitors as required to get the capacitance given the output voltage and dc bias effect of the ceramic capacitors is best. The recommended typical output capacitor values are outlined in Output Filter Selection. Please also see the Recommended Operating Conditions for the minimum and maximum capacitance at the output.
Larger capacitors will cause lower output voltage ripple as well as lower output voltage drop during load transients.

Table 6. Typical Capacitors

| VALUE | PART NUMBER | COMPONENT SUPPLIER ${ }^{(1)}$ | COMMENT | SIZE (LxWxH mm) |
| :--: | :--: | :--: | :--: | :--: |
| $22 \mu \mathrm{~F}$ | EMK212BBJ226MG-T | Taiyo Yuden | input capacitor for Vin $\leq 8 \mathrm{~V}$ | $2 \times 1.25 \times 1.25$ |
| $22 \mu \mathrm{~F}$ | TMK316BBJ226ML | Taiyo Yuden | input capacitor | $3.2 \times 1.6 \times 1.6$ |
| $10 \mu \mathrm{~F}$ | TMK107BBJ106MA-T | Taiyo Yuden | bypass capacitor directly at device pins on VIN to GND and VOUT to GND | $1.6 \times 0.8 \times 0.8$ |
| $10 \mu \mathrm{~F}$ | GRM21BC71E106ME11 | Murata | small body size; 2 parts required if used at VIN $>6 \mathrm{~V}$ | $2 \times 1.25 \times 1.25$ |
| $22 \mu \mathrm{~F}$ | GRM21BC81C226ME44 | Murata | small body size; 3 parts required if used at Vo $>5 \mathrm{~V}$; otherwise 2 parts | $2 \times 1.25 \times 1.25$ |

(1) See Third-party Products Disclaimer# 9.2.3 Application Curves 

Table 7. Typical Application Curves for Adjustable Version

| Parameter | Conditions | Figure |
| :--: | :--: | :--: |
| Efficiency |  |  |
| Efficiency vs Output Current (PFM/PWM) | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\mathrm{OUT}}= \\ & 7 \mathrm{~V}, \text { PS/SYNC = Low } \end{aligned}$ | Figure 11 |
| Efficiency vs Output Current (PWM only) | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\mathrm{OUT}}= \\ & 7 \mathrm{~V}, \text { PS/SYNC = High } \end{aligned}$ | Figure 12 |
| Efficiency vs Output Current (PFM/PWM) | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\mathrm{OUT}}= \\ & 9 \mathrm{~V}, \text { PS/SYNC = Low } \end{aligned}$ | Figure 13 |
| Efficiency vs Output Current (PWM only) | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\mathrm{OUT}}= \\ & 9 \mathrm{~V}, \text { PS/SYNC = High } \end{aligned}$ | Figure 14 |
| Load Regulation |  |  |
| Load Regulation, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\mathrm{OUT}}= \\ & 7 \mathrm{~V}, \text { PS/SYNC = Low } \end{aligned}$ | Figure 15 |
| Load Regulation, PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\mathrm{OUT}}= \\ & 7 \mathrm{~V}, \text { PS/SYNC = High } \end{aligned}$ | Figure 16 |
| Load Regulation, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\mathrm{OUT}}= \\ & 9 \mathrm{~V}, \text { PS/SYNC = Low } \end{aligned}$ | Figure 17 |
| Load Regulation, PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\mathrm{OUT}}= \\ & 9 \mathrm{~V}, \text { PS/SYNC = High } \end{aligned}$ | Figure 18 |
| Output Current |  |  |
| Typical Start-up Current vs Input Voltage | $\begin{aligned} & \mathrm{V}_{\text {OUT }}=7 \mathrm{~V}, \mathrm{~T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}, 25^{\circ} \mathrm{C}, 85^{\circ} \mathrm{C}, 125 \\ & { }^{\circ} \mathrm{C} \end{aligned}$ | Figure 19 |
| Maximum Load Current vs Input Voltage | $\begin{aligned} & \mathrm{V}_{\text {OUT }}=7 \mathrm{~V}, \mathrm{~T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}, 25^{\circ} \mathrm{C}, 85^{\circ} \mathrm{C}, 125 \\ & { }^{\circ} \mathrm{C}, \mathrm{PG}=\text { high } \end{aligned}$ | Figure 20 |
| Typical Start-up Current vs Input Voltage | $\begin{aligned} & \mathrm{V}_{\text {OUT }}=9 \mathrm{~V}, \mathrm{~T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}, 25^{\circ} \mathrm{C}, 85^{\circ} \mathrm{C}, 125 \\ & { }^{\circ} \mathrm{C} \end{aligned}$ | Figure 21 |
| Maximum Load Current vs Input Voltage | $\begin{aligned} & \mathrm{V}_{\text {OUT }}=9 \mathrm{~V}, \mathrm{~T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}, 25^{\circ} \mathrm{C}, 85^{\circ} \mathrm{C}, 125 \\ & { }^{\circ} \mathrm{C}, \mathrm{PG}=\text { high } \end{aligned}$ | Figure 22 |
| Regulation Accuracy |  |  |
| Load Transient, PFM/PWM Boost Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=4.2 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=7 \mathrm{~V}, \text { Load }=100 \mathrm{~mA} \text { to } 1 \\ & \text { A, PS/SYNC = Low } \end{aligned}$ | Figure 23 |
| Load Transient, PFM/PWM Buck Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=7 \mathrm{~V}, \text { Load }=200 \mathrm{~mA} \text { to } \\ & 1.8 \mathrm{~A}, \text { PS/SYNC = Low } \end{aligned}$ | Figure 24 |
| Load Transient, PFM/PWM Boost Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=4.2 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=9 \mathrm{~V}, \text { Load }=100 \mathrm{~mA} \text { to } 1 \\ & \text { A, PS/SYNC = Low } \end{aligned}$ | Figure 25 |
| Load Transient, PFM/PWM Buck Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=9 \mathrm{~V}, \text { Load }=200 \mathrm{~mA} \text { to } \\ & 1.8 \mathrm{~A}, \text { PS/SYNC = Low } \end{aligned}$ | Figure 26 |
| Line Transient, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V} \text { to } 9 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=7 \mathrm{~V}, \text { Load }=1 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 27 |
| Line Transient, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=8 \mathrm{~V} \text { to } 12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=9 \mathrm{~V}, \text { Load }=1 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 28 |
| Output Voltage Ripple |  |  |
| Output Voltage Ripple, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=7 \mathrm{~V}, \text { Load }=0.3 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 29 |
| Output Voltage Ripple, PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=7 \mathrm{~V}, \text { Load }=1 \mathrm{~A}, \\ & \text { PS/SYNC = high } \end{aligned}$ | Figure 30 |
| Output Voltage Ripple, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=7 \mathrm{~V}, \text { Load }=0.3 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 31 |
| Output Voltage Ripple, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=9 \mathrm{~V}, \text { Load }=0.1 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 32 |
| Output Voltage Ripple, PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=5 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=9 \mathrm{~V}, \text { Load }=0.5 \mathrm{~A}, \\ & \text { PS/SYNC = high } \end{aligned}$ | Figure 33 |
| Output Voltage Ripple, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=9 \mathrm{~V}, \text { Load }=0.1 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 34 |Table 7. Typical Application Curves for Adjustable Version (continued)

| Parameter | Conditions | Figure |
| :-- | :-- | :-- |
| Startup |  |  |
| Start-up Behavior from Rising Enable, PFM/PWM <br> Operation | $\mathrm{V}_{\mathrm{IN}}=4.5 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=7 \mathrm{~V}$, Load $=0.5 \mathrm{~A}$, <br> PS/SYNC $=$ Low | Figure 35 |
| Start-up Behavior from Rising Enable, PFM/PWM <br> Operation | $\mathrm{V}_{\mathrm{IN}}=7 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=9 \mathrm{~V}$, Load $=0.5 \mathrm{~A}$, <br> PS/SYNC $=$ Low | Figure 36 |

![img-10.jpeg](img-10.jpeg)![img-11.jpeg](img-11.jpeg)

Figure 17. Output Voltage vs Output Current
![img-12.jpeg](img-12.jpeg)

Figure 19. Typical Start-up Current
![img-13.jpeg](img-13.jpeg)

Figure 21. Typical Start-up Current
![img-14.jpeg](img-14.jpeg)

Figure 18. Output Voltage vs Output Current
![img-15.jpeg](img-15.jpeg)

Figure 20. Maximum Load Current vs Input Voltage
![img-16.jpeg](img-16.jpeg)

Figure 22. Maximum Load Current vs Input Voltage![img-17.jpeg](img-17.jpeg)

Figure 23. Load Transient Response
![img-18.jpeg](img-18.jpeg)

Figure 25. Load Transient Response
![img-19.jpeg](img-19.jpeg)

Figure 27. Line Transient Response
![img-20.jpeg](img-20.jpeg)

Figure 24. Load Transient Response
![img-21.jpeg](img-21.jpeg)

Figure 26. Load Transient Response
![img-22.jpeg](img-22.jpeg)

Figure 28. Line Transient Response![img-23.jpeg](img-23.jpeg)

Figure 29. Output Voltage Ripple
![img-24.jpeg](img-24.jpeg)

Figure 31. Output Voltage Ripple
![img-25.jpeg](img-25.jpeg)

Figure 33. Output Voltage Ripple
![img-26.jpeg](img-26.jpeg)

Figure 30. Output Voltage Ripple
![img-27.jpeg](img-27.jpeg)

Figure 32. Output Voltage Ripple
![img-28.jpeg](img-28.jpeg)

Figure 34. Output Voltage Ripplewww.ti.com
SLVSC58B - JUNE 2016-REVISED MARCH 2019
![img-29.jpeg](img-29.jpeg)# 9.3 Typical Application for Fixed Voltage Version 

![img-30.jpeg](img-30.jpeg)

Figure 37. Typical Application For Fixed Voltage Version With Minimum External Part Count And Minimum Soft Start Time

### 9.3.1 Design Requirements

The design guidelines provide a component selection to operate the device within the recommended operating conditions. The input and output capacitors have been split into a small 0603 size capacitor close to the device pins and 0805 size capacitors to get the required capacitance.

Table 8. Bill of Materials

| REFERENCE | DESCRIPTION | VALUE | MANUFACTURER |
| :--: | :--: | :--: | :--: |
| IC | TPS630701RNM |  | Texas Instruments |
| L | XFL4020-1.5 $\mu \mathrm{H}$ | $1.5 \mu \mathrm{H}$ | Coilcraft |
| CIN | GRM21BC71E106ME11L | $2 \times 10 \mu \mathrm{~F} / 25 \mathrm{~V} /$ <br> X7S / 0805 | Murata |
| C1 | TMK107BBJ106MA-T | $10 \mu \mathrm{~F} / 25 \mathrm{~V} / \mathrm{X} 5 \mathrm{R} /$ <br> 0603 | Taiyo Yuden |
| COUT | GRM21BC81C226ME44L | $3 \times 22 \mu \mathrm{~F} / 16 \mathrm{~V} /$ <br> X6S / 0805 | Murata |
| C4 | TMK107BBJ106MA-T | $10 \mu \mathrm{~F} / 25 \mathrm{~V} / \mathrm{X} 5 \mathrm{R} /$ <br> 0603 | Taiyo Yuden |
| CVAUX | TMK105B7104MV-FR | $100 \mathrm{nF} / 25 \mathrm{~V} / \mathrm{X} 7 \mathrm{R} /$ <br> 0402 | Taiyo Yuden |
| R4 | Metal Film Resistor ; 1\% | $100 \mathrm{k} \Omega$ | - |# 9.3.2 Detailed Design Procedure 

The TPS6307x series of buck-boost converter has internal loop compensation. Therefore, the external L-C filter has to be selected according to the internal compensation. It's important to consider that the effective inductance, due to inductor tolerance and current derating can vary between $20 \%$ and $-30 \%$. The same for the capacitance of the output filter: the effective capacitance can vary between $+20 \%$ and $-80 \%$ of the specified datasheet value, due to capacitor tolerance and bias voltage. For this reason, Output Filter Selection shows the nominal capacitance and inductance value allowed. For the fixed voltage version TPS630701, the effective capacitance on the output (in $\mu \mathrm{F}$ ) needs to be at least 15 times higher than the effective inductance (in $\mu \mathrm{H}$ ) to ensure a good transient response and stable operation.

### 9.3.3 Application Curves

Table 9. Typical Application Curves for Fixed Voltage Version

| Parameter | Conditions | Figure |
| :--: | :--: | :--: |
| Efficiency |  |  |
| Efficiency vs Output Current (PFM/PWM) | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}= \\ & 5 \mathrm{~V}, \text { PS/SYNC = Low } \end{aligned}$ | Figure 38 |
| Efficiency vs Output Current (PWM only) | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}= \\ & 5 \mathrm{~V}, \text { PS/SYNC = High } \end{aligned}$ | Figure 39 |
| Load Regulation |  |  |
| Load Regulation, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}= \\ & 5 \mathrm{~V}, \text { PS/SYNC = Low } \end{aligned}$ | Figure 40 |
| Load Regulation, PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=3 \mathrm{~V}, 4.2 \mathrm{~V}, 5 \mathrm{~V}, 7 \mathrm{~V}, 9 \mathrm{~V}, 12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}= \\ & 5 \mathrm{~V}, \text { PS/SYNC = High } \end{aligned}$ | Figure 41 |
| Output Current |  |  |
| Typical Start-up Current vs Input Voltage | $\begin{aligned} & \mathrm{V}_{\text {OUT }}=5 \mathrm{~V}, \mathrm{~T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}, 25^{\circ} \mathrm{C}, 85^{\circ} \mathrm{C}, 125 \\ & { }^{\circ} \mathrm{C} \end{aligned}$ | Figure 42 |
| Maximum Load Current vs Input Voltage | $\begin{aligned} & \mathrm{V}_{\text {OUT }}=5 \mathrm{~V}, \mathrm{~T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}, 25^{\circ} \mathrm{C}, 85^{\circ} \mathrm{C}, 125 \\ & { }^{\circ} \mathrm{C}, \mathrm{PG}=\text { high } \end{aligned}$ | Figure 43 |
| Regulation Accuracy |  |  |
| Load Transient, PFM/PWM Boost Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=4.2 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}, \text { Load }=100 \mathrm{~mA} \text { to } 1 \\ & \text { A, PS/SYNC = Low } \end{aligned}$ | Figure 44 |
| Load Transient, PFM/PWM Buck Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}, \text { Load }=200 \mathrm{~mA} \text { to } \\ & 1.8 \mathrm{~A}, \text { PS/SYNC = Low } \end{aligned}$ | Figure 45 |
| Line Transient, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=4.2 \mathrm{~V} \text { to } 7 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}, \text { Load }=1 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 46 |
| Output Voltage Ripple |  |  |
| Output Voltage Ripple, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=4.2 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}, \text { Load }=0.3 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 47 |
| Output Voltage Ripple, PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=4.2 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}, \text { Load }=1 \mathrm{~A}, \\ & \text { PS/SYNC = high } \end{aligned}$ | Figure 48 |
| Output Voltage Ripple, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=7.2 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}, \text { Load }=0.3 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 49 |
| Startup |  |  |
| Start-up Behavior from Rising Enable, PFM/PWM Operation | $\begin{aligned} & \mathrm{V}_{\mathrm{IN}}=4.5 \mathrm{~V}, \mathrm{~V}_{\text {OUT }}=5 \mathrm{~V}, \text { Load }=0.5 \mathrm{~A}, \\ & \text { PS/SYNC = Low } \end{aligned}$ | Figure 50 |![img-31.jpeg](img-31.jpeg)

Figure 38. Efficiency vs Output Current
![img-32.jpeg](img-32.jpeg)

Figure 40. Output Voltage vs Output Current
![img-33.jpeg](img-33.jpeg)

Figure 42. Typical Start-up Current
![img-34.jpeg](img-34.jpeg)

Figure 39. Efficiency vs Output Current
![img-35.jpeg](img-35.jpeg)

Figure 41. Output Voltage vs Output Current
![img-36.jpeg](img-36.jpeg)

Figure 43. Maximum Load Current vs Input Voltage![img-37.jpeg](img-37.jpeg)

Figure 44. Load Transient Response
![img-38.jpeg](img-38.jpeg)

Figure 46. Line Transient Response
![img-39.jpeg](img-39.jpeg)

Figure 48. Output Voltage Ripple
![img-40.jpeg](img-40.jpeg)

Figure 45. Load Transient Response
![img-41.jpeg](img-41.jpeg)

Figure 47. Output Voltage Ripple
![img-42.jpeg](img-42.jpeg)

Figure 49. Output Voltage Ripple![img-43.jpeg](img-43.jpeg)

Figure 50. Start-up Timing# 10 Power Supply Recommendations 

The TPS63070 device family has no special requirements for its power supply. The power supply output current needs to be rated according to the supply voltage, output voltage and output current of TPS63070. Please see the layout guidelines about the placement of the external components.

### 10.1 Thermal Information

Implementation of integrated circuits in low-profile and fine-pitch surface-mount packages typically requires special attention to power dissipation. Many system-dependent issues such as thermal coupling, airflow, added heat sinks and convection surfaces, and the presence of other heat-generating components affect the powerdissipation limits of a given component.
Three basic approaches for enhancing thermal performance are listed below.

- Improving the power dissipation capability of the PCB design
- Improving the thermal coupling of the component to the PCB by soldering the PowerPAD ${ }^{\text {TM }}$
- Introducing airflow in the system

For more details on how to use the thermal parameters in the dissipation ratings table please check the Thermal Characteristics Application Note (SZZA017) and the IC Package Thermal Metrics Application Note (SPRA953).# 11 Layout 

### 11.1 Layout Guidelines

For all switching power supplies, the layout is an important step in the design, especially at high peak currents and high switching frequencies. If the layout is not carefully done, the regulator could show stability problems as well as EMI problems. Therefore, use wide and short traces for the main current path and for the power ground connection. The input capacitor, output capacitor, and the inductor should be placed as close as possible to the IC. Use a common ground node for power ground and a different one for control ground to minimize the effects of ground noise. Connect these ground nodes at any place close to one of the ground pin of the IC.
A ceramic capacitor each, as close as possible from the VIN pin to GND and one from the VOUT pin to GND, shown as C 1 and C 4 in the layout proposal are used to suppress high frequency noise. The case size should be 0603 or smaller for good high frequency performance. Additional 0805 size input and output capacitors are used to get the required capacitance on the input and output depending on the supply voltage range and the output voltage.
The feedback divider should be placed as close as possible to the feedback pin of the IC. To lay out the control ground, short traces are recommended as well, separation from the power ground traces. This avoids ground shift problems, which can occur due to superimposition of power ground current and control ground current.
In case any of the digital inputs EN, VSEL or PS/SYNC need to be tied to the input supply voltage VIN, a 10k resistor must be used in series. One common resistor for all digital inputs that are tied to VIN is sufficient.

### 11.2 Layout Example

![img-44.jpeg](img-44.jpeg)

Figure 51. EVM Layout# 12 Device and Documentation Support 

### 12.1 Device Support

### 12.1.1 Third-Party Products Disclaimer

TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

### 12.2 Related Links

The table below lists quick access links. Categories include technical documents, support and community resources, tools and software, and quick access to order now.

Table 10. Related Links

| PARTS | PRODUCT FOLDER | ORDER NOW | TECHNICAL <br> DOCUMENTS | TOOLS \& <br> SOFTWARE | SUPPORT \& <br> COMMUNITY |
| :--: | :--: | :--: | :--: | :--: | :--: |
| TPS63070 | Click here | Click here | Click here | Click here | Click here |
| TPS630701 | Click here | Click here | Click here | Click here | Click here |
| TPS630702 | Click here | Click here | Click here | Click here | Click here |

### 12.3 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper right corner, click on Alert me to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

### 12.4 Community Resources

The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.
TI E2E ${ }^{\text {TM }}$ Online Community TI's Engineer-to-Engineer (E2E) Community. Created to foster collaboration among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help solve problems with fellow engineers.
Design Support TI's Design Support Quickly find helpful E2E forums along with design support tools and contact information for technical support.

### 12.5 Trademarks

E2E is a trademark of Texas Instruments.
All other trademarks are the property of their respective owners.

### 12.6 Electrostatic Discharge Caution

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

### 12.7 Glossary

SLYZ022 - TI Glossary.
This glossary lists and explains terms, acronyms, and definitions.# 13 Mechanical, Packaging, and Orderable Information 

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
|  TPS630701RNMR | Active | Production | VQFN-HR (RNM) | 15 | 3000 | LARGE T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 125  |
|  TPS630701RNMR.A | Active | Production | VQFN-HR (RNM) | 15 | 3000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 125 | 0701  |
|  TPS630701RNMT | Active | Production | VQFN-HR (RNM) | 15 | 250 | SMALL T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 125  |
|  TPS630701RNMT.A | Active | Production | VQFN-HR (RNM) | 15 | 250 | SMALL T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 125 | 0701  |
|  TPS630702RNMR | Active | Production | VQFN-HR (RNM) | 15 | 3000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 125 | 0702  |
|  TPS630702RNMR.A | Active | Production | VQFN-HR (RNM) | 15 | 3000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 125 | 0702  |
|  TPS630702RNMT | Active | Production | VQFN-HR (RNM) | 15 | 250 | SMALL T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 125  |
|  TPS630702RNMT.A | Active | Production | VQFN-HR (RNM) | 15 | 250 | SMALL T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 125 | 0702  |
|  TPS63070RNNR | Active | Production | VQFN-HR (RNM) | 15 | 3000 | LARGE T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 125  |
|  TPS63070RNNR.A | Active | Production | VQFN-HR (RNM) | 15 | 3000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 125 | 3070  |
|  TPS63070RNNR | Active | Production | VQFN-HR (RNM) | 15 | 250 | SMALL T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 125  |
|  TPS63070RNNR.A | Active | Production | VQFN-HR (RNM) | 15 | 250 | SMALL T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 125 | 3070  |

${ }^{(1)}$ Status: For more details on status, see our product life cycle. ${ }^{(2)}$ Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind. ${ }^{(3)}$ RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition. ${ }^{(4)}$ Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width. ${ }^{(5)}$ MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board. ${ }^{(6)}$ Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "-" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.# TAPE AND REEL INFORMATION 

![img-45.jpeg](img-45.jpeg)

TAPE DIMENSIONS
![img-46.jpeg](img-46.jpeg)

| A0 | Dimension designed to accommodate the component width |
| :-- | :-- |
| B0 | Dimension designed to accommodate the component length |
| K0 | Dimension designed to accommodate the component thickness |
| W | Overall width of the carrier tape |
| P1 | Pitch between successive cavity centers |

QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE
![img-47.jpeg](img-47.jpeg)

Pocket Quadrants
*All dimensions are nominal

| Device | Package <br> Type | Package <br> Drawing | Pins | SPQ | Reel <br> Diameter <br> (mm) | Reel <br> Width <br> W1 (mm) | A0 <br> (mm) | B0 <br> (mm) | K0 <br> (mm) | P1 <br> (mm) | W <br> (mm) | Pin1 <br> Quadrant |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| TPS630701RNMT | VQFN- <br> HR | RNM | 15 | 250 | 180.0 | 12.4 | 2.8 | 3.3 | 1.2 | 8.0 | 12.0 | Q1 |
| TPS63070RNMR | VQFN- <br> HR | RNM | 15 | 3000 | 180.0 | 12.4 | 2.8 | 3.3 | 1.1 | 4.0 | 12.0 | Q1 |
| TPS63070RNMT | VQFN- <br> HR | RNM | 15 | 250 | 180.0 | 12.4 | 2.8 | 3.3 | 1.1 | 4.0 | 12.0 | Q1 |# PACKAGE MATERIALS INFORMATION

## TAPE AND REEL BOX DIMENSIONS

![img-48.jpeg](img-48.jpeg)

*All dimensions are nominal

|  Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS630701RNMT | VQFN-HR | RNM | 15 | 250 | 341.0 | 182.0 | 80.0  |
|  TPS63070RNMR | VQFN-HR | RNM | 15 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS63070RNMT | VQFN-HR | RNM | 15 | 250 | 210.0 | 185.0 | 35.0  |![img-49.jpeg](img-49.jpeg)

PLASTIC QUAD FLATPACK - NO LEAD
![img-50.jpeg](img-50.jpeg)

# NOTES: 

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.![img-51.jpeg](img-51.jpeg)

NOTES: (continued)
3. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).
4. Solder mask tolerances between and around signal pads can vary based on board fabrication site.# EXAMPLE STENCIL DESIGN 

## RNM0015A

## VQFN - 1 mm max height

PLASTIC QUAD FLATPACK - NO LEAD
![img-52.jpeg](img-52.jpeg)

NOTES: (continued)
5. For alternate stencil design recommendations, see IPC-7525 or board assembly site preference.# IMPORTANT NOTICE AND DISCLAIMER 

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.
These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.
TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.
TI objects to and rejects any additional or different terms you may have proposed.
Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265
Copyright © 2025, Texas Instruments Incorporated