# -*- coding: utf-8 -*-
"""
This is the main program that parses turing programs and executes them on either virtual or physical hardware.

@author: Chad Spensky, Kyania Burke, and Trevon Bennett
"""
filename = "turingFiles/unary_addition.turing"

# Native
import pprint
import sys
import os
import argparse

from tmachine.PhysicalHardware import PhysicalHardware
from tmachine.VirtualHardware import VirtualHardware

def read_turing_program(filename):
    """
        Read in the turing program from a file and return a state machine represented as nested dictionaries.
        
        :param: filename - Filename of turing program 
                           Format: state_name read_val write_val move_dir next_state)
        :return: state machien dictionary
                Format: {sate_name: 
                            {read_val: 
                                {"wv": write_val, 
                                "mv": move_dir, "ns": next_state
                                }
                            }
                        }
        
    """
    # Define our dictionary to fill our state with
    statedict = {}
        
    # read in file, poplating statedict(first dictionary)
    f = open(filename)

    # Read initial tape
    tape_line = f.readline().strip()
    initial_tape = tape_line.split(",")
    # Replace _'s with None
    initial_tape = [None if x=="_" else x for x in initial_tape]

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

    return statedict, initial_tape


def execute_turing_machine(statedict, turing_machine):
    """
        This function will execution the provide states on the provided turing machine, either physical or virtual.
    """
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
            print "ERROR: Found an undefined state (%s)"%current_state
            break

        # Look up function from read value
        if read_val in read_function:
            state_function = read_function[read_val]
        else :
            print "ERROR: Got a read value with no definition. (%s)"%read_val
            break
        
        # Extract our values
        move_dir = state_function["mv"]
        write_val = state_function["wv"]
        next_state = state_function["ns"]
        
        # Print current state info
        print "-"*15 \
            + " State %s / Iteration %s "%(current_state,count) \
            + "-"*15
        print "* Tape position: %s"%turing_machine.position()
        print "* Read: %s"%read_val
        print "--"
        print "** Write: %s"%write_val
        print "** Move: %s"%move_dir
        print "** Transition: %s"%next_state
        print "--"

        # Write our next value
        turing_machine.write(write_val)

        # Move our tape
        if move_dir == "R":
            turing_machine.moveLeft()
        elif move_dir == "L":
            turing_machine.moveRight()

        # Keep output pretty
        print ""

        # Update our state and counter
        current_state = next_state
        count += 1

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("turing_program", help="Filename of the turing machine program to execute. (e.g. turingFiles/unary_addition.turing)")
    parser.add_argument("-s", "--arduino_serial", help="Serial port of the Arduino. (e.g. /dev/tty.usbmodem1d11131)", default=None)
    args = parser.parse_args()
    
    # Read in our state machine
    (statedict, initial_tape) = read_turing_program(args.turing_program)
    
    print "* Sucessfully read in our state machine:"
    pprint.pprint(statedict)
    print "* Initial tape: %s"%initial_tape
    print ""
    
        # Initialize our turing machine
    if args.arduino_serial is not None:
        print "* Connecting to our physical turing machine..."
        turing_machine = PhysicalHardware(serial_name=args.arduino_serial,
                                         init = initial_tape)
    else:
        print "* Initializing a virtual turing machine..."
        turing_machine = VirtualHardware(init = initial_tape)
                                      
    print "* Beginning execution..."
    print ""

    execute_turing_machine(statedict,turing_machine)

    
        
    
        
    


        
    
