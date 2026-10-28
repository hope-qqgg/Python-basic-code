s = input().strip()
s_new = s.split(";")
vals = {'a':0,'b':0,'c':0}
for i in s_new:
    if not i:
        continue
    letter,num = i.split(":=")
    if num in vals:
        vals[letter] = vals[num]
    else:
        vals[letter] = num
print(f"{vals['a']} {vals['b']} {vals['c']}")