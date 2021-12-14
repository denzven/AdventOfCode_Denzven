InputFile = open('Day4Input.txt')
InputFileLines = InputFile.read().splitlines()

BingoCallNum = InputFileLines[0]

#for q in InputFileLines:

BoardPosArray = [num for num in range(len(InputFileLines))][2::6]
#print(BoardPosArray)
#print(BoardPosArray[1::5])

for i in BoardPosArray:
	BingoBoard1 = [InputFileLines[i],InputFileLines[i+1],InputFileLines[i+2],InputFileLines[i+3],InputFileLines[i+4]]
	print(BingoBoard1)
	print("\n \n")

#print(BingoCallNum)
#print(BingoBoard)