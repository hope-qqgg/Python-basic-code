#------------------------------ 函数 - 变量的作用域 ------------------------------
# 全局变量：在函数外部 或 函数的内部都是可以访问的
num = 100

# 定义函数
def circle_area(r):
    # 局部变量：只能在函数内部使用
    pi = 3.14
    area = pi * r**2

    global  num
    num = 1000 # 修改全局变量
    print("num = ",num) # 1000

    return area

# 调用函数
c_area = circle_area(10)
print(c_area)

print("num = ",num) # 1000;把 global 注释结果为：100

#------------------------------ 函数 - 传参方式 ------------------------------
# 定义函数
def reg_stu(name,age,gender,city):
    print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市{city}")
    return {"name" : name,"age" : age,"gender" : gender,"city" : city}

# 传参方式一：位置参数
stu = reg_stu("张三",18,"男","北京")
print(stu)

# 传参方式二：关键字参数
stu = reg_stu(name = "晓钢",age = 20,gender = "男",city ="福建")
print(stu)

stu = reg_stu(age = 20,gender = "女",city ="福建",name = "小黑子")
print(stu)

# 传参方式三：位置参数 + 关键字参数 ---> 位置参数在前，关键字参数在后面
stu = reg_stu("鸡哥",20,gender = "女",city ="福建")

#------------------------------ 函数 - 传参方式 ------------------------------
# 定义函数
def reg_stu1(name,age,gender="男",city="福建"):
    print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市{city}")
    return {"name" : name,"age" : age,"gender" : gender,"city" : city}

# 调用函数
stu = reg_stu1("王林",20)
print(stu)

stu = reg_stu1("王琳",18,"女")
print(stu)

stu = reg_stu1("王维",22,city = "上海")
print(stu)

#------------------------------ 函数 - 不定长参数（位置参数 *args ---> 元组） ------------------------------
# 需求：根据传入的这批数据，计算这批数据的最大值、最小值和平均值
def calc_data(*args):
    max_data = max(args)
    min_data = min(args)
    avg_data = sum(args) / len(args)
    return max_data,min_data,avg_data

# 调用函数
print(calc_data(2,7,9,10,45))
print(calc_data(2,7,9,10,45,73,37,93,92,111,222))

#------------------------------ 函数 - 不定长参数（关键字参数 **kwargs ---> 字典） ------------------------------
# 需求：根据传入的这批数据，计算这批数据的最大值、最小值和平均值
def calc_data1(*args,**kwargs):
    """
    根据传入的这批数据，计算这批数据的最大值、最小值和平均值
    :param args: 不定长位置参数，需要计算的这批数据
    :param kwargs: 不定长关键字参数
        round: 保留的小数位数
        print: 是否打印
    :return: 最大值、最小值和平均值
    """
    max_data = max(args)
    min_data = min(args)
    avg_data = sum(args) / len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))
    if kwargs.get("print") is not None:
        print(f"计算出来的最大值：{max_data},最小值{min_data},平均值：{avg_data}")
    return max_data,min_data,avg_data

# 调用函数
print(calc_data1(2,7,9,10,45,round=3,print=True))
print(calc_data1(2,7,9,10,45,73,37,93,92,111,222,round=3,print=True))
