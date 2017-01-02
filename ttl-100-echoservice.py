#!/usr/bin/env python
# echos messages in the form of "echo [msg]\n"

import ttl100, time, sys
port = ttl100.get_serial_port()

time.sleep(1)
while True:
    line = ""
    while len(line) == 0 or line[-1] != "\n":
        line += port.read(1)
    sys.stdout.write(line)
    sys.stdout.flush()
    
    if line.startswith("echo "):
        ohce = "ohce "+line[5:]
        port.write(ohce)
        sys.stdout.write(ohce)
        sys.stdout.flush()
        