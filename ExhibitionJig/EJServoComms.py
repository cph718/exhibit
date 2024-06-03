# EJServoComms.py
# 11/05/2024
# Commission motors before operation with Motion Studio
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
    clientServo.write_register(0x600a, 0x05, slave=1) # Homing Configuration
    clientServo.write_register(0x6002, 0x0020, slave=1) # Homing
    print("Homing Up")

def HomingDown():
    clientServo.write_register(0x600a, 0x04, slave=1) # Homing
    clientServo.write_register(0x6002, 0x0020, slave=1) # Homing
    print("Homing Down")

def NormalVelocityUp():
    packetData = [0x0002, 0x0000, 0x0000, 0xfc18, 0x0062, 0x0060, 0x0000, 0x0010]
    clientServo.write_registers(0x6200, packetData, slave=1)
    print("Normal Velocity Up")

def NormalVelocityDown():
    packetData = [0x0002, 0x0000, 0x0000, 0x03e8, 0x0062, 0x0060, 0x0000, 0x0010]
    clientServo.write_registers(0x6200, packetData, slave=1)
    print("Normal Velocity Down")

def NormalUp(): 
    #Call Path 6
    clientServo.write_register(0x6002, 0x0016, slave=1)
    #Call path2
    #clientServo.write_register(0x6002, 0x0012, slave=1) #Run Path2
    print("Normal Up")

def NormalDown(): #Call path3
    clientServo.write_register(0x6002, 0x0013, slave=1) #Run Path3
    print("Normal Down")

#Configure paths 3 to 6
#Path 2(6210) = Move up to Limit
#Path 3(6218) = Move down to material height
#Path 4(6220) = Move down to bend depth (BDC) with pause
#Path 5(6228) = Move up to material height
#Path 6(6230) = Move up to TDC

#Path 2 
#6210 = Path2 Mode          Bit0-3 MODE 0=Disabled, 1=Position, 2=Velocity, 3=Homing, 4=Stop| Bit4 INS 0=No interrupt, 1=Interrupt
#                           Bit5 OVLP 0=No Overlap, 1=Overlap| Bit6-7 0=Absolute position, 1=Relative to command, 2=Relative to motor,
#                           Bit8-13 0-15 Jump to corresponding path| Bit5 JUMP 0=No Jump, 1=Jump
#6211 = Path2 Position High
#6212 = Path2 Position Low
#6213 = Path2 Speed         Speed in RPM
#6214 = Path 2 Acceleration Acceleration in ms/1000rpm
#6215 = Path 2 Deceleration Deceleration in ms/1000rpm
#6216 = Path 2 Pause Time   Time to pause between Paths in ms
#6217 = Special Parameters  

def SetPaths():
    packetData = [0x0002, 0x0000, 0x0000, 0xff38, 0x0064, 0x0064, 0x0000, 0x0000] #velocity mode
    clientServo.write_registers(0x6210, packetData, slave=1) #Set Path 2
    print("Path 2 Configured")

    packetData = [0x4421, 0xffff, 0x3cb0, 0xfe0c, 0x0064, 0x0064, 0x0000, 0x0000] #Position Mode, Overlap, Absolute position, Jump to 4, Jump (-50000)
    clientServo.write_registers(0x6218, packetData, slave=1) #Set Path 3
    print("Path 3 Configured")

    packetData = [0x4501, 0xffff, 0x15a0, 0xffce, 0x0064, 0x0064, 0x01f4, 0x0000] #Position Mode, Absolute position, Jump to 5, Pause 0.5s, Jump (-60000)
    clientServo.write_registers(0x6220, packetData, slave=1) #Set Path 4
    print("Path 4 Configured")

    packetData = [0x4621, 0xffff, 0x3cb0, 0x0032, 0x0064, 0x0064, 0x0000, 0x0000] #Position Mode, Overlap, Absolute position, Jump to 6, Jump (-50000)
    clientServo.write_registers(0x6228, packetData, slave=1) #Set Path 5
    print("Path 5 Configured")

#TODO need to make this uninteruptible
    packetData = [0x0001, 0x0000, 0x0000, 0x01f4, 0x0064, 0x0064, 0x0000, 0x0000] #Position Mode, Absolute position
    clientServo.write_registers(0x6230, packetData, slave=1) #Set Path 5
    print("Path 6 Configured")