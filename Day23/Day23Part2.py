with open('Day23/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
from collections import defaultdict

connections = {}
names = []
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
    if first not in names:
        names.append(first)
    if second not in names:
        names.append(second)
    

def neighbors(name):
    return set(connections[name])
maximalCliques = []

def bronKerbosch(inToBeMaximalClique,setToConsider,alreadyConsidered):
    if len(setToConsider) == 0 and len(alreadyConsidered) == 0:
        maximalCliques.append(inToBeMaximalClique)
        return
    else:
        for v in setToConsider:
            bronKerbosch(inToBeMaximalClique.union(set([v])),neighbors(v).intersection(setToConsider),neighbors(v).intersection(alreadyConsidered))
            setToConsider = setToConsider.difference(set([v]))
            alreadyConsidered = alreadyConsidered.union(set([v]))

bronKerbosch(set(), set(names), set())
max = 0
for clique in maximalCliques:
    if len(clique) > max:
        max = len(clique)
        maxClique = clique
print(",".join(sorted(maxClique)))
