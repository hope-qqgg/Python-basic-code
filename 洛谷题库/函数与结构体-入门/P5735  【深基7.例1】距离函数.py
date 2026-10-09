def dis(arr1,arr2):
    x1, y1 = arr1
    x2, y2 = arr2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
arr = [list(map(float,input().split())) for _ in  range(3)]
print(f'{dis(arr[0],arr[1]) + dis(arr[0],arr[2]) + dis(arr[1],arr[2]):.2f}')
