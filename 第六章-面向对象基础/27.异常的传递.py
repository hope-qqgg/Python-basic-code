# 异常的传递
def fun1():
    print("fun ... running ...")
    fun2()

def fun2():
    print("fun ... running ...")
    fun3()

def fun3():
    print("fun ... running ...")
    print(my_name)

if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print("程序运行出错,错误信息：\n", e)