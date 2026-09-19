m,n = map(int,input().split())
if m % 2 == 0:
    m += 1
num = 0
for i in range(m,n+1,2):
    num += i
print(num)
    
    
