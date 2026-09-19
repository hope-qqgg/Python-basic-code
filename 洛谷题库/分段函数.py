x = float(input())
if 0 <= x < 5:
    y = - x + 2.5
    print(f'{y:.3f}')
elif 5 <= x < 10:
    y = 2 - 1.5 * (x - 3)**2
    print(f'{y:.3f}')
elif 10 <= x < 20:
    y = x / 2 - 1.5
    print(f'{y:.3f}')
