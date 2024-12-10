with open('Day8/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
antenna = {}
for lineInd in range(len(lines)):
    for charInd in range(len(lines[0])):
        element = lines[lineInd][charInd]
        if element != '.' and element != '#':
            if element not in antenna:
                antenna[element] = [(lineInd, charInd)]
            else:
                antenna[element].append((lineInd, charInd))
maxRowInd = len(lines)
maxColInd = len(lines[0])
listOfAntis = []

def calcAntinode(first, second):
    (x1, y1) = first
    (x2, y2) = second
    diffVec = (x2-x1, y2-y1)
    acc = 0
    currVec = second
    stillIn = True
    while stillIn:
        if currVec[0] >= 0 and currVec[0] < maxRowInd and currVec[1] >= 0 and currVec[1] < maxColInd:
            if currVec not in listOfAntis:
                listOfAntis.append(currVec)
                acc += 1
            currVec = (currVec[0]+diffVec[0], currVec[1]+diffVec[1])
        else:
            stillIn = False
    currVec = first
    stillIn = True
    while stillIn:
        if currVec[0] >= 0 and currVec[0] < maxRowInd and currVec[1] >= 0 and currVec[1] < maxColInd:
            if currVec not in listOfAntis:
                listOfAntis.append(currVec)
                acc += 1
            currVec = (currVec[0]-diffVec[0], currVec[1]-diffVec[1])
        else:
            stillIn = False
    return acc

acc = 0
for type in antenna:
    for firstInd in range(len(antenna[type])):
        for secondInd in range(firstInd +1, len(antenna[type])):
            acc += calcAntinode(antenna[type][firstInd], antenna[type][secondInd])
print(acc)