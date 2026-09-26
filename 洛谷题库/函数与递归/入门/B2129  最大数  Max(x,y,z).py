def get_max(x,y,z):
    return max(x,y,z)

a, b, c = map(int,input().split())
m = get_max(a,b,c) / (get_max(a + b,b,c) * get_max(a,b,b+c))
print(f'{m:.3f}')