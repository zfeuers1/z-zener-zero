# ZF0001 Wearable Voice Logger

**Status:** In Progress 
**Revision:** v0.0.1

A compact wearable device that continuously records audio, captures GPS location, and monitors battery status. Records 30-second audio clips (16kHz PCM), uploads them to a server via WiFi, and saves backups to SD card. Built with ESP32-S3, MAX-M10S GPS, and powered by a rechargeable LiPo battery with USB-C charging.

---

## 📚 Documentation (3 Files Only!)

1. **[HARDWARE.md](boards/ZF0001/HARDWARE.md)** - Complete hardware design with diagrams
2. **[firmware/FIRMWARE.md](boards/ZF0001/firmware/FIRMWARE.md)** - Firmware API and server guide  
3. **[QUICKSTART.md](boards/ZF0001/QUICKSTART.md)** - Step-by-step: flash, program, debug (Mac)

---

## ⚡ Quick Summary

### Audio Recording
- **Format:** Raw PCM samples (16kHz, 12-bit, mono)
- **Buffering:** 30 seconds on device (in PSRAM)
- **Upload:** Every 30 seconds via WiFi HTTP POST
- **Backup:** Saves to SD card as WAV if WiFi fails

### What Device Sends
```json
{
  "audio": { "data": [480,000 samples], "sample_rate": 16000 },
  "gps": { "latitude": 37.7749, "longitude": -122.4194 },
  "battery": { "voltage": 3.85, "soc": 67.5 }
}
```

### MP3 Conversion (5 Lines!)
```python
from pydub import AudioSegment
audio = AudioSegment(samples.tobytes(), frame_rate=16000, sample_width=2, channels=1)
audio.export("out.mp3", format="mp3", bitrate="64k")
```

---

## 🚀 Get Started (Mac)

```bash
# 1. Flash MicroPython (once)
esptool.py --chip esp32s3 --port /dev/cu.usbmodem14201 \
    write_flash -z 0x0 micropython.bin

# 2. Configure WiFi in boards/ZF0001/firmware/config.py
WIFI_SSID = "YourWiFi"

# 3. Upload firmware
cd boards/ZF0001/firmware && ./upload.sh /dev/cu.usbmodem14201

# 4. Test
mpremote connect /dev/cu.usbmodem14201
```

**See [QUICKSTART.md](boards/ZF0001/QUICKSTART.md) for complete step-by-step guide**

---

## 🔧 Debugging

Debug over USB (no JTAG needed):

```bash
mpremote connect /dev/cu.usbmodem14201
>>> import main
>>> main.battery.get_voltage()  # Check anything instantly!
3.87
```

---

## 📁 Files

```
boards/ZF0001/
├── README.md              ← Original board README
├── HARDWARE.md            ← Hardware design with mermaid diagrams
├── QUICKSTART.md          ← Complete Mac setup guide
├── ZF0001.zen             ← Board design file
└── firmware/
    ├── FIRMWARE.md        ← API spec and server code
    ├── config.py          ← Edit WiFi/server settings
    ├── main.py            ← Main application
    ├── upload.sh          ← Upload script
    └── lib/               ← Modules (audio, gps, battery, network, storage)
```

---

**Ready to build? See [QUICKSTART.md](boards/ZF0001/QUICKSTART.md)!**
