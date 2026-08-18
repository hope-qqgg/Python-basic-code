# # # 字符串 基本操作 ---> 不可变（无法修改）、有序性、可迭代性
# # s = "Hello-Python"
# #
# # print(s[4]) # 正向索引
# # print(s[-8]) # 反向索引
# #
# # for i in s:
# #     print(i)
# #
# # # 切片
# # print(s[0:5:1])
# # print(s[:5:1])
# # print(s[:5:])
# # print(s[:5])
# #
# # # 步长 ---> 正数：从前往后截取：负数：从后往前截取
# # print(s[:5:-1])
#
# #------------------------------ 字符串常用方法 ------------------------------
# s = " Hello-Python-Hello-World "
#
# # find() 查找指定字符串第一次出现的索引的位置
# f = s.find("-")
# print(f)
#
# # cont() 统计指定子字符串在指定字符串出现的次数
# c = s.count("Hello")
# print(c)
#
# # upper() 转换成大写
# su = s.upper()
# print(su)
#
# # lower() 转换成小写
# sl = s.lower()
# print(sl)
#
# # split() 将字符串按指定字符串切割 - 列表
# slist = s.split("-")
# print(slist)
#
# # strip() 去除字符串两端空格
# ss = s.strip()
# print(ss)
#
# # replace() 将字符串的指定子字符串替换为新内容
# sr = s.replace("-","_")
# print(sr)
#
# # startswith() / endswith 判断字符串是否以指定的字符串开头 / 结尾，返回布尔值
# print(s.startswith(" Hello"))
# print(s.endswith("Python "))
#
# print("------------------------------")
#
# # 原始字符串不会发生变化
# print(s)
#
# #------------------------------ 字符串案例 ------------------------------
# # 案例1：邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.），如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"。
# # 1.接收用户输入的邮箱
# mail = input("请输入邮箱：")
#
# # 2.判断邮箱格式
# if mail.count("@") == 1 and mail.count(".") >= 1:
#     print(f"邮箱：{mail}格式正确")
# else:
#     print(f"邮箱：{mail}格式错误")
#
# # 方法二
# # 1.接收用户输入的邮箱
# mail = input("请输入邮箱：")
#
# # 2.判断邮箱格式
# if mail.count("@") == 1 and "." in mail:
#     print(f"邮箱：{mail}格式正确")
# else:
#     print(f"邮箱：{mail}格式错误")
#
# #------------------------------ 字符串练习 ------------------------------
# # 1．输入一个字符串，判断该字符串是否是回文（两边对称）。
# # 1.输入一个字符串
# hui_wen = input("请输入一个字符串：")
#
# # 2.判断该字符串是否是回文
# fan_hui_wen = hui_wen[::-1]
# if fan_hui_wen == hui_wen:
#     print(f"“{hui_wen}”是回文")
# else:
#     print(f"“{hui_wen}”不是回文")

# 2，将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。
# 1.输入10个字符串
zi_fu_chuan = input("")

# 2.反转
fan = zi_fu_chuan[::-1]

# 3.转换为大写
fan_u = fan.upper()

# 4.遍历
for i in fan_u:
    print(i)

# 1.创建一个空列表用于存储结果
result_list = []

# 2.循环10次，接收用户输入的字符串
for i in range(10):
    # 接收用户输入的字符串
    s = input(f"请输入第{i + 1}个字符串：")

    # 3.反转字符串
    reversed_s = s[::-1]

    # 4.转换为大写
    upper_s = reversed_s.upper()

    # 5.将处理后的字符串添加到列表中
    result_list.append(upper_s)

# 6.遍历列表输出结果
print("处理结果：")
for i, item in enumerate(result_list):
    print(f"第{i + 1}个字符串：{item}")
