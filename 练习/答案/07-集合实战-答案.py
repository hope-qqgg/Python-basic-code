"""
==========================
  07-集合实战 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:列表去重
lst = [5, 3, 8, 3, 9, 5, 3, 8]
s = set(lst)
print(s)          # {8, 9, 3, 5} 无序,已去重
print(list(s))    # 转回列表

# 题目 2:共同好友
my_friends = {"小明", "小红", "小刚", "小丽"}
your_friends = {"小刚", "小丽", "小强", "小华"}
print(my_friends & your_friends)   # 共同好友: {'小刚', '小丽'}
print(my_friends | your_friends)   # 全部好友
print(my_friends - your_friends)   # 只有我有: {'小红', '小明'}
print("小红" in my_friends)        # True

# 题目 3:选课分析
football = {"王林", "曾牛", "徐立国", "遁天"}
basketball = {"张铁", "墨居仁", "王林", "曾牛"}
print(football & basketball)       # 同时选两门
print(football - basketball)       # 只选足球
print(len(football | basketball))  # 参与选课总人数

# 题目 4:集合推导式
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s1 = {x ** 2 for x in lst if x % 2 == 0}
print(s1)  # {64, 4, 36, 100, 16} 偶数平方

s2 = {x ** 2 for x in range(1, 11)}
print(s2)  # 1~10 的平方集合

# 题目 5:综合挑战:朋友圈统计
a = {"王林", "曾牛", "韩立", "厉飞雨"}
b = {"曾牛", "韩立", "紫灵", "天运子"}
c = {"韩立", "紫灵", "厉飞雨", "云露"}

# 1. 三个人共同的好友
print(a & b & c)  # {'韩立'}

# 2. 至少出现在两个人朋友圈里的好友
two_or_more = (a & b) | (a & c) | (b & c)
print(two_or_more)
