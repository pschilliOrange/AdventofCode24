with open('Day2/input.txt', 'r') as file:
    lines = file.readlines()
reports = []
for line in lines:
    report = [int(element) for element in line.split(' ')]
    reports.append(report)
acc = 0
safe = False

def detIfSafe(report):
    safe = False
    if report[0] < report[1]:
        safe = True
        for i in range(1,len(report)):
            if report[i-1] >= report[i]:
                safe = False
                break
            if abs(report[i-1]-report[i]) >= 4:
                safe = False
                break
    elif report[0] > report[1]:
        safe = True
        for i in range(1,len(report)):
            if report[i-1] <= report[i]:
                safe = False
                break
            if abs(report[i-1]-report[i]) >= 4:
                safe = False
                break
    return safe


for report in reports:
    safe = False
    if detIfSafe(report):
        safe = True
    elif detIfSafe(report[1:]):
        safe = True
    elif detIfSafe(report[0:len(report)]):
        safe = True
    else:
        for i in range(len(report)):
            if detIfSafe(report[0:i]+report[i+1:]):
                safe = True
                break
    if safe:
        acc += 1
print(acc)