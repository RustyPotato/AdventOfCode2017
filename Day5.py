#---------------#
#     DAY 4     #
#---------------#

def setup():
    file = open("Day5Input.txt")
    ji = []
    for line in file:
        ji.append(int(line.strip()))
    return ji

## Part 1
jumpInstructions = setup()
currentStep = 0
iterations = 0
while (currentStep >= 0 and currentStep < len(jumpInstructions)):
    thisJump = jumpInstructions[currentStep]
    jumpInstructions[currentStep] = jumpInstructions[currentStep] + 1
    currentStep += thisJump
    iterations += 1

print("Part 1 Iterations =", iterations)

## Part 2
jumpInstructions = setup()
currentStep = 0
iterations = 0
while (currentStep >= 0 and currentStep < len(jumpInstructions)):
    thisJump = jumpInstructions[currentStep]
    if (jumpInstructions[currentStep] >= 3):
        jumpInstructions[currentStep] = jumpInstructions[currentStep] - 1        
    else:
        jumpInstructions[currentStep] = jumpInstructions[currentStep] + 1
    currentStep += thisJump
    iterations += 1

print("Part 2 Iterations =", iterations)