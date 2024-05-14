# EJServo.py
# 11/05/2024
__author__ = "CHaynes"
__version__ = "0.0.1"

import EJServoComms
import time

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

#Homing > Software does a double step homing process for accuracy
def HomingUpServo():  
    EJServoComms.HomingUp()

def HomingDownServo():  
    EJServoComms.HomingDown()

def TestServoJog():  
    EJServoComms.Jog()




#TODO see page 91 for polling position
    
