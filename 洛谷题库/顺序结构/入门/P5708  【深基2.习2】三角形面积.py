def triangle_area(a,b,c):
    p = 0.5 * (a + b + c)
    return round((p * (p - a) * (p - b) * (p - c))**0.5,1)
a, b, c = map(float,input().split())
print(triangle_area(a,b,c))