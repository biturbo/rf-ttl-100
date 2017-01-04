#!/usr/bin/env python
# echos messages in the form of "echo [msg]\n"

import ttl100, time, sys
port = ttl100.get_serial_port()

def test_echo():
    send_time = time.time()
    print("{}: echo hello".format(send_time))
    port.write("echo hello\n")
    
    line = ""
    timout = 3.0
    while (len(line) == 0 or line[-1] != "\n") and timout > 0:
        line += port.read(1)
        timout -= 1.0
    if line == "": return 0
    recv_time = time.time()
    sys.stdout.write("{}: {}".format(recv_time, line))
    sys.stdout.flush()
    if line.startswith("ohce "):
        rtt = recv_time-send_time
        print("RTT: {}\n".format(rtt))
        return rtt
        
rtts = []
for i in range(10000):
    rtts.append(test_echo())

print(rtts)