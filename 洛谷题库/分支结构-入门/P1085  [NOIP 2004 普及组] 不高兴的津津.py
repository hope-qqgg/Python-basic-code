arr = []
ls = []
for i in range(7):
    a, b = map(int,input().split())
    arr.append(a + b - 8)
    if a + b <= 8:
        ls.append(False)
    else:
        ls.append(True)
print(arr)
print(ls)
if sum(ls) == 0:
    print(0)
else:
    max_index = arr.index(max(arr))
    print(max_index+1)