"""
==========================
  06-元组实战 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:元组基础操作
t = (88, 92, 76, 88, 95)
print(t[2])         # 76
print(t[-1])        # 95
print(t[:3])        # (88, 92, 76)
print(t.count(88))  # 2
print(t.index(76))  # 2

# 题目 2:单元素元组陷阱
a = (100)
b = (100,)
print(type(a))  # <class 'int'>  ← 没有逗号,() 只是数学括号,所以是整数
print(type(b))  # <class 'tuple'> ← 加了逗号才是元组!

# 题目 3:解包练习
scores = (85, 90, 78)
x, y, z = scores
print(x, y, z)  # 85 90 78

nums = (1, 2, 3, 4, 5, 6)
first, *middle, last = nums
print(first)    # 1
print(middle)   # [2, 3, 4, 5] ← 注意:*收集到的是列表!
print(last)     # 6

# 题目 4:变量交换
a = 30
b = 50
a, b = b, a
print(a, b)  # 50 30

# 题目 5:综合挑战:学生成绩统计
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
)

# 1. 每个人的总分和平均分
print("姓名 \t 总分 \t 平均分")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[1]} \t {total} \t {avg:.2f}")

# 2. 平均分最高的人(边循环边比较)
top_name = ""
top_avg = 0
for s in students:
    avg = (s[2] + s[3] + s[4]) / 3
    if avg > top_avg:
        top_avg = avg
        top_name = s[1]
print(f"平均分最高:{top_name},{top_avg:.2f}")

# 3. 平均分大于 85 的人
print("平均分大于85的人:")
for s in students:
    avg = (s[2] + s[3] + s[4]) / 3
    if avg > 85:
        print(f"{s[1]} 平均分 {avg:.2f}")
