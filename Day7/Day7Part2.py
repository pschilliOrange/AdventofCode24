with open('Day7/input.txt', 'r') as file:
    lines = [line.strip() for line in file]

#copied from stack overflow
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))    

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
    for i in range(3**numOperations):
        base3 = str(ternary(i))
        if len(base3) < numOperations:
            base3 = '0'*(numOperations-len(base3)) + base3
        acc = nums[0]
        for opInd in range(numOperations):
            if base3[opInd] == '0':
                acc += nums[1+opInd]
            elif base3[opInd] == '1':
                acc = acc*nums[1+opInd]
            else:
                acc = int(str(acc)+str(nums[1+opInd]))
        if acc == result:
            sumOfWorking += result
            break
print(sumOfWorking)