"""
==========================
  04-列表实战 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:成绩统计
scores = []
for i in range(5):
    s = int(input(f"请输入第{i + 1}个成绩:"))
    scores.append(s)
print(f"成绩列表:{scores}")
print(f"平均分:{sum(scores) / len(scores)}")
print(f"最高分:{max(scores)}")
print(f"最低分:{min(scores)}")

# 题目 2:合并去重
list1 = [3, 1, 4, 1, 5]
list2 = [9, 2, 6, 5, 3]
new_list = []
for num in list1 + list2:
    if num not in new_list:
        new_list.append(num)
new_list.sort()
print(f"合并去重排序后:{new_list}")

# 题目 3:朋友名单管理
friends = ["小明", "小红", "小刚"]
while True:
    print("\n===== 朋友名单管理 =====")
    print("1.查看名单  2.添加朋友  3.删除朋友  4.修改朋友  0.退出")
    choice = input("请选择:")
    if choice == "1":
        if len(friends) == 0:
            print("名单还是空的")
        else:
            for i, name in enumerate(friends):
                print(f"{i + 1}.{name}")
    elif choice == "2":
        name = input("请输入新朋友的名字:")
        friends.append(name)
        print(f"已添加 {name}")
    elif choice == "3":
        name = input("请输入要删除的朋友名字:")
        if name in friends:
            friends.remove(name)
            print(f"已删除 {name}")
        else:
            print("名单里没有这个人")
    elif choice == "4":
        name = input("请输入要修改的朋友名字:")
        if name in friends:
            new_name = input("请输入新名字:")
            friends[friends.index(name)] = new_name
            print(f"已把 {name} 改为 {new_name}")
        else:
            print("名单里没有这个人")
    elif choice == "0":
        print("再见!")
        break
    else:
        print("输入错误,请重新选择")

# 题目 4:列表推导式
result = [x ** 2 for x in range(1, 31) if x % 3 == 0]
print(f"1~30 中能被3整除的数的平方:{result}")

# 题目 5:反转练习
print([1, 2, 3, 4, 5][::-1])
print("Hello-Python"[::-1])
