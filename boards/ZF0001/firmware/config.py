"""
ZF0001 Configuration
Edit these values for your setup
"""

# WiFi Configuration
WIFI_SSID = "YourWiFiSSID"
WIFI_PASSWORD = "YourWiFiPassword"

# Server Configuration
SERVER_HOST = "192.168.1.100"  # Your server IP
SERVER_PORT = 8080
SERVER_ENDPOINT = "/api/audio"

# Device Configuration
DEVICE_ID = "ZF0001-00001"  # Unique device identifier

# Pin Configuration (hardware-specific)
PINS = {
    # Audio
    'MIC_ADC': 1,           # GPIO1 - ADC for microphone
    
    # GPS
    'GPS_TX': 15,           # GPIO15 - ESP32 TX -> GNSS RX
    'GPS_RX': 16,           # GPIO16 - ESP32 RX <- GNSS TX
    
    # I2C (Fuel Gauge)
    'I2C_SDA': 21,          # GPIO21
    'I2C_SCL': 47,          # GPIO47
    'I2C_FREQ': 100000,     # 100kHz (recommended for 10kΩ pull-ups)
    
    # LEDs
    'LED_RED': 4,           # GPIO4
    'LED_GREEN': 5,         # GPIO5
    'LED_BLUE': 6,          # GPIO6
    
    # Buttons
    'BTN_RECORD': 2,        # GPIO2 - Record button
    'BTN_BOOT': 0,          # GPIO0 - Boot button
    
    # Status
    'CHG_STAT': 7,          # GPIO7 - Charger status
    'PG_STAT': 8,           # GPIO8 - Power good
    'FG_ALERT': 9,          # GPIO9 - Fuel gauge alert
    
    # SD Card (optional)
    'SD_CS': 10,
    'SD_MOSI': 11,
    'SD_CLK': 12,
    'SD_MISO': 13,
    'SD_DETECT': 14,
}

# Audio Configuration
AUDIO_SAMPLE_RATE = 16000   # 16kHz
AUDIO_BUFFER_SIZE = 160000  # 160,000 samples = 10 seconds of audio (~320KB fits in RAM)
AUDIO_SEND_INTERVAL = 10000  # Send every 10 seconds (ms)

# GPS Configuration
GPS_BAUD_RATE = 9600
GPS_UPDATE_INTERVAL = 1000  # Update every 1 second (ms)

# Battery Configuration
BATTERY_UPDATE_INTERVAL = 5000  # Update every 5 seconds (ms)
BATTERY_LOW_THRESHOLD = 20      # 20% warning
BATTERY_CRITICAL_THRESHOLD = 10 # 10% critical

# Network Configuration
HTTP_TIMEOUT = 10  # seconds
WIFI_CONNECT_TIMEOUT = 20  # seconds

# Debug Configuration
DEBUG = True
DEBUG_AUDIO_STATS = True
DEBUG_GPS_DATA = True
DEBUG_BATTERY_DATA = True

