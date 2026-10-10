def recursion(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    return recursion(x - 1) + recursion(x - 2)

def recurrence(x):
    a = 1
    b = 2
    c = 0
    if x <= 2:
        return n
    else:
        for i in range(3,n+1):
            c = a + b
            a = b
            b = c
        return c

n = int(input())
print(recursion(n))