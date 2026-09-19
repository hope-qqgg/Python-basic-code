n = int(input())
cont = 1
q = 3
k = 0
while cont <= n :
    cot = 0
    l = 1
    for m in range(l,q+1):
        if q % m == 0:
            cot +=1
            if cot == 2:
                cont +=1
                k = max(k,m)
                l = m
                
    q += 1
print(k)
    
