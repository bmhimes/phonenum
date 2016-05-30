import sys
import itertools
import os.path

letters = []
letters.append(['0'])
letters.append(['1'])
letters.append(['A', 'B', 'C'])
letters.append(['D', 'E', 'F'])
letters.append(['G', 'H', 'I'])
letters.append(['J', 'K', 'L'])
letters.append(['M', 'N', 'O'])
letters.append(['P', 'Q', 'R', 'S'])
letters.append(['T', 'U', 'V'])
letters.append(['W', 'X', 'Y'])

outputFileName = 'outputletters.txt'

mode = ''
inputFileName = ''
cliNumber = ''

if len(sys.argv) > 1:
	mainInput = sys.argv[1]

	if mainInput.isdigit():
		mode = 'cli'
		cliNumbers = mainInput
	else:
		mode = 'file'
		inputFileName = mainInput
else:
	mode = 'file'
	inputFileName = 'inputnums.txt'

print 'mode =',mode

if mode == 'file':
	if not(os.path.isfile(inputFileName)):
		raise OSError(1, 'Input file not found.')

numbersList = []
if mode == 'cli':
	numbersList.append(cliNumbers)
if mode == 'file':
	with open(inputFileName, 'r') as f:
		for line in f:
			numbersList.append(line.strip())

print 'Started generating letter combinations.'

outputFile = open(outputFileName, 'w+')
numbersIndex = -1
for numbers in numbersList:

	numbersIndex += 1
	if numbersIndex > 0:
		outputFile.write('\n\n')
	outputFile.write(numbers)

	letterInputs = []
	for number in numbers:
		letterInputs.append(letters[int(number)])

	solutions = apply(itertools.product, letterInputs)
	solutionCount = 0
	
	for solution in solutions:
		solutionCount += 1
		solutionText = ''.join(solution)
		outputFile.write('\n' + solutionText)
		print solutionText

	digits = len(numbers)
	print 'numbers =',numbers
	print 'digits = ',digits
	print 'letterInputs =',letterInputs
	print 'solution count for',numbers,'=',solutionCount

outputFile.close()
print 'Finished.'