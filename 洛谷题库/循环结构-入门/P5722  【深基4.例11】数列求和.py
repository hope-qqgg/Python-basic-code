# 递推
n = int(input())
count = 0
for i in range(1,n+1):
    count += i
print(count)

# 递归
def recursion(m):
    if m == 1:
        return 1
    return recursion(m - 1) + m
print(recursion(n))