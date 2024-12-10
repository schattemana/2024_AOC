from itertools import pairwise
with open('02\input.txt') as f:
    lines = f.read().splitlines()
linenums = []

for line in lines:
    line_num = [int(item) for item in line.split()]
    linenums.append(line_num)

count = 0
def linecheck(line_num):
    inrange = False
    for i, j in pairwise(line_num):
        if abs(i-j) > 0 and abs(i-j) <= 3:
            inrange = True
        else:
            inrange = False
            break
    if line_num == sorted(line_num, reverse=True) and inrange == True:
        return True
    elif line_num == sorted(line_num, reverse=False) and inrange == True:
        return True
    else:
        return False

#werkte van de eerste keer?????
count = 0
for line in linenums:
    if linecheck(line):
        count += 1
    else:
        for i in range(len(line)):
            testline = line[:]
            testline = line[:i] + line[i+1:]
            if linecheck(testline):
                count += 1
                break
            else:
                continue
print(count)  