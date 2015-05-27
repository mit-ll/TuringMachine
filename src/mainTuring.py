# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:49:01 2015

@author: Div 5 Cyberpatriot
"""
filename = "turingFiles/unary_addition.turing"

# Native
import pprint
import sys
import os

from tmachine.PhysicalHardware import PhysicalHardware
tape = [None,"1","1",None,"1","1","1","1","1","1","1",None]
turing_machine = PhysicalHardware("/dev/tty.usbmodem1d11131",
                                  init = tape)

# Define our dictionary to fill our state with
statedict = {}
    
# read in file, poplating statedict(first dictionary)
f = open(filename)

# same as if statments, run touring machine
for line in f:
    
    # Read, strip, split line
    value = line.strip()
    valuelist= value.split()
    
    if len(valuelist) != 5:
        print "Error! I don't like this line: %s"%valuelist
        print len(valuelist)
        continue

    # Extract our values
    statename = valuelist[0]
    readvalue = valuelist[1]
    writevalue = valuelist[2]
    movevalue = valuelist[3]
    nextstate = valuelist[4]

    # _ is None to keep our input files clean
    if readvalue == "_":
        readvalue = None
    if writevalue == "_":
        writevalue = None

    statefunction = {"wv":writevalue,
             "mv":movevalue,
             "ns":nextstate}

    # Create a new state if needed
    if statename  not in statedict:
        statedict[statename] = {}

    # Update our dict for state transitions
    readdict = statedict[statename]
    readdict[readvalue]=statefunction

print "* Sucessfully read in our state machine:"
pprint.pprint(statedict)
print ""
print "* Beginning execution..."
print ""

# Start at state 0
current_state = "0"
count = 0
# Loop until we hit the end state
while current_state != "stop":
    
    # Read the current value of the tape
    read_val = turing_machine.read()
    state_function = None
    read_function = None

    # Lookup state in dictionary    
    if current_state in statedict:
        read_function = statedict[current_state]
    else:
        print "ERROR: Found an undefined state (%s)"%state
        break

    # Look up function from read value
    if read_val in read_function:
        state_function = read_function[read_val]
    else :
        print "ERROR: Got a read value with no definition. (%s)"%read_val
        break
    
    # Print current state info
    print "-"*15 \
        + " State %s / Iteration %s "%(statename,count) \
        + "-"*15
    print "* Tape position: %s"%turing_machine.position()
    print "* Read: %s"%read_val
    print "--"
    print "** Write: %s"%state_function['wv']
    print "** Move: %s"%state_function['mv']
    print "** Transition: %s"%state_function['ns']
    print "--"

    # Write our next value
    write_val = state_function["wv"]
    turing_machine.write(write_val)

    # Move our tape
    move_dir = state_function["mv"]
    if move_dir == "R":
        turing_machine.moveLeft()
    else:
        turing_machine.moveRight()

    # Update our state
    next_state = statefunction["ns"]



    print ""

    # Update our state and counter
    current_state = state_function['ns']
    count += 1

    
    
    
    
        
    
        
    


        
    