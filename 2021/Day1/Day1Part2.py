import time
StartTime = time.time()
InputArray = [int(line) for line in open('Day1Input.txt').readlines()]

i = prev3val = Inc = Dec = 0

for readings in InputArray:
	if i < 2:
		i += 1

	elif i > len(InputArray) - 2:
		break

	else:
		prev3val2 = int(InputArray[i-2] + InputArray[i-1] + InputArray[i])
		if int(prev3val - prev3val2) > 0:
			Inc += 1
			prev3val = prev3val2

		if int(prev3val - prev3val2) < 0:
			Dec += 1
			prev3val = prev3val2
		i += 1

FinalAnswer = Dec
EndTime = time.time()
print(f"Sums that are larger than the previous sum: {FinalAnswer}")
print(f'Execution Time: {EndTime - StartTime}')