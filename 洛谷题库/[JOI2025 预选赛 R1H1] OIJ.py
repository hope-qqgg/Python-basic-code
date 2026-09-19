n = int(input())
s = input()
s_new = ''
for c in s:
    if c == 'J':
        s_new += 'O'
    elif c == 'O':
        s_new += 'I'
    elif c == 'I':
        s_new += 'J'
print(s_new)
