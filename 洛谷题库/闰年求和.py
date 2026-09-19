n,m = map(int,input().split())
year_sum = 0
for  year in range(n + 1,m):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        year_sum += year
print(year_sum)
