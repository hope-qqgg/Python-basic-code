# __all__ 指定 from ... import * 导入的是那些功能
__all__ = ["log_separator1","log_separator3","PI"]

# 常量（不会变化的数据；常量的名称为全部大写）
PI = 3.1415926
NAME = "H0PEO_o"

# 函数
def log_separator1():
    print("- " * 30)

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

# 测试函数
# log_separator1() # ---> 调用模块时也会执行
# __name__:Python中内置变量，表示的是当前模块的名字（直接运行模块，__name__的值为"__main__"；当模块被导入时，__name__的值为模块名）
# 执行当前文件，则会执行如下代码；如果被当作模块导入，不会执行
if __name__ == "__main__":
    log_separator1()