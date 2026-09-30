def judge_ab(n):
    n = bin(n)
    if n.count('1') > n.count('0')-1:
        return True
    else:
        return False

count_a = 0
count_b = 0
n = int(input())
for i in range(1,n+1):
    if judge_ab(i):
        count_a += 1
    else:
        count_b += 1
print(count_a,count_b)