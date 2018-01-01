
circularArray = [0]
pos = 0
steps = 377

print(circularArray)

for i in range(1,2018):
    pos += steps
    pos = pos%len(circularArray)
    circularArray.insert(pos+1, i)
    pos = pos+1

print(circularArray)
print(circularArray[circularArray.index(2017)+1])

