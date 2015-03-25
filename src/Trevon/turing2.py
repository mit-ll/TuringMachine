# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:49:01 2015

@author: Div 5 Cyberpatriot
"""
filename = "unary addition.turing.py"

statedict = {}
    

f = open(filename)

for line in f:
    value = line.strip()
    valuelist= value.split()

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

from tmachine.VirtualHardware import VirtualHardware
tape = [None,1,1,None,1,1,1,1,1,1,1,None]
turing_machine = VirtualHardware(tape_length=50,init = tape)
running = True
state = 0
#while running == True:
    print "state=",state
    print "tape position=",turing_machine.position()
    read_val = turing_machine.read()
    print "read_val=",read_val
    print turing_machine.position() 
   
while statename != stop:
    statefunction=statedict[state][read_val]
    
pprint     
        
    