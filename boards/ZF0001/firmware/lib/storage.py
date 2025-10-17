"""
SD card storage module
Saves audio as WAV files when WiFi fails or for backup
"""
from machine import SPI, Pin
import os
import struct
import time

class SDCard:
    """MicroSD card interface"""
    def __init__(self, cs_pin, mosi_pin, miso_pin, clk_pin):
        try:
            # Initialize SPI
            self.spi = SPI(1, baudrate=10_000_000,
                          sck=Pin(clk_pin),
                          mosi=Pin(mosi_pin),
                          miso=Pin(miso_pin))
            
            # Import SD card driver (local file)
            from . import sdcard as sdcard_module
            self.sd = sdcard_module.SDCard(self.spi, Pin(cs_pin))
            
            # Mount filesystem
            os.mount(self.sd, '/sd')
            
            # Create recordings directory
            try:
                os.mkdir('/sd/recordings')
            except:
                pass  # Already exists
            
            self.mounted = True
            print("[SD] Card mounted successfully")
            
            # Check free space
            stats = os.statvfs('/sd')
            free_mb = (stats[0] * stats[3]) / (1024 * 1024)
            print(f"[SD] Free space: {free_mb:.1f} MB")
            
        except Exception as e:
            print(f"[SD] Mount failed: {e}")
            self.mounted = False
    
    def is_mounted(self):
        """Check if SD card is mounted"""
        return self.mounted
    
    def save_wav(self, filename, samples, sample_rate=16000):
        """Save audio samples as WAV file"""
        if not self.mounted:
            return False
        
        try:
            filepath = f"/sd/recordings/{filename}"
            
            with open(filepath, 'wb') as f:
                # Write WAV header
                num_samples = len(samples)
                num_channels = 1
                bytes_per_sample = 2  # 16-bit
                byte_rate = sample_rate * num_channels * bytes_per_sample
                block_align = num_channels * bytes_per_sample
                
                # RIFF header
                f.write(b'RIFF')
                f.write(struct.pack('<I', 36 + num_samples * bytes_per_sample))  # File size
                f.write(b'WAVE')
                
                # fmt chunk
                f.write(b'fmt ')
                f.write(struct.pack('<I', 16))  # Chunk size
                f.write(struct.pack('<H', 1))   # PCM format
                f.write(struct.pack('<H', num_channels))
                f.write(struct.pack('<I', sample_rate))
                f.write(struct.pack('<I', byte_rate))
                f.write(struct.pack('<H', block_align))
                f.write(struct.pack('<H', 16))  # Bits per sample
                
                # data chunk
                f.write(b'data')
                f.write(struct.pack('<I', num_samples * bytes_per_sample))
                
                # Write audio data
                for sample in samples:
                    f.write(struct.pack('<h', sample))
            
            print(f"[SD] Saved {filepath} ({num_samples} samples)")
            return True
            
        except Exception as e:
            print(f"[SD] Save failed: {e}")
            return False
    
    def save_audio_backup(self, device_id, timestamp_ms, audio_buffer,
                         gps_data=None, battery_data=None):
        """Save audio with metadata as WAV file"""
        # Create filename with timestamp
        filename = f"{device_id}_{timestamp_ms}.wav"
        
        success = self.save_wav(filename, audio_buffer)
        
        if success and (gps_data or battery_data):
            # Save metadata as text file
            meta_file = f"/sd/recordings/{device_id}_{timestamp_ms}.txt"
            try:
                with open(meta_file, 'w') as f:
                    f.write(f"Device: {device_id}\n")
                    f.write(f"Timestamp: {timestamp_ms}\n")
                    if gps_data and gps_data.get('has_fix'):
                        f.write(f"GPS: {gps_data['latitude']:.6f}, {gps_data['longitude']:.6f}\n")
                        f.write(f"Altitude: {gps_data['altitude']:.1f}m\n")
                        f.write(f"Satellites: {gps_data['satellites']}\n")
                    if battery_data:
                        f.write(f"Battery: {battery_data['voltage']:.2f}V, {battery_data['soc']:.1f}%\n")
            except:
                pass
        
        return success
    
    def list_files(self):
        """List all WAV files on SD card"""
        if not self.mounted:
            return []
        
        try:
            files = os.listdir('/sd/recordings')
            wav_files = [f for f in files if f.endswith('.wav')]
            return wav_files
        except:
            return []
    
    def get_free_space_mb(self):
        """Get free space in MB"""
        if not self.mounted:
            return 0
        
        try:
            stats = os.statvfs('/sd')
            return (stats[0] * stats[3]) / (1024 * 1024)
        except:
            return 0

