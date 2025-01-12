with open('Day4/input.txt', 'r') as file:
    unpaddedLines = file.readlines()
dot_row = '.' * (len(unpaddedLines[0].strip()) + 2)
lines = [dot_row]
for line in unpaddedLines:
    lines.append('.' + line.strip() + '.')
lines.append(dot_row)

def isCross_masAt(rowInd, colInd):
    directions = [
        (1, 1), 
        (1, -1)    
    ]
    crossFound = True
    word1 = ['M','A','S']
    word2 = ['S','A','M']
    word1Found = True
    word2Found = True
    for i in range(3):
        (dx, dy) = directions[0]
        if word1[i] != lines[rowInd + i*dx][colInd + i*dy]:
            word1Found = False
        if word2[i] != lines[rowInd + i*dx][colInd + i*dy]:
            word2Found = False
    if not word1Found and not word2Found:
        return 0
    
    colInd = colInd + 2
    word1Found = True
    word2Found = True
    for i in range(3):
        (dx, dy) = directions[1]
        word1Found = True
        if word1[i] != lines[rowInd + i*dx][colInd + i*dy]:
            word1Found = False
        word2Found = True
        if word2[i] != lines[rowInd + i*dx][colInd + i*dy]:
            word2Found = False
    if not word1Found and not word2Found:
        return 0
    return 1
count = 0
for lineInd in range(len(lines) - 2):
    for charInd in range(len(lines[0]) - 2):
        count += isCross_masAt(lineInd, charInd)
        if isCross_masAt(lineInd, charInd) > 0:
            print(lineInd, charInd)
print(count)