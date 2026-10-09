arr = list(map(int,input().split()))
n = arr[0]
index = 1
row =[]
ls = [[0] * n for _ in range(n)]
while index <= len(arr) - 1:
    if index % 2 == 0:
        for _ in range(arr[index]):
            row.append(1)
        index += 1
        continue
    else:
        for _ in range(arr[index]):
            row.append(0)
        index += 1
        continue

index = 0
for i in range(n):
    for j in range(n):
        ls[i][j] = row[index]
        index += 1

for i in ls:
    print(''.join(map(str,i)))
print(row)