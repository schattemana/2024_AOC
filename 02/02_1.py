from itertools import pairwise
with open('02\input.txt') as f:
    lines = f.read().splitlines()
count = 0
for line in lines:
    inrange = False
    line_num = [int(item) for item in line.split()]
    for i, j in pairwise(line_num):
        diff = abs(i-j)
        if abs(i-j) > 0 and abs(i-j) <= 3:
            inrange = True
        else:
            inrange = False
            break
    if line_num == sorted(line_num, reverse=True) and inrange == True:
        count += 1
    elif line_num == sorted(line_num, reverse=False) and inrange == True:
        count += 1
    else:
        continue
print(count)

