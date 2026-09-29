words = input().split()
a = input().strip()
b = input().strip()
print(' '.join(b if w == a else w for w in words))
# 一句话："整行当值"就 .strip()，"数字"和"切词"不用管。
# 你前面 B2131~B2134 全是数字/切词，所以都没踩到这个坑 —— 这题是你第一次遇到"拿整行去比较"。