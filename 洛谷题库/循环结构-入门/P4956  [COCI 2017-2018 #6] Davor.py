n = int(input())
m = n // 364
for x in range(min(100,m - 3),0,-1):
    if (m - x) % 3 == 0:
        k = (m - x) // 3
        print(x)
        print(k)
        break
