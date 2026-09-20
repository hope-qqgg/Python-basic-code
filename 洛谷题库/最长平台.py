n = int(input())
arr = list(map(int,input().split()))
arr_max = 0
cont = 1
for m in range(1,n):
    if arr[m-1] == arr[m]:
        cont += 1
        arr_max = max(arr_max,cont)
    else:
        cont = 1
        arr_max = max(arr_max,cont)
print(arr_max)
