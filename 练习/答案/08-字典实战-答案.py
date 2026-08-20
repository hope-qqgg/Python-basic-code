"""
==========================
  08-字典实战 参考答案
  建议:先独立完成,再看答案对照
==========================
"""

# 题目 1:字典基础操作
score = {"王林": 92, "李慕婉": 88, "韩立": 75}
print(score["李慕婉"])   # 88 查询
score["韩立"] = 80        # 修改(key 存在 → 修改)
score["曾牛"] = 95        # 添加(key 不存在 → 添加)
del score["王林"]         # 删除
print(score)
print(score.keys())       # 所有名字
print(score.values())     # 所有成绩

# 题目 2:get() 的妙用
print(score.get("不存在的人"))        # None,不报错
# print(score["不存在的人"])          # ← 打开这行会报 KeyError,试试再注释掉
print(score.get("不存在的人", 0))     # 0 默认值

# 题目 3:遍历字典
for k in score.keys():
    print(k)              # 只拿名字
for v in score.values():
    print(v)              # 只拿成绩
for k, v in score.items():
    print(f"{k}: {v}")    # 名字和成绩

# 题目 4:单词计数器
text = "hello python hello world python"
words = text.split()
word_count = {}
for w in words:
    word_count[w] = word_count.get(w, 0) + 1
print(word_count)  # {'hello': 2, 'python': 2, 'world': 1}

# 题目 5:综合挑战:通讯录系统
contacts = {"小明": "13800000001", "小红": "13900000002"}
while True:
    print("\n===== 通讯录 =====")
    print("1.查看全部  2.添加  3.查找  4.删除  0.退出")
    choice = input("请选择:")
    if choice == "1":
        if len(contacts) == 0:
            print("通讯录是空的")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif choice == "2":
        name = input("请输入姓名:")
        phone = input("请输入电话:")
        contacts[name] = phone
        print("添加成功")
    elif choice == "3":
        name = input("请输入要查找的姓名:")
        if name in contacts:
            print(f"{name} 的电话是 {contacts[name]}")
        else:
            print("通讯录里没有这个人")
    elif choice == "4":
        name = input("请输入要删除的姓名:")
        if name in contacts:
            del contacts[name]
            print("删除成功")
        else:
            print("通讯录里没有这个人")
    elif choice == "0":
        print("再见!")
        break
    else:
        print("输入错误,请重新选择")
