# if条件判断：如果分数超过680，我就去学go
score = 700
if score > 680:
    print("你可以学懂go")
print("------------------------------")

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
print("------------------------------")

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
print("------------------------------")

# 案例1：根据用户输入的年份，判断这一年是闰年还是平年（非整百年份，且能被4整除的年份是闰年；整百年份（如1900、2000）必须被400整除才是闰年）
# 1.定义变量记录键盘输入的年份
year = int(input("请输入年份："))

# 2.判断这一年是闰年还是平年（非整百年份，且能被4整除的年份是闰年；整百年份（如1900、2000）必须被400整除才是闰年）
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年是平年")
print("------------------------------")

# 需求1：根据用户输入的数字，判断这个数字是奇数还是偶数。
# 1.定义变量记录键盘输入的数字
num = int(input("请输入数字："))
# 2.判断这个数字是奇数还是偶数
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
print("------------------------------")

# 需求2：根据用户输入的年龄，判断该用户是否已经成年（ >=18,成年；否则，未成年）
# 1.定义一个变量记录键盘录入的年龄
age = int(input("请输入年龄："))
# 2.判断该用户是否已经成年
if age >= 18:
    print("成年")
else:
    print("未成年")
print("------------------------------")

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
print("------------------------------")

# 需求4：根据用户输入的考试分数，判断该用户是否通过考试（分数>=60，及格；否则，不及格）
# 1.定义变量记录键盘输入的分数
score = int(input("请输入分数："))
# 2.判断该用户是否通过考试
if score >= 60:
    print("及格")
else:
    print("不及格")
print("------------------------------")

# 练习：根据输入用户名、密码进行登录系统（用户名、密码为 admin/666888或 root/777888）
# 1.定义变量记录正确用户名和密码
correct_username1 = "admin"
correct_password1 = "666888"
correct_username2 = "root"
correct_password2 = "777888"
# 2.定义变量记录键盘输入的用户名和密码
username = input("请输入用户名：")
password = input("请输入密码：")
# 3.判断用户名和密码是否正确
if username == correct_username1 and password == correct_password1:
    print("登录成功")
elif username == correct_username2 and password == correct_password2:
    print("登录成功")
else:
    print("登录失败")
print("------------------------------")

"""
    案例：三角形类型判断：根据输入的三个边的边长（正整数），判定是等边三角形、等腰三角形、普通三角形，还是不能构成三角形。
        1.构成三角形的条件：两边之和大于第三边
        2.三角形判定规则：
            三个边都相等：等边三角形
            两个边相等：等腰三角形
            三个边都不相等：普通三角形
"""
# 1.定义变量记录键盘输入的三个边的边长
a = int(input("请输第一条边长a："))
b = int(input("请输入第二条边长b："))
c = int(input("请输入第三条边长c："))
# 2.判断是否能构成三角形
if a + b > c and a + c > b and b + c > a:
    # 3.判断三角形类型
    if a == b == c:
        print(f"{a}{b}{c}能构成等边三角形")
    elif a == b or a == c or b == c:
        print(f"{a}{b}{c}能构成等腰三角形")
    else:
        print(f"{a}{b}{c}能构成普通三角形")
else:
    print(f"{a}{b}{c}不能构成三角形")
print("------------------------------")

"""
    北京市居民年度用电电费计算：根据输入的用电度数，计算电费
        北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
    阶梯电价规则：
        第一档：2880度以下，电费单价0.4883元/度
        第二档：2880-4800度，电费单价0.5383元/度
        第三档：4800度以上，电费单价0.7883元/度
"""
# 1.定义变量记录键盘输入的用电度数
electricity = int(input("请输入用电度数："))
# 2.判断用电度数所在的档位，并计算电费
if electricity < 2880:
    electricity_bill = electricity * 0.4883
elif electricity < 4800:
    electricity_bill = 2880 * 0.4883 + (electricity - 2880) * 0.5383
else:
    electricity_bill = 2880 * 0.4883 + 1920 * 0.5383 + (electricity - 4800) * 0.7883
print(f"您的电费为：{electricity_bill}元")
print("------------------------------")
