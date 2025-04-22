def main(n, p, m, temp):
    d = {}
    for i in range(n):
        d[i] = []
        d[i].append(i)
    for i in range(len(p)):
        if p[i] != 0:
            d[p[i] - 1].append(i)
    changes = 0
    while changes == 0:
        changes = 1
        for i in range(len(d)):
            for j in d[i]:
                for k in d[j]:
                    if k not in d[i]:
                        changes = 0
                        d[i].append(k)
    for i in range(m):
        s = 0
        for j in range(1, len(temp[i])):
            s += len(d[temp[i][j] - 1])
        print(s)
n = 5
p = [0, 1, 2, 0, 4]
m = 3
temp = [
    [3, 2, 5],
    [1, 4, 3],
    [2, 1, 4],
]
main(n, p, m, temp)