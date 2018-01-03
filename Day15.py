
lastA = 116
lastB = 299
judgeCounter = 0

for i in range(40000000):
    # Generation cycle
    aRes = (lastA * 16807) % 2147483647
    bRes = (lastB * 48271) % 2147483647
    
    # Judging time
    if (aRes % 65536 == bRes % 65536):
        print("Match found! With ", aRes, " and ", bRes, sep="")
        judgeCounter += 1
    
    # Setup for next round
    lastA = aRes
    lastB = bRes
print("Final judge score, part 1:", judgeCounter)


## Part 2
lastA = 116
lastB = 299
judgeCounter = 0

for i in range(5000000):
    # Generation cycle
    aRes = (lastA * 16807) % 2147483647
    while (aRes % 4 != 0):
        aRes = (aRes * 16807) % 2147483647
    bRes = (lastB * 48271) % 2147483647
    while (bRes % 8 != 0):
        bRes = (bRes * 48271) % 2147483647
    
    # Judging time
    if (aRes % 65536 == bRes % 65536):
        print(i, ": Match found!", sep="")
        judgeCounter += 1
    
    # Setup for next round
    lastA = aRes
    lastB = bRes
print("Final judge score, part 2:", judgeCounter)



