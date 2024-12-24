with open('Day14/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
xLen = 101
yLen = 103
robots = []
safetyFactors = []
for line in lines:
    pos = [int(line.split(' ')[0].split(',')[0].split('=')[1]), int(line.split(' ')[0].split(',')[1])]
    vel = [int(line.split(' ')[1].split(',')[0].split('=')[1]), int(line.split(' ')[1].split(',')[1])]
    robots.append([pos,vel])

array = []
for i in range(xLen):
    array.append([])
    for j in range(yLen):
        array[i].append(0)
for robot in robots:
    array[robot[0][0]][robot[0][1]] += 1

for i in range(7916):
    for robotInd in range(len(robots)):
        robot = robots[robotInd]
        array[robot[0][0]][robot[0][1]] -= 1
        robots[robotInd][0] = [(robot[0][0]+robot[1][0])%xLen, (robot[0][1]+robot[1][1])%yLen]
        array[robots[robotInd][0][0]][robots[robotInd][0][1]] += 1

    xHalf = int((xLen-1)/2)
    yHalf = int((yLen-1)/2)
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for robot in robots:
        if robot[0][0] < xHalf and robot[0][1] < yHalf:
            q1 += 1
        elif robot[0][0] > xHalf and robot[0][1] < yHalf:
            q2 += 1
        elif robot[0][0] < xHalf and robot[0][1] > yHalf:
            q3 += 1
        elif robot[0][0] > xHalf and robot[0][1] > yHalf:
            q4 += 1
    safetyFactors.append(q1*q2*q3*q4)

print(safetyFactors.index(min(safetyFactors)))
with open("output.txt", "w") as f:
    for line in array:
        for char in line:
            if char > 0:
                f.write(str(char))
            else:
                f.write('.')
        f.write("\n")
print(i+1)

    # array = []
    # for i in range(yLen):
    #     array.append([])
    #     for j in range(xLen):
    #         char = '.'
    #         for robot in robots:
    #             if robot[0] == [j,i]:
    #                 char = '0'
    #                 break
    #         array[i].append(char)
    
# with open("output.txt", "w") as f:
#     for line in array:
#         for char in line:
#             f.write(char)
#         f.write("\n")
#     breakpoint = 1

