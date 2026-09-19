n,k = map(int,input().split())
cont = 0
arr = list(map(int,input().split()))
arr[k-1] = -arr[k-1]
cont = sum(arr)
print(cont)


