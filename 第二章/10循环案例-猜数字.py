"""
    案例2：猜数字游戏
    1．系统随机生成一个随机数
    2.用户根据提示猜数字，并将所猜的数字输入系统
    3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
    4.如果猜对，系统自动退出，游戏结束
"""
import random
number = random.randint(1, 100) # 生成随机数
while True: # 比较
    num = int(input("请输入数字：")) # 接收输入数字
    if num > number:
        print("猜大了")
    elif num < number:
        print("猜小了")
    else:
        print("恭喜你猜对了")
        break
print(f"答案为：{number}")