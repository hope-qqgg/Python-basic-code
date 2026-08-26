"""
==========================
  09-函数基础实战 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:打招呼函数
def welcome():
    print("欢迎来到Python世界!")

welcome()
welcome()

# 题目 2:矩形面积函数
def rect_area(w, h):
    return w * h

print(f"5 × 8 的矩形面积是:{rect_area(5, 8)}")

# 题目 3:判断偶数函数
def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

# 题目 4:多返回值函数
def score_info(a, b, c):
    total = a + b + c
    avg = round(total / 3, 1)
    return total, avg

t, a = score_info(85, 92, 78)
print(f"总分:{t}, 平均分:{a}")

# 题目 5:综合挑战:成绩统计函数
def stats(scores):
    return max(scores), min(scores), round(sum(scores) / len(scores), 1)

print(stats([85, 92, 78, 90, 88]))  # (92, 78, 86.6)
