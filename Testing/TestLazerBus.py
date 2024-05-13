import serial

print("connect to Lazer Bus")
ser=serial.Serial(port='/dev/ttyUSB0', baudrate=19200, timeout=2, bytesize=8, parity=serial.PARITY_NONE, stopbits=1)
print(ser.name)

#packet = bytearray()
#packet.append(0x01)
#packet.append(0x00)
#packet.append(0x00)
#packet.append(0x00)
#packet.append(0x00)
#packet.append(0x00)
#packet.append(0x00)
#packet.append(0x00)
#packet.append(0x00)
#packet.append(0x00)
#packet.append(0x00)
#packet.append(0xFE)
#print(packet)

command = b'\x01\x000000\x000000\x000000\x00\xfe'
print(command)

ser.write(command)
ser.flush()
s=ser.read().hex()
print(s)


print('closing')
ser.close()