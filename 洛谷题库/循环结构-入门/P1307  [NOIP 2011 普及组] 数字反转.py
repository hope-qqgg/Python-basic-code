n = int(input())
if n < 0:
    print(-int(str(-n)[::-1]))
else:
    print(int(str(n)[::-1]))

# 方法二
n = int(input())

sign = -1 if n < 0 else 1     # 先把符号记下来
m = abs(n)                    # 只处理"数字部分"

rev = 0
while m > 0:
    rev = rev * 10 + m % 10   # m%10 是当前个位，*10 让已拼好的位升一格
    m //= 10                  # 丢掉刚用过的个位

print(sign * rev)