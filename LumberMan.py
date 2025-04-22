def main(n, temp):
    y = []
    r = []
    s = []
    b = []
    for i in range(n):
        y.append(temp[i][0])
        r.append(temp[i][1])
        s.append(temp[i][2])
        b.append(temp[i][3])
    year = 0
    counter = 0
    final = 0
    ready = [0 for x in range(n)]
    while counter == 0:
        for i in range(len(s)):
            if year >= b[i]:
                if b[i] + y[i] > year:
                    s[i] += r[i]
                elif b[i] + y[i] <= year:
                    if s[i] != 0:
                        s[i] -= r[i]
                        if s[i] < 0:
                            s[i] = 0
                    else:
                        ready[i] = 1
        year += 1
        if sum(s) > final:
            final = sum(s)
        if sum(ready) == n:
            counter = 1
    print(final)
    

n = 3
temp = [(2, 5, 1, 8), (3, 2, 2, 6), (1, 8, 3, 7)]
main(n, temp)
