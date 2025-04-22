def main(m, temp):
    d = {}
    for i in range(m):
        if temp[i][0] not in d:
            d[temp[i][0]] = []
        if temp[i][1] not in d:
            d[temp[i][1]] = []
        for k in d.keys():
            for j in range(len(d[k])):
                if d[k][j][0] == temp[i][0]:
                    d[k].append([temp[i][1], d[k][j][1] + 1])
                elif d[k][j][0] == temp[i][1]:
                    d[k].append([temp[i][0], d[k][j][1] + 1])
        d[temp[i][0]].append([temp[i][1], 0])
        d[temp[i][1]].append([temp[i][0], 0])
    

main(4, [(1, 2), (2, 3), (3, 4), (4, 1)])
