h,m,s,w = input().split()
h,m,s = int(h),int(m),int(s)
if w == 'A':
    H = h * 3600
    M = m * 60
    cnt = H + M + s
elif w == 'P':
    H = (h + 12) * 3600
    M = m * 60
    cnt = H + M + s
print(cnt)
