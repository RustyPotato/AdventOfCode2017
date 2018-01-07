import copy

def boardToString(board):
    output = ""
    for i in board:
        for j in i:
            for k in j:
                output += k
        output += '/'
    return output[:-1]
    

def printBoard(board):
    print(boardToString(board).replace('/', '\n'))

def allPermutations(inGrid):
    possibilities = set()
    if (type(inGrid) == str):
        inGrid = inGrid.split("/")
        inGrid = list(map(list, inGrid))
        

    # Try the four rotations! 
    for i in range(4):
        # Rotate the grid.
        inGrid = list(zip(*inGrid[::-1]))
        inGrid = list(map(list, inGrid))
        
        # Generate the horizontal flip
        hFlip = copy.deepcopy(inGrid)
        for subL in hFlip:
            subL.reverse()
        
        # Generate the vertical flip
        vFlip = copy.deepcopy(inGrid)
        for i in range(len(vFlip)):
            col = []
            for j in range(len(vFlip)):
                col.append(vFlip[j][i])
            col.reverse()
            for j in range(len(vFlip)):
                vFlip[j][i] = col[j]
        
        # Add the all to the possibilities
        possibilities.add(boardToString(inGrid))
        possibilities.add(boardToString(hFlip))
        possibilities.add(boardToString(vFlip))
        
    return possibilities


def matchesPattern(inGrid, rule):
    rule = list(map(list, rule.split("/")))
    
    if (len(inGrid) != len(rule)):
        return False
    
    # Try the four rotations! 
    for i in range(4):
        # Rotate the grid.
        rule = list(zip(*rule[::-1]))
        rule = list(map(list, rule))
        
        # If it pattern matches the rotation...
        #print("    R:", rule)
        if (inGrid == rule):
            return True
    
        # Otherwise a horizontal flip of the rotation...
        hFlip = copy.deepcopy(rule)
        for subL in hFlip:
            subL.reverse()
        #print("    H:", hFlip)
        if (inGrid == hFlip):
            return True
        
        # Otherwise a vertical flip of the rotation...
        vFlip = copy.deepcopy(rule)
        for i in range(len(vFlip)):
            col = []
            for j in range(len(vFlip)):
                col.append(vFlip[j][i])
            col.reverse()
            for j in range(len(vFlip)):
                vFlip[j][i] = col[j]
        #print("    V:", vFlip)
        if (inGrid == vFlip):
            return True
        
    return False


def decompose(grid):
    if type(grid) == str:
        grid = grid.split("/")
        grid = list(map(list, grid))
        
    
    result = []
    
    if (len(grid) % 2 == 0):
        # Divide into 2x2 squares
        for i in range(len(grid)//2):
            line = []
            for j in range(len(grid[0])//2):
                group = []
                group.append(grid[i*2  ][j*2:j*2+2])
                group.append(grid[i*2+1][j*2:j*2+2])
                line.append(group)
            result.append(line)
            
    elif (len(grid) % 3 == 0):
        # Divide into 3x3 squares
        for i in range(len(grid)//3):
            line = []
            for j in range(len(grid[0])//3):
                group = []
                
                group.append(grid[i*3+0][j*3:j*3+3])
                group.append(grid[i*3+1][j*3:j*3+3])
                group.append(grid[i*3+2][j*3:j*3+3])
                
                line.append(group)
            result.append(line)
    else:
        print("Error! Found a ", len(grid), ", ", len(grid[0]), " board", sep="")
        print(grid)
    
    return result


ruleBook = {"../..":"..#/.#./...","#./..":".../#../.##","##/..":".##/###/##.",".#/#.":"#.#/..#/#.#","##/#.":".../.##/...","##/##":"##./..#/..#",".../.../...":"##../..../##../.###","#../.../...":"...#/.#.#/.#../.#.#",".#./.../...":"#.#./...#/#.#./.##.","##./.../...":"..#./#.##/#.../.###","#.#/.../...":"##../##.#/..#./#.##","###/.../...":"..../.#.#/.###/#..#",".#./#../...":"#..#/#.../.##./....","##./#../...":"#.##/..##/####/.###","..#/#../...":"..#./#.##/####/####","#.#/#../...":".##./#.##/#.#./##.#",".##/#../...":"#.##/####/.###/...#","###/#../...":"..../#.#./##.#/..##",".../.#./...":".###/.##./##../.##.","#../.#./...":"..../#.##/...#/#.#.",".#./.#./...":"...#/####/.##./#...","##./.#./...":".###/#.##/###./....","#.#/.#./...":"#.##/###./..../..#.","###/.#./...":".#../#.#./#.##/#.##",".#./##./...":".###/##../..##/#..#","##./##./...":"..#./#.#./.#.#/##.#","..#/##./...":".#../####/...#/..##","#.#/##./...":"..../##.#/.##./....",".##/##./...":".#.#/.#.#/.##./####","###/##./...":"##.#/..../..../....",".../#.#/...":"..##/##../##.#/###.","#../#.#/...":"####/#.##/#.../###.",".#./#.#/...":"..../#..#/..##/.#..","##./#.#/...":"#.../..##/##../..#.","#.#/#.#/...":"...#/#.#./#.#./#...","###/#.#/...":"###./###./##.#/###.",".../###/...":"..#./###./##.#/####","#../###/...":"##.#/..#./##../..##",".#./###/...":"#.../#.##/##../....","##./###/...":"..##/.#.#/#..#/#.##","#.#/###/...":"#.##/..#./.#../..##","###/###/...":"..#./#..#/####/.##.","..#/.../#..":"##.#/#.##/...#/###.","#.#/.../#..":"#..#/..#./##../###.",".##/.../#..":"..#./.#../###./#.#.","###/.../#..":"...#/...#/.#.#/.##.",".##/#../#..":"##../#.#./#..#/##..","###/#../#..":"##../.#.#/##../#..#","..#/.#./#..":"##.#/##.#/...#/.#..","#.#/.#./#..":".###/.#.#/###./....",".##/.#./#..":"#..#/###./####/..#.","###/.#./#..":"..#./.###/.###/...#",".##/##./#..":"#.##/..##/...#/.###","###/##./#..":"####/##.#/#.##/#..#","#../..#/#..":"..../.##./#.##/#...",".#./..#/#..":"#..#/##../...#/#...","##./..#/#..":"..#./.###/..##/.#.#","#.#/..#/#..":".##./..##/..#./#..#",".##/..#/#..":"####/.#.#/#.../.#.#","###/..#/#..":"..../..##/#.##/###.","#../#.#/#..":"#.##/.#.#/.#../.##.",".#./#.#/#..":"..##/###./.###/###.","##./#.#/#..":"##.#/##.#/#.#./##..","..#/#.#/#..":"###./###./.#.#/.#..","#.#/#.#/#..":"##../..#./##../....",".##/#.#/#..":".###/#.#./##.#/##..","###/#.#/#..":"##.#/#.#./.#.#/#...","#../.##/#..":".#.#/...#/.#.#/..#.",".#./.##/#..":"###./##../##.#/....","##./.##/#..":"..##/###./#.#./#.#.","#.#/.##/#..":"##.#/..##/#..#/####",".##/.##/#..":"..../####/..#./##..","###/.##/#..":".###/#..#/..../.#..","#../###/#..":"#..#/.#../.#.#/#...",".#./###/#..":".#../..../.##./.###","##./###/#..":"##.#/.#../.#.#/#..#","..#/###/#..":"#.##/##../..##/#...","#.#/###/#..":"####/..##/.#../##.#",".##/###/#..":".###/#..#/.###/#.##","###/###/#..":"..##/.##./##../#..#",".#./#.#/.#.":"..##/.##./.##./.###","##./#.#/.#.":"..##/...#/.##./####","#.#/#.#/.#.":".###/.###/#.#./.#..","###/#.#/.#.":"##.#/###./##.#/####",".#./###/.#.":"...#/..#./.#.#/.#..","##./###/.#.":"###./##.#/#.../#.#.","#.#/###/.#.":".##./#.#./...#/..#.","###/###/.#.":".#.#/.#../..##/####","#.#/..#/##.":".##./...#/#..#/.###","###/..#/##.":"#.##/.#.#/...#/..##",".##/#.#/##.":"###./.###/...#/....","###/#.#/##.":".##./.##./#.#./#...","#.#/.##/##.":"#.#./.##./.#.#/.###","###/.##/##.":"..../####/.#.#/#.##",".##/###/##.":".##./.###/###./.#..","###/###/##.":"#.../###./.##./##.#","#.#/.../#.#":"#.#./..../#.##/###.","###/.../#.#":".#../.#.#/#.../.###","###/#../#.#":"###./#..#/####/##..","#.#/.#./#.#":"###./##.#/..../.#..","###/.#./#.#":"####/.#.#/.#../..##","###/##./#.#":"#.#./####/..##/#...","#.#/#.#/#.#":"#.#./#.#./#.../#.##","###/#.#/#.#":"#.##/.#../..#./.##.","#.#/###/#.#":".###/..##/####/#..#","###/###/#.#":"#.../..#./..#./#.##","###/#.#/###":".#.#/.###/#.##/..##","###/###/###":"#.#./...#/.#../.#.#"}

#ruleBook = [("../.#", "##./#../..."), (".#./..#/###", "#..#/..../..../#..#")]


workingGrid = ".#./..#/###"
workingGrid = workingGrid.split("/")
workingGrid = list(map(list, workingGrid))

print("Iteration", 0)
printBoard(workingGrid)

for tick in range(1,19):
    resultGrid = []
    decomposition = decompose(workingGrid)
    
    for line in decomposition:
        resultLine = [ [], [], [], [] ]
        
        for group in line:
            possibleOrientations = allPermutations(group)
            resultGroup = ""
            for i in possibleOrientations:
                if i in ruleBook.keys():
                    resultGroup = ruleBook[i]
                    break
            
            resultGroup = resultGroup.split("/")
            resultGroup = list(map(list, resultGroup))
            
            resultLine[0] += (resultGroup[0])
            resultLine[1] += (resultGroup[1])
            resultLine[2] += (resultGroup[2])
            if(len(resultGroup) > 3):
                resultLine[3] += (resultGroup[3])
            
            
        resultGrid += resultLine[0:3]
        if (len(resultLine[3]) > 0):
            resultGrid += resultLine[3:]
        
    workingGrid = resultGrid
    print("\nIteration", tick)
    printBoard(workingGrid)

liveCells = 0
for i in workingGrid:
    for j in i:
        if (j == '#'):
            liveCells += 1

print(liveCells)

