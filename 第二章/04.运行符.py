# 算数运算符 ：+ - * / // % **
print("10 + 4 =", 10 + 4) # 加
print("10 - 4 =", 10 - 4) # 减
print("10 * 4 =", 10 * 4) # 乘
print("10 / 4 =", 10 / 4) # 除（结果为float类型） - 2.5
print("10 // 4 =", 10 // 4) # 整除（结果为整数） - 2
print("10 % 4 =", 10 % 4) # 取余 - 2
print("10 ** 4 =", 10 ** 4) # 幂运算（10的4次方） - 10000
print("------------------------------\n")

# 运算符优先级：** > * / // % > + -
print("0.1 + 10 / 4**2 =", 0.1 + 10 / 4**2)
print("------------------------------\n")

# 案例：输入两个数字 x 和 y，计算 x + y 和 x - y，并将结果输出
# float(...) 函数用于将字符串转换为浮点数
x = float(input("请输入第一个数字 x："))
y = float(input("请输入第二个数字 y："))
print(f"{x} + {y} = {x + y}, {x} - {y} = {x - y}")
# 浮点数运算损失精度问题：计算机基于二进制进行运算，浮点数在计算机中是以二进制形式存储的，而有些十进制小数无法精确表示为二进制小数，因此在进行浮点数运算时可能会出现精度损失的问题。
print("------------------------------\n")

# 练习1：计算输入3个整数的平均值
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
num3 = int(input("请输入第三个整数："))
average = (num1 + num2 + num3) / 3
print(f"三个整数的平均值是：{average}")
print("------------------------------\n")

# 练习2：输入梯形的上底、下底和高，计算梯形的面积
top_base = float(input("请输入梯形的上底："))
bottom_base = float(input("请输入梯形的下底："))
height = float(input("请输入梯形的高："))
area = (top_base + bottom_base) * height / 2
print(f"梯形的面积是：{area}")
print("------------------------------\n")

# 练习3：输入圆的半径，计算圆的面积和周长
pi = 3.14
radius = float(input("请输入圆的半径："))
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"圆的面积是：{area}, 圆的周长是：{circumference}")
print("------------------------------\n")

# 练习4：计算BMI指数
height = float(input("请输入你的身高（米）："))
weight = float(input("请输入你的体重（千克）："))
bmi = weight / (height ** 2)
print(f"你的BMI指数是：{bmi}")
print("------------------------------\n")