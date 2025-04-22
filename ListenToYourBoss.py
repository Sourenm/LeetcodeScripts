def main(n, m, mans, temp):
    d = {}
    for i in range(n - 1):
        if mans[i] not in d:
            d[mans[i]] = []
        d[mans[i]].append(i + 2)
    
    while True:
        flag = 0
        for i in d.keys():
            for j in range(len(d[i])):
                if d[i][j] in d.keys() and d[i][j] != i:
                    for k in range(len(d[d[i][j]])):
                        if d[d[i][j]][k] not in d[i]:
                            flag = 1
                            d[i].append(d[d[i][j]][k])
        if flag == 0:
            break
    for i in range(m):
        if temp[i][1] not in d:
            print('Yes')
        else:
            if temp[i][0] in d[temp[i][1]]:
                print('No')
            else:
                print('Yes')

n = 6
m = 3
mans = [1, 1, 2, 3, 3]
temp = [(1, 4), (3, 2), (2, 5)]
main(n, m, mans, temp)