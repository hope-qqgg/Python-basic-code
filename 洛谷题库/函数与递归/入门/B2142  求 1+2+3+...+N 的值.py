# 题目要求用递归的方式
def cum_sum(n):
    if n == 0:
        return 0
    return cum_sum(n-1) + n

n = int(input())
print(cum_sum(n))