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
    firstAnti = (x2+diffVec[0], y2+diffVec[1])
    secondAnti = (x1-diffVec[0], y1-diffVec[1])
    acc = 0
    if firstAnti[0] >= 0 and firstAnti[0] < maxRowInd and firstAnti[1] >= 0 and firstAnti[1] < maxColInd:
        # print(firstAnti)
        if firstAnti not in listOfAntis:
            listOfAntis.append(firstAnti)
            acc += 1
    if secondAnti[0] >= 0 and secondAnti[0] < maxRowInd and secondAnti[1] >= 0 and secondAnti[1] < maxColInd:
        if secondAnti not in listOfAntis:
            listOfAntis.append(secondAnti)
            acc += 1
    return acc

acc = 0
for type in antenna:
    for firstInd in range(len(antenna[type])):
        for secondInd in range(firstInd +1, len(antenna[type])):
            acc += calcAntinode(antenna[type][firstInd], antenna[type][secondInd])
print(acc)
