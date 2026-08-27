# 变量定义 - 未指定类型注释 ---> 类型推断
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A","B","C","E"]
phones = {"15905036358","13015906597","859737571"}
options = {"count":2,"total":10}
goods = ("手机",6999,1)

names.append("X")
names.append(10010)
print(names)

# 变量定义 - 指定类型注释
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int] = ["A","B","C","E"]
phones2: set[str] = {"15905036358","13015906597","859737571"}
options2: dict[str, int] = {"count":2,"total":10}
goods2:tuple[str, int, int] = ("手机",6999,1)

# Python是动态类型语言，添加的类型注解只是提示，并不是强制约束！！!
names2.append("X")
names2.append(10010)
names2.append(10010.1)
print(names2)

# 函数类型注释：
def circle_len(r:float) -> tuple[float, float]:
    """
    该函数用于根据圆的半径，计算圆的面积、周长
    :param r: 半径
    :return: (面积,周长)
    """
    return  round(3.14 * r * r,1),round(2 * 3.14 * r,1)

al = circle_len(8.5)
print(al)

def calc_order_cost(*args:tuple[str, float, int],coupon=0,score=0,express=0) -> float:
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