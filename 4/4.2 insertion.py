a = [1, 3, 2, 7, 4, 5, 9, 8, 6]


def sort_ins(a):
    N = len(a)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break
    return (a)


print(a)
print(sort_ins(a))
