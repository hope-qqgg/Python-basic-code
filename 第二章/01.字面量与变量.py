# 字面量的写法
from operator import truediv

print(100) # 整数（int）
print(3.14) # 浮点数（float）
print(True) # 布尔值（bool）
print(False) # 布尔值（bool）
print("Hello World") # 字符串（str）
print(None) # 空值（NoneType）
print("------------------------------")

# 布尔类型本质也是整数类型，True = 1，False = 0
print(True + 1)#2
print(False - 1)#-1
print("------------------------------")

# 变量 ---> Python是动态类型语言，一个变量是可以存储不同类型的数据的（但在项目开发中，推荐变量只存储一种类型的数据）
num = 1114.1
print(num)

num = num + 1
print(num)

num = "Hello Python"
print(num)

num = True
print(num)

a = True
print(a)
print("------------------------------")

# 案例
base = 20.7 # 基础播放量
incr = 50 # 每月增量播放量
print("未来第一个月的播放量", base + incr)
print("未来第二个月的播放量", base + incr)
print("------------------------------")

# 案例 —— 升级：一次性可以定义多个变量
base, incr = 20.7, 50
print("未来第一个月的播放量", base + incr)
print("未来第二个月的播放量", base + incr)
print("------------------------------")

# 案例1：现在有两个变量，分别为：a = 10，b = 20，请交换两个变量的值，并打印交换后的结果。
a = 10
b = 20

c = a # c = 10
a = b # a = 20
b = c # b = 10

print(a, b)
print("------------------------------")

# 案例2：现在有三个变量，分别为：a = 100，b = 200，c = 300，现在要求交换三个变量的值，使得a = 200，b = 300，c = 100，并打印交换后的结果。
a = 100
b = 200
c = 300

d = a # d = 100
a = b # a = 200
b = c # b = 300
c = d # c = 100

print(a, b, c)