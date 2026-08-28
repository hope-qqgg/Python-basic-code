# # 定义类
# class Car: # 类名定义要遵循大驼峰命名法
#     pass
#
# # 创建对象
# c1 = Car()
# # 动态的为对象添加属性 ---> 不推荐
# c1.color = "红色"
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 500000
#
# print(c1) # 默认是输出16进制的内存地址
# print(c1.brand)
# print(c1.__dict__) # 会将对象中的所有属性以字典的形式输出

# # 定义类
# class Car:
#     # __init__ 方法是初始化的方法，会在创建对象时自动调用，可以在该方法中为对象设置对应的属性
#     # self：是第一个参数，表示当前所创建出来的实例对象
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.coler = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕")
#
# # 创建对象
# c1 = Car("红色","BMW","X5",500000)
# print(c1.__dict__)
#
# c2 = Car("红色","BMW","E300",500000)
# print(c1.__dict__)

#------------------------------ 定义类 实例方法 ------------------------------
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.coler = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕")
#
#     # 定义实例方法
#     def running(self):
#         print(f"{self.brand}{self.name} 正在高速行驶中......")
#
#     def total_cost(self,discount,rate=0.1):
#         """
#         计算提车的总费用，包含两个部分：车的价格，税费
#         :param discount: 折扣
#         :param rate: 税费
#         :return: 提车的总费用
#         """
#         total_cost = self.price * discount + rate * self.price
#         return total_cost
#
# # 测试
# c1 = Car("红色","BMW","X5",500000)
#
# # 调用对象中的方法
# c1.running()
# print(c1.total_cost(0.9))

#------------------------------ 定义类 魔法方法 ------------------------------
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.coler = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕")
#
#     def running(self):
#         print(f"{self.brand}{self.name} 正在高速行驶中......")
#
#     def total_cost(self,discount,rate=0.1):
#         """
#         计算提车的总费用，包含两个部分：车的价格，税费
#         :param discount: 折扣
#         :param rate: 税费
#         :return: 提车的总费用
#         """
#         total_cost = self.price * discount + rate * self.price
#         return total_cost
#
#     # 魔法方法
#     def __str__(self):
#         return f"{self.coler},{self.brand},{self.name},{self.price}"
#
#     def __eq__(self, other):
#         return self.coler == other.coler and self.price == other.price and self.brand == other.brand and self.name == other.name
#
#     def __lt__(self, other):
#         return self.price < other.price
#
# # 测试
# c1 = Car("红色","BMW","X5",500000)
# print(c1)
#
# c2 = Car("红色","BMW","X5",500000)
# print(c2)
#
# print(c1 == c2) # 默认比较地址
#
# print(c1 < c2) # 默认无法比较大小

#------------------------------ 实例属性 与 类属性 ------------------------------
class Car:
    # 类属性
    wheel = 4 # 轮胎的数量
    tax_rate = 0.1 # 购置的税率

    def __init__(self,c_color,c_brand,c_name,c_price):
        # 实例属性（所有实例对象共享的）
        self.coler = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 2
        print("Car 类型的对象初始化完毕，对象属性已经添加完毕")

    def running(self):
        print(f"{self.brand}{self.name} 正在高速行驶中......")

    def total_cost(self,discount,rate=0.1):
        """
        计算提车的总费用，包含两个部分：车的价格，税费
        :param discount: 折扣
        :param rate: 税费
        :return: 提车的总费用
        """
        total_cost = self.price * discount + rate * self.price
        return total_cost

# 测试
c1 = Car("红色","BMW","X5",500000)
print(c1.brand)
print(c1.wheel) # 通过实例对象，查找属性时，会先查找实例属性。实例属性不存在在查找类属性