import random
num = random.randint(1,100)
# 给定一个100以内的数，如何在最少的次数内猜到这个数？(每次会告诉你大了还是小了)
def binary_search(item):
    mylist = range(1,101)
    low = 0
    high = len(mylist) - 1
    count = 0

    while low <= high:
        mid =(low + high) // 2
        guess = mylist[mid]
        if guess == item:
            count += 1
            return print(f"猜了{count}次，答案是{guess}")
        if guess < item:
            count += 1
            low = mid + 1
        else:
            count += 1
            high = mid - 1

binary_search(num)
