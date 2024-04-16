import serial

ser=serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=2, bytesize=8, parity=serial.PARITY_NONE, stopbits=1)
print(ser.name)
ser.write(b'a\r')
ser.flush()
s=ser.readline()
print(s)
s=ser.readline()
print(s)
s=ser.readline()
print(s)
print('closing')
ser.close()