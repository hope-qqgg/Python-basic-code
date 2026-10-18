# 异常处理
try:
    print("=========================================")
    # print(my_name)
    # print(1/0)
    # print("abc"[10])
    print("abc".hello)
    print("=========================================")
except NameError as e: # 捕获NameError 类型的异常
    print("程序运行出错,错误信息：\n",e)
except ZeroDivisionError as e:
    print("程序运行出错,错误信息：\n", e)
except IndexError as e:
    print("程序运行出错,错误信息：\n", e)
except Exception as e: # 捕获所有异常
    print("程序运行出错,错误信息：\n", e)
finally: # 无论程序是否异常都会执行 
    print("释放资源~")