l,m = map(int,input().split())
arr = [1] * (l + 1)
for _ in range(m):
    q,s = map(int,input().split())
    for n in range(q,s+1):
        arr[n] = 0
print(sum(arr))
print('=============================================')
l,m = map(int,input().split())
arr = [1] * (l + 1)
for _ in range(m):
    u,v = map(int,input().split())
    arr[u:v+1] = [0] * (v - u + 1)
print(sum(arr))
