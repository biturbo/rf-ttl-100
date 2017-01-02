#!/usr/bin/env python

import serial, time, threading, sys

HOSTNAME = "protina"
RATE_S = 3

ser = serial.Serial("/dev/cu.SLAB_USBtoUART", 9600)
print("Connected to {}".format(ser.name))

i = 0
def schedule_send_hello():
    threading.Timer(RATE_S, schedule_send_hello).start()
    global i
    msg = "{}: hello {} from {}! Es wird kalt....\n".format(int(time.time()), str(i), HOSTNAME)
    i += 1
    ser.write(msg)
    sys.stdout.write(msg)
    sys.stdout.flush()

schedule_send_hello()

recv_lines = []
while True:
    line = ser.readline()
    recv_lines += line
    print(line)
