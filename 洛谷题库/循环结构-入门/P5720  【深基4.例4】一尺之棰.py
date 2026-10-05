n = int(input())
count = 1
while n != 1:
    n /= 2
    n = int(n)
    count += 1
print(count)