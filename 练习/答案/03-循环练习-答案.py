"""
==========================
  03-循环练习 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:1~100 求和(for 版)
total = 0
for i in range(1, 101):
    total += i
print(f"for 版:1~100 的和是 {total}")

# 1~100 求和(while 版)
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"while 版:1~100 的和是 {total}")

# 题目 2:九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={j * i}", end="\t")
    print()

# 题目 3:三角形星星
for i in range(1, 6):
    print("*" * i)

# 题目 4:偶数和(continue 版)
total = 0
for i in range(1, 51):
    if i % 2 == 1:
        continue
    total += i
print(f"1~50 偶数和:{total}")

# 题目 5:猜数字(简单版)
import random
number = random.randint(1, 50)
count = 0
while True:
    guess = int(input("请输入您猜的数字(1~50):"))
    count += 1
    if guess > number:
        print("猜大了")
    elif guess < number:
        print("猜小了")
    else:
        print(f"恭喜猜对了!一共猜了 {count} 次")
        break
