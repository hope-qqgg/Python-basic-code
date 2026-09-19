n = int(input())
arr = list(map(int,input().split()))
cont = 0
for m in arr:
    g = m % 10
    s = m // 10 % 10
    b = m // 100 % 10
    q = m // 1000
    if g - q - b  - s > 0:
        cont += 1
print(cont)
