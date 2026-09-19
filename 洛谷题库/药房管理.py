m = int(input())  
n = int(input())
arr = list(map(int,input().split()))
cont = 0
for c in arr:
    if m - c >= 0:
        m -= c
        cont += 1
print(n - cont)

