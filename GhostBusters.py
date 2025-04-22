def main(n, temp):
    x = []
    y = []
    flag_x = 0
    flag_y = 0
    for i in range(n):
        x.append(temp[i][0])
        if x.count(x[-1]) > 1:
            flag_x = 1
        y.append(temp[i][1])
        if y.count(y[-1]) > 1:
            flag_y = 1
    if flag_y == 0 or flag_x == 0:
        print('UNLIMITED')
    else:
        max_dif = 0
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                if x[i] == x[j]:
                    if abs(y[i] - y[j]) - 1 > max_dif:
                        flag = 0
                        for k in range(i + 1, j):
                            if (y[k] < y[i] and y[k] > y[j]) or (y[k] > y[i] and y[k] < y[j]):
                                flag = 1
                        if flag == 0:
                            max_dif = abs(y[i] - y[j]) - 1
                if y[i] == y[j]:
                    if abs(x[i] - x[j]) - 1 > max_dif:
                        flag = 0
                        for k in range(i + 1, j):
                            if (x[k] < x[i] and x[k] > x[j]) or (x[k] > x[i] and x[k] < x[j]):
                                flag = 1
                        if flag == 0:
                            max_dif = abs(x[i] - x[j]) - 1
        print(max_dif)
    
    
    

n = 5
temp = [(1, 2), (3, 4), (1, 5), (6, 4), (3, 2)]
main(n, temp)