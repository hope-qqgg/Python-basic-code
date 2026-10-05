def zhao_yishu(num):
    max_shushu = 0
    for i in range(3,num + 2,2):
        if num % i == 0 and is_shushu(i):
            max_shushu = max(max_shushu,i)
    return max_shushu

def is_shushu(n):
    arr = [True] * (n + 1)
    arr [0] = arr[1] = False
    for i in range(2,int(n**0.5)+1):
        if arr[i]:
            for j in range(i * i,n + 1,i):
                arr[j] = False
    return arr[n]

m, n = map(int,input().split())
arr = []
for i in range(m,n+1):
    arr.append(zhao_yishu(i))
print(','.join(map(str,arr)))