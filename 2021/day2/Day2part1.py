import time
StartTime = time.time()
InputFileLines = open('Day2Input.txt').readlines()

HorizontalPos = VerticalDepth = 0

for line in InputFileLines:
	if line.startswith("up"):
		VerticalDepth -= int(line[-2:])

	if line.startswith("down"): 
		VerticalDepth += int(line[-2:])

	if line.startswith("forward"):
		HorizontalPos += int(line[-2:])

FinalAnswer = HorizontalPos * VerticalDepth

EndTime = time.time()
print(f"Multiply your final horizontal position by your final depth?: {FinalAnswer}")
print(f'Execution Time: {EndTime - StartTime}')