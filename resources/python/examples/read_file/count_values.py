"""
        This is a sample program to read in a file from the disk.

	In this example we keep track of the number of 1s, 0s and ''s
"""

# Import our system module
import sys

# Check for command line arguments (Our filename)
if len(sys.argv) < 2:
	print "Usage: %s <tape filename>"%sys.argv[0]
	sys.exit(0)

# Define our filename (From the command line argument)
filename = sys.argv[1]

# Open our file
f = open(filename)

# Define our variables to keep track of our counts
ones = 0
zeros = 0
nothing = 0

# Loop over every line in the file
for line in f:
        # Read value from line
        value = line.strip()

	if value == "1":
    	ones += 1
    elif value == "0":
		zeros += 1
	elif value == "":
		nothing += 1
	else:
		print "Found invalid character: %s"%value

# Close our file
f.close()

# Print our answer
print "I found %d ones, %d zeros, %d nothings"%(ones, zeros, nothing)
