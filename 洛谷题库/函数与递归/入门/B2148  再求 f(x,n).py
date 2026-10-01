def f(x,n):
    if n == 1:
        return x / (1 + x)
    return x / (n + f(x,n-1))

x = float(input())
n = int(input())
print(f'{f(x,n):.2f}')