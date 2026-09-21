arr = [list(map(int,input().split())) for _ in range(5)]
m,n = map(int,input().split())
for j in range(5):
    arr[m-1][j],arr[n-1][j] = arr[n-1][j],arr[m-1][j]
for n in arr:
    print(*n)
