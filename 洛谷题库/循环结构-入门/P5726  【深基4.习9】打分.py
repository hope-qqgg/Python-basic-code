n = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(f'{(sum(arr)-arr[-1]-arr[0])/(n-2):.2f}')