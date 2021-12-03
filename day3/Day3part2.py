from time import sleep

InputFile = open('Day3Input.txt')
InputFileLines = InputFile.readlines()
InputArray = [str(int(line)) for line in InputFileLines]
InputArray.sort(reverse=True) 
#print(InputArray)
#sleep(5)
IniArray = [1,2,3,4,5,6,7,8,9,10,11,12]
ones = 0
zeros = 0
i = 0
ArrayOnes = []
ArrayZeros = []

InputArray = ['000110000001','011011001101','001101100111','111101010010']
def looper():
    global InputArray
    global IniArray
    global i

    ones = 0
    zeros = 0
    ArrayOnes = []
    ArrayZeros = []

    for q in IniArray:
        if i > 11:
            break
        for number in InputArray:
            print(number)
            print(i)
            print(int(number[i:i+1]))
            if number[i:i+1] == '':
                break
            if int(number[i:i+1]) == 1:
                print(int(number[i:i+1]))
                ones += 1
                ArrayOnes.append(number)
                pass    
        
            elif int(number[i:i+1]) == 0:
                print(int(number[i:i+1]))
                zeros += 1
                ArrayZeros.append(number)
                pass
        
            print(f"ArrayOnes: {ArrayOnes}\n\n\n")
            #sleep(1)
            print(f"ArrayZeros: {ArrayZeros}\n\n\n")
    i+=1
    if ones < zeros:
        InputArray = ArrayOnes
    if ones > zeros:
        InputArray = ArrayZeros
    sleep(5)
    looper()
looper()
