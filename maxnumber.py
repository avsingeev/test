def maxnumber():
    s = [3, 81, 5]
    m = 0
    k = ''
    p = []
    for i in s:
        p.append(str(i))
    while p != []:
        for i in range(len(p)):
            if int(p[i][0]) > m:
                m = int(p[i][0])
                n = p[i]
        k += n
        p.remove(n)
        m = 0
    return k


print(maxnumber())
