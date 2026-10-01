def digit(n,k):
    return str(n)[-k]
n, k = map(int,input().split())
print(digit(n,k))