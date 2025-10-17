"""
GPS/GNSS module
Parses NMEA sentences from MAX-M10S
"""
from machine import UART
import time

class GPS:
    """Simple NMEA parser for GPS data"""
    def __init__(self, tx_pin, rx_pin, baud_rate=9600):
        self.uart = UART(1, baudrate=baud_rate, tx=tx_pin, rx=rx_pin)
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0
        self.speed = 0.0
        self.heading = 0.0
        self.satellites = 0
        self.hdop = 99.99
        self.fix_quality = 0
        self.timestamp = ""
        self.has_fix_flag = False
        
        print(f"[GPS] Initialized on UART1")
    
    def update(self):
        """Read and parse NMEA sentences"""
        while self.uart.any():
            try:
                line = self.uart.readline()
                if line:
                    sentence = line.decode('ascii').strip()
                    self._parse_nmea(sentence)
            except:
                pass
    
    def _parse_nmea(self, sentence):
        """Parse NMEA sentence"""
        if not sentence.startswith('$'):
            return
        
        parts = sentence.split(',')
        msg_type = parts[0]
        
        try:
            if msg_type == '$GPGGA' or msg_type == '$GNGGA':
                # GGA - Fix data
                if len(parts) > 9:
                    self.fix_quality = int(parts[6]) if parts[6] else 0
                    self.satellites = int(parts[7]) if parts[7] else 0
                    self.hdop = float(parts[8]) if parts[8] else 99.99
                    
                    if self.fix_quality > 0 and parts[2] and parts[4]:
                        # Parse latitude
                        lat = float(parts[2])
                        lat_deg = int(lat / 100)
                        lat_min = lat - (lat_deg * 100)
                        self.latitude = lat_deg + (lat_min / 60)
                        if parts[3] == 'S':
                            self.latitude = -self.latitude
                        
                        # Parse longitude
                        lon = float(parts[4])
                        lon_deg = int(lon / 100)
                        lon_min = lon - (lon_deg * 100)
                        self.longitude = lon_deg + (lon_min / 60)
                        if parts[5] == 'W':
                            self.longitude = -self.longitude
                        
                        # Altitude
                        if parts[9]:
                            self.altitude = float(parts[9])
                        
                        self.has_fix_flag = True
                    else:
                        self.has_fix_flag = False
            
            elif msg_type == '$GPRMC' or msg_type == '$GNRMC':
                # RMC - Recommended minimum data
                if len(parts) > 7 and parts[2] == 'A':  # A = valid
                    # Speed in knots, convert to km/h
                    if parts[7]:
                        self.speed = float(parts[7]) * 1.852
                    # Heading
                    if parts[8]:
                        self.heading = float(parts[8])
        except:
            pass
    
    def has_fix(self):
        """Check if GPS has valid fix"""
        return self.has_fix_flag and self.fix_quality > 0
    
    def get_data(self):
        """Get GPS data as dictionary"""
        return {
            'has_fix': self.has_fix(),
            'latitude': self.latitude,
            'longitude': self.longitude,
            'altitude': self.altitude,
            'speed': self.speed,
            'heading': self.heading,
            'satellites': self.satellites,
            'hdop': self.hdop,
        }
    
    def print_data(self):
        """Print GPS data"""
        if self.has_fix():
            print(f"[GPS] {self.latitude:.6f}, {self.longitude:.6f}, "
                  f"Alt: {self.altitude:.1f}m, Sats: {self.satellites}")
        else:
            print(f"[GPS] No fix (Sats: {self.satellites})")

