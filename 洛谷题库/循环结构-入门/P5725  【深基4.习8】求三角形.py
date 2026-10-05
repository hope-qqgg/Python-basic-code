n = int(input())
count = 1
for i in range(n):
    for j in range(n):
        print(f'{count:02d}',end='')
        count += 1
    print()
print()

count = 1
for i in range(n):
    print(' ' * 2 * (n - i - 1), end='')
    for j in range(i+1):
        print(f'{count:02d}',end='')
        count += 1
    print()