n, m, k = map(int, input().split())
OFF = 3                      # 四周留 3 格边框
S = n + 6
arr = [[0] * S for _ in range(S)]
for i in range(OFF, OFF + n):        # 中间 n×n 才是真的棋盘
    for j in range(OFF, OFF + n):
        arr[i][j] = 1                # 1 = 黑暗(会刷怪)

# 火把
for _ in range(m):
    x, y = map(int, input().split())
    x += OFF - 1                     # 1 下标 -> 0 下标 + 平移
    y += OFF - 1
    for d in range(-2, 3):
        arr[x][y + d] = 0            # 横着的 5 格
        arr[x + d][y] = 0            # 竖着的 5 格
    for dx in (-1, 1):               # 4 个斜角
        for dy in (-1, 1):
            arr[x + dx][y + dy] = 0

# 萤石
for _ in range(k):
    o, p = map(int, input().split())
    x, y = o + OFF - 1, p + OFF - 1
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            arr[x + dx][y + dy] = 0

count = 0
for i in range(OFF, OFF + n):        # 只数中间 n×n
    for j in range(OFF, OFF + n):
        count += arr[i][j]
print(count)

