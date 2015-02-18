"""
	This is a sample program to read in a file from the disk.
"""
# Define our filename
filename = "tape.txt"

# Open our file
f = open(filename)

# Loop over every line in the file
for line in f:
	# Read value from line
	value = line.strip()

	# Print our value
	print value

# Close our file
f.close()

