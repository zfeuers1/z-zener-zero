"""
ZF0001 Wearable Voice Logger - Main Application

Records audio, tags with GPS and battery data, streams to server via WiFi
"""
import time
import gc
from machine import Pin

# Import configuration
import config

# Import modules
from lib.hardware import LED, Button, StatusPins
from lib.audio import Audio
from lib.gps import GPS
from lib.battery import Battery
from lib.network import Network
from lib.storage import SDCard

print("\n" + "="*40)
print("ZF0001 Wearable Voice Logger")
print("="*40)
print(f"Device ID: {config.DEVICE_ID}")
print(f"Firmware: MicroPython v1.0.0")
print("="*40 + "\n")

# ============================================================================
# Initialize Hardware
# ============================================================================
print("[INIT] Initializing hardware...")

# LEDs
led = LED(config.PINS['LED_RED'], config.PINS['LED_GREEN'], config.PINS['LED_BLUE'])
led.set(True, False, False)  # Red
time.sleep(0.2)
led.set(False, True, False)  # Green
time.sleep(0.2)
led.set(False, False, True)  # Blue
time.sleep(0.2)
led.off()

# Buttons
btn_record = Button(config.PINS['BTN_RECORD'])

# Status pins
status = StatusPins(
    config.PINS['CHG_STAT'],
    config.PINS['PG_STAT'],
    config.PINS['FG_ALERT']
)

# ============================================================================
# Initialize Peripherals
# ============================================================================
print("[INIT] Initializing peripherals...")

# Audio
audio = Audio(
    config.PINS['MIC_ADC'],
    config.AUDIO_SAMPLE_RATE,
    config.AUDIO_BUFFER_SIZE
)

# GPS
gps = GPS(
    config.PINS['GPS_TX'],
    config.PINS['GPS_RX'],
    config.GPS_BAUD_RATE
)

# Battery
battery = Battery(
    config.PINS['I2C_SDA'],
    config.PINS['I2C_SCL']
)

# Network
network = Network(
    config.WIFI_SSID,
    config.WIFI_PASSWORD,
    config.SERVER_HOST,
    config.SERVER_PORT,
    config.SERVER_ENDPOINT
)

# SD Card (for backup when WiFi fails)
try:
    sd = SDCard(
        config.PINS['SD_CS'],
        config.PINS['SD_MOSI'],
        config.PINS['SD_MISO'],
        config.PINS['SD_CLK']
    )
except Exception as e:
    print(f"[SD] Not available: {e}")
    sd = None

# ============================================================================
# Connect to WiFi
# ============================================================================
print("[INIT] Connecting to WiFi...")
led.blue_on()

if network.connect(config.WIFI_CONNECT_TIMEOUT):
    print("[INIT] WiFi connected successfully!")
    led.green_on()
else:
    print("[INIT] WiFi connection failed!")
    led.set(True, False, False)  # Red = error
    time.sleep(2)

# Initial battery reading
battery.print_data(status)

print("\n[READY] Press RECORD button to start recording")
print("[READY] Waiting for GPS fix...\n")

# ============================================================================
# Main Loop
# ============================================================================
is_recording = False
last_gps_update = time.ticks_ms()
last_battery_update = time.ticks_ms()
last_status_print = time.ticks_ms()
last_send_time = time.ticks_ms()

# Pre-fetch data
gps_data = gps.get_data()
battery_data = battery.get_data(status)

try:
    while True:
        now = time.ticks_ms()
        
        # ========================================
        # Button Handling
        # ========================================
        if btn_record.was_pressed():
            is_recording = not is_recording
            
            if is_recording:
                print("\n[RECORD] *** RECORDING STARTED ***")
                led.red_on()
                
                # Check prerequisites
                if not network.is_connected():
                    print("[WARNING] Not connected to WiFi!")
                if not gps.has_fix():
                    print("[WARNING] No GPS fix yet!")
            else:
                print("\n[RECORD] *** RECORDING STOPPED ***")
                led.green_on()
        
        # ========================================
        # GPS Update
        # ========================================
        gps.update()
        
        if time.ticks_diff(now, last_gps_update) > config.GPS_UPDATE_INTERVAL:
            last_gps_update = now
            gps_data = gps.get_data()
            
            if config.DEBUG_GPS_DATA and gps.has_fix():
                gps.print_data()
        
        # ========================================
        # Battery Update
        # ========================================
        if time.ticks_diff(now, last_battery_update) > config.BATTERY_UPDATE_INTERVAL:
            last_battery_update = now
            battery_data = battery.get_data(status)
            
            if config.DEBUG_BATTERY_DATA:
                battery.print_data(status)
            
            # Check critical battery
            if battery_data['is_critical'] and is_recording:
                print("[WARNING] Critical battery! Stopping recording.")
                is_recording = False
                led.green_on()
        
        # ========================================
        # WiFi Reconnect
        # ========================================
        if not network.is_connected():
            if is_recording:
                print("[WARNING] WiFi disconnected during recording!")
            
            led.blue_on()
            if network.connect(10):
                led.green_on() if not is_recording else led.red_on()
        
        # ========================================
        # Audio Recording
        # ========================================
        if is_recording:
            # Continuously sample audio
            audio.sample()  # Returns True when buffer full
            
            # Send every second (buffer fills every 1 second with 16000 samples)
            if time.ticks_diff(now, last_send_time) >= config.AUDIO_SEND_INTERVAL:
                audio_buffer = audio.get_buffer()
                
                if audio_buffer and network.is_connected():
                    # Get audio stats
                    if config.DEBUG_AUDIO_STATS:
                        stats = audio.get_stats()
                        print(f"[AUDIO] Peak-to-peak: {stats['peak_to_peak']} "
                              f"({stats['utilization']:.1f}% of range)")
                    
                    # Send packet (10 seconds of audio = 160,000 samples)
                    print(f"[SEND] Sending {len(audio_buffer)} samples (10 sec), "
                          f"GPS: {'VALID' if gps_data['has_fix'] else 'NO FIX'}, "
                          f"Battery: {battery_data['soc']:.1f}%")
                    
                    success = network.send_audio_packet(
                        config.DEVICE_ID,
                        time.ticks_ms(),
                        audio_buffer,
                        config.AUDIO_SAMPLE_RATE,
                        gps_data,
                        battery_data
                    )
                    
                    last_send_time = now
                    
                    if success:
                        # Quick green blink
                        led.off()
                        time.sleep_ms(50)
                        led.red_on()
                    else:
                        # WiFi send failed - save to SD card as backup
                        if sd and sd.is_mounted():
                            print("[BACKUP] WiFi failed, saving to SD card...")
                            sd.save_audio_backup(
                                config.DEVICE_ID,
                                time.ticks_ms(),
                                audio_buffer,
                                gps_data,
                                battery_data
                            )
                        
                        # Error blink
                        for _ in range(2):
                            led.off()
                            time.sleep_ms(50)
                            led.red_on()
                            time.sleep_ms(50)
        
        # ========================================
        # Status Report
        # ========================================
        if time.ticks_diff(now, last_status_print) > 30000:  # Every 30 seconds
            last_status_print = now
            
            print("\n" + "="*40)
            print("STATUS REPORT")
            print("="*40)
            print(f"Uptime: {time.ticks_ms() // 1000} seconds")
            print(f"State: {'RECORDING' if is_recording else 'IDLE'}")
            print(f"Free RAM: {gc.mem_free()} bytes")
            
            network.print_stats()
            
            print(f"[GPS] Fix: {'YES' if gps.has_fix() else 'NO'}, "
                  f"Sats: {gps_data['satellites']}")
            if gps.has_fix():
                print(f"[GPS] {gps_data['latitude']:.6f}, {gps_data['longitude']:.6f}")
            
            battery.print_data(status)
            
            print("="*40 + "\n")
        
        # Small delay to prevent tight loop
        time.sleep_ms(1)

except KeyboardInterrupt:
    print("\n[EXIT] Stopped by user")
    led.off()

except Exception as e:
    print(f"\n[ERROR] Exception: {e}")
    import sys
    sys.print_exception(e)
    led.set(True, False, False)  # Red for error

