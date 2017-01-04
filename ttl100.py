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
speedy_config =  [  0xc0,           # configure mode - 0xc0: persistent; 0xc2 non-persistent
                    0xFF,           # address high (broadcast)
                    0xFF,           # address low (broadcast)
                    0b00111111,     # parity (8N1): 00, baud rate (115200 bps): 111, air data rate (25kbps): 111
                    0x60,           # frequency (425 + CHAN * 0.1M) ~ 0x50: 433M
                    0b00000000      # transparent: 0, internal pull-up: 0, wake-up time: 000, transmit power: 000
                 ]
read_config_cmd = [0xc1, 0xc1, 0xc1]
read_version_cmd = [0xc3, 0xc3, 0xc3]
reset_cmd = [0xc4, 0xc4, 0xc4]

def get_serial_port(location=None, baudrate=115200):
    default_locations = [
        "/dev/ttyUSB0",
        "/dev/cu.SLAB_USBtoUART"
    ]
    
    if location == None:
        for loc in default_locations:
            if os.path.exists(loc):
                location = loc
                break
    
    ser = serial.Serial(
        port=location,
        baudrate=baudrate,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS )
    if ser.isOpen(): 
        return ser
    else: 
        raise RuntimeError("Could not open serial port {}".format(location))

if __name__ == "__main__":
    port = get_serial_port(baudrate=9600)
    print("Programming speedy config...")
    port.write(speedy_config)
    config = port.read(6)
    from hexdump import hexdump
    hexdump(config)