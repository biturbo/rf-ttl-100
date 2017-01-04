#!/usr/bin/env python
import ttl100, sys
port = ttl100.get_serial_port()

port.write(sys.argv[1])