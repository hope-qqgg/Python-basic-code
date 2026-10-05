n, x = map(int,input().split())
x = str(x)
index = 0
for i in range(1,n+1):
    i = str(i)
    index += i.count(x)
print(index)