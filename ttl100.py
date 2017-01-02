import time, serial, sys, socket
import os.path

HOSTNAME = socket.gethostname()

default_config = [  0xc0,           # configure mode - 0xc0: persistent; 0xc2 non-persistent
                    0xFF,           # address high (broadcast)
                    0xFF,           # address low (broadcast)
                    0b00011000,     # parity (8N1): 00, baud rate (9600 bps): 011, air data rate (1kbps): 000
                    0x50,           # frequency (425 + CHAN * 0.1M) ~ 0x50: 433M
                    0b01111000      # transparent: 0, internal pull-up: 1, wake-up time: 000, transmit power: 000
                 ]
read_config_cmd = [0xc1, 0xc1, 0xc1]
read_version_cmd = [0xc3, 0xc3, 0xc3]
reset_cmd = [0xc4, 0xc4, 0xc4]

def get_serial_port(location=None):
    default_locations = [
        "/dev/cu.SLAB_USBtoUART",
        "/dev/cu.SLAB_USBtoUART"
    ]
    
    if location == None:
        for loc in default_locations:
            if os.path.exists(loc):
                location = loc
                break
    
    ser = serial.Serial(
        port=location,
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS )
    if ser.isOpen(): 
        return ser
    else: 
        raise RuntimeError("Could not open serial port {}".format(location))
