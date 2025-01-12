with open('Day5/input.txt', 'r') as file:
    lines = file.readlines()
blankInd = next(i for i, line in enumerate(lines) if line.strip() == "")
rules = [line.strip() for line in lines[:blankInd]]
updates = [line.strip() for line in lines[blankInd+1:]]
lst = []
dict = {}
for rule in rules:
    firstNum, secondNum = rule.strip().split('|')
    firstNum = int(firstNum)
    secondNum = int(secondNum)
    if firstNum in dict:
        dict[firstNum].append(secondNum)
    else:
        dict[firstNum] = [secondNum]
def reorder(nums):
    if len(nums) == 1:
        return nums
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[j] in dict:
                if nums[i] in dict[nums[j]]:
                    nums.insert(j+1, nums[i])
                    nums[j+1:] = reorder(nums[j+1:])
                    nums.pop(i)
                    break
    return nums

acc = 0
for update in updates:
    nums = [int(i) for i in update.strip().split(',')]
    safe = True
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[j] in dict:
                if nums[i] in dict[nums[j]]:
                    safe = False
                    break
        if not safe:
            break
    if not safe:
        nums = reorder(nums)
        middleInd = int((len(nums)-1)/2)
        middleNum = nums[middleInd]
        acc += middleNum
print(acc)