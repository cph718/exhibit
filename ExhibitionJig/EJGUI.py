# EJGUI.py
# 11/05/2024
__author__ = "CHaynes"
__version__ = "0.0.1"

import tkinter as tk
import tkinter.font
import EJServo

win = None

def StopMotor():
    EJServo.StopServo()

def ReleaseMotor(event):
    EJServo.StopServo()

def ResetWarning():
    EJServo.StopServo()

def MoveUp(event):
    EJServo.MoveUp()

def MoveDown(event):
    EJServo.MoveDown()

def Exit():
    EJServo.DeinitServo()
    #win.quit() #doesn't close window, need to figure it out

def StartGUI():
    global win
    win=tk.Tk()
    win.title("LS Exhibition Press Controller")
    myFont=tkinter.font.Font(family = 'helvetica', size = 16, weight = "bold")

    operationFrame=tk.Frame(master=win, relief=tk.GROOVE, borderwidth=5)
    operationFrame.pack(fill=tk.Y, side=tk.LEFT)
    operationLabel=tk.Label(master=operationFrame, text="Operating Mode")
    operationLabel.pack()

    normalModeButton=tk.Button(master=operationFrame, text = 'Normal Mode', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    normalModeButton["state"] = "disabled"
    normalModeButton.pack()

    enduranceModeButton=tk.Button(master=operationFrame, text = 'Endurance Mode', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    enduranceModeButton["state"] = "disabled"
    enduranceModeButton.pack()

    exitButton=tk.Button(master=operationFrame, text = 'Exit', font=myFont, command=Exit, bg='bisque2', height=2, width=16)
    exitButton.pack()


    pressControlFrame=tk.Frame(master=win, relief=tk.GROOVE, borderwidth=5)
    pressControlFrame.pack(fill=tk.Y, side=tk.LEFT)
    pressControlLabel=tk.Label(master=pressControlFrame, text="Press Control")
    pressControlLabel.pack()

    moveUpButton=tk.Button(master=pressControlFrame, text = 'Move Up', font=myFont, bg='bisque2', height=2, width=16)
    moveUpButton.pack()
    moveUpButton.bind('<ButtonPress>', MoveUp)
    moveUpButton.bind('<ButtonRelease>', ReleaseMotor)

    moveDownButton=tk.Button(master=pressControlFrame, text = 'Move Down', font=myFont, bg='bisque2', height=2, width=16)
    moveDownButton.pack()
    moveDownButton.bind('<ButtonPress>', MoveDown)
    moveDownButton.bind('<ButtonRelease>', ReleaseMotor)

    moveDownButton=tk.Button(master=pressControlFrame, text = 'E-Stop', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    moveDownButton.pack()

    moveDownButton=tk.Button(master=pressControlFrame, text = 'Reset Warning', font=myFont, command=ResetWarning, bg='bisque2', height=2, width=16)
    moveDownButton.pack()


    utilityFrame=tk.Frame(master=win, relief=tk.GROOVE, borderwidth=5)
    utilityFrame.pack(fill=tk.Y, side=tk.LEFT)
    utilityLabel=tk.Label(master=utilityFrame, text="Utilities")
    utilityLabel.pack()

    bracketHomeButton=tk.Button(master=utilityFrame, text = 'Home Bracket', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    bracketHomeButton["state"] = "disabled"
    bracketHomeButton.pack()

    bracketUpButton=tk.Button(master=utilityFrame, text = 'Bracket Up', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    bracketUpButton["state"] = "disabled"
    bracketUpButton.pack()

    bracketDownButton=tk.Button(master=utilityFrame, text = 'Bracket Down', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    bracketDownButton["state"] = "disabled"
    bracketDownButton.pack()

    bracketTTButton=tk.Button(master=utilityFrame, text = 'Tooltip Hunt', font=myFont, command=StopMotor, bg='bisque2', height=2, width=16)
    bracketTTButton["state"] = "disabled"
    bracketTTButton.pack()

    tk.mainloop()