with open('Day18/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
size = 71
m = []
m.append([1]*(size+2))
for i in range(1, size + 1):
    m.append([])
    m[i].append(1)
    for j in range(size):
        m[i].append(0)
    m[i].append(1)
m.append([1]*(size+2))

squares = {}

def findMoves(inp):
    toReturn = []
    xInd = inp[0]
    yInd = inp[1]
    count = inp[2]
    for dir in directions:
        if m[xInd + dir[0]][yInd + dir[1]] == 0:
            if (xInd + dir[0], yInd + dir[1]) not in squares or squares[(xInd + dir[0], yInd + dir[1])] > count + 1:
                squares[(xInd + dir[0], yInd + dir[1])] = count + 1
                toReturn.append((xInd + dir[0], yInd + dir[1], count + 1))
    return toReturn

for lineInd in range(1023):
    line = lines[lineInd]
    firstInt = int(line.split(',')[0]) + 1
    secondInt = int(line.split(',')[1]) + 1
    m[secondInt][firstInt] = 1

for j in range(1024, len(lines)):
    line = lines[j]
    firstInt = int(line.split(',')[0]) + 1
    secondInt = int(line.split(',')[1]) + 1
    m[secondInt][firstInt] = 1
    if j > 1024 and (firstInt,secondInt) not in squares:
        continue

    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    squares = {}

    runners = []
    runners.append((1,1,0))
    while runners:
        currRunner = runners.pop()
        toAppend = findMoves(currRunner)
        runners += toAppend
    if (size,size) not in squares:
        ansInd = j
        break
print(lines[j])