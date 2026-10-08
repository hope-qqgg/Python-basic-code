n = int(input())
ans = 0
for _ in range(n):
    a, t = input().split()
    t = int(t)
    A = int(a.replace('.', ''))      # 1.618034 -> 1618034
    for k in range(1, t + 1):
        ans ^= (k * A) // 1000000    # 等价于 ⌊k × a⌋，整数运算零误差
print(ans)

# 还是不理解

n = int(input())
arr = [0] * 2000000
for _ in range(n):
    a, t = input().split()
    t = int(t)
    A = int(a.replace('.', ''))
    for i in range(1,t+1):
        if arr[int(A * i // 1000000)]:
            arr[int(A * i // 1000000)] = 0
        else:
            arr[int(A * i // 1000000)] = 1

count = 0
for i in arr:
    if i:
        print(count)
    else:
        count += 1