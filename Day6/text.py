previouslyVisited = set()
loopFound = False
def moveGuard2(guardPos, dir):
    OGguardPos = guardPos
    rowInd = guardPos[0] + dir[0]
    colInd = guardPos[1] + dir[1]
    if rowInd >= 0 and rowInd < maxRowInd and colInd >= 0 and colInd < maxColInd:
        if lines[rowInd][colInd] != '#':
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
guardPos = initGuardPos
dir = (-1,0)
while inside:
    guardPos, dir, inside = moveGuard2(guardPos, dir)
    if (guardPos, dir) in previouslyVisited:
        return True