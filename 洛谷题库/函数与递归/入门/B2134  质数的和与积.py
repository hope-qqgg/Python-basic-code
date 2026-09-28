def is_shushu(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

s = int(input())
ans = 0
for a in range(2, s // 2 + 1):
    if is_shushu(a) and is_shushu(s - a):
        ans = max(ans, a * (s - a))
print(ans)