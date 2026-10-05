def f(n):
    return (((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n)/5**0.5

n = float(input())
print(f'{f(n):.2f}')