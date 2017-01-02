import time, serial, sys

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port="/dev/cu.SLAB_USBtoUART",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

time.sleep(1)
while True:
    line = ""
    while line[-1] != "\n":
        line += ser.readline()
    sys.stdout.write(out)
    sys.stdout.flush()