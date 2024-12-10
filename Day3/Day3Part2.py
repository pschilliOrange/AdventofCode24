with open('Day3/input.txt', 'r') as file:
    text = file.read()
acc = 0
do = True
for charInd in range(len(text)):

    if text[charInd] == 'd' and text[charInd+1] == 'o' and text[charInd+2] == '(' and text[charInd+3] == ')':
        do = True
    if text[charInd] == 'd' and text[charInd+1] == 'o' and text[charInd+2] == 'n' and text[charInd+3] == "'" and text[charInd+4] == 't' and text[charInd+5] == '(' and text[charInd+6] == ')':
        do = False
    if not do:
        continue
    if text[charInd] == 'm' and text[charInd+1] == 'u' and text[charInd+2] == 'l' and text[charInd+3] == '(':
        firstNumStart = charInd + 4
        running = firstNumStart
        firstNum = []
        while text[running].isdigit():
            firstNum.append(text[running])
            running += 1
        if len(firstNum) >= 4:
            continue
        if text[running] != ',':
            continue
        running += 1
        secondNum = []
        while text[running].isdigit():
            secondNum.append(text[running])
            running += 1
        if text[running] != ')':
            continue
        prod = int(''.join(firstNum))*int(''.join(secondNum))
        acc += prod
print(acc)