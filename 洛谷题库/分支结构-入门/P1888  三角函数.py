import math
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
arr = list(map(int,input().split()))
arr.sort()
g = math.gcd(arr[0],arr[-1] )
print(f'{arr[0] // g}/{arr[-1] // g}')