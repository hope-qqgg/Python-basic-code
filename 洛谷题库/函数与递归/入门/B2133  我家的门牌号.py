def zhao(n):
    for m in range(1, 1000):
        total = m * (m + 1) // 2
        for x in range(1, m + 1):
            if total - 3 * x == n:
                return x, m

n = int(input())
x, m = zhao(n)
print(x, m)