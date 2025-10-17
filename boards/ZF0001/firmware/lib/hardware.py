"""
Hardware abstraction layer for LEDs and buttons
"""
from machine import Pin
import time

class LED:
    """RGB LED control"""
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red = Pin(red_pin, Pin.OUT)
        self.green = Pin(green_pin, Pin.OUT)
        self.blue = Pin(blue_pin, Pin.OUT)
        self.off()
    
    def set(self, r, g, b):
        """Set RGB state (True/False for each color)"""
        self.red.value(1 if r else 0)
        self.green.value(1 if g else 0)
        self.blue.value(1 if b else 0)
    
    def off(self):
        """Turn off all LEDs"""
        self.set(False, False, False)
    
    def red_on(self):
        """Red = recording"""
        self.set(True, False, False)
    
    def green_on(self):
        """Green = ready/idle"""
        self.set(False, True, False)
    
    def blue_on(self):
        """Blue = connecting"""
        self.set(False, False, True)
    
    def blink(self, color, duration_ms=100):
        """Quick blink"""
        if color == 'red':
            self.set(True, False, False)
        elif color == 'green':
            self.set(False, True, False)
        elif color == 'blue':
            self.set(False, False, True)
        time.sleep_ms(duration_ms)
        self.off()


class Button:
    """Button with debouncing"""
    def __init__(self, pin, pull=Pin.PULL_UP):
        self.pin = Pin(pin, Pin.IN, pull)
        self.last_state = self.pin.value()
        self.last_change = time.ticks_ms()
        self.debounce_ms = 50
    
    def is_pressed(self):
        """Check if button is currently pressed (active low)"""
        return self.pin.value() == 0
    
    def was_pressed(self):
        """Check for button press event (with debouncing)"""
        current_state = self.pin.value()
        now = time.ticks_ms()
        
        # Detect press (high to low transition)
        if current_state == 0 and self.last_state == 1:
            if time.ticks_diff(now, self.last_change) > self.debounce_ms:
                self.last_state = current_state
                self.last_change = now
                return True
        
        self.last_state = current_state
        return False


class StatusPins:
    """Read-only status pins"""
    def __init__(self, chg_pin, pg_pin, alert_pin):
        self.chg = Pin(chg_pin, Pin.IN)
        self.pg = Pin(pg_pin, Pin.IN)
        self.alert = Pin(alert_pin, Pin.IN, Pin.PULL_UP)
    
    def is_charging(self):
        """Check if battery is charging (active low)"""
        return self.chg.value() == 0
    
    def is_power_good(self):
        """Check if power is good (active low)"""
        return self.pg.value() == 0
    
    def is_battery_alert(self):
        """Check fuel gauge alert (active low)"""
        return self.alert.value() == 0

