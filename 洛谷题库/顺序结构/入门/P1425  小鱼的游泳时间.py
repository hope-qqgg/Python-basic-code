a, b, c, d = map(int,input().split())
zd = c * 60 + d
qd = a * 60 + b
h = (zd - qd) // 60
m = (zd - qd) % 60
print(h,m)