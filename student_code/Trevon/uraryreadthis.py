# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:50:48 2015

@author: Div 5 Cyberpatriot
"""
import pprint
filename = "unary addition.turing.py"

statedict = {}
    

f = open(filename)

for line in f:
    value = line.strip()
    valuelist= value.split()
    if len(valuelist) != 5:
        print "can't use line. Error!"
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
        
        
    
    
    

            
f.close
pprint.pprint(statedict)    
    