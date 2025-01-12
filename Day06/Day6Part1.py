with open('Day6/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
visited = set()
for lineInd in range(len(lines)):
    for charInd in range(len(lines[0])):
        if lines[lineInd][charInd] == '^':
            initGuardPos = (lineInd, charInd)
visited.add(initGuardPos)
maxRowInd = len(lines)
maxColInd = len(lines[0])

def moveGuard(guardPos, dir):
    rowInd = guardPos[0] + dir[0]
    colInd = guardPos[1] + dir[1]
    if rowInd >= 0 and rowInd < maxRowInd and colInd >= 0 and colInd < maxColInd:
        if lines[rowInd][colInd] != '#':
            inside = True
            guardPos = (rowInd, colInd)
            visited.add(guardPos)
            dir = dir
        else:
            dir = (dir[1], -dir[0])
            rowInd = guardPos[0] + dir[0]
            colInd = guardPos[1] + dir[1]
            if rowInd >= 0 and rowInd < maxRowInd and colInd >= 0 and colInd < maxColInd:
                inside = True
                guardPos = (rowInd, colInd)
                visited.add(guardPos)
                dir = dir
            else:
                inside = False
    else:
        inside = False
    return guardPos, dir, inside

inside = True
guardPos = initGuardPos
dir = (-1,0)
while inside:
    guardPos, dir, inside = moveGuard(guardPos, dir)
print(len(visited))

