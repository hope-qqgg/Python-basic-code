def is_shushu(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
n = int(input())
arr = [2]
for i in range(3, n + 1, 2):
    if is_shushu(i):
        arr.append(i)

found = False
for i in range(1, len(arr)):
    if arr[i] - arr[i - 1] == 2:
        print(arr[i - 1], arr[i])
        found = True

if not found:
    print('empty')
