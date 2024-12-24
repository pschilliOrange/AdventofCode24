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
for line in lines:
    num = int(line)
    for i in range(iterations):
        num = nextSecret(num)
    acc += num
print(acc)