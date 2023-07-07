x, y, p = int(input()), int(input()), int(input())
while x < y:
    x = x + int(x * p / 100)
    print(x)
print(x)
