InputFile = open('Day2Input.txt')
InputFileLines = InputFile.readlines()
HorizontalPos = 0
VerticalDepth = 0
for line in InputFileLines:
	if line.startswith("up"):
		print(int(line[-2:]))
		VerticalDepth -= int(line[-2:])
	if line.startswith("down"):
		print(int(line[-2:])) 
		VerticalDepth += int(line[-2:])
	if line.startswith("forward"):
		print(int(line[-2:]))
		HorizontalPos += int(line[-2:])
print(HorizontalPos)
print(VerticalDepth)
print(HorizontalPos * VerticalDepth)