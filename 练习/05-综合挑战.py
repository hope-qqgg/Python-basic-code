"""
==========================
  练习 05:综合挑战
  把前面学的所有知识组装起来!
  难度:★★★★★
  规则:先自己尝试写,每道题都是"完整的程序"
       写完可以运行测试,卡住超过15分钟再看答案
==========================
"""

# ------------------------------------------------------------
# 挑战 1:猜数字·进化版 🎲
# 要求:
#   1. 系统随机 1~100 的数字
#   2. 用户猜,猜错提示"大了/小了"
#   3. 每次猜的数字都存进列表
#   4. 猜对后输出:一共猜了几次、每次猜了什么(用列表展示)
#   5. 附加题:猜对时还提示"最高/最低的猜测"分别是多少
# ------------------------------------------------------------
# 【小提示】
# history = [] 存每次猜测;猜对后:
#   print(f"您一共猜了{len(history)}次")
#   print(f"猜测记录:{history}")

# 您的代码写在这里 ↓↓↓
import random
number = random.randint(1,100)
history = []
while True:
    num = int(input("请输入你觉得正确的数字："))
    if num > number:
        print("猜大了")
        history.append(num)
        continue
    elif num < number:
        print("猜小了")
        history.append(num)
        continue
    else:
        history.append(num)
        print(f"恭喜你猜对了是{number}")
        print(f"您一共猜了{len(history)}次")
        print(f"猜测记录:{sorted(history)}")
        print(f"猜测最大值{max(history)}")
        print(f"猜测最小值{min(history)}")
        break

# ------------------------------------------------------------
# 挑战 2:登录系统·限次版 🔐
# 要求:
#   1. 账号密码存进列表(3个账号,参考您之前的案例)
#   2. 最多尝试 3 次,第 4 次输入前提示"尝试次数已用完,账号锁定!"
#   3. 用户名或密码不能为空
#   4. 登录成功输出"登录成功,进入B站首页~"
# ------------------------------------------------------------
# 【小提示】
# users = [["admin", "666888"], ["zhangsan", "123456"], ["taoge", "888666"]]
# count 记录失败次数,失败 3 次 break
# 判断账号:[username, password] in users

# 您的代码写在这里 ↓↓↓
users = [["admin", "666888"], ["zhangsan", "123456"], ["taoge", "888666"]]
count = 0
username_password = []
while True:
    if count < 3:
        username = input("请输入用户名：")
        username_password.append(username)
        password = input("请输入密码：")
        username_password.append(password)
        if username_password in users:
            print("登录成功，进入B站首页~")
            break
        else:
            count += 1
            print("用户名或密码错误，请重新输入！")
            continue
    else:
        print("失败多次，强制退出")
        break

# ------------------------------------------------------------
# 挑战 3:工资统计(自由发挥)💰
# 定义一个工资列表: [8000, 12000, 6500, 15000, 9000, 11000]
# 输出:
#   1. 最高工资、最低工资、平均工资
#   2. 工资超过平均工资的人数
#   3. 工资从高到低排序后的列表
#   附加题:把低于 8000 的工资每人涨 1000,输出新列表
# ------------------------------------------------------------
# 【小提示】
# 超过平均:循环列表,if 工资 > 平均: 计数 +1
# 降序排序:s.sort(reverse=True) 或 sorted(s, reverse=True)

# 您的代码写在这里 ↓↓↓
salary = [8000, 12000, 6500, 15000, 9000, 11000]
print(f"最高工资:{max(salary)}")
print(f"最低工资:{min(salary)}")
print(f"平均工资:{sum(salary) / len(salary):.2f}")
count = 0
for num in salary:
    if num > sum(salary) / len(salary):
        count += 1
print(f"工资超过平均工资的人数为：{count}人")
salary.sort(reverse=True)
print(salary)
new_salary = []
for num1 in salary:
    if num1 < 8000:
        new_salary.append(num1 + 1000)
    else:
        new_salary.append(num1)
print(f"涨薪后的工资为:{new_salary}")