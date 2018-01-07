#---------------#
#     DAY 3     #
#---------------#
def day3Challenge(target):
    layer = 0
    for i in range(target): 
        if (i%2 == 1):
            if (i*i <= target):
                layer = i
            else:
                break
    side = ((target-((layer)**2)))//(layer+1)
    pos = ((target - ((layer-2)**2)) % (layer+1))
        
    deltaX = 0
    deltaY = 0
    
    if (target == layer**2):
        deltaX = layer//2
        deltaY = layer//2
    else:
        if (side == 0):
            deltaX = ((layer+2)//2)
            deltaY = ((layer+2)//2)-pos
        if (side == 1):
            deltaY = ((layer+2)//2)
            deltaX = (-((layer+2)//2)+pos)
        if (side == 2):
            deltaY = ((layer+2)//2)
            deltaX = -(-((layer+2)//2)+pos)
        if (side == 3):
            deltaX = ((layer+2)//2)
            deltaY = -(-((layer+2)//2)+pos)
            
        
    print("dX = ", deltaX, "  dY = ", deltaY)
    print("Distance to origin =", abs(deltaX)+abs(deltaY))
    return (deltaX, deltaY)
    
day3Challenge(289326)