l,m = map(int,input().split())
arr = [1] * (l + 1)
for _ in range(m):
    q,s = map(int,input().split())
    for n in range(q,s+1):
        arr[n] = 0
print(sum(arr))