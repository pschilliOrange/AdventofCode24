with open('Day16/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
for lineInd in range(len(lines)):
    for charInd in range(len(lines[0])):
        if lines[lineInd][charInd] == 'S':
            start = (lineInd, charInd)
        elif lines[lineInd][charInd] == 'E':
            end = (lineInd, charInd)
squaresWithDir = {}

directions = [(0,1),(1,0),(-1,0),(0,-1)]
def getNextPos(pos,facing,acc):
    nextPos = []
    for dir in directions:
        if lines[pos[0]+dir[0]][pos[1]+dir[1]] == '.':
            if dir == facing:
                if ((pos[0]+dir[0],pos[1]+dir[1]),dir) not in squaresWithDir or acc+1<squaresWithDir[((pos[0]+dir[0],pos[1]+dir[1]),dir)]:
                    nextPos.append([[pos[0]+dir[0], pos[1]+dir[1]], dir, acc+1])
                    squaresWithDir[((pos[0]+dir[0],pos[1]+dir[1]),dir)] = acc + 1
            else:
                if ((pos[0]+dir[0],pos[1]+dir[1]),dir) not in squaresWithDir or acc+1001<squaresWithDir[((pos[0]+dir[0],pos[1]+dir[1]),dir)]:
                    nextPos.append([[pos[0]+dir[0], pos[1]+dir[1]], dir, acc+1001])
                    squaresWithDir[((pos[0]+dir[0],pos[1]+dir[1]),dir)] = acc + 1001
        elif lines[pos[0]+dir[0]][pos[1]+dir[1]] == 'E':
            if dir == facing:                    
                if ((pos[0]+dir[0],pos[1]+dir[1]),dir) not in squaresWithDir or acc+1<squaresWithDir[((pos[0]+dir[0],pos[1]+dir[1]),dir)]:
                    squaresWithDir[((pos[0]+dir[0],pos[1]+dir[1]),dir)] = acc + 1
            else:
                if ((pos[0]+dir[0],pos[1]+dir[1]),dir) not in squaresWithDir or acc+1001<squaresWithDir[((pos[0]+dir[0],pos[1]+dir[1]),dir)]:
                    squaresWithDir[((pos[0]+dir[0],pos[1]+dir[1]),dir)] = acc + 1001
    return nextPos
runners = []
runners.append([start,directions[0],0])
while runners:
    currRunner = runners.pop()
    toAppend = getNextPos(currRunner[0], currRunner[1], currRunner[2])
    runners += toAppend
    # if len(runners) > 10:
    #     break
    # # print(len(runners))
min = 10010000000
for dir in directions:
    if (end,dir) in squaresWithDir and squaresWithDir[(end,dir)] < min:
        min = squaresWithDir[(end,dir)]
print(min)
