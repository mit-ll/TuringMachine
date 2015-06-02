from Tkinter import *
import options_gui

textOptions = dict(font = ("Helvetica", 16))

class GUI:
        def __init__(self,window):
                self.window = window
                self.optionsGUI = None
                self.language = "English"
                self.speed = "Slow"
                
                w = 50
                h =15
                self.programs = Button(self.window,
                                             text = "Programs",
                                             height = h,
                                             width = w,
                                             **textOptions)
                self.programs.grid (row = 1, column  = 1) 
                self.about = Button(self.window,
                                    text = "About",
                                    height = h,
                                    width = w,
                                    **textOptions)
                self.about.grid (row = 1, column = 2)
                self.reset = Button(self.window,
                                             text = "Reset",
                                             height = h,
                                             width = w,
                                             command = self.output,
                                             **textOptions)
                self.reset.grid (row = 2, column = 1)
                self.options = Button(self.window,
                                                 text = "Options",
                                                 height = h,
                                                 width = w,
                                                 command = self.showOptions,
                                                 **textOptions)
                self.options.grid (row = 2, column = 2)
                                          
        def showOptions(self):
            self.setState(DISABLED)
            t = Toplevel(self.window)
            t.minsize(width = 300, height = 300)
            self.optionsGUI = options_gui.Options(t,self)
            t.protocol("WM_DELETE_WINDOW", self.optionsGUI.close)
            t.mainloop()
            
            
        def output(self):
            print self.language
            print self.speed
        def setState(self, newState):
            self.programs.config(state = newState)
            self.about.config(state = newState)
            self.reset.config(state = newState)
            self.options.config(state = newState)
            
        
            
                                             
window = Tk()
window.resizable(width=FALSE, height = FALSE)
window.minsize(width = 600, height = 600)
#window.geometry = ("2500x1600")
window.wm_title("Turing Machine")

app = GUI(window)

window.mainloop()

                                             
                  