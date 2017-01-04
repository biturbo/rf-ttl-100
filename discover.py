#!/usr/bin/env python

import ttl100, sys, time
port = ttl100.get_serial_port()

i = 0

while True: 
    msg = "{}: {} hello {}\n".format(int(time.time()), ttl100.HOSTNAME, str(i))
    i += 1
    
    port.write(msg)
    sys.stdout.write(msg)
    sys.stdout.flush()
    
    time.sleep(1)