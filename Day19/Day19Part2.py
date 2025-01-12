with open('Day19/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
towelsAval = lines[0].split(', ')
patterns = []
for i in range(2,len(lines)):
    patterns.append(lines[i])

prevChecked = {}

def returnIfPos(str, count):
    if str in prevChecked:
        return count + prevChecked[str]
    OGcount = count
    for towel in towelsAval:
        if len(towel) <= len(str) and towel == str[0:len(towel)]:
            if len(towel) == len(str):
                count += 1
            if len(towel) != len(str):
                count = returnIfPos(str[len(towel):], count)
    prevChecked[str] = count - OGcount
    return count
count = 0
for pattern in patterns:
    count = returnIfPos(pattern, count)
print(count)