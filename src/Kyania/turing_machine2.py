# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:09:44 2015

@author: Community Outreach
"""

import pprint
filename = "unary_addition.turing.py"
statedict = {}

f = open(filename)

import pprint 
import sys
import os
sys.path.append("../")

from tmachine.VirtualHardware import VirtualHardware
tape = ["_","1","1","_","1","1","1","1","1","1","1","_"]
turing_machine = VirtualHardware(tape_length=50, init = tape)
running = True
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
    readvalue = valuelist[1]
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
#print read_val
    write_val = state_function["write_value"]
    turing_machine.write(write_val)
    move_dir = state_function["move"]
    if move_dir == "R":
        turing_machine.moveLeft()
    else:
        turing_machine.moveRight()
    
    state = state_function["next_state"]
#    print read_val
#    print state_function
#    print state
#   # print turing_machine.position()
    turing_machine.tape()
