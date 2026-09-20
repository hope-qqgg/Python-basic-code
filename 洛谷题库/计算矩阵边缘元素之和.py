m,n = map(int,input().split())
cont = 0
for i in range(m):
    arr = list(map(int,input().split()))
    if i == 0 or i == m - 1:
        cont += sum(arr)
    else:
        cont += (arr[0] + arr[-1])
print(cont)
        
