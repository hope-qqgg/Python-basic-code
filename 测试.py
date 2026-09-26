n = int(input())
# 0 表示关，1 表示开
arr = [0 for _ in range(n)]
for i in range(1,n+1):
    for j in range(0,n,i):
        if arr[j] == 0:
            arr[j] = 1
        elif arr[j] == 1:
            arr[j] = 0
print(arr)