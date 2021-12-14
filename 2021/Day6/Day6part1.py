import time
StartTime = time.time()
IntialArray = [int(num) for num in open('Day6Input.txt').read().split(',')]

NumDays = 80
DayI = NumOfFish = 0
def lanternfish(IntialArray,NumDays):
	NextArray = []
	i = nth = 0
	global DayI
	global NumOfFish

	for i in IntialArray:
		if i >= 1:
			NextArray.append(i-1)
			nth += 1

		if i == 0:
			NextArray.append(8)
			NextArray += [6]
			nth += 1

		if DayI >= NumDays:
			return NumOfFish
	DayI += 1
	NumOfFish = len(NextArray)
	lanternfish(NextArray,NumDays)

lanternfish(IntialArray,NumDays)
FinalAnswer = NumOfFish

EndTime = time.time()
print(f"Number of Lanternfish: {FinalAnswer}")
print(f'Execution Time: {EndTime - StartTime}')