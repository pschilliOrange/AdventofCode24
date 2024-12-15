with open('Day12/input.txt', 'r') as file:
    unpaddedLines = [line.strip() for line in file]
dot_row = '.' * (len(unpaddedLines[0]) + 2)
lines = [dot_row]
for line in unpaddedLines:
    lines.append('.' + line + '.')
lines.append(dot_row)


directions = [(0,1),(1,0),(-1,0),(0,-1)]
groups = []
inSomeGroup = set()
for lineInd in range(len(lines)):
    for charInd in range(len(lines[0])):
        if (lineInd,charInd) not in inSomeGroup and lines[lineInd][charInd] != '.':
            currGroup = []
            neighbors = []
            neighbors.append((lineInd,charInd))
            while neighbors:
                currSquare = neighbors.pop()
                currGroup.append(currSquare)
                inSomeGroup.add(currSquare)
                for dir in directions:
                    if lines[currSquare[0]+dir[0]][currSquare[1]+dir[1]] == lines[currSquare[0]][currSquare[1]] and (currSquare[0]+dir[0],currSquare[1]+dir[1]) not in neighbors and (currSquare[0]+dir[0],currSquare[1]+dir[1]) not in currGroup:
                        neighbors.append((currSquare[0]+dir[0],currSquare[1]+dir[1]))
            groups.append(currGroup)

def getPerimeter(group):
    rowCount = 0
    currentlyIn = False
    for lineInd in range(len(lines)):
        for colInd in range(len(lines[0])):
            if (lineInd, colInd) in group and not currentlyIn:
                currentlyIn = True
                rowCount += 1
            elif (lineInd, colInd) not in group and currentlyIn:
                currentlyIn = False
                rowCount += 1
    
    colCount = 0
    currentlyIn = False
    for colInd in range(len(lines[0])):
        for lineInd in range(len(lines)):
            if (lineInd, colInd) in group and not currentlyIn:
                currentlyIn = True
                colCount += 1
            elif (lineInd, colInd) not in group and currentlyIn:
                currentlyIn = False
                colCount += 1
    return colCount + rowCount

acc = 0
for group in groups:
    area = len(group)
    perimeter = getPerimeter(group)
    acc += area*perimeter
print(acc)
