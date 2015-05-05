# -*- coding: utf-8 -*-
"""
Created on Tue May 05 12:57:46 2015

@author: John
"""

from Tkinter import *
import tmachine.VirtualHardware as hw
from os import listdir


textOptions = dict(font = ("Helvetica", 16))

class Run:
    def __init__(self, window, parent):
        self.window = window
        self.parent = parent
        self.speed = self.parent.speed
        self.window.wm_title("Run Turing Program")
        
        files = []
        for f in listdir("turingFiles"):
            if ".turing" in f:
                files.append(f)
        
        self.available = files
        
        self.availableLabel = Label(self.window, text = "Program to Run:", **textOptions)
        self.availableLabel.grid(row = 1, column = 1)
        
        self.program = StringVar()
        self.availableMenu = OptionMenu(self.window, self.program, *self.available)
        self.availableMenu.grid(row = 1, column = 2)
        self.availableMenu.config(width = 20)
        
        self.stateLabel = Label(self.window, text = "State:", **textOptions)
        self.stateLabel.grid(row = 2, column = 1)
        self.state = StringVar()
        self.state.set("Start")
        self.stateDisplay = Label(self.window, textvariable = self.state)
        self.stateDisplay.config(**textOptions)
        self.stateDisplay.grid(row = 2, column = 2)
        
        
    def close(self):
        self.window.destroy() 
        self.parent.setState(NORMAL)