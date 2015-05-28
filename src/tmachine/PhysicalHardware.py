from AbstractHardware import *

import serial
import time

WRITE_ONE = "1"
WRITE_ZERO = "0"
ERASE = "D"
MOVE_LEFT = "l"
MOVE_RIGHT = "r"

class PhysicalHardware(AbstractHardware):
    """ Software-implemented Turing machine hardware

    Used for general testing of Turing machine logic and interface """

    def __init__(self, **kwargs):
        """ Creates the virtual hardware. 

        Keyword arguments:
         + tape_length = 1000    <- Length of tape in units
         + init        = []      <- starting data of tape (calls initialize)
         """

        self.__serial = serial.Serial(kwargs["serial_name"], 9600, timeout=1)
        time.sleep(2)
            
        self.__tape_length = 1000
        if "tape_length" in kwargs.keys():
            self.__tape_length = kwargs["tape_length"]

        self.__tape = [None] * self.__tape_length

        self.__position = self.__tape_length / 2 # int division

        if "init" in kwargs.keys():
            self.initialize(kwargs["init"])

    def _send_command(self, command):
        
        print "*** Sending command (%s) to Arduino..."%command
        self.__serial.write(command)
        self.__serial.write("\n")
        self.__serial.flush()
        
        rtn = self.__serial.readline()
        rtn = rtn.strip()
        
        while rtn != "done\r\n":
            rtn = self.__serial.readline()
            continue

        return True
    
    def moveLeft(self):
        """ moves the tape x units to the left """
        newPos = self.__position + 1
        if newPos >= self.__tape_length:
            raise Exception("Out of (Virtual) Tape!")
        else:
            self._send_command(MOVE_LEFT)
            self.__position = newPos

    def moveRight(self):
        """ moves the tape x units to the left """
        newPos = self.__position - 1
        if newPos < 0:
            raise Exception("Out of (Virtual) Tape!")
        else:
            self._send_command(MOVE_RIGHT)
            self.__position = newPos
    
    def write(self,value):
        """ Writes value to current position in tape"""
        
        if value != self.__tape[self.__position]:
            self.__tape[self.__position] = value
            
            # Erase whatever is already there
            if self.__tape[self.__position] != None:
                self._send_command(ERASE)

            # Write our new value
            if value == "1":
                self._send_command(WRITE_ONE)
            elif value == "0":
                self._send_command(WRITE_ZERO)
            elif value == None:
                print "* Write None. Doing nothing."
            else:
                print "*** ERROR: Got a write value that we don't support: %s"%value
    
    def read(self):
        """ Reads the value in the current position"""
        return self.__tape[self.__position]


    def erase(self):
        """ Erase the value on the tape in the current position. """
        self.__tape[self.__position] = None
    
        # Only erase if we have to
        if self.__tape[self.__position] != None:
            self._send_command(ERASE)
        
    
    def initialize(self,tape):
        """ Initializes starting data for the tape"""
        for i in range(len(tape)):
            self.__tape[self.__position + i] = tape[i]
    
            # Clean our tape
            self._send_command(ERASE)
            
            # Write our initial value
            if tape[i] == "1":
                self._send_command(WRITE_ONE)
            elif tape[i] == "0":
                self._send_command(WRITE_ZERO)
            
            # Move left
            self._send_command(MOVE_LEFT)

        # Move our write head back
        for i in range(len(tape)):
            self._send_command(MOVE_RIGHT)
    
    def bulk_erase(self):
        """ Deletes everything on the tape """
        self.tape = [None] * self.__tape_length

    def tape(self):
        """ For debug use only: prints and returns the whole tape"""
        return self.__tape

    def position(self):
        """ For debug use only: prints and returns the current location of the tape """
        return self.__position
