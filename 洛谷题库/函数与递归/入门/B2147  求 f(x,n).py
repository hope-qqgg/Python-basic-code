def f(x,n):
    if n == 1:
        return (1 + x)**0.5
    return (n + f(x,n-1))**0.5

x, n = input().split()
x = float(x)
n = int(n)
print(f'{f(x,n):.2f}')