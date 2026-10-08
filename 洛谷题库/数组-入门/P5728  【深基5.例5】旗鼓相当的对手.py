n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
count = 0
print(arr)
for i in range(n-1):
    for j in range(i+1,n):
       if abs(sum(arr[i]) - sum(arr[j])) <= 10 and abs(arr[i][0] - arr[j][0]) <= 5 and abs(arr[i][1] - arr[j][1]) <= 5 and abs(arr[i][2] - arr[j][2]) <= 5:
           count += 1
print(count)
