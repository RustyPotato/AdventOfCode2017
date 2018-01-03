
lastA = 116
lastB = 299
judgeCounter = 0

for i in range(40000000):
    # Generation cycle
    aRes = (lastA * 16807) % 2147483647
    bRes = (lastB * 48271) % 2147483647
    
    # Judging time
    if (aRes % 65536 == bRes % 65536):
        print(i, ": Match found!", sep="")
        judgeCounter += 1
    
    # Setup for next round
    lastA = aRes
    lastB = bRes
print("Final judge score:", judgeCounter)



