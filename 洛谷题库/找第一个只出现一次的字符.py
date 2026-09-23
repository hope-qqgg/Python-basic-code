s = input()
# 遍历每个字符
for char in s:
    # 如果字符只出现一次
    if s.count(char) == 1:
        print(char)
        break # 找到第一个跳出循环
else: # 与for对齐，表示循环正常结束时运行
    print('no')
