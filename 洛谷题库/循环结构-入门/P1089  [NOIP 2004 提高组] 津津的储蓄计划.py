# 月初妈妈给的钱
rest = 0

# 存在妈妈那里的钱
bank = 0

# 判断有没有花超提前跳出
pd = True

for month in range(1,12+1):
    # 预算m
    m = int(input())
    rest += 300
    if rest < m:
        print(-month)
        pd = False
        break

    rest -= m
    if rest > 100:
        bank += rest // 100 * 100
        rest %= 100

if pd:
    print(rest + bank * 6 // 5)