import time
StartTime = time.time()
InputFileLines = open('Day3Input.txt').readlines()
ones = zeros = 0
GamaRate = []
EpsilonRate = []

def get_GamaRate(digit):
	global InputFileLines
	global GamaRate
	global EpsilonRate
	ones = 0
	zeros = 0
	for line in InputFileLines:
		if int(line[digit-1:digit]) == 1:
			ones += 1
		if int(line[digit-1:digit]) == 0:
			zeros += 1
	if ones > zeros:
		GamaRate.append(1)
		EpsilonRate.append(0)

	if ones < zeros:
		GamaRate.append(0)
		EpsilonRate.append(1)

for i in range(1,13):
	get_GamaRate(i)

GamaRate = int(str("".join(str(i) for i in GamaRate)),2)
EpsilonRate = int(str("".join(str(i) for i in EpsilonRate)),2)
PowerConsumption = GamaRate * EpsilonRate

FinalAnswer = PowerConsumption

EndTime = time.time()
print(f"Power consumption of the submarine: {FinalAnswer}")
print(f'Execution Time: {EndTime - StartTime}')