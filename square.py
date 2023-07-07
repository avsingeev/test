def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    return s


a, b, c = int(input()), int(input()), int(input())
print(area(a, b, c))
