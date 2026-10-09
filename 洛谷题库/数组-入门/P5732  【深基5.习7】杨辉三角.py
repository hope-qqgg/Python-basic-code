n = int(input())
row = [1]
for i in range(n):
    print(' '.join(map(str,row)))
    row.append(0)
    for j in range(len(row)-1,0,-1):
        row[j] += row[j-1]