k = int(input())
count = 0
arr =[]
n = 0
for i in range(1,k+1):
    for j in range(i):
        if n == k:
            break
        n += 1
        count += i
        arr.append(i)
print(arr)
print(count)