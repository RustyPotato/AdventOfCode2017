def calculateWeight(name, allSupporters):
    summation = 0
    if (len(allSupporters[name]) > 1):
        for e in allSupporters[name][1]:
            summation += calculateWeight(e, allSupporters)
    return allSupporters[name][0]+summation

def findAppropriateTree(name, allSupporters):
    allWeights = []
    for i in allSupporters[name][1]:
        allWeights.append( (calculateWeight(i, allSupporters), i) )
        
    allWeights.sort()
    if (allWeights[0][0] == allWeights[-1][0]):
        return allSupporters[name][0]
    else:
        if (allWeights[0][0] == allWeights[1][0]):
            ret = findAppropriateTree(allWeights[-1][1], allSupporters)
            if (ret != None):
                print("The weight of", allWeights[-1][1], "needs to be changed by", allWeights[0][0]-allWeights[-1][0], \
                      "to", allSupporters[allWeights[-1][1]][0]+(allWeights[0][0]-allWeights[-1][0]) )
        else:
            ret = findAppropriateTree(allWeights[0][1], allSupporters)
    

file = open("Day7Input.txt")

allSupporters = dict()
for line in file:
    splitput = line.split()
    name = splitput[0]
    value = int(splitput[1][1:-1])
    children = splitput[3:]
    for i in range(len(children)):
        children[i] = children[i].replace(',', '')
    
    allSupporters[name] = [value, children]
copy = allSupporters.copy()
while (len(copy) > 1):
    for e in allSupporters:
        if (len(allSupporters[e]) > 1):
            for oth in allSupporters[e][1]:
                copy.pop(oth, None)

print("Root of tree =", list(copy)[0])
findAppropriateTree('mkxke', allSupporters)
