def judge_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

n = int(input())
for i in range(4,n+1,2):
    for j in range(1,i):
        if judge_prime(j) and judge_prime(i - j):
            print(f"{i}={j}+{i - j}")
            break
