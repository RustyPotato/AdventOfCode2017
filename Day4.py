#---------------#
#     DAY 4     #
#---------------#
def anagramable(str1, str2):
    if len(str1) != len(str2):
        return False
    dict1 = dict()
    for i in str1:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    dict2 = dict()
    for i in str2:
        if i in dict2:
            dict2[i] = dict2[i] + 1
        else:
            dict2[i] = 1
    
    shared_items = set(dict1.items()) & set(dict2.items())
    return (len(shared_items) == len(dict1) and len(shared_items) == len(dict2))

def anagramableStarter(string):
    string = string.split(' ')
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j and anagramable(string[i], string[j]):
                return False
    return True

def validWords(string):
    string = string.split(' ')
    string.sort()
    for i in range(len(string)-1):
        if (string[i] == string[i+1]):
            return False
    return True

## Part 1
file = open("Day4Input.txt")
line = file.readline()
line = line.strip()
total = 0
while (line != ''):
    if (validWords(line)):
        total += 1
    line = file.readline().strip()
print(total)

## Part 2
file = open("Day4Input.txt")
line = file.readline()
line = line.strip()
total = 0
while (line != ''):
    if (validWords(line) and anagramableStarter(line)):
        total += 1
    line = file.readline().strip()
print(total)
