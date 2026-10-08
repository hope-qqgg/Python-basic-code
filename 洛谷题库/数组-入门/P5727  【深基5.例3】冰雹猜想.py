def hail(x,arr=[]):
    arr.append(str(x))
    if x == 1:
        return arr[::-1]
    if x % 2 != 0:
        return hail(x * 3 + 1)
    elif x % 2 == 0:
        return hail(int(x / 2))

n = int(input())
print(' '.join(hail(n)))
