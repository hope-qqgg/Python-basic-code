n = int(input())
cost = 0
if n <= 150:
    cost = n * 0.4463
elif 150 < n <= 400:
    cost = 150 * 0.4463 + (n - 150) * 0.4663
elif n > 400:
    cost = 150 * 0.4463 + 250 * 0.4663 + (n - 400) * 0.5663
print(f'{cost:.1f}')    
