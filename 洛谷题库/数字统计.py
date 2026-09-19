l,r = map(int,input().split())
s = ''
for m in range(l,r+1):
    m = str(m)
    s += m
cont = s.count('2')
print(cont)
