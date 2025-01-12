with open('Day1/input.txt', 'r') as file:
    lines = file.readlines()
firstList = []
secondList = []
for line in lines:
    firstList.append(int(line[0:6]))
    secondList.append(int(line[7:13]))
def getSimilarity(list1, list2):
    acc = 0
    for i in range(len(list1)):
        currentNum = list1[i]
        occurences = list2.count(currentNum)
        acc += occurences*currentNum
    return acc

def orderList(lst):
    orderedList = [lst[0]]
    length = len(lst)
    for i in range(1,length):
        numToInsert = lst[i]
        for j in range(i):
            numToCompare = orderedList[j]
            if numToInsert <= numToCompare:
                orderedList.insert(j, numToInsert)
                break
        else:
            orderedList.append(numToInsert)
    return orderedList
def getDif(list1, list2):
    acc = 0
    for i in range(len(list1)):
        acc += abs(list1[i]-list2[i])
    return(acc)
print(getSimilarity(firstList, secondList))