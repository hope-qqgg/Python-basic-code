cont = 0
n = int(input())
for m in range(n):
    k = int(input())
    cont += ((k + 69) // 70)
print(f'{cont*0.1:.1f}')
