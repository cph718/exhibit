# EJGUI.py
# 11/05/2024
__author__ = "CHaynes"
__version__ = "0.0.1"

import tkinter as tk
import tkinter.font
import EJServo
from enum import Enum

class pressMode(Enum):
    normalMode = 1
    enduranceMode = 2

win = None
currPressMode = pressMode.normalMode

def StartMotor():
    EJServo.StartServo()

def StopMotor():
    EJServo.StopServo()

def Exit():
    win.quit()

def StartGUI():
    global win
    win=tk.Tk()
    win.title("LS Exhibition Press Controller")
    myFont=tkinter.font.Font(family = 'helvetica', size = 16, weight = "bold")

    operationFrame=tk.Frame(master=win, relief=tk.GROOVE, borderwidth=5)
    operationFrame.pack(fill=tk.Y, side=tk.LEFT)
    operationLabel=tk.Label(master=operationFrame, text="Operating Mode")
    operationLabel.pack()

    normalModeButton=tk.Button(master=operationFrame, text = 'Normal Mode', font=myFont, command=StartMotor, bg='bisque2', height=2, width=16)
    normalModeButton.pack()

    enduranceModeButton=tk.Button(master=operationFrame, text = 'Endurance Mode', font=myFont, command=StartMotor, bg='bisque2', height=2, width=16)
    enduranceModeButton.pack()


    pressControlFrame=tk.Frame(master=win, relief=tk.GROOVE, borderwidth=5)
    pressControlFrame.pack(fill=tk.Y, side=tk.LEFT)
    pressControlLabel=tk.Label(master=pressControlFrame, text="Press Control")
    pressControlLabel.pack()

    moveUpButton=tk.Button(master=pressControlFrame, text = 'Move Up', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    moveUpButton.pack()

    moveDownButton=tk.Button(master=pressControlFrame, text = 'Move Down', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    moveDownButton.pack()

    moveDownButton=tk.Button(master=pressControlFrame, text = 'E-Stop', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    moveDownButton.pack()

    moveDownButton=tk.Button(master=pressControlFrame, text = 'Reset Warning', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    moveDownButton.pack()


    utilityFrame=tk.Frame(master=win, relief=tk.GROOVE, borderwidth=5)
    utilityFrame.pack(fill=tk.Y, side=tk.LEFT)
    utilityLabel=tk.Label(master=utilityFrame, text="Utilities")
    utilityLabel.pack()

    moveUpButton=tk.Button(master=utilityFrame, text = 'Home Bracket', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    moveUpButton.pack()

    moveUpButton=tk.Button(master=utilityFrame, text = 'Bracket Up', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    moveUpButton.pack()

    moveUpButton=tk.Button(master=utilityFrame, text = 'Bracket Down', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    moveUpButton.pack()

    moveUpButton=tk.Button(master=utilityFrame, text = 'Tooltip Hunt', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    moveUpButton.pack()

    tk.mainloop()