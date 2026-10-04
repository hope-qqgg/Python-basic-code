n = int(input())
# 本地
b_time = n * 5
# 上传
s_time = n * 3 + 11
if b_time < s_time:
    print('Local')
else:
    print('Luogu')