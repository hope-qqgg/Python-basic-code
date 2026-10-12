n = int(input())
s = input()
for i in s:
        print(chr(ord('a') + (ord(i) - ord('a') + n) % 26),end='')