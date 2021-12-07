def get_GamaRate(digit):
	global InputFile
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
		print(ones,zeros)
		print(GamaRate)
		print(EpsilonRate)
	if ones < zeros:
		GamaRate.append(0)
		EpsilonRate.append(1)
		print(GamaRate)
		print(EpsilonRate)

InputFile = open('Day3Input.txt')
InputFileLines = InputFile.readlines()
ones = 0
zeros = 0
GamaRate = []
EpsilonRate = []
for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
	print(i)
	get_GamaRate(i)

GamaRate = str("".join(str(i) for i in GamaRate))
EpsilonRate = str("".join(str(i) for i in EpsilonRate))

print(GamaRate)
print(EpsilonRate)

GamaRateDeci = int(GamaRate,2)
print(GamaRateDeci)
EpsilonRateDeci = int(EpsilonRate,2)
print(EpsilonRateDeci)
PowerConsumption = GamaRateDeci * EpsilonRateDeci
print(PowerConsumption)
