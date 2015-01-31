#from PIL import Image, ImageTk # broken for some reason on windows box
import Tkinter as tk
import webbrowser

import options_gui
import run_gui

textOptions = dict(font = ("Helvetica", 18),
                   bg = "lightblue")

class GUI:
        def __init__(self,window):
                self.window = window
                self.optionsGUI = None
                self.runGUI = None
                self.language = "English"
                self.speed = "Slow"
                
                w = 22
                h = 7
                self.programs = tk.Button(self.window,
                                             text = "Programs",
                                             height = h,
                                             width = w,
                                             command = self.showRun,
                                             **textOptions)
                self.programs.grid (row = 1, column  = 2) 
                self.about = tk.Button(self.window,
                                    text = "About",
                                    height = h,
                                    width = w,
                                    command = self.showAbout,
                                    **textOptions)
                self.about.grid (row = 2, column = 1)

                self.options = tk.Button(self.window,
                                                 text = "Options",
                                                 height = h,
                                                 width = w,
                                                 command = self.showOptions,
                                                 **textOptions)
                self.options.grid (row = 2, column = 2)
                
                # doesn't work on windows, but seems to have better support on unix
                #image = Image.open("turing.jpg")
                #photo = ImageTk.PhotoImage(image)
                #self.ll = tk.Label(self.window, 
                #                height = h, 
                #                width = w,
                #                image = photo
                #                )
		self.logo = tk.Label(self.window, text = "MIT Lincoln Lab",
				     font = ("Helvetica", 22))
		self.logo.grid(row = 1, column = 1)		

                                          
        def showOptions(self):
            self.setState(tk.DISABLED)
            t = tk.Toplevel(self.window)
            t.minsize(width = 300, height = 150)
            self.optionsGUI = options_gui.Options(t,self)
            t.protocol("WM_DELETE_WINDOW", self.optionsGUI.close)
            t.mainloop()
        
        def showRun(self):
            self.setState(tk.DISABLED)
            t = tk.Toplevel(self.window)
            t.minsize(width = 600, height = 600)
            self.runGUI = run_gui.Run(t,self)
            t.protocol("WM_DELETE_WINDOW", self.runGUI.close)
            t.mainloop()
            
        def output(self):
            print self.language
            print self.speed
        def setState(self, newState):
            self.programs.config(state = newState)
            self.about.config(state = newState)
            self.options.config(state = newState)
            
        def showAbout(self):
            webbrowser.open("turing.html")

            
                                             
window = tk.Tk()

#window.minsize(width =10, height = 1)
window.geometry = ("10x5")
#window.resizable(width=tk.FALSE, height = tk.FALSE)
window.wm_title("Turing Machine")

app = GUI(window)

window.mainloop()

                                             
                  