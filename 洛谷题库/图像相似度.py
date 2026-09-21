m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m)]
b = [list(map(int,input().split())) for _ in range(m)]
count = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == b[i][j]:
            count += 1
print(f'{(count/(n*m)) * 100:.2f}')
