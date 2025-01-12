with open('Day19/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
towelsAval = lines[0].split(', ')
patterns = []
for i in range(2,len(lines)):
    patterns.append(lines[i])

def returnIfPos(str):
    for towel in towelsAval:
        if len(towel) <= len(str) and towel == str[0:len(towel)]:
            if len(towel) == len(str):
                return True
            possible = returnIfPos(str[len(towel):])
            if possible:
                return True
    return False

count = 0
for pattern in patterns:
    if returnIfPos(pattern):
        count += 1
print(count)