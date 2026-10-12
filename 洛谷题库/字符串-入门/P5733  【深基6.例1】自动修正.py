# 通过ASCLL码
s = input()
s_new = ''
for i in s:
    if ord(i) in range(97,97 + 26 + 1):
        i = chr((ord(i) - 32))
        s_new += i
    else:
        s_new += i
print(s_new)

# upper() 转换成大写/lower() 转换成小写，python内置
s = input()
print(s.upper())
