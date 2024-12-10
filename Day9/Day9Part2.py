with open('Day9/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
lst = [int(x) for x in lines[0]]
lst.append(0)
m = 0
for i in range(0,len(lst),2):
    lst[i] = [lst[i], int(i/2)]
    m = int(i/2)
for ind in range(m,-1,-1):
    for posNextInd in range(len(lst)-2,-1,-2):
        if lst[posNextInd][1] == ind:
            lenGroupInd = posNextInd 
            break
    lenGroup = lst[lenGroupInd][0]
    indexGroup = lst[lenGroupInd][1]
    for freeSpaceLenInd in range(1,lenGroupInd,2):
        freeSpaceLen = lst[freeSpaceLenInd]
        if freeSpaceLen >= lenGroup:
            if freeSpaceLenInd != lenGroupInd - 1:
                lst[freeSpaceLenInd] = 0
                lst[lenGroupInd-1] = lst[lenGroupInd-1] + lst[lenGroupInd][0] + lst[lenGroupInd+1]
                del lst[lenGroupInd+1]
                del lst[lenGroupInd]
                lst.insert(freeSpaceLenInd+1,freeSpaceLen-lenGroup)
                lst.insert(freeSpaceLenInd+1,[lenGroup, indexGroup])
                break
            else:
                lst[freeSpaceLenInd] = 0
                lst[lenGroupInd+1] = freeSpaceLen + lst[lenGroupInd+1]
acc = 0
ind = 0
for i in range(len(lst)):
    if i % 2 == 0:
        for j in range(lst[i][0]):
            acc += ind*lst[i][1]
            ind += 1
    else:
        ind += lst[i]
print(acc)