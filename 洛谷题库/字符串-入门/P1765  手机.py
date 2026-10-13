# 方法一
s = input()
count = 0
arr =[' ',"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
for i in s:
    for j in arr:
        if i in j:
            count += j.index(i) + 1
            break
print(count)

# 方法二（字典）
s = input()
hxb = {
    'a':1, 'b':2, 'c':3,
    'd':1, 'e':2, 'f':3,
    'g':1, 'h':2, 'i':3,
    'j':1, 'k':2, 'l':3,
    'm':1, 'n':2, 'o':3,
    'p':1, 'q':2, 'r':3, 's':4,
    't':1, 'u':2, 'v':3,
    'w':1, 'x':2, 'y':3, 'z':4,
    ' ':1
}
count = 0
for i in s:
    count += hxb[i]
print(count)