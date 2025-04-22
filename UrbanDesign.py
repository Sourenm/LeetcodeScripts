from math import inf
def main(t, temp, lots, temp2):
    lines = [[0.0, 0.0] for x in range(t)]
    for i in range(t):
        if temp[i][2] - temp[i][0] != 0:
            m = (temp[i][3] - temp[i][1]) / (temp[i][2] - temp[i][0])
            lines[i][1] = temp[i][1] - m * temp[i][0]
        else:
            m = inf
            lines[i][1] = temp[0]
        lines[i][0] = m
    for i in range(lots):
        flag = 0
        for j in range(len(lines)):
            if lines[j][0] == inf:
                if temp2[i][2] - temp2[i][0] != 0:
                    m = (temp2[i][3] - temp2[i][1]) / (temp2[i][2] - temp2[i][0])
                    if m != 0:
                        flag = 1
                    else:
                        d1 = abs(temp2[i][1] - lines[j][0] * temp2[i][0] - lines[j][1])
                        d2 = abs(temp2[i][3] - lines[j][0] * temp2[i][2] - lines[j][1])
                        if d1 == d2:
                            print('different')
                            break
                else:
                    flag = 1
            elif lines[j][0] == 0:
                if temp2[i][2] - temp2[i][0] != 0:
                    flag = 1
                else:
                    if abs(temp2[i][1] - lines[j][1]) == abs(temp2[i][3] - lines[j][1]):
                        print('different')
                        break
                    else:
                        flag = 1
            else:
                if temp2[i][2] - temp2[i][0] != 0:
                    m = (temp2[i][3] - temp2[i][1]) / (temp2[i][2] - temp2[i][0])
                    if m * lines[j][0] != -1:
                        flag = 1
                    else:
                        d1 = abs(temp2[i][1] - lines[j][0] * temp2[i][0] - lines[j][1])
                        d2 = abs(temp2[i][3] - lines[j][0] * temp2[i][2] - lines[j][1])
                        if d1 == d2:
                            print('different')
                            break
                        else:
                            flag = 1
                else:
                    flag = 1
        if flag == 1:
            print('same')
t = 3
temp = [[1.0, 1.0, 3.0, 3.0], [0.0, 0.0, 1.0, 1.0], [2.0, 2.0, 4.0, 4.0]]
lots = 2
temp2 = [[1.0, 0.0, 3.0, 2.0], [0.0, 0.0, 1.0, 1.0]]
main(t, temp, lots, temp2)
