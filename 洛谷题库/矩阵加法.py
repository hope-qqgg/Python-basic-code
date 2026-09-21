# 方法一
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
b = []
for _ in range(n):
    b.append(list(map(int,input().split())))
for i in range(n):
    arr = []
    for j in range(m):
        arr.append(a[i][j] + b[i][j])
    print(*arr)
# 方法二
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    b = list(map(int,input().split()))
    print(' '.join(str(a[i][j] + b[j]) for j in range(m)))
# x = print(*arr)               屏幕上打出 2 4 6 ... 但 x 是 None！
# s = " ".join(map(str, arr))   s 就是字符串 "2 4 6"，能接着做别的
# 方法三
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    print(*[a[i][j] + b[i][j] for j in range(m)])
