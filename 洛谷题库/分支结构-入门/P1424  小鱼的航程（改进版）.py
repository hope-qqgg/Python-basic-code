x, n = map(int, input().split())
total = 0
d = x
for _ in range(n):
    if d <= 5:
        total += 250
    d = d % 7 + 1
print(total)

# 方法二
x, n = map(int, input().split())
weeks, rem = divmod(n, 7)   # 整周数 + 余下几天
days = weeks * 5            # 每个整周固定游 5 天
d = x                       # 余下几天照样从周 x 逐天看
for _ in range(rem):
    if d <= 5:
        days += 1
    d = d % 7 + 1
print(days * 250)
# divmod(a, b) 一次返回「商」和「余数」两个数
# divmod(10, 7)      = (1, 3)          ← 10 ÷ 7 = 1 余 3