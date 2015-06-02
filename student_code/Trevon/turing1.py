# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:37:20 2015

@author: Div 5 Cyberpatriot
"""
import sys
import os
sys.path.append("../")

from tmachine.VirtualHardware import VirtualHardware
tape = [None,1,1,None,1,1,1,1,1,1,1,None]
turing_machine = VirtualHardware(tape_length=50,init = tape)
running = True
state = 0
while running == True:
    print "state=",state
    print "tape position=",turing_machine.position()
    read_val = turing_machine.read()
    print "read_val=",read_val
    #print turing_machine.position()    
    if state == 0 :
        if read_val == None:
            turing_machine.write(None)
            turing_machine.moveLeft()
        elif read_val == 1:
            turing_machine.write("1")
            turing_machine.moveLeft()
            state = 1
    elif state == 1:
        if read_val == None:
            turing_machine.write(None)
            turing_machine.moveLeft()
            state = 2
        elif read_val == 1:
             turing_machine.write(1)
             turing_machine.moveLeft()
    elif state == 2 :
         if read_val == None:
             turing_machine.write(None)
             turing_machine.moveRight()
             state = 3
         elif read_val == 1:
             turing_machine.write(1)
             turing_machine.moveLeft()
    elif state == 3 :
        if read_val ==None:
            turing_machine.write(None)
            turing_machine.moveRight()
        elif read_val == 1:
            turing_machine.write(1)
            turing_machine.moveRight()
            state = 4
    elif state == 4:
        if read_val == None:
            turing_machine.write(None)
            turing_machine.moveLeft()
            break
        elif read_val ==1:
            turing_machine.write(1)
            turing_machine.moveRight()
print tape
         
            
             
    
     
                
        
        
        
    