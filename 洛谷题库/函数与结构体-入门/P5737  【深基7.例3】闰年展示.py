def estimate_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

x, y = map(int,input().split())
count = 0
arr = []

for year in range(x,y+1):
    if estimate_year(year):
        arr.append(year)
        count += 1

print(count)
print(' '.join(map(str,arr)))