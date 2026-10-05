def is_prime(n):
    arr = [True] * (n+1)
    arr[0] = arr[1] = False
    for i in range(2,int(n**0.5)+1):
        if arr[i]:
            for j in range(i * i,n + 1,i):
                arr[j] = False
    return arr

def is_yiShu(m):
    ls = []
    for i in range(2,m):
        if m % i == 0:
            ls.append(i)
    ls.sort()
    return ls

def is_shushu(n):
    if n < 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
ls = is_yiShu(n)
arr = is_prime(n)
for i in ls:
    if arr[i]:
        print(i)
        break

n = int(input())
ls = is_yiShu(n)
for i in ls:
    if is_shushu(i):
        print(n//i)
        break

n = int(input())
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(n // i)
        break