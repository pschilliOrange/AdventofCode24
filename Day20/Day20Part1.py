with open('Day20/input.txt', 'r') as file:
    lines = [line.strip() for line in file]

map = []
for lineInd in range(len(lines)):
    map.append([])
    for charInd in range(len(lines[0])):
        char = lines[lineInd][charInd]
        if char == 'S':
            start = (lineInd, charInd)
            map[lineInd].append('.')
        elif char == 'E':
            end = (lineInd, charInd)
            map[lineInd].append('.')
        else:
            map[lineInd].append(lines[lineInd][charInd])


directions = [(0,1),(1,0),(-1,0),(0,-1)]
countDict = {}
def findShortest(start, end):
    count = 0
    notEnd = True
    curr = start
    past = (0,0)
    while notEnd:
        nextMoves = 0
        countDict[curr] = count
        for direction in directions:
            if map[curr[0]+direction[0]][curr[1]+direction[1]] == '.' and (curr[0]+direction[0],curr[1]+direction[1]) != past:
                count += 1
                nextMoves += 1
                next = (curr[0]+direction[0],curr[1]+direction[1])
        if nextMoves > 1:
            print("uhoh, more than one options at ", curr)
        past = curr
        curr = next
        if curr == end:
            notEnd = False
    return count
countDict[end] = findShortest(start,end)

twoDirections = [(-1,1),(-2,0),(-1,-1),(0,-2),(1,-1),(2,0),(1,1),(0,2)]
def getShortcuts():
    count = 0
    for spot in countDict:
        (rowInd,colInd) = spot
        for d in twoDirections:
            if (rowInd+d[0],colInd+d[1]) in countDict:
                if countDict[(rowInd+d[0],colInd+d[1])] - countDict[spot] - 2 >= 100:
                    count += 1
    return count
print(getShortcuts())