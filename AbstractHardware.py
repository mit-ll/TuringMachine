from abc import ABCMeta, abstractmethod

class AbstractHardware:
	""" An abstract class that all hardware interfaces are derived from. 

	Descended classes will be a VirtualHardWare and Hardware, 
	allowing for software testing and real implementation to use
	the same interface. 

	Methods:

	-- move_tape
	-- write
	-- read
	-- initialize
	-- bulk_erase
	"""

	__metaclass__ = ABCMeta

	@abstractmethod
	def move_tape(self,x):
		""" moves the tape x units to the left """
		pass

	@abstractmethod
	def write(self,value):
		""" Writes value to current position in tape"""
		pass

	@abstractmethod
	def read(self):
		""" Reads the value in the current position"""
		pass

	@abstractmethod
	def initialize(self,tape):
		""" Initializes starting data for the tape"""
		pass

	@abstractmethod
	def bulk_erase(self):
		""" Deletes everything on the tape """
		pass