import tkinter as tk
import tkinter.font

win=tk.Tk()
win.title("using tkinter")
myFont=tkinter.font.Font(family = 'helvetica', size = 12, weight = "bold")

def doNothing():
    win.quit()

def exitProgram():
    win.quit()

doButton=tk.Button(win, text = 'snack', font=myFont, command=doNothing, bg='bisque2', height=1, width=24)
doButton.grid(row=0, sticky=tk.NSEW)
exitButton=tk.Button(win, text = 'EXIT', font=myFont, command=exitProgram, bg='cyan', height=1, width=6)
exitButton.grid(row=0, sticky=tk.NSEW)

tk.mainloop()