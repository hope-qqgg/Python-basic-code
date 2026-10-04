import math
def y(n,arr):
    m = math.ceil(n/arr[0])
    return arr[1] * m
# n = int(input())
# arr_min = 0
# arr_1 = list(map(int,input().split()))
# arr_2 = list(map(int,input().split()))
# arr_3 = list(map(int,input().split()))
# print(min(y(n,arr_1),y(n,arr_2),y(n,arr_3)))

# 方法二
n = int(input())
zd = {}
m = float('inf')
for i in range(1,4):
    arr = list(map(int,input().split()))
    zd[i] = arr
    m = min(m,y(n,arr))
print(m)
