# EJServo.py
# 11/05/2024
__author__ = "CHaynes"
__version__ = "0.0.1"

import EJServoComms
import time

def StartServo():
    EJServoComms.InitComms()
    EJServoComms.SetPRMode()
    EJServoComms.EnableServo()
    EJServoComms.Jog()

def StopServo():  
    EJServoComms.EStop()
    EJServoComms.DisableServo()
    EJServoComms.CloseComms()


    
