# TPS6293x 3.8-V to 30-V, 2-A, 3-A Synchronous Buck Converters in a SOT583 Package 

## 1 Features

- Configured for a wide range of applications
- 3.8-V to 30-V input voltage range
- 0.8-V to 22-V output voltage range
- Ultra-low quiescent current: $12 \mu \mathrm{~A}$ (TPS62932, TPS62933, and TPS62933P)
- Integrated $76-\mathrm{m} \Omega$ and $32-\mathrm{m} \Omega$ MOSFETs
- $0.8 \mathrm{~V} \pm 1 \%$ reference voltage $\left(25^{\circ} \mathrm{C}\right)$
- Maximum $98 \%$ duty cycle operation
- Precision EN threshold
- 2-A (TPS62932) and 3-A (TPS62933 and TPS62933x) continuous output current
- $-40^{\circ} \mathrm{C}$ to $150^{\circ} \mathrm{C}$ operating junction temperature
- Numerous pin-compatible options
- TPS62932, TPS62933, and TPS62933F with the SS pin for adjustable soft-start time
- TPS62933P and TPS62933O with the PG pin for a power-good indicator
- TPS62932, TPS62933, and TPS62933P with pulse frequency modulation (PFM) for high light-load efficiency
- TPS62933F with forced continuous current modulation (FCCM)
- TPS62933O with out-of-audio (OOA) feature
- Ease of use and small solution size
- Peak current control mode with internal compensation
- 200-kHz to 2.2-MHz selectable frequency
- EMI friendly with frequency spread spectrum (TPS62932, TPS62933, TPS62933P and TPS62933O)
- Supports start-up with prebiased output
- Cycle-by-cycle OC limit for both high-side and low-side MOSFETs
- Non-latched protections for OTP, OCP, OVP, UVP, and UVLO
- 1.6-mm $\times 2.1-\mathrm{mm}$ SOT583 package
- Create a custom design with the TPS6293x using the WEBENCH ${ }^{\circledR}$ Power Designer


## 2 Applications

- Building automation, appliances, industrial PC
- Multifunction printers, enterprise projectors
- Portable electronics, connected peripherals
- Smart speakers, monitors
- Distributed power systems with 5-V, 12-V, 19-V, and $24-\mathrm{V}$ input


## 3 Description

The TPS6293x is a high-efficiency, easy-to-use synchronous buck converter with a wide input voltage
range of 3.8 V to 30 V , and supports up to 2-A (TPS62932) and 3-A (TPS62933 and TPS62933x) continuous output current and $0.8-\mathrm{V}$ to $22-\mathrm{V}$ output voltage.

The device employs fixed-frequency peak current control mode for fast transient response and good line and load regulation. The optimized internal loop compensation eliminates external compensation components.

The TPS62932, TPS62933, and TPS62933P operate in pulse frequency modulation for high light load efficiency. The TPS62933F operates in forced continuous current modulation which maintains lower output ripple during all load conditions. The TPS62933O operates in out of audio mode to avoid audible noise.

Device Information

| Part Number | Package ${ }^{(1)}$ | Body Size (NOM) |
| :--: | :--: | :--: |
| TPS6293x | SOT583 (8) | $1.60 \mathrm{~mm} \times 2.10 \mathrm{~mm}$ |

(1) For all available packages, see the orderable addendum at the end of the data sheet.
![img-0.jpeg](img-0.jpeg)

Simplified Schematic
![img-1.jpeg](img-1.jpeg)

TPS62933 Efficiency, $\mathrm{V}_{\mathrm{IN}}=24 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$# Table of Contents 

1 Features ..... 1
9.4 Device Functional Modes ..... 26
2 Applications ..... 1
10 Application and Implementation ..... 28
3 Description ..... 1
10.1 Application Information ..... 28
4 Revision History ..... 2
10.2 Typical Application ..... 28
5 Description (continued) ..... 3
10.3 What to Do and What Not to Do ..... 38
6 Device Comparison Table ..... 3
11 Power Supply Recommendations ..... 39
7 Pin Configuration and Functions ..... 3
12 Layout ..... 40
8 Specifications ..... 5
12.1 Layout Guidelines ..... 40
8.1 Absolute Maximum Ratings ..... 5
12.2 Layout Example ..... 41
8.2 ESD Ratings ..... 5
13 Device and Documentation Support ..... 42
8.3 Recommended Operating Conditions ..... 5
13.1 Device Support ..... 42
8.4 Thermal Information ..... 6
13.2 Receiving Notification of Documentation Updates ..... 42
8.5 Electrical Characteristics ..... 6
13.3 Support Resources ..... 42
8.6 Typical Characteristics ..... 9
13.4 Trademarks ..... 42
9 Detailed Description ..... 16
13.5 Electrostatic Discharge Caution ..... 42
9.1 Overview ..... 16
13.6 Glossary ..... 42
9.2 Functional Block Diagram ..... 17
14 Mechanical, Packaging, and Orderable Information ..... 43
9.3 Feature Description ..... 18

## 4 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision C (July 2022) to Revision D (August 2022) Page

- Added the TPS62933O ..... 1
- Changed link of WEBENCH® Power Designer for TPS6293x ..... 1
Changes from Revision B (February 2022) to Revision C (July 2022) Page
- Added the TPS62933F ..... 1
- Added the TPS62933P ..... 1# 5 Description (continued) 

The ULQ (ultra-low quiescent) feature is beneficial for long battery lifetime. The switching frequency can be set by the configuration of the RT pin in the range of 200 kHz to 2.2 MHz , which can optimize system efficiency, solution size, and bandwidth. The soft-start time of the TPS62932, TPS62933, and TPS62933F can be adjusted by the external capacitor at the SS pin. The TPS62932, TPS62933, TPS62933P and TPS62933O are featured with frequency spread spectrum, which helps with lowering down EMI noise.

The TPS6293x is in a small SOT583 ( $1.6 \mathrm{~mm} \times 2.1 \mathrm{~mm}$ ) package with $0.5-\mathrm{mm}$ pin pitch, and has an optimized pinout for easy PCB layout and promotes good EMI performance.

## 6 Device Comparison Table

| Part Number | Output Current | PFM or FCCM or OOA | SS or PG Pin |
| :--: | :--: | :--: | :--: |
| TPS62932 | 2 A | PFM | SS |
| TPS62933 | 3 A | PFM | SS |
| TPS62933F | 3 A | FCCM | SS |
| TPS62933P | 3 A | PFM | PG |
| TPS62933O | 3 A | OOA | PG |

## 7 Pin Configuration and Functions

![img-2.jpeg](img-2.jpeg)

Figure 7-1. TPS62932, TPS62933, and TPS62933F 8-Pin SOT583 DRL Package (Top View)
![img-3.jpeg](img-3.jpeg)

Figure 7-2. TPS62933P and TPS62933O 8-Pin SOT583 DRL Package (Top View)

Table 7-1. Pin Functions

| Pin |  | Type $^{(1)}$ | Description |
| :--: | :--: | :--: | :--: |
| Name | NO. |  |  |
| RT | 1 | A | Frequency programming input. Float for 500 kHz , tie to GND for 1.2 MHz , or connect to an RT timing resistor. See Section 9.3.5 for details. |
| EN | 2 | A | Enable input to the converter. Driving EN high or leaving this pin floating enables the converter. An external resistor divider can be used to implement an adjustable $\mathrm{V}_{\text {IN }}$ UVLO function. |
| VIN | 3 | $P$ | Supply input pin to internal LDO and high-side FET. Input bypass capacitors must be directly connected to this pin and GND. |
| GND | 4 | G | Ground pin. Connected to the source of the low-side FET as well as the ground pin for the controller circuit. Connect to system ground and the ground side of $\mathrm{C}_{\text {IN }}$ and $\mathrm{C}_{\text {OUT }}$. The path to $\mathrm{C}_{\text {IN }}$ must be as short as possible. |
| SW | 5 | $P$ | Switching output of the convertor. Internally connected to the source of the high-side FET and drain of the low-side FET. Connect to the power inductor. |
| BST | 6 | $P$ | Bootstrap capacitor connection for high-side FET driver. Connect a high-quality, 100-nF ceramic capacitor from this pin to the SW pin. |Table 7-1. Pin Functions (continued)

| Pin |  | Type $^{(1)}$ | Description |
| :--: | :--: | :--: | :--: |
| Name | NO. |  |  |
| SS/PG | 7 | A | TPS62932, TPS62933, and TPS62933F soft-start control pin. An external capacitor connected to this pin sets the internal voltage reference rising time. See Section 9.3.7 for details. A minimum $6.8-\mathrm{nF}$ ceramic capacitor must be connected at this pin, which sets the minimum soft-start time to approximately 1 ms . Do not float. |
|  |  | A | TPS62933P and TPS62933O open-drain power good indicator, which is asserted low if output voltage is out of PG threshold, overvoltage, or if the device is under thermal shutdown, EN shutdown, or during soft start. |
| FB | 8 | A | Output feedback input. Connect FB to the tap of an external resistor divider from the output to GND to set output voltage. |

(1) $\mathrm{A}=$ Analog, $\mathrm{P}=$ Power, $\mathrm{G}=$ Ground# 8 Specifications 

### 8.1 Absolute Maximum Ratings

Over the recommended operating junction temperature range of $-40^{\circ} \mathrm{C}$ to $+150^{\circ} \mathrm{C}$, unless otherwise noted ${ }^{(1)}$

|  |  | MIN | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: |
| Input voltage | $\mathrm{V}_{\text {IN }}$ | $-0.3$ | 32 | V |
|  | EN | $-0.3$ | 6 |  |
|  | FB | $-0.3$ | 6 |  |
| Output voltage | SW, DC | $-0.3$ | 32 |  |
|  | SW, transient < 10 ns | $-3$ | 33 |  |
|  | BST | $-0.3$ | $\mathrm{SW}+6$ |  |
|  | BST-SW | $-0.3$ | 6 |  |
|  | SS/PG | $-0.3$ | 6 |  |
|  | RT | $-0.3$ | 6 |  |
| $T_{J}$ | Operating junction temperature ${ }^{(2)}$ | $-40$ | 150 | ${ }^{\circ} \mathrm{C}$ |
| $T_{\text {alg }}$ | Storage temperature | $-65$ | 150 |  |

(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions. If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.
(2) Operating at junction temperatures greater than $150^{\circ} \mathrm{C}$, although possible, degrades the lifetime of the device.

### 8.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| :--: | :--: | :--: | :--: | :--: |
| $\mathrm{V}_{\text {(ESD) }}$ | Electrostatic discharge | Human body model (HBM), per ANSI/ESDA/JEDEC JS-001, all pins ${ }^{(1)}$ | $\pm 2000$ | V |
|  |  | Charged device model (CDM), per ANSI/ESDA/JEDEC JS-002, all pins ${ }^{(2)}$ | $\pm 500$ |  |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

### 8.3 Recommended Operating Conditions

Over the recommended operating junction temperature range of $-40^{\circ} \mathrm{C}$ to $+150^{\circ} \mathrm{C}$, unless otherwise noted ${ }^{(1)}$

|  |  |  | MIN | NOM | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Input voltage | $\mathrm{V}_{\text {IN }}$ |  | 3.8 |  | 30 | V |
|  | EN |  | $-0.1$ |  | 5.5 |  |
|  | FB |  | $-0.1$ |  | 5.5 |  |
|  | PG |  | $-0.1$ |  | 5.5 |  |
| Output voltage | $\mathrm{V}_{\text {OUT }}$ |  | 0.8 |  | 22 |  |
|  | SW, DC |  | $-0.1$ |  | 30 |  |
|  | SW, transient < 10 ns |  | $-3$ |  | 32 |  |
|  | BST |  | $-0.1$ |  | $\mathrm{SW}+5.5$ |  |
|  | BST-SW |  | $-0.1$ |  | 5.5 |  |
| Ouput current | $\mathrm{I}_{\text {OUT }}$ | TPS62933, TPS62933x | 0 |  | 3 | A |
|  |  | TPS62932 | 0 |  | 2 |  |
| Temperature | Operating junction temperature, $T_{J}$ |  | $-40$ |  | 150 | ${ }^{\circ} \mathrm{C}$ |

(1) The Recommended Operating Conditions indicate conditions for which the device is intended to be functional, but do not guarantee specific performance limits. For compliant specifications, see the Electrical Characteristics.# 8.4 Thermal Information 

| THERMAL METRIC ${ }^{(1)}$ |  | TPS6293x |  | UNIT |
| :--: | :--: | :--: | :--: | :--: |
|  |  | DRL (SOT583), 8 PINS |  |  |
|  |  | JEDEC ${ }^{(2)}$ | $\mathrm{EVM}^{(3)}$ |  |
| $R_{8 \text { JA }}$ | Junction-to-ambient thermal resistance | 112.2 | N/A | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $R_{8 \text { JC(top) }}$ | Junction-to-case (top) thermal resistance | 29.1 | N/A | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $R_{8 \text { JB }}$ | Junction-to-board thermal resistance | 19.3 | N/A | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $\Psi_{J T}$ | Junction-to-top characterization parameter | 1.6 | N/A | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $\Psi_{\text {JB }}$ | Junction-to-board characterization parameter | 19.2 | N/A | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |
| $R_{8 \text { JA_EVM }}$ | Junction-to-ambient thermal resistance on official EVM board | N/A | 60.2 | ${ }^{\circ} \mathrm{C} / \mathrm{W}$ |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.
(2) The value of $R_{8 \text { JA }}$ given in this table is only valid for comparison with other packages and can not be used for design purposes. These values were simulated on a standard JEDEC board. They do not represent the performance obtained in an actual application.
(3) The real $R_{8 \text { JA }}$ is tested on TI EVM (2 layer, 2-ounce copper thickness).

### 8.5 Electrical Characteristics

The electrical ratings specified in this section apply to all specifications in this document, unless otherwise noted. These specifications are interpreted as conditions that do not degrade the device parametric or functional specifications for the life of the product containing it. $T_{J}=-40^{\circ} \mathrm{C}$ to $+150^{\circ} \mathrm{C}, V_{\mathrm{IN}}=3.8 \mathrm{~V}$ to 30 V , unless otherwise noted.

| PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| POWER SUPPLY (VIN PIN) |  |  |  |  |  |  |
| $V_{\text {IN }}$ | Operation input voltage |  | 3.8 |  | 30 | V |
| $I_{Q}$ | Nonswitching quiescent current | $\begin{aligned} & \mathrm{EN}=5 \mathrm{~V}, \mathrm{~V}_{\mathrm{FB}}=0.85 \mathrm{~V}, \text { TPS62932, } \\ & \text { TPS62933, and TPS62933P } \end{aligned}$ | 12 |  |  | $\mu \mathrm{A}$ |
|  |  | $\mathrm{EN}=5 \mathrm{~V}, \mathrm{~V}_{\mathrm{FB}}=1 \mathrm{~V}, \mathrm{TPS62933F}$ | 125 |  |  |  |
|  |  | $\mathrm{EN}=5 \mathrm{~V}, \mathrm{~V}_{\mathrm{FB}}=1 \mathrm{~V}, \mathrm{TPS62933O}$ | 45 |  |  |  |
|  | Shutdown supply current | $\mathrm{V}_{\mathrm{EN}}=0 \mathrm{~V}$ | 2 |  |  | $\mu \mathrm{A}$ |
|  | Input undervoltage lockout thresholds | Rising threshold | 3.4 | 3.6 | 3.8 | V |
|  |  | Falling threshold | 3.1 | 3.3 | 3.5 | V |
|  |  | Hysteresis | 300 |  |  | mV |
| ENABLE (EN PIN) |  |  |  |  |  |  |
|  | Enable threshold | Rising enable threshold |  | 1.21 | 1.28 | V |
| $V_{\text {EN_FALL }}$ | Disable threshold | Falling disable threshold | 1.1 | 1.17 |  | V |
|  | EN pullup current | $\mathrm{V}_{\mathrm{EN}}=1.0 \mathrm{~V}$ | 0.7 |  |  | $\mu \mathrm{A}$ |
|  | EN pullup hysteresis current | $\mathrm{V}_{\mathrm{EN}}=1.5 \mathrm{~V}$ | 1.4 |  |  | $\mu \mathrm{A}$ |
| VOLTAGE REFERENCE (FB PIN) |  |  |  |  |  |  |
|  |  | $T_{J}=25^{\circ} \mathrm{C}$ | 792 | 800 | 808 | mV |
| $V_{F B}$ | FB voltage | $T_{J}=0^{\circ} \mathrm{C}$ to $85^{\circ} \mathrm{C}$ | 788 | 800 | 812 | mV |
|  |  | $T_{J}=-40^{\circ} \mathrm{C}$ to $150^{\circ} \mathrm{C}$ | 784 | 800 | 816 | mV |
|  | Input leakage current | $\mathrm{V}_{\mathrm{FB}}=0.8 \mathrm{~V}$ |  |  | 0.15 | $\mu \mathrm{A}$ |
| INTEGRATED POWER MOSFETS |  |  |  |  |  |  |
|  | High-side MOSFET on-resistance | $T_{J}=25^{\circ} \mathrm{C}, \mathrm{V}_{\text {BST }}-\mathrm{SW}=5 \mathrm{~V}$ | 76 |  |  | $\mathrm{m} \Omega$ |
|  | Low-side MOSFET on-resistance | $T_{J}=25^{\circ} \mathrm{C}$ | 32 |  |  | $\mathrm{m} \Omega$ |
| CURRENT LIMIT |  |  |  |  |  |  |
|  | High-side MOSFET current limit | TPS62933 and TPS62933x | 4.2 | 5 | 5.8 | A |
|  |  | TPS62932 | 2.8 | 3.4 | 4 |  |# 8.5 Electrical Characteristics (continued) 

The electrical ratings specified in this section apply to all specifications in this document, unless otherwise noted. These specifications are interpreted as conditions that do not degrade the device parametric or functional specifications for the life of the product containing it. $T_{J}=-40^{\circ} \mathrm{C}$ to $+150^{\circ} \mathrm{C}, V_{\mathrm{IN}}=3.8 \mathrm{~V}$ to 30 V , unless otherwise noted.

| PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\mathrm{I}_{\text {LS LIMIT }}$ | Low-side MOSFET current limit | TPS62933 and TPS62933x | 2.9 | 3.8 | 4.5 | A |
|  |  | TPS62932 | 2 | 2.5 | 3 |  |
| $\mathrm{I}_{\text {LS_NOC }}$ | Reverse current limit | TPS62933F | 1.2 | 2.4 | 3.6 | A |
| $\mathrm{I}_{\text {PEAK_MIN }}$ | Minimum peak inductor current | TPS62933, TPS62933P, and TPS62933O | 0.75 |  |  | A |
|  |  | TPS62932 | 0.53 |  |  |  |
| SOFT START (SS PIN) |  |  |  |  |  |  |
| $\mathrm{I}_{\text {SS }}$ | Soft-start charge current | TPS62932, TPS62933, and TPS62933F | 4.5 | 5.5 | 6.5 | $\mu \mathrm{A}$ |
| $\mathrm{T}_{\text {SS }}$ | Fixed internal soft-start time | TPS62933P and TPS62933O | 2 |  |  | ms |
| POWER GOOD (PG PIN) |  |  |  |  |  |  |
| $V_{\text {PGTH }}$ | PG threshold, $\mathrm{V}_{\mathrm{FB}}$ percentage | $\mathrm{V}_{\mathrm{FB}}$ falling, PG high to low | $85 \%$ |  |  |  |
|  |  | $\mathrm{V}_{\mathrm{FB}}$ rising, PG low to high | $90 \%$ |  |  |  |
|  |  | $\mathrm{V}_{\mathrm{FB}}$ falling, PG low to high | $110 \%$ |  |  |  |
|  |  | $\mathrm{V}_{\mathrm{FB}}$ rising, PG high to low | $115 \%$ |  |  |  |
| $\mathrm{T}_{\mathrm{PG} \_\mathrm{R}}$ | PG delay time | PG from low to high | 70 |  |  | $\mu \mathrm{s}$ |
| $\mathrm{T}_{\mathrm{PG} \_\mathrm{F}}$ | PG delay time | PG from high to low | 18 |  |  | $\mu \mathrm{s}$ |
| $V_{\text {IN_PG_VALID }}$ | Minimum $V_{\text {IN }}$ for valid PG output | Measured when PG $<0.5 \mathrm{~V}$ with $100-\mathrm{k} \Omega$ pullup to external 5 V | 2 | 2.5 |  | V |
| $V_{\text {PG_OL }}$ | PG output low-level voltage | $\mathrm{I}_{\mathrm{PG}}=0.5 \mathrm{~mA}$ |  | 0.3 |  | V |
| $\mathrm{I}_{\text {PG_LK }}$ | PG leakage current when open drain is high | $\mathrm{V}_{\mathrm{PG}}=5.5 \mathrm{~V}$ | $-1$ | 1 |  | $\mu \mathrm{A}$ |
| OSCILLATOR FREQUENCY (RT PIN) |  |  |  |  |  |  |
| $f_{\text {SW }}$ | Switching center frequency | RT = floating | 450 | 500 | 550 | kHz |
|  |  | RT = GND | 1000 | 1200 | 1350 |  |
|  |  | RT $=71.5 \mathrm{k} \Omega$ | 310 |  |  |  |
|  |  | RT $=9.09 \mathrm{k} \Omega$ | 2100 |  |  |  |
| $f_{\text {SW_min }}$ | Minimum switching frequency | TPS62933O | 30 |  |  | kHz |
| $t_{\text {ON_MIN }}{ }^{(1)}$ | Minimum ON pulse width |  | 70 |  |  | ns |
| $t_{\text {OFF_MIN }}{ }^{(1)}$ | Minimum OFF pulse width |  | 140 |  |  | ns |
| $t_{\text {ON_MAX }}{ }^{(1)}$ | Maximum ON pulse width |  | 7 |  |  | $\mu \mathrm{s}$ |
| OUTPUT OVERVOLTAGE AND UNDERVOLTAGE PROTECTION |  |  |  |  |  |  |
| $V_{\text {OVP }}$ | Output OVP threshold | OVP detect $(\mathrm{L} \rightarrow \mathrm{H})$ | $112 \%$ | $115 \%$ | $118 \%$ |  |
|  |  | Hysteresis | $5 \%$ |  |  |  |
| $V_{\text {UVP }}$ | Output UVP threshold | UVP detect $(\mathrm{H} \rightarrow \mathrm{L})$ | $65 \%$ |  |  |  |
| $t_{\text {hiccup_ON }}$ | UV hiccup ON time before entering hiccup mode after soft start ends |  | 256 |  |  | $\mu \mathrm{s}$ |
| $t_{\text {hiccup_OFF }}$ | UV hiccup OFF time before restart |  | $\begin{gathered} 10.5 \times \\ t_{\text {SS }} \end{gathered}$ |  |  | s |
| THERMAL SHUTDOWN |  |  |  |  |  |  |
| $\mathrm{T}_{\text {SHDN }}{ }^{(1)}$ | Thermal shutdown threshold | Shutdown temperature | 165 |  |  | ${ }^{\circ} \mathrm{C}$ |
| $T_{\text {HYS }}{ }^{(1)}$ |  | Hysteresis | 30 |  |  | ${ }^{\circ} \mathrm{C}$ |
| SPREAD SPECTRUM FREQUENCY |  |  |  |  |  |  |
| $f_{m}$ | Modulation frequency |  | $\begin{gathered} \mathrm{f}_{\text {SW }} / \\ 128 \end{gathered}$ |  |  | kHz |# 8.5 Electrical Characteristics (continued) 

The electrical ratings specified in this section apply to all specifications in this document, unless otherwise noted. These specifications are interpreted as conditions that do not degrade the device parametric or functional specifications for the life of the product containing it. $\mathrm{T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}$ to $+150^{\circ} \mathrm{C}, \mathrm{V}_{\mathrm{IN}}=3.8 \mathrm{~V}$ to 30 V , unless otherwise noted.

| PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\mathrm{f}_{\text {spread }}$ | Internal spread oscillator frequency |  |  | $\pm 6 \%$ |  |  |

(1) Not production tested, specified by design.# 8.6 Typical Characteristics 

$\mathrm{T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}$ to $150^{\circ} \mathrm{C}, \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}$, unless otherwise noted.
![img-4.jpeg](img-4.jpeg)

Figure 8-1. TPS62933 Quiescent Current vs Junction Temperature
![img-5.jpeg](img-5.jpeg)

Figure 8-3. High-Side $\mathrm{R}_{\text {DSON }}$ vs Junction Temperature
![img-6.jpeg](img-6.jpeg)

Figure 8-5. Feedback Voltage vs Junction Temperature
![img-7.jpeg](img-7.jpeg)

Figure 8-2. Shutdown Current vs Junction Temperature
![img-8.jpeg](img-8.jpeg)

Figure 8-4. Low-Side $\mathrm{R}_{\text {DSON }}$ vs Junction Temperature
![img-9.jpeg](img-9.jpeg)

Figure 8-6. Enable Threshold vs Junction Temperature# 8.6 Typical Characteristics (continued) 

$\mathrm{T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}$ to $150^{\circ} \mathrm{C}, \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}$, unless otherwise noted.
![img-10.jpeg](img-10.jpeg)

Figure 8-7. Disable Threshold vs Junction Temperature
![img-11.jpeg](img-11.jpeg)

Figure 8-9. $\mathrm{V}_{\text {IN }}$ UVLO Falling Threshold vs Junction Temperature
![img-12.jpeg](img-12.jpeg)

Figure 8-11. TPS62933 High-Side Current Limit vs Junction Temperature
![img-13.jpeg](img-13.jpeg)

Figure 8-8. $\mathrm{V}_{\text {IN }}$ UVLO Rising Threshold vs Junction Temperature
![img-14.jpeg](img-14.jpeg)

Figure 8-10. Switching Frequency (RT Floating) vs Junction Temperature
![img-15.jpeg](img-15.jpeg)

Figure 8-12. TPS62933 Low-Side Current Limit vs Junction Temperature# 8.6 Typical Characteristics (continued) 

$\mathrm{T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}$ to $150^{\circ} \mathrm{C}, \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}$, unless otherwise noted.
![img-16.jpeg](img-16.jpeg)

Figure 8-13. TPS62932 High-Side Current Limit vs Junction Temperature
![img-17.jpeg](img-17.jpeg)

Figure 8-15. OVP Threshold vs Junction Temperature
![img-18.jpeg](img-18.jpeg)

Figure 8-17. Soft-Start Charge Current vs Junction Temperature
![img-19.jpeg](img-19.jpeg)

Figure 8-14. TPS62932 Low-Side Current Limit vs Junction Temperature
![img-20.jpeg](img-20.jpeg)

Figure 8-16. UVP Threshold vs Junction Temperature
![img-21.jpeg](img-21.jpeg)

Figure 8-18. TPS62933 Efficiency, $\mathrm{V}_{\text {OUT }}=3.3 \mathrm{~V}$, $f_{5 W}=500 \mathrm{kHz}, \mathrm{L}=4.7 \mu \mathrm{H}$# 8.6 Typical Characteristics (continued) 

$T_{J}=-40^{\circ} \mathrm{C}$ to $150^{\circ} \mathrm{C}, \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}$, unless otherwise noted.
![img-22.jpeg](img-22.jpeg)

Figure 8-19. TPS62933 Efficiency, $\mathrm{V}_{\text {OUT }}=3.3 \mathrm{~V}$, $f_{S W}=1200 \mathrm{kHz}, \mathrm{L}=2.2 \mu \mathrm{H}$
![img-23.jpeg](img-23.jpeg)

Figure 8-21. TPS62932 Efficiency, $\mathrm{V}_{\text {OUT }}=5 \mathrm{~V}$, $f_{S W}=500 \mathrm{kHz}, \mathrm{L}=10 \mu \mathrm{H}$
![img-24.jpeg](img-24.jpeg)

Figure 8-23. TPS62933O Efficiency, $\mathrm{V}_{\text {OUT }}=5 \mathrm{~V}$, $f_{S W}=500 \mathrm{kHz}, \mathrm{L}=6.8 \mu \mathrm{H}$
![img-25.jpeg](img-25.jpeg)

Figure 8-20. TPS62933 Efficiency, $\mathrm{V}_{\text {OUT }}=12 \mathrm{~V}$, $f_{S W}=500 \mathrm{kHz}, \mathrm{L}=12 \mu \mathrm{H}$
![img-26.jpeg](img-26.jpeg)

Figure 8-22. TPS62933F Efficiency, $\mathrm{V}_{\text {OUT }}=5 \mathrm{~V}$, $f_{S W}=500 \mathrm{kHz}, \mathrm{L}=6.8 \mu \mathrm{H}$
![img-27.jpeg](img-27.jpeg)

Figure 8-24. TPS62933 Load Regulation, $\mathrm{V}_{\text {OUT }}=3.3 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$# 8.6 Typical Characteristics (continued) 

$\mathrm{T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}$ to $150^{\circ} \mathrm{C}, \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}$, unless otherwise noted.
![img-28.jpeg](img-28.jpeg)

Figure 8-25. TPS62933 Load Regulation, $\mathrm{V}_{\text {OUT }}=3.3 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=1200 \mathrm{kHz}$
![img-29.jpeg](img-29.jpeg)

Figure 8-27. TPS62932 Load Regulation, $\mathrm{V}_{\text {OUT }}=5 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$
![img-30.jpeg](img-30.jpeg)
![img-31.jpeg](img-31.jpeg)

Figure 8-26. TPS62933 Load Regulation, $\mathrm{V}_{\text {OUT }}=12 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$
![img-32.jpeg](img-32.jpeg)

Figure 8-28. TPS62933F Load Regulation, $\mathrm{V}_{\text {OUT }}=5 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$
![img-33.jpeg](img-33.jpeg)# 8.6 Typical Characteristics (continued) 

$T_{J}=-40^{\circ} \mathrm{C}$ to $150^{\circ} \mathrm{C}, \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}$, unless otherwise noted.
![img-34.jpeg](img-34.jpeg)

Figure 8-31. TPS62933 Line Regulation, $\mathrm{V}_{\text {OUT }}=12 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$
![img-35.jpeg](img-35.jpeg)

Figure 8-33. TPS62933F Line Regulation, $\mathrm{V}_{\text {OUT }}=5 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$
![img-36.jpeg](img-36.jpeg)

Figure 8-35. TPS62933 Switching Frequency vs Load Current, $\mathrm{V}_{\text {OUT }}=3.3 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$ (RT Floating)
![img-37.jpeg](img-37.jpeg)# 8.6 Typical Characteristics (continued) 

$\mathrm{T}_{\mathrm{J}}=-40^{\circ} \mathrm{C}$ to $150^{\circ} \mathrm{C}, \mathrm{V}_{\mathrm{IN}}=12 \mathrm{~V}$, unless otherwise noted.
![img-38.jpeg](img-38.jpeg)

Figure 8-37. TPS62933 Switching Frequency vs $V_{\text {IN }}, V_{\text {OUT }}=3.3 \mathrm{~V}, I_{\text {OUT }}=3 \mathrm{~A}$# 9 Detailed Description 

### 9.1 Overview

The TPS62932 and TPS62933x are a 30-V, 2-A and 3-A, synchronous buck (step-down) converters with two integrated n-channel MOSFETs. They employ fixed-frequency peak current control mode for fast transient response and good line and load regulation. With the optimized internal loop compensation, the devices eliminate the external compensation components over a wide range of output voltage and switching frequency.
The integrated $76-\mathrm{m} \Omega$ and $32-\mathrm{m} \Omega$ MOSFETs allow for high-efficiency power supply designs with continuous output currents up to 2 A (TPS62932) or 3 A (TPS62933 and TPS62933x). The feedback reference voltage is designed at 0.8 V . The output voltage can be stepped down from 0.8 V to 22 V . The devices are ideally suited for systems powered from $5-\mathrm{V}, 12-\mathrm{V}, 19-\mathrm{V}$, and $24-\mathrm{V}$ power-bus rails.
The TPS6293x has been designed for safe monotonic start-up into prebiased loads. The default start-up is at $\mathrm{V}_{\mathrm{IN}}$ equal to 3.8 V . After the device is enabled, the output rises smoothly from 0 V to its regulated voltage. The TPS6293x has low operating current when not switching under no load, especially the TPS62932, TPS62933, and TPS62933P whose operating current is $12 \mu \mathrm{~A}$ (typical). When the TPS6293x is disabled, the supply current is approximately $2 \mu \mathrm{~A}$ (typical). These features are extremely beneficial for long battery life time in low-power operation.

Pulse frequency modulation (PFM) mode allows the TPS62932, TPS62933, and TPS62933P to maximize the light-load efficiency. Continuous current mode allows the TPS62933F to have low output ripple in all load conditions. The TPS62933O operates in out of audio mode which can avoid the audible noise.
The EN pin has an internal pullup current that can be used to adjust the input voltage undervoltage lockout (UVLO) with two external resistors. In addition, the EN pin can be floating for the device to operate with the internal pullup current.
The switching frequency can be set by the configuration of the RT pin in the range of 200 kHz to 2.2 MHz , which allows for efficiency and solution size optimization when selecting the output filter components. The TPS62932, TPS62933, TPS62933P, and TPS62933O also have a frequency spread spectrum feature, which helps with lowering down EMI noise.
A small value capacitor or resistor divider is connected to the SS pin of the TPS62932, TPS62933, and TPS62933F for soft-start time setting or voltage tracking. The TPS62933P and TPS62933O indicate power good through PG pin.
The devices have the on-time extension function with a maximum on time of $7 \mu \mathrm{~s}$ (typical). During low dropout operation, the high-side MOSFET can turn on up to $7 \mu \mathrm{~s}$, then the high-side MOSFET turns off and the low-side MOSFET turns on with a minimum off time of 140 ns (typical). The devices support the maximum $98 \%$ duty cycle.

The devices reduce the external component count by integrating the bootstrap circuit. The bias voltage for the integrated high-side MOSFET is supplied by a capacitor between the BST and SW pins. A UVLO circuit monitors the bootstrap capacitor voltage, $\mathrm{V}_{\text {BST-SW }}$. When it falls below a preset threshold of 2.5 V (typical), the SW pin is pulled low to recharge the bootstrap capacitor.
Cycle-by-cycle current limiting on the high-side MOSFET protects the device in overload situations and is enhanced by a low-side sourcing current limit, which prevents current runaway. The TPS6293x provides output undervoltage protection (UVP) when the regulated output voltage is lower than $65 \%$ of the nominal voltage due to overcurrent being triggered, approximately $256-\mu \mathrm{s}$ (typical) deglitch time later, both the high-side and low-side MOSFET turn off, the device steps into hiccup mode.
The devices minimize excessive output overvoltage transient by taking advantage of the overvoltage comparator. When the regulated output voltage is greater than $115 \%$ of the nominal voltage, the overvoltage comparator is activated, and the high-side MOSFET is turned off and masked from turning on until the output voltage is lower than $110 \%$.
Thermal shutdown disables the devices when the die temperature, $\mathrm{T}_{\mathrm{J}}$, exceeds $165^{\circ} \mathrm{C}$ and enables the devices again after $T_{J}$ decreases below the hysteresis amount of $30^{\circ} \mathrm{C}$.# 9.2 Functional Block Diagram 

![img-39.jpeg](img-39.jpeg)# 9.3 Feature Description 

### 9.3.1 Fixed Frequency Peak Current Mode

The following operation description of the TPS6293x refers to the functional block diagram and to the waveforms in Figure 9-1. The TPS6293x is a synchronous buck converter with integrated high-side (HS) and low-side (LS) MOSFETs (synchronous rectifier). The TPS6293x supplies a regulated output voltage by turning on the HS and LS NMOS switches with controlled duty cycle. During high-side switch on time, the SW pin voltage swings up to approximately $\mathrm{V}_{\mathrm{IN}}$, and the inductor current, $\mathrm{i}_{\mathrm{L}}$, increases with linear slope ( $\mathrm{V}_{\mathrm{IN}}-\mathrm{V}_{\text {OUT }}$ ) / L. When the HS switch is turned off by the control logic, the LS switch is turned on after an anti-shoot-through dead time. Inductor current discharges through the low-side switch with a slope of $-V_{\text {OUT }} / \mathrm{L}$. The control parameter of a buck converter is defined as Duty Cycle $D=t_{O N} / t_{S W}$, where $t_{O N}$ is the high-side switch on time and $t_{S W}$ is the switching period. The converter control loop maintains a constant output voltage by adjusting the duty cycle D. In an ideal buck converter where losses are ignored, D is proportional to the output voltage and inversely proportional to the input voltage: $D=V_{\text {OUT }} / V_{\text {IN }}$.
![img-40.jpeg](img-40.jpeg)

Figure 9-1. SW Node and Inductor Current Waveforms in Continuous Conduction Mode (CCM)
The TPS6293x employs the fixed-frequency peak current mode control. A voltage feedback loop is used to get accurate DC voltage regulation by adjusting the peak current command based on voltage offset. The peak inductor current is sensed from the HS switch and compared to the peak current threshold to control the on time of the HS switch. The voltage feedback loop is internally compensated, which allows for fewer external components, makes it easy to design, and provides stable operation with almost any combination of output capacitors.

### 9.3.2 Pulse Frequency Modulation

The TPS62932, TPS62933, and TPS62933P are designed to operate in pulse frequency modulation (PFM) mode at light load currents to boost light load efficiency.

When the load current is lower than half of the peak-to-peak inductor current in CCM, the devices operate in discontinuous conduction mode (DCM). In DCM operation, the low-side switch is turned off when the inductor current drops to $\mathrm{I}_{\mathrm{LS} \_\mathrm{ZC}}$ to improve efficiency. Both switching losses and conduction losses are reduced in DCM, compared to forced CCM operation at light load.

At even lighter current load, pulse frequency modulation (PFM) mode is activated to maintain high-efficiency operation. When either the minimum high-side switch on time, $\mathrm{t}_{\mathrm{ON} \text { MIN }}$, or the minimum peak inductor current $\mathrm{I}_{\text {PEAK_MIN }}$ is reached, the switching frequency decreases to maintain regulation. In PFM mode, the switching frequency is decreased by the control loop to maintain output voltage regulation when load current reduces.Switching loss is further reduced in PFM operation due to less frequent switching actions. Since the integrated current comparator catches the peak inductor current only, the average load current entering PFM mode varies with the applications and external output LC filters.

In PFM mode, the high-side MOSFET is turned on in a burst of one or more pulses to provide energy to the load. The duration of the burst depends on how long it takes the feedback voltage catches $\mathrm{V}_{\text {REF }}$. The periodicity of these bursts is adjusted to regulate the output, while zero current crossing detection turns off the low-side MOSFET to maximize efficiency. This mode provides high light-load efficiency by reducing the amount of input supply current required to regulate the output voltage at small loads. This trades off very good light-load efficiency for larger output voltage ripple and variable switching frequency.

# 9.3.3 Voltage Reference 

The internal reference voltage, $\mathrm{V}_{\mathrm{REF}}$, is designed at 0.8 V (typical). The negative feedback system of converter produces a precise $\pm 2 \%$ feedback voltage, $\mathrm{V}_{\mathrm{FB}}$, over full temperature by scaling the output of a temperaturestable internal band-gap circuit.

### 9.3.4 Output Voltage Setting

A precision $0.8-\mathrm{V}$ reference voltage, $\mathrm{V}_{\text {REF }}$, is used to maintain a tightly regulated output voltage over the entire operating temperature range. The output voltage is set by a resistor divider from the output voltage to the FB pin. TI recommends using $1 \%$ tolerance resistors with a low temperature coefficient for the FB divider. Select the bottom-side resistor, $\mathrm{R}_{\text {FBB }}$, for the desired divider current and use Equation 1 to calculate the top-side resistor, $R_{F B T}$. Lower $R_{F B B}$ increases the divider current and reduces efficiency at very light load. Larger $R_{F B B}$ makes the FB voltage more susceptible to noise, so larger $R_{F B B}$ values require a more carefully designed feedback path on the PCB. Setting $R_{F B B}=10 \mathrm{k} \Omega$ and $R_{F B T}$ in the range of $10 \mathrm{k} \Omega$ to $300 \mathrm{k} \Omega$ is recommended for most applications.
The tolerance and temperature variation of the resistor dividers affect the output voltage regulation.
![img-41.jpeg](img-41.jpeg)

Figure 9-2. Output Voltage Setting

$$
R_{\text {FBT }}=\frac{V_{\text {OUT }}-\mathrm{V}_{\text {REF }}}{\mathrm{V}_{\text {REF }}} \times \mathrm{R}_{\text {FBB }}
$$

where

- $\mathrm{V}_{\text {REF }}$ is the 0.8 V (the internal reference voltage).
- $R_{\text {FBB }}$ is $10 \mathrm{k} \Omega$ (recommended).


### 9.3.5 Switching Frequency Selection

The switching frequency is set by the condition of the RT input. The condition of this input is detected when the device is first enabled. Once the converter is running, the switching frequency selection is fixed and cannot be changed until the next power-on cycle or EN toggle. Table 9-1 shows the selection programming. In adjustable frequency mode, the switching frequency can be set between 200 kHz and 2200 kHz by proper selection of RT resistor. See Equation 2.$$
\mathrm{f}_{\mathrm{SW}}(\mathrm{kHz})=17293 \times \mathrm{RT}(\mathrm{k} \Omega)^{-0.942}
$$

where

- RT is the value of RT timing resistor in $\mathrm{k} \Omega$.
- $\mathrm{f}_{\mathrm{SW}}$ is the switching frequency in kHz .

Table 9-1. RT Pin Resistor Settings

| RT Pin | Resistance | Switching Frequency |
| :--: | :--: | :--: |
| Floating | $>280 \mathrm{k} \Omega$ | 500 kHz |
| GND | $<1 \mathrm{k} \Omega$ | 1200 kHz |
| RT to GND | $8.9 \mathrm{k} \Omega$ to $111 \mathrm{k} \Omega$ | 200 kHz to 2200 kHz |

Figure 9-3 indicates the required resistor value for RT to set a desired switching frequency.
![img-42.jpeg](img-42.jpeg)

Figure 9-3. Switching Frequency vs $\mathbf{R}_{\mathbf{T}}$
There are four cases where the switching frequency does not conform to the condition set by the RT pin:

- Light load operation (PFM mode)
- Low dropout operation
- Minimum on-time operation
- Current limit tripped

Under all of these cases, the switching frequency folds back, meaning it is less than that programmed by the RT pin. During these conditions, the output voltage remains in regulation, except for current limit operation.

# 9.3.6 Enable and Adjusting Undervoltage Lockout 

The EN pin provides electrical ON and OFF control of the device. When the EN pin voltage exceeds the enable threshold voltage, $\mathrm{V}_{\text {EN_RISE }}$, the TPS6293x begins operation. If the EN pin voltage is pulled below the disable threshold voltage, $\mathrm{V}_{\text {EN_FALL }}$, the converter stops switching and enters shutdown mode.
The EN pin has an internal pullup current source, which allows the user to float the EN pin to enable the device. If an application requires control of the EN pin, use an open-drain or open-collector or GPIO output logic to interface with the pin.

The TPS6293x implements internal undervoltage-lockout (UVLO) circuitry on the VIN pin. The device is disabled when the VIN pin voltage falls below the internal $\mathrm{V}_{\mathrm{IN} \text { UVLO }}$ threshold. The internal $\mathrm{V}_{\mathrm{IN} \text { UVLO }}$ threshold has a hysteresis of typical 300 mV . If an application requires a higher UVLO threshold on the VIN pin, the EN pin canbe configured as shown in Figure 9-4. When using the external UVLO function, setting the hysteresis at a value greater than 500 mV is recommended.

The EN pin has a small pullup current, $\mathrm{I}_{\mathrm{p}}$, which sets the default state of the EN pin to enable when no external components are connected. The pullup hysteresis current, $\mathrm{I}_{\mathrm{h}}$, is used to control the hysteresis voltage for the UVLO function when the EN pin voltage crosses the enable threshold. Use Equation 3 and Equation 4 to calculate the values of R1 and R2 for a specified UVLO threshold. Once R1 and R2 are settled down, $\mathrm{V}_{\mathrm{EN}}$ can be calculated by Equation 5, which must be lower than 5.5 V with the maximum $\mathrm{V}_{\mathrm{IN}}$.
![img-43.jpeg](img-43.jpeg)

Figure 9-4. Adjustable $\mathrm{V}_{\text {IN }}$ Undervoltage Lockout

$$
\begin{aligned}
& R_{1}=\frac{V_{\text {START }} \times \frac{V_{\text {EN_FALL }}}{V_{\text {EN_RISE }}}-V_{\text {STOP }}}{I_{p} \times\left(1-\frac{V_{\text {EN FALL }}}{V_{\text {EN_RISE }}}\right)+I_{h}} \\
& R_{2}=\frac{R_{1} \times V_{\text {EN FALL }}}{V_{\text {STOP }}-V_{\text {EN FALL }}+R_{1} \times\left(I_{p}+I_{h}\right)} \\
& V_{\mathrm{EN}}=\frac{R_{2} \times V_{\mathrm{IN}}+R_{1} \times R_{2} \times\left(I_{p}+I_{h}\right)}{R_{1}+R_{2}}
\end{aligned}
$$

where

- $\mathrm{I}_{\mathrm{p}}$ is $0.7 \mu \mathrm{~A}$.
- $\mathrm{I}_{\mathrm{h}}$ is $1.4 \mu \mathrm{~A}$.
- $\mathrm{V}_{\text {EN FALL }}$ is 1.17 V .
- $\mathrm{V}_{\text {EN RIISE }}$ is 1.21 V .
- $\mathrm{V}_{\text {START }}$ is the input voltage enabling the device.
- $\mathrm{V}_{\text {STOP }}$ is the input voltage disabling the device.


# 9.3.7 External Soft Start and Prebiased Soft Start 

The SS pin of TPS62932, TPS62933, and TPS62933F are used to minimize inrush current when driving capacitive load. The devices use the lower voltage of the internal voltage reference, $\mathrm{V}_{\text {REF }}$, or the SS pin voltage as the reference voltage and regulates the output accordingly. A capacitor on the SS pin to ground implements a soft-start time. The device has an internal pullup current source that charges the external soft-start capacitor. Use Equation 6 to calculate the soft-start time ( $\mathrm{t}_{\mathrm{SS}}, 0 \%$ to 100\%) and soft-start capacitor ( $\mathrm{C}_{\mathrm{SS}}$ ).$$
\mathrm{t}_{\mathrm{SS}}=\frac{\mathrm{C}_{\mathrm{SS}} \times \mathrm{V}_{\mathrm{REF}}}{\mathrm{I}_{\mathrm{SS}}}
$$

where

- $\mathrm{V}_{\text {REF }}$ is 0.8 V (the internal reference voltage).
- $\mathrm{I}_{\mathrm{SS}}$ is $5.5 \mu \mathrm{~A}$ (typical), the internal pullup current.

If the output capacitor is prebiased at start-up, the devices initiate switching and start ramping up only after the internal reference voltage becomes greater than the feedback voltage, $\mathrm{V}_{\mathrm{FB}}$. This scheme makes sure that the converters ramp up smoothly into regulation point.

A resistor divider connected to the SS pin can implement voltage tracking of the other power rail.

# 9.3.8 Power Good 

The TPS62933P and TPS62933O have a built-in power good (PG) function to indicate whether the output voltage has reached its appropriate level or not. The PG signal can be used for start-up sequencing of multiple rails. The PG pin is an open-drain output that requires a pullup resistor to any voltage below 5.5 V . TI recommends a pullup resistor of $10 \mathrm{k} \Omega-100 \mathrm{k} \Omega$. The device can sink approximately 4 mA of current and maintain its specified logic low level. After the FB pin voltage is between $90 \%$ and $110 \%$ of the internal reference voltage ( $\mathrm{V}_{\text {REF }}$ ) and after a deglitch time of $70 \mu \mathrm{~s}$, the PG turns to high impedance status. The PG pin is pulled low after a deglitch time of $18 \mu \mathrm{~s}$ when FB pin voltage is lower than $85 \%$ of the internal reference voltage or greater than $115 \%$ of the internal reference voltage, or in events of thermal shutdown, EN shutdown, or UVLO conditions. VIN must remain present for the PG pin to stay low.

Table 9-2. PG Status

| Device State |  | PG Logic Status |  |
| :--: | :--: | :--: | :--: |
|  |  | High Impedance | Low |
| Enable (EN = High) | $\mathrm{V}_{\text {FB }}$ does not trigger $\mathrm{V}_{\text {PGTH }}$ | $\checkmark$ |  |
|  | $\mathrm{V}_{\text {FB }}$ triggers $\mathrm{V}_{\text {PGTH }}$ |  | $\checkmark$ |
| Shutdown (EN = Low) |  |  | $\checkmark$ |
| UVLO | $2.5 \mathrm{~V}<\mathrm{V}_{\text {IN }}<\mathrm{V}_{\text {UVLO }}$ |  | $\checkmark$ |
| Thermal shutdown | $\mathrm{T}_{\mathrm{J}}>\mathrm{T}_{\mathrm{SD}}$ |  | $\checkmark$ |
| Power supply removal | $\mathrm{V}_{\text {IN }}<2.5 \mathrm{~V}$ | $\checkmark$ |  |

### 9.3.9 Minimum On Time, Minimum Off Time, and Frequency Foldback

Minimum on time ( $\mathrm{t}_{\mathrm{ON} \_ \text {MIN }}$ ) is the smallest duration of time that the high-side switch can be on. $\mathrm{t}_{\mathrm{ON} \_ \text {MIN }}$ is typically 70 ns in the TPS6293x. Minimum off time ( $\mathrm{t}_{\text {OFF_MIN }}$ ) is the smallest duration that the high-side switch can be off. $\mathrm{t}_{\text {OFF_MIN }}$ is typically 140 ns . In CCM operation, $\mathrm{t}_{\mathrm{ON} \_ \text {MIN }}$, and $\mathrm{t}_{\text {OFF_MIN }}$, limit the voltage conversion range without switching frequency foldback.

The minimum duty cycle without frequency foldback allowed is:

$$
\mathrm{D}_{\mathrm{MIN}}=\mathrm{t}_{\mathrm{ON} \_\mathrm{MIN}} \times \mathrm{f}_{\mathrm{SW}}
$$

The maximum duty cycle without frequency foldback allowed is:

$$
\mathrm{D}_{\mathrm{MAX}}=1-\mathrm{t}_{\mathrm{OFF} \_\mathrm{MIN}} \times \mathrm{f}_{\mathrm{SW}}
$$

Given a required output voltage, the maximum $\mathrm{V}_{\text {IN }}$ without frequency foldback is:

$$
\mathrm{V}_{\mathrm{IN} \_\mathrm{MAX}}=\frac{\mathrm{V}_{\mathrm{OUT}}}{\mathrm{f}_{\mathrm{SW}} \times \mathrm{t}_{\mathrm{ON} \_\mathrm{MIN}}}
$$The minimum $\mathrm{V}_{\text {IN }}$ without frequency foldback is:

$$
\mathrm{V}_{\mathrm{IN} \_ \text {MIN }}=\frac{\mathrm{V}_{\mathrm{OUT}}}{1-\mathrm{f}_{\mathrm{SW}} \times \mathrm{t}_{\mathrm{OFF} \_\mathrm{MIN}}}
$$

In TPS6293x, a frequency foldback scheme is employed once $t_{\text {ON_MIN }}$ or $t_{\text {OFF_MIN }}$ is triggered, which can extend the maximum duty cycle or lower the minimum duty cycle.
The on time decreases while $\mathrm{V}_{\mathrm{IN}}$ voltage increases. Once the on time decreases to $t_{\text {ON_MIN }}$, the switching frequency starts to decrease while $\mathrm{V}_{\mathrm{IN}}$ continues to go up, which lowers the duty cycle further to keep $\mathrm{V}_{\mathrm{OUT}}$ in regulation according to Equation 7.

The frequency foldback scheme also works once larger duty cycle is needed under low $\mathrm{V}_{\mathrm{IN}}$ condition. The frequency decreases once the device hits its $t_{\text {OFF_MIN }}$, which extends the maximum duty cycle according to Equation 8. A wide range of frequency foldback allows the TPS6293x output voltage to stay in regulation with a much lower supply voltage $\mathrm{V}_{\mathrm{IN}}$, which allows a lower effective dropout.
With frequency foldback, $\mathrm{V}_{\mathrm{IN} \_\mathrm{MAX}}$ is raised, and $\mathrm{V}_{\mathrm{IN} \_\mathrm{MIN}}$ is lowered by decreased $\mathrm{f}_{\mathrm{SW}}$.
![img-44.jpeg](img-44.jpeg)

Figure 9-5. Frequency Foldback at $\mathrm{t}_{\mathrm{ON} \_\mathrm{MIN}}$, $\mathrm{V}_{\mathrm{OUT}}=1.8 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=1200 \mathrm{kHz}$
![img-45.jpeg](img-45.jpeg)

Figure 9-6. Frequency Foldback at $\mathrm{t}_{\mathrm{OFF} \_\mathrm{MIN}}$, $\mathrm{V}_{\mathrm{OUT}}=5 \mathrm{~V}, \mathrm{f}_{\mathrm{SW}}=1200 \mathrm{kHz}$

# 9.3.10 Frequency Spread Spectrum 

To reduce EMI, the TPS62932, TPS62933, TPS62933P, and TPS62933O introduce frequency spread spectrum. The jittering span is typically $\Delta \mathrm{fc}= \pm 6 \%$ of the switching frequency with the modulation frequency of $\mathrm{f}_{\mathrm{m}}=$ $\mathrm{f}_{\mathrm{SW}} / 128$. The purpose of spread spectrum is to eliminate peak emissions at specific frequencies by spreading emissions across a wider range of frequencies than a part with fixed frequency operation. Figure 9-7 shows the frequency spread spectrum modulation. Figure 9-8 shows the energy is spread out at the center frequency, $\mathrm{f}_{\mathrm{c}}$.![img-46.jpeg](img-46.jpeg)

Figure 9-7. Frequency Spread Spectrum Diagram
![img-47.jpeg](img-47.jpeg)

Figure 9-8. Energy vs Frequency

# 9.3.11 Overvoltage Protection 

The device incorporates an output overvoltage protection (OVP) circuit to minimize output voltage overshoot. The OVP feature minimizes the overshoot by comparing the FB pin voltage to the OVP threshold. If the FB pin voltage is greater than the OVP threshold of $115 \%$, the high-side MOSFET is turned off, which prevents current from flowing to the output and minimizes output overshoot. When the FB pin voltage drops lower than the OVP threshold minus hysteresis, the high-side MOSFET is allowed to turn on at the next clock cycle. This function is non-latch operation.

### 9.3.12 Overcurrent and Undervoltage Protection

The TPS6293x incorporates both peak and valley inductor current limits to provide protection to the device from overloads and short circuits and limit the maximum output current. Valley current limit prevents inductor current run-away during short circuits on the output, while both peak and valley limits work together to limit the maximum output current of the converter. Hiccup mode is also incorporated for sustained short circuits.
The high-side switch current is sensed when it is turned on after a set blanking time ( $t_{\text {ON_MIN }}$ ), the peak current of high-side switch is limited by the peak current threshold, $\mathrm{I}_{\text {HS_LIMIT }}$. The current going through low-side switch is also sensed and monitored. When the low-side switch turns on, the inductor current begins to ramp down.

As the device is overloaded, a point is reached where the valley of the inductor current cannot reach below $\mathrm{I}_{\mathrm{LS} \_\mathrm{LIMIT}}$ before the next clock cycle, then the low-side switch is kept on until the inductor current ramps belowthe valley current threshold, $\mathrm{I}_{\mathrm{LS} \_}$LIMIT, then the low-side switch is turned off and the high-side switch is turned on after a dead time. When this occurs, the valley current limit control skips that cycle, causing the switching frequency to drop. Further overload causes the switching frequency to continue to drop, but the output voltage remains in regulation. As the overload is increased, both the inductor current ripple and peak current increase until the high-side current limit, $\mathrm{I}_{\text {HS }}$ LIIIIT, is reached. When this limit is tripped, the switch duty cycle is reduced and the output voltage falls out of regulation. This represents the maximum output current from the converter and is given approximately by Equation 11. The output voltage and switching frequency continue to drop as the device moves deeper into overload while the output current remains at approximately $\mathrm{I}_{\text {OMAX }}$. There is another situation, if the inductor ripple current is large, the high-side current limit can be tripped before the low-side limit is reached. In this case, Equation 12 gives the approximate maximum output current.

$$
\begin{aligned}
& \mathrm{I}_{\text {OMAX }} \approx \frac{\mathrm{I}_{\text {HS_LIMIT }}+\mathrm{I}_{\text {LS_LIMIT }}}{2} \\
& \mathrm{I}_{\text {OMAX }} \approx \mathrm{I}_{\text {HS_LIMIT }}-\frac{\left(\mathrm{V}_{\mathrm{IN}}-\mathrm{V}_{\text {OUT }}\right)}{2 \times \mathrm{L} \times \mathrm{f}_{\mathrm{SW}}} \times \frac{\mathrm{V}_{\text {OUT }}}{\mathrm{V}_{\mathrm{IN}}}
\end{aligned}
$$

Furthermore, if a severe overload or short circuit causes the FB voltage to fall below the $\mathrm{V}_{\text {UVP }}$ threshold, $65 \%$ of the $\mathrm{V}_{\text {REF }}$, and triggering current limit, and the condition occurs for more than the hiccup on time (typical $256 \mu \mathrm{~s}$ ), the converter enters hiccup mode. In this mode, the device stops switching for hiccup off time, 10.5 $\times \mathrm{t}_{\mathrm{SS}}$, and then goes to a normal restart with soft-start time. If the overload or short-circuit condition remains, the device runs in current limit and then shuts down again. This cycle repeats as long as the overload or short-circuit condition persists. This mode of operation reduces the temperature rise of the device during a sustained overload or short circuit condition on the output. Once the output short is removed, the output voltage recovers normally to the regulated value.
For FCCM version, the inductor current is allowed to go negative. When this current exceed the LS negative current limit $\mathrm{I}_{\mathrm{LS} \_ \text {NEG }}$, the LS switch is turned off and HS switch is turned on immediately, which is used to protect the LS switch from excessive negative current.

# 9.3.13 Thermal Shutdown 

The junction temperature $\left(T_{J}\right)$ of the device is monitored by an internal temperature sensor. If $T_{J}$ exceeds $165^{\circ} \mathrm{C}$ (typical), the device goes into thermal shutdown, both the high-side and low-side power FETs are turned off. When $T_{J}$ decreases below the hysteresis amount of $30^{\circ} \mathrm{C}$ (typical), the converter resumes normal operation, beginning with a soft start.# 9.4 Device Functional Modes 

### 9.4.1 Modes Overview

The TPS6293x moves between CCM, DCM, PFM, OOA and FCCM mode as the load changes. Depending on the load current, the TPS6293x is in one of below modes:

- Continuous conduction mode (CCM) with fixed switching frequency when load current is above half of the peak-to-peak inductor current ripple
- Discontinuous conduction mode (DCM) with fixed switching frequency when load current is lower than half of the peak-to-peak inductor current ripple in CCM operation
- Pulse frequency modulation mode (PFM) when switching frequency is decreased at very light load
- Out of audio (OOA) mode when switching frequency is decreased but is always above 30 kHz at very light load
- Forced continuous conduction mode (FCCM) with fixed switching frequency even at light load


### 9.4.2 Heavy Load Operation

The TPS6293x operates in continuous conduction mode (CCM) when the load current is higher than half of the peak-to-peak inductor current. In CCM operation, the output voltage is regulated by switching at a constant frequency and modulating the duty cycle to control the power to the load. Regulating the output voltage provides excellent line and load regulation and minimum output voltage ripple, and the maximum continuous output current of 2 A or 3 A can be supplied by the TPS6293x.

### 9.4.3 Light Load Operation

The TPS62932, TPS62933, and TPS62933P are designed to operate in pulse frequency modulation (PFM) mode at light load currents to boost light load efficiency.
When the load current is lower than half of the peak-to-peak inductor current in CCM, the device operates in discontinuous conduction mode (DCM), also known as diode emulation mode (DEM). In DCM operation, the LS switch is turned off when the inductor current drops to $\mathrm{I}_{\mathrm{LS}, 2 \mathrm{C}}$ to improve efficiency. Both switching losses and conduction losses are reduced in DCM, compared to forced CCM operation at light load.
At even lighter current load, pulse frequency modulation (PFM) mode is activated to maintain high efficiency operation. When either the minimum on time, $\mathrm{t}_{\mathrm{ON} \text { MIN }}$, or the minimum peak inductor current, $\mathrm{I}_{\text {PEAK MIN }}$ ( 750 mA typical), is reached, the switching frequency decreases to maintain regulation. In PFM mode, switching frequency is decreased by the control loop to maintain output voltage regulation when load current reduces. Switching loss is further reduced in PFM operation due to less frequent switching actions. The output current for mode change depends on the input voltage, inductor value, and the programmed switching frequency. For applications where the switching frequency must be known for a given condition, the transition between PFM and CCM must be carefully tested before the design is finalized.

### 9.4.4 Out of Audio Operation

TPS62933O implements the out of audio (OOA) mode which is a unique control feature that keeps the switching frequency above audible frequency ( 20 Hz to 20 kHz ) even at no load condition. When operates in OOA mode, the minimum switching frequency is clamped above 30 kHz which avoids the audible noise in the system. The loading to enter OOA mode depends on output LC filter.

### 9.4.5 Forced Continuous Conduction Operation

The TPS62933F is designed to operate in forced continuous conduction mode (FCCM) under light load conditions. During FCCM, the switching frequency is maintained at a constant level over the entire load range, which is suitable for applications requiring tight control of the switching frequency and output voltage ripple at the cost of lower efficiency under light load. For some audio applications, this mode can help avoid switching frequency drop into audible range that can introduce some noise.

### 9.4.6 Dropout Operation

The dropout performance of any buck converter is affected by the $R_{\text {DSON }}$ of the power MOSFETs, the DC resistance of the inductor, and the maximum duty cycle that the controller can achieve. As the input voltage levelapproaches the output voltage, the off time of the high-side MOSFET starts to approach the minimum value. Beyond this point, the switching frequency becomes erratic and the output voltage can fall out of regulation. To avoid this problem, the TPS6293x automatically reduces the switching frequency (on-time extension function) to increase the effective duty cycle and maintain in regulation until the switching frequency reach to the lowest limit of about 140 kHz , the period is equal to $\mathrm{t}_{\mathrm{ON} \_ \text {MAX }}+\mathrm{t}_{\text {OFF_MIN }} \text { (7.14 } \mu \mathrm{S}$ typical). In this condition, the difference voltage between $\mathrm{V}_{\mathrm{IN}}$ and $\mathrm{V}_{\text {OUT }}$ is defined as dropout voltage. The typical overall dropout characteristics can be found as Figure 9-9.
![img-48.jpeg](img-48.jpeg)

Figure 9-9. Overall Dropout Characteristic, $\mathrm{V}_{\text {OUT }}=\mathbf{5} \mathrm{V}$

# 9.4.7 Minimum On-Time Operation 

Every switching converter has a minimum controllable on time dictated by the inherent delays and blanking times associated with the control circuits, which imposes a minimum switch duty cycle and, therefore, a minimum conversion ratio. The constraint is encountered at high input voltages and low output voltages. To help extend the minimum controllable duty cycle, the TPS6293x automatically reduces the switching frequency when the minimum on-time limit is reached. This way, the converter can regulate the lowest programmable output voltage at the maximum input voltage. Use Equation 13 to find an estimate for the approximate input voltage for a given output voltage before frequency foldback occurs. The values of $t_{O N \_M I N}$ and $f_{S W}$ can be found in Section 8.5.

$$
\mathrm{V}_{\mathrm{IN}} \leq \frac{\mathrm{V}_{\mathrm{OUT}}}{\mathrm{t}_{\mathrm{ON} \_\mathrm{MIN}} \times \mathrm{f}_{\mathrm{SW}}}
$$

As the input voltage is increased, the switch on time (duty-cycle) reduces to regulate the output voltage. When the on time reaches the minimum on time, $\mathrm{t}_{\mathrm{ON} \_\mathrm{MIN}}$, the switching frequency drops while the on time remains fixed.

### 9.4.8 Shutdown Mode

The EN pin provides electrical ON and OFF control for the device. When $\mathrm{V}_{\mathrm{EN}}$ is below typical 1.1 V , the TPS6293x is in shutdown mode. The device also employs VIN UVLO protection. If $\mathrm{V}_{\mathrm{IN}}$ voltage is below their respective UVLO level, the converter is turned off too.# 10 Application and Implementation 

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

### 10.1 Application Information

The TPS62933 is a highly integrated, synchronous, step-down, DC-DC converter. This device is used to convert a higher DC input voltage to a lower DC output voltage, with a maximum output current of 3 A .

### 10.2 Typical Application

The application schematic of Figure 10-1 was developed to meet the requirements of the device. This circuit is available as the TPS62933EVM evaluation module. The design procedure is given in this section.

Figure 10-1. TPS62933 5-V Output, 3-A Reference Design
![img-49.jpeg](img-49.jpeg)

### 10.2.1 Design Requirements

Table 10-1 shows the design parameters for this application.
Table 10-1. Design Parameters

| Parameter |  | Conditions | MIN | TYP | MAX | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\mathrm{V}_{\text {IN }}$ | Input voltage |  | 5.5 | 24 | 30 | V |
| $\mathrm{V}_{\text {OUT }}$ | Output voltage |  | 5 |  |  | V |
| $\mathrm{I}_{\text {OUT }}$ | Output current rating |  | 3 |  |  | A |
| $\Delta \mathrm{V}_{\text {OUT }}$ | Transient response | Load step from $0.5 \mathrm{~A} \rightarrow 2.5$ <br> $\mathrm{A} \rightarrow 0.5 \mathrm{~A}, 0.8-\mathrm{A} / \mu \mathrm{S}$ slew rate | $\begin{gathered} \pm 5 \% \times \\ V_{\text {OUT }} \end{gathered}$ |  |  | V |
| $\mathrm{V}_{\text {INripple) }}$ | Input ripple voltage |  | 400 |  |  | mV |
| $\mathrm{V}_{\text {OUTripple) }}$ | Output ripple voltage |  | 30 |  |  | mV |
| $\mathrm{F}_{\text {SW }}$ | Switching frequency | RT = floating | 500 |  |  | kHz |
| $\mathrm{t}_{\text {SS }}$ | Soft-start time | $\mathrm{C}_{\mathrm{SS}}=33 \mathrm{nF}$ | 5 |  |  | mS |
| $\mathrm{V}_{\text {START }}$ | Start input voltage (Rising $\mathrm{V}_{\text {IN }}$ ) |  | 8 |  |  | V |
| $\mathrm{V}_{\text {STOP }}$ | Stop input voltage (Falling $\mathrm{V}_{\text {IN }}$ ) |  | 7 |  |  | V |
| $T_{A}$ | Ambient temperature |  | 25 |  |  | ${ }^{\circ} \mathrm{C}$ |# 10.2.2 Detailed Design Procedure 

### 10.2.2.1 Custom Design With WEBENCH® Tools

Create a custom design with the TPS6293x using the WEBENCH ${ }^{\circledR}$ Power Designer.

1. Start by entering the input voltage $\left(V_{I N}\right)$, output voltage $\left(V_{\text {OUT }}\right)$, and output current $\left(I_{\text {OUT }}\right)$ requirements.
2. Optimize the design for key parameters such as efficiency, footprint, and cost using the optimizer dial.
3. Compare the generated design with other possible solutions from Texas Instruments.

The WEBENCH Power Designer provides a customized schematic along with a list of materials with real-time pricing and component availability.
In most cases, these actions are available:

- Run electrical simulations to see important waveforms and circuit performance
- Run thermal simulations to understand board thermal performance
- Export customized schematic and layout into popular CAD formats
- Print PDF reports for the design, and share the design with colleagues

Get more information about WEBENCH tools at www.ti.com/WEBENCH.

### 10.2.2.2 Output Voltage Resistors Selection

The output voltage is set with a resistor divider from the output node to the FB pin. TI recommends using 1\% tolerance or better divider resistors. Referring to the application schematic of Figure 10-1, start with $10.2 \mathrm{k} \Omega$ for R7 and use Equation 14 to calculate R6 $=53.6 \mathrm{k} \Omega$. To improve efficiency at light loads, consider using larger value resistors. If the values are too high, the converter is more susceptible to noise and voltage errors from the FB input leakage current are noticeable.

$$
\mathrm{R}_{6}=\frac{\mathrm{V}_{\text {OUT }}-\mathrm{V}_{\text {REF }}}{\mathrm{V}_{\text {REF }}} \times \mathrm{R}_{7}
$$

Table 10-2 shows the recommended components value for common output voltages.

### 10.2.2.3 Choosing Switching Frequency

The choice of switching frequency is a compromise between conversion efficiency and overall solution size. Higher switching frequency allows the use of smaller inductors and output capacitors, and hence, a more compact design. However, lower switching frequency implies reduced switching losses and usually results in higher system efficiency, so the $500-\mathrm{kHz}$ switching frequency was chosen for this example, remove the jumper on JP2 and leave RT pin floating.

Please note the switching frequency is also limited by the following as mentioned in Section 9.3.9:

- Minimum on time of the integrated power switch
- Input voltage
- Output voltage
- Frequency shift limitation


### 10.2.2.4 Soft-Start Capacitor Selection

The large $\mathrm{C}_{\mathrm{SS}}$ can reduce inrush current when driving large capacitive load. 33 nF is chosen for C 4 , which sets the soft-start time, $\mathrm{t}_{\mathrm{SS}}$, to approximately 5 ms .

In addition, the SS pin cannot be floated, so a minimum $6.8-\mathrm{nF}$ capacitor must be connected at this pin.

### 10.2.2.5 Bootstrap Capacitor Selection

A $0.1-\mu \mathrm{F}$ ceramic capacitor must be connected between the BST to SW pins for proper operation. TI recommends to use a ceramic capacitor with X5R or better grade dielectric. The capacitor C5 must have a $16-\mathrm{V}$ or higher voltage rating.

In addition, adding one BST resistor R4 to reduce the spike voltage on the SW node, TI recommends the resistance smaller than $10 \Omega$ be used between BST to the bootstrap capacitor.# 10.2.2.6 Undervoltage Lockout Setpoint 

The undervoltage lockout (UVLO) can be adjusted using the external voltage divider network of R1 and R2. R1 is connected between VIN and the EN pin and R2 is connected between EN and GND. The UVLO has two thresholds: one for power up when the input voltage is rising and one for power down or brownouts when the input voltage is falling. For the example design, the supply turns on and starts switching when the input voltage increases above $8 \mathrm{~V}\left(\mathrm{~V}_{\text {START }}\right)$. After the converter starts switching, it continues to do so until the input voltage falls below $7 \mathrm{~V}\left(\mathrm{~V}_{\text {STOP }}\right)$. Equation 3 and Equation 4 can be used to calculate the values for the upper and lower resistor values. For the stop voltages specified, the nearest standard resistor value for R1 is $511 \mathrm{k} \Omega$ and for R2 is $80.7 \mathrm{k} \Omega$.

### 10.2.2.7 Output Inductor Selection

The most critical parameters for the inductor are the inductance, saturation current, and the RMS current. The inductance is based on the desired peak-to-peak ripple current, $\Delta \mathrm{I}_{\mathrm{L}}$, which can be calculated by Equation 15.

$$
\Delta \mathrm{I}_{\mathrm{L}}=\frac{\mathrm{V}_{\mathrm{OUT}}}{\mathrm{~V}_{\mathrm{IN} \_\mathrm{MAX}}} \times \frac{\mathrm{V}_{\mathrm{IN} \_\mathrm{MAX}}-\mathrm{V}_{\mathrm{OUT}}}{\mathrm{~L} \times \mathrm{f}_{\mathrm{SW}}}
$$

Usually, define K coefficient represents the amount of inductor ripple current relative to the maximum output current of the device, a reasonable value of K is $20 \%$ to $60 \%$. Experience shows that the best value of K is $40 \%$. Since the ripple current increases with the input voltage, the maximum input voltage is always used to calculate the minimum inductance L. Use Equation 16 to calculate the minimum value of the output inductor.

$$
\mathrm{L}=\frac{\left(\mathrm{V}_{\mathrm{IN}}-\mathrm{V}_{\mathrm{OUT}}\right)}{\mathrm{f}_{\mathrm{SW}} \times \mathrm{K} \times \mathrm{I}_{\mathrm{OUT} \_\mathrm{MAX}}} \times \frac{\mathrm{V}_{\mathrm{OUT}}}{\mathrm{~V}_{\mathrm{IN}}}
$$

where

- K is the ripple ratio of the inductor current $\left(\Delta \mathrm{I}_{\mathrm{L}} / \mathrm{I}_{\text {OUT_MAX }}\right)$.

In general, it is preferable to choose lower inductance in switching power supplies, because it usually corresponds to faster transient response, smaller DCR, and reduced size for more compact designs. Too low of an inductance can generate too large of an inductor current ripple such that overcurrent protection at the full load can be falsely triggered. The device also generates more inductor core loss since the current ripple is larger. Larger inductor current ripple also implies larger output voltage ripple with the same output capacitors.
After inductance $L$ is determined, the maximum inductor peak current and RMS current can be calculated by Equation 17 and Equation 18.

$$
\begin{aligned}
& \mathrm{I}_{\mathrm{L} \_\text {PEAK }}=\mathrm{I}_{\mathrm{OUT}}+\frac{\Delta \mathrm{I}_{\mathrm{L}}}{2} \\
& \mathrm{I}_{\mathrm{L} \_\mathrm{RMS}}=\sqrt{\mathrm{I}_{\mathrm{OUT}}^{2}+\frac{\Delta \mathrm{I}_{\mathrm{L}}^{2}}{12}}
\end{aligned}
$$

Ideally, the saturation current rating of the inductor is at least as large as the high-side switch current limit, $\mathrm{I}_{\text {HS_LIMIT }}$ (see Section 8.5). This ensures that the inductor does not saturate even during a short circuit on the output. When the inductor core material saturates, the inductance falls to a very low value, causing the inductor current to rise very rapidly. Although the valley current limit, $\mathrm{I}_{\mathrm{LS} \_\text {LIMIT }}$, is designed to reduce the risk of current runaway, a saturated inductor can cause the current to rise to high values very rapidly, this can lead to component damage, so do not allow the inductor to saturate. In any case, the inductor saturation current must not be less than the maximum peak inductor current at full load.

For this design example, choose the following values:

- $\mathrm{K}=0.4$
- $\mathrm{V}_{\text {IN_MAX }}=30 \mathrm{~V}$- $\mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$
- $\mathrm{I}_{\text {OUT_MAX }}=3 \mathrm{~A}$

The inductor value is calculated to be $6.94 \mu \mathrm{H}$. Choose the nearest standard value of $6.8 \mu \mathrm{H}$, which gives a new K value of 0.408 . The maximum $\mathrm{I}_{\mathrm{HS} \_}$LIMIT is 5.8 A , the calculated peak current is 3.61 A , and the calculated RMS current is 3.02 A . The chosen inductor is a Würth Elektronik, $74439346068,6.8 \mu \mathrm{H}$, which has a saturation current rating of 10 A and a RMS current rating of 6.5 A .

The maximum inductance is limited by the minimum current ripple required for the peak current mode control to perform correctly. To avoid subharmonic oscillation, as a rule-of-thumb, the minimum inductor ripple current must be no less than approximately $10 \%$ of the device maximum rated current (3 A) under nominal conditions.

# 10.2.2.8 Output Capacitor Selection 

The device is designed to be used with a wide variety of LC filters, so it is generally desired to use as little output capacitance as possible to keep cost and size down. Choose the output capacitance, $\mathrm{C}_{\text {OUT }}$, with care since it directly affects the following specifications:

- Steady state output voltage ripple
- Loop stability
- Output voltage overshoot and undershoot during load current transient

The output voltage ripple is essentially composed of two parts. One is caused by the inductor current ripple going through the Equivalent Series Resistance (ESR) of the output capacitors:

$$
\Delta \mathrm{V}_{\text {OUT_ESR }}=\Delta \mathrm{I}_{\mathrm{L}} \times \mathrm{ESR}=\mathrm{K} \times \mathrm{I}_{\text {OUT }} \times \mathrm{ESR}
$$

The other is caused by the inductor current ripple charging and discharging the output capacitors:

$$
\Delta \mathrm{V}_{\text {OUT_C }}=\frac{\Delta \mathrm{I}_{\mathrm{L}}}{8 \times \mathrm{f}_{\mathrm{SW}} \times \mathrm{C}_{\text {OUT }}}=\frac{\mathrm{K} \times \mathrm{I}_{\text {OUT }}}{8 \times \mathrm{f}_{\mathrm{SW}} \times \mathrm{C}_{\text {OUT }}}
$$

where

- K is the ripple ratio of the inductor current $\left(\Delta \mathrm{I}_{\mathrm{L}} / \mathrm{I}_{\text {OUT_MAX }}\right)$.

The two components in the voltage ripple are not in phase, so the actual peak-to-peak ripple is smaller than the sum of the two peaks.

Output capacitance is usually limited by the load transient requirements rather than the output voltage ripple if the system requires tight voltage regulation with presence of large current steps and fast slew rate. When a large load step happens, output capacitors provide the required charge before the inductor current can slew up to the appropriate level. The control loop of the converter usually needs eight or more clock cycles to regulate the inductor current equal to the new load level. The output capacitance must be large enough to supply the current difference for about eight clock cycles to maintain the output voltage within the specified range. Equation 21 shows the minimum output capacitance needed for specified $\mathrm{V}_{\text {OUT }}$ overshoot and undershoot.

$$
\mathrm{C}_{\text {OUT }} \geq \frac{\Delta \mathrm{I}_{\text {OUT }}}{\mathrm{f}_{\mathrm{SW}} \times \Delta \mathrm{V}_{\text {OUT }} \times \mathrm{K}} \times\left[(1-\mathrm{D}) \times(1+\mathrm{K})+\frac{\mathrm{K}^{2}}{12}(2-\mathrm{D})\right]
$$

where

- D is $\mathrm{V}_{\text {OUT }} / \mathrm{V}_{\text {IN }}$, duty cycle of steady state.
- $\Delta \mathrm{V}_{\text {OUT }}$ is the output voltage change.
- $\Delta \mathrm{I}_{\text {OUT }}$ is the output current change.

For this design example, the target output ripple is 30 mV . Presuppose $\Delta \mathrm{V}_{\text {OUT_ESR }}=\Delta \mathrm{V}_{\text {OUT_C }}=30 \mathrm{mV}$ and choose $\mathrm{K}=0.4$. Equation 19 yields ESR no larger than $25 \mathrm{~m} \Omega$ and Equation 20 yields $\dot{\mathrm{C}}_{\text {OUT }}$ no smaller than $10 \mu \mathrm{~F}$. For the target overshoot and undershoot limitation of this design, $\Delta \mathrm{V}_{\text {OUT_SHOOT }}<5 \% \times \mathrm{V}_{\text {OUT }}$ $=250 \mathrm{mV}$ for an output current step of $\Delta \mathrm{I}_{\text {OUT }}=1.5 \mathrm{~A} . \mathrm{C}_{\text {OUT }}$ is calculated to be no smaller than $25 \mu \mathrm{~F}$by Equation 21. In summary, the most stringent criterion for the output capacitor is $25 \mu \mathrm{~F}$. Considering the ceramic capacitor has DC bias de-rating, it can be achieved with a bank of $2 \times 22-\mu \mathrm{F}, 35-\mathrm{V}$, ceramic capacitor C3216X5R1V226M160AC in the 1206 case size.
More output capacitors can be used to improve the load transient response. Ceramic capacitors can easily meet the minimum ESR requirements. In some cases, an aluminum electrolytic capacitor can be placed in parallel with the ceramics to build up the required value of capacitance. When using a mixture of aluminum and ceramic capacitors, use the minimum recommended value of ceramics and add aluminum electrolytic capacitors as needed.

The recommendations given in Table 10-2 provide typical and minimum values of output capacitance for the given conditions. These values are the effective figures. If the minimum values are to be used, the design must be tested over all of the expected application conditions, including input voltage, output current, and ambient temperature. This testing must include both bode plot and load transient assessments. The maximum value of total output capacitance can be referred to $\mathrm{C}_{\text {OUT }}$ selection and $\mathrm{C}_{\mathrm{FF}}$ selection in the TPS62933 Thermal Performance with SOT583 Package Application Report. Large values of output capacitance can adversely affect the start-up behavior of the converter as well as the loop stability. If values larger than noted here must be used, then a careful study of start-up at full load and loop stability must be performed.
In practice, the output capacitor has the most influence on the transient response and loop phase margin. Load transient testing and bode plots are the best way to validate any given design and must always be completed before the application goes into production. In addition to the required output capacitance, a small ceramic placed on the output can reduce high frequency noise. Small case size ceramic capacitors in the range of 1 nF to 100 nF can help reduce spikes on the output caused by inductor and board parasitics.
Table 10-2 shows the recommended LC combination.
Table 10-2. Recommended LC Combination for TPS62933

| $\mathrm{V}_{\text {OUT }}(\mathrm{V})$ | $\mathrm{f}_{\text {SW }}(\mathrm{kHz})$ | $\mathrm{R}_{\text {TOP }}(\mathrm{k} \Omega)$ | $\mathrm{R}_{\text {DOWN }}(\mathrm{k} \Omega)$ | Typical Inductor $\mathrm{L}(\mu \mathrm{H})$ | Typical Effective $\mathrm{C}_{\text {OUT }}(\mu \mathrm{F})$ | Minimum Effective $\mathrm{C}_{\text {OUT }}$ <br> ( $\mu \mathrm{F}$ ) |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 3.3 | 500 | 31.3 | 10.0 | 4.7 | 40 | 15 |
|  | 1200 |  |  | 2.2 | 30 | 10 |
| 5 | 500 | 52.5 | 10.0 | 6.8 | 20 | 10 |
|  | 1200 |  |  | 3.3 | 20 | 10 |
| 12 | 500 | 140.0 | 10.0 | 12 | 15 | 10 |

# 10.2.2.9 Input Capacitor Selection 

The TPS6293x device requires an input decoupling capacitor and, depending on the application, a bulk input capacitor. The typical recommended value for the decoupling capacitor is $10 \mu \mathrm{~F}$, and an additional $0.1-\mu \mathrm{F}$ capacitor from the VIN pin to ground is recommended to provide high frequency filtering.
The value of a ceramic capacitor varies significantly over temperature and the amount of DC bias applied to the capacitor. X5R and X7R ceramic dielectrics are recommended because they have a high capacitance-to-volume ratio and are fairly stable over temperature. The capacitor must also be selected with the DC bias taken into account. The effective capacitance value decreases as the DC bias increases.
The capacitor voltage rating needs to be greater than the maximum input voltage. The capacitor must also have a ripple current rating greater than the maximum input current ripple. The input ripple current can be calculated using Equation 22.

$$
\mathrm{I}_{\mathrm{CIN} \_ \text {RMS }}=\mathrm{I}_{\mathrm{OUT}} \times \sqrt{\frac{\mathrm{V}_{\mathrm{OUT}}}{\mathrm{~V}_{\mathrm{IN} \_ \mathrm{MIN}}}} \times \frac{\mathrm{V}_{\mathrm{IN} \_\mathrm{MIN}}-\mathrm{V}_{\mathrm{OUT}}}{\mathrm{~V}_{\mathrm{IN} \_\mathrm{MIN}}}
$$

For this example design, two TDK CGA5L1X7R1H106K160AC (10- $\mu \mathrm{F}, 50-\mathrm{V}, 1206, \mathrm{X} 7 \mathrm{R}$ ) capacitors have been selected. The effective capacitance under input voltage of 24 V for each one is $3.45 \mu \mathrm{~F}$. The input capacitance value determines the input ripple voltage of the converter. The input voltage ripple can be calculated usingEquation 23. Using the design example values, $\mathrm{I}_{\text {OUT_MAX }}=3 \mathrm{~A}, \mathrm{C}_{\mathrm{IN} \_ \text {EFF }}=2 \times 3.45=6.9 \mu \mathrm{~F}$, and $\mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$, yields an input voltage ripple of 222 mV and a RMS input ripple current of 1.22 A .

$$
\Delta \mathrm{V}_{\mathrm{IN}}=\frac{\mathrm{I}_{\text {OUT_MAX }} \times 0.25}{\mathrm{C}_{\mathrm{IN}} \times \mathrm{f}_{\mathrm{SW}}}+\left(\mathrm{I}_{\text {OUT_MAX }} \times \mathrm{R}_{\text {ESR_MAX }}\right)
$$

where

- $\mathrm{R}_{\text {ESR_MAX }}$ is the maximum series resistance of the input capacitor, which is approximately $1.5 \mathrm{~m} \Omega$ of two capacitors in paralleled.


# 10.2.2.10 Feedforward Capacitor $\mathrm{C}_{\text {FF }}$ Selection 

In some cases, a feedforward capacitor can be used across $R_{F B T}$ to improve the load transient response or improve the loop phase margin. This is especially true when values of $R_{F B T}>100 \mathrm{k} \Omega$ are used. Large values of $R_{F B T}$ in combination with the parasitic capacitance at the FB pin can create a small signal pole that interferes with the loop stability. A $\mathrm{C}_{\mathrm{FF}}$ helps mitigate this effect. Use lower values to determine if any advantage is gained by the use of a $\mathrm{C}_{\mathrm{FF}}$ capacitor.
The Optimizing Transient Response of Internally Compensated DC-DC Converters with Feedforward Capacitor Application Report is helpful when experimenting with a feedforward capacitor.

For this example design, a 10-pF capacitor C9 can be mounted to boost load transient performance.

### 10.2.2.11 Maximum Ambient Temperature

As with any power conversion device, the TPS6293x dissipates internal power while operating. The effect of this power dissipation is to raise the internal temperature of the converter above ambient. The internal die temperature $\left(T_{J}\right)$ is a function of the following:

- Ambient temperature
- Power loss
- Effective thermal resistance, $R_{\theta \mathrm{JA}}$, of the device
- PCB combination

The maximum internal die temperature must be limited to $150^{\circ} \mathrm{C}$. This establishes a limit on the maximum device power dissipation and, therefore, the load current. Equation 24 shows the relationships between the important parameters. It is easy to see that larger ambient temperatures $\left(T_{A}\right)$ and larger values of $R_{\theta J A}$ reduce the maximum available output current. The converter efficiency can be estimated by using the curves provided in this data sheet. Note that these curves include the power loss in the inductor. If the desired operating conditions cannot be found in one of the curves, then interpolation can be used to estimate the efficiency. Alternatively, the EVM can be adjusted to match the desired application requirements and the efficiency can be measured directly. The correct value of $R_{\theta J A}$ is more difficult to estimate. As stated in the Semiconductor and IC Package Thermal Metrics Application Report, the value of $R_{\theta J A}$ given in the Thermal Information table is not valid for design purposes and must not be used to estimate the thermal performance of the application. The values reported in that table were measured under a specific set of conditions that are rarely obtained in an actual application. The data given for $\mathrm{R}_{\theta J C(b o t t)}$ and $\Psi_{\text {JT }}$ can be useful when determining thermal performance. See the Semiconductor and IC Package Thermal Metrics Application Report for more information and the resources given at the end of this section.

$$
\mathrm{I}_{\text {OUT_MAX }}=\frac{\left(\mathrm{T}_{\mathrm{J}}-\mathrm{T}_{\mathrm{A}}\right)}{\mathrm{R}_{\theta \mathrm{UA}}} \times \frac{\eta}{1-\eta} \times \frac{1}{\mathrm{~V}_{\text {OUT }}}
$$

where

- $\eta$ is efficiency.

The effective $R_{\theta J A}$ is a critical parameter and depends on many factors such as the following:

- Power dissipation- Air temperature and flow
- PCB area
- Copper heat-sink area
- Number of thermal vias under the package
- Adjacent component placement# 10.2.3 Application Curves 

$V_{\text {IN }}=24 \mathrm{~V}, V_{\text {OUT }}=5 \mathrm{~V}, \mathrm{~L}_{1}=6.8 \mu \mathrm{H}, C_{\text {OUT }}=44 \mu \mathrm{~F}, \mathrm{~T}_{\mathrm{A}}=25^{\circ} \mathrm{C}$ (unless otherwise noted)
![img-50.jpeg](img-50.jpeg)

Figure 10-2. Efficiency
![img-51.jpeg](img-51.jpeg)

Figure 10-4. Line Regulation
![img-52.jpeg](img-52.jpeg)

Figure 10-6. Switching Frequency vs $\mathrm{V}_{\text {IN }}, \mathrm{V}_{\text {OUT }}=\mathbf{5}$ V
![img-53.jpeg](img-53.jpeg)

Figure 10-3. Load Regulation
![img-54.jpeg](img-54.jpeg)

Figure 10-5. Switching Frequency vs Load Current
![img-55.jpeg](img-55.jpeg)

Figure 10-7. Loop Frequency Response, $\mathrm{I}_{\text {OUT }}=\mathbf{3} \mathrm{A}$, $\mathrm{BW}=49.4 \mathrm{kHz}, \mathrm{PM}=57^{\circ}, \mathrm{GM}=-12 \mathrm{~dB}$![img-56.jpeg](img-56.jpeg)

Figure 10-8. Case Temperature, $\mathrm{V}_{\mathrm{IN}}=24 \mathrm{~V}, \mathrm{I}_{\text {OUT }}=3$ $\mathrm{A}, \mathrm{f}_{\mathrm{SW}}=500 \mathrm{kHz}$
![img-57.jpeg](img-57.jpeg)

Figure 10-10. Shutdown Relative to $\mathrm{V}_{\mathrm{IN}}, \mathrm{I}_{\text {OUT }}=3 \mathrm{~A}$
![img-58.jpeg](img-58.jpeg)

Figure 10-12. Shutdown Through EN, $\mathrm{I}_{\text {OUT }}=3 \mathrm{~A}$
![img-59.jpeg](img-59.jpeg)

Figure 10-9. Start-Up Relative to $\mathrm{V}_{\mathrm{IN}}, \mathrm{I}_{\text {OUT }}=3 \mathrm{~A}$
![img-60.jpeg](img-60.jpeg)

Figure 10-11. Start-Up Through EN, $\mathrm{I}_{\text {OUT }}=3 \mathrm{~A}$
![img-61.jpeg](img-61.jpeg)

Figure 10-13. Steady State, $\mathrm{I}_{\text {OUT }}=0 \mathrm{~A}$![img-62.jpeg](img-62.jpeg)

Figure 10-14. Steady State, $\mathrm{I}_{\text {OUT }}=0.1 \mathrm{~A}$
![img-63.jpeg](img-63.jpeg)

Figure 10-16. Steady State, $\mathrm{I}_{\text {OUT }}=1 \mathrm{~A}$
![img-64.jpeg](img-64.jpeg)

Figure 10-18. Steady State, $\mathrm{I}_{\text {OUT }}=3 \mathrm{~A}$
![img-65.jpeg](img-65.jpeg)

Figure 10-15. Steady State, $\mathrm{I}_{\text {OUT }}=0.5 \mathrm{~A}$
![img-66.jpeg](img-66.jpeg)

Figure 10-17. Steady State, $\mathrm{I}_{\text {OUT }}=2 \mathrm{~A}$
![img-67.jpeg](img-67.jpeg)

Figure 10-19. Load Transient Response, 0.5 to 2.5 A, Slew Rate $=0.8 \mathrm{~A} / \mu \mathrm{S}$![img-68.jpeg](img-68.jpeg)

Figure 10-20. Load Transient Response, 1 to 3 A, Slew Rate $=0.8 \mathrm{~A} / \mu \mathrm{S}$
![img-69.jpeg](img-69.jpeg)

Figure 10-21. $\mathrm{V}_{\text {OUT }}$ Hard Short Protection
![img-70.jpeg](img-70.jpeg)

Figure 10-22. $\mathrm{V}_{\text {OUT }}$ Hard Short Recovery

# 10.3 What to Do and What Not to Do 

- Do not exceed the Absolute Maximum Ratings.
- Do not exceed the Recommended Operating Conditions.
- Do not exceed the ESD Ratings.
- Do not allow the SS pin floating.
- Do not allow the output voltage to exceed the input voltage, nor go below ground.
- Do not use the value of $R_{B, I A}$ given in the Thermal Information table to design your application. See Section 10.2.2.11.
- Follow all the guidelines and suggestions found in this data sheet before committing the design to production. TI application engineers are ready to help critique your design and PCB layout to help make your project a success.
- Use a 100-nF capacitor connected directly to the VIN and GND pins of the device. See Section 10.2.2.9 for details.# 11 Power Supply Recommendations 

The devices are designed to operate from an input voltage supply range between 3.8 V and 30 V . This input supply must be well regulated and compatible with the limits found in the specifications of this data sheet. In addition, the input supply must be capable of delivering the required input current to the loaded converter. The average input current can be estimated with Equation 25.

$$
\mathrm{I}_{\mathrm{IN}}=\frac{\mathrm{V}_{\mathrm{OUT}} \times \mathrm{I}_{\mathrm{OUT}}}{\mathrm{~V}_{\mathrm{IN}} \times \eta}
$$

where

- $\eta$ is efficiency.

If the converter is connected to the input supply through long wires or PCB traces, special care is required to achieve good performance. The parasitic inductance and resistance of the input cables can have an adverse effect on the operation of the converter. The parasitic inductance, in combination with the low-ESR, ceramic input capacitors, can form an under-damped resonant circuit, resulting in overvoltage transients at the input to the converter. The parasitic resistance can cause the voltage at the VIN pin to dip whenever a load transient is applied to the output. If the application is operating close to the minimum input voltage, this dip can cause the converter to momentarily shutdown and reset. The best way to solve these kind of issues is to reduce the distance from the input supply to the converter and use an aluminum or tantalum input capacitor in parallel with the ceramics. The moderate ESR of these types of capacitors help damp the input resonant circuit and reduce any overshoots. A value in the range of $20 \mu \mathrm{~F}$ to $100 \mu \mathrm{~F}$ is usually sufficient to provide input damping and help hold the input voltage steady during large load transients.

TI recommends that the input supply must not be allowed to fall below the output voltage by more than 0.3 V. Under such conditions, the output capacitors discharges through the body diode of the high-side power MOSFET. The resulting current can cause unpredictable behavior, and in extreme cases, possible device damage. If the application allows for this possibility, then use a Schottky diode from VIN to VOUT to provide a path around the converter for this current.

In some cases, a transient voltage suppressor (TVS) is used on the input of converters. One class of this device has a snap-back characteristic (thyristor type). The use of a device with this type of characteristic is not recommended. When the TVS fires, the clamping voltage falls to a very low value. If this voltage is less than the output voltage of the converter, the output capacitors discharges through the device, as mentioned above.

Sometimes, for other system considerations, an input filter is used in front of the converter, which can lead to instability as well as some of the effects mentioned above, unless it is designed carefully. The AN-2162 Simple Success with Conducted EMI from DCDC Converters User's Guide provides helpful suggestions when designing an input filter for any switching converter.# 12 Layout 

### 12.1 Layout Guidelines

The PCB layout of any DC/DC converter is critical to the optimal performance of the design. Bad PCB layout can disrupt the operation of a good schematic design. Even if the converter regulates correctly, bad PCB layout can mean the difference between a robust design and one that cannot be mass produced. Furthermore, the EMI performance of the converter is dependent on the PCB layout to a great extent. In a buck converter, the most critical PCB feature is the loop formed by the input capacitors and power ground, as shown in Figure 12-1. This loop carries large transient currents that can cause large transient voltages when reacting with the trace inductance. These unwanted transient voltages disrupt the proper operation of the converter. Because of this, the traces in this loop must be wide and short, and the loop area as small as possible to reduce the parasitic inductance.

TI recommends a 2-layer board with 2-oz copper thickness of top and bottom layer, and proper layout provides low current conduction impedance, proper shielding, and lower thermal resistance. Figure 12-2 and Figure 12-3 show the recommended layouts for the critical components of the TPS62933.

- Place the inductor, input and output capacitors, and the IC on the same layer.
- Place the input and output capacitors as close as possible to the IC. The VIN and GND traces must be as wide as possible and provide sufficient vias on them to minimize trace impedance. The wide areas are also of advantage from the view point of heat dissipation.
- Place a $0.1-\mu \mathrm{F}$ ceramic decoupling capacitor or capacitors as close as possible to VIN and GND pins, which is key to EMI reduction.
- Keep the SW trace as physically short and wide as practical to minimize radiated emissions.
- Place a BST capacitor and resistor close to the BST pin and SW node. A > 10-mil width trace is recommended to reduce the parasitic inductance.
- Place the feedback divider as close as possible to the FB pin. A > 10-mil width trace is recommended for heat dissipation. Connect a separate $\mathrm{V}_{\text {OUT }}$ trace to the upper feedback resistor. Place the voltage feedback loop away from the high-voltage switching trace. The voltage feedback loop preferably has ground shield.
- Place the SS capacitor and RT resistor close to the IC and routed with minimal lengths of trace. A > 10-mil width trace is recommended for heat dissipation.
![img-71.jpeg](img-71.jpeg)

Figure 12-1. Current Loop With Fast Edges12.2 Layout Example
![img-72.jpeg](img-72.jpeg)

Figure 12-2. TPS62933 Top Layout Example
![img-73.jpeg](img-73.jpeg)

Figure 12-3. TPS62933 Bottom Layout Example# 13 Device and Documentation Support 

### 13.1 Device Support

### 13.1.1 Third-Party Products Disclaimer

TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

### 13.1.2 Development Support

### 13.1.2.1 Custom Design With WEBENCH® Tools

Create a custom design with the TPS6293x using the WEBENCH ${ }^{\circledR}$ Power Designer.

1. Start by entering the input voltage $\left(\mathrm{V}_{\mathrm{IN}}\right)$, output voltage $\left(\mathrm{V}_{\mathrm{OUT}}\right)$, and output current $\left(\mathrm{I}_{\mathrm{OUT}}\right)$ requirements.
2. Optimize the design for key parameters such as efficiency, footprint, and cost using the optimizer dial.
3. Compare the generated design with other possible solutions from Texas Instruments.

The WEBENCH Power Designer provides a customized schematic along with a list of materials with real-time pricing and component availability.
In most cases, these actions are available:

- Run electrical simulations to see important waveforms and circuit performance
- Run thermal simulations to understand board thermal performance
- Export customized schematic and layout into popular CAD formats
- Print PDF reports for the design, and share the design with colleagues

Get more information about WEBENCH tools at www.ti.com/WEBENCH.

### 13.2 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Subscribe to updates to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

### 13.3 Support Resources

TI E2E ${ }^{\text {TM }}$ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.
Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

### 13.4 Trademarks

TI E2E ${ }^{\text {TM }}$ is a trademark of Texas Instruments.
WEBENCH ${ }^{\circledR}$ is a registered trademark of Texas Instruments.
All trademarks are the property of their respective owners.

### 13.5 Electrostatic Discharge Caution

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

### 13.6 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.# 14 Mechanical, Packaging, and Orderable Information 

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
|  TPS62932DRLR | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 150  |
|  TPS62932DRLR.A | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 2932  |
|  TPS62932DRLR.B | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 2932  |
|  TPS62933DRLR | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 150  |
|  TPS62933DRLR.A | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 2933  |
|  TPS62933DRLR.B | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 2933  |
|  TPS62933FDRLR | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 150  |
|  TPS62933FDRLR.A | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 933F  |
|  TPS62933FDRLR.B | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 933F  |
|  TPS62933ODRLR | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 150  |
|  TPS62933ODRLR.A | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 933O  |
|  TPS62933ODRLR.B | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 933O  |
|  TPS62933PDRLR | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | Call TI | Sn | Level-1-260C-UNLIM | $-40$ to 150  |
|  TPS62933PDRLR.A | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 933P  |
|  TPS62933PDRLR.B | Active | Production | SOT-5X3 (DRL) | 8 | 4000 | LARGE T\&R | Yes | SN | Level-1-260C-UNLIM | $-40$ to 150 | 933P  |

${ }^{(1)}$ Status: For more details on status, see our product life cycle. ${ }^{(2)}$ Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind. ${ }^{(3)}$ RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition. ${ }^{(4)}$ Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width. ${ }^{(5)}$ MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board. ${ }^{(6)}$ Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "-" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.# TAPE AND REEL INFORMATION 

![img-74.jpeg](img-74.jpeg)

TAPE DIMENSIONS
![img-75.jpeg](img-75.jpeg)

| A0 | Dimension designed to accommodate the component width |
| :-- | :-- |
| B0 | Dimension designed to accommodate the component length |
| K0 | Dimension designed to accommodate the component thickness |
| W | Overall width of the carrier tape |
| P1 | Pitch between successive cavity centers |

QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE
![img-76.jpeg](img-76.jpeg)

Pocket Quadrants
*All dimensions are nominal

| Device | Package <br> Type | Package <br> Drawing | Pins | SPQ | Reel <br> Diameter <br> (mm) | Reel <br> Width <br> W1 (mm) | A0 <br> (mm) | B0 <br> (mm) | K0 <br> (mm) | P1 <br> (mm) | W <br> (mm) | Pin1 <br> Quadrant |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| TPS62932DRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |
| TPS62933DRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |
| TPS62933FDRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |
| TPS62933ODRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |
| TPS62933PDRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |# PACKAGE MATERIALS INFORMATION

## TAPE AND REEL BOX DIMENSIONS

![img-77.jpeg](img-77.jpeg)

*All dimensions are nominal

|  Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS62932DRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0  |
|  TPS62933DRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0  |
|  TPS62933FDRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0  |
|  TPS62933ODRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0  |
|  TPS62933PDRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0  |![img-78.jpeg](img-78.jpeg)

NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, interlead flash, protrusions, or gate burrs shall not exceed 0.15 mm per side.
4. Reference JEDEC Registration MO-293, Variation UDAD![img-79.jpeg](img-79.jpeg)

NOTES: (continued)
5. Publication IPC-7351 may have alternate designs.
6. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
7. Land pattern design aligns to IPC-610, Bottom Termination Component (BTC) solder joint inspection criteria.![img-80.jpeg](img-80.jpeg)

NOTES: (continued)
8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
9. Board assembly site may have different recommendations for stencil design.# IMPORTANT NOTICE AND DISCLAIMER 

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.
These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.
TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.
TI objects to and rejects any additional or different terms you may have proposed.
Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265
Copyright © 2025, Texas Instruments Incorporated