h = int(input())
cont = h
for c in range(1,10):
    h /= 2
    cont += (h*2)
h /= 2
print("%g" %cont)
print("%g" %h)
