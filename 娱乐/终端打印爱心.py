import sys
RED = '\033[91m'
RESET = '\033[0m'
y = 1.5
while y > -1.5:
    x = -1.5
    while x <= 1.5:
        a = x**2 + y**2 - 1
        if a**3 - x**2 * y**3 <= 0.0:
            sys.stdout.write(f'{RED}*{RESET}')
        else:
            sys.stdout.write(' ')
        x += 0.05
    print()
    y -= 0.1