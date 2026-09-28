def is_jialiu(bt,ks):
    return bt >= 37.5 and ks == 1
n = int(input())
count = 0
for _ in range(n):
    info = input().split()
    name = info[0]
    bt = float(info[1])
    ks = int(info[2])
    if is_jialiu(bt,ks):
        print(name)
        count += 1
print(count)

