s1, s2, s3 = map(int,input().split())

max_sum = s1 + s2 + s3
count = [0] * (max_sum + 1)
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            count[i+j+k] += 1

# 求次数还可以用字典
max_count = -1
ans = 0
for i in range(3,max_sum + 1):
    if count[i] > max_count:
        max_count = count[i]
        ans = i
print(ans)