nums = [6571, 0, 5851763, 526746, 23, 69822, 9, 989]
for blinkInd in range(25):
    ogLenAfterBlink = len(nums)
    for numInd in range(ogLenAfterBlink-1,-1,-1):
        if nums[numInd] == 0:
            nums[numInd] = 1
        elif len(string := str(nums[numInd])) % 2 == 0:
            firstHalf = int(string[0:int(len(string)/2)])
            secondHalf = int(string[int(len(string)/2):])
            nums[numInd] = firstHalf
            nums.insert(numInd+1, secondHalf)
        else:
            nums[numInd] = nums[numInd]*2024
print(len(nums))