# PIP install pyserial
# PIP install pybluez
import serial
import serial.tools.list_ports as ls

l = ls.comports()
for p in l:
    print(p)

sock = serial.Serial("COM4")
while(True):
    s = sock.readline()
    print(s.strip().decode())
sock.close()