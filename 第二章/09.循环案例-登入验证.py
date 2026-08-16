""""
    ●需求：根据输入的用户名密码执行登录操作，具体要求如下：)
    1.正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
    2，输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
    3．输入的用户名和密码不能为空！
    4.登录成功：输出"登录成功，进入B站首页~”
    5．登录失败：输出“用户名或密码错误，请重新输入！”

    关键字：
        break：只能出现在循环中，表示结束循环（break跳出循环时，while后面的else中的代码将不会执行）
        continue：只能出现在循环中，表示跳过本次循环
"""
while True:
    # 1.键盘输入用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 2.校验：用户名和密码不能为空
    if username == "" or password == "":
        print("用户名或密码不能为空！")
        continue # 跳过本次循环，继续下一次循环
    # 3.判断用户名和密码是否正确
    if username == "admin" and password == "666888":
        print("登录成功，进入B站首页~")
        break # 结束循环
    elif username == "zhangsan" and password == "123456":
        print("登录成功，进入B站首页~")
        break # 结束循环
    elif username == "taoge" and password == "888666":
        print("登录成功，进入B站首页~")
        break # 结束循环
    else:
        print("用户名或密码错误，请重新输入！")
