# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 15:37:23 2015

@author: Div 5 Cyberpatriot
"""
from Tkinter import *

textOptions = dict(font = ("Helvetica", 16))

class Options:
        def __init__(self, window, parent):
                self.window = window
                self.window.wm_title("Options")
                self.parent = parent                
                
                self.language = StringVar()
                self.language.set("English")
                self.speed = StringVar()
                self.speed.set("Slow")
                
                w = 20
                h = 20

                self.langMenu = OptionMenu(self.window,
                                           self.language,
                                           "English",
                                           "Spanish")

                self.langMenu.config(**textOptions)                             
                self.langMenu.grid(row = 1, column = 1)
                
                self.speedMenu = OptionMenu(self.window,
                                           self.speed,
                                           "Slow",
                                           "Fast",
                                           **textOptions)
                self.speedMenu.grid(row = 1, column = 2)

                
                self.back = Button(self.window,
                                    text = "Back",
                                    height = h,
                                    width = w,
                                    command = self.close,
                                    **textOptions)
                self.back.grid (row = 2, column = 2) 
    
        def close(self):
            self.window.destroy() 
            self.parent.setState(NORMAL)
            self.parent.language = self.language.get()
            self.parent.speed = self.speed.get()
            
            