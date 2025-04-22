import math
def main(v, e, temp, s, t):
    d = {}
    sp = [math.inf for x in range(v)]
    flag = 0
    visited = [-1 for x in range(v)]
    for i in range(e):
        if temp[i][0] not in d:
            d[temp[i][0]] = []
        d[temp[i][0]].append([temp[i][1], temp[i][2]])
    sp[s] = 0
    current = s
    visited[s] = 0
    while True:
        if current in d:
            for i in range(len(d[current])):
                if current == s:
                    sp[d[current][i][0]] = d[current][i][1]
                else:
                    if sp[d[current][i][0]] > (d[current][i][1] + sp[current]):
                        sp[d[current][i][0]] = (d[current][i][1] + sp[current])
            for i in range(len(d[current])):
                if visited[d[current][i][0]] == -1:
                    current = d[current][i][0]
                    visited[current] = 0
                    break
        else:
            for i in range(v):
                if visited[i] == -1:
                    current = i
                    visited[current] = 0
                    break
        if flag == 1:
            break
        if sum(visited) == 0:
            flag = 1
    print(sp[t])
v = 6
e = 8
temp = [(0, 1, 2), (0, 2, 5), (1, 2, 1), (1, 3, 3), (2, 3, 1), (2, 4, 7), (3, 5, 2), (4, 5, 1)]
s = 0
t = 5
main(v, e, temp, s, t)
