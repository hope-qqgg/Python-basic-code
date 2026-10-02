import math
PI = 3.14
h, r = map(int,input().split())
v = PI * r**2 * h
n = math.ceil((20*1000)/v)
print(n)