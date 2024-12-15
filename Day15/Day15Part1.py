with open('Day15/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
instructions = []
map = []
directions = [(0,1),(1,0),(-1,0),(0,-1)]
for lineInd in range(len(lines)):
    line = lines[lineInd]
    if len(line) == 0:
        continue
    if line[0] == '#':
        map.append([])
        for i in range(len(lines[0])):
            map[lineInd].append(line[i])
        if '@' in line:
            ogPos = [len(map)-1, line.index('@')]
    elif line[0] == '<' or line[0] == '>' or line[0] == 'v' or line[0] == '^':
        for char in line:
            if char == '>':
                instructions.append(directions[0])
            elif char == 'v':
                instructions.append(directions[1])
            elif char == '^':
                instructions.append(directions[2])
            else:
                instructions.append(directions[3])

def findIfCanMove(pos,dir):
    newPos = [pos[0]+dir[0], pos[1]+dir[1]]
    if map[newPos[0]][newPos[1]] == '.':
        map[newPos[0]][newPos[1]] = map[pos[0]][pos[1]]
        map[pos[0]][pos[1]] = '.'
        return True
    elif map[newPos[0]][newPos[1]] == 'O':
        if findIfCanMove(newPos,dir):
            map[newPos[0]][newPos[1]] = map[pos[0]][pos[1]]
            map[pos[0]][pos[1]] = '.'
            return True
        else:
            return False
    elif map[newPos[0]][newPos[1]] == '#':
        return False

pos = ogPos
for instruction in instructions:
    if findIfCanMove(pos,instruction):
        pos = [pos[0]+instruction[0], pos[1]+instruction[1]]
acc = 0
for lineInd in range(len(map)):
    for charInd in range(len(map[0])):
        if map[lineInd][charInd] == 'O':
            acc += 100*lineInd + charInd
print(acc)