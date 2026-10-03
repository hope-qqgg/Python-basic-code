arr = list(map(int,input().split()))
s = input()
arr.sort()
dict_1 = {}
dict_1['A'] = arr[0]
dict_1['B'] = arr[1]
dict_1['C'] = arr[2]
for i in s:
    print(dict_1[i],end=' ')

