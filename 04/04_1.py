filename = '04\input.txt'
diag = []

horizontal = 0
diagonal = 0
vertical = 0

def diag_1(test):
    results = set()
    tot = 0
    for i in range(len(test)):
        tmp1=""
        tmp2=""
        for j in range(0,len(test)-i):
            tmp1+=test[i+j][j]
            tmp2+=test[j][i+j]
        results.add(tmp1)
        results.add(tmp2)
        d_1 = list(results)
    for item in d_1:
        tot += item.count('XMAS')
        tot += item[::-1].count('XMAS')
    return(tot)


def diag_2(test):
    results = set()
    n=len(test)
    tot = 0
    for i in range(n):
        tmp1=""
        tmp2=""
        for j in range(i+1):
            tmp1+=test[i-j][j]
            tmp2+=test[n-1-j][n-1-i+j]
        results.add(tmp1)
        results.add(tmp2)
        d_1 = list(results)
    for item in d_1:
        tot += item.count('XMAS')
        tot += item[::-1].count('XMAS')
    return(tot)


with open(filename) as file:
    lines = [line.rstrip() for line in file]
    linelen = len(lines[0])
    vert = [''] * linelen
    for line in lines:
        linelist = list(line)
        reverse = line[::-1]
        diag.append(linelist)

        horizontal += line.count('XMAS')
        horizontal += reverse.count('XMAS')

        for i in range(linelen):
            vert[i] += line[i]
    for col in vert:
        vertical += col.count('XMAS')
        reverse_col = col[::-1]
        vertical += reverse_col.count('XMAS')


print(diag_1(diag)+ diag_2(diag) + horizontal + vertical)

