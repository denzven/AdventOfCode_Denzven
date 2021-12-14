InputFile = open('Day1Input.txt')
InputFileLines = InputFile.readlines()
i = 0
Inc = 0
Dec = 0
prevline = None
for line in InputFileLines:
	line = int(line)
	if i == 0:
		print(int(line))
		prevline = int(line)
		i += 1
	if i > 0:
		#print(int(line))
		if int(prevline - line) > 0:
			Dec += 1
			prevline = int(line)
		if int(prevline - line) < 0:
			Inc += 1
			prevline = int(line)
		i+=1

	print(f"{line}(Increased by {Inc})")
	print(f"{line}(Decreased by {Dec})")
print("---")
print(Inc)
print(Dec)