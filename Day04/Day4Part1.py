with open('Day4/input.txt', 'r') as file:
    unpaddedLines = file.readlines()
dot_row = '.' * (len(unpaddedLines[0]) + 2)
lines = [dot_row]
for line in unpaddedLines:
    lines.append('.' + line + '.')
lines.append(dot_row)

def isXmasAt(rowInd, colInd):
    count = 0
    directions = [
        (-1, 0),
        (1, 0),   
        (0, -1),  
        (0, 1),   
        (-1, -1), 
        (-1, 1),  
        (1, -1),  
        (1, 1)    
    ]
    for direction in directions:
        wordFoundInDirection = True
        (dx, dy) = direction
        word = ['X','M','A','S']
        for i in range(4):
            if word[i] != lines[rowInd + i*dx][colInd + i*dy]:
                wordFoundInDirection = False
                break
        if wordFoundInDirection:
            count += 1
    return count
count = 0
for lineInd in range(len(lines)):
    for charInd in range(len(line)):
        count += isXmasAt(lineInd, charInd)
print(count)