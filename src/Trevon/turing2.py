# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:49:01 2015

@author: Div 5 Cyberpatriot
"""
filename = "unary addition.turing.py"

from tmachine.VirtualHardware import VirtualHardware
tape = ["_","1","1","_","1","1","1","1","1","1","1","_"]
turing_machine = VirtualHardware(tape_length=50,init = tape)

running = True
state = 0
turin

statedict = {}
    
#read in file, poplating statedict(first dictionary)
f = open(filename)
#same as if statments, run touring machine
for line in f:
    value = line.strip()
    valuelist= value.split()
    if len(valuelist) != 5:
        print "Error! I don't like this line"
        print len(valuelist)
        continue

    statename = valuelist[0]
    readvalue = valuelist[1]
    statefunction = {"wv":valuelist[2],
             "mv":valuelist[3],
             "ns":valuelist[4],}
             
    if statename  not in statedict:
        statedict[valuelist[0]] = {}
    
    readdict = statedict[valuelist[0]]
    readdict[valuelist[1]]=statefunction

import pprint
import sys
import os
sys.path.append("../")


    #while running == True:


print read_val

state = "0"
while statename != "stop":
    read_val = turing_machine.read()
    state_function = None
    read_function = None

    # Lookup state in dictionary    
    if state in statedict:
        read_function = statedict[state]
    else:
        print "ERROR: Found an undefined state (%s)"%state
        break
    # Look up function from read value
    if read_val in read_function:
        state_function = read_function[read_val]
    else :
        print "ERROR: Got a read value with no definition. (%s)"%read_val
        break
    
#print read_val
    write_val = state_function["wv"]
    turing_machine.write(write_val)
    move_dir = state_function["mv"]
    if move_dir == "R":
        turing_machine.moveLeft()
    else:
        turing_machine.moveRight()
    next_state =statefunction["ns"]
    print read_val
    print state_function
    print statename
    print turing_machine.position()
    
    
    
    
    
        
    
        
    


        
    