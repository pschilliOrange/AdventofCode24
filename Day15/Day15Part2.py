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
            if line[i] == 'O':
                map[lineInd].append('[')
                map[lineInd].append(']')
            elif line[i] == '@':
                map[lineInd].append('@')
                map[lineInd].append('.')
            else:
                map[lineInd].append(line[i])
                map[lineInd].append(line[i])
        if '@' in line:
            ogPos = [len(map)-1, map[lineInd].index('@')]
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

def findIfCanMoveLeftRight(pos,dir):
    newPos = [pos[0]+dir[0], pos[1]+dir[1]]
    if map[newPos[0]][newPos[1]] == '.':
        map[newPos[0]][newPos[1]] = map[pos[0]][pos[1]]
        map[pos[0]][pos[1]] = '.'
        return True
    elif map[newPos[0]][newPos[1]] == '#':
        return False
    else:
        if findIfCanMoveLeftRight(newPos,dir):
            map[newPos[0]][newPos[1]] = map[pos[0]][pos[1]]
            map[pos[0]][pos[1]] = '.'
            return True
        else:
            return False

def findIfCanMoveUpDown(pos1,pos2,dir,move):
    newPos1 = [pos1[0]+dir[0], pos1[1]+dir[1]]
    newPos2 = [pos2[0]+dir[0], pos2[1]+dir[1]]
    if map[newPos1[0]][newPos1[1]] == '.' and map[newPos2[0]][newPos2[1]] == '.':
        if move:
            map[newPos1[0]][newPos1[1]] = '['
            map[newPos2[0]][newPos2[1]] = ']'
            map[pos1[0]][pos1[1]] = '.'
            map[pos2[0]][pos2[1]] = '.'
        return True
    elif map[newPos1[0]][newPos1[1]] == '#' or map[newPos2[0]][newPos2[1]] == '#':
        return False
    elif map[newPos1[0]][newPos1[1]] == '[' and map[newPos2[0]][newPos2[1]] == ']':
        if findIfCanMoveUpDown(newPos1,newPos2,dir,move):
            if move:
                map[newPos1[0]][newPos1[1]] = '['
                map[newPos2[0]][newPos2[1]] = ']'
                map[pos1[0]][pos1[1]] = '.'
                map[pos2[0]][pos2[1]] = '.'
            return True
        else:
            return False
    elif map[newPos1[0]][newPos1[1]] == ']' and map[newPos2[0]][newPos2[1]] == '.':
        if findIfCanMoveUpDown([newPos1[0], newPos1[1]-1],[newPos1[0], newPos1[1]],dir,move):
            if move:
                map[newPos1[0]][newPos1[1]] = '['
                map[newPos2[0]][newPos2[1]] = ']'
                map[pos1[0]][pos1[1]] = '.'
                map[pos2[0]][pos2[1]] = '.'
            return True
        else:
            return False
    elif map[newPos1[0]][newPos1[1]] == '.' and map[newPos2[0]][newPos2[1]] == '[':
        if findIfCanMoveUpDown([newPos2[0], newPos2[1]],[newPos2[0], newPos2[1]+1],dir,move):
            if move:
                map[newPos1[0]][newPos1[1]] = '['
                map[newPos2[0]][newPos2[1]] = ']'
                map[pos1[0]][pos1[1]] = '.'
                map[pos2[0]][pos2[1]] = '.'
            return True
        else:
            return False
    elif map[newPos1[0]][newPos1[1]] == ']' and map[newPos2[0]][newPos2[1]] == '[':
        if findIfCanMoveUpDown([newPos1[0], newPos1[1]-1],[newPos1[0], newPos1[1]],dir,move) and findIfCanMoveUpDown([newPos2[0], newPos2[1]],[newPos2[0], newPos2[1]+1],dir,move):
            if move:
                map[newPos1[0]][newPos1[1]] = '['
                map[newPos2[0]][newPos2[1]] = ']'
                map[pos1[0]][pos1[1]] = '.'
                map[pos2[0]][pos2[1]] = '.'
            return True
        else:
            return False

def findIfRobotCanMove(pos1,dir,move):
    newPos1 = [pos1[0]+dir[0], pos1[1]+dir[1]]
    if map[newPos1[0]][newPos1[1]] == '.':
        if move:
            map[newPos1[0]][newPos1[1]] = map[pos1[0]][pos1[1]]
            map[pos1[0]][pos1[1]] = '.'
        return True
    elif map[newPos1[0]][newPos1[1]] == '#':
        return False
    else:
        if map[newPos1[0]][newPos1[1]] == '[':
            newPos2 = [newPos1[0], newPos1[1]+1]
            if findIfCanMoveUpDown(newPos1,newPos2,dir,move):
                if move:
                    map[newPos1[0]][newPos1[1]] = map[pos1[0]][pos1[1]]
                    map[pos1[0]][pos1[1]] = '.'
                return True
            else:
                return False
        elif map[newPos1[0]][newPos1[1]] == ']':
            newPos2 = [newPos1[0], newPos1[1]-1]
            if findIfCanMoveUpDown(newPos2,newPos1,dir,move):
                if move:
                    map[newPos1[0]][newPos1[1]] = map[pos1[0]][pos1[1]]
                    map[pos1[0]][pos1[1]] = '.'
                return True
            else:
                return False

pos = ogPos
for instruction in instructions:
    if instruction == (1,0) or instruction == (-1,0):
        if findIfRobotCanMove(pos,instruction,False):
            findIfRobotCanMove(pos,instruction,True)
            pos = [pos[0]+instruction[0], pos[1]+instruction[1]]
    else:
        if findIfCanMoveLeftRight(pos,instruction):
            pos = [pos[0]+instruction[0], pos[1]+instruction[1]]
acc = 0
for lineInd in range(len(map)):
    for charInd in range(len(map[0])):
        if map[lineInd][charInd] == '[':
            acc += 100*lineInd + charInd
print(acc)