import math
# 填上你觉得需要的其他模块
def main():
    T = int(input())
    if T == 1:
        print("I love Luogu!")

    elif T == 2:
        print(2 + 4, 10 - 2 - 4)

    elif T == 3:
        print(14 // 4)
        print(14 - 14 % 4)
        print(14 % 4)

    elif T == 4:
        print(f'{500 / 3:.6g}')

    elif T == 5:
        l = 260 +220
        v = 12 + 20
        print(int(l/v))

    elif T == 6:
        print(f'{math.sqrt(9**2 + 6**2):.6g}')

    elif T == 7:
        uim = 100
        uim += 10
        print(uim)
        uim -= 20
        print(uim)
        print(0)

    elif T == 8:
        pi = 3.141593
        r = 5
        c = 2 * pi * r
        s = pi * r**2
        v = 4/3 * pi * r**3
        print(f'{c:.6g}')
        print(f'{s:.6g}')
        print(f'{v:.6g}')

    elif T == 9:
        n = 1
        for i in range(3):
            n = (n + 1) * 2
        print(n)

    elif T == 10:
        n = 15
        x = 7.5
        print(math.ceil((n + 10 * x) / 10))

    elif T == 11:
        va = 5
        vb = 8
        x = 100
        t = x / (vb - va)
        print(f'{t:.6g}')

    elif T == 12:
        m_index = ord('M') - ord('A') + 1
        print(m_index)
        n18 = chr(ord('A') + 18 - 1)
        print(n18)

    elif T == 13:
        pi = 3.141593
        r1 = 4
        r2 = 10
        v1 = 4/3 * pi * r1**3
        v2 = 4/3 * pi * r2**3
        v3 = v1 + v2
        l = v3**(1/3)
        print(int(l))

    elif T == 14:
        a, b, c = 1, -100, 2400
        delta = b ** 2 - 4 * a * c
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        price1 = 110 - x1
        price2 = 110 - x2
        ans = round(min(price1, price2))
        print(ans)

if __name__ == "__main__":
    main()
