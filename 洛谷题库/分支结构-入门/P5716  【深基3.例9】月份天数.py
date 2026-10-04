# 判断是否是闰年（闰年）。闰年2月29天，平年2月28天。
def estimate_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 29
    return 28

year, month = map(int,input().split())
if month == 2:
    print(estimate_year(year))
elif month in [1,3,5,7,8,10,12]:
    print(31)
elif month in [4,6,9,11]:
    print(30)