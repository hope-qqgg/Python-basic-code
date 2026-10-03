def f1(n):
    if n % 2 == 0:
        return True
    return False
def f2(n):
    if 4 < n <= 12:
        return True
    return False

n = int(input())
if f1(n) and f2(n):
    print(1,end=' ')
else:
    print(0,end=' ')
if f1(n) or f2(n):
    print(1,end=' ')
else:
    print(0,end=' ')
if (not f1(n) and f2(n)) or (not f2(n) and f1(n)):
    print(1,end=' ')
else:
    print(0,end=' ')
if not f1(n) and not f2(n):
    print(1)
else:
    print(0)