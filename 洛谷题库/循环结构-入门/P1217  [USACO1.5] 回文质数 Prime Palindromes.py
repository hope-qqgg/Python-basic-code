def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

a, b = map(int, input().split())

hi = min(b, 10 ** 7)
ans = []
half = 1
while True:
    s = str(half)
    cand = int(s + s[-2::-1])
    if cand > hi:
        break
    if cand >= a and is_prime(cand):
        ans.append(cand)
    half += 1

if a <= 11 <= b:
    ans.append(11)

print('\n'.join(map(str, sorted(ans))))
