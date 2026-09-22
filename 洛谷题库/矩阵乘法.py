n,m,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(m)]
c = []
for i in range(n):
    arr = []
    for j in range(k):
        num = 0
        for x in range(m):
            num += (a[i][x] * b[x][j])
        arr.append(num)
    c.append(arr)
for i in c:
    print(' '.join(map(str,i)))
