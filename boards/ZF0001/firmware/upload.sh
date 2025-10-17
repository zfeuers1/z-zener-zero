#!/bin/bash
# Upload MicroPython firmware to ZF0001

PORT=${1:-/dev/ttyACM0}

echo "Uploading MicroPython firmware to $PORT"
echo "========================================"

# Check if mpremote is installed
if ! command -v mpremote &> /dev/null; then
    echo "Error: mpremote not found. Install with: pip3 install mpremote"
    exit 1
fi

# Create lib directory on device
echo "Creating lib directory..."
mpremote connect $PORT fs mkdir :lib 2>/dev/null || true

# Upload config
echo "Uploading config.py..."
mpremote connect $PORT fs cp config.py :

# Upload main
echo "Uploading main.py..."
mpremote connect $PORT fs cp main.py :

# Upload library files
echo "Uploading lib/audio.py..."
mpremote connect $PORT fs cp lib/audio.py :lib/

echo "Uploading lib/gps.py..."
mpremote connect $PORT fs cp lib/gps.py :lib/

echo "Uploading lib/battery.py..."
mpremote connect $PORT fs cp lib/battery.py :lib/

echo "Uploading lib/network.py..."
mpremote connect $PORT fs cp lib/network.py :lib/

echo "Uploading lib/hardware.py..."
mpremote connect $PORT fs cp lib/hardware.py :lib/

echo "Uploading lib/storage.py..."
mpremote connect $PORT fs cp lib/storage.py :lib/

echo "Uploading lib/sdcard.py..."
mpremote connect $PORT fs cp lib/sdcard.py :lib/

echo ""
echo "✓ Upload complete!"
echo ""
echo "To run the firmware:"
echo "  mpremote connect $PORT run main.py"
echo ""
echo "Or press the RESET button on the board"
echo "(if main.py is named boot.py, it runs automatically)"

