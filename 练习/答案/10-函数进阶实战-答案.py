"""
==========================
  10-函数进阶实战 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:默认参数
def register(name, age, gender="男", city="北京"):
    print(f"注册成功:{name}, {age}岁, {gender}, {city}")

register("张三", 20)
register("李四", 18, "女", "上海")

# 题目 2:关键字参数
register(city="广州", name="王五", age=22, gender="男")

# 题目 3:不定长位置参数 *args
def my_sum(*nums):
    return sum(nums)

print(my_sum(1, 2, 3))                 # 6
print(my_sum(10, 20, 30, 40, 50))      # 150

# 题目 4:不定长关键字参数 **kwargs
def show_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

show_info(姓名="小明", 年龄=18, 城市="北京")

# 题目 5:global 修改全局变量
count = 0

def add_count():
    global count
    count += 1

add_count()
add_count()
add_count()
print(count)  # 3

# 题目 6:综合挑战:成绩统计函数(*args 版)
def calc_scores(*scores):
    avg = round(sum(scores) / len(scores), 1)
    pass_count = len([s for s in scores if s >= 60])
    return max(scores), min(scores), avg, pass_count

print(calc_scores(85, 92, 78, 55, 90, 88))  # (92, 55, 81.3, 5)
