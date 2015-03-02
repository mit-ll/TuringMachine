#!/usr/bin/python
from Tkinter import *

class MyApp:
        def __init__(self,window):
                self.window = window
                
                w = 8
                h = 4
                
                # Contents of main display
                self.text = StringVar()

                # Main display
                self.display = Label(self.window,
                                     textvariable = self.text,
                                     width = 3*w,
                                     height = h,
                                     font = ("Times",14))
                self.display.grid(row = 0, columnspan = 4)

                # Buttons

                self.button1 = Button(self.window,
                                      text = "1",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("1"))
                self.button1.grid(row = 4, column = 0)

                self.button2 = Button(self.window,
                                      text = "2",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("2"))
                self.button2.grid(row = 4, column = 1)

                self.button3 = Button(self.window,
                                      text = "3",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("3"))
                self.button3.grid(row = 4, column = 2)

                self.button4 = Button(self.window,
                                      text = "4",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("4"))
                self.button4.grid(row = 3, column = 0)

                self.button5 = Button(self.window,
                                      text = "5",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("5"))
                self.button5.grid(row = 3, column = 1)

                self.button6 = Button(self.window,
                                      text = "6",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("6"))
                self.button6.grid(row = 3, column = 2)
                
                self.button7 = Button(self.window,
                                      text = "7",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("7"))
                self.button7.grid(row = 2, column = 0)

                self.button8 = Button(self.window,
                                      text = "8",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("8"))
                self.button8.grid(row = 2, column = 1)

                self.button9 = Button(self.window,
                                      text = "9",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("9"))
                self.button9.grid(row = 2, column = 2)

                self.button0 = Button(self.window,
                                      text = "0",
                                      height = h,
                                      width = w,
                                      command = lambda: self.show("0"))
                self.button0.grid(row = 5, column = 0)

                self.plus = Button(self.window,
                                   text = "+",
                                   height = h,
                                   width = w,
                                      command = lambda: self.show(" + "))
                self.plus.grid(row = 5, column = 4)

                self.minus = Button(self.window,
                                    text = "-",
                                    height = h,
                                    width = w,
                                      command = lambda: self.show(" - "))
                self.minus.grid(row = 4, column = 4)

                self.multiply = Button(self.window,
                                    text = "*",
                                    height = h,
                                    width = w,
                                      command = lambda: self.show(" * "))
                self.multiply.grid(row = 3, column = 4)

                self.divide = Button(self.window,
                                    text = "/",
                                    height = h,
                                    width = w,
                                      command = lambda: self.show(" / "))
                self.divide.grid(row = 2, column = 4)

                
                
                self.equals = Button(self.window,
                                     text = "=",
                                     height = h,
                                     width = w,
                                     command = self.calculate)
                self.equals.grid(row = 5, column = 2)

                self.clear = Button(self.window,
                                     text = "C",
                                     height = h,
                                     width = w,
                                    command = self.clearText)
                self.clear.grid(row = 0, column = 4)

                self.decimal = Button(self.window,
                	                  text = ".",
                	                  height = h,
                	                  width = w,
                	                  command = lambda: self.show("."))
                self.decimal.grid(row = 5, column = 1)
                
        def show(self,text):
        	# Adds something to the display
                if "=" in self.text.get():
                        self.clearText()
                self.text.set(self.text.get() + text)
        def clearText(self):
                self.text.set("")
        def calculate(self):
                try:
                        out = eval(self.text.get())
                except:
                        out = "Error"
                self.text.set(self.text.get() + " = " + str(out))
                
                


window = Tk()
window.geometry = ("800x800")
window.wm_title("Python Calculator")

app = MyApp(window)

window.mainloop()
# window.destroy()
