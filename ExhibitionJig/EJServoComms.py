# EJServoComms.py
# 11/05/2024
__author__ = "CHaynes"
__version__ = "0.0.1"

#import serial
import time
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
)

clientServo = None

def InitComms():
    global clientServo
    clientServo = ModbusClient.ModbusSerialClient(port='/dev/ttyUSB0', framer=Framer.RTU, baudrate=19200, bytesize=8, parity="N", stopbits=2)

    print("connect to server")
    clientServo.connect()

    print("get and verify data")
    try:
        rr = clientServo.read_holding_registers(9, 2, slave=1)
    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
        clientServo.close()
        return
    if rr.isError():
        print(f"Received Modbus library error({rr})")
        clientServo.close()
        return
    if isinstance(rr, ExceptionResponse):
        print(f"Received Modbus library exception ({rr})")
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        clientServo.close()
    print("Servo communications enabled")

def CloseComms():
    clientServo.close()
    print("Servo communications disabled")

def SetPRMode():
    clientServo.write_register(0x0003, 0x0, slave=1) # Set to PR Mode
    print("PR Mode")

def EnableServo():
    clientServo.write_register(0x0405, 0x83, slave=1) # Enable Servo Motor
    print("Enable Servo")

def DisableServo():
    clientServo.write_register(0x0405, 0x3, slave=1) # Disable Servo Motor
    print("Disable Servo")

def EStop():
    clientServo.write_register(0x6002, 0x0040, slave=1) # E-Stop
    print("E-Stop")

    #Jog Mode
def Jog():
    packetData = [0x0002, 0x0000, 0x0000, 0x03e8, 0x0062, 0x0060, 0x0000, 0x0010]
    clientServo.write_registers(0x6200, packetData, slave=1)

