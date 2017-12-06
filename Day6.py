
def cycle(LS):
    index = LS.index(max(LS))
    steps = LS[index]
    LS[index] = 0
    for i in range(1, steps+1):
        LS[(index+i)%len(LS)] += 1
        

seenPossibilities = set()
currentState = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
totalCycles = 0
while (tuple(currentState) not in seenPossibilities):
    totalCycles += 1
    seenPossibilities.add(tuple(currentState))
    cycle(currentState)
print("Total cycles =", totalCycles)



seenPossibilities = dict()
currentState = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
totalCycles = 0
while (tuple(currentState) not in seenPossibilities):
    totalCycles += 1
    seenPossibilities[tuple(currentState)] = totalCycles
    cycle(currentState)
print("CurrentState =", currentState)
print("Previously seen =", seenPossibilities[tuple(currentState)])
print("Total cycles =", totalCycles)
print("Cycles since last seen =", totalCycles-seenPossibilities[tuple(currentState)])


