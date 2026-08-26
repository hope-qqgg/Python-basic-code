"""
==========================
  12-模块与包实战 参考答案
  建议:先独立完成,再看答案对照
  使用前提:把 答案/my_tools.py 复制到本文件同目录(练习/目录)下
==========================
"""

# 题目 1:import 整个模块
import my_tools

print(my_tools.c_to_f(100))  # 212.0
print(my_tools.is_prime(7))  # True
print(my_tools.is_prime(8))  # False
print(my_tools.gcd(12, 18))  # 6

# 题目 2:from ... import ... 导入指定函数
from my_tools import is_prime
print(is_prime(13))  # True

# 题目 3:别名导入
import my_tools as mt
print(mt.c_to_f(37))  # 98.6
print(mt.gcd(24, 36))  # 12

# 题目 4:自由挑战 —— 调用新增的 avg_score
print(my_tools.avg_score([85, 92, 78]))  # 85.0
