n = int(input())
arr = list(map(int,input().split()))
for i in range(n):
    count = 0
    for j in range(i):
        if arr[j] < arr[i]:
            count += 1
    print(count,end=' ')
