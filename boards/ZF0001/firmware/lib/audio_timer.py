"""
Audio capture using Timer interrupt (better than polling)
More accurate timing for 16kHz sampling
"""
from machine import ADC, Timer
import array

class Audio:
    """Timer-based audio sampling"""
    def __init__(self, adc_pin, sample_rate=16000, buffer_size=160000):
        self.adc = ADC(adc_pin)
        self.adc.atten(ADC.ATTN_11DB)
        self.adc.width(ADC.WIDTH_12BIT)
        
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        
        # Pre-allocate buffer
        self.buffer = array.array('h', [0] * buffer_size)
        self.buffer_index = 0
        self.buffer_ready = False
        
        # Create timer for precise sampling
        self.timer = Timer(0)
        self.sampling = False
        
        print(f"[AUDIO] Initialized with timer: {sample_rate} Hz")
    
    def start_sampling(self):
        """Start timer-based sampling"""
        if not self.sampling:
            self.buffer_index = 0
            self.buffer_ready = False
            
            # Start timer interrupt (calls _sample_isr at sample_rate frequency)
            period_us = 1000000 // self.sample_rate
            self.timer.init(
                mode=Timer.PERIODIC,
                period=period_us,
                callback=self._sample_isr
            )
            self.sampling = True
            print("[AUDIO] Timer sampling started")
    
    def stop_sampling(self):
        """Stop timer-based sampling"""
        if self.sampling:
            self.timer.deinit()
            self.sampling = False
            print("[AUDIO] Timer sampling stopped")
    
    def _sample_isr(self, timer):
        """Timer interrupt service routine - samples ADC"""
        # Read ADC
        raw = self.adc.read()
        
        # Convert to signed 16-bit
        sample = (raw - 2048) * 16
        
        # Store in buffer
        self.buffer[self.buffer_index] = sample
        self.buffer_index += 1
        
        # Check if full
        if self.buffer_index >= self.buffer_size:
            self.buffer_index = 0
            self.buffer_ready = True
            self.stop_sampling()  # Auto-stop when buffer full
    
    def is_ready(self):
        """Check if buffer is full"""
        return self.buffer_ready
    
    def get_buffer(self):
        """Get audio buffer"""
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
            'utilization': (peak_to_peak / 65536) * 100
        }

