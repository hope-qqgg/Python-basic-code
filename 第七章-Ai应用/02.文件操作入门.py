# # 读文件
# # 1.打开文件
# file = open("resources/横渠四句.txt", "r", encoding="utf-8")
#
# # 2.读取文件内容
# # content = file.read() # 读取文件全部内容
# # print(content)
# content_list = file.readlines() # 读取文件全部内容，返回一个列表，每个元素是一行
# for line in content_list:
#     print(line, end="")
#
# # 3.关闭文件
# file.close()

# # 写文件
# # 1.打开文件
# file = open("resources/静夜思.txt", "w", encoding="utf-8") # 没有文件则创建文件
#
# # 2.写入文件内容
# file.write("  静夜思\n")
# file.write("   李白\n")
# file.write("床前明月光，\n")
# file.write("疑是地上霜。\n")
# file.write("举头望明月，\n")
# file.write("低头思故乡。\n")
#
# # 3.关闭文件
# file.close()

# #------------------------------ 异常处理方法一 ------------------------------
# # 写文件
# # 1.打开文件
# file = open("resources/静夜思.txt", "w", encoding="utf-8") # 没有文件则创建文件
#
# try: # 异常处理（try内的代码错误也不影响finally内的代码 ---> 繁琐）
#     # 2.写入文件内容
#     file.write("  静夜思\n")
#     file.write("   李白\n")
#     file.write("床前明月光，\n")
#     i = 1 / 0
#     file.write("疑是地上霜。\n")
#     file.write("举头望明月，\n")
#     file.write("低头思故乡。\n")
# finally:
#     # 3.关闭文件
#     file.close()
#     print("文件关闭")

#------------------------------ 异常处理方法二（推荐） ------------------------------
# 写文件
# 1.打开文件
with open("resources/静夜思.txt", "w", encoding="utf-8") as file:
    # 2.写入文件内容
    file.write("  静夜思\n")
    file.write("   李白\n")
    file.write("床前明月光，\n")
    file.write("疑是地上霜。\n")
    file.write("举头望明月，\n")
    file.write("低头思故乡。\n")

