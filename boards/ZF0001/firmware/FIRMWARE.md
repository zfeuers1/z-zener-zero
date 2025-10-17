# ZF0001 Firmware Documentation

**Language:** MicroPython  
**Version:** 1.0.0  
**Hardware:** ZF0001 Rev A

---

## Overview

Records audio from microphone, tags with GPS and battery data, and streams to server via WiFi.

**Key Features:**
- Audio: 16kHz mono, 12-bit ADC
- Buffering: 30 seconds on-device (uses PSRAM)
- Upload: Every 30 seconds via HTTP POST
- GPS tagging: Real-time location data
- Battery monitoring: Voltage and state-of-charge

---

## Configuration

Edit `config.py`:

```python
# WiFi - CHANGE THESE
WIFI_SSID = "YourWiFiNetwork"
WIFI_PASSWORD = "YourPassword"

# Server - CHANGE THESE  
SERVER_HOST = "192.168.1.100"  # Your server IP
SERVER_PORT = 8080
SERVER_ENDPOINT = "/api/audio"

# Device ID
DEVICE_ID = "ZF0001-00001"  # Make unique per device
```

---

## Audio Format & Upload Frequency

### What Gets Uploaded

**Format:** Raw PCM samples (not MP3/WAV file)  
**Container:** JSON via HTTP POST  
**Encoding:** Array of signed 16-bit integers

**Specifications:**
- **Sample Rate:** 16,000 Hz (16 kHz)
- **Bit Depth:** 12-bit (from ADC)
- **Channels:** Mono (1 channel)
- **Buffer Size:** 480,000 samples = **30 seconds of audio**
- **Upload Frequency:** Once every **30 seconds**

**Why 30 seconds?**
- ✅ Reduces network overhead (1 request/30s vs 15/s)
- ✅ Near real-time for transcription (acceptable latency)
- ✅ Fits in PSRAM (480K samples × 2 bytes = 960 KB)
- ✅ Reasonable chunk size for server processing

**Data Size:**
- Audio samples: 480,000 × 2 bytes = 960 KB
- JSON overhead: ~1-2 KB
- **Total payload: ~960 KB per upload**
- **Bandwidth: ~32 KB/sec average = 256 Kbps**

Much better than previous 15.6 uploads/sec!

---

## Server API

### HTTP Request

**Method:** POST  
**URL:** `http://{SERVER_HOST}:{SERVER_PORT}{SERVER_ENDPOINT}`  
**Content-Type:** application/json

### JSON Payload Structure

```json
{
  "device_id": "ZF0001-00001",
  "timestamp": 123456789,
  "audio": {
    "sample_rate": 16000,
    "bit_depth": 12,
    "channels": 1,
    "samples": 480000,
    "format": "raw_pcm",
    "duration_ms": 30000,
    "data": [0, 127, 253, ..., -320]  // 480,000 samples
  },
  "gps": {
    "latitude": 37.774929,
    "longitude": -122.419418,
    "altitude": 16.5,
    "speed": 8.3,
    "satellites": 12
  } || null,
  "battery": {
    "voltage": 3.85,
    "soc": 67.5,
    "charging": false
  }
}
```

**Expected Response:**
```json
{
  "status": "success",
  "message": "Audio received"
}
```

---

## Converting to MP3 on Server - Super Easy!

### Method 1: Using pydub (5 lines of code!)

```python
from pydub import AudioSegment
import numpy as np

# Get samples from JSON
samples = np.array(data['audio']['data'], dtype=np.int16)

# Convert to audio segment
audio = AudioSegment(
    samples.tobytes(),
    frame_rate=16000,
    sample_width=2,  # 16-bit
    channels=1       # Mono
)

# Save as MP3 - done!
audio.export("output.mp3", format="mp3", bitrate="64k")
```

**Install:** `pip install pydub` and `brew install ffmpeg`

### Method 2: Direct Transcription (No MP3 needed!)

```python
import whisper
import numpy as np

# Load Whisper model
model = whisper.load_model("base")

# Get samples and convert to float
samples = np.array(data['audio']['data'], dtype=np.int16)
audio_float = samples.astype(np.float32) / 32768.0

# Transcribe directly - no MP3 conversion!
result = model.transcribe(audio_float, fp16=False, language="en")
text = result["text"]  # Done!
```

**Install:** `pip install openai-whisper`

---

## Server Implementation - Complete Example

### Simple Flask Server with MP3 Conversion

```python
from flask import Flask, request, jsonify
import numpy as np
from pydub import AudioSegment
import io

app = Flask(__name__)

@app.route('/api/audio', methods=['POST'])
def receive_audio():
    try:
        data = request.json
        
        # Extract audio samples
        samples = np.array(data['audio']['data'], dtype=np.int16)
        sample_rate = data['audio']['sample_rate']
        device_id = data['device_id']
        
        print(f"Received {len(samples)} samples from {device_id}")
        
        # GPS data (if available)
        gps = data.get('gps')
        if gps:
            print(f"Location: {gps['latitude']:.6f}, {gps['longitude']:.6f}")
        
        # Battery data
        battery = data['battery']
        print(f"Battery: {battery['soc']:.1f}% ({battery['voltage']:.2f}V)")
        
        # Convert to MP3 (easy!)
        audio_segment = AudioSegment(
            samples.tobytes(),
            frame_rate=sample_rate,
            sample_width=2,  # 16-bit = 2 bytes
            channels=1       # Mono
        )
        
        # Export as MP3
        mp3_filename = f"{device_id}_{data['timestamp']}.mp3"
        audio_segment.export(mp3_filename, format="mp3", bitrate="64k")
        print(f"Saved as {mp3_filename}")
        
        # Or keep in memory and transcribe
        mp3_buffer = io.BytesIO()
        audio_segment.export(mp3_buffer, format="mp3", bitrate="64k")
        mp3_data = mp3_buffer.getvalue()
        
        # Send to transcription service (Whisper, Google Speech, etc.)
        # ... your transcription code here ...
        
        return jsonify({
            'status': 'success',
            'message': 'Audio received and processed',
            'samples': len(samples),
            'duration_sec': len(samples) / sample_rate
        }), 200
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

### Install Dependencies

```bash
pip install flask numpy pydub

# pydub requires ffmpeg
# Mac: brew install ffmpeg
# Linux: sudo apt install ffmpeg
# Windows: Download from ffmpeg.org
```

---

## Converting to MP3 - Super Easy!

### Method 1: Using pydub (Easiest)

```python
from pydub import AudioSegment
import numpy as np

# Get samples from JSON
samples = np.array(data['audio']['data'], dtype=np.int16)
sample_rate = data['audio']['sample_rate']

# Create audio segment
audio = AudioSegment(
    samples.tobytes(),
    frame_rate=sample_rate,
    sample_width=2,  # 16-bit
    channels=1       # Mono
)

# Save as MP3
audio.export("output.mp3", format="mp3", bitrate="64k")
```

**That's it! 5 lines of code!**

### Method 2: Using scipy + lameenc

```python
import numpy as np
from scipy.io import wavfile
import subprocess

# Get samples
samples = np.array(data['audio']['data'], dtype=np.int16)

# Save as WAV first
wavfile.write('temp.wav', 16000, samples)

# Convert to MP3 with ffmpeg
subprocess.run([
    'ffmpeg', '-i', 'temp.wav',
    '-acodec', 'libmp3lame',
    '-ab', '64k',
    'output.mp3'
])
```

### Method 3: Direct to Whisper (No MP3 needed!)

```python
import whisper
import numpy as np

# Load Whisper model (once)
model = whisper.load_model("base")

# Get samples from device
samples = np.array(data['audio']['data'], dtype=np.int16)

# Convert to float32 (-1.0 to 1.0 range)
audio_float = samples.astype(np.float32) / 32768.0

# Transcribe directly!
result = model.transcribe(
    audio_float,
    fp16=False,
    language="en"
)

text = result["text"]
print(f"Transcription: {text}")

# Save with GPS location
save_transcription(text, gps_data)
```

**Even easier - no MP3 conversion needed!**

---

## Updated Firmware Details

### Memory Usage

**Audio Buffer:**
- 480,000 samples × 2 bytes = 960 KB
- Stored in PSRAM (8 MB available)
- Only ~12% of PSRAM used

**Upload Stats:**
- **Frequency:** 1 upload every 30 seconds
- **Chunk size:** ~960 KB (30 seconds of audio)
- **Bandwidth:** ~32 KB/sec average (256 Kbps)
- **Latency:** 30 seconds (acceptable for transcription)

### Pin Configuration

All pins match hardware exactly (verified):

```python
PINS = {
    'MIC_ADC': 1,       # Microphone
    'GPS_TX': 15,       # To GNSS RX
    'GPS_RX': 16,       # From GNSS TX
    'I2C_SDA': 21,      # Fuel gauge
    'I2C_SCL': 47,      # Fuel gauge
    'LED_RED': 4,       # Status
    'LED_GREEN': 5,     # Status
    'LED_BLUE': 6,      # Status
    'BTN_RECORD': 2,    # Record control
}
```

---

## LED Status

| Color | Meaning |
|-------|---------|
| Green | Ready / Idle |
| Red | Recording (solid during 30s buffer) |
| Blue | Connecting to WiFi |
| Green flash | Upload successful |
| Red flash | Upload failed |

---

## Server Processing Pipeline

```
1. Receive JSON with 480,000 samples (30 seconds)
2. Convert to numpy array
3. Option A: Save as MP3 (5 lines of code with pydub)
4. Option B: Transcribe directly (Whisper doesn't need MP3)
5. Tag transcription with GPS coordinates
6. Store in database with battery metadata
7. Respond with success
```

**Processing time:** ~5-30 seconds depending on transcription model

---

## Example Complete Server

```python
from flask import Flask, request, jsonify
import numpy as np
from pydub import AudioSegment
import whisper
import datetime

app = Flask(__name__)

# Load Whisper once at startup
model = whisper.load_model("base")

@app.route('/api/audio', methods=['POST'])
def receive_audio():
    data = request.json
    
    # Extract data
    samples = np.array(data['audio']['data'], dtype=np.int16)
    sample_rate = data['audio']['sample_rate']
    device_id = data['device_id']
    timestamp = data['timestamp']
    
    # GPS and battery
    gps = data.get('gps')
    battery = data['battery']
    
    print(f"\n[{datetime.datetime.now()}] Received from {device_id}")
    print(f"  Audio: {len(samples)} samples ({len(samples)/sample_rate:.1f}s)")
    if gps:
        print(f"  GPS: {gps['latitude']:.6f}, {gps['longitude']:.6f}")
    print(f"  Battery: {battery['soc']:.1f}%")
    
    # Option 1: Save as MP3
    audio = AudioSegment(
        samples.tobytes(),
        frame_rate=sample_rate,
        sample_width=2,
        channels=1
    )
    mp3_file = f"recordings/{device_id}_{timestamp}.mp3"
    audio.export(mp3_file, format="mp3", bitrate="64k")
    print(f"  Saved: {mp3_file}")
    
    # Option 2: Transcribe
    audio_float = samples.astype(np.float32) / 32768.0
    result = model.transcribe(audio_float, fp16=False, language="en")
    text = result["text"]
    print(f"  Transcription: {text[:100]}...")
    
    # Save to database with GPS
    # save_to_db(device_id, text, gps, battery, timestamp)
    
    return jsonify({
        'status': 'success',
        'transcription': text,
        'mp3_file': mp3_file
    }), 200

if __name__ == '__main__':
    import os
    os.makedirs('recordings', exist_ok=True)
    app.run(host='0.0.0.0', port=8080)
```

**Dependencies:**
```bash
pip install flask numpy pydub openai-whisper
brew install ffmpeg  # or apt install ffmpeg
```

Run:
```bash
python server.py
# Server ready on port 8080
```

---

## Updated Specifications

### Audio Transmission

- **Buffer:** 30 seconds (480,000 samples)
- **Upload Frequency:** Once every 30 seconds
- **Payload Size:** ~960 KB per upload
- **Average Bandwidth:** ~32 KB/sec (256 Kbps)
- **Memory Used:** 960 KB (12% of 8MB PSRAM)

**Much better!**
- 15.6 uploads/sec → **1 upload/30sec** (467× reduction!)
- Still near real-time for transcription
- Much less network overhead
- More efficient for both device and server

### Server Processing

**Easy conversions available:**

| To Format | Library | Lines of Code |
|-----------|---------|---------------|
| **MP3** | pydub | 5 lines ✅ |
| **WAV** | scipy.io.wavfile | 1 line ✅ |
| **FLAC** | pydub | 5 lines ✅ |
| **Transcription** | whisper | 3 lines ✅ |

**No complex encoding needed!** Raw PCM → MP3 conversion is trivial with pydub.

---

## File Structure

```
firmware/
├── config.py           Configuration (edit WiFi/server)
├── main.py             Main application
├── upload.sh           Upload script
├── FIRMWARE.md         This file
└── lib/
    ├── audio.py        ADC sampling (16kHz)
    ├── gps.py          NMEA parsing
    ├── battery.py      MAX17048 I2C
    ├── network.py      WiFi + HTTP
    └── hardware.py     LEDs + buttons
```

---

## Quick Reference

### Upload Firmware
```bash
cd firmware
./upload.sh /dev/ttyACM0
```

### Monitor Output
```bash
mpremote connect /dev/ttyACM0
```

### Debug Interactive
```bash
mpremote connect /dev/ttyACM0
>>> import main
>>> main.battery.get_voltage()
```

---

**For hardware details, see HARDWARE.md**  
**For programming/debugging, see QUICKSTART.md**
