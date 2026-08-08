# 常见的数据类型 ---> type()获取指定字面量或变量的类型

print(type(1))  # int
print(type(3.14))  # float
print(type(True))  # bool
print(type(False))  # bool
print(type("Hello World"))  # str
print(type(None))  # NoneType
num = 111
print(type(num))  # int
print("------------------------------\n")

# 常见的数据类型 ---> isinstance()判断指定字面量或变量是否是指定类型，如果是返回True，否则返回False
print(isinstance(num, int))  # True
print(isinstance(num, bool))  # False
print(isinstance(num, float))  # False
print(isinstance(num, str))  # False
print("------------------------------\n")

# 字符串
# 定义字符串的三种方式
s1 = "Hello Python" # 双引号定义
s2 = '你好世界' # 单引号定义
s3 = """
hello:
    你好世界
    Hello Python
""" # 三引号定义（多行字符串）

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))
print("------------------------------\n")

# 定义字符---> It's very good
# 转义字符\' \" \n \t
msg = 'It\'s very good' # 转义字符
print(msg)

msg2 = "It's very good"
print(msg2)

msg3 = "hello的意思是\"你好\""
print(msg3)

msg4 = 'hello的意思是\"你好\"'
print(msg4)

msg5 = "hello:\n\t你好世界\n\tHello Python" # \n 换行 \t 制表符
print(msg5)
print("------------------------------\n")

# 字符串操作
s1 = "永远有多远""，野狗牛奶"
print(s1)

msg1 ="人生苦短"
msg2 ="我用Python"
print("龟叔说：" + msg1 + "，" + msg2)

# 案例 ---> str(int数字) 将int型整数转换为字符串
name = "HOPE"
age = 19
pro = "计算机应用技术"
hoppy = "Java、Python、C++"
message = "姓名：" + name + "，年龄：" + str(age) + "岁，专业：" + pro + "，爱好：" + hoppy
print(message)
print("------------------------------\n")

# 字符串格式化 ---> 方法一：%s 占位符
name = "HOPE"
age = 19
pro = "计算机应用技术"
hoppy = "Java、Python、C++"
message = "姓名：%s，年龄：%d岁，专业：%s，爱好：%s" % (name, age, pro, hoppy)
print(message)

# 字符串格式化 ---> 方法二：f"..{变量名/表达式}.."
name = "HOPE"
age = 19
pro = "计算机应用技术"
hoppy = "Java、Python、C++"
message = f"姓名：{name}，年龄：{age}岁，专业：{pro}，爱好：{hoppy}"
print(message)

