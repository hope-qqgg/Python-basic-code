arr = list(input().split())
a = input()
b = input()
arr_len =len(arr)
for i in range(arr_len):
    if arr[i] == a:
        arr[i] = b
print(' '.join(arr))