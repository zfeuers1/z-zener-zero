# TPS62933x Reference Design

Synchronous buck converter module for 3.8V-30V input to regulated output.

## Usage

```python
TPS62933 = Module("../../modules/TPS62933x.zen")

TPS62933(
    name = "U_BUCK",
    vin = VSYS,           # 3.8V-30V input
    vout = VDD_3V3,       # Regulated output
    gnd = GND,
    en = Gpio("EN"),      # Optional enable control
    config_vout = 3.3,    # Output voltage (default 3.3V)
    config_frequency = "500kHz",  # "500kHz" or "1200kHz"
)
```

## Features

- **Input:** 3.8V-30V
- **Output:** 0.8V-22V (configurable)
- **Current:** Up to 3A continuous
- **Efficiency:** Up to 98%
- **Quiescent:** 12µA typical (PFM mode)
- **Frequency:** 200kHz-2.2MHz (configurable)

## Configuration

### Output Voltage
Set `config_vout` to desired voltage (float). Common values:
- `3.3` → 3.3V (default)
- `5.0` → 5.0V
- `12.0` → 12.0V

Feedback resistors calculated automatically using 0.8V reference.

### Switching Frequency
Set `config_frequency`:
- `"500kHz"` → 500kHz (default, RT floating)
- `"1200kHz"` → 1.2MHz (RT tied to GND)

Lower frequency = higher efficiency, larger components
Higher frequency = smaller solution size, slightly lower efficiency

### Enable Control
- If `en` provided: external enable control
- If `en` omitted: internal pull-up enables device (always on)

## Design Notes

Based on TPS62933 datasheet typical application (Figure 10-1).

**Integrated components:**
- Input capacitor: 10µF/50V
- Output capacitors: 2×22µF/10V
- Output inductor: 6.8µH (Isat > 5.8A)
- Bootstrap capacitor: 100nF with 4.7Ω series resistor
- Feedback resistor divider: 1% tolerance
- Soft-start capacitor: 33nF (~5ms)

**Protection features:**
- Cycle-by-cycle overcurrent limiting
- Output overvoltage protection (115%)
- Output undervoltage protection (65%)
- Thermal shutdown (165°C)

**Operating modes:**
- CCM: Continuous conduction at heavy loads
- PFM: Pulse frequency modulation for light-load efficiency
- Automatic frequency reduction for dropout/min-on-time

## Typical Performance

For 3.3V output at 500kHz:
- **Load regulation:** < 0.5%
- **Line regulation:** < 0.1%
- **Ripple:** < 30mV p-p
- **Efficiency:** 
  - 95% @ 1A (12V input)
  - 93% @ 3A (24V input)
  - 85% @ 10mA (light load, PFM)

## Component Selection

### Inductor
Chosen: 6.8µH, Isat > 5.8A, DCR < 50mΩ
- Example: Würth 74439346068

Calculate for different applications:
```
L (µH) = (VIN - VOUT) / (fsw × K × IOUT) × VOUT / VIN
```
Where K = 0.4 (40% ripple ratio recommended)

### Output Capacitors
Minimum: 22µF ceramic (X5R or better)
Recommended: 2×22µF for low ESR and better ripple

### Input Capacitor
Minimum: 10µF ceramic placed close to VIN pin

## Layout Guidelines

1. **Input capacitor** as close as possible to VIN/GND pins
2. **SW node** minimize trace length and area (hot loop)
3. **Inductor** place near SW pin, route away from sensitive signals
4. **Output capacitors** near inductor output and load
5. **Bootstrap capacitor** close to BST/SW pins
6. **Feedback divider** near FB pin, short traces
7. **Ground plane** solid connection for thermal and electrical performance

## Power Budget

For 3.3V @ 1A output from 12V input:
- **Input power:** ~3.8W
- **Output power:** 3.3W
- **Efficiency:** ~87%
- **Power loss:** ~0.5W (handle with thermal vias and ground plane)

