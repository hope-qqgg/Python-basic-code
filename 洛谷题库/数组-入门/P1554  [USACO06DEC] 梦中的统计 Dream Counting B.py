m, n = map(int,input().split())
arr = [str(i) for i in range(m,n+1)]
counts = [0] * 10
for i in arr:
    for j in i:
        counts[int(j)] += 1
print(*counts)
print(' '.join(map(str,counts)))

# 用底层的c语言来完成
m, n = map(int, input().split())
s = ''.join(map(str, range(m, n + 1)))
print(' '.join(str(s.count(str(d))) for d in range(10)))