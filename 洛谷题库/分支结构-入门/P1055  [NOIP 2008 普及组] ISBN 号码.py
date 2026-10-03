s = input().strip()
s1 = s.replace('-','')
count = 0
j = 1
for i in s1[:-1]:
    i = int(i) * j
    count += i
    j += 1
m = count % 11
check = 'X' if m == 10 else str(m)

if s[-1] == check:
    print('Right')
else:
    print(s[:-1] + check)