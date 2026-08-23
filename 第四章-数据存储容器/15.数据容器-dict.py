# 字典 -- key不能重复（如果重复，后面的值，会覆盖前面的值）、key必须是不可变类型（str，int，float，tuple）
# 定义字典
dict1 = {"王林":670,"李慕婉":608,"小明":580,"王维":688}

print(dict1)
print(type(dict1))

# key必须是不可变类型（str，int，float，tuple），不能是 list、set、dict
dict2 = {0:670,1.5:608,(1,2):580,"aa":661}
print(dict2)

# 访问
print(dict1["李慕婉"]) # 获取
dict1["李慕婉"] = 985 # 修改
print(dict1)
print("------------------------------")

#------------------------------ 字典 常见操作 ------------------------------
dict_1 = {"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
print(dict_1)

# 添加 - key不存在就是添加
dict_1["涛哥"] = 553
print(dict_1["涛哥"])

# 修改 - key存在就是修改
dict_1["涛哥"] = 661
print(dict_1["涛哥"])

# 查询
print(dict_1["涛哥"]) # 根据key获取value
print(dict_1.get("涛哥")) # 根据key获取value

print(dict_1.keys()) # 获取所有的key
print(dict_1.values()) # 获取所有的value
print(dict_1.items()) #获取所有的键值对 key：value

# 删除
score = dict_1.pop("许立国")
print(score)
print(dict_1)

del dict_1["韩立"]
print(dict_1)

# 遍历
for k in dict_1.keys():
    print(f"{k} : {dict_1[k]}")

for item in dict_1.items():
    print(f"{item[0]} : {item[1]}")

for k,v in dict_1.items():
    print(f"{k} : {v}")

#------------------------------ 案例 ------------------------------
"""
完成如下需求
●开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，
通过控制台菜单与用户交互。具体功能如下：
    1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：×X×，商品价格：×Xx，商品数量：xxx"。
    5.退出购物车
"""
# 1.制作菜单
shopping_cart = {}
print("欢迎使用购物车管理系统")
xuan_ze_cai_dan = """
########## 购物系统 ##########
#        1.添加购物车        #
#        2.修改购物车        #
#        3.删除购物车        #
#        4.查询购物车        #
#        5.退出购物车        #
#############################
"""
print(xuan_ze_cai_dan)

# 2.执行操作
while True:
    choice = input("请选择要执行的操作（1~5）：")
    match choice:
        case "1":  # 添加购物车
            while True:
                product_name = input("请输入商品名称：")
                if product_name in shopping_cart:
                    print("商品已经存在，请重新操作~")
                    continue
                else:
                    commodity_prices = float(input("请输入商品价格："))
                    num = int(input("请输入商品数量："))
                    shopping_cart[product_name] = {"cp":commodity_prices,"nu":num}
                home_1 = input("输入 1 继续添加商品、2 返回选择菜单：")
                match home_1:
                    case "1":
                        continue
                    case "2":
                        break
                continue
        case "2":  # 修改购物车
            while True:
                product_name = input("请输入要修改的商品名称：")
                if product_name not in shopping_cart:
                    print("商品不存在，请重新操作~")
                else:
                    commodity_prices = float(input("请输入商品的新价格："))
                    num = int(input("请输入商品的新数量："))
                    shopping_cart[product_name] = {"cp":commodity_prices,"nu":num}
                home_1 = input("输入 1 继续修改商品、2 返回选择菜单：")
                match home_1:
                    case "1":
                        continue
                    case "2":
                        break
                continue
        case "3":  # 删除购物车
            while True:
                product_name = input("请输入要删除的商品名称：")
                if product_name not in shopping_cart:
                    print("商品不存在，请重新操作~")
                else:
                    del shopping_cart[product_name]
                    print("删除成功~")
                home_1 = input("输入 1 继续删除商品、2 返回选择菜单：")
                match home_1:
                    case "1":
                        continue
                    case "2":
                        break
                continue
        case "4":  # 查询购物车
            for item in shopping_cart.keys():
                cn = shopping_cart[item]
                print(f"商品名称：{item} \t 商品价格：{cn["cp"]} \t 商品数量：{cn["nu"]}")
            print("到底了")
            home = input("输入 1 返回选择菜单：")
            if home == "1":
                continue
        case "5":  # 退出购物车
            break
        case _:
            print("请输入正确的操作（1~5）：")
            continue

