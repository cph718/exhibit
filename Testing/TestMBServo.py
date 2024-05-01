import serial
import time

# Default Baud rate is 9600 but for some reason it seems to be set to 19200 on startup
ser=serial.Serial(port='/dev/ttyUSB0', baudrate=19200, timeout=2, bytesize=8, parity=serial.PARITY_NONE, stopbits=2) 
print(ser.name)
print("Comms Active: ")

print(ser.isOpen())
sendPacket = "\x01\x06\x62\x00\x00\x02\x17\xB3"
ser.write(sendPacket.encode())
s=ser.readline()
print(s)

sendPacket = "\x01\x06\x62\x03\x02\x58\x66\xE8"
ser.write(sendPacket.encode())
ser.flush()

sendPacket = "\x01\x06\x62\x04\x00\x32\x56\x66"
ser.write(sendPacket.encode())
ser.flush()

sendPacket = "\x01\x06\x62\x05\x00\x32\x07\xA6"
ser.write(sendPacket.encode())
ser.flush()

sendPacket = "\x01\x06\x62\x02\x00\x10\x37\xC6"
ser.write(sendPacket.encode())
ser.flush()

time.sleep(3)

print('closing')
ser.close()