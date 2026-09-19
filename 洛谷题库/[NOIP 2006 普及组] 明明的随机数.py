n = int(input())
arr = list(map(int,input().split()))
arr.sort()
se = set()
for m in arr:
    se.add(m)
print(len(se))
print(*sorted(se))
   
