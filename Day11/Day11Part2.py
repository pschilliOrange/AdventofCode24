nums = [[6571,1], [0,1], [5851763,1], [526746,1], [23,1], [69822,1], [9,1], [989,1]]
print(nums[1][0])
for blinkInd in range(75):
    for i in range(len(nums)-2,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[i][0] == nums[j][0]:
                nums[i][1] += nums[j][1]
                nums.pop(j)
                break
    ogLenAfterBlink = len(nums)
    for numInd in range(ogLenAfterBlink-1,-1,-1):
        if nums[numInd][0] == 0:
            nums[numInd][0] = 1
        elif len(string := str(nums[numInd][0])) % 2 == 0:
            numNums = nums[numInd][1]
            firstHalf = int(string[0:int(len(string)/2)])
            secondHalf = int(string[int(len(string)/2):])
            nums[numInd] = [firstHalf,numNums]
            nums.insert(numInd+1, [secondHalf,numNums])
        else:
            nums[numInd] = [nums[numInd][0]*2024,nums[numInd][1]]
acc = 0
for i in range(len(nums)):
    acc += nums[i][1]
print(acc)