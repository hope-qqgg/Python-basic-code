import json

# # 写入json数据文件
# user = {
#     "name": "张三",
#     "age": 18,
#     "sex": "男",
#     "hobby": ["看电影", "玩游戏", "听音乐"]
# }
# with open("user.json", "w", encoding="utf-8") as f:
#     # ensure_ascii: 是否将非ascii字符转换为ascii字符
#     # indent: 缩进
#     json.dump(user, f, ensure_ascii=False, indent=4)

# 读取json数据文件
with open("user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))
