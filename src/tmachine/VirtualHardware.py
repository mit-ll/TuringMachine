from AbstractHardware import *

class VirtualHardware(AbstractHardware):
	""" Software-implemented Turing machine hardware

	Used for general testing of Turing machine logic and interface """

	def __init__(self, **kwargs):
		""" Creates the virtual hardware. 

		Keyword arguments:
		 + tape_length = 1000    <- Length of tape in units
		 + init        = []      <- starting data of tape (calls initialize)
		 """

		self.__tape_length = 1000
		if "tape_length" in kwargs.keys():
			self.__tape_length = kwargs["tape_length"]

		self.__tape = [None] * self.__tape_length

		self.__position = self.__tape_length / 2 # int division

		if "init" in kwargs.keys():
			self.initialize(kwargs["init"])

	def moveLeft(self,x=1):
		""" moves the tape x units to the left """
		newPos = self.__position + x
		if newPos >= self.__tape_length:
			raise Exception("Out of (Virtual) Tape!")
		else:
			self.__position = newPos

	def moveRight(self,x=1):
		""" moves the tape x units to the left """
		newPos = self.__position - x
		if newPos < 0:
			raise Exception("Out of (Virtual) Tape!")
		else:
			self.__position = newPos
	
	def write(self,value):
		""" Writes value to current position in tape"""
		self.__tape[self.__position] = value

	
	def read(self):
		""" Reads the value in the current position"""
		return self.__tape[self.__position]


	def erase(self):
		""" Erase the value on the tape in the current position. """
		self.__tape[self.__position] = None
		
	
	def initialize(self,tape):
		""" Initializes starting data for the tape"""
		for i in range(len(tape)):
			self.__tape[self.__position + i] = tape[i]

	
	def bulk_erase(self):
		""" Deletes everything on the tape """
		self.tape = [None] * self.__tape_length

	def tape(self):
		""" For debug use only: prints and returns the whole tape"""
		return self.__tape

	def position(self):
		""" For debug use only: prints and returns the current location of the tape """
		return self.__position
