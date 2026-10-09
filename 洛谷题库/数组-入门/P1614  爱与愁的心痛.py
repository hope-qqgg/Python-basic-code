n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

if m == 0:
    print(0)
else:
    cur = sum(arr[:m])            # 第一个窗口的和
    best = cur
    for i in range(m, n):
        cur += arr[i] - arr[i - m]   # 进一个、出一个
        if cur < best:
            best = cur
    print(best)