def main(n, temp):
    vert = []
    for i in range(n):
        vert.append(temp[i])
    flag = []
    for i in range(n):
        flag.append(0)
    for i in range(n):
        for j in range(n):
            if vert[i][j] == 1:
                for k in range(j, n):
                    if vert[i][k] == 1 and vert[j][k] == 1:
                        flag[i] = 1
                        flag[j] = 1
                        flag[k] = 1
    for i in range(n):
        if flag[i] == 0:
            print(i)
n = 5
temp = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
]
main(n, temp)
