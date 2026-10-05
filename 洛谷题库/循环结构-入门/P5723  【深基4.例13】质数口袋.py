def ass(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False
    return arr

ls = ass(100000)
count = 0
n = int(input())
m = 0
for i in range(1,n+1):
    if m + i > n:
        break
    if ls[i]:
        print(i)
        count += 1
        m += i
print(count)
