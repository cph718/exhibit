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

    #Configure Inputs
    clientServo.write_register(0x0407, 0x27, slave=1) # Homing switch CN1-Pin7-DI4
    #Hardware limit switch positive default state CN1-Pin8-DI5
    #Hardware limit switch negative default state CN1-Pin9-DI6

    #TODO Set software limits, they are enabled once homed
    #clientServo.write_register(0x6006, 0x0, slave=1) Positive SW Limit H
    print("PR Mode")

def ReadServoState():
    ServoState = clientServo.read_holding_registers(0x0b05, 2, slave=1)
    print("Servo state", ServoState.registers[0])
    return ServoState

def EnableServo():
    clientServo.write_register(0x0405, 0x83, slave=1) # Enable Servo Motor
    print("Enable Servo")

def DisableServo():
    clientServo.write_register(0x0405, 0x3, slave=1) # Disable Servo Motor
    print("Disable Servo")

def EStop():
    clientServo.write_register(0x6002, 0x0040, slave=1) # E-Stop
    print("E-Stop")

def HomingUp():
    clientServo.write_register(0x600a, 0x04, slave=1) # Homing Configuration
    clientServo.write_register(0x6002, 0x0020, slave=1) # Homing
    print("Homing Up")

def HomingDown():
    clientServo.write_register(0x600a, 0x05, slave=1) # Homing
    clientServo.write_register(0x6002, 0x0020, slave=1) # Homing
    print("Homing Down")

def NormalUp():
    packetData = [0x0002, 0x0000, 0x0000, 0xfc18, 0x0062, 0x0060, 0x0000, 0x0010]
    clientServo.write_registers(0x6200, packetData, slave=1)
    print("Normal Up")

def NormalDown():
    packetData = [0x0002, 0x0000, 0x0000, 0x03e8, 0x0062, 0x0060, 0x0000, 0x0010]
    clientServo.write_registers(0x6200, packetData, slave=1)
    print("Normal Down")



