def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3,int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int,input().split()))
ls = []
for i in arr:
    if is_prime(i):
        ls.append(i)
print(' '.join(map(str,ls)))