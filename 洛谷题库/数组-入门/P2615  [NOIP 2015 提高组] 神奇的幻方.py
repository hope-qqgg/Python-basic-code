n = int(input())
array = [[0] * n for _ in range(n)]
x, y = 0,n // 2
array[x][y] = 1
for k in range(2,n * n + 1):
    if x == 0 and y != n - 1:
        x = n - 1
        y = y + 1
    elif y == n - 1 and x != 0:
        x = x - 1
        y = 0
    elif x == 0 and y == n - 1:
        x = x + 1
    else:
        if array[x - 1][y + 1] == 0:
            x = x - 1
            y = y + 1
        else:
            x = x + 1
    array[x][y] = k

for i in array:
    print(' '.join(map(str,i)))