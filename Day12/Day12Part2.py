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

def getSides(group):
    rowSideCount = 0
    for colInd in range(len(lines[0])):
        perimSquaresInCol = [x for x in group if x[1] == colInd and (x[0],x[1]-1) not in group]
        while perimSquaresInCol:
            currSquare = perimSquaresInCol.pop()
            currLineInd = currSquare[0] + 1
            while (currLineInd, colInd) in perimSquaresInCol:
                perimSquaresInCol.remove((currLineInd,colInd))
                currLineInd += 1
            currLineInd = currSquare[0] - 1
            while (currLineInd, colInd) in perimSquaresInCol:
                perimSquaresInCol.remove((currLineInd,colInd))
                currLineInd -= 1
            rowSideCount += 1
    for colInd in range(len(lines[0])):
        perimSquaresInCol = [x for x in group if x[1] == colInd and (x[0],x[1]+1) not in group]
        while perimSquaresInCol:
            currSquare = perimSquaresInCol.pop()
            currLineInd = currSquare[0] + 1
            while (currLineInd, colInd) in perimSquaresInCol:
                perimSquaresInCol.remove((currLineInd,colInd))
                currLineInd += 1
            currLineInd = currSquare[0] - 1
            while (currLineInd, colInd) in perimSquaresInCol:
                perimSquaresInCol.remove((currLineInd,colInd))
                currLineInd -= 1
            rowSideCount += 1
    
    colSideCount = 0 
    for rowInd in range(len(lines)):
        perimSquaresInRow = [x for x in group if x[0] == rowInd and (x[0]-1,x[1]) not in group]
        while perimSquaresInRow:
            currSquare = perimSquaresInRow.pop()
            currColInd = currSquare[1] + 1
            while (rowInd, currColInd) in perimSquaresInRow:
                perimSquaresInRow.remove((rowInd, currColInd))
                currColInd += 1
            currColInd = currSquare[1] - 1
            while (rowInd, currColInd) in perimSquaresInRow:
                perimSquaresInRow.remove((rowInd, currColInd))
                currColInd -= 1
            colSideCount += 1
    for rowInd in range(len(lines)):
        perimSquaresInRow = [x for x in group if x[0] == rowInd and (x[0]+1,x[1]) not in group]
        while perimSquaresInRow:
            currSquare = perimSquaresInRow.pop()
            currColInd = currSquare[1] + 1
            while (rowInd, currColInd) in perimSquaresInRow:
                perimSquaresInRow.remove((rowInd, currColInd))
                currColInd += 1
            currColInd = currSquare[1] - 1
            while (rowInd, currColInd) in perimSquaresInRow:
                perimSquaresInRow.remove((rowInd, currColInd))
                currColInd -= 1
            colSideCount += 1
    return colSideCount + rowSideCount

acc = 0
for group in groups:
    area = len(group)
    perimeter = getSides(group)
    acc += area*perimeter
print(acc)
