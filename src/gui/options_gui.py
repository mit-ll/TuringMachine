# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 15:37:23 2015

@author: Div 5 Cyberpatriot
"""
from Tkinter import *

textOptions = dict(font = ("Helvetica", 16))
                   


class Options:
        def __init__(self, window, parent):
                h = 2
                w = 10            
            
                self.window = window
                self.window.wm_title("Options")
                self.parent = parent                
                
                self.language = StringVar()
                self.language.set("English")
                self.speed = StringVar()
                self.speed.set("Slow")
                

                self.languageLabel = Label(self.window,
                                           text = "Language",
                                           height = h/2,
                                           width = w,
                                           **textOptions)
                self.languageLabel.grid(row = 1, column = 1)
                
                self.speedLabel = Label(self.window,
                                           text = "Speed",
                                           height = h/2,
                                           width = w,
                                           **textOptions)
                self.speedLabel.grid(row = 1, column = 2)

                self.langMenu = OptionMenu(self.window,
                                           self.language,
                                           "English")

                self.langMenu.config(height = h, width = w, **textOptions)                             
                self.langMenu.grid(row = 2, column = 1)
                
                self.speedMenu = OptionMenu(self.window,
                                           self.speed,
                                           "Slow",
                                           "Fast")
                self.speedMenu.grid(row = 2, column = 2)
                self.speedMenu.config(height = h, width = w, **textOptions)

                
                self.back = Button(self.window,
                                    text = "Back",
                                    command = self.close,
                                    **textOptions)
                self.back.grid (row = 3, column = 1, columnspan = 2)

    
        def close(self):
            self.window.destroy() 
            self.parent.setState(NORMAL)
            self.parent.language = self.language.get()
            self.parent.speed = self.speed.get()
            
            