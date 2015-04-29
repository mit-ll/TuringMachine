from Tkinter import *
import options_gui

class GUI:
        def __init__(self,window):
                self.window = window
                
                w = 8
                h = 4
                self.programs = Button(self.window,
                                             text = "Programs",
                                             height = h,
                                             width = w,)
                self.programs.grid (row = 1, column  = 1) 
                self.about = Button(self.window,
                                    text = "About",
                                    height = h,
                                    width = w,)
                self.about.grid (row = 1, column = 2)
                self.reset = Button(self.window,
                                             text = "Reset",
                                             height = h,
                                             width = w,)
                self.reset.grid (row = 2, column = 1)
                self.options = Button(self.window,
                                                 text = "Options",
                                                 height = h,
                                                 width = w,
                                                 command = self.Options)
                self.options.grid (row = 2, column = 2)
                                          
        def Options(self):
            print "hello"
#            window = Tk()
#            window.geometry = ("800x500")
#            window.wm_title("Turing Machine")

            app = options_gui.Options(window)

            window.mainloop()
        
            
                                             
window = Tk()
window.geometry = ("800x500")
window.wm_title("Turing Machine")

app = GUI(window)

window.mainloop()

                                             
                  