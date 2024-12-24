with open('Day23/input.txt', 'r') as file:
    lines = [line.strip() for line in file]

connections = {}
for line in lines:
    first = line.split('-')[0]
    second = line.split('-')[1]
    if first not in connections:
        connections[first] = []
        connections[first].append(second)
    elif second not in connections[first]:
        connections[first].append(second)
    if second not in connections:
        connections[second] = []
        connections[second].append(first)
    elif first not in connections[second]:
        connections[second].append(first)
setOfSets = set()
acc = 0
for key1 in connections:
    for key2 in connections:
        for key3 in connections:
            if key1 != key2 and key1 != key3 and key2 != key3:
                if key3 in connections[key1] and key2 in connections[key1]:
                    if key3 in connections[key2]:
                        if 't' == key1[0] or 't' == key2[0] or 't' == key3[0]:
                            acc += 1
print(acc/6)