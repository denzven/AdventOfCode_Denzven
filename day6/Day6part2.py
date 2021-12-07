IntialArray = [3,4,3,1,2]
#IntialArray = [int(num) for num in open('Day6Input.txt').read().split(',')]
print(IntialArray)
ithnum = 256
ith = 0
lenarr = 0
def lanternfish(IntialArray,ithnum):
	NextArray = []
	day = 0
	i = 0
	nth = 0
	global ith
	global lenarr
	for i in IntialArray:
		if i >= 1:
			NextArray.append(i-1)
			nth += 1
		if i == 0:
			#print(NextArray[nth])
			NextArray.append(8)
			NextArray += [6]
			nth+=1
		if ith >= ithnum:
			print(lenarr)
			return lenarr
	ith += 1

	print(f"ith:{ith} NxtArr:NextArray len: {len(NextArray)}")
	lenarr = len(NextArray)
	lanternfish(NextArray,ithnum)


lanternfish(IntialArray,ithnum)