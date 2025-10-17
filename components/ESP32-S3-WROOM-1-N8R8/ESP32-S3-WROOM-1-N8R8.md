# ESP32-S3-WROOM-1 ESP32-S3-WROOM-1U

## Datasheet Version 1.6

2.4 GHz Wi-Fi (802.11b/g/n) and Bluetooth® 5 module

Built around ESP32-S3 series of SoCs, Xtensa® dual-core 32-bit LX7 microprocessor

Flash up to 16 MB, PSRAM up to 16 MB

Up to 36 GPIOs, rich set of peripherals

On-board PCB antenna or external antenna connector

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

ESP32-S3-WROOM-1

ESP32-S3-WROOM-1U

![img-3.jpeg](img-3.jpeg)# 1 Module Overview 

## Note:

Check the link or the QR code to make sure that you use the latest version of this document: https://www.espressif.com/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf

### 1.1 Features

## CPU and On-Chip Memory

- ESP32-S3 series of SoCs embedded, Xtensa ${ }^{\circledR}$ dual-core 32-bit LX7 microprocessor (with single precision FPU), up to 240 MHz
- 384 KB ROM
- 512 KB SRAM
- 16 KB SRAM in RTC
- Up to 16 MB PSRAM


## Wi-Fi

- $802.11 \mathrm{~b} / \mathrm{g} / \mathrm{n}$
- Bit rate: 802.11n up to 150 Mbps
- A-MPDU and A-MSDU aggregation
- $0.4 \mu \mathrm{~s}$ guard interval support
- Center frequency range of operating channel: $2412 \sim 2484 \mathrm{MHz}$


## Bluetooth

- Bluetooth LE: Bluetooth 5, Bluetooth mesh
- Speed: 125 Kbps, 500 Kbps, 1 Mbps, 2 Mbps
- Advertising extensions
- Multiple advertisement sets
- Channel selection algorithm \#2
- Internal co-existence mechanism between Wi-Fi and Bluetooth to share the same antenna


## Peripherals

- 36 GPIOs


## - 4 strapping GPIOs

- SPI, LCD interface, Camera interface, UART, I2C, I2S, remote control, pulse counter, LED PWM, full-speed USB 2.0 OTG, USB Serial/JTAG controller, MCPWM, SD/MMC host controller, GDMA, TWAI ${ }^{\circledR}$ controller (compatible with ISO 11898-1), ADC, touch sensor, temperature sensor, timers and watchdogs


## Integrated Components on Module

- 40 MHz crystal oscillator
- Up to 16 MB Quad SPI flash


## Antenna Options

- ESP32-S3-WROOM-1: On-board PCB antenna
- ESP32-S3-WROOM-1U: External antenna via a connector


## Operating Conditions

- Operating voltage/Power supply: $3.0 \sim 3.6 \mathrm{~V}$
- Operating ambient temperature:
- $65^{\circ} \mathrm{C}$ version: $-40 \sim 65^{\circ} \mathrm{C}$
- $85^{\circ} \mathrm{C}$ version: $-40 \sim 85^{\circ} \mathrm{C}$
- $105^{\circ} \mathrm{C}$ version: $-40 \sim 105^{\circ} \mathrm{C}$


## Certification

- RF certification: See certificates
- Green certification: RoHS/REACH


## Test

- HTOL/HTSL/uHAST/TCT/ESD# 1.2 Series Comparison 

ESP32-S3-WROOM-1 and ESP32-S3-WROOM-1U are two powerful, generic Wi-Fi + Bluetooth LE MCU modules that are built around the ESP32-S3 series of SoCs. On top of a rich set of peripherals, the acceleration for neural network computing and signal processing workloads provided by the SoC make the modules an ideal choice for a wide variety of application scenarios related to AI and Artificial Intelligence of Things (AIoT), such as wake word detection, speech commands recognition, face detection and recognition, smart home, smart appliances, smart control panel, smart speaker, etc.

ESP32-S3-WROOM-1 comes with a PCB antenna. ESP32-S3-WROOM-1U comes with an external antenna connector. A wide selection of module variants are available for customers as shown in Table 1-1 and 1-2. H4 series modules operate at $-40 \sim 105^{\circ} \mathrm{C}$ ambient temperature, R8 and R16V series modules operate at $-40 \sim$ $65^{\circ} \mathrm{C}$ ambient temperature, and other module variants operate at $-40 \sim 85^{\circ} \mathrm{C}$ ambient temperature. For R8 and R16V series modules with Octal SPI PSRAM, if the PSRAM ECC function is enabled, the maximum ambient temperature can be improved to $85^{\circ} \mathrm{C}$, while the usable size of PSRAM will be reduced by $1 / 16$.

Table 1-1. ESP32-S3-WROOM-1 Series Comparison ${ }^{1}$

| Ordering Code ${ }^{2}$ | Flash ${ }^{3,4}$ | PSRAM $^{4}$ | Ambient Temp. ${ }^{5}$ <br> $\left({ }^{\circ} \mathrm{C}\right)$ | Size ${ }^{6}$ <br> (mm) |
| :-- | :--: | :--: | :--: | :--: |
| ESP32-S3-WROOM-1-N4 | 4 MB (Quad SPI) | - | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1-N8 | 8 MB (Quad SPI) | - | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1-N16 | 16 MB (Quad SPI) | - | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1-H4 | 4 MB (Quad SPI) | - | $-40 \sim 105$ |  |
| ESP32-S3-WROOM-1-N4R2 | 4 MB (Quad SPI) | 2 MB (Quad SPI) | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1-N8R2 | 8 MB (Quad SPI) | 2 MB (Quad SPI) | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1-N16R2 | 16 MB (Quad SPI) | 2 MB (Quad SPI) | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1-N4R8 | 4 MB (Quad SPI) | 8 MB (Octal SPI) | $-40 \sim 65$ |  |
| ESP32-S3-WROOM-1-N8R8 | 8 MB (Quad SPI) | 8 MB (Octal SPI) | $-40 \sim 65$ |  |
| ESP32-S3-WROOM-1-N16R8 | 16 MB (Quad SPI) | 8 MB (Octal SPI) | $-40 \sim 65$ |  |
| ESP32-S3-WROOM-1-N16R16VA ${ }^{7}$ | 16 MB (Quad SPI) | 16 MB (Octal SPI) | $-40 \sim 65$ |  |

${ }^{1}$ This table shares the same notes presented in Table 1-2 below.
Table 1-2. ESP32-S3-WROOM-1U Series Comparison

| Ordering Code ${ }^{2}$ | Flash ${ }^{3,4}$ | PSRAM $^{4}$ | Ambient Temp. ${ }^{5}$ <br> $\left({ }^{\circ} \mathrm{C}\right)$ | Size ${ }^{6}$ <br> (mm) |
| :-- | :--: | :--: | :--: | :--: |
| ESP32-S3-WROOM-1U-N4 | 4 MB (Quad SPI) | - | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1U-N8 | 8 MB (Quad SPI) | - | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1U-N16 | 16 MB (Quad SPI) | - | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1U-H4 | 4 MB (Quad SPI) | - | $-40 \sim 105$ |  |
| ESP32-S3-WROOM-1U-N4R2 | 4 MB (Quad SPI) | 2 MB (Quad SPI) | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1U-N8R2 | 8 MB (Quad SPI) | 2 MB (Quad SPI) | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1U-N16R2 | 16 MB (Quad SPI) | 2 MB (Quad SPI) | $-40 \sim 85$ |  |
| ESP32-S3-WROOM-1U-N4R8 | 4 MB (Quad SPI) | 8 MB (Octal SPI) | $-40 \sim 65$ |  |
| ESP32-S3-WROOM-1U-N8R8 | 8 MB (Quad SPI) | 8 MB (Octal SPI) | $-40 \sim 65$ |  |
| ESP32-S3-WROOM-1U-N16R8 | 16 MB (Quad SPI) | 8 MB (Octal SPI) | $-40 \sim 65$ |  |
| ESP32-S3-WROOM-1U-N16R16VA ${ }^{7}$ | 16 MB (Quad SPI) | 16 MB (Octal SPI) | $-40 \sim 65$ |  |${ }^{2}$ For customization of ESP32-S3-WROOM-1-H4, ESP32-S3-WROOM-1U-H4, and ESP32-S3-WROOM-1UN16R16VA, please contact us.
${ }^{3}$ By default, the SPI flash on the module operates at a maximum clock frequency of 80 MHz and does not support the auto suspend feature. If you have a requirement for a higher flash clock frequency of 120 MHz or if you need the flash auto suspend feature, please contact us.
${ }^{4}$ The modules use PSRAM integrated in the chip's package. For specifications, refer to Section 6.5 Memory Specifications.
${ }^{5}$ Ambient temperature specifies the recommended temperature range of the environment immediately outside the Espressif module.
${ }^{6}$ For details, refer to Section 10.1 Module Dimensions.
${ }^{7}$ Please note that the VDD_SPI voltage is 1.8 V for ESP32-S3-WROOM-1-N16R16VA and ESP32-S3-WROOM-1U-N16R16VA only.

At the core of the modules is an ESP32-S3 series of SoC, an Xtensa ${ }^{\circledR} 32$-bit LX7 CPU that operates at up to 240 MHz . You can power off the CPU and make use of the low-power co-processor to constantly monitor the peripherals for changes or crossing of thresholds.

# Note: 

For more information on ESP32-S3, please refer to ESP32-S3 Series Datasheet.
For chip revision identification, ESP-IDF release that supports a specific chip revision, and other information on chip revisions, please refer to ESP32-S3 Series SoC Errata > Section Chip Revision Identification.

### 1.3 Applications

- Smart Home
- Industrial Automation
- Health Care
- Consumer Electronics
- Smart Agriculture
- POS Machines
- Service Robot
- Audio Devices
- Generic Low-power loT Sensor Hubs
- Generic Low-power loT Data Loggers
- Cameras for Video Streaming
- USB Devices
- Speech Recognition
- Image Recognition
- Wi-Fi + Bluetooth Networking Card
- Touch and Proximity Sensing# Contents 

1 Module Overview ..... 2
1.1 Features ..... 2
1.2 Series Comparison ..... 3
1.3 Applications ..... 4
2 Block Diagram ..... 9
3 Pin Definitions ..... 10
3.1 Pin Layout ..... 10
3.2 Pin Description ..... 11
4 Boot Configurations ..... 13
4.1 Chip Boot Mode Control ..... 14
4.2 VDD_SPI Voltage Control ..... 15
4.3 ROM Messages Printing Control ..... 15
4.4 JTAG Signal Source Control ..... 15
4.5 Chip Power-up and Reset ..... 16
5 Peripherals ..... 17
5.1 Peripheral Overview ..... 17
5.2 Peripheral Description ..... 17
5.2.1 Connectivity Interface ..... 17
5.2.1.1 UART Controller ..... 17
5.2.1.2 I2C Interface ..... 18
5.2.1.3 I2S Interface ..... 19
5.2.1.4 LCD and Camera Controller ..... 19
5.2.1.5 Serial Peripheral Interface (SPI) ..... 19
5.2.1.6 Two-Wire Automotive Interface (TWAI ${ }^{\circledR}$ ) ..... 22
5.2.1.7 USB 2.0 OTG Full-Speed Interface ..... 23
5.2.1.8 USB Serial/JTAG Controller ..... 24
5.2.1.9 SD/MMC Host Controller ..... 25
5.2.1.10 LED PWM Controller ..... 25
5.2.1.11 Motor Control PWM (MCPWM) ..... 26
5.2.1.12 Remote Control Peripheral (RMT) ..... 26
5.2.1.13 Pulse Count Controller (PCNT) ..... 27
5.2.2 Analog Signal Processing ..... 27
5.2.2.1 SAR ADC ..... 28
5.2.2.2 Temperature Sensor ..... 28
5.2.2.3 Touch Sensor ..... 28
6 Electrical Characteristics ..... 29
6.1 Absolute Maximum Ratings ..... 29
6.2 Recommended Operating Conditions ..... 296.3 DC Characteristics $\left(3.3 \mathrm{~V}, 25^{\circ} \mathrm{C}\right)$ ..... 29
6.4 Current Consumption Characteristics ..... 30
6.4.1 Current Consumption in Active Mode ..... 30
6.4.2 Current Consumption in Other Modes ..... 30
6.5 Memory Specifications ..... 32
7 RF Characteristics ..... 33
7.1 Wi-Fi Radio ..... 33
7.1.1 Wi-Fi RF Transmitter (TX) Characteristics ..... 33
7.1.2 Wi-Fi RF Receiver (RX) Characteristics ..... 34
7.2 Bluetooth LE Radio ..... 35
7.2.1 Bluetooth LE RF Transmitter (TX) Characteristics ..... 36
7.2.2 Bluetooth LE RF Receiver (RX) Characteristics ..... 37
8 Module Schematics ..... 40
9 Peripheral Schematics ..... 42
10 Physical Dimensions ..... 43
10.1 Module Dimensions ..... 43
10.2 Dimensions of External Antenna Connector ..... 44
11 PCB Layout Recommendations ..... 46
11.1 PCB Land Pattern ..... 46
11.2 Module Placement for PCB Design ..... 47
12 Product Handling ..... 48
12.1 Storage Conditions ..... 48
12.2 Electrostatic Discharge (ESD) ..... 48
12.3 Reflow Profile ..... 48
12.4 Ultrasonic Vibration ..... 49
Datasheet Versioning ..... 50
Related Documentation and Resources ..... 51
Revision History ..... 52# List of Tables 

1-1 ESP32-S3-WROOM-1 Series Comparison ${ }^{1}$ ..... 3
1-2 ESP32-S3-WROOM-1U Series Comparison ..... 3
3-1 Pin Definitions ..... 11
4-1 Default Configuration of Strapping Pins ..... 13
4-2 Description of Timing Parameters for the Strapping Pins ..... 14
4-3 Chip Boot Mode Control ..... 14
4-4 VDD_SPI Voltage Control ..... 15
4-5 JTAG Signal Source Control ..... 16
4-6 Description of Timing Parameters for Power-up and Reset ..... 16
6-1 Absolute Maximum Ratings ..... 29
6-2 Recommended Operating Conditions ..... 29
6-3 DC Characteristics (3.3 V, $25^{\circ} \mathrm{C}$ ) ..... 29
6-4 Current Consumption in Avtice Mode ..... 30
6-5 Current Consumption in Modem-sleep Mode ..... 31
6-6 Current Consumption in Low-Power Modes ..... 31
6-7 Flash Specifications ..... 32
6-8 PSRAM Specifications ..... 32
7-1 Wi-Fi RF Characteristics ..... 33
7-2 TX Power with Spectral Mask and EVM Meeting 802.11 Standards ..... 33
7-3 TX EVM Test ${ }^{1}$ ..... 33
7-4 RX Sensitivity ..... 34
7-5 Maximum RX Level ..... 35
7-6 RX Adjacent Channel Rejection ..... 35
7-7 Bluetooth LE RF Characteristics ..... 35
7-8 Bluetooth LE - Transmitter Characteristics - 1 Mbps ..... 36
7-9 Bluetooth LE - Transmitter Characteristics - 2 Mbps ..... 36
7-10 Bluetooth LE - Transmitter Characteristics - 125 Kbps ..... 36
7-11 Bluetooth LE - Transmitter Characteristics - 500 Kbps ..... 37
7-12 Bluetooth LE - Receiver Characteristics - 1 Mbps ..... 37
7-13 Bluetooth LE - Receiver Characteristics - 2 Mbps ..... 37
7-14 Bluetooth LE - Receiver Characteristics - 125 Kbps ..... 38
7-15 Bluetooth LE - Receiver Characteristics - 500 Kbps ..... 38# List of Figures 

2-1 ESP32-S3-WROOM-1 Block Diagram ..... 9
2-2 ESP32-S3-WROOM-1U Block Diagram ..... 9
3-1 Pin Layout (Top View) ..... 10
4-1 Visualization of Timing Parameters for the Strapping Pins ..... 14
4-2 Visualization of Timing Parameters for Power-up and Reset ..... 16
8-1 ESP32-S3-WROOM-1 Schematics ..... 40
8-2 ESP32-S3-WROOM-1U Schematics ..... 41
9-1 Peripheral Schematics ..... 42
10-1 ESP32-S3-WROOM-1 Physical Dimensions ..... 43
10-2 ESP32-S3-WROOM-1U Physical Dimensions ..... 43
10-3 Dimensions of External Antenna Connector ..... 44
11-1 ESP32-S3-WROOM-1 Recommended PCB Land Pattern ..... 46
11-2 ESP32-S3-WROOM-1U Recommended PCB Land Pattern ..... 47
12-1 Reflow Profile ..... 48# 2 Block Diagram 

![img-4.jpeg](img-4.jpeg)

Figure 2-1. ESP32-S3-WROOM-1 Block Diagram
![img-5.jpeg](img-5.jpeg)

Figure 2-2. ESP32-S3-WROOM-1U Block Diagram

## Note:

For the pin mapping between the chip and the in-package PSRAM, please refer to ESP32-S3 Series Datasheet > Table Pin Mapping Between Chip and In-package Flash/PSRAM.# 3 Pin Definitions 

### 3.1 Pin Layout

The pin diagram below shows the approximate location of pins on the module. For the actual diagram drawn to scale, please refer to Figure 10.1 Module Dimensions.
![img-6.jpeg](img-6.jpeg)

Figure 3-1. Pin Layout (Top View)

## Note A:

The zone marked with dotted lines is the antenna keepout zone. The pin diagram is applicable to ESP32-S3-WROOM1 and ESP32-S3-WROOM-1U, but the latter has no antenna keepout zone. To learn more about the keepout zone for module's antenna on the base board, please refer to ESP32-S3 Hardware Design Guidelines > Section General Principles of PCB Layout for Modules.# 3.2 Pin Description 

The module has 41 pins. See pin definitions in Table 3-1 Pin Definitions.
For explanations of pin names and function names, as well as configurations of peripheral pins, please refer to ESP32-S3 Series Datasheet.

Table 3-1. Pin Definitions

| Name | No. | Type ${ }^{a}$ | Function |
| :--: | :--: | :--: | :--: |
| GND | 1 | $P$ | GND |
| 3V3 | 2 | $P$ | Power supply |
| EN | 3 | I | High: on, enables the chip. <br> Low: off, the chip powers off. <br> Note: Do not leave the EN pin floating. |
| IO4 | 4 | I/O/T | RTC_GPIO4, GPIO4, TOUCH4, ADC1_CH3 |
| IO5 | 5 | I/O/T | RTC_GPIO5, GPIO5, TOUCH5, ADC1_CH4 |
| IO6 | 6 | I/O/T | RTC_GPIO6, GPIO6, TOUCH6, ADC1_CH5 |
| 107 | 7 | I/O/T | RTC_GPIO7, GPIO7, TOUCH7, ADC1_CH6 |
| 1015 | 8 | I/O/T | RTC_GPIO15, GPIO15, UORTS, ADC2_CH4, XTAL_32K_P |
| 1016 | 9 | I/O/T | RTC_GPIO16, GPIO16, UOCTS, ADC2_CH5, XTAL_32K_N |
| 1017 | 10 | I/O/T | RTC_GPIO17, GPIO17, U1TXD, ADC2_CH6 |
| 1018 | 11 | I/O/T | RTC_GPIO18, GPIO18, U1RXD, ADC2_CH7, CLK_OUT3 |
| 108 | 12 | I/O/T | RTC_GPIO8, GPIO8, TOUCH8, ADC1_CH7, SUBSPICS1 |
| 1019 | 13 | I/O/T | RTC_GPIO19, GPIO19, U1RTS, ADC2_CH8, CLK_OUT2, USB_D- |
| 1020 | 14 | I/O/T | RTC_GPIO20, GPIO20, U1CTS, ADC2_CH9, CLK_OUT1, USB_D+ |
| 103 | 15 | I/O/T | RTC_GPIO3, GPIO3, TOUCH3, ADC1_CH2 |
| 1046 | 16 | I/O/T | GPIO46 |
| 109 | 17 | I/O/T | RTC_GPIO9, GPIO9, TOUCH9, ADC1_CH8, FSPIHD, SUBSPIHD |
| 1010 | 18 | I/O/T | RTC_GPIO10, GPIO10, TOUCH10, ADC1_CH9, FSPICSO, FSPIIO4, SUBSPICSO |
| 1011 | 19 | I/O/T | RTC_GPIO11, GPIO11, TOUCH11, ADC2_CH0, FSPID, FSPIIO5, SUBSPID |
| 1012 | 20 | I/O/T | RTC_GPIO12, GPIO12, TOUCH12, ADC2_CH1, FSPICLK, FSPIIO6, SUBSPICLK |
| 1013 | 21 | I/O/T | RTC_GPIO13, GPIO13, TOUCH13, ADC2_CH2, FSPIQ, FSPIIO7, SUBSPIQ |
| 1014 | 22 | I/O/T | RTC_GPIO14, GPIO14, TOUCH14, ADC2_CH3, FSPIWP, FSPIDQS, SUBSPIWP |
| 1021 | 23 | I/O/T | RTC_GPIO21, GPIO21 |
| $1047^{C}$ | 24 | I/O/T | SPICLK_P_DIFF,GPIO47, SUBSPICLK_P_DIFF |
| $1048^{C}$ | 25 | I/O/T | SPICLK_N_DIFF,GPIO48, SUBSPICLK_N_DIFF |
| 1045 | 26 | I/O/T | GPIO45 |
| 100 | 27 | I/O/T | RTC_GPIOO, GPIOO |
| $1035^{b}$ | 28 | I/O/T | SPIIO6, GPIO35, FSPID, SUBSPID |
| $1036^{b}$ | 29 | I/O/T | SPIIO7, GPIO36, FSPICLK, SUBSPICLK |
| $1037^{b}$ | 30 | I/O/T | SPIDQS, GPIO37, FSPIQ, SUBSPIQ |
| 1038 | 31 | I/O/T | GPIO38, FSPIWP, SUBSPIWP |Table 3-1 - cont'd from previous page

| Name | No. | Type ${ }^{\text {a }}$ | Function |
| :-- | :--: | :--: | :-- |
| IO39 | 32 | I/O/T | MTCK, GPIO39, CLK_OUT3, SUBSPICS1 |
| IO40 | 33 | I/O/T | MTDO, GPIO40, CLK_OUT2 |
| IO41 | 34 | I/O/T | MTDI, GPIO41, CLK_OUT1 |
| IO42 | 35 | I/O/T | MTMS, GPIO42 |
| RXDO | 36 | I/O/T | UORXD, GPIO44, CLK_OUT2 |
| TXDO | 37 | I/O/T | UOTXD, GPIO43, CLK_OUT1 |
| IO2 | 38 | I/O/T | RTC_GPIO2, GPIO2, TOUCH2, ADC1_CH1 |
| IO1 | 39 | I/O/T | RTC_GPIO1, GPIO1, TOUCH1, ADC1_CHO |
| GND | 40 | P | GND |
| EPAD | 41 | P | GND |

${ }^{a} \mathrm{P}$ : power supply; I: input; O: output; T: high impedance. Pin functions in bold font are the default pin functions. For pin $28 \sim 30$, the default function is decided by eFuse bit.
${ }^{b}$ For modules with Octal SPI PSRAM, i.e., modules embedded with ESP32-S3R8 or ESP32-S3R16V, pins IO35, IO36, and IO37 are connected to the Octal SPI PSRAM and are not available for other uses.
${ }^{c}$ For modules embedded with ESP32-S3R16V, as the VDD_SPI voltage of the ESP32-S3R16V chip is set to 1.8 V , the working voltage for GPIO47 and GPIO48 is also 1.8 V , which is different from other GPIOs.# 4 Boot Configurations 

## Note:

The content below is excerpted from ESP32-S3 Series Datasheet > Section Boot Configurations. For the strapping pin mapping between the chip and modules, please refer to Chapter 8 Module Schematics.

The chip allows for configuring the following boot parameters through strapping pins and eFuse bits at power-up or a hardware reset, without microcontroller interaction.

## - Chip boot mode

- Strapping pin: GPIOO and GPIO46
- VDD_SPI voltage
- Strapping pin: GPIO45
- eFuse parameter: EFUSE_VDD_SPI_FORCE and EFUSE_VDD_SPI_TIEH
- ROM message printing
- Strapping pin: GPIO46
- eFuse parameter: EFUSE_UART_PRINT_CONTROL and EFUSE_DIS_USB_SERIAL_JTAG_ROM_PRINT
- JTAG signal source
- Strapping pin: GPIO3
- eFuse parameter: EFUSE_DIS_PAD_JTAG, EFUSE_DIS_USB_JTAG, and EFUSE_STRAP_JTAG_SEL

The default values of all the above eFuse parameters are 0 , which means that they are not burnt. Given that eFuse is one-time programmable, once programmed to 1 , it can never be reverted to 0 . For how to program eFuse parameters, please refer to ESP32-S3 Technical Reference Manual > Chapter eFuse Controller.

The default values of the strapping pins, namely the logic levels, are determined by pins' internal weak pull-up/pull-down resistors at reset if the pins are not connected to any circuit, or connected to an external high-impedance circuit.

Table 4-1. Default Configuration of Strapping Pins

| Strapping Pin | Default Configuration | Bit Value |
| :-- | :--: | :--: |
| GPIOO | Weak pull-up | 1 |
| GPIO3 | Floating | - |
| GPIO45 | Weak pull-down | 0 |
| GPIO46 | Weak pull-down | 0 |

To change the bit values, the strapping pins should be connected to external pull-down/pull-up resistances. If the ESP32-S3 is used as a device by a host MCU, the strapping pin voltage levels can also be controlled by the host MCU.

All strapping pins have latches. At system reset, the latches sample the bit values of their respective strapping pins and store them until the chip is powered down or shut down. The states of latches cannot be changed inany other way. It makes the strapping pin values available during the entire chip operation, and the pins are freed up to be used as regular IO pins after reset.

The timing of signals connected to the strapping pins should adhere to the setup time and hold time specifications in Table 4-2 and Figure 4-1.

Table 4-2. Description of Timing Parameters for the Strapping Pins

| Parameter | Description | Min (ms) |
| :-- | :-- | :--: |
| $\mathrm{t}_{S U}$ | Setup time is the time reserved for the power rails to stabilize be- <br> fore the EN pin is pulled high to activate the chip. | 0 |
| $\mathrm{t}_{H}$ | Hold time is the time reserved for the chip to read the strapping <br> pin values after EN is already high and before these pins start op- <br> erating as regular IO pins. | 3 |

![img-7.jpeg](img-7.jpeg)

Figure 4-1. Visualization of Timing Parameters for the Strapping Pins

# 4.1 Chip Boot Mode Control 

GPIOO and GPIO46 control the boot mode after the reset is released. See Table 4-3 Chip Boot Mode Control.

Table 4-3. Chip Boot Mode Control

| Boot Mode | GPIOO | GPIO46 |
| :-- | :--: | :--: |
| SPI Boot | 1 | Any value |
| Joint Download Boot ${ }^{2}$ | 0 | 0 |

${ }^{1}$ Bold marks the default value and configuration.
2 Joint Download Boot mode supports the following download methods:

- USB Download Boot:

- USB-Serial-JTAG Download Boot
- USB-OTG Download Boot
- UART Download BootIn SPI Boot mode, the ROM bootloader loads and executes the program from SPI flash to boot the system.

In Joint Download Boot mode, users can download binary files into flash using UARTO or USB interface. It is also possible to download binary files into SRAM and execute it from SRAM.

In addition to SPI Boot and Joint Download Boot modes, ESP32-S3 also supports SPI Download Boot mode. For details, please see ESP32-S3 Technical Reference Manual > Chapter Chip Boot Control.

# 4.2 VDD_SPI Voltage Control 

Depending on the value of EFUSE_VDD_SPI_FORCE, the voltage can be controlled in two ways.
Table 4-4. VDD_SPI Voltage Control

| VDD_SPI power source ${ }^{2}$ | Voltage | EFUSE_VDD_SPI_FORCE | GPIO45 | EFUSE_VDD_SPI_TIEH |
| :-- | :--: | :--: | :--: | :--: |
| VDD3P3_RTC via $\mathbf{R}_{S P I}$ | 3.3 V | 0 | 0 | Ignored |
| Flash Voltage Regulator | 1.8 V | 1 | 1 |  |
| Flash Voltage Regulator | 1.8 V | 1 | Ignored | 0 |
| VDD3P3_RTC via $\mathrm{R}_{S P I}$ | 3.3 V |  |  | 1 |

${ }^{1}$ Bold marks the default value and configuration.
2 See ESP32-S3 Series Datasheet > Section Power Scheme.

### 4.3 ROM Messages Printing Control

During boot process the messages by the ROM code can be printed to:

- (Default) UARTO and USB Serial/JTAG controller
- USB Serial/JTAG controller
- UARTO

The ROM messages printing to UART or USB Serial/JTAG controller can be respectively disabled by configuring registers and eFuse. For detailed information, please refer to ESP32-S3 Technical Reference Manual > Chapter Chip Boot Control.

### 4.4 JTAG Signal Source Control

The strapping pin GPIO3 can be used to control the source of JTAG signals during the early boot process. This pin does not have any internal pull resistors and the strapping value must be controlled by the external circuit that cannot be in a high impedance state.

As Table 4-5 shows, GPIO3 is used in combination with EFUSE_DIS_PAD_JTAG, EFUSE_DIS_USB_JTAG, and EFUSE_STRAP_JTAG_SEL.Table 4-5. JTAG Signal Source Control

| JTAG Signal Source | EFUSE_DIS_PAD_JTAG | EFUSE_DIS_USB_JTAG | EFUSE_STRAP_JTAG_SEL | GPIO3 |
| :--: | :--: | :--: | :--: | :--: |
| USB Serial/JTAG Controller | 0 | 0 | 0 | Ignored |
|  | 0 | 0 | 1 | 1 |
|  | 1 | 0 | Ignored | Ignored |
| JTAG pins 2 | 0 | 0 | 1 | 0 |
|  | 0 | 1 | Ignored | Ignored |
| JTAG is disabled | 1 | 1 | Ignored | Ignored |

1 Bold marks the default value and configuration.
2 JTAG pins refer to MTDI, MTCK, MTMS, and MTDO.

# 4.5 Chip Power-up and Reset 

Once the power is supplied to the chip, its power rails need a short time to stabilize. After that, EN - the pin used for power-up and reset - is pulled high to activate the chip. For information on EN as well as power-up and reset timing, see Figure 4-2 and Table 4-6.
![img-8.jpeg](img-8.jpeg)

Figure 4-2. Visualization of Timing Parameters for Power-up and Reset

Table 4-6. Description of Timing Parameters for Power-up and Reset

| Parameter | Description | Min ( $\mu \mathrm{s}$ ) |
| :-- | :-- | :--: |
| $\mathrm{t}_{\text {STBL }}$ | Time reserved for the power rails of VDDA, VDD3P3, <br> VDD3P3_RTC, and VDD3P3_CPU to stabilize before the EN <br> pin is pulled high to activate the chip | 50 |
| $\mathrm{t}_{\text {RST }}$ | Time reserved for EN to stay below $\mathrm{V}_{I L, \mu R S T}$ to reset the chip <br> (see Table 6-3) | 50 |# 5 Peripherals 

### 5.1 Peripheral Overview

ESP32-S3 integrates a rich set of peripherals including SPI, LCD, Camera interface, UART, I2C, I2S, remote control, pulse counter, LED PWM, USB Serial/JTAG, MCPWM, SD/MMC host controller, TWAI ${ }^{\circledR}$ controller (compatible with ISO 11898-1, i.e., CAN Specification 2.0), ADC, touch sensor, and temperature sensor. It also includes a full-speed USB 2.0 On-The-Go (OTG) interface to enable USB communication.

To learn more about on-chip components, please refer to ESP32-S3 Series Datasheet > Section Functional Description.


#### Abstract

Note: The content below is sourced from ESP32-S3 Series Datasheet > Section Peripherals. Some information may not be applicable to ESP32-S3-WROOM-1 and ESP32-S3-WROOM-1U as not all the IO signals are exposed on the module. To learn more about peripheral signals, please refer to ESP32-S3 Technical Reference Manual > Section Peripheral Signals via GPIO Matrix.


### 5.2 Peripheral Description

This section describes the chip's peripheral capabilities, covering connectivity interfaces and on-chip sensors that extend its functionality.

### 5.2.1 Connectivity Interface

This subsection describes the connectivity interfaces on the chip that enable communication and interaction with external devices and networks.

### 5.2.1.1 UART Controller

ESP32-S3 has three UART (Universal Asynchronous Receiver Transmitter) controllers, i.e., UARTO, UART1, and UART2, which support IrDA and asynchronous communication (RS232 and RS485) at a speed of up to 5 Mbps.

## Feature List

- Three clock sources that can be divided
- Programmable baud rate
- 1024 x 8-bit RAM shared by TX FIFOs and RX FIFOs of the three UART controllers
- Full-duplex asynchronous communication
- Automatic baud rate detection of input signals
- Data bits ranging from 5 to 8
- Stop bits of 1, 1.5, 2, or 3 bits
- Parity bit- Special character AT_CMD detection
- RS485 protocol
- IrDA protocol
- High-speed data communication using GDMA
- UART as wake-up source
- Software and hardware flow control

For details, see ESP32-S3 Technical Reference Manual > Chapter UART Controller.

# Pin Assignment 

- UARTO
- The pins UOTXD and UORXD that are connected to transmit and receive signals are multiplexed with GPIO13 GPIO44 via IO MUX, and can also be connected to any GPIO via the GPIO Matrix.
- The pins UORTS and UOCTS that are connected to hardware flow control signals are multiplexed with GPIO15 GPIO16, RTC_GPIO15 RTC_GPIO16, XTAL_32K_P and XTAL_32K_N, and SAR ADC2 interface via IO MUX, and can also be connected to any GPIO via the GPIO Matrix.
- The pins UODTR and UODSR that are connected to hardware flow control signals can be chosen from any GPIO via the GPIO Matrix.
- UART1
- The pins U1TXD and U1RXD that are connected to transmit and receive signals are multiplexed with GPIO17 GPIO18, RTC_GPIO17 RTC_GPIO18, and SAR ADC2 interface via IO MUX, and can also be connected to any GPIO via the GPIO Matrix.
- The pins U1RTS and U1CTS that are connected to hardware flow control signals are multiplexed with GPIO19 GPIO20, RTC_GPIO19 RTC_GPIO20, USB_D- and USB_D+ pins, and SAR ADC2 interface via IO MUX, and can also be connected to any GPIO via the GPIO Matrix.
- The pins U1DTR and U1DSR that are connected to hardware flow control signals can be chosen from any GPIO via the GPIO Matrix.
- UART2: The pins used can be chosen from any GPIO via the GPIO Matrix.

For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.2 I2C Interface

ESP32-S3 has two I2C bus interfaces which are used for I2C master mode or slave mode, depending on the user's configuration.

## Feature List

- Standard mode (100 kbit/s)
- Fast mode (400 kbit/s)
- Up to 800 kbit/s (constrained by SCL and SDA pull-up strength)- 7-bit and 10-bit addressing mode
- Double addressing mode (slave addressing and slave register addressing)

The hardware provides a command abstraction layer to simplify the usage of the I2C peripheral.
For details, see ESP32-S3 Technical Reference Manual > Chapter I2C Controller.

# Pin Assignment 

For I2C, the pins used can be chosen from any GPIOs via the GPIO Matrix.
For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.3 I2S Interface

ESP32-S3 includes two standard I2S interfaces. They can operate in master mode or slave mode, in full-duplex mode or half-duplex communication mode, and can be configured to operate with an 8-bit, 16-bit, 24-bit, or 32-bit resolution as an input or output channel. BCK clock frequency, from 10 kHz up to 40 MHz , is supported.

The I2S interface has a dedicated DMA controller. It supports TDM PCM, TDM MSB alignment, TDM LSB alignment, TDM Phillips, and PDM interface.

## Pin Assignment

For I2S, the pins used can be chosen from any GPIOs via the GPIO Matrix.
For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.4 LCD and Camera Controller

The LCD and Camera controller of ESP32-S3 consists of a LCD module and a camera module.
The LCD module is designed to send parallel video data signals, and its bus supports 8-bit 16-bit parallel RGB, I8080, and MOTO6800 interfaces. These interfaces operate at 40 MHz or lower, and support conversion among RGB565, YUV422, YUV420, and YUV411.

The camera module is designed to receive parallel video data signals, and its bus supports an 8-bit 16-bit DVP image sensor, with clock frequency of up to 40 MHz . The camera interface supports conversion among RGB565, YUV422, YUV420, and YUV411.

## Pin Assignment

For LCD and Camera controller, the pins used can be chosen from any GPIOs via the GPIO Matrix.
For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.5 Serial Peripheral Interface (SPI)

ESP32-S3 has the following SPI interfaces:- SPIO used by ESP32-S3's GDMA controller and cache to access in-package or off-package flash/PSRAM
- SPI1 used by the CPU to access in-package or off-package flash/PSRAM
- SPI2 is a general purpose SPI controller with access to a DMA channel allocated by the GDMA controller
- SPI3 is a general purpose SPI controller with access to a DMA channel allocated by the GDMA controller


# Feature List 

- SPIO and SPI1:
- Supports Single SPI, Dual SPI, Quad SPI, Octal SPI, QPI, and OPI modes
- 8-line SPI mode supports single data rate (SDR) and double data rate (DDR)
- Configurable clock frequency with a maximum of 120 MHz for 8-line SPI SDR/DDR modes
- Data transmission is in bytes
- SPI2:
- Supports operation as a master or slave
- Connects to a DMA channel allocated by the GDMA controller
- Supports Single SPI, Dual SPI, Quad SPI, Octal SPI, QPI, and OPI modes
- Configurable clock polarity (CPOL) and phase (CPHA)
- Configurable clock frequency
- Data transmission is in bytes
- Configurable read and write data bit order: most-significant bit (MSB) first, or least-significant bit (LSB) first
- As a master
* Supports 2-line full-duplex communication with clock frequency up to 80 MHz
* Full-duplex 8-line SPI mode supports single data rate (SDR) only
* Supports 1-, 2-, 4-, 8-line half-duplex communication with clock frequency up to 80 MHz
* Half-duplex 8-line SPI mode supports both single data rate (up to 80 MHz ) and double data rate (up to 40 MHz )
* Provides six SPI_CS pins for connection with six independent SPI slaves
* Configurable CS setup time and hold time
- As a slave
* Supports 2-line full-duplex communication with clock frequency up to 60 MHz
* Supports 1-, 2-, 4-line half-duplex communication with clock frequency up to 60 MHz
* Full-duplex and half-duplex 8-line SPI mode supports single data rate (SDR) only
- SPI3:
- Supports operation as a master or slave- Connects to a DMA channel allocated by the GDMA controller
- Supports Single SPI, Dual SPI, Quad SPI, and QPI modes
- Configurable clock polarity (CPOL) and phase (CPHA)
- Configurable clock frequency
- Data transmission is in bytes
- Configurable read and write data bit order: most-significant bit (MSB) first, or least-significant bit (LSB) first
- As a master
* Supports 2-line full-duplex communication with clock frequency up to 80 MHz
* Supports 1-, 2-, 4-line half-duplex communication with clock frequency up to 80 MHz
* Provides three SPI_CS pins for connection with three independent SPI slaves
* Configurable CS setup time and hold time
- As a slave
* Supports 2-line full-duplex communication with clock frequency up to 60 MHz
* Supports 1-, 2-, 4-line half-duplex communication with clock frequency up to 60 MHz

For details, see ESP32-S3 Technical Reference Manual > Chapter SPI Controller.

Pin Assignment

# Note: 

Please refer to ESP32-S3 Series Datasheet > Section IO MUX Function > Table IO MUX Pin Functions for the corresponding SPI interface details.

- SPIO/1
- Via IO MUX:
* Interface $4 a$ is multiplexed with GPIO26 GPIO32 via IO MUX. When used in conjunction with $4 b$, it can operate as the lower 4 bits data line interface and the CLK, CSO, and CS1 interfaces in 8 -line SPI mode.
* Interface $4 b$ is multiplexed with GPIO33 GPIO37 and SPI interfaces $4 e$ and $4 f$ via IO MUX. When used in conjunction with $4 a$, it can operate as the higher 4 bits data line interface and DQS interface in 8 -line SPI mode.
* Interface $4 d$ is multiplexed with GPIO8 GPIO14, RTC_GPIO8 RTC_GPIO14, Touch Sensor interface, SAR ADC interface, and SPI interfaces $4 c$ and $4 g$ via IO MUX. Note that the fast SPI2 interface will not be available.
* Interface $4 e$ is multiplexed with GPIO33 GPIO39, JTAG MTCK interface, and SPI interfaces $4 b$ and $4 f$ via IO MUX. It is an alternative group of signal lines that can be used if SPIO/1 does not use 8 -line SPI connection.
- Via GPIO Matrix: The pins used can be chosen from any GPIOs via the GPIO Matrix.
- SPI2- Via IO MUX:
* Interface 4c is multiplexed with GPIO9 GPIO14, RTC_GPIO9 RTC_GPIO14, Touch Sensor interface, SAR ADC interface, and SPI interfaces $4 d$ and $4 g$ via IO MUX. It is the SPI2 main interface for fast SPI connection.
* (not recommended) Interface $4 f$ is multiplexed with GPIO33 GPIO38, SPI interfaces $4 e$ and $4 b$ via IO MUX. It is the alternative SPI2 interface if the main SPI2 is not available. Its performance is comparable to SPI2 via GPIO matrix, so use the GPIO matrix instead.
* (not recommended) Interface $4 g$ is multiplexed with GPIO10 GPIO14, RTC_GPIO10 RTC_GPIO14, Touch Sensor interface, SAR ADC interface, and SPI interfaces $4 c$ and $4 d$ via IO MUX. It is the alternative SPI2 interface signal lines for 8-line SPI connection.
- Via GPIO Matrix: The pins used can be chosen from any GPIOs via the GPIO Matrix.
- SPI3: The pins used can be chosen from any GPIOs via the GPIO Matrix.

For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

# 5.2.1.6 Two-Wire Automotive Interface (TWAI ${ }^{\circledR}$ ) 

The Two-Wire Automotive Interface (TWAI ${ }^{\circledR}$ ) is a multi-master, multi-cast communication protocol with error detection and signaling as well as inbuilt message priorities and arbitration.

## Feature List

- Compatible with ISO 11898-1 protocol (CAN Specification 2.0)
- Standard frame format (11-bit ID) and extended frame format (29-bit ID)
- Bit rates from $1 \mathrm{Kbit} / \mathrm{s}$ to $1 \mathrm{Mbit} / \mathrm{s}$
- Multiple modes of operation:
- Normal
- Listen Only
- Self-Test (no acknowledgment required)
- 64-byte receive FIFO
- Acceptance filter (single and dual filter modes)
- Error detection and handling:
- Error counters
- Configurable error interrupt threshold
- Error code capture
- Arbitration lost capture

For details, see ESP32-S3 Technical Reference Manual > Chapter Two-wire Automotive Interface.# Pin Assignment 

For TWAI, the pins used can be chosen from any GPIOs via the GPIO Matrix.
For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.7 USB 2.0 OTG Full-Speed Interface

ESP32-S3 features a full-speed USB OTG interface along with an integrated transceiver. The USB OTG interface complies with the USB 2.0 specification.

## General Features

- FS and LS data rates
- HNP and SRP as A-device or B-device
- Dynamic FIFO (DFIFO) sizing
- Multiple modes of memory access
- Scatter/Gather DMA mode
- Buffer DMA mode
- Slave mode
- Can choose integrated transceiver or external transceiver
- Utilizing integrated transceiver with USB Serial/JTAG by time-division multiplexing when only integrated transceiver is used
- Support USB OTG using one of the transceivers while USB Serial/JTAG using the other one when both integrated transceiver or external transceiver are used


## Device Mode Features

- Endpoint number 0 always present (bi-directional, consisting of EPO IN and EPO OUT)
- Six additional endpoints (endpoint numbers 1 to 6), configurable as IN or OUT
- Maximum of five IN endpoints concurrently active at any time (including EPO IN)
- All OUT endpoints share a single RX FIFO
- Each IN endpoint has a dedicated TX FIFO


## Host Mode Features

- Eight channels (pipes)
- A control pipe consists of two channels (IN and OUT), as IN and OUT transactions must be handled separately. Only Control transfer type is supported.
- Each of the other seven channels is dynamically configurable to be IN or OUT, and supports Bulk, Isochronous, and Interrupt transfer types.- All channels share an RX FIFO, non-periodic TX FIFO, and periodic TX FIFO. The size of each FIFO is configurable.

For details, see ESP32-S3 Technical Reference Manual > Chapter USB On-The-Go.

# Pin Assignment 

When using the on-chip PHY, the differential signal pins USB_D- and USB_D+ of the USB OTG are multiplexed with GPIO19 GPIO2O, RTC_GPIO19 RTC_GPIO2O, UART1 interface, and SAR ADC2 interface via IO MUX.

When using external PHY, the USB OTG pins are multiplexed with GPIO21, RTC_GPIO21, GPIO38 GPIO42, and SPI interface via IO MUX:

- VP signal connected to MTMS pin
- VM signal connected to MTDI pin
- RCV signal connected to GPIO21
- OEN signal connected to MTDO pin
- VPO signal connected to MTCK pin
- VMO signal connected to GPIO38

For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.8 USB Serial/JTAG Controller

ESP32-S3 integrates a USB Serial/JTAG controller.

## Feature List

- USB Full-speed device.
- Can be configured to either use internal USB PHY of ESP32-S3 or external PHY via GPIO matrix.
- Fixed function device, hardwired for CDC-ACM (Communication Device Class - Abstract Control Model) and JTAG adapter functionality.
- Two OUT Endpoints, three IN Endpoints in addition to Control Endpoint 0; Up to 64-byte data payload size.
- Internal PHY, so no or very few external components needed to connect to a host computer.
- CDC-ACM adherent serial port emulation is plug-and-play on most modern OSes.
- JTAG interface allows fast communication with CPU debug core using a compact representation of JTAG instructions.
- CDC-ACM supports host controllable chip reset and entry into download mode.

For details, see ESP32-S3 Technical Reference Manual > Chapter USB Serial/JTAG Controller.# Pin Assignment 

When using the on-chip PHY, the differential signal pins USB_D- and USB_D+ of the USB Serial/JTAG controller are multiplexed with GPIO19 GPIO2O, RTC_GPIO19 RTC_GPIO2O, UART1 interface, and SAR ADC2 interface via IO MUX.

When using external PHY, the USB Serial/JTAG controller pins are multiplexed with GPIO38 GPIO42 and SPI interface via IO MUX:

- VP signal connected to MTMS pin
- VM signal connected to MTDI pin
- OEN signal connected to MTDO pin
- VPO signal connected to MTCK pin
- VMO signal connected to GPIO38

For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.9 SD/MMC Host Controller

ESP32-S3 has an SD/MMC Host controller.

## Feature List

- Secure Digital (SD) memory version 3.0 and version 3.01
- Secure Digital I/O (SDIO) version 3.0
- Consumer Electronics Advanced Transport Architecture (CE-ATA) version 1.1
- Multimedia Cards (MMC version 4.41, eMMC version 4.5 and version 4.51)
- Up to 80 MHz clock output
- Three data bus modes:
- 1-bit
- 4-bit (supports two SD/SDIO/MMC 4.41 cards, and one SD card operating at 1.8 V in 4-bit mode)
- 8-bit

For details, see ESP32-S3 Technical Reference Manual > Chapter SD/MMC Host Controller.

## Pin Assignment

For SD/MMC Host, the pins used can be chosen from any GPIOs via the GPIO Matrix.
For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.10 LED PWM Controller

The LED PWM controller can generate independent digital waveforms on eight channels.# Feature List 

- Can generate a digital waveform with configurable periods and duty cycle. The duty cycle resolution can be up to 14 bits within a 1 ms period
- Multiple clock sources, including APB clock and external main crystal clock
- Can operate when the CPU is in Light-sleep mode
- Gradual increase or decrease of duty cycle, useful for the LED RGB color-fading generator

For details, see ESP32-S3 Technical Reference Manual > Chapter LED PWM Controller.

## Pin Assignment

For LED PWM, the pins used can be chosen from any GPIOs via the GPIO Matrix.
For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.11 Motor Control PWM (MCPWM)

ESP32-S3 integrates two MCPWMs that can be used to drive digital motors and smart light. Each MCPWM peripheral has one clock divider (prescaler), three PWM timers, three PWM operators, and a capture module. PWM timers are used for generating timing references. The PWM operators generate desired waveform based on the timing references. Any PWM operator can be configured to use the timing references of any PWM timers. Different PWM operators can use the same PWM timer's timing references to produce related PWM signals. PWM operators can also use different PWM timers' values to produce the PWM signals that work alone. Different PWM timers can also be synchronized together.

For details, see ESP32-S3 Technical Reference Manual > Chapter Motor Control PWM.

## Pin Assignment

For MCPWM, the pins used can be chosen from any GPIOs via the GPIO Matrix.
For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.12 Remote Control Peripheral (RMT)

The Remote Control Peripheral (RMT) is designed to send and receive infrared remote control signals.

## Feature List

- Four TX channels
- Four RX channels
- Support multiple channels (programmable) transmitting data simultaneously
- Eight channels share a $384 \times 32$-bit RAM
- Support modulation on TX pulses
- Support filtering and demodulation on RX pulses- Wrap TX mode
- Wrap RX mode
- Continuous TX mode
- DMA access for TX mode on channel 3
- DMA access for RX mode on channel 7

For details, see ESP32-S3 Technical Reference Manual > Chapter Remote Control Peripheral.

# Pin Assignment 

For RMT, the pins used can be chosen from any GPIOs via the GPIO Matrix.
For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.1.13 Pulse Count Controller (PCNT)

The pulse count controller (PCNT) captures pulse and counts pulse edges through multiple modes.

## Feature List

- Four independent pulse counters (units) that count from 1 to 65535
- Each unit consists of two independent channels sharing one pulse counter
- All channels have input pulse signals (e.g. sig_chO_un) with their corresponding control signals (e.g. ctrI_chO_un)
- Independently filter glitches of input pulse signals (sig_chO_un and sig_ch1_un) and control signals (ctrl_chO_un and ctrl_ch1_un) on each unit
- Each channel has the following parameters:

1. Selection between counting on positive or negative edges of the input pulse signal
2. Configuration to Increment, Decrement, or Disable counter mode for control signal's high and low states

For details, see ESP32-S3 Technical Reference Manual > Chapter Pulse Count Controller.

## Pin Assignment

For pulse count controller, the pins used can be chosen from any GPIOs via the GPIO Matrix.
For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.2 Analog Signal Processing

This subsection describes components on the chip that sense and process real-world data.# 5.2.2.1 SAR ADC 

ESP32-S3 integrates two 12-bit SAR ADCs and supports measurements on 20 channels (analog-enabled pins). For power-saving purpose, the ULP coprocessors in ESP32-S3 can also be used to measure voltage in sleep modes. By using threshold settings or other methods, we can awaken the CPU from sleep modes.

For more details, see ESP32-S3 Technical Reference Manual > Chapter On-Chip Sensors and Analog Signal Processing.

## Pin Assignment

The pins for the SAR ADC are multiplexed with GPIO1 GPIO2O, RTC_GPIO1 RTC_GPIO2O, Touch Sensor interface, SPI interface, UART interface, and USB_D- and USB_D+ pins via IO MUX.

For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.

### 5.2.2.2 Temperature Sensor

The temperature sensor generates a voltage that varies with temperature. The voltage is internally converted via an ADC into a digital value.

The temperature sensor has a range of $-40^{\circ} \mathrm{C}$ to $125^{\circ} \mathrm{C}$. It is designed primarily to sense the temperature changes inside the chip. The temperature value depends on factors such as microcontroller clock frequency or I/O load. Generally, the chip's internal temperature is higher than the ambient temperature.

For more details, see ESP32-S3 Technical Reference Manual > Chapter On-Chip Sensors and Analog Signal Processing.

### 5.2.2.3 Touch Sensor

ESP32-S3 has 14 capacitive-sensing GPIOs, which detect variations induced by touching or approaching the GPIOs with a finger or other objects. The low-noise nature of the design and the high sensitivity of the circuit allow relatively small pads to be used. Arrays of pads can also be used, so that a larger area or more points can be detected. The touch sensing performance can be further enhanced by the waterproof design and digital filtering feature.

Note:
ESP32-S3 touch sensor has not passed the Conducted Susceptibility (CS) test for now, and thus has limited application scenarios.

For more details, see ESP32-S3 Technical Reference Manual > Chapter On-Chip Sensors and Analog Signal Processing.

## Pin Assignment

The pins for touch sensor are multiplexed with GPIO1 GPIO14, RTC_GPIO1 RTC_GPIO14, SAR ADC interface, and SPI interface via IO MUX.

For more information about the pin assignment, see ESP32-S3 Series Datasheet > Section IO Pins and ESP32-S3 Technical Reference Manual > Chapter IO MUX and GPIO Matrix.# 6 Electrical Characteristics 

### 6.1 Absolute Maximum Ratings

Stresses above those listed in Table 6-1 Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only and functional operation of the device at these or any other conditions beyond those indicated under Table 6-2 Recommended Operating Conditions is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

Table 6-1. Absolute Maximum Ratings

| Symbol | Parameter | Min | Max | Unit |
| :-- | :-- | :--: | :--: | :--: |
| VDD33 | Power supply voltage | -0.3 | 3.6 | V |
| $\mathrm{~T}_{\text {STORE }}$ | Storage temperature | -40 | 105 | ${ }^{\circ} \mathrm{C}$ |

### 6.2 Recommended Operating Conditions

Table 6-2. Recommended Operating Conditions

| Symbol | Parameter | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| VDD33 | Power supply voltage | 3.0 | 3.3 | 3.6 | V |
| $\mathrm{I}_{V D D}$ | Current delivered by external power supply | 0.5 | - | - | A |
| $\mathrm{T}_{A}$ | Operating ambient temperature | $65^{\circ} \mathrm{C}$ version | -40 | - | 65 | ${ }^{\circ} \mathrm{C}$ |
|  |  | $85^{\circ} \mathrm{C}$ version |  |  | 85 |  |
|  |  | $105^{\circ} \mathrm{C}$ version |  |  | 105 |  |

### 6.3 DC Characteristics $\left(3.3 \mathrm{~V}, 25^{\circ} \mathrm{C}\right)$

Table 6-3. DC Characteristics $\left(3.3 \mathrm{~V}, 25^{\circ} \mathrm{C}\right)$

| Parameter | Description | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $\mathrm{C}_{I N}$ | Pin capacitance | - | 2 | - | pF |
| $\mathrm{V}_{I H}$ | High-level input voltage | $0.75 \times \mathrm{VDD}^{1}$ | - | VDD $^{1}+0.3$ | V |
| $\mathrm{V}_{I L}$ | Low-level input voltage | $-0.3$ | - | $0.25 \times$ VDD $^{1}$ | V |
| $\mathrm{I}_{I H}$ | High-level input current | - | - | 50 | nA |
| $\mathrm{I}_{I L}$ | Low-level input current | - | - | 50 | nA |
| $\mathrm{V}_{\text {OH }}{ }^{2}$ | High-level output voltage | $0.8 \times$ VDD $^{1}$ | - | - | V |
| $\mathrm{V}_{\text {OL }}{ }^{2}$ | Low-level output voltage | - | - | $0.1 \times$ VDD $^{1}$ | V |
| $\mathrm{I}_{O H}$ | High-level source current (VDD ${ }^{1}=3.3 \mathrm{~V}$, <br> $\mathrm{V}_{\text {OH }}$ >= 2.64 V, PAD_DRIVER = 3) | - | 40 | - | mA |
| $\mathrm{I}_{O L}$ | Low-level sink current (VDD ${ }^{1}=3.3 \mathrm{~V}, \mathrm{~V}_{O L}=$ <br> 0.495 V, PAD_DRIVER = 3) | - | 28 | - | mA |
| $\mathrm{R}_{P U}$ | Internal weak pull-up resistor | - | 45 | - | $\mathrm{k} \Omega$ |
| $\mathrm{R}_{P D}$ | Internal weak pull-down resistor | - | 45 | - | $\mathrm{k} \Omega$ || $\mathrm{V}_{I H_{-} \text {nRST }}$ | Chip reset release voltage (EN voltage is <br> within the specified range) | $0.75 \times \mathrm{VDD}^{1}$ | - | VDD $^{1}+0.3$ | V |
| :-- | :-- | --: | --: | :--: | :--: |
| $\mathrm{V}_{\text {IL_nRST }}$ | Chip reset voltage (EN voltage is within the <br> specified range) | -0.3 | - | $0.25 \times \mathrm{VDD}^{1}$ | V |

${ }^{1}$ VDD - voltage from a power pin of a respective power domain.
$2 \mathrm{~V}_{O H}$ and $\mathrm{V}_{O L}$ are measured using high-impedance load.

# 6.4 Current Consumption Characteristics 

### 6.4.1 Current Consumption in Active Mode

With the use of advanced power-management technologies, the module can switch between different power modes. For details on different power modes, please refer to Section Power Management Unit in ESP32-S3 Series Datasheet.

The current consumption measurements are taken with a 3.3 V supply at $25^{\circ} \mathrm{C}$ ambient temperature.
TX current consumption is rated at a 100\% duty cycle.
RX current consumption is rated when the peripherals are disabled and the CPU idle.

Table 6-4. Current Consumption in Avtice Mode

| Work mode | Description |  | Peak (mA) |
| :--: | :--: | :--: | :--: |
| Active (RF working) | TX | 802.11b, 1 Mbps, @20.5 dBm | 355 |
|  |  | 802.11g, 54 Mbps, @18 dBm | 297 |
|  |  | 802.11n, HT20, MCS 7, @17.5 dBm | 286 |
|  |  | 802.11n, HT40, MCS 7, @17 dBm | 285 |
|  | RX | 802.11b/g/n, HT20 | 95 |
|  |  | 802.11n, HT40 | 97 |

Note:
The content below is excerpted from Section Power Consumption in Other Modes in ESP32-S3 Series Datasheet.

### 6.4.2 Current Consumption in Other Modes

Please note that if the chip embedded has in-package PSRAM, the current consumption of the module might be higher compared to the measurements below.Table 6-5. Current Consumption in Modem-sleep Mode

| Work mode | Frequency <br> (MHz) | Description | Typ $^{1}$ <br> (mA) | Typ $^{2}$ <br> (mA) |
| :--: | :--: | :--: | :--: | :--: |
| Modem-sleep ${ }^{3}$ | 40 | WAITI (Dual core in idle state) | 13.2 | 18.8 |
|  |  | Single core running 32-bit data access instructions, the other core in idle state | 16.2 | 21.8 |
|  |  | Dual core running 32-bit data access instructions | 18.7 | 24.4 |
|  |  | Single core running 128-bit data access instructions, the other core in idle state | 19.9 | 25.4 |
|  |  | Dual core running 128-bit data access instructions | 23.0 | 28.8 |
|  | 80 | WAITI | 22.0 | 36.1 |
|  |  | Single core running 32-bit data access instructions, the other core in idle state | 28.4 | 42.6 |
|  |  | Dual core running 32-bit data access instructions | 33.1 | 47.3 |
|  |  | Single core running 128-bit data access instructions, the other core in idle state | 35.1 | 49.6 |
|  |  | Dual core running 128-bit data access instructions | 41.8 | 56.3 |
|  | 160 | WAITI | 27.6 | 42.3 |
|  |  | Single core running 32-bit data access instructions, the other core in idle state | 39.9 | 54.6 |
|  |  | Dual core running 32-bit data access instructions | 49.6 | 64.1 |
|  |  | Single core running 128-bit data access instructions, the other core in idle state | 54.4 | 69.2 |
|  |  | Dual core running 128-bit data access instructions | 66.7 | 81.1 |
|  | 240 | WAITI | 32.9 | 47.6 |
|  |  | Single core running 32-bit data access instructions, the other core in idle state | 51.2 | 65.9 |
|  |  | Dual core running 32-bit data access instructions | 66.2 | 81.3 |
|  |  | Single core running 128-bit data access instructions, the other core in idle state | 72.4 | 87.9 |
|  |  | Dual core running 128-bit data access instructions | 91.7 | 107.9 |

${ }^{1}$ Current consumption when all peripheral clocks are disabled.
2 Current consumption when all peripheral clocks are enabled. In practice, the current consumption might be different depending on which peripherals are enabled.
3 In Modem-sleep mode, Wi-Fi is clock gated, and the current consumption might be higher when accessing flash. For a flash rated at $80 \mathrm{Mbit} / \mathrm{s}$, in SPI 2-line mode the consumption is 10 mA .

Table 6-6. Current Consumption in Low-Power Modes

| Work mode | Description | Typ ( $\mu \mathrm{A}$ ) |
| :-- | :-- | :--: |
| Light-sleep ${ }^{1}$ | VDD_SPI and Wi-Fi are powered down, and all GPIOs <br> are high-impedance. | 240 |
| Deep-sleep | RTC memory and RTC peripherals are powered up. <br> RTC memory is powered up. RTC peripherals are <br> powered down. | 8 || Power off | EN is set to low level. The chip is shut down. | 1 |
| :-- | :-- | :-- |

${ }^{1}$ In Light-sleep mode, all related SPI pins are pulled up. For chips embedded with PSRAM, please add corresponding PSRAM consumption values, e.g., 140 $\mu \mathrm{A}$ for 8 MB Octal PSRAM ( 3.3 V ), $200 \mu \mathrm{~A}$ for 8 MB Octal PSRAM ( 1.8 V ) and $40 \mu \mathrm{~A}$ for 2 MB Quad PSRAM ( 3.3 V ).

# 6.5 Memory Specifications 

The data below is sourced from the memory vendor datasheet. These values are guaranteed through design and/or characterization but are not fully tested in production. Devices are shipped with the memory erased.

Table 6-7. Flash Specifications

| Parameter | Description | Min | Typ | Max | Unit |
| :-- | :-- | --: | --: | --: | --: |
|  | Power supply voltage (1.8 V) | 1.65 | 1.80 | 2.00 | V |
|  | Power supply voltage (3.3 V) | 2.7 | 3.3 | 3.6 | V |
|  | Maximum clock frequency | 80 | - | - | MHz |
|  | Program/erase cycles | 100,000 | - | - | cycles |
|  | Data retention time | 20 | - | - | years |
|  | Page program time | - | 0.8 | 5 | ms |
|  | Sector erase time (4 KB) | - | 70 | 500 | ms |
|  | Block erase time (32 KB) | - | 0.2 | 2 | s |
|  | Block erase time (64 KB) | - | 0.3 | 3 | s |
|  | Chip erase time (16 Mb) | - | 7 | 20 | s |
|  | Chip erase time (32 Mb) | - | 20 | 60 | s |
|  | Chip erase time (64 Mb) | - | 25 | 100 | s |
|  | Chip erase time (128 Mb) | - | 60 | 200 | s |
|  | Chip erase time (256 Mb) | - | 70 | 300 | s |

Table 6-8. PSRAM Specifications

| Parameter | Description | Min | Typ | Max | Unit |
| :-- | :-- | :--: | :--: | :--: | :--: |
|  | Power supply voltage (1.8 V) | 1.62 | 1.80 | 1.98 | V |
|  | Power supply voltage (3.3 V) | 2.7 | 3.3 | 3.6 | V |
|  | Maximum clock frequency | 80 | - | - | MHz |# 7 RF Characteristics 

This section contains tables with RF characteristics of the Espressif product.
The RF data is measured at the antenna port, where RF cable is connected, including the front-end loss. The external antennas used for the tests on the modules with external antenna connectors have an impedance of $50 \Omega$.
Devices should operate in the center frequency range allocated by regional regulatory authorities. The target center frequency range and the target transmit power are configurable by software. See ESP RF Test Tool and Test Guide for instructions.

Unless otherwise stated, the RF tests are conducted with a $3.3 \mathrm{~V}( \pm 5 \%)$ supply at $25^{\circ} \mathrm{C}$ ambient temperature.

### 7.1 Wi-Fi Radio

Table 7-1. Wi-Fi RF Characteristics

| Name | Description |
| :-- | :-- |
| Center frequency range of operating channel | $2412-2484 \mathrm{MHz}$ |
| Wi-Fi wireless standard | IEEE $802.11 \mathrm{~b} / \mathrm{g} / \mathrm{n}$ |

### 7.1.1 Wi-Fi RF Transmitter (TX) Characteristics

Table 7-2. TX Power with Spectral Mask and EVM Meeting 802.11 Standards

| Rate | Min <br> (dBm) | Typ <br> (dBm) | Max <br> (dBm) |
| :-- | :--: | :--: | :--: |
| 802.11b, 1 Mbps | - | 20.5 | - |
| 802.11b, 11 Mbps | - | 20.5 | - |
| 802.11g, 6 Mbps | - | 20.0 | - |
| 802.11g, 54 Mbps | - | 18.0 | - |
| 802.11n, HT20, MCS 0 | - | 19.0 | - |
| 802.11n, HT20, MCS 7 | - | 17.5 | - |
| 802.11n, HT40, MCS 0 | - | 18.5 | - |
| 802.11n, HT40, MCS 7 | - | 17.0 | - |

Table 7-3. TX EVM Test ${ }^{1}$

| Rate | Min <br> (dB) | Typ <br> (dB) | Limit <br> (dB) |
| :-- | :--: | :--: | :--: |
| 802.11b, 1 Mbps, @20.5 dBm | - | -24.5 | -10 |
| 802.11b, 11 Mbps, @20.5 dBm | - | -24.5 | -10 |
| 802.11g, 6 Mbps, @20 dBm | - | -23.0 | -5 |
| 802.11g, 54 Mbps, @18 dBm | - | -29.5 | -25 |
|  |  |  |  |

Cont'd on next pageTable 7-3 - cont'd from previous page

| Rate | Min <br> $(\mathbf{d B})$ | Typ <br> $(\mathbf{d B})$ | Limit <br> $(\mathbf{d B})$ |
| :-- | :--: | :--: | :--: |
| $802.11 \mathrm{n}, \mathrm{HT} 2 \mathrm{O}, \mathrm{MCS} 0, @ 19 \mathrm{dBm}$ | - | -24.0 | -5 |
| $802.11 \mathrm{n}, \mathrm{HT} 2 \mathrm{O}, \mathrm{MCS} 7, @ 17.5 \mathrm{dBm}$ | - | -30.5 | -27 |
| $802.11 \mathrm{n}, \mathrm{HT} 4 \mathrm{O}, \mathrm{MCS} 0, @ 18.5 \mathrm{dBm}$ | - | -25.0 | -5 |
| $802.11 \mathrm{n}, \mathrm{HT} 4 \mathrm{O}, \mathrm{MCS} 7, @ 17 \mathrm{dBm}$ | - | -30.0 | -27 |

${ }^{1}$ EVM is measured at the corresponding typical TX power provided in Table 7-2 TX Power with Spectral Mask and EVM Meeting 802.11 Standards above.

# 7.1.2 Wi-Fi RF Receiver (RX) Characteristics 

For RX tests, the PER (packet error rate) limit is $8 \%$ for $802.11 b$, and $10 \%$ for $802.11 \mathrm{~g} / \mathrm{n}$.

Table 7-4. RX Sensitivity

| Rate | Min <br> $(\mathbf{d B m})$ | Typ <br> $(\mathbf{d B m})$ | Max <br> $(\mathbf{d B m})$ |
| :-- | :--: | :--: | :--: |
| $802.11 \mathrm{~b}, 1 \mathrm{Mbps}$ | - | -98.2 | - |
| $802.11 \mathrm{~b}, 2 \mathrm{Mbps}$ | - | -95.6 | - |
| $802.11 \mathrm{~b}, 5.5 \mathrm{Mbps}$ | - | -92.8 | - |
| $802.11 \mathrm{~b}, 11 \mathrm{Mbps}$ | - | -88.5 | - |
| $802.11 \mathrm{~g}, 6 \mathrm{Mbps}$ | - | -93.0 | - |
| $802.11 \mathrm{~g}, 9 \mathrm{Mbps}$ | - | -92.0 | - |
| $802.11 \mathrm{~g}, 12 \mathrm{Mbps}$ | - | -90.8 | - |
| $802.11 \mathrm{~g}, 18 \mathrm{Mbps}$ | - | -88.5 | - |
| $802.11 \mathrm{~g}, 24 \mathrm{Mbps}$ | - | -85.5 | - |
| $802.11 \mathrm{~g}, 36 \mathrm{Mbps}$ | - | -82.2 | - |
| $802.11 \mathrm{~g}, 48 \mathrm{Mbps}$ | - | -78.0 | - |
| $802.11 \mathrm{~g}, 54 \mathrm{Mbps}$ | - | -76.2 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 0$ | - | -93.0 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 1$ | - | -90.6 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 2$ | - | -88.4 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 3$ | - | -84.8 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 4$ | - | -81.6 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 5$ | - | -77.4 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 6$ | - | -75.6 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 7$ | - | -74.2 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 0$ | - | -90.0 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 1$ | - | -87.5 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 2$ | - | -85.0 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 3$ | - | -82.0 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 4$ | - | -78.5 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 5$ | - | -74.4 | - |
|  |  | Cont'd on next page |  |Table 7-4 - cont'd from previous page

| Rate | Min <br> $(\mathbf{d B m})$ | Typ <br> $(\mathbf{d B m})$ | Max <br> $(\mathbf{d B m})$ |
| :-- | :--: | :--: | :--: |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 6$ | - | -72.5 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 7$ | - | -71.2 | - |

Table 7-5. Maximum RX Level

| Rate | Min <br> $(\mathbf{d B m})$ | Typ <br> $(\mathbf{d B m})$ | Max <br> $(\mathbf{d B m})$ |
| :-- | :--: | :--: | :--: |
| $802.11 \mathrm{~b}, 1 \mathrm{Mbps}$ | - | 5 | - |
| $802.11 \mathrm{~b}, 11 \mathrm{Mbps}$ | - | 5 | - |
| $802.11 \mathrm{~g}, 6 \mathrm{Mbps}$ | - | 5 | - |
| $802.11 \mathrm{~g}, 54 \mathrm{Mbps}$ | - | 0 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 0$ | - | 5 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 7$ | - | 0 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 0$ | - | 5 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 7$ | - | 0 | - |

Table 7-6. RX Adjacent Channel Rejection

| Rate | Min <br> $(\mathbf{d B})$ | Typ <br> $(\mathbf{d B})$ | Max <br> $(\mathbf{d B})$ |
| :-- | :--: | :--: | :--: |
| $802.11 \mathrm{~b}, 1 \mathrm{Mbps}$ | - | 35 | - |
| $802.11 \mathrm{~b}, 11 \mathrm{Mbps}$ | - | 35 | - |
| $802.11 \mathrm{~g}, 6 \mathrm{Mbps}$ | - | 31 | - |
| $802.11 \mathrm{~g}, 54 \mathrm{Mbps}$ | - | 14 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 0$ | - | 31 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 20, \mathrm{MCS} 7$ | - | 13 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 0$ | - | 19 | - |
| $802.11 \mathrm{n}, \mathrm{HT} 40, \mathrm{MCS} 7$ | - | 8 | - |

# 7.2 Bluetooth LE Radio 

Table 7-7. Bluetooth LE RF Characteristics

| Name | Description |
| :-- | :-- |
| Center frequency range of operating channel | $2402 \sim 2480 \mathrm{MHz}$ |
| RF transmit power range | $-24.0 \sim 20.0 \mathrm{dBm}$ |# 7.2.1 Bluetooth LE RF Transmitter (TX) Characteristics 

Table 7-8. Bluetooth LE - Transmitter Characteristics - 1 Mbps

| Parameter | Description | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Carrier frequency offset and drift | $\operatorname{Max}\left|f_{n}\right|_{n=0,1,2, \ldots k}$ | - | 2.50 | - | kHz |
|  | $\operatorname{Max}\left|f_{0}-f_{n}\right|$ | - | 2.00 | - | kHz |
|  | $\operatorname{Max}\left|f_{n}-f_{n-5}\right|$ | - | 1.40 | - | kHz |
|  | $\left|f_{1}-f_{0}\right|$ | - | 1.00 | - | kHz |
| Modulation characteristics | $\Delta f 1_{\text {avg }}$ | - | 249.00 | - | kHz |
|  | Min $\Delta f 2_{\text {max }}$ (for at least $99.9 \%$ of all $\Delta f 2_{\text {max }}$ ) | - | 198.00 | - | kHz |
|  | $\Delta f 2_{\text {avg }} / \Delta f 1_{\text {avg }}$ | - | 0.86 | - | - |
| In-band spurious emissions | $\pm 2 \mathrm{MHz}$ offset | - | $-37.00$ | - | dBm |
|  | $\pm 3 \mathrm{MHz}$ offset | - | $-42.00$ | - | dBm |
|  | $> \pm 3 \mathrm{MHz}$ offset | - | $-44.00$ | - | dBm |

Table 7-9. Bluetooth LE - Transmitter Characteristics - 2 Mbps

| Parameter | Description | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Carrier frequency offset and drift | $\operatorname{Max}\left|f_{n}\right|_{n=0,1,2, \ldots k}$ | - | 2.50 | - | kHz |
|  | $\operatorname{Max}\left|f_{0}-f_{n}\right|$ | - | 2.00 | - | kHz |
|  | $\operatorname{Max}\left|f_{n}-f_{n-5}\right|$ | - | 1.40 | - | kHz |
|  | $\left|f_{1}-f_{0}\right|$ | - | 1.00 | - | kHz |
| Modulation characteristics | $\Delta f 1_{\text {avg }}$ | - | 499.00 | - | kHz |
|  | Min $\Delta f 2_{\text {max }}$ (for at least $99.9 \%$ of all $\Delta f 2_{\text {max }}$ ) | - | 416.00 | - | kHz |
|  | $\Delta f 2_{\text {avg }} / \Delta f 1_{\text {avg }}$ | - | 0.89 | - | - |
| In-band spurious emissions | $\pm 4 \mathrm{MHz}$ offset | - | $-42.00$ | - | dBm |
|  | $\pm 5 \mathrm{MHz}$ offset | - | $-44.00$ | - | dBm |
|  | $> \pm 5 \mathrm{MHz}$ offset | - | $-47.00$ | - | dBm |

Table 7-10. Bluetooth LE - Transmitter Characteristics - 125 Kbps

| Parameter | Description | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Carrier frequency offset and drift | $\operatorname{Max}\left|f_{n}\right|_{n=0,1,2, \ldots k}$ | - | 0.80 | - | kHz |
|  | $\operatorname{Max}\left|f_{0}-f_{n}\right|$ | - | 1.00 | - | kHz |
|  | $\left|f_{n}-f_{n-3}\right|$ | - | 0.30 | - | kHz |
|  | $\left|f_{0}-f_{3}\right|$ | - | 1.00 | - | kHz |
| Modulation characteristics | $\Delta f 1_{\text {avg }}$ | - | 248.00 | - | kHz |
|  | Min $\Delta f 1_{\text {max }}$ (for at least $99.9 \%$ of all $\Delta f 1_{\text {max }}$ ) | - | 222.00 | - | kHz |
| In-band spurious emissions | $\pm 2 \mathrm{MHz}$ offset | - | $-37.00$ | - | dBm |
|  | $\pm 3 \mathrm{MHz}$ offset | - | $-42.00$ | - | dBm |
|  | $> \pm 3 \mathrm{MHz}$ offset | - | $-44.00$ | - | dBm |Table 7-11. Bluetooth LE - Transmitter Characteristics - 500 Kbps

| Parameter | Description | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Carrier frequency offset and drift | $\left.\operatorname{Max}\left|f_{n}\right|_{n=0,1,2, \ldots k}\right\|$ | - | 0.80 | - | kHz |
|  | $\left.\operatorname{Max}\left|f_{0}-f_{n}\right|\right\|$ | - | 1.00 | - | kHz |
|  | $\left|f_{n}-f_{n-3}\right|$ | - | 0.85 | - | kHz |
|  | $\left|f_{0}-f_{3}\right|$ | - | 0.34 | - | kHz |
| Modulation characteristics | $\Delta f 2_{\text {avg }}$ | - | 213.00 | - | kHz |
|  | Min $\Delta f 2_{\text {max }}$ (for at least $99.9 \%$ of all $\Delta f 2_{\text {max }}$ ) | - | 196.00 | - | kHz |
| In-band spurious emissions | $\pm 2 \mathrm{MHz}$ offset | - | $-37.00$ | - | dBm |
|  | $\pm 3 \mathrm{MHz}$ offset | - | $-42.00$ | - | dBm |
|  | $> \pm 3 \mathrm{MHz}$ offset | - | $-44.00$ | - | dBm |

# 7.2.2 Bluetooth LE RF Receiver (RX) Characteristics 

Table 7-12. Bluetooth LE - Receiver Characteristics - 1 Mbps

| Parameter | Description | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Sensitivity @30.8\% PER | - | - | $-96.5$ | - | dBm |
| Maximum received signal @30.8\% PER | - | - | 8 | - | dBm |
| Co-channel C/I | $F=F 0 \mathrm{MHz}$ | - | 8 | - | dB |
| Adjacent channel selectivity C/I | $F=F 0+1 \mathrm{MHz}$ | - | 4 | - | dB |
|  | $F=F 0-1 \mathrm{MHz}$ | - | 4 | - | dB |
|  | $F=F 0+2 \mathrm{MHz}$ | - | $-23$ | - | dB |
|  | $F=F 0-2 \mathrm{MHz}$ | - | $-23$ | - | dB |
|  | $F=F 0+3 \mathrm{MHz}$ | - | $-34$ | - | dB |
|  | $F=F 0-3 \mathrm{MHz}$ | - | $-34$ | - | dB |
|  | $F>F 0+3 \mathrm{MHz}$ | - | $-36$ | - | dB |
|  | $F>F 0-3 \mathrm{MHz}$ | - | $-37$ | - | dB |
| Image frequency | - | - | $-36$ | - | dB |
| Adjacent channel to image frequency | $F=F_{\text {image }}+1 \mathrm{MHz}$ | - | $-39$ | - | dB |
|  | $F=F_{\text {image }}-1 \mathrm{MHz}$ | - | $-34$ | - | dB |
| Out-of-band blocking performance | $30 \mathrm{MHz} \sim 2000 \mathrm{MHz}$ | - | $-12$ | - | dBm |
|  | $2003 \mathrm{MHz} \sim 2399 \mathrm{MHz}$ | - | $-18$ | - | dBm |
|  | $2484 \mathrm{MHz} \sim 2997 \mathrm{MHz}$ | - | $-16$ | - | dBm |
|  | $3000 \mathrm{MHz} \sim 12.75 \mathrm{GHz}$ | - | $-10$ | - | dBm |
| Intermodulation | - | - | $-29$ | - | dBm |

Table 7-13. Bluetooth LE - Receiver Characteristics - 2 Mbps

| Parameter | Description | Min | Typ | Max | Unit |
| :-- | :-- | :--: | :--: | :--: | :--: |
| Sensitivity @30.8\% PER | - | - | -92 | - | dBm |
| Maximum received signal @30.8\% PER | - | - | 3 | - | dBm |Table 7-13 - cont'd from previous page

| Parameter | Description | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Co-channel C/I | $\mathrm{F}=\mathrm{FO} \mathrm{MHz}$ | - | 8 | - | dB |
| Adjacent channel selectivity C/I | $\mathrm{F}=\mathrm{FO}+2 \mathrm{MHz}$ | - | 4 | - | dB |
|  | $\mathrm{F}=\mathrm{FO}-2 \mathrm{MHz}$ | - | 4 | - | dB |
|  | $\mathrm{F}=\mathrm{FO}+4 \mathrm{MHz}$ | - | $-27$ | - | dB |
|  | $\mathrm{F}=\mathrm{FO}-4 \mathrm{MHz}$ | - | $-27$ | - | dB |
|  | $\mathrm{F}=\mathrm{FO}+6 \mathrm{MHz}$ | - | $-38$ | - | dB |
|  | $\mathrm{F}=\mathrm{FO}-6 \mathrm{MHz}$ | - | $-38$ | - | dB |
|  | $\mathrm{F}>\mathrm{FO}+6 \mathrm{MHz}$ | - | $-41$ | - | dB |
|  | $\mathrm{F}>\mathrm{FO}-6 \mathrm{MHz}$ | - | $-41$ | - | dB |
| Image frequency | - | - | $-27$ | - | dB |
| Adjacent channel to image frequency | $\mathrm{F}=\mathrm{F}_{\text {image }}+2 \mathrm{MHz}$ | - | $-38$ | - | dB |
|  | $\mathrm{F}=\mathrm{F}_{\text {image }}-2 \mathrm{MHz}$ | - | 4 | - | dB |
| Out-of-band blocking performance | $30 \mathrm{MHz} \sim 2000 \mathrm{MHz}$ | - | $-15$ | - | dBm |
|  | $2003 \mathrm{MHz} \sim 2399 \mathrm{MHz}$ | - | $-21$ | - | dBm |
|  | $2484 \mathrm{MHz} \sim 2997 \mathrm{MHz}$ | - | $-21$ | - | dBm |
|  | $3000 \mathrm{MHz} \sim 12.75 \mathrm{GHz}$ | - | $-9$ | - | dBm |
| Intermodulation | - | - | $-29$ | - | dBm |

Table 7-14. Bluetooth LE - Receiver Characteristics - 125 Kbps

| Parameter | Description | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Sensitivity @30.8\% PER | - | - | $-103.5$ | - | dBm |
| Maximum received signal @30.8\% PER | - | - | 8 | - | dBm |
| Co-channel C/I | $\mathrm{F}=\mathrm{FO} \mathrm{MHz}$ | - | 4 | - | dB |
| Adjacent channel selectivity C/I | $\mathrm{F}=\mathrm{FO}+1 \mathrm{MHz}$ | - | 1 | - | dB |
|  | $\mathrm{F}=\mathrm{FO}-1 \mathrm{MHz}$ | - | 2 | - | dB |
|  | $\mathrm{F}=\mathrm{FO}+2 \mathrm{MHz}$ | - | $-26$ | - | dB |
|  | $\mathrm{F}=\mathrm{FO}-2 \mathrm{MHz}$ | - | $-26$ | - | dB |
|  | $\mathrm{F}=\mathrm{FO}+3 \mathrm{MHz}$ | - | $-36$ | - | dB |
|  | $\mathrm{F}=\mathrm{FO}-3 \mathrm{MHz}$ | - | $-39$ | - | dB |
|  | $\mathrm{F}>\mathrm{FO}+3 \mathrm{MHz}$ | - | $-42$ | - | dB |
|  | $\mathrm{F}>\mathrm{FO}-3 \mathrm{MHz}$ | - | $-43$ | - | dB |
| Image frequency | - | - | $-42$ | - | dB |
| Adjacent channel to image frequency | $\mathrm{F}=\mathrm{F}_{\text {image }}+1 \mathrm{MHz}$ | - | $-43$ | - | dB |
|  | $\mathrm{F}=\mathrm{F}_{\text {image }}-1 \mathrm{MHz}$ | - | $-36$ | - | dB |

Table 7-15. Bluetooth LE - Receiver Characteristics - 500 Kbps

| Parameter | Description | Min | Typ | Max | Unit |
| :-- | :-- | :--: | :--: | :--: | :--: |
| Sensitivity @30.8\% PER | - | - | -100 | - | dBm |
| Maximum received signal @30.8\% PER | - | - | 8 | - | dBm |
| Co-channel C/I | $\mathrm{F}=\mathrm{FO} \mathrm{MHz}$ | - | 4 | - | dB |

Cont'd on next pageTable 7-15 - cont'd from previous page

| Parameter | Description | Min | Typ | Max | Unit |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Adjacent channel selectivity C/I | $\mathrm{F}=\mathrm{FO}+1 \mathrm{MHz}$ | - | 1 | - | dB |
|  | $\mathrm{F}=\mathrm{FO}-1 \mathrm{MHz}$ | - | 0 | - | dB |
|  | $\mathrm{F}=\mathrm{FO}+2 \mathrm{MHz}$ | - | $-24$ | - | dB |
|  | $\mathrm{F}=\mathrm{FO}-2 \mathrm{MHz}$ | - | $-24$ | - | dB |
|  | $\mathrm{F}=\mathrm{FO}+3 \mathrm{MHz}$ | - | $-37$ | - | dB |
|  | $\mathrm{F}=\mathrm{FO}-3 \mathrm{MHz}$ | - | $-39$ | - | dB |
|  | $\mathrm{F}>\mathrm{FO}+3 \mathrm{MHz}$ | - | $-38$ | - | dB |
|  | $\mathrm{F}>\mathrm{FO}-3 \mathrm{MHz}$ | - | $-42$ | - | dB |
| Image frequency | - | - | $-38$ | - | dB |
| Adjacent channel to image frequency | $\mathrm{F}=\mathrm{F}_{\text {image }}+1 \mathrm{MHz}$ | - | $-42$ | - | dB |
|  | $\mathrm{F}=\mathrm{F}_{\text {image }}-1 \mathrm{MHz}$ | - | $-37$ | - | dB |# 8 Module Schematics 

This is the reference design of the module. For modules with PSRAM, the VDD_SPI voltage is fixed to 3.3 V or 1.8 V via eFuse, so their VDD_SPI voltage will not be affected by the GPIO45 level. However, for other modules, please ensure that GPIO45 is not pulled high when the module is powered up by the external circuit.
![img-9.jpeg](img-9.jpeg)

Figure 8-1. ESP32-S3-WROOM-1 Schematics![img-10.jpeg](img-10.jpeg)

Figure 8-2. ESP32-S3-WROOM-1U Schematics# 9 Peripheral Schematics 

This is the typical application circuit of the module connected with peripheral components (for example, power supply, antenna, reset button, JTAG interface, and UART interface).
![img-11.jpeg](img-11.jpeg)

Figure 9-1. Peripheral Schematics

- Soldering the EPAD to the ground of the base board is not a must, however, it can optimize thermal performance. If you choose to solder it, please apply the correct amount of soldering paste. Too much soldering paste may increase the gap between the module and the baseboard. As a result, the adhesion between other pins and the baseboard may be poor.
- To ensure that the power supply to the ESP32-S3 chip is stable during power-up, it is advised to add an RC delay circuit at the EN pin. The recommended setting for the RC delay circuit is usually $R=10 \mathrm{k} \Omega$ and $\mathrm{C}=1 \mu \mathrm{~F}$. However, specific parameters should be adjusted based on the power-up timing of the module and the power-up and reset sequence timing of the chip. For ESP32-S3's power-up and reset sequence timing diagram, please refer Section 4.5 Chip Power-up and Reset.# 10 Physical Dimensions 

### 10.1 Module Dimensions

![img-12.jpeg](img-12.jpeg)

Figure 10-1. ESP32-S3-WROOM-1 Physical Dimensions
![img-13.jpeg](img-13.jpeg)

Figure 10-2. ESP32-S3-WROOM-1U Physical Dimensions

## Note:

For information about tape, reel, and product marking, please refer to ESP32-S3 Module Packaging Information.# 10.2 Dimensions of External Antenna Connector 

ESP32-S3-WROOM-1U uses the first generation external antenna connector as shown in Figure 10-3 Dimensions of External Antenna Connector. This connector is compatible with the following connectors:

- U.FL Series connector from Hirose
- MHF I connector from I-PEX
- AMC connector from Amphenol
![img-14.jpeg](img-14.jpeg)

Figure 10-3. Dimensions of External Antenna ConnectorThe external antenna used for ESP32-S3-WROOM-1U during certification testing is the first generation monopole antenna, with material code TFPDO5HO8750011.

The module does not include an external antenna upon shipment. If needed, select a suitable external antenna based on the product's usage environment and performance requirements.

It is recommended to select an antenna that meets the following requirements:

- 2.4 GHz band
- $50 \Omega$ impedance
- The maximum gain does not exceed 2.33 dBi , the gain of the antenna used for certification
- The connector matches the specifications shown in Figure 10-3 Dimensions of External Antenna Connector


# Note: 

If you use an external antenna of a different type or gain, additional testing, such as EMC, may be required beyond the existing antenna test reports for Espressif modules. Specific requirements depend on the certification type.# 11 PCB Layout Recommendations 

### 11.1 PCB Land Pattern

This section provides the following resources for your reference:

- Figures for recommended PCB land patterns with all the dimensions needed for PCB design. See Figure 11-1 ESP32-S3-WROOM-1 Recommended PCB Land Pattern and Figure 11-2 ESP32-S3-WROOM-1U Recommended PCB Land Pattern.
- Source files of recommended PCB land patterns to measure dimensions not covered in Figure 11-1 and Figure 11-2. You can view the source files for ESP32-S3-WROOM-1 and ESP32-S3-WROOM-1U with Autodesk Viewer.
- 3D models of ESP32-S3-WROOM-1 and ESP32-S3-WROOM-1U. Please make sure that you download the 3D model file in .STEP format (beware that some browsers might add .txt).
![img-15.jpeg](img-15.jpeg)

Figure 11-1. ESP32-S3-WROOM-1 Recommended PCB Land Pattern![img-16.jpeg](img-16.jpeg)

Figure 11-2. ESP32-S3-WROOM-1U Recommended PCB Land Pattern

# 11.2 Module Placement for PCB Design 

If module-on-board design is adopted, attention should be paid while positioning the module on the base board. The interference of the base board on the module's antenna performance should be minimized.

For details about module placement for PCB design, please refer to ESP32-S3 Hardware Design Guidelines > Section General Principles of PCB Layout for Modules.# 12 Product Handling 

### 12.1 Storage Conditions

The products sealed in moisture barrier bags (MBB) should be stored in a non-condensing atmospheric environment of $<40^{\circ} \mathrm{C}$ and $90 \% \mathrm{RH}$. The module is rated at the moisture sensitivity level (MSL) of 3.

After unpacking, the module must be soldered within 168 hours with the factory conditions $25 \pm 5^{\circ} \mathrm{C}$ and $60 \% \mathrm{RH}$. If the above conditions are not met, the module needs to be baked.

### 12.2 Electrostatic Discharge (ESD)

- Human body model (HBM): $\pm 2000 \mathrm{~V}$
- Charged-device model (CDM): $\pm 500 \mathrm{~V}$


### 12.3 Reflow Profile

Solder the module in a single reflow.
![img-17.jpeg](img-17.jpeg)

Figure 12-1. Reflow Profile# 12.4 Ultrasonic Vibration 

Avoid exposing Espressif modules to vibration from ultrasonic equipment, such as ultrasonic welders or ultrasonic cleaners. This vibration may induce resonance in the in-module crystal and lead to its malfunction or even failure. As a consequence, the module may stop working or its performance may deteriorate.# Datasheet Versioning 

| Datasheet Version | Status | Watermark | Definition |
| :--: | :--: | :--: | :--: |
| v0.1 v0.5 (excluding v0.5) | Draft | Confidential | This datasheet is under development for products in the design stage. Specifications may change without prior notice. |
| v0.5 v1.0 (excluding v1.0) | Preliminary release | Preliminary | This datasheet is actively updated for products in the verification stage. Specifications may change before mass production, and the changes will be documentation in the datasheet's Revision History. |
| v1.0 and higher | Official release | $-$ | This datasheet is publicly released for products in mass production. Specifications are finalized, and major changes will be communicated via Product Change Notifications (PCN). |
| Any version | - | Not <br> Recommended for New Design (NRND) ${ }^{1}$ | This datasheet is updated less frequently for products not recommended for new designs. |
| Any version | - | End of Life <br> (EOL) ${ }^{2}$ | This datasheet is no longer mtained for products that have reached end of life. |

${ }^{1}$ Watermark will be added to the datasheet title page only when all the product variants covered by this datasheet are not recommended for new designs.
2 Watermark will be added to the datasheet title page only when all the product variants covered by this datasheet have reached end of life.# Related Documentation and Resources 

## Related Documentation

- ESP32-S3 Series Datasheet - Specifications of the ESP32-S3 hardware.
- ESP32-S3 Technical Reference Manual - Detailed information on how to use the ESP32-S3 memory and peripherals.
- ESP32-S3 Hardware Design Guidelines - Guidelines on how to integrate the ESP32-S3 into your hardware product.
- ESP32-S3 Series SoC Errata - Descriptions of known errors in ESP32-S3 series of SoCs.
- Certificates
https://espressif.com/en/support/documents/certificates
- ESP32-S3 Product/Process Change Notifications (PCN)
https://espressif.com/en/support/documents/pcns?keys=ESP32-S3
- ESP32-S3 Advisories - Information on security, bugs, compatibility, component reliability.
https://espressif.com/en/support/documents/advisories?keys=ESP32-S3
- Documentation Updates and Update Notification Subscription
https://espressif.com/en/support/download/documents


## Developer Zone

- ESP-IDF Programming Guide for ESP32-S3 - Extensive documentation for the ESP-IDF development framework.
- ESP-IDF and other development frameworks on GitHub.
https://github.com/espressif
- ESP32 BBS Forum - Engineer-to-Engineer (E2E) Community for Espressif products where you can post questions, share knowledge, explore ideas, and help solve problems with fellow engineers.
https://esp32.com/
- ESP-FAQ - A summary document of frequently asked questions released by Espressif.
https://espressif.com/projects/esp-faq/en/latest/index.html
- The ESP Journal - Best Practices, Articles, and Notes from Espressif folks.
https://blog.espressif.com/
- See the tabs SDKs and Demos, Apps, Tools, AT Firmware.
https://espressif.com/en/support/download/sdks-demos


## Products

- ESP32-S3 Series SoCs - Browse through all ESP32-S3 SoCs.
https://espressif.com/en/products/socs?id=ESP32-S3
- ESP32-S3 Series Modules - Browse through all ESP32-S3-based modules.
https://espressif.com/en/products/modules?id=ESP32-S3
- ESP32-S3 Series DevKits - Browse through all ESP32-S3-based devkits.
https://espressif.com/en/products/devkits?id=ESP32-S3
- ESP Product Selector - Find an Espressif hardware product suitable for your needs by comparing or applying filters. https://products.espressif.com/\#/product-selector?language=en


## Contact Us

- See the tabs Sales Questions, Technical Enquiries, Circuit Schematic \& PCB Design Review, Get Samples (Online stores), Become Our Supplier, Comments \& Suggestions.
https://espressif.com/en/contact-us/sales-questions# Revision History 

| Date | Version | Release notes |
| :--: | :--: | :--: |
| 2025-07-25 | v1.6 | - Added Section 4.5 Chip Power-up and Reset <br> - Added Section 6.5 Memory Specifications <br> - Added the external antenna information for certification in Section 10.2 Dimensions of External Antenna Connector <br> - Added Section Datasheet Versioning <br> - Other minor changes |
| 2025-06-10 | v1.5 | - Added a note about the pin mapping between the chip and the inpackage flash/PSRAN in Section 2 Block Diagram |
| 2024-11-14 | v1.4 | - Renamed module variants ESP32-S3-WROOM-1-N16R16V and ESP32-S3-WROOM-1U-N16R16V to ESP32-S3-WROOM-1-N16R16VA and ESP32-S3-WROOM-1U-N16R16VA <br> - Added a reference to the chip revision information in the note in Section Section 1.2 Series Comparison <br> - Updated Section 1.3 Applications <br> - Restructured the previous Section Strapping Pins as Section 4 Boot Configurations <br> - Added Section 5.2 Peripheral Description <br> - Divided Section Electrical Characteristics into Section 6 Electrical Characteristics and Section 7 RF Characteristics with updated formatting and wording <br> - Divided Section Physical Dimensions and PCB Land Pattern into Section 10 Physical Dimensions and 11 PCB Layout Recommendations and added Section 11.2 Module Placement for PCB Design <br> - Added the 3D model link of ESP32-S3-WROOM-1U in Section 11.1 PCB Land Pattern <br> - Updated Figure 12-1 Reflow Profile <br> - Other minor updates to formatting and wording |
| 2023-11-24 | v1.3 | - Added the new module variants ESP32-S3-WROOM-1-N16R16VA and ESP32-S3-WROOM-1U-N16R16VA, and updated the related information <br> - Updated table notes to Table 1-2 ESP32-S3-WROOM-1U Series Comparison <br> - Updated Section 4.1 Chip Boot Mode Control <br> - Updated the module schematics in Section 8 Module Schematics <br> - Updated the physical dimensions figure in Section 10.1 Module Dimensions <br> - Other minor updates |Cont'd from previous page

| Date | Version | Release notes |
| :--: | :--: | :--: |
| 2023-03-07 | v1.2 | - Update Section Strapping Pins <br> - Update Section 6.4 Current Consumption Characteristics <br> - Update the minimum value of RF transmit power in Section 7.2.1 Bluetooth LE RF Transmitter (TX) Characteristics <br> - Update descriptions in Section 9 Peripheral Schematics <br> - Add descriptions in Section 11.1 PCB Land Pattern <br> - Update Section 12.4 <br> - Other minor changes |
| 2022-07-22 | v1.1 | - Update Table 1-1 and Table 1-2 <br> - Other minor updates |
| 2022-04-21 | v1.0 | - Update Bluetooth LE RF data <br> - Update power consumption data in Table 6-6 <br> - Add certification and test information <br> - Update Section Strapping Pins |
| 2021-10-29 | v0.6 | Overall update for chip evision 1 |
| 2021-07-19 | v0.5.1 | Preliminary release, for chip revision 0 |# ESPRESSIF 

## Disclaimer and Copyright Notice

Information in this document, including URL references, is subject to change without notice.
ALL THIRD PARTY'S INFORMATION IN THIS DOCUMENT IS PROVIDED AS IS WITH NO WARRANTIES TO ITS AUTHENTICITY AND ACCURACY.

NO WARRANTY IS PROVIDED TO THIS DOCUMENT FOR ITS MERCHANTABILITY, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, NOR DOES ANY WARRANTY OTHERWISE ARISING OUT OF ANY PROPOSAL, SPECIFICATION OR SAMPLE.
All liability, including liability for infringement of any proprietary rights, relating to use of information in this document is disclaimed. No licenses express or implied, by estoppel or otherwise, to any intellectual property rights are granted herein.
The Wi-Fi Alliance Member logo is a trademark of the Wi-Fi Alliance. The Bluetooth logo is a registered trademark of Bluetooth SIG.
All trade names, trademarks and registered trademarks mentioned in this document are property of their respective owners, and are hereby acknowledged.
Copyright © 2025 Espressif Systems (Shanghai) Co., Ltd. All rights reserved.
www.espressif.com