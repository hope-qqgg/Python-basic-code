# if条件判断：如果分数超过680，我就去学go
score = 700
if score > 680:
    print("你可以学懂go")
print("------------------------------\n")

# if案例：结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现（正确账号和密码为18888888888/666888）
# 1.定义正确账号和密码
correct_account = 18888888888
correct_password = 666888

# 2.键盘输入账号和密码
account = int(input("请输入账号："))
password = int(input("请输入密码："))

# 3.判断输入的账号和密码是否正确，正确输出登入成功
if password == correct_password and account == correct_account:
    print("登入成功")

# 4.判断输入的账号和密码是否正确，不正确输出登入失败，账号或者密码错误
if password != correct_password or account != correct_account:
    print("登入失败")
    print("账号或者密码错误")
print("------------------------------\n")

# if...else...案例：结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现（正确账号和密码为18888888888/666888）
# 1.定义正确账号和密码
correct_account = 18888888888
correct_password = 666888

# 2.键盘输入账号和密码
account = int(input("请输入账号："))
password = int(input("请输入密码："))

# 3.判断
if password == correct_password and account == correct_account:
    print("登入成功")
else:
    print("登入失败")
    print("账号或者密码错误")
print("------------------------------\n")

# 案例1：根据用户输入的年份，判断这一年是闰年还是平年（非整百年份，且能被4整除的年份是闰年；整百年份（如1900、2000）必须被400整除才是闰年）
# 1.定义变量记录键盘输入的年份
year = int(input("请输入年份："))

# 2.判断这一年是闰年还是平年（非整百年份，且能被4整除的年份是闰年；整百年份（如1900、2000）必须被400整除才是闰年）
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年是平年")
print("------------------------------\n")

# 需求1：根据用户输入的数字，判断这个数字是奇数还是偶数。
# 1.定义变量记录键盘输入的数字
num = int(input("请输入数字："))
# 2.判断这个数字是奇数还是偶数
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
print("------------------------------\n")

# 需求2：根据用户输入的年龄，判断该用户是否已经成年（ >=18,成年；否则，未成年）
# 1.定义一个变量记录键盘录入的年龄
age = int(input("请输入年龄："))
# 2.判断该用户是否已经成年
if age >= 18:
    print("成年")
else:
    print("未成年")
print("------------------------------\n")

# 需求3：根据用户输入的数字，判断该数字是正数还是负数（不考虑0）
# 1.定义一个变量记录键盘输入的数字
num = int(input("请输入数字："))
# 2.判断该数字是正数还是负数
if num > 0:
    print(f"{num}是正数")
elif num < 0:
    print(f"{num}是负数")
else:
    print(f"{num}既不是正数也不是负数")
print("------------------------------\n")

# 需求4：根据用户输入的考试分数，判断该用户是否通过考试（分数>=60，及格；否则，不及格）
# 1.定义变量记录键盘输入的分数
score = int(input("请输入分数："))
# 2.判断该用户是否通过考试
if score >= 60:
    print("及格")
else:
    print("不及格")
print("------------------------------\n")
