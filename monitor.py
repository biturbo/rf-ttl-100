#!/usr/bin/env python
import ttl100, sys
port = ttl100.get_serial_port()

data = ""
while True:
    new = port.read(1)
    data += new
    sys.stdout.write(new)
    sys.stdout.flush()