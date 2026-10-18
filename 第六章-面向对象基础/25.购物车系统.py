# 商品类
class Goods:
    def __init__(self,name,price,num):
        """
        商品类的基础信息
        :param name: 商品名字
        :param price: 商品价格
        :param num: 数量
        """
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称：{self.name} | 商品价格：{self.price} | 商品数量：{self.num}"

    # 修改商品数量和价格
    def update_price_num(self,price=None,num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num

# 购物车系统类
class ShoppingCart:
    system_version = "1.0"
    system_name = "购物车系统"
    def __init__(self):
        # 用列表记录购物车中物品的信息
        self.goods_list = []

    # 添加商品到购物车
    def add_good(self):
        name = input("请输入商品名：")

        # 判断商品是否存在，如果存在，则添加失败（不能重复添加）
        for s in self.goods_list:
            if s.name == name:
                print("该商品已经存在，添加失败~")
                return

        price = float(input("请输入商品的价格："))
        num = int(input("请输入商品的数量："))
        good = Goods(name,price,num)
        self.goods_list.append(good)
        print("添加成功")
        return

    # 修改购物车
    def update_goods(self):
        name = input("请输入要修改的商品名称：")
        for s in self.goods_list:
            if s.name == name:
                print(f"商品信息：\n{s}")
                price = float(input("请输入商品修改后的价格:"))
                num = int(input("请输入商品修改后的数量:"))
                s.update_price_num(price,num)
                return print(f"现在的商品信息：\n{s}")
        return print("该商品不存在于购物车中")

    # 删除购物车中的商品
    def def_goods(self):
        name = input("请输入要删除的商品名称：")
        for s in self.goods_list:
            if s.name == name:
                self.goods_list.remove(s)
                return print("删除完成~")
        return print("该商品不存在于购物车中")

    # 查询购物车
    def list_goods(self):
        for s in self.goods_list:
            print(s)

    # 运行系统
    def run(self):
        print(f"欢迎使用购物车系统 {ShoppingCart.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加商品    2.修改商品    3.删除商品    4.查询购物车    5.退出系统          #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()
            choice = int(input("请选择要执行的操作，输入1 - 5:"))
            match choice:
                case 1:  # 添加商品
                    self.add_good()
                case 2:  # 修改商品
                    self.update_goods()
                case 3:  # 删除商品
                    self.def_goods()
                case 4:  # 查询购物车
                    self.list_goods()
                case 5:  # 退出系统
                    break
                case _:
                    print("输入错误！！！")
        return print("系统结束运行!!!")

# 测试
if __name__ == "__main__":
    shopping_cart = ShoppingCart()
    shopping_cart.run()
