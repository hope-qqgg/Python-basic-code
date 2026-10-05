n = int(input())
arr = list(map(int,input().split()))
count = 1
max_c = 1
for i in range(n-1):
    if arr[i] +1 == arr[i+1]:
        count += 1
        max_c = max(max_c,count)
    else:
        count = 1
print(max_c)