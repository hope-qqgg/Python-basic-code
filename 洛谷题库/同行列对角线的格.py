n,i,j = map(int,input().split())
print(' '.join(f'({i},{m})' for m in range(1,n+1)))
print(' '.join(f'({m},{j})' for m in range(1,n+1)))
arr = []
for x in range(1,n+1):
    y = (j - i) + x
    if 0 < y <=n:
        arr.append(f'({x},{y})')
print(' '.join(m for m in arr))
arr = []
for x in range(n,0,-1):
    y = (j + i) - x
    if 0 < y <=n:
        arr.append(f'({x},{y})')
print(' '.join(m for m in arr))
