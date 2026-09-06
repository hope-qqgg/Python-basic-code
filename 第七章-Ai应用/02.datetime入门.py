from datetime import datetime

print(datetime.now())

# %Y年 %m月 %d日 %H时 %M分 %S秒
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
