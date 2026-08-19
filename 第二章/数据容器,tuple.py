# 元组基本操作 - tuple ---> 元素可重复，有序，不可修改

# 定义
t1 = (80,95,78,50,76,80,85,20)

print(t1)
print(type(t1))

# 索引访问
print(t1[0])
print(t1[-1])

# 切片
print(t1[:5])

# cout() 统计元素个数
print(t1.count(80))

# index() 获取元素的索引（第一个元素的位置）
print(t1.index(80))

# 注意点：如果定义单元素的元组，单元素之后需要加逗号，比如(100,)
t2 = ()
print(t2)
print(type(t2))

t3 = (100)
print(t3)
print(type(t3))

t4 = (100,)
print(t4)
print(type(t4))

#------------------------------ 元组 tuple 组包与解包 ------------------------------
# 组包
tu1 = (5,7,9,10,2,23,12)
tu2 = 5,7,9,10,2,23,12

print(tu1)
print(tu2)


# 解包操作
# 基础解包（变量数量与容器的元素个数一样）
a,b,c,d,e,f,g = tu1
print(a,b,c,d,e,f,g)

# * 扩展解包 （* 收集剩余的所以元素，封装列表list中）
first,second,*other,last = tu1
print(first,second)
print(other)
print(last)

# 案例1.现有两个变量，分别为：a=10，b=20，现需要将这两个变量值交换，然后输出到控制台。
a = 10
b = 20
a,b = b,a
"""
t = a,b (组包)
a,b = t (解包)
"""
print(a)
print(b)

# 案例2.现有三个变量，分别为：a=100，b=200，c=300，现需要将这三个变量值进行交换，将a,b,c的值分别赋值给c,a,b，并将其输出到控制台。
a=100
b=200
c=300
a,b,c = c,a,b
print(a)
print(b)
print(c)

#------------------------------ 元组 tuple 练习 ------------------------------
"""
    根据如下提供的成绩单，完成如下需求：
        1.计算每个学生的总分、各科平均分，然后一起输出
        2.统计各科最低分、最高分、平均分，并输出
        3.查找成绩优秀（平均分大于90）的学生，并输出
"""
students =(
    ("S001","王林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周轶",95,96,89),
    ("S006","王卓",76,82,77),
    ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许木",86,89,98),
    ("S010","遁天",66,59,72)
)
# 1.计算每个学生的总分、各科平均分，然后一起输出
print("学号 \t 姓名 \t 总分 \t 平均分")
for s in students:
    total = s[2] + s[3] + s[4]
    average = total / 3
    print(f"{s[0]} \t {s[1]} \t {total} \t {average:.2f}")
print()

# 方法二
# 1.计算每个学生的总分、各科平均分，然后一起输出
print("学号 \t 姓名 \t 总分 \t 平均分")
for s in students:
    iD,name,yw,sx,yy = s
    total = yw + sx + yy
    average = total / 3
    print(f"{iD} \t {name} \t {total} \t {average:.2f}")
print()

# 2.统计各科最低分、最高分、平均分，并输出
language = [s[2] for s in students]
print(f"语文：最低分{min(language)} \t 最高分{max(language)} \t 平均分{sum(language) /len(language):.2f}")
math = [s[3] for s in students]
print(f"数学：最低分{min(math)} \t 最高分{max(math)} \t 平均分{sum(math) /len(math):.2f}")
english = [s[4] for s in students]
print(f"英语：最低分{min(english)} \t 最高分{max(english)} \t 平均分{sum(english) /len(english):.2f}")
print()

# 3.查找成绩优秀（平均分大于90）的学生，并输出
gr = [s[1] for s in students if (s[2] + s[3] + s[4]) / 3 >= 90]
print("成绩优秀（平均分大于90）的学生：")
for i in gr:
    print(i)



