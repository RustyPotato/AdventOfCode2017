#---------------#
#     DAY 3     #
#---------------#
target = 289326
layer = 0
for i in range(target): 
    if (i%2 == 1):
        if (i*i <= target):
            layer = i
        else:
            break
print("Layer", layer)
print("Layer from", layer**2, "to", (layer+2)**2)

print("Steps from start =", target - (layer**2 + 1))
side = (target - (layer**2 + 1))//(layer+1)
print("On side", side)
pos = ((target - (layer**2))%(layer+1))
print("Steps from side start", pos)

deltaX = 0
deltaY = 0

if (target == layer**2):
    print("Moves required asdf = ", 2*(layer-2))
else:
    deltaY = layer-1
    deltaX = -(layer-1)+pos
    print("dX = ", deltaX, "  dY = ", deltaY)
    print("Moves required = ", abs(deltaX)+abs(deltaY))

