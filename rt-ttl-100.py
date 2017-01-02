#!/usr/bin/env python

import serial

ser = serial.Serial('/dev/cu.SLAB_USBtoUART')
print("Connected to {}".format(ser.name))

config = [  0xc0,           # configure mode - 0xc0: persistent; 0xc2 non-persistent
            0xFF,           # address high
            0xFF,           # address low
            0b00011000,     # parity (8N1): 00, baud rate (9600 bps): 011, air data rate (1kbps): 000
            0x50,           # frequency (425 + CHAN * 0.1M) ~ 0x50: 433M
            0b01111000      # transparent: 0, internal pull-up: 1, wake-up time: 000, transmit power: 000
            ]
read_config_cmd = [0xc1, 0xc1, 0xc1]
read_version_cmd = [0xc3, 0xc3, 0xc3]
reset_cmd = [0xc4, 0xc4, 0xc4]

ser.write(read_config_cmd)
config_read = ser.read(6)

print(", ".join("{:02x}".format(ord(c)) for c in config_read))

ser.close()