n = int(input())
m = 1
count = 0
for i in range(1,n+1):
    m *= i
    count += m
print(count)

# 递推
def factorial(i):
    if i == 1:
        return 1
    return factorial(i-1) * i

count = 0
for i in range(1,n+1):
    count += factorial(i)
print(count)