# 注意：函数定义的时候并不会执行，只有在调用函数的时候，函数体的逻辑才会执行：函数必须先定义，后调用
# 函数定义
def out_line():
    print("------------------------------")
    print("------------------------------")

# 函数调用
out_line()

# 函数的参数与返回值
# 函数1：计算圆的面积 --- 半径
def circle_area(r):
    """
    该函数用于根据圆的半径，计算圆的面积
    :param r: 半径
    :return: 圆的面积
    """
    area = 3.14 * r**2
    return print(round(area,1))

circle_area = circle_area(100)


# 函数2：计算长方形的面积 --- 长，宽
def rectangle_area(l,w):
    """
    该函数用于根据长方形的长、宽，计算长方形的面积
    :param l: 长方形的长
    :param w: 长方形的宽
    :return: 长方形的面积
    """
    area =l * w
    return print(round(area, 1))

help(rectangle_area) # 调用说明文档
rectangle_area(20,10)

# 函数3：计算圆的面积、周长 -- 半径 ---> 如果返回值之间逗号分隔 ---> 多个返回值会封装到元组之中
def circle_len(r):
    """
    该函数用于根据圆的半径，计算圆的面积、周长
    :param r: 半径
    :return: (面积,周长)
    """
    return  round(3.14 * r * r,1),round(2 * 3.14 * r,1)

al = circle_len(10)
print(al)
print(type(al))

area, len1 = circle_len(10)
print(area)
print(len1)

# 函数的嵌套调用
def function_a():
    print("a ... before")
    function_b()
    print("a .... after")

def function_b():
    print("b ... before")
    function_c()
    print("b .... after")

def function_c():
    print("c ...")

function_a()
print("函数调用完毕~")

"""
function_a() 开始
    |———— 打印 "a ... before"
    |———— 调用 function_b()
    |      |———— 打印 "b ... before"
    |      |———— 调用 function_c()
    |      |       |———— 打印 "c ..."
    |      |———— 打印 "b .... after"
    |      |———— function_b() 返回
    |———— 打印 "a .... after"
    |———— function_a() 返回
"""


