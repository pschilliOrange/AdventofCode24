with open('Day10/input.txt', 'r') as file:
    unpaddedLines = [line.strip() for line in file]
dot_row = '.' * (len(unpaddedLines[0]) + 2)
lines = [dot_row]
for line in unpaddedLines:
    lines.append('.' + line + '.')
lines.append(dot_row)

def isInt(element):
    try:
        int(element)
        return True
    except ValueError:
        return False

trailheads = []
for lineInd in range(len(lines)):
    for charInd in range(len(lines[0])):
        if isInt(lines[lineInd][charInd]) and int(lines[lineInd][charInd]) == 0:
            trailheads.append((lineInd, charInd))
directions = [(0,1),(1,0),(-1,0),(0,-1)]

def getNextInds(inds, ninesReached=None):
    if ninesReached is None: 
        ninesReached = set()
    acc = 0
    currNum = int(lines[inds[0]][inds[1]])
    nextInds = []
    lineInd = inds[0]
    charInd = inds[1]
    for direction in directions:
        element = lines[lineInd+direction[0]][charInd+direction[1]]
        if isInt(element) and int(element) == currNum + 1:
            element = int(element)
            if element == 9:
                ninesReached.add((lineInd+direction[0],charInd+direction[1]))
            else:
                nextInds.append((lineInd+direction[0],charInd+direction[1]))
    if not nextInds:
        return ninesReached
    else:
        for x in nextInds:  # Iterate over the next indices
            getNextInds(x, ninesReached)  # Recursively call for each
        return ninesReached  # Return the accumulated set

acc = 0
for trailhead in trailheads:
    ninesReached = set()
    ninesReached = getNextInds(trailhead)
    acc += len(ninesReached)
print(acc)