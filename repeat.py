l=[1, 4, 1, 6, "hello", "a", 5, "hello"]
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(l)
print(s)