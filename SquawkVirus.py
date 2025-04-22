def main(n, m, s, t, temp):
    d = {}
    for i in range(m):
        if temp[i][0] not in d:
            d[temp[i][0]] = []
        d[temp[i][0]].append(temp[i][1])
        if temp[i][1] not in d:
            d[temp[i][1]] = []
        d[temp[i][1]].append(temp[i][0])
    virus = [0 for x in range(n)]
    virus[s] = 1
    while t > 0:
        next = [0 for x in range(n)]
        for i in range(n):
            if virus[i] > 0:
                if i in d.keys():
                    for v in d[i]:
                        next[v] += virus[i]
        virus = next.copy()
        t -= 1
    print(sum(virus))
n = 6
m = 5
s = 0
t = 2
temp = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4),
    (3, 5),
]
main(n, m, s, t, temp)
