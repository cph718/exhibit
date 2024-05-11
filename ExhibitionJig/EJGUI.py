# EJGUI.py
# 11/05/2024
__author__ = "CHaynes"
__version__ = "0.0.1"

import tkinter as tk
import tkinter.font
import EJServo

win = None

def StartMotor():
    EJServo.StartServo()

def StopMotor():
    EJServo.StopServo()

def Exit():
    win.quit()

def StartGUI():
    global win
    win=tk.Tk()
    win.title("using tkinter")
    myFont=tkinter.font.Font(family = 'helvetica', size = 12, weight = "bold")

    startButton=tk.Button(win, text = 'Start Motor', font=myFont, command=StartMotor, bg='bisque2', height=1, width=24)
    startButton.grid(row=0, sticky=tk.NSEW)
    stopButton=tk.Button(win, text = 'Stop Motor', font=myFont, command=StopMotor, bg='bisque2', height=1, width=24)
    stopButton.grid(row=2, sticky=tk.NSEW)
    exitButton=tk.Button(win, text = 'EXIT', font=myFont, command=Exit, bg='cyan', height=1, width=6)
    exitButton.grid(row=4, sticky=tk.NSEW)

    tk.mainloop()