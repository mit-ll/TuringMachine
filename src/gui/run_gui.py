# -*- coding: utf-8 -*-
"""
Created on Tue May 05 12:57:46 2015

@author: John
"""

import Tkinter as tk
import tmachine.VirtualHardware as hw
from os import listdir
import time


textOptions = dict(font = ("Helvetica", 16))

class Run:
    def __init__(self, window, parent):
        self.window = window
        self.parent = parent
        self.speed = self.parent.speed
        self.window.wm_title("Run Turing Program")
        self.dead = False
        
        # Determine programs available to us
        files = []
        for f in listdir("turingFiles"):
            if ".turing" in f:
                files.append(f)
        
        self.available = files
        
        # Display avaiable files
        self.availableLabel = tk.Label(self.window, text = "Program to Run:", **textOptions)
        self.availableLabel.grid(row = 1, column = 1, columnspan = 2)
        
        self.program = tk.StringVar()
        self.program.set(self.available[0])
        self.availableMenu = tk.OptionMenu(self.window, self.program, *self.available)
        self.availableMenu.grid(row = 1, column = 3, columnspan = 2)
        self.availableMenu.config(width = 20)
        
        # State tracking and display 
        self.stateLabel = tk.Label(self.window, text = "State:", **textOptions)
        self.stateLabel.grid(row = 2, column = 1)
        self.state = tk.StringVar()
        self.state.set("NULL")
        self.stateDisplay = tk.Label(self.window, textvariable = self.state)
        self.stateDisplay.config(bg = "grey", **textOptions)
        self.stateDisplay.grid(row = 2, column = 2)
        
        # Display of number of steps
        self.numStepsLabel = tk.Label(self.window, 
                                      text = "Step Number:",
                                      **textOptions)
        self.numStepsLabel.grid(row = 2, column = 3)
        self.numSteps = tk.StringVar()
        self.numSteps.set("0")
        self.numStepsDisplay = tk.Label(self.window,
                                        textvariable = self.numSteps,
                                        bg = "grey",
                                        **textOptions)
        self.numStepsDisplay.grid(row = 2, column = 4)
        
        # Run
        self.runButton = tk.Button(self.window,
                                   text = "Run!",
                                   command = self.run,
                                   width = 5,
                                   height = 1,
                                   **textOptions)
        self.runButton.grid(column = 5, row = 1, columnspan = 2, rowspan = 2)
        
        self.display = tk.Text(self.window)
        self.display.grid(row = 3, column = 1, rowspan = 2, columnspan = 5)
        
        self.exit = tk.Button(self.window,
                              text = "Exit",
                              width = 5, 
                              height = 1,
                              command = self.close,
                              **textOptions)
        self.exit.grid(row = 9, column = 5, columnspan = 2, rowspan = 2)
        
        
    def close(self):
        self.window.destroy() 
        self.parent.setState(tk.NORMAL)
        self.dead = True
    def run(self):
        
        # Reset from previous run
        self.numSteps.set("0")
        self.state.set("NULL")
        self.display.delete(1.0, tk.END)
        self.window.update()
        self.runButton.config(state = tk.DISABLED)
        
        filename = "turingFiles/" + self.program.get()
        
        f = open(filename)
        statedict = {}
        tape = ["_","1","1","_","1","1","1","1","1","1","1","_"]
        turing_machine = hw.VirtualHardware(tape_length = 50, init = tape)
        state = 0
        
        
        #Read in the file 
        for line in f:
            value = line.strip()
            valuelist = value.split()
            if len(valuelist) != 5:
                print "can't use line, ERROR!"
                print len(valuelist)
                continue 
            
            
            statename = valuelist[0]
#            readvalue = valuelist[1]
            statefunction = {"write_value":valuelist[2],
                      "move":valuelist[3],
                      "next_state":valuelist[4],}
                      
            if statename not in statedict:
                statedict[valuelist[0]] = {}
                
            readdict = statedict [valuelist[0]]
            readdict[valuelist[1]]=statefunction
            
            
        read_val = turing_machine.read()
        print read_val
        
        state = "0"
        while state != "stop":
            time.sleep(1)
            read_val = turing_machine.read()
            state_function = None
            read_function = None
            
            if state in statedict:
                read_function = statedict[state]
            else:
                print "ERROR: Found an undefind state (%s)" %state
            #Look up function from read value
            if read_val in read_function:
                state_function = read_function[read_val]
            else:
                print "ERROR: Got a read value with no definition. (%s)"%read_val
                break
            write_val = state_function["write_value"]
            turing_machine.write(write_val)
            move_dir = state_function["move"]
            if move_dir == "R":
                turing_machine.moveLeft()
            else:
                turing_machine.moveRight()
            
            oldState = state
            state = state_function["next_state"]
            self.state.set(state)
            self.numSteps.set(str(int(self.numSteps.get()) + 1))
            
            self.display.tag_config("highlight", foreground="blue")
            self.display.tag_config("normal", foreground = "black")
            
            self.display.mark_set("matchStart", "1.0")
            self.display.mark_set("matchEnd","end")            
            
            self.display.tag_add("normal", "matchStart", "matchEnd")
            
            self.display.insert(tk.END,"State: " + oldState + " Read: " + read_val + " -> Next State: " + state + " Moving: " + move_dir + "\n", "highlight")
            
            if state == "stop":
                self.display.tag_config("done",foreground = "darkgreen")
                self.display.insert(tk.END,"COMPLETE.\n", "done")            
            
            self.window.update()

            turing_machine.tape()
            
            # Detect stop
            if self.dead:
                break
        self.runButton.config(state = tk.NORMAL)
