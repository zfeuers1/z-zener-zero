"""
SD Card driver for MicroPython
Minimal implementation for ESP32-S3
"""
from machine import SPI
import time

class SDCard:
    """Minimal SD card driver"""
    CMD_TIMEOUT = 200
    R1_IDLE_STATE = const(1 << 0)
    TOKEN_CMD25 = const(0xfe)
    TOKEN_STOP_TRAN = const(0xfd)
    TOKEN_DATA = const(0xfe)

    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs

        # Initialize CS high
        self.cs.init(self.cs.OUT, value=1)

        # Initialize card
        self.init_card()

    def init_card(self):
        """Initialize SD card"""
        # Wait for card to be ready
        time.sleep_ms(20)
        
        # Send 80+ clock pulses with CS high
        self.cs(1)
        for _ in range(10):
            self.spi.write(b'\xff')
        
        # Send CMD0 (GO_IDLE_STATE)
        self.cs(0)
        self.cmd(0, 0, 0x95)
        
        # Initialize in SPI mode
        for _ in range(1000):
            self.cmd(1, 0, 0xff)  # CMD1 (SEND_OP_COND)
            if self.spi.read(1)[0] == 0:
                break
            time.sleep_ms(10)
        
        self.cs(1)
        self.spi.write(b'\xff')

    def cmd(self, cmd, arg, crc):
        """Send SD card command"""
        buf = bytearray(6)
        buf[0] = 0x40 | cmd
        buf[1] = arg >> 24
        buf[2] = arg >> 16
        buf[3] = arg >> 8
        buf[4] = arg
        buf[5] = crc
        self.spi.write(buf)

        # Wait for response
        for _ in range(self.CMD_TIMEOUT):
            r = self.spi.read(1)[0]
            if r != 0xff:
                return r
        return 0xff

    def readinto(self, buf):
        """Read a block from the card"""
        self.cs(0)
        
        # Wait for start token
        for _ in range(100000):
            if self.spi.read(1)[0] == self.TOKEN_DATA:
                break
        
        # Read data
        mv = memoryview(buf)
        self.spi.readinto(mv)
        
        # Read CRC
        self.spi.read(2)
        
        self.cs(1)
        self.spi.write(b'\xff')

    def writeblocks(self, block_num, buf):
        """Write blocks to card"""
        self.cs(0)
        
        # CMD24 (WRITE_SINGLE_BLOCK)
        if self.cmd(24, block_num, 0xff) != 0:
            self.cs(1)
            return
        
        # Send data token
        self.spi.write(bytes([self.TOKEN_DATA]))
        
        # Write data
        self.spi.write(buf)
        
        # Write dummy CRC
        self.spi.write(b'\xff\xff')
        
        # Wait for response
        resp = self.spi.read(1)[0]
        
        self.cs(1)
        self.spi.write(b'\xff')

