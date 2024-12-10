with open('Day6/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
for lineInd in range(len(lines)):
    for charInd in range(len(lines[0])):
        if lines[lineInd][charInd] == '^':
            initGuardPos = (lineInd, charInd)
maxRowInd = len(lines)
maxColInd = len(lines[0])

def move90(dir):
    return (dir[1], -dir[0])

def moveGuard(guardPos, dir, added=(-1,-1)):
    loop = False
    rowInd = guardPos[0] + dir[0]
    colInd = guardPos[1] + dir[1]
    if rowInd >= 0 and rowInd < maxRowInd and colInd >= 0 and colInd < maxColInd:
        if lines[rowInd][colInd] != '#' and (rowInd,colInd) != added:
            inside = True
            guardPos = (rowInd, colInd)
        else:
            dir = move90(dir)
            inside = True
    else:
        inside = False
    return guardPos, dir, inside

def determineIfLoop(pos, dir, added):
    visitedWithDir = set()
    if added[0] >= 0 and added[0] < maxRowInd and added[1] >= 0 and added[1] < maxColInd:
        inside = True
        while inside:
            if (pos,dir) in visitedWithDir:
                return True
            visitedWithDir.add((pos,dir))
            pos, dir, inside = moveGuard(pos, dir, added)
    return False


loopCausers = set()
visited = set()
inside = True
guardPos = initGuardPos
dir = (-1,0)
while inside:
    if (guardPos[0]+dir[0], guardPos[1]+dir[1]) not in visited:
        if determineIfLoop(guardPos, dir, (guardPos[0]+dir[0], guardPos[1]+dir[1])):
            loopCausers.add((guardPos[0]+dir[0], guardPos[1]+dir[1]))
    visited.add(guardPos)
    guardPos, dir, inside = moveGuard(guardPos, dir)
if initGuardPos in loopCausers:
    loopCausers.remove(initGuardPos)
toRemove = []
for causer in loopCausers:
    if lines[causer[0]][causer[1]] == '#':
        toRemove.append(causer)
for s in toRemove:
    loopCausers.remove(s)
print(loopCausers)
print(len(loopCausers))