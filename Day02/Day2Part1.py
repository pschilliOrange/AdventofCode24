with open('Day2/input.txt', 'r') as file:
    lines = file.readlines()
reports = []
for line in lines:
    report = [int(element) for element in line.split(' ')]
    reports.append(report)
acc = 0
safe = False
for report in reports:
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
    if safe:
        acc += 1
        print(report)
print(acc)