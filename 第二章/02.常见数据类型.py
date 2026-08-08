# 常见的数据类型 ---> type()获取指定字面量或变量的类型
print(type(1))  # int
print(type(3.14))  # float
print(type(True))  # bool
print(type(False))  # bool
print(type("Hello World"))  # str
print(type(None))  # NoneType
num = 111
print(type(num))  # int
print("------------------------------")

# 常见的数据类型 ---> isinstance()判断指定字面量或变量是否是指定类型，如果是返回True，否则返回False
print(isinstance(num, int))  # True
print(isinstance(num, bool))  # False
print(isinstance(num, float))  # False
print(isinstance(num, str))  # False


