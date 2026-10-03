import math
m,t,s = map(int,input().split())
if t == 0:
    print(0)
else:
    if m - math.ceil(s/t) <= 0:
        print(0)
    else:
        print(m - math.ceil(s/t))
