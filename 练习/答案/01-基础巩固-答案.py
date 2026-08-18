"""
==========================
  01-基础巩固 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:温度转换器
c = float(input("请输入摄氏温度:"))
f = c * 9 / 5 + 32
print(f"华氏温度:{f}")

# 题目 2:四则运算器
a = int(input("请输入第一个整数:"))
b = int(input("请输入第二个整数:"))
print(f"和:{a + b}")
print(f"差:{a - b}")
print(f"积:{a * b}")
print(f"商:{a // b}")
print(f"余数:{a % b}")

# 题目 3:圆的面积
r = float(input("请输入半径:"))
area = 3.14 * r ** 2
print(f"面积:{area}")

# 题目 4:自我介绍
name = "小明"
age = 18
print(f"我叫{name},今年{age}岁,正在学习Python!")
