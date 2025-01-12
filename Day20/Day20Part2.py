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
countList = []
def findShortest(start, end):
    count = 0
    notEnd = True
    curr = start
    past = (0,0)
    while notEnd:
        nextMoves = 0
        countList.append(curr)
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
findShortest(start,end)
countList.append(end)

minSaving = 100
count = 0
for spotInd in range(len(countList)):
    curr = countList[spotInd]
    for endCheatInd in range(spotInd+minSaving,len(countList)):
        potEndCheat = countList[endCheatInd]
        dist = abs(curr[0]-potEndCheat[0]) + abs(curr[1] - potEndCheat[1])
        if dist <= 20 and endCheatInd - spotInd - dist >= minSaving:
            count += 1
print(count)