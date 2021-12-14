import time
StartTime = time.time()
InputFileLines = open('Day1Input.txt').readlines()

i = Inc = Dec = 0

for line in InputFileLines:
	line = int(line)
	if i == 0:
		prevline = int(line)
		i += 1
	if i > 0:
		if int(prevline - line) > 0:
			Dec += 1
			prevline = int(line)
		if int(prevline - line) < 0:
			Inc += 1
			prevline = int(line)
		i += 1

FinalAnswer = Inc
EndTime = time.time()
print(f"Measurements are larger than the previous measurement: {FinalAnswer}")
print(f'Execution Time: {EndTime - StartTime}')