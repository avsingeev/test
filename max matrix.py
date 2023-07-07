from random import randint

n = 5
max1 = 0
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
print(m)
for i in range(n):
    for j in range(n):
        if m[i][j] > max1:
            max1 = m[i][j]
print(max1)
