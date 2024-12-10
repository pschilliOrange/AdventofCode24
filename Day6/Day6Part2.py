with open('Day6/sample.txt', 'r') as file:
    lines = [line.strip() for line in file]
loopCausers = set()
visitedWithDir = set()
for lineInd in range(len(lines)):
    for charInd in range(len(lines[0])):
        if lines[lineInd][charInd] == '^':
            initGuardPos = (lineInd, charInd)
visitedWithDir.add((initGuardPos, (-1,0)))
maxRowInd = len(lines)
maxColInd = len(lines[0])

def determineIfLoop(newLines, currPos, currDir):
    previouslyVisited = set()
    previouslyVisited.add((currPos, currDir))
    def moveGuard2(guardPos, dir):
        rowInd = guardPos[0] + dir[0]
        colInd = guardPos[1] + dir[1]
        if rowInd >= 0 and rowInd < maxRowInd and colInd >= 0 and colInd < maxColInd:
            if newLines[rowInd][colInd] != '#':
                inside = True
                guardPos = (rowInd, colInd)
                previouslyVisited.add((guardPos, dir))
                dir = dir
            else:
                dir = (dir[1], -dir[0])
                rowInd = guardPos[0] + dir[0]
                colInd = guardPos[1] + dir[1]
                if rowInd >= 0 and rowInd < maxRowInd and colInd >= 0 and colInd < maxColInd:
                    inside = True
                    guardPos = (rowInd, colInd)
                    previouslyVisited.add((guardPos, dir))
                    dir = dir
                else:
                    inside = False
        else:
            inside = False
        return guardPos, dir, inside

    inside = True
    guardPos = currPos
    dir = currDir
    while inside:
        guardPos, dir, inside = moveGuard2(guardPos, dir)
        if (guardPos, dir) in previouslyVisited:
            return True
    return False


def moveGuard(guardPos, dir):
    OGguardPos = guardPos
    rowInd = guardPos[0] + dir[0]
    colInd = guardPos[1] + dir[1]
    if rowInd >= 0 and rowInd < maxRowInd and colInd >= 0 and colInd < maxColInd:
        if lines[rowInd][colInd] != '#':
            inside = True
            guardPos = (rowInd, colInd)
            dir = dir
            posDir = (dir[1], -dir[0])
            newLines = list(lines)
            if determineIfLoop(lines, OGguardPos, posDir):
                loopCausers.add(guardPos)
            visitedWithDir.add((guardPos, dir))
        else:
            dir = (dir[1], -dir[0])
            rowInd = guardPos[0] + dir[0]
            colInd = guardPos[1] + dir[1]
            if rowInd >= 0 and rowInd < maxRowInd and colInd >= 0 and colInd < maxColInd:
                inside = True
                guardPos = (rowInd, colInd)
                visitedWithDir.add((guardPos, dir))
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

print(len(loopCausers))
print(loopCausers)
print(determineIfLoop())