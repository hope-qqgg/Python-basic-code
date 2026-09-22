arr = [list(map(int,input().split())) for _ in range(5)]
found = False
for i in range(5):
    for j in range(5):
        val = arr[i][j]
        i_max = max(arr[i])
        j_min = min([arr[x][j] for x in range(5)])
        if val == i_max and val == j_min:
            ans = [i+1,j+1,val]
            found = True
            break
    if found:
        break
if not found:
    print('not found')
else:
    print(' '.join(map(str,ans)))
