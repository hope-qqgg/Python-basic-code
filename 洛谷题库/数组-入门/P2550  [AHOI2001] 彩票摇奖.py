def zj(arr,ls):
    count = 0
    for i in ls:
        if i in arr:
            count += 1
    return count
specialPrize = 0
firstPrize = 0
secondPrize = 0
thirdPrize = 0
fourthPrize = 0
fifthPrize = 0
sixthPrize = 0
n = int(input())
arr = list(map(int,input().split()))
for i in range(n):
    ls = list(map(int,input().split()))
    if zj(arr,ls) == 1:
        sixthPrize += 1
    elif zj(arr,ls) == 2:
        fifthPrize += 1
    elif zj(arr,ls) == 3:
        fourthPrize += 1
    elif zj(arr,ls) == 4:
        thirdPrize += 1
    elif zj(arr,ls) == 5:
        secondPrize += 1
    elif zj(arr,ls) == 6:
        firstPrize += 1
    elif zj(arr,ls) == 7:
        specialPrize += 1
print(specialPrize,firstPrize,secondPrize,thirdPrize,fourthPrize,fifthPrize,sixthPrize)