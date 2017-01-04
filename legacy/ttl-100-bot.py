#!/usr/bin/env python

import serial, time

ser = serial.Serial("/dev/cu.SLAB_USBtoUART")
print("Connected to {}".format(ser.name))

i = 0

while True: 
    msg = "echo {}: hello number {}!".format(int(time.time()), str(i))
    i += 1
    ser.write(msg+"\n")
    print(msg)
    time.sleep(3)