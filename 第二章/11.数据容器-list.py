# 列表操作
# 定义列表 - list
s = [56,90,88,65,90,"A","Hello",True]
print(type(s))

# 访问列表元素
# 获取
print(s[0]) # 正向索引
print(s[-8]) # 反向索引
print(s[2])
print(s[-6])

# 修改
print(s[5])# 未修改
s[5] = "探索未至之境"
print(s[5])


# 删除
print(s)
del s[6]
print(s)

# 遍历
for item in s:
    print(item)
print("------------------------------")

#------------------------------ 列表 list 切片 ------------------------------
# 定义列表
s = ["A","C","H","K","L","B","D","X","C","U"]

# 切片操作 s[开始索引:结束索引:步长]
print(s[:5]) # 截取前面5个元素,步长为1
print(type(s[:5]))
print(s[0:5:2])
print(s[0:-2:1])
print("------------------------------")

#------------------------------ 列表 list 常用方法 ------------------------------
# 列表定义
s = [56,90,88,90,65,100,209,72,145]
print(s)

# append()：在列表末尾追加元素
s.append(188)
print(s)

# insert(n,m)：在指定索引n之前，插入元素m
s.insert(2,80)
print(s)

# remove()：移除列表中第一个匹配到的元素
s.remove(90)
print(s)

# pop()：删除指定索引位置的元素并返回（如果未指定，默认删除最后一个）
e = s.pop(1)
print(e)

e = s.pop()
print(e)

print(s)

# sort()：排序
s.sort() # 默认从小到大
print(s)

# reverse()：反转列表元素
s.reverse()
print(s)
print("------------------------------")

#------------------------------ 列表 list 案例1 ------------------------------
# 将用户输入的10个数字,存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值。
# 1.定义列表
num_list = []

# 2.将用户输入的10个数字存入列表
for i in range(10):
    num = int(input(f"请输入第{i + 1}个有效数字："))
    num_list.append(num)
print(f"未排序的列表{num_list}")

# 3.排序
num_list.sort()
print(f"排序完成的列表{num_list}")

# 4.输出其中的最小值、最大值和平均值
print(f"最小值{num_list[0]}")
print(f"最大值{num_list[-1]}")
print(f"平均值{sum(num_list) / len(num_list)}") #sum() 求和，len() 获取元素个数
print("------------------------------")

#------------------------------ 列表 list 案例2 ------------------------------
# 合并两个列表中的元素，并去除重复元素
num_list1 = [19,23,54,64,875,20,109,232,54]
num_list2 = [55,89,72,35,60,123,20,54,91]

# 1.合并列表
for num in num_list2:
    num_list1.append(num)
print(f"合并后的列表{num_list1}")

# 2.去除重复元素
num_list = [] # 记录去除重复元素的新列表
for num in num_list1 + num_list2:
    if num not in num_list: # 判断 num是否在 num_list中，不在就加到新列表 num_list中
        num_list.append(num)
print(f"去除重复元素的新列表{num_list}")

# 方法二：
# 1.合并列表
new_list = [*num_list1,*num_list2] # 解包
print(f"合并后的列表{new_list}")

# 2.去除重复元素
num_list = [] # 记录去除重复元素的新列表
for num in num_list1 + num_list2:
    if num not in num_list: # 判断 num是否在 num_list中，不在就加到新列表 num_list中
        num_list.append(num)
print(f"去除重复元素的新列表{num_list}")

# 方法三：
# 1.合并列表
new_list = num_list1 + num_list2 # 解包
print(f"合并后的列表{new_list}")

# 2.去除重复元素
num_list = [] # 记录去除重复元素的新列表
for num in num_list1 + num_list2:
    if num not in num_list: # 判断 num是否在 num_list中，不在就加到新列表 num_list中
        num_list.append(num)
print(f"去除重复元素的新列表{num_list}")
print("------------------------------")

#------------------------------ 列表 list 案例3 ------------------------------
#生成1 ~ 20的平方列表
num_list = []
for num in range(1,21):
    num_list.append(num**2)
print(f"1 ~ 20的平方列表为：{num_list}")

# 方法二：列表推导式 ---> [要输入的值 for num in 列表/序列]
num_list = [num**2 for num in range(1,21)]
print(f"1 ~ 20的平方列表为：{num_list}")
print("------------------------------")

#------------------------------ 列表 list 案例4 ------------------------------
# 从一个数字列表中提取所有偶数，并计算平方，组成一个新列表
num_list = [12,32,45,77,80,92,33,57,97,98,110,111,122]
new_list = [i**2 for i in num_list if i % 2 == 0] # 列表推导式二 ---> [要输入的值 for num in 列表/序列 if 条件]
print(new_list)