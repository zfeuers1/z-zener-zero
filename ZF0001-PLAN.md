# ZF0001 Wearable Voice Logger Board - Implementation Plan

## Overview
Create a wearable voice logger PCB featuring ESP32-S3 Wi-Fi streaming, analog microphone via 3.5mm TRRS audio jack, GPS tagging, battery power management, USB-C connectivity, and RGB LED status indicators.

## Component Strategy

### From Registry (existing):
- **USB-C Module**: Use `@registry/modules/usb/UsbC.zen` (USB2_SINK mode with 5.1k CC resistors)
- **Push Button**: Use `@registry/modules/basic/PushButton.zen`
- **LDO Regulator**: Use `@registry/common/regulator-ldo.zen` (TPS7A8101 or compatible)
- **Buck Regulator**: Use `@registry/common/regulator-switching.zen` or similar
- **Generic LED**: Use `@stdlib/generics/Led.zen` for status indicators
- **JST-GH Connectors**: Available in registry for various connections

### Components Added (via pcb-pro search):
- ✅ **ESP32-S3-WROOM-1-N8R8** - ESP32-S3 module with 8MB flash, 8MB PSRAM, Wi-Fi
- ✅ **BQ24075** - Li-ion battery charger IC with power-path management
- ✅ **MAX17048** - Fuel gauge IC (I2C battery state-of-charge monitoring)
- ✅ **MAX-M10S** - u-blox GNSS module for GPS coordinate tagging
- ✅ **CSS-1210TB** - Slide switch for hard power on/off
- ✅ **MSD-12-A** - MicroSD card socket (SPI interface)
- ✅ **S2B-PH-K-S** - JST-PH 2-pin battery connector
- 🔄 **TRRS Audio Jack** - 3.5mm audio jack for analog microphone input (search: SJ-3524-SMT-TR, PJ-320A, or MJ-3536)

### Additional Components Needed:
- **Buck/Boost Converter IC** - For 3.3V main rail (check registry for TPS6xxxx series)
- **Op-Amp** - For microphone bias and amplification circuit (e.g., OPA344)
- **u.FL Antenna Connector** - For GNSS external antenna

## Implementation Steps

### 1. Board Structure Setup ✅
- ✅ Renamed `boards/CS0001/` to `boards/ZF0001/`
- ✅ Renamed `boards/ZF0001/CS0001.zen` to `boards/ZF0001/ZF0001.zen`
- ✅ Updated `boards/ZF0001/pcb.toml` with new board name and description
- ✅ Renamed `boards/ZF0001/layout/CS0001/` to `boards/ZF0001/layout/ZF0001/`
- ✅ Created `boards/ZF0001/src/` directory for split-out modules

### 2. Component Acquisition 🔄
- ✅ ESP32-S3-WROOM-1-N8R8 added to components
- ✅ BQ24075 battery charger added
- ✅ MAX17048 fuel gauge added
- ✅ MAX-M10S GNSS module added
- ✅ CSS-1210TB slide switch added
- ✅ MSD-12-A microSD socket added
- ✅ S2B-PH-K-S JST-PH battery connector added
- 🔄 TRRS audio jack (pending search)
- ⏳ Additional power management components (as needed)

### 3. Create Custom Modules
Create in `z-zener-zero/modules/`:
- **Esp32S3.zen**: ESP32-S3 reference wrapper with decoupling, boot/reset circuitry
- **BatteryPower.zen**: BQ24075 charger + MAX17048 fuel gauge + power switching
- **GnssModule.zen**: MAX-M10S wrapper with antenna connection and backup supply
- **MicrophoneInput.zen**: Analog microphone input with bias, amplification, and ADC interface

### 4. Main Board Design (ZF0001.zen)

#### Power Architecture:
- **VBUS_5V** from USB-C (for charging and programming)
- **VBAT** 3.7V rechargeable Li-ion battery (1000-2000mAh) via JST-PH connector
- **BQ24075** power-path charger
  - Enables system to run from USB while charging battery
  - OR run from battery alone when USB disconnected
  - Charge status outputs for LED indicators
- **Buck Converter** 3.3V @ 1A from charger output (PMID pin) for main VDD_3V3 rail
- **Separate LDO** for GNSS (low noise 3.3V_GNSS rail)
- **Hard power switch** (CSS-1210TB slide switch) to completely disconnect battery
- **MAX17048** fuel gauge on battery line for SoC monitoring via I2C

#### Microcontroller Section:
- ESP32-S3 module with proper decoupling capacitors
- Boot button (GPIO0 pull-down with PushButton module)
- Reset button (EN pin with PushButton module)
- USB data lines connected to ESP32 native USB (GPIO19/20)
- Analog microphone input to ESP32 ADC (GPIO1-GPIO10, use ADC1 for WiFi compatibility)
- SPI to microSD card (MISO, MOSI, SCK, CS)
- UART to GNSS module (TX, RX)
- I2C for MAX17048 fuel gauge (SCL, SDA)
- GPIO for RGB status LEDs (multiple pins or WS2812B data pin)
- GPIO for record button input

#### Interface Assignments:
- **ADC1_CH0-CH3** (GPIO1-4): Analog microphone input
- **SPI2**: MicroSD card (GPIO12=MISO, GPIO13=MOSI, GPIO14=SCK, GPIO15=CS)
- **UART1**: GNSS module (GPIO16=RX, GPIO17=TX)
- **I2C0**: Fuel gauge (GPIO21=SDA, GPIO22=SCL)
- **GPIO**: 
  - GPIO0: Boot button
  - GPIO5: Record button
  - GPIO6-8: Status LEDs (or single WS2812B data pin)
  - GPIO9: Charge status input from BQ24075
  - GPIO10: Power good sense

#### Microphone Input Circuit:
- TRRS 3.5mm audio jack
  - Tip: Microphone signal
  - Ring 1: Not connected (or second mic channel)
  - Ring 2: Ground
  - Sleeve: Microphone bias voltage
- Microphone bias circuit (2.5V)
  - Voltage divider from 3.3V
  - Decoupling capacitor
- Op-amp amplifier stage
  - Gain: 10-20x (adjustable via resistor ratio)
  - AC-coupled input (DC blocking capacitor)
  - Output to ESP32 ADC input
- Low-pass filter before ADC (anti-aliasing)

#### Peripheral Connections:
- GNSS module with u.FL antenna connector for external GPS antenna
- MicroSD socket on SPI2 bus with card detect pin
- TRRS audio jack for analog microphone
- Status LEDs (charge, power, recording, GPS fix)
- USB-C connector (charging, data, programming)

#### Power Indicators & Status:
- CHG LED (red): Charging status from BQ24075
- PWR LED (green): Power good indicator
- REC LED (blue): Recording status
- GPS LED (yellow/orange): GPS fix status
- Or single RGB LED (WS2812B) for all status indication

### 5. Board Configuration ✅
`boards/ZF0001/pcb.toml`:
- Board name: ZF0001
- Description: Wearable voice logger with WiFi streaming, GPS tagging, and battery operation
- 4-layer PCB recommended

### 6. Layout Guidelines (in docs)
Document PCB layout considerations:
- **ESP32 antenna area**: Keep clear of copper pour (5mm keepout zone)
- **GNSS power island**: Separate 3.3V_GNSS rail with LC filtering
- **Place microphone jack**: Away from switching regulators and digital noise sources
- **USB ESD protection**: Close to connector
- **Battery connector**: Near slide switch and charger IC
- **Decoupling capacitors**: Close to IC power pins
- **Compact form factor**: Target ~40mm x 50mm for wearable size
- **Ground plane**: Solid ground pour on layer 2
- **Power plane**: 3.3V pour on layer 3

### 7. Pin Mapping Documentation
Detailed GPIO assignments:

**ESP32-S3 Pin Map:**
```
GPIO0:  Boot button (pulled high, button to GND)
GPIO1:  Microphone analog input (ADC1_CH0)
GPIO5:  Record button
GPIO6:  Status LED 1 (or WS2812B data)
GPIO7:  Status LED 2
GPIO8:  Status LED 3
GPIO9:  Charge status sense (from BQ24075 CHG pin)
GPIO10: Power good sense
GPIO12: SPI2 MISO (microSD)
GPIO13: SPI2 MOSI (microSD)
GPIO14: SPI2 SCK (microSD)
GPIO15: SPI2 CS (microSD)
GPIO16: UART1 RX (GNSS)
GPIO17: UART1 TX (GNSS)
GPIO19: USB D- (native USB)
GPIO20: USB D+ (native USB)
GPIO21: I2C SDA (fuel gauge)
GPIO22: I2C SCL (fuel gauge)
EN:     Reset button (pulled high, button to GND)
```

## Key Files to Create/Modify

### Created:
- ✅ `/Users/zach/Documents/diodeinc/z-zener-zero/boards/ZF0001/ZF0001.zen`
- ✅ `/Users/zach/Documents/diodeinc/z-zener-zero/boards/ZF0001/pcb.toml`
- ⏳ `/Users/zach/Documents/diodeinc/z-zener-zero/boards/ZF0001/docs/ZF0001.md`
- ✅ `/Users/zach/Documents/diodeinc/z-zener-zero/boards/ZF0001/src/` (directory)
- ⏳ `/Users/zach/Documents/diodeinc/z-zener-zero/modules/Esp32S3.zen`
- ⏳ `/Users/zach/Documents/diodeinc/z-zener-zero/modules/BatteryPower.zen`
- ⏳ `/Users/zach/Documents/diodeinc/z-zener-zero/modules/GnssModule.zen`
- ⏳ `/Users/zach/Documents/diodeinc/z-zener-zero/modules/MicrophoneInput.zen`

### Leverage from Registry:
- `@registry/modules/usb/UsbC.zen`
- `@registry/modules/basic/PushButton.zen`
- `@registry/common/regulator-ldo.zen`
- `@registry/common/regulator-switching.zen`
- `@stdlib/generics/Led.zen`
- `@stdlib/generics/Resistor.zen`
- `@stdlib/generics/Capacitor.zen`

## Expected Outcome
A complete, production-ready wearable voice logger board design with:
- ✅ WiFi streaming capability via ESP32-S3
- 🔄 Analog audio capture via 3.5mm TRRS jack (16kHz sampling via ESP32 ADC)
- ✅ GPS coordinate tagging via MAX-M10S
- ✅ 3-5 hour battery runtime with 1000-2000mAh Li-ion battery
- ✅ USB-C charging and programming with power-path management
- ⏳ Visual status feedback via multiple LEDs or RGB LED
- ⏳ Single-button recording control
- ✅ Optional SD card backup via microSD socket

## Status Legend
- ✅ Complete
- 🔄 In Progress
- ⏳ Pending
- ❌ Blocked/Issue

## Next Steps
1. Search for and add TRRS audio jack component
2. Search for op-amp component (OPA344 or similar)
3. Search for buck converter IC (if not in registry)
4. Create ESP32-S3 module wrapper
5. Create BatteryPower module (BQ24075 + MAX17048)
6. Create MicrophoneInput module (TRRS + op-amp + bias circuit)
7. Create GnssModule wrapper
8. Implement main ZF0001.zen board file
9. Create comprehensive documentation
10. Review and test design

