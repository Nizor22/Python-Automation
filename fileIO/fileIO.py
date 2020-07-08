count = 0
file = open('inputFile.txt', 'r')
passedFile = open('Passed.txt', 'w')
failedFile = open('Failed.txt', 'w')
for line in file:
	line_split = line.split()
	if line_split[2] == 'P':
		passedFile.write(line)
	else:
		failedFile.write(line)
file.close()
passedFile.close()
failedFile.close()
