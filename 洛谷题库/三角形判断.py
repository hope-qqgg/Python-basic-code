a,b,c = map(int,input().split())
if a + b > c and b + c > a and c + a >b:
    print(1)
else:
    print(0)
