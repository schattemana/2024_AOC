import pandas as pd
rules = pd.read_csv('05\instructions.txt', delimiter= '|', header = None, engine='python')

with open('05\input.txt') as f:
    lines = f.read().splitlines()
    arrays = []
    for line in lines:
        arrays.append([int(x) for x in line.split(',')])


def check(array):
    for index, row in rules.iterrows():
        if row[0] in array and row[1] in array:
            if array.index(row[0]) < array.index(row[1]):
                continue
            else:
                return(False)
    return(True)


total = 0
for array in arrays:
    if check(array) == True:
        middleIndex = (len(array) - 1)/2
        total += array[int(middleIndex)]

print(total)