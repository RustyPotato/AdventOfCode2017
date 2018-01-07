
file = open("Day8Input.txt")
allRegisters = dict()

def operatorHelp(registerValue, operation, value):
    if (operation == '>'):
        return registerValue > value
    elif (operation == '<'):
        return registerValue < value
    elif (operation == '>='):
        return registerValue >= value
    elif (operation == '<='):
        return registerValue <= value
    elif (operation == '=='):
        return registerValue == value
    elif (operation == '!='):
        return registerValue != value

maxValue = 0
for line in file:
    div = line.split(' ')
    modReg = div[0]
    operator = div[1]
    delta = int(div[2])
    
    queryReg = div[4]
    comparison = div[5]
    queryAmt = int(div[6])
    if (modReg not in allRegisters):
        allRegisters[modReg] = 0
    if (queryReg not in allRegisters):
        allRegisters[queryReg] = 0
    
    if (operatorHelp(allRegisters[queryReg], comparison, queryAmt)):
        # Either increment
        if (operator == 'inc'):
            allRegisters[modReg] = allRegisters[modReg] + delta
        # Or decrement
        if (operator == 'dec'):
            allRegisters[modReg] = allRegisters[modReg] - delta
    if (allRegisters[modReg] > maxValue):
        maxValue = allRegisters[modReg]
    

print("Largest value throughout simulation =", maxValue)
maxEndValue = 0
for i in allRegisters:
    if (allRegisters[i] > maxEndValue):
        maxEndValue = allRegisters[i]
print("Largest value at the end =", maxEndValue)
