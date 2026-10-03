import math
s, v = map(int,input().split())
t = math.ceil(s/v)
m = 8 * 60
ans = m - t - 10
if ans < 0:
    ans += 24 * 60
print(f'{ans // 60:02d}:{ans % 60:02d}')