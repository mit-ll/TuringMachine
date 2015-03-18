#!/usr/bin/python
"""
Inputs a number from the user, and prints it to the turing machine using only turing 
state transition rules. 
"""
__author__ = "Kyania Burke and Trevon Bennett"

#  defines what a turing machine is
from tmachine.VirtualHardware import VirtualHardware
#creates virtual turing machine, including how long the tape of machine is
turing_machine = VirtualHardware(tape_length=100)


# asks for input
state = raw_input("enter # ")
#says input given will always be a number
state = int(state)

#converts integer given to binary number
state = bin(state)
#from second on, to remove 0,b from binary tape
state = state[2:]
#as long as there are still more digits in binary number...
while state !="":

    print state # write binary number
    turing_machine.moveLeft()#move virtual tape left once(default is once, can be specified)
    turing_machine.write(state[0])#write first digit of binary code
    state = state[1:]#redueces state to what ever's left in binary code
# show turing tape w
turing_machine.tape()

    

    

