# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 15:37:23 2015

@author: Div 5 Cyberpatriot
"""
import o_my_gui
from Tkinter import *

class Options:
        def __init__(self,window):
                self.window = window
                
                w = 8
                h = 4
                self.programs = Button(self.window,
                                             text = "Language",
                                             height = h,
                                             width = w,)
                self.programs.grid (row = 1, column  = 1) 
                self.about = Button(self.window,
                                    text = "Speed",
                                    height = h,
                                    width = w,)
                self.about.grid (row = 1, column = 2)
                self.back = Button(self.window,
                                    text = "Back",
                                    height = h,
                                    width = w,
                                    command = self.main )
                self.back.grid (row = 2, column = 2) 
    
        def main(self):
            self.window.destroy()
            window = Tk()
            window.geometry = ("800x500")
            window.wm_title("Turing Machine")
            app = o_my_gui.GUI(window)
            window.mainloop()
            
            
            
            

#window = Tk()
#window.geometry = ("800x500")
#window.wm_title("Turing Machine")
#
#app = MyApp(window)
#
#window.mainloop()

#                