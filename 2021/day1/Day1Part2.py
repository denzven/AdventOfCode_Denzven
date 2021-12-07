InputFile = open('Day1Input.txt')
InputFileLines = InputFile.readlines()
InputArray = [int(line) for line in InputFileLines]
i = 0
prev3val = 0
Inc = 0
Dec = 0
for readings in InputArray:
	if i < 2:
		i += 1

	elif i > len(InputArray) - 2:
		print(len(InputArray))
		break

	else:
		prev3val2 = int((InputArray[i-2]+InputArray[i-1]+InputArray[i]))
		if int(prev3val - prev3val2) > 0:
			Inc += 1
			prev3val = prev3val2


		if int(prev3val - prev3val2) < 0:
			Dec += 1
			prev3val = prev3val2
		i += 1

	print(f"{prev3val} decreased by {Dec}")
	print(f"{prev3val} increased by {Inc}")

print("---")
print(Inc)
print(Dec)




