"""
==========================
  05-综合挑战 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 挑战 1:猜数字·进化版
import random
number = random.randint(1, 100)
history = []
while True:
    guess = int(input("请输入您猜的数字(1~100):"))
    history.append(guess)
    if guess > number:
        print("猜大了")
    elif guess < number:
        print("猜小了")
    else:
        print("恭喜你猜对了!")
        break
print(f"一共猜了 {len(history)} 次")
print(f"猜测记录:{history}")
print(f"最高猜测:{max(history)}")
print(f"最低猜测:{min(history)}")

# 挑战 2:登录系统·限次版
users = [["admin", "666888"], ["zhangsan", "123456"], ["taoge", "888666"]]
count = 0
while True:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == "" or password == "":
        print("用户名或密码不能为空!")
        continue
    if [username, password] in users:
        print("登录成功,进入B站首页~")
        break
    else:
        count += 1
        print("用户名或密码错误!")
        if count >= 3:
            print("尝试次数已用完,账号锁定!")
            break
        print(f"您还有 {3 - count} 次机会")

# 挑战 3:工资统计
salary = [8000, 12000, 6500, 15000, 9000, 11000]
highest = max(salary)
lowest = min(salary)
average = sum(salary) / len(salary)
print(f"最高工资:{highest}")
print(f"最低工资:{lowest}")
print(f"平均工资:{average}")

count = 0
for s in salary:
    if s > average:
        count += 1
print(f"超过平均工资的人数:{count}")

salary_desc = sorted(salary, reverse=True)
print(f"工资从高到低:{salary_desc}")

# 附加题:低于 8000 的涨 1000
new_salary = []
for s in salary:
    if s < 8000:
        new_salary.append(s + 1000)
    else:
        new_salary.append(s)
print(f"调薪后:{new_salary}")
