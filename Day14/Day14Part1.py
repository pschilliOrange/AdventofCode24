with open('Day14/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
xLen = 101
yLen = 103
robots = []
for line in lines:
    pos = [int(line.split(' ')[0].split(',')[0].split('=')[1]), int(line.split(' ')[0].split(',')[1])]
    vel = [int(line.split(' ')[1].split(',')[0].split('=')[1]), int(line.split(' ')[1].split(',')[1])]
    robots.append([pos,vel])

for i in range(100):
    for robotInd in range(len(robots)):
        robot = robots[robotInd]
        robots[robotInd][0] = [(robot[0][0]+robot[1][0])%xLen, (robot[0][1]+robot[1][1])%yLen]

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
print(q1*q2*q3*q4)

