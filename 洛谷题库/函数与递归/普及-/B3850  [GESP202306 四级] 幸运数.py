def bh(n):
    n = int(n)
    if n * 7 <= 9:
        return n * 7
    else:
        return geweisum(n * 7)

def geweisum(n):
    if n // 10 + n % 10 <= 9:
        return n // 10 + n % 10
    else:
        return geweisum(n // 10 + n % 10)

n = int(input())
for i in range(n):
    count = 0
    s = list(''.join(input().split()))
    s_len = len(s)
    for j in range(s_len - 1,-1,-2):
        s[j] = bh(s[j])
        count += s[j]
    for k in range(s_len-2,-1,-2):
        s[k] = int(s[k])
        count += s[k]
    if count % 8 == 0:
        print('T')
    else:
        print('F')
