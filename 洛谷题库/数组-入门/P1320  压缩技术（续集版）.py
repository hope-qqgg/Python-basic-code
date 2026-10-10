s = input()
n = len(s)
left = 0
right = 0
arr = [n]
string = ''
for i in s:
    string += i
for _ in range(n-1):
    string += input()
if string[left] == '0':
    while right < n * n:
        if string[left] == string[right]:
            right += 1
        else:
            arr.append(right-left)
            left = right
elif string[left] == '1':
    arr.append(0)
    while right < n * n:
        if string[left] == string[right]:
            right += 1
        else:
            arr.append(right-left)
            left = right
if sum(arr[1::]) != n * n:
    arr.append(n*n-sum(arr[1::]))
print(' '.join(map(str,arr)))

