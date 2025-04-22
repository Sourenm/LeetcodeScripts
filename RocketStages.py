def main(n, temp):
    s = []
    l = []
    t = []
    c = []
    for i in range(n):    
        s.append(temp[i][0])
        l.append(temp[i][1])
        t.append(temp[i][2])
        c.append(temp[i][3])
    reversed(s)
    reversed(l)
    reversed(t)
    reversed(c)
    a = 0
    for i in range(n):
        while l[i] > 0:
            a += (t[i] - (sum(s) + sum(l)) * 9.8) / (sum(s) + sum(l))
            l[i] -= c[i]
        s[i] = 0
    v = a / sum(c)
    print(round(v))
n = 3
temp = [
    (10, 5, 2, 1),
    (8, 4, 3, 2),
    (12, 6, 1, 1),
]
main(n, temp)
