"""
==========================
  11-函数高阶实战 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:lambda 加法
add = lambda x, y: x + y
print(add(3, 5))  # 8

# 题目 2:lambda + sort 排序
words = ["Python", "Java", "Go", "JavaScript", "C"]
words.sort(key=lambda w: len(w))
print(words)  # ['C', 'Go', 'Java', 'Python', 'JavaScript']

# 题目 3:递归求和
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(100))  # 5050

# 题目 4:递归阶乘
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# 题目 5:函数作为参数
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def calc(x, y, oper):
    return oper(x, y)

print(calc(10, 5, add))  # 15
print(calc(10, 5, sub))  # 5
print(calc(10, 5, mul))  # 50
print(calc(10, 5, div))  # 2.0

# 题目 6:综合挑战(力扣风格)两数之和
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
