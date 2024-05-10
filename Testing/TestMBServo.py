#Code to test Servo can be controlled

#import serial
import time
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
)

def run_sync_simple_client():
    client = ModbusClient.ModbusSerialClient(port='/dev/ttyUSB0', framer=Framer.RTU, baudrate=19200, bytesize=8, parity="N", stopbits=2)

    print("connect to server")
    client.connect()

    print("get and verify data")
    try:
        rr = client.read_holding_registers(9, 2, slave=1)
    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
        client.close()
        return
    if rr.isError():
        print(f"Received Modbus library error({rr})")
        client.close()
        return
    if isinstance(rr, ExceptionResponse):
        print(f"Received Modbus library exception ({rr})")
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        client.close()

    client.write_register(0x0003, 0x0, slave=1) # Set to PR Mode
    print("PR Mode")
    client.write_register(0x0405, 0x83, slave=1) # Enable Servo Motor
    print("Enable Servo")

    #Testing Writing Registers
    #rr = client.read_holding_registers(9, 2, slave=1)
    #print(rr.registers)
    #client.write_register(9, 250, slave=1)
    #rr = client.read_holding_registers(9, 2, slave=1)
    #print(rr.registers)
    #rr = client.read_holding_registers(9, 2, slave=1)

    #Test Run Path0.
    #rr = client.read_holding_registers(0x0405, 2, slave=1)
    #print(rr.registers)
    #rr = client.read_holding_registers(0x6002, 2, slave=1)
    #print(rr.registers)
    #client.write_register(0x6002, 0x10, slave=1)
    #rr = client.read_holding_registers(0x6002, 2, slave=1)
    #print(rr.registers)

    #Test Jog Mode
    rr = client.read_holding_registers(0x6200, 16, slave=1)
    print(rr.registers)
    packetData = [0x0002, 0x0000, 0x0000, 0x03e8, 0x0062, 0x0060, 0x0000, 0x0010]
    client.write_registers(0x6200, packetData, slave=1)
    rr = client.read_holding_registers(0x6200, 16, slave=1)
    print(rr.registers)

    #i = 0
    #while i < 10:
    #    client.write_register(0x6207, 0x10, slave=1)
    #    print(i)
    #    i += 1

    time.sleep(10)

    client.write_register(0x6002, 0x0040, slave=1) # E-Stop
    print("E-Stop")

    time.sleep(2)

    client.write_register(0x0405, 0x3, slave=1) # Disable Servo Motor

    print("close connection")
    client.close()

if __name__ == "__main__":
    run_sync_simple_client()

# RS485 Serial through converter.
# SW3 should be on for termination resistor. SW1, 2 and 4 should be off
# Default Baud rate is 9600 but for some reason it seems to be set to 19200 on startup.
#TODO Method to ensure comms port is correct.
#ser=serial.Serial(port='/dev/ttyUSB0', baudrate=19200, timeout=2, bytesize=8, parity=serial.PARITY_NONE, stopbits=2) 
#print(ser.name)
#print("Comms Active: ")
#print(ser.isOpen())

#sendPacket = "\x01\x03\x00\x04\x00\x02\x85\xCA"
#ser.write(sendPacket.encode())
#s=ser.readline()
#print(s)

#sendPacket = "\x01\x06\x62\x00\x00\x02\x17\xb3"
#ser.write(sendPacket.encode())
#s=ser.readline()
#print(s)

#sendPacket = "\x01\x06\x62\x03\x02\x58\x66\xe8"
#ser.write(sendPacket.encode())
#s=ser.readline()
#print(s)

#sendPacket = "\x01\x06\x62\x04\x00\x32\x56\x66"
#ser.write(sendPacket.encode())
#s=ser.readline()
#print(s)

#sendPacket = "\x01\x06\x62\x05\x00\x32\x07\xa6"
#ser.write(sendPacket.encode())
#s=ser.readline()
#print(s)

#sendPacket = "\x01\x06\x62\x02\x00\x10\x37\xc6"
#ser.write(sendPacket.encode())
#s=ser.readline()
#print(s)

#time.sleep(3)

#print('closing')
#ser.close()