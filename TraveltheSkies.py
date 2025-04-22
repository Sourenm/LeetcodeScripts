def main(k, n, m, temp, temp2):
    source = [[0 for x in range(k)] for y in range(n)]
    destination = [[0 for w in range(k)] for z in range(n)]
    for i in range(m):
        source[(temp[i][2] - 1)][(temp[i][0] - 1)] += temp[i][3]
        if temp[i][2] < n:
            destination[temp[i][2]][(temp[i][1] - 1)] += temp[i][3]
    flag = 0
    for i in range(k * n):
        destination[temp2[i][1] - 1][temp2[i][0] - 1] += temp2[i][2]
    for i in range(n):
        for j in range(k):
            if source[i][j] <= destination[i][j]:
                destination[i][j] -= source[i][j]
            else:
                if i > 0:
                    sum = 0
                    for h in range(i + 1):
                        sum += destination[h][j]
                    if source[i][j] > sum:
                        flag = 1
                        print('Suboptimal')
                        break
                    else:
                        temp = source[i][j]
                        h = 0
                        while temp > 0 and h <= i:
                            if destination[h][j] < temp:
                                temp -= destination[h][j]
                                destination[h][j] = 0
                            else:
                                destination[h][j] -= temp
                                temp = 0
                            h += 1
                else:
                    flag = 1
                    print('Suboptimal')
                    break
        if flag == 1:
            break
    if flag == 0:
        print('Optimal')
k = 3
n = 2
m = 3
temp = [
    (1, 2, 1, 5),
    (2, 1, 2, 8),
    (2, 2, 2, 3)
]
temp2 = [
    (1, 1, 2),
    (1, 2, 1),
    (2, 2, 5),
    (2, 1, 3),
    (1, 1, 1),
    (2, 2, 2)
]
main(k, n, m, temp, temp2)
