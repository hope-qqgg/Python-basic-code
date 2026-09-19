a,b,c,f = input().split()
a = int(a)
b = int(b)
f = int(f)
if f == 0:
    for g in range(a):
        if g == 0 or g == a - 1:
            print(c * b)
        else:
            print(c," " * (b - 2),c,sep = '')
else:
    for g in range(a):
        print(c * b)
        
    
