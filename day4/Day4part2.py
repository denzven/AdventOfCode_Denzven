from time import sleep

InputFile = open('Day3Input.txt')
InputFileLines = InputFile.readlines()
#InputArray = [str(int(line)) for line in InputFileLines]
InputArray = InputFile.read().splitlines()
#print(InputArray)
#sleep(5)

IniArray = [1,2,3,4,5,6,7,8,9,10,11,12]
ones = 0
zeros = 0
i = 0
ArrayOnes = []
ArrayZeros = []
number = None
#InputArray = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
def Looper(InputArray):
    ones = 0
    zeros = 0
    global i
    ArrayOnes = []
    ArrayZeros = []
    for number in InputArray:
        if len(str(number)) ==  12:
            print(f" Len: {len(str(number))}")
            pass
        elif len(str(number)) !=  12: 
            print(f"{len(str(number))},{number},{i}")
            return

        print(number)
        print(i)
        print(number[i:i+1])
        if int(number[i:i+1]) == 0:
            ArrayZeros.append(number)
            zeros += 1
    
        if int(number[i:i+1]) == 1:
            ArrayOnes.append(number)
            ones += 1
    
        print(f"Ones: {ones} \n Zeros: {zeros}")
        print(f"ArrayOnes: {ArrayOnes} \n ArrayZeros: {ArrayZeros}")
    
    #if zeros > ones:
    if len(ArrayZeros) > len(ArrayOnes):
        InputArray = ArrayZeros
        sleep(1)
        i+=1
        Looper(InputArray)
        
    elif len(ArrayZeros) == len(ArrayOnes):
        if int(number[i:i+1]) == 1:
            InputArray = ArrayOnes
        if int(number[i:i+1]) == 0:
            InputArray = ArrayZeros

    #if zeros < ones:
    elif len(ArrayZeros) < len(ArrayOnes):
        InputArray = ArrayOnes
        sleep(1)
        i+=1
        Looper(InputArray)
        

    if len(InputArray) == 1:
        print(f"\n\n {int(InputArray[0])} is the ans \n {int(InputArray[0],2)} in deci")
        return InputArray


Looper(InputArray)
