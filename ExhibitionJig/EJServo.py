# EJServo.py
# 11/05/2024
__author__ = "CHaynes"
__version__ = "0.0.1"

import EJServoComms
from enum import Enum
import time

class pressMode(Enum):
    notReferenced = 1
    referenced = 2

currPressMode = pressMode.notReferenced

def InitServo():
    EJServoComms.InitComms()
    EJServoComms.SetPRMode()
    EJServoComms.EnableServo()

def DeinitServo():
    EJServoComms.EStop()
    EJServoComms.DisableServo()
    EJServoComms.CloseComms()

def StopServo(): 
    EJServoComms.EStop()
    CheckServoStatus()

def CheckServoStatus():
    global currPressMode
    #Status Bit0:ServoReady, Bit1:ServoRun, Bit2:Err, Bit3:HomeOK, Bit4:PositionComplete, Bit5:AtSpeed
    status = EJServoComms.ReadServoState()

    if((status.registers[0]&0x08)):
        currPressMode = pressMode.referenced
        print('referenced')

def MoveUp():
    global currPressMode

    if(currPressMode == pressMode.notReferenced):
        EJServoComms.HomingUp()
    elif(currPressMode == pressMode.referenced):
        EJServoComms.NormalUp()

def MoveDown():
    global currPressMode

    if(currPressMode == pressMode.notReferenced):
        EJServoComms.HomingDown()
    elif(currPressMode == pressMode.referenced):
        EJServoComms.NormalDown()

#Homing > Software does a double step homing process for accuracy
#If a limit switch is hit while homing the direction changes


def TestServoJog():  
    EJServoComms.Jog()




#TODO see page 91 for polling position
#TODO see page 54-55 for reading position etc
    
