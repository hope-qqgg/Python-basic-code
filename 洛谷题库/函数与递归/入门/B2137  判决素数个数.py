def is_shuShu(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
x, y = map(int,input().split())
if x > y:
    x, y = y, x
count = 0
for i in range(x,y+1):
    if is_shuShu(i):
        count += 1
print(count)
# 埃氏筛
x, y = map(int, input().split())
if x > y:                      # 题面没保证 X <= Y（上次 40 分的坑）
    x, y = y, x

if y < 2:
    print(0)                   # 连 2 都不到，就是 0 个
else:
    is_prime = [True] * (y + 1)     # 建一排"开关"：True=还留着，False=划掉了
    is_prime[0] = False             # 0 不是素数
    is_prime[1] = False             # 1 也不是

    for i in range(2, int(y ** 0.5) + 1):    # 只试到 √y 就够
        if is_prime[i]:                      # i 还留着 → i 是素数
            for j in range(i * i, y + 1, i): # 把 i 的倍数一个个划掉
                is_prime[j] = False

    count = 0
    for n in range(x, y + 1):                # 最后数一数 [x, y] 里还剩几个 True
        if is_prime[n]:
            count += 1
    print(count)


