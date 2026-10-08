n, m, k = map(int,input().split())
arr = [[0] * n for _ in range(n)]
for i in arr:
    for j in i:
        print(j,end=' ')
    print()