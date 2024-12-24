with open('Day22/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
import math

def mix(num1, num2):
    return num1 ^ num2
def prune(num):
    return num % 16777216
def nextSecret(num):
    num = prune(mix(num,num*64))
    num = prune(mix(num,math.floor(num/32)))
    num = prune(mix(num,num*2048))
    return num

iterations = 2000
acc = 0
differences = []
prices = []
for lineInd in range(len(lines)):
    line = lines[lineInd]
    differences.append([])
    prices.append([])
    num = int(line)
    prevPrice = num % 10
    for i in range(iterations):
        num = nextSecret(num)
        differences[lineInd].append(num % 10 - prevPrice)
        prices[lineInd].append(num % 10)
        prevPrice = num % 10
    acc += num
def getBanana(tup):
    bCount = 0
    for lineInd in range(len(lines)):
        for i in range(3,2000):
            toCheck = (differences[lineInd][i-3], differences[lineInd][i-2], differences[lineInd][i-1], differences[lineInd][i])
            if toCheck == tup:
                bCount += prices[lineInd][i]
                break
    return bCount

sequenceToBanana = {}
for lineInd in range(len(lines)):
    for i in range(3,2000):
        tup = (differences[lineInd][i-3], differences[lineInd][i-2], differences[lineInd][i-1], differences[lineInd][i])
        if tup not in sequenceToBanana:          
            sequenceToBanana[tup] = getBanana(tup)
max = 0
for key in sequenceToBanana:
    if sequenceToBanana[key] > max:
        max = sequenceToBanana[key]
with open("output.txt", "w") as file:
    file.write(str(max))