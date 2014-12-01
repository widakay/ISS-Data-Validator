import csv, sys

#from datetime import datetime

############################
# Parse command line input #
############################
if len(sys.argv) == 2:
	fileName = sys.argv[1]

elif len(sys.argv) == 1:
	fileName = "data-raw.csv"

elif len(sys.argv) > 2:
    print "usage:", "python", sys.argv[1], "[filename.csv]"
    sys.exit(0)



#############################
# Parse CSV file into array #
#############################
f = open(fileName, 'rt')

data = []
try:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
finally:
    f.close()


##############
# Parse data #
##############

# Loop through all the rows of the file
for i in xrange(len(data)-1):
	row = data[i+1]

	# Check row length
	if len(row) != 10:
		print "Wrong length. Got", len(row), "instead of 10",row
		
		# Probably a critical parse error, so let the program end
		sys.exit(0)

	# Loop through all of the columns
	for index in range(len(row)):
		# switch on which column is getting parsed
		if index == 0:	# Timestamp
			pass
		if index == 1:	# Name
			pass
		if index == 2:	# Section
			# Ensure section is capitalized and only one character (misses a few, but gets the majority)
			row[index] = row[index][0].upper()
		if index == 0:	# Day of Discussion
			pass
		if index > 3:	# Data
			try:
				# Try parsing value as number
				row[index] = int(row[index])
			except:
				# If parse failed, check if it was left blank or somebody put a n/a in
				if row[index] == "" or row[index] == "n/a":
					row[index] = 0
				# If it was not one of those, let the user figure out what it meant
				else:
					print "Text in data box on line", str(i) + ": ", row[index]



####################
# Prepare printout #
####################

print '\n'
if raw_input("Would you like a reformatted copy of the data to be printed out? (y/N)").lower() == "y":
	string = ""

	for row in data:
		string += row[0]
		for cell in row[1:]:
			string += "," + str(cell)
		string += '\n'

	print string

