"""
Network module
WiFi connectivity and HTTP client
"""
import network
import urequests
import ujson
import time

class Network:
    """WiFi and HTTP client"""
    def __init__(self, ssid, password, server_host, server_port, endpoint):
        self.ssid = ssid
        self.password = password
        self.server_host = server_host
        self.server_port = server_port
        self.endpoint = endpoint
        
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        
        self.packets_sent = 0
        self.packets_failed = 0
        
        print("[NETWORK] Initialized")
    
    def connect(self, timeout_sec=20):
        """Connect to WiFi"""
        if self.wlan.isconnected():
            print("[NETWORK] Already connected")
            return True
        
        print(f"[NETWORK] Connecting to {self.ssid}...")
        self.wlan.connect(self.ssid, self.password)
        
        start = time.time()
        while not self.wlan.isconnected():
            if time.time() - start > timeout_sec:
                print("[NETWORK] Connection timeout")
                return False
            time.sleep(0.5)
            print(".", end="")
        
        print()
        print(f"[NETWORK] Connected! IP: {self.wlan.ifconfig()[0]}")
        print(f"[NETWORK] Signal: {self.wlan.status('rssi')} dBm")
        return True
    
    def is_connected(self):
        """Check if connected to WiFi"""
        return self.wlan.isconnected()
    
    def get_rssi(self):
        """Get WiFi signal strength"""
        if self.is_connected():
            return self.wlan.status('rssi')
        return 0
    
    def send_audio_packet(self, device_id, timestamp_ms, audio_buffer, 
                         sample_rate, gps_data, battery_data):
        """Send audio packet to server"""
        if not self.is_connected():
            print("[NETWORK] Not connected")
            return False
        
        # Build URL
        url = f"http://{self.server_host}:{self.server_port}{self.endpoint}"
        
        # Build payload
        payload = {
            'device_id': device_id,
            'timestamp': timestamp_ms,
            'audio': {
                'sample_rate': sample_rate,
                'bit_depth': 12,
                'channels': 1,
                'samples': len(audio_buffer),
                'format': 'raw_pcm',
                'duration_ms': (len(audio_buffer) * 1000) // sample_rate,
                'data': list(audio_buffer),  # Convert array to list
            },
            'battery': {
                'voltage': battery_data['voltage'],
                'soc': battery_data['soc'],
                'charging': battery_data['is_charging'],
            }
        }
        
        # Add GPS if available
        if gps_data['has_fix']:
            payload['gps'] = {
                'latitude': gps_data['latitude'],
                'longitude': gps_data['longitude'],
                'altitude': gps_data['altitude'],
                'speed': gps_data['speed'],
                'heading': gps_data['heading'],
                'satellites': gps_data['satellites'],
                'hdop': gps_data['hdop'],
            }
        else:
            payload['gps'] = None
        
        # Send POST request
        try:
            print(f"[NETWORK] Sending to {url}")
            response = urequests.post(
                url,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            if response.status_code == 200 or response.status_code == 201:
                print(f"[NETWORK] ✓ Success: {response.text}")
                self.packets_sent += 1
                response.close()
                return True
            else:
                print(f"[NETWORK] ✗ Error {response.status_code}: {response.text}")
                self.packets_failed += 1
                response.close()
                return False
                
        except Exception as e:
            print(f"[NETWORK] ✗ Exception: {e}")
            self.packets_failed += 1
            return False
    
    def print_stats(self):
        """Print network statistics"""
        if self.is_connected():
            ip = self.wlan.ifconfig()[0]
            rssi = self.get_rssi()
            print(f"[NETWORK] IP: {ip}, RSSI: {rssi} dBm")
        else:
            print("[NETWORK] Not connected")
        print(f"[NETWORK] Sent: {self.packets_sent}, Failed: {self.packets_failed}")

