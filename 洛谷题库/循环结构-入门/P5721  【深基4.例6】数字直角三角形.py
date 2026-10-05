n = int(input())
count = 1
for i in range(n):
    for j in range(n-i):
        print(f'{count:02d}',end='')
        count += 1
    print()