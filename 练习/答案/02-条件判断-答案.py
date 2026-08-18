"""
==========================
  02-条件判断 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:成绩等级
score = int(input("请输入成绩(0~100):"))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 题目 2:判断闰年
year = int(input("请输入年份:"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")

# 题目 3:星期翻译机
day = int(input("请输入 1~7:"))
match day:
    case 1:
        print("周一")
    case 2:
        print("周二")
    case 3:
        print("周三")
    case 4:
        print("周四")
    case 5:
        print("周五")
    case 6:
        print("周六")
    case 7:
        print("周日")
    case _:
        print("输入错误")

# 题目 4:简易计算器
a = float(input("请输入第一个数字:"))
b = float(input("请输入第二个数字:"))
op = input("请输入运算符(+ - * /):")
if op == "+":
    print(f"结果:{a + b}")
elif op == "-":
    print(f"结果:{a - b}")
elif op == "*":
    print(f"结果:{a * b}")
elif op == "/":
    if b == 0:
        print("除数不能为0")
    else:
        print(f"结果:{a / b}")
else:
    print("不认识的运算符")
