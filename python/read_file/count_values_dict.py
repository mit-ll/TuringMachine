"""
        This is a sample program to read in a file from the disk.

	In this case we use a dictionary to keep track of the count for every value that we might encounter.
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
count_dict = {}

# Loop over every line in the file
for line in f:
        # Read value from line
        value = line.strip()

	# Do we already have a counter for this value?
        if value in count_dict:
		# If so, just increment it by one
                count_dict[value] += 1
	else:
		# If this is the first time seeing this value, set our counter to 1
		count_dict[value] = 1

# Close our file
f.close()

# Print our answer
print "I found the following counts:"
for value in count_dict:
	print "%d lines with value '%s'"%(count_dict[value],value)
