s = input().strip().replace(' ','')
# replace(' ','')   把空格替换成空，删除空格
op = ''
op_index = -1
for i in range(len(s)):
    if s[i] in '+-*/%':
        op = s[i]
        op_index = i
        break
num1 = int(s[:op_index])
num2 = int(s[op_index + 1:])
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 // num2)
elif op == '%':
    print(num1 % num2)