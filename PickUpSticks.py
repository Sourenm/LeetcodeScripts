def main(n, m, temp):
    d = {}
    for i in range(n):
        d[i] = []
    for i in range(m):
        d[temp[i][1] - 1].append(temp[i][0] - 1)
    while len(d) > 0:
        for i in d.keys():
            if len(d[i]) == 0:
                print(i + 1)
                d.pop(i)
                for j in d.keys():
                    if d[j].count(i) > 0:
                        d[j].pop(d[j].index(i))
                break

n = 5
m = 4
temp = [(1, 2), (2, 3), (3, 4), (4, 5)]
main(n, m, temp)
