def score(ls,m):
    ls.sort()
    ls = ls[1:-1]
    return sum(ls) / (m - 2)

n,m = map(int,input().split())
max_score = 0
for _ in range(n):
    arr = list(map(int,input().split()))
    sc = score(arr,m)
    max_score = max(max_score,sc)
print(f"{max_score:.2f}")