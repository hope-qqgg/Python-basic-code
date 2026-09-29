def is_shuShu(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def is_huiWenShu(num):
    sn= str(num)
    return sn[::-1] == sn

n = int(input())
count = 0
for i in range(11,n+1):
    if is_shuShu(i) and is_huiWenShu(i):
        count += 1
print(count)
