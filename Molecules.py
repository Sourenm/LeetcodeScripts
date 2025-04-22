def main(n, m, x, y, a, b):
    coordinates = []
    d = {}
    for i in range(n):
        coordinates.append([x[i], y[i]])
    for i in range(m):
        a[i] -= 1
        b[i] -= 1
        if a[i] not in d:
            d[a[i]] = []
        d[a[i]].append(b)
        if b[i] not in d:
            d[b[i]] = []
        d[b[i]].append(a[i])
    while coordinates.count([-1, -1]) > 0:
        for i in range(n):
            x = 0
            y = 0
            flag = 0
            if coordinates[i][0] == -1 and coordinates[i][1] == -1:
                for j in range(len(d[i])):
                    if coordinates[d[i][j]][0] == -1 and coordinates[d[i][j]][1] == -1:
                        flag = 1
                        break
                    else:
                        x += coordinates[d[i][j]][0]
                        y += coordinates[d[i][j]][1]
                if flag == 0:
                    coordinates[i][0] = x / len(d[i])
                    coordinates[i][1] = y / len(d[i])
    for i in range(n):
        print(coordinates[i][0], ' ', coordinates[i][1])
    

n = 4
m = 3
x = [1.0, 2.0, 3.0, 4.0]
y = [5.0, 6.0, 7.0, 8.0]
a = [1, 2, 3]
b = [2, 3, 4]
main(n, m, x, y, a, b)