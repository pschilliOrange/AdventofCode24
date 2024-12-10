with open('Day9/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
line = lines[0]
lst = []
freeSpaceTot = 0
for charInd in range(0,len(line),2):
    index = int(charInd/2)
    numNums = int(line[charInd])
    if charInd+1<len(line):
        numDots = int(line[charInd+1])
        freeSpaceTot += numDots
    else:
        numDots = 0
    for i in range(numNums):
        lst.append(index)
    for i in range(numDots):
        lst.append('.')
def lastIntBeforeInd(m):
    for i in range(m-1,-1,-1):
        if isinstance(lst[i], int):
            return i
frontInd = 0
backInd = len(lst)-1
newlst = []
for i in range(len(lst)):
    if backInd < i:
        break
    if isinstance(lst[i],int):
        newlst.append(lst[i])
    else:
        newlst.append(lst[backInd])
        backInd = lastIntBeforeInd(backInd)


#sloowwwww
# while (firstDotInd := lst.index('.')) <= len(lst) - 1 - freeSpaceTot:
#     lastIntInd = next((i for i, x in reversed(list(enumerate(lst))) if isinstance(x, int)), -1)
#     num = lst[lastIntInd]
#     lst[firstDotInd] = int(num)
#     lst[lastIntInd] = '.'

acc = 0
for i in range(len(newlst)):
    if isinstance(newlst[i], int):
        acc += i*newlst[i]
    else:
        break
print(acc)