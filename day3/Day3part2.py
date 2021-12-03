InputFile = open('Day3Input.txt')
InputFileLines = InputFile.readlines()
InputArray = [str(line) for line in InputFileLines]
IniArray = [1,2,3,4,5,6,7,8,9,10,11,12]
ones = 0
zeros = 0
i = 0
Array = []
Array2 = []

for i in IniArray:
	for number in InputArray:
		print(int(number[i:i+1]))
		if int(number[i:i+1]) == 1:
			print(int(number[i:i+1]))
			ones += 1
			i += 1
			Array2 = Array2.append(InputArray[i])
			print(Array2)

		if int(number[i:i+1]) == 0:
			zeros += 1
			i += 1
			Array2 = Array2.append(InputArray[i])
			print(Array2)

if ones > zeros:
	Array2.append()