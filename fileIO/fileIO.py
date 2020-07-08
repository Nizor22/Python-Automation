from pathlib import Path
count = 0
path = Path('C:/Users/megan/Desktop/Courses/Python_Automation/my files/fileIO/inputFile.txt')
file = open(path, 'r')
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
