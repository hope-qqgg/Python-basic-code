# 函数的参数类型
# 加
from functools import total_ordering


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

#------------------------------ 案例 ------------------------------
# 案例1：计算n的阶乘
# 递归调用：指的是在函数中自己调用自己的情况 ---> 一定得有终结点
"""
    jc(10) = 10 * jc(9)
    jc(9) = 9 * jc(8)
    jc(8) = 8 * jc(7)
    jc(7) = 7 * jc(6)
    jc(6) = 6 * jc(5)
    jc(5) = 5 * jc(4)
    jc(4) = 4 * jc(3)
    jc(3) = 3 * jc(2)
    jc(2) = 2 * jc(1)
    jc(1) = 1
"""
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)
print(jc(10))

"""
    案例2：定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数
    具体规则如下：
        1．优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
        2，积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）
"""
def calc_order_cost(*args,coupon=0,score=0,express=0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量）
    :param coupon: 优惠券
    :param score: 积分抵扣
    :param express: 运费
    :return: 订单的总金额
    """
    # 算订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    # 1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cots =sum(total_price)

    # 2.扣减优惠券(优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价)
    if total_cots > 5000 and coupon < total_cots:
        total_cots -= coupon

    # 3.扣减积分抵扣(积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）)
    if total_cots > 5000 and score // 100 < total_cots:
        total_cots -= score // 100

    # 4.添加运费
    total_cots += express

    return total_cots

# 测试
total = calc_order_cost(("鼠标",188,2),("键盘",388,1),("手机",3999,1),coupon=10,score=4000,express=9.9)
print(total)