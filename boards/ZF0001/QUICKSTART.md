# ZF0001 Quick Start Guide - Mac

**From zero to running firmware in 15 minutes**

---

## 📦 What You Need

- ZF0001 board
- USB-C cable (data capable, not charge-only)
- Mac computer
- WiFi network
- Li-Ion battery (optional for initial testing)

---

## Step 1: Plug In Board (30 seconds)

1. **Connect USB-C cable** from Mac to ZF0001 board
2. **Flip power switch to ON** (slide switch)
3. **Green power LED should light up** ✅

If green LED doesn't light:
- Check USB cable (try different one)
- Check power switch position
- Check battery is connected OR USB provides power

---

## Step 2: Install Software on Mac (5 minutes)

### Install Homebrew (if not already installed)

```bash
# Open Terminal app
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install Python Tools

```bash
# Install Python tools via Homebrew
brew install python3

# Install esptool (for flashing)
pip3 install esptool

# Install mpremote (for uploading code)
pip3 install mpremote
```

**Check installation:**
```bash
esptool.py version
# Should show: esptool.py v4.x.x

mpremote --help
# Should show usage info
```

---

## Step 3: Find Your Device (1 minute)

```bash
# List USB serial devices
ls /dev/cu.usbmodem*

# Should show something like:
# /dev/cu.usbmodem14201
```

**If you see multiple devices**, unplug board, run command again to see which one disappears, then plug back in.

**Your port is:** `/dev/cu.usbmodem14201` (or similar - note this for later)

---

## Step 4: Download MicroPython (1 minute)

```bash
# Download ESP32-S3 MicroPython firmware
cd ~/Downloads
curl -O https://micropython.org/resources/firmware/ESP32_GENERIC_S3-20231005-v1.21.0.bin
```

---

## Step 5: Flash MicroPython (2 minutes)

```bash
# Erase flash (only needed first time)
esptool.py --chip esp32s3 --port /dev/cu.usbmodem14201 erase_flash

# Flash MicroPython
esptool.py --chip esp32s3 --port /dev/cu.usbmodem14201 --baud 460800 \
    write_flash -z 0x0 ESP32_GENERIC_S3-20231005-v1.21.0.bin

# Wait for "Hash of data verified" message
```

**Expected output:**
```
Chip is ESP32-S3
...
Wrote 1576960 bytes at 0x00000000 in 35.2 seconds
Hash of data verified.

Leaving...
```

✅ **MicroPython is now installed!**

---

## Step 6: Test Connection (1 minute)

```bash
# Connect to device
mpremote connect /dev/cu.usbmodem14201

# You should see:
Connected to MicroPython at /dev/cu.usbmodem14201
Use Ctrl-] to exit this shell
>>>
```

**Test it:**
```python
>>> print("Hello from ESP32-S3!")
Hello from ESP32-S3!

>>> import machine
>>> machine.freq()
240000000  # 240 MHz - working!

>>> # Blink LED
>>> led = machine.Pin(4, machine.Pin.OUT)
>>> led.on()   # Red LED should light
>>> led.off()

>>> # Exit (press Ctrl-] )
```

✅ **Board is working!**

---

## Step 7: Configure WiFi (2 minutes)

Navigate to firmware folder and edit config:

```bash
cd /path/to/z-zener-zero/boards/ZF0001/firmware

# Edit config.py (use nano, vim, or any text editor)
nano config.py
```

**Change these lines:**
```python
WIFI_SSID = "YourWiFiName"          # ← Your WiFi network name
WIFI_PASSWORD = "YourWiFiPassword"   # ← Your WiFi password
SERVER_HOST = "192.168.1.100"       # ← Your Mac's IP address
DEVICE_ID = "ZF0001-001"            # ← Unique ID for this device
```

**To find your Mac's IP:**
```bash
ipconfig getifaddr en0  # WiFi
# Or: System Settings → Network → WiFi → Details → TCP/IP
```

Save and exit (Ctrl-X, then Y, then Enter in nano)

---

## Step 8: Upload Firmware (1 minute)

```bash
# Make upload script executable
chmod +x upload.sh

# Upload all firmware files
./upload.sh /dev/cu.usbmodem14201
```

**Expected output:**
```
Uploading MicroPython firmware to /dev/cu.usbmodem14201
========================================
Creating lib directory...
Uploading config.py...
Uploading main.py...
Uploading lib/audio.py...
Uploading lib/gps.py...
Uploading lib/battery.py...
Uploading lib/network.py...
Uploading lib/hardware.py...
Uploading lib/storage.py...

✓ Upload complete!
```

---

## Step 9: Test Firmware (2 minutes)

```bash
# Connect to device and watch output
mpremote connect /dev/cu.usbmodem14201

# Press Reset button on board (or soft reset)
# You should see:
```

```
========================================
ZF0001 Wearable Voice Logger
========================================
Device ID: ZF0001-001
Firmware: MicroPython v1.0.0
========================================

[INIT] Initializing hardware...
[AUDIO] Initialized: 16000 Hz, 480000 samples
[GPS] Initialized on UART1
[BATTERY] MAX17048 detected, version: 0x0012
[NETWORK] WiFi initialized
[SD] Card mounted successfully
[SD] Free space: 7234.5 MB
[INIT] Connecting to WiFi...
..
[NETWORK] Connected! IP: 192.168.1.50
[BATTERY] 3.87V, 72.5% SOC

[READY] Press RECORD button to start recording
[READY] Waiting for GPS fix...
```

✅ **Firmware is running!**

---

## Step 10: Test Recording (2 minutes)

### Start Test Server on Mac

```bash
# Simple test server (run in another terminal)
python3 -m http.server 8080

# Or use this simple Flask server:
```

Save as `test_server.py`:
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/audio', methods=['POST'])
def receive_audio():
    data = request.json
    print(f"\n✓ Received {len(data['audio']['data'])} samples")
    print(f"  GPS: {data.get('gps')}")
    print(f"  Battery: {data['battery']['soc']:.1f}%")
    return jsonify({'status': 'success'}), 200

app.run(host='0.0.0.0', port=8080)
```

Run it:
```bash
pip3 install flask
python3 test_server.py
# Server running on port 8080
```

### Test on Device

1. **Press RECORD button** on board
2. **Red LED turns on** (recording)
3. **Wait 30 seconds**
4. Watch serial monitor - should show: `[SEND] Sending 480000 samples...`
5. **Server receives data** ✅
6. **Press RECORD again** to stop

---

## Debugging Commands

### Connect and Watch Output

```bash
mpremote connect /dev/cu.usbmodem14201
# See all print() statements
```

### Interactive Testing

```bash
mpremote connect /dev/cu.usbmodem14201

# Press Ctrl-C to interrupt, then:
>>> import main

# Check battery
>>> main.battery.get_voltage()
3.87

# Check GPS
>>> main.gps.has_fix()
False  # Normal indoors

# Test LED
>>> main.led.green_on()
>>> main.led.off()

# Force recording
>>> main.is_recording = True

# Check SD card
>>> main.sd.is_mounted()
True
>>> main.sd.get_free_space_mb()
7234.5

# Exit: Ctrl-D to resume, or Ctrl-] to disconnect
```

### Edit and Re-upload

```bash
# Edit any file
nano firmware/main.py

# Upload just that file
mpremote connect /dev/cu.usbmodem14201 fs cp main.py :

# Soft reset to reload
mpremote connect /dev/cu.usbmodem14201 exec "import machine; machine.soft_reset()"
```

---

## Troubleshooting

### "Device not found"

```bash
# Check device is connected
ls /dev/cu.usbmodem*

# If nothing shows:
- Try different USB cable
- Press Reset button on board
- Check power LED is on
```

### "Permission denied"

```bash
# Give your user access (Mac usually doesn't need this)
sudo chmod 666 /dev/cu.usbmodem14201
```

### "WiFi won't connect"

```python
# Test WiFi manually in REPL
>>> import network
>>> wlan = network.WLAN(network.STA_IF)
>>> wlan.active(True)
>>> wlan.scan()  # Should show networks
[(b'YourWiFi', ...)]

>>> wlan.connect("YourWiFi", "YourPassword")
>>> # Wait 10 seconds
>>> wlan.isconnected()
True
```

### "GPS no fix"

- Must be outdoors or near window (GPS doesn't work indoors)
- Wait 30-60 seconds for cold start
- Check antenna is connected (u.FL connector)

### "SD card not detected"

```python
>>> import main
>>> main.sd.is_mounted()
False  # Not mounted

# Check if card is inserted
# Try reinitializing
>>> from lib.storage import SDCard
>>> sd = SDCard(10, 11, 13, 12)
```

---

## SD Card Backup Feature

### How It Works

**Normal operation:**
- Device buffers 30 seconds of audio
- Sends to server via WiFi
- ✅ If successful: green flash, continue

**WiFi fails:**
- ❌ Server not reachable
- Device automatically saves to SD card as WAV file
- Format: `{DEVICE_ID}_{timestamp}.wav`
- Also saves `{DEVICE_ID}_{timestamp}.txt` with GPS/battery metadata

**SD Card Files:**
```
/sd/recordings/
├── ZF0001-001_123456.wav    (30 seconds of audio)
├── ZF0001-001_123456.txt    (GPS and battery data)
├── ZF0001-001_456789.wav
├── ZF0001-001_456789.txt
└── ...
```

### Retrieve Files from SD Card

**Option 1: Remove SD card and read on computer**
- Power off device
- Remove microSD card
- Insert into computer SD reader
- Copy files from `recordings/` folder

**Option 2: Download via USB** (future feature)

---

## File Structure

```
firmware/
├── config.py           ← EDIT WiFi/server settings here
├── main.py             Main application
├── upload.sh           Upload script
├── FIRMWARE.md         Complete firmware docs
└── lib/
    ├── audio.py        Audio sampling (16kHz)
    ├── gps.py          GPS/NMEA parsing
    ├── battery.py      Fuel gauge I2C
    ├── network.py      WiFi + HTTP client
    ├── hardware.py     LED + button control
    └── storage.py      SD card WAV files
```

---

## Complete Command Reference

```bash
# Flash MicroPython (once)
esptool.py --chip esp32s3 --port /dev/cu.usbmodem14201 \
    write_flash -z 0x0 ESP32_GENERIC_S3-20231005-v1.21.0.bin

# Upload firmware (after changes)
./upload.sh /dev/cu.usbmodem14201

# Monitor output
mpremote connect /dev/cu.usbmodem14201

# Interactive debug
mpremote connect /dev/cu.usbmodem14201
>>> import main  # Then test anything

# Soft reset
mpremote connect /dev/cu.usbmodem14201 \
    exec "import machine; machine.soft_reset()"

# Upload single file
mpremote connect /dev/cu.usbmodem14201 fs cp main.py :
```

---

## Next Steps

1. ✅ **Firmware is running**
2. Build your server (see FIRMWARE.md for API spec)
3. Test with microphone connected (3.5mm jack)
4. Test outdoors for GPS fix
5. Monitor SD card files when WiFi unavailable

---

**Questions? Use interactive REPL to debug anything!**

```bash
mpremote connect /dev/cu.usbmodem14201
>>> import main
>>> # Test anything interactively
```

---

**Guide Version:** 1.0  
**Last Updated:** October 17, 2025  
**Platform:** macOS
