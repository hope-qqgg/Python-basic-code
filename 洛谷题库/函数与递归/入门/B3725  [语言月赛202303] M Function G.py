def m(arr,r,l=1):
    if abs(r - l) <= 5:
        return max(arr[l-1:r])
    mid = (l + r) // 2
    x = m(arr,mid,l)
    y = max(m(arr, r, mid + 1), 7)
    c = arr[mid-1] - 1
    return x % y + c

r = int(input())
arr = list(map(int,input().split()))
print(m(arr,r))