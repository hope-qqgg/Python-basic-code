def hermite(n,x):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    elif n > 1:
        return 2 * x * hermite(n-1,x) - 2 * (n - 1) * hermite(n - 2,x)

n, x = map(int,input().split())
print(hermite(n,x))