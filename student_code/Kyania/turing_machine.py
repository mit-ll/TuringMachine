# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:28:35 2015

@author: Community Outreach
"""
import sys
sys.path.append("../")

from tmachine.VirtualHardware import VirtualHardware
tape = [None,1,1, None,1,1,1,1,1,1,1,None]
turing_machine = VirtualHardware(tape_length=1000, init=tape)

running = True
state = 0
while running == True:
    read_val = turing_machine.read()
    print read_val 
    print turing_machine.position()
    if state == 0:
        if read_val == None:
            turing_machine.write(None)
            turing_machine.moveLeft()
            print "nothing"
        elif read_val == 1:
            turing_machine.write(1)
            turing_machine.moveLeft()
            print "1"
            state=1
    elif state == 1:
        if read_val == None:
            turing_machine.write(None)
            turing_machine.moveLeft()
            print "nothing"
            state=2
        elif read_val == 1:
            turing_machine.write(1)
            turing_machine.moveLeft()
            print "1"
    elif state == 2:
        if read_val == None:
            turing_machine.write(None)
            turing_machine.moveRight()
            print "nothing"
            state=3
        elif read_val == 1:
            turing_machine.write(1)
            turing_machine.moveLeft()
            print "1"
    elif state ==3:
        if read_val == None :
            turing_machine.write(None)
            turing_machine.moveRight()
            print "nothing"
        elif read_val == 1:
            turing_machine.write(1)
            turing_machine.moveRight()
            print "1"
            state=4
    elif state ==4:
        if read_val == None:
            turing_machine.write(None)
            turing_machine.moveLeft()
            print "nothing"
            break
        elif read_val == 1:
            turing_machine.write(1)
            turing_machine.moveRight()
            print "1"
print tape
