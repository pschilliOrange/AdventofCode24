with open('Day13/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
from decimal import Decimal
def isInt(element):
    try:
        int(element)
        return True
    except ValueError:
        return False
    
def convertIfClose(num):
    if abs(num - round(num)) < 1e-2:
        if num > 0:
            return True, int(round(num))
    return False, -1

count = 0
cost = 0
for lineInd in range(0,len(lines),4):
    A = [int(lines[lineInd].split(',')[0].split('+')[1]), int(lines[lineInd].split(',')[1].split('+')[1])]
    B = [int(lines[lineInd+1].split(',')[0].split('+')[1]), int(lines[lineInd+1].split(',')[1].split('+')[1])]
    p = [int(lines[lineInd+2].split(',')[0].split('=')[1]), int(lines[lineInd+2].split(',')[1].split('=')[1])]
    [x1,y1] = A
    [x2,y2] = B
    [p1,p2] = p
    p1 += 10000000000000
    p2 += 10000000000000
    b = Decimal((-(p1*y1)/x1+p2)/(-(x2*y1)/x1+y2))
    a = Decimal((p1-b*x2)/x1)
    (agood, a) = convertIfClose(a)
    (bgood, b) = convertIfClose(b)
    if agood and bgood:
        if a*x1 + b*x2 == p1 and a*y1 + b*y2 == p2:
            cost += 3*int(a) + int(b)
            count += 1
print(cost)