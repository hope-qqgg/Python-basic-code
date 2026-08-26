# my_tools.py — 参考答案版工具模块
# 用法:把这个文件放到 练习/ 目录下,就能被 12-模块与包实战.py 导入

def c_to_f(c):
    """摄氏温度转华氏温度"""
    return c * 9 / 5 + 32

def is_prime(n):
    """判断 n 是否为素数(质数)"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """计算 a 和 b 的最大公约数(辗转相除法)"""
    while b != 0:
        a, b = b, a % b
    return a

def avg_score(scores):
    """计算成绩列表的平均分(保留1位)"""
    return round(sum(scores) / len(scores), 1)
