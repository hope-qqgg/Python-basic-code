n = float(input())
s1 = input()
s2 = input()
m = len(s1)
count = 0
for k in range(m):
    if s1[k] == s2[k]:
        count += 1
if count/m >= n:
    print('yes')
else:
    print('no')