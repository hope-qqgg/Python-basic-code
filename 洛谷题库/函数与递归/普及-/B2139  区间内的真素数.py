def build_sieve(num):
    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, num + 1, i):
                is_prime[j] = False
    return is_prime

m, n = map(int, input().split())
is_prime = build_sieve(100000)
arr = []
for x in range(m, n + 1):
    r = int(str(x)[::-1])
    if is_prime[x] and is_prime[r]:
        arr.append(str(x))
if arr:
    print(','.join(arr))
else:
    print('No')