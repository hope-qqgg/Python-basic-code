s = float(input())
count = 1
x = 2
m = 2
while m < s:
    x = x * 0.98
    m += x
    count += 1
print(count)