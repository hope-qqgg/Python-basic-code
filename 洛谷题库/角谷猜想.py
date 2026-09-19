n = int(input())
while n != 1:
    if n % 2 == 0:
        print(f'{int(n)}/2={int(n/2)}')
        n /= 2
    else:
        print(f'{int(n)}*3+1={int(n * 3 + 1)}')
        n = n * 3 + 1
print('End')
