"""
Audio capture module
Samples microphone via ADC at configurable rate
"""
from machine import ADC, Timer
import array
import time

class Audio:
    """Audio sampling class"""
    def __init__(self, adc_pin, sample_rate=16000, buffer_size=1024):
        self.adc = ADC(adc_pin)
        self.adc.atten(ADC.ATTN_11DB)  # 0-2.45V range
        self.adc.width(ADC.WIDTH_12BIT)  # 12-bit resolution
        
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        
        # Pre-allocate buffer for efficiency
        self.buffer = array.array('h', [0] * buffer_size)  # signed 16-bit
        self.buffer_index = 0
        self.buffer_ready = False
        
        # Timing
        self.sample_interval_us = 1000000 // sample_rate
        self.last_sample_time = time.ticks_us()
        
        print(f"[AUDIO] Initialized: {sample_rate} Hz, {buffer_size} samples")
    
    def sample(self):
        """Sample one audio point (call continuously in loop)"""
        now = time.ticks_us()
        
        # Check if it's time for next sample
        if time.ticks_diff(now, self.last_sample_time) < self.sample_interval_us:
            return False
        
        self.last_sample_time = now
        
        # Read ADC (0-4095 for 12-bit)
        raw = self.adc.read()
        
        # Convert to signed 16-bit, centered at 0
        # ADC range: 0-4095, center: 2048
        sample = (raw - 2048) * 16  # Scale to ~±32k range
        
        # Store in buffer
        self.buffer[self.buffer_index] = sample
        self.buffer_index += 1
        
        # Check if buffer is full
        if self.buffer_index >= self.buffer_size:
            self.buffer_index = 0
            self.buffer_ready = True
            return True
        
        return False
    
    def get_buffer(self):
        """Get audio buffer (returns None if not ready)"""
        if not self.buffer_ready:
            return None
        
        self.buffer_ready = False
        return self.buffer
    
    def get_stats(self):
        """Get audio statistics"""
        if len(self.buffer) == 0:
            return None
        
        min_val = min(self.buffer)
        max_val = max(self.buffer)
        avg_val = sum(self.buffer) // len(self.buffer)
        peak_to_peak = max_val - min_val
        
        return {
            'min': min_val,
            'max': max_val,
            'avg': avg_val,
            'peak_to_peak': peak_to_peak,
            'utilization': (peak_to_peak / 65536) * 100  # Percent of range
        }

