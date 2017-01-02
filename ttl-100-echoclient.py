#!/usr/bin/env python
# echos messages in the form of "echo [msg]\n"

import ttl100, time, sys
port = ttl100.get_serial_port()

def test_echo():
    send_time = time.time()
    print("{}: echo hello".format(send_time))
    port.write("echo hello\n")
    
    while True:
        line = ""
        while len(line) == 0 or line[-1] != "\n":
            line += port.read(1)
        recv_time = time.time()
        sys.stdout.write("{}: {}".format(recv_time, line))
        sys.stdout.flush()
        if line.startswith("ohce "):
            rtt = recv_time-send_time
            print("RTT: {}".format(rtt))
            return rtt
        
rtts = []
for i in range(10):
    rtts.append(test_echo())

print(rtts)