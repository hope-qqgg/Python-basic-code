# 函数的参数类型
# 加
def add (x,y):
    return x + y
# 减
def subtract (x,y):
    return x - y
# 乘
def multiply (x,y):
    return x * y
# 除
def divide (x,y):
    return x / y

# 计算
def calc(x,y,oper):
    return oper(x,y)

print(calc(10,20,multiply))

# 匿名函数
# 需求1：打印一个分割线
def out_line():
    print("-" * 20)

out_line_1 = lambda : print("-" * 20)
out_line()
out_line_1()

# 需求2：计算两个数之和
add_1 = lambda x,y : x + y
print(add_1(100,200))
print(add(100,200))

# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序
data_list = ["c++","c","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
print(data_list)

data_list.sort(key = lambda item : len(item)) # 匿名函数经典的应用场景
print(data_list)