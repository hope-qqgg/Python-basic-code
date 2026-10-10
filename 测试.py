n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=False)
print(' '.join(map(str,arr)))