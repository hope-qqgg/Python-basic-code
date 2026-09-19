arr = list(map(int,input().split()))
cont = 0
for i in arr:
    if i < 60:
        cont += 1
if cont == 1:
    print(1)
else:
    print(0)
    
