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
    copy1 = list(report)
    copy2 = list(report)
    if report[0] < report[1]:
        safe = True
        for i in range(1,len(report)):
            if report[i-1] >= report[i]:
                report.pop(i)
                safe = detIfSafe(report)
                break
            elif abs(report[i-1]-report[i]) >= 4:
                report.pop(i)
                safe = detIfSafe(report)
                break
    elif report[0] > report[1]:
        safe = True
        for i in range(1,len(report)):
            if report[i-1] <= report[i]:
                report.pop(i)
                safe = detIfSafe(report)
                break
            if abs(report[i-1]-report[i]) >= 4:
                report.pop(i)
                safe = detIfSafe(report)
                break
    copy1.pop(1)
    if not safe and detIfSafe(copy1):
        safe = True
        print(report)
        print(copy1)
    copy2.pop(0)
    if not safe and detIfSafe(copy2):
        safe = True
    if safe:
        acc += 1
print(acc)