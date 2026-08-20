# 集合 set ---> 无序，不可重复，可修改
# 定义
s1 = {5,3,2,0,9,12,43,64,22,5,0}

print(s1)
print(type(s1))

s2 = set()
print(s2)
print(type(s2))

s3 = {} # 直接 {}是字典不是集合
print(s3)
print(type(s3))

#------------------------------ 集合常用方法 ------------------------------
# add()；添加元素到集合
se1 = {100,200,300,400,500,600,700,800,900}
print(se1)

se1.add(1000)
print(se1)

# remove()：移除集合中的指定元素（指定元素不存在将报错）
se1.remove(200)
print(se1)

# pop()：随机删除集合中的元素并返回
e = se1.pop()
print(e)
print(se1)

# clear()：清空集合
se1.clear()
print(se1)

se2 = {"A","B","C","D","E","X","Y"}
se3 = {"C","E","Y","Z"}
# difference()：求两个集合的差集（存在与第一个合集，但不在第二个合集）
print(se2.difference(se3))

# union()：求两个集合的并集
print(se2.union(se3))
print(se3.union(se2))

# intersection()：求两个集合的交集
print(se2.intersection(se3))
print(se3.intersection(se2))

#------------------------------ 案例 ------------------------------
"""
    根据提供的班级学生的选课情况，完成如下需求：
        1，找出同时选修了法语和艺术的学生
        2，找出同时选修了所有四门课程的学生
        3.找出选修了足球，但是没有选修篮球的学生
        4.统计每一个学生选修的课程数量
"""

#选修足球学生名单
football_set ={"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
#选修篮球学生名单
basketball_set ={"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
#选修法语学生名单
french_set={"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
#选修艺术学生名单
art_set={"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

# 1，找出同时选修了法语和艺术的学生 ---> 求 french_set 和 art_set 的交集
# 方法一：
fa_set = french_set.intersection(art_set)
print(f"同时选修了法语和艺术的学生{fa_set}")
# 方法二：& ---> 交集
fa2_set = french_set & art_set
print(f"同时选修了法语和艺术的学生{fa2_set}")

# 2，找出同时选修了所有四门课程的学生 ---> football_set,basketball_set,french_set,art_set 的交集
# 方法一.1：使用 intersection() 传入多个参数
fbfa1_set = football_set.intersection(basketball_set, french_set, art_set)
print(f"同时选修了所有四门课程的学生{fbfa1_set}")
# 方法一.2：链式调用 intersection()
fbfa1_set1 = football_set.intersection(basketball_set).intersection(french_set).intersection(art_set)
print(f"同时选修了所有四门课程的学生{fbfa1_set1}")
# 方法二：
fbfa2_set = football_set & basketball_set & french_set & art_set
print(f"同时选修了所有四门课程的学生{fbfa2_set}")

# 3.找出选修了足球，但是没有选修篮球的学生 ---> 求 football_set 与 basketball_set 的差集
# 方法一：
f_b_set = football_set.difference(basketball_set)
print(f"选修了足球，但是没有选修篮球的学生{f_b_set}")
# 方法二：- ---> 差集
f_b_set2 = football_set - basketball_set
print(f"选修了足球，但是没有选修篮球的学生{f_b_set2}")
# 方法三：集合推导式 ---> {要输入的值 for num in 列表/序列 if 条件}
f_b_set3 = {j for j in football_set if j not in basketball_set}
print(f"选修了足球，但是没有选修篮球的学生{f_b_set3}")

# 4.统计每一个学生选修的课程数量
# 4.1 获取学生名单 ---> 求 football_set,basketball_set,french_set,art_set 的并集
# 方法一：
fbfa3_set = football_set.union(basketball_set,french_set,art_set)
print(f"学生名单{fbfa3_set}")
# 方法二：| ---> 并集
fbfa3_set1 = football_set | basketball_set | french_set | art_set
print(f"学生名单{fbfa3_set1}")
# 4.2 统计每一个学生选修的课程数量
tj_list = [*football_set,*basketball_set,*french_set,*art_set]
for n in fbfa3_set1:
    print(f"{n} 选修了 {tj_list.count(n)} 门课程")