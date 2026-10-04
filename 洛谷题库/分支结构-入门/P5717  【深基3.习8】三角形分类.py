arr = list(map(int,input().split()))
arr.sort()
a = arr[0]
b = arr[1]
c = arr[2]
if a + b <= c:
    print('Not triangle')
elif a**2 + b**2 > c**2:
    print('Acute triangle')
elif a**2 + b**2 == c**2:
    print('Right triangle')
elif a**2 + b**2 < c**2:
    print('Obtuse triangle')

if (a == b or b == c) and a + b > c:
    print('Isosceles triangle')
    if a == b == c:
        print('Equilateral triangle')
