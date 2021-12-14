import time

StartTime = time.time()

FishArray = [int(num) for num in open('Day6Input.txt').read().split(',')]

# Preparing for Cesus
FishCensus = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}

# Intial Census
for fish in FishArray:
    FishCensus[fish] += 1

for i in range(256):
    PregFish = FishCensus[0]
    for q in range(8):
    	FishCensus[q] = FishCensus[q+1]
    	#print(q)
    
    FishCensus[8] = PregFish
    FishCensus[6] += PregFish

TotalNumFish = sum(FishCensus.values())

EndTime = time.time()

print(f'Total Fish: {TotalNumFish}')
print(f'Execution Time (s): {EndTime - StartTime}')

# Thx a ton to @SukenSplash aka SunkenSplashGaming#4953 on discord