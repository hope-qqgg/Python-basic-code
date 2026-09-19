n = int(input())
cont = 0
j = 1
for m in range(1,n+1):
    j *= m
    cont += j
print(cont)
print('========================================================')
n = int(input())
cont = 0
for m in range(1,n+1):
    j = 1
    for i in range(1,m+1):
        j *= i
    cont += j
print(cont)
