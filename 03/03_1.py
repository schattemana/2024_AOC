import re
with open('03\input.txt') as f:
    lines = f.read().splitlines()
total = 0
for line in lines:
    all_mul = [m.start() for m in re.finditer("mul", line)]
    for muldex in all_mul:
        if line[muldex +3] == "(":
            closed=line[muldex+3:].find(")")
            if closed <= 8 and closed > 4:
                numbers = line[muldex+4:muldex+3+closed]
                numlist = numbers.split(',')
                if numlist[0].isdigit():
                    if numlist[1].isdigit():
                        total += int(numlist[0]) * int(numlist[1])

print(total)