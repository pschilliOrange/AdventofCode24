with open('Day7/input.txt', 'r') as file:
    lines = [line.strip() for line in file]

equations = []
for line in lines:
    result = int(line.split(':')[0])
    nums = [int(x) for x in line.split(':')[1].split(' ')[1:]]
    equations.append([result, nums])

sumOfWorking = 0
for equation in equations:
    nums = equation[1]
    result = equation[0]
    numOperations = len(nums)-1
    for i in range(2**numOperations):
        base2 = bin(i)[2:]
        if len(base2) < numOperations:
            base2 = '0'*(numOperations-len(base2)) + base2
        acc = nums[0]
        for opInd in range(numOperations):
            if base2[opInd] == '0':
                acc += nums[1+opInd]
            else:
                acc = acc*nums[1+opInd]
        if acc == result:
            sumOfWorking += result
            break
print(sumOfWorking)