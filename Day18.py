def value(register, ind):
    if (isinstance(ind, int)):
        return ind
    else:
        return register[ind]

instructions=[["set","i",31],["set","a",1],["mul","p",17],["jgz","p","p"],["mul","a",2],["add","i",-1],["jgz","i",-2],["add","a",-1],["set","i",127],["set","p",735],["mul","p",8505],["mod","p","a"],["mul","p",129749],["add","p",12345],["mod","p","a"],["set","b","p"],["mod","b",10000],["snd","b"],["add","i",-1],["jgz","i",-9],["jgz","a",3],["rcv","b"],["jgz","b",-1],["set","f",0],["set","i",126],["rcv","a",],["rcv","b",],["set","p","a"],["mul","p",-1],["add","p","b"],["jgz","p",4],["snd","a"],["set","a","b"],["jgz",1,3],["snd","b"],["set","f",1],["add","i",-1],["jgz","i",-11],["snd","a"],["jgz","f",-16],["jgz","a",-19]]

from collections import defaultdict
register = defaultdict(lambda: 0)
lastPlayed = None

i = 0
while i >= 0 and i < len(instructions):
    a = instructions[i]
    
    if (a[0] == "snd"):
        print("Playing noise ", value(register, a[1]))
        lastPlayed = value(register, a[1])
    elif (a[0] == "set"):
        register[a[1]] = value(register, a[2])
    elif (a[0] == "add"):
        register[a[1]] = value(register, a[1]) + value(register, a[2])
    elif (a[0] == "mul"):
        register[a[1]] = value(register, a[1]) * value(register, a[2])
    elif (a[0] == "mod"):
        register[a[1]] = value(register, a[1]) % value(register, a[2])
    elif (a[0] == "rcv" and value(register, a[1]) != 0):
        print("Recovered sound of ", lastPlayed)
        break
    elif (a[0] == "jgz" and value(register, a[1]) > 0):
        print("There was a jump here")
        i += value(register, a[2])
        continue
    
    i += 1
print(register)
    
