"""
	This is an example using our turing machine class
"""

# Import our machine
from tmachine.VirtualHardware import VirtualHardware

# Initialize our turing machine
turing_machine = VirtualHardware()


# Write 10 1's to the tape
for x in range(10):
	turing_machine.write(1)
	turing_machine.moveLeft()

# print the tape for sanity
tape = turing_machine.tape()