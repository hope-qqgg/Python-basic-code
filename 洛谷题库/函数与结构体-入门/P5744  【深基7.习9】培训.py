n = int(input())
for _ in range(n):
    arr = list(input().split())
    two = int(arr[1]) + 1
    three = int(arr[2])
    three = int(three + three // 5)
    if three > 600:
        three = 600
    print(arr[0],two,three)