"""
==========================
  练习 08:字典实战
  用到的知识:dict 定义、增删改查、遍历、嵌套
  难度:★★★★☆
  规则:每道题先自己思考,卡住再看题下的【小提示】
==========================
"""
from nltk.corpus import words

# ------------------------------------------------------------
# 题目 1:字典基础操作
# 定义成绩字典 score = {"王林": 92, "李慕婉": 88, "韩立": 75}
# 1. 查询 "李慕婉" 的成绩
# 2. 把 "韩立" 的成绩改成 80
# 3. 添加新同学 "曾牛": 95
# 4. 删除 "王林"(用 del 或 pop)
# 5. 输出所有同学的名字(keys)和所有成绩(values)
# ------------------------------------------------------------
# 【小提示】
# 查询:score["名字"];修改/添加:score["名字"] = 新成绩
# key 存在就是修改,key 不存在就是添加!

# 您的代码写在这里 ↓↓↓
score = {"王林": 92, "李慕婉": 88, "韩立": 75}
# 1. 查询 "李慕婉" 的成绩
print(score["李慕婉"])

# 2. 把 "韩立" 的成绩改成 80
score["韩立"] = 80
print(score)

# 3. 添加新同学 "曾牛": 95
score["曾牛"] = 95
print(score)

# 4. 删除 "王林"(用 del 或 pop)
del score["王林"] # pop_score = score.pop("王林")

# 5. 输出所有同学的名字(keys)和所有成绩(values)
print(f"所有同学的名字：{score.keys()}")
print(f"所有同学的成绩：{score.values()}")
# ------------------------------------------------------------
# 题目 2:get() 的妙用
# 接着题目 1 的 score:
# 1. 用 score.get("不存在的人") 访问不存在的 key,输出结果(观察:不会报错,返回 None)
# 2. 用 score["不存在的人"] 访问,观察报错(把代码注释掉,保留注释说明)
# 3. 用 score.get("不存在的人", 0) 设置默认值,输出 0
# ------------------------------------------------------------
# 【小提示】
# get(key, 默认值):key 不存在时返回默认值,不会崩溃
# 这是字典最实用的安全访问方式

# 您的代码写在这里 ↓↓↓
print(score.get("不存在的人"))        # None,不报错
# print(score["不存在的人"])          # ← 打开这行会报 KeyError,试试再注释掉
print(score.get("不存在的人", 0))     # 0 默认值

# ------------------------------------------------------------
# 题目 3:遍历字典
# 用三种方式遍历 score:
# 1. for k in score.keys()    只拿名字
# 2. for v in score.values()  只拿成绩
# 3. for k, v in score.items()  名字和成绩一起,输出 "姓名: 成绩"
# ------------------------------------------------------------
# 【小提示】
# items() 返回的是 (key, value) 对,可以直接 for k, v 解包

# 您的代码写在这里 ↓↓↓
# 1. for k in score.keys()    只拿名字
for k in score.keys():
    print(k)

# 2. for v in score.values()  只拿成绩
for v in score.values():
    print(v)

# 3. for k, v in score.items()  名字和成绩一起,输出 "姓名: 成绩"
for k, v in score.items():
    print(k,v)
# ------------------------------------------------------------
# 题目 4:单词计数器(经典题!)
# 给一句话 text = "hello python hello world python"
# 用字典统计每个单词各出现几次,输出:
#   {'hello': 2, 'python': 2, 'world': 1}
# ------------------------------------------------------------
# 【小提示】
# 第一步:text.split() 把句子按空格切成单词列表
# 第二步:for w in words: 统计
# 优雅写法(一行搞定):
#   word_count[w] = word_count.get(w, 0) + 1
# 想一想这个 get 默认值 0 起什么作用?

# 您的代码写在这里 ↓↓↓
text = "hello python hello world python"

# 第一步:text.split() 把句子按空格切成单词列表
words = text.split( )

# 第二步:for w in words: 统计
words_count = {}
for w in words:
    words_count[w] = words_count.get(w,0) + 1
print(words_count)

# ------------------------------------------------------------
# 题目 5:综合挑战:通讯录系统(菜单版)📱
# 初始字典:contacts = {"小明": "13800000001", "小红": "13900000002"}
# 菜单循环:
#   1.查看全部  2.添加  3.查找(输入名字查号码)  4.删除  0.退出
# 提示:
#   - while True + if/elif(或 match)
#   - 查看:for name, phone in contacts.items()
#   - 添加:contacts[名字] = 号码
#   - 查找:先判断 名字 in contacts,再输出号码
#   - 删除:del contacts[名字](先判断存在)
# ------------------------------------------------------------
# 【小提示】
# 参考您写的"购物车管理系统"结构,只是换成通讯录
# 空通讯录时查看,提示"通讯录是空的"更友好

# 您的代码写在这里 ↓↓↓
contacts = {"小明": "13800000001", "小红": "13900000002"}
while True:
    print("\n===== 通讯录 =====")
    print("1.查看全部  2.添加  3.查找  4.删除  0.退出")
    choice = int(input("请选择:"))
    match choice:
        case 1:
            # 1.查看全部
            if contacts == {}:
                print("通讯录为空")
            else:
                for k, v in contacts.items():
                    print(k, v)
        case 2:
            # 2.添加
            k = input("请输入要添加的新朋友的名字：")
            if k in contacts.keys():
                print(f"{k}已经在通讯录内")
            else:
                v = input("请输入要添加的新朋友的号码：")
                choice[k] = v
                print("添加成功")
        case 3:
            # 3.查找
            k = input("请输入要查询的姓名：")
            if k in contacts:
                print(f"{k} \t {contacts[k]}")
            else:
                print(f"通讯录里没有 '{k} 这个人'")
        case 4:
            # 4.删除
            k = input("请输入要删除人的姓名：")
            if k in contacts:
                del contacts[k]
                print(f"已经删除{k}")
            else:
                print(f"通讯录里没有 '{k} 这个人'")
        case 0:
            # 0.退出
            break
        case _:
            print("输入错误，请重新输入！！！")
            continue