n = int(input())
arr = [[0] * n for _ in range(n)]
count = 1
qd = 0
zd = n // 2
while qd < zd:
    for j in range(qd, n - 1 - qd):
        arr[qd][j] = count
        count += 1
    for i in range(qd, n - 1 - qd):
        arr[i][n - 1 - qd] = count
        count += 1
    for j in range(n - 1 - qd, qd, -1):
        arr[n - 1 - qd][j] = count
        count += 1
    for i in range(n - 1 - qd, qd, -1):
        arr[i][qd] = count
        count += 1
    qd += 1

if n % 2 != 0:
    arr[n//2][n//2] = count

for i in arr:
    for j in i:
        print(f'{j:>3}',end='')
    print()

