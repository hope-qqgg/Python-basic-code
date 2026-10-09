n = int(input())
arr = list(map(int,input().split()))
arr.sort()
arr_len = len(arr)
res = set()
for left in range(arr_len-1):
    for right in range(left+1,arr_len):
        lr_sum = arr[left] + arr[right]
        if lr_sum in arr:
            res.add(lr_sum)
print(len(res))
