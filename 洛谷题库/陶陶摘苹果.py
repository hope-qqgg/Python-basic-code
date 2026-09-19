arr = map(int,input().split())
h = int(input())
cont = 0
for n in arr:
    if n <= (h + 30):
        cont += 1
print(cont)
