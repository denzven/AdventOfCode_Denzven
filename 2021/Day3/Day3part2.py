from time import sleep
import time
StartTime = time.time()
InputArrayFile = [line.rstrip() for line in open('Day3Input.txt')]
i = 0
q = 0
InputArray = InputArray2 = InputArrayFile
def GetOxyGenRate(InputArray):
    ones = zeros = 0
    ArrayOnes = ArrayZeros = []
    global i
    global OxyGenRate

    for number in InputArray:
        if len(InputArray) == 2:
            OxyGenRate = InputArray[0]
            return

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


    if len(ArrayZeros) > len(ArrayOnes):
        InputArray = ArrayZeros
        sleep(1)
        i+=1
        GetOxyGenRate(InputArray)
        
    elif len(ArrayZeros) == len(ArrayOnes):
        if int(number[i:i+1]) == 1:
            InputArray = ArrayOnes
            GetOxyGenRate(InputArray)
        if int(number[i:i+1]) == 0:
            InputArray = ArrayZeros
            GetOxyGenRate(InputArray)

    #if zeros < ones:
    elif len(ArrayZeros) < len(ArrayOnes):
        InputArray = ArrayOnes
        sleep(1)
        i+=1
        GetOxyGenRate(InputArray)

def GetCO2rate(InputArray2):
    ones = zeros = 0
    ArrayOnes = ArrayZeros = []
    global q 
    global CO2Rate

    for number in InputArray2:
        if q >= 12:
            print(q)
            return
        if len(InputArray2) == 2:
            print(f"\n\n {int(InputArray2[0])} is the ans \n {int(InputArray[0],2)} in deci")
            CO2rate = InputArray2[0]
            return

        if len(str(number)) ==  12:
            print(f" Len: {len(str(number))}")
            print(f"{q}")
            pass
        elif len(str(number)) !=  12: 
            print(f"{len(str(number))},{number},{q}")
            return

        print(number)
        print(q)
        print(number[q:q+1])
        if int(number[q:q+1]) == 0:
            ArrayZeros.append(number)
            zeros += 1
    
        if int(number[q:q+1]) == 1:
            ArrayOnes.append(number)
            ones += 1
    
        print(f"Ones: {ones} \n Zeros: {zeros}")
        print(f"ArrayOnes: {ArrayOnes} \n ArrayZeros: {ArrayZeros}")

    #if zeros > ones:
    if len(ArrayZeros) < len(ArrayOnes):
        InputArray2 = ArrayZeros
        sleep(1)
        q+=1
        GetCO2rate(InputArray2)
        
    elif len(ArrayZeros) == len(ArrayOnes):
        if int(number[q:q+1]) == 0:
            InputArray2 = ArrayOnes
            GetCO2rate(InputArray2)
        if int(number[q:q+1]) == 1:
            InputArray2 = ArrayZeros
            GetCO2rate(InputArray2)

    #if zeros < ones:
    elif len(ArrayZeros) > len(ArrayOnes):
        InputArray = ArrayOnes
        #sleep(1)
        q+=1
        GetCO2rate(InputArray2)

GetCO2rate(InputArray2)
sleep(10)

GetOxyGenRate(InputArray)

print(OxyGenRate)
print(CO2Rate)
