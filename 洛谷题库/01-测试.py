# ===== 断点练习 =====
def add(a, b):
    result = a + b
    return result

total = 0
for n in [1, 2, 3]:
    total = add(total, n)        # ← 断点设在这一行！
    print("累加到", n, "，总和 =", total)

print("结束，最终 =", total)
