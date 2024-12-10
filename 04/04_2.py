import pandas as pd

data = pd.read_csv('04\input.txt', delimiter= '', header = None, engine='python')
rows, columns = data.shape
data = data.drop(columns = [0, columns-1])

red_df = data.drop([0, rows-1])
red_df = red_df.drop(columns = [1, columns-2])

print(data)
print(red_df)
count =0
for index, row in red_df.iterrows(): 
    for i in range(2, columns-2):
        if row[i] == 'A':
            print(data[i-1][index-1], data[i+1][index-1], data[i-1][index+1], data[i+1][index+1])
            if data[i-1][index-1] == 'M' and data[i+1][index+1] == 'S':
                if data[i-1][index+1] == 'S' and data[i+1][index-1] == 'M':
                    count += 1
                if data[i-1][index+1] == 'M' and data[i+1][index-1] == 'S':
                    count += 1

            if data[i-1][index-1] == 'S' and data[i+1][index+1] == 'M':
                if data[i-1][index+1] == 'S' and data[i+1][index-1] == 'M':
                    count += 1
                if data[i-1][index+1] == 'M' and data[i+1][index-1] == 'S':
                    count += 1

print(count)