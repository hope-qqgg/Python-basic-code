n = int(input())
n_list = []
for i in range(n):
    j = float(input())
    n_list.append(j)
n_list.sort()
n_list.pop(0)
n_list.pop(-1)
avg = sum(n_list) / len(n_list)
n_max = 0
for c in n_list:
    n_max = max(n_max,abs(avg - c))
print(f'{avg:.2f} {n_max:.2f}')
