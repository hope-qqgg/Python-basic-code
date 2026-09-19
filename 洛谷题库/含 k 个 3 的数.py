m,k = input().split()
if m.count(k) == 3:
    print('YES')
else:
    print('NO')
#===============================================    
m,k = input().split()
cont = 0
for n in m:
    if n == k:
        cont +=1
if cont == 3:
    print('YES')
else:
    print('NO')
        
