"""
Battery monitoring module
MAX17048 fuel gauge via I2C
"""
from machine import I2C
import time

class Battery:
    """MAX17048 Fuel Gauge"""
    ADDR = 0x36
    REG_VCELL = 0x02
    REG_SOC = 0x04
    REG_MODE = 0x06
    REG_VERSION = 0x08
    REG_CONFIG = 0x0C
    
    def __init__(self, sda_pin, scl_pin, freq=100000):
        # Initialize I2C on VDD_3V3 domain
        # Note: I2C pull-ups are to VDD_3V3 (3.3V) to stay within ESP32 GPIO spec
        # ESP32-S3 max input voltage: VDD+0.3V = 3.6V (VBAT 4.2V would exceed this)
        self.i2c = I2C(0, sda=sda_pin, scl=scl_pin, freq=freq)
        time.sleep_ms(100)
        
        # Check if device is present
        devices = self.i2c.scan()
        if self.ADDR in devices:
            version = self._read_reg(self.REG_VERSION)
            print(f"[BATTERY] MAX17048 detected, version: 0x{version:04X}")
            self.initialized = True
            
            # Configure alert threshold
            self._configure_alert(20)  # 20% threshold
        else:
            print("[BATTERY] ERROR: MAX17048 not found!")
            self.initialized = False
    
    def _read_reg(self, reg):
        """Read 16-bit register"""
        try:
            data = self.i2c.readfrom_mem(self.ADDR, reg, 2)
            return (data[0] << 8) | data[1]
        except:
            return 0
    
    def _write_reg(self, reg, value):
        """Write 16-bit register"""
        try:
            data = bytes([(value >> 8) & 0xFF, value & 0xFF])
            self.i2c.writeto_mem(self.ADDR, reg, data)
            return True
        except:
            return False
    
    def _configure_alert(self, threshold_percent):
        """Configure alert threshold"""
        config = self._read_reg(self.REG_CONFIG)
        # Set ATHD bits (bits 4-0) to threshold
        config = (config & 0xFFE0) | (32 - threshold_percent)
        self._write_reg(self.REG_CONFIG, config)
    
    def get_voltage(self):
        """Get battery voltage in volts"""
        if not self.initialized:
            return 0.0
        
        vcell = self._read_reg(self.REG_VCELL)
        # VCELL register: 12-bit value, LSB = 78.125 µV
        voltage = (vcell >> 4) * 0.00125
        return voltage
    
    def get_soc(self):
        """Get state of charge as percentage"""
        if not self.initialized:
            return 0.0
        
        soc = self._read_reg(self.REG_SOC)
        # SOC register: upper byte = integer %, lower byte = fractional %
        percent = (soc >> 8) + ((soc & 0xFF) / 256.0)
        return percent
    
    def get_data(self, status_pins):
        """Get complete battery data"""
        voltage = self.get_voltage()
        soc = self.get_soc()
        
        return {
            'voltage': voltage,
            'soc': soc,
            'is_charging': status_pins.is_charging(),
            'is_low': soc < 20,
            'is_critical': soc < 10,
        }
    
    def print_data(self, status_pins):
        """Print battery data"""
        data = self.get_data(status_pins)
        status = " [CHARGING]" if data['is_charging'] else ""
        status += " [LOW]" if data['is_low'] else ""
        status += " [CRITICAL]" if data['is_critical'] else ""
        print(f"[BATTERY] {data['voltage']:.2f}V, {data['soc']:.1f}%{status}")

