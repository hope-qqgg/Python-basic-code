s = input()
count = 0
# 遍历每个字符
for char in s:
    #.isdigit()是字符串内置的函数。
    #用来判断是不是数字，返回True是数字，False不是数字
    if char.isdigit():
        count += 1
print(count)
print('====================')

s = input()
print(sum(1 for char in s if char.isdigit()))
