import math
def main(in_n, in_co, out_n, out_co):
    
    min = math.inf    
    for i in range(len(out_co)):
        flag = 0
        if i == len(out_co) - 1:
            if out_co[0][0] == out_co[i][0]:
                flag = -1
                m = 1
                b = out_co[0][0]
            else:
                m = (out_co[0][1] - out_co[i][1]) / (out_co[0][0] - out_co[i][0])
                b = out_co[0][1] - m * out_co[0][0]
            for j in range(len(in_co)):
                if flag != -1:
                    if m != 0:
                        c = in_co[j][1] + (1/ m) * in_co[j][0]
                        intersect_x = (c - b) / (m + (1 / m))
                        intersect_y = ((m ** 2) * c + b) / ((m ** 2) + 1)
                    else:
                        intersect_x = in_co[j][0]
                        intersect_y = out_co[0][1]
                else:
                    intersect_x = out_co[0][0]
                    intersect_y = in_co[j][1]
                if (intersect_x < out_co[0][0] and intersect_x < out_co[i][0]) or (intersect_x > out_co[0][0] and intersect_x > out_co[i][0]) or (intersect_y < out_co[0][1] and intersect_y < out_co[i][1]) or (intersect_y > out_co[0][1] and intersect_y > out_co[i][1]):
                    temp = math.sqrt((in_co[j][0] - out_co[0][0]) ** 2 + (in_co[j][1] - out_co[0][1]) ** 2)
                    temp2 = math.sqrt((in_co[j][0] - out_co[i][0]) ** 2 + (in_co[j][1] - out_co[i][1]) ** 2)
                    if temp > temp2:
                        d = temp2
                    else:
                        d = temp
                else:
                    if m == 1 and flag == -1:
                        d = abs(m * in_co[j][0] - b)
                    else:
                        d = abs(m * in_co[j][0] - in_co[j][1] + b)
                    if d == 0:
                        temp = math.sqrt((in_co[j][0] - out_co[0][0]) ** 2 + (in_co[j][1] - out_co[0][1]) ** 2)
                        temp2 = math.sqrt((in_co[j][0] - out_co[i][0]) ** 2 + (in_co[j][1] - out_co[i][1]) ** 2)
                        if temp > temp2:
                            d = temp2
                        else:
                            d = temp
                if d < min:
                    min = d
        else:
            if out_co[i + 1][0] == out_co[i][0]:
                flag = -1
                m = 1
                b = out_co[i + 1][0]
            else:
                m = (out_co[i + 1][1] - out_co[i][1]) / (out_co[i + 1][0] - out_co[i][0])
                b = out_co[i + 1][1] - m * out_co[i + 1][0]
            for j in range(len(in_co)):
                if flag != -1:
                    if m != 0:
                        c = in_co[j][1] + (1/ m) * in_co[j][0]
                        intersect_x = (c - b) / (m + (1 / m))
                        intersect_y = ((m ** 2) * c + b) / ((m ** 2) + 1)
                    else:
                        intersect_x = in_co[j][0]
                        intersect_y = out_co[i][1]
                else:
                    intersect_x = out_co[i][0]
                    intersect_y = in_co[j][1]
                if (intersect_x < out_co[i + 1][0] and intersect_x < out_co[i][0]) or (intersect_x > out_co[i + 1][0] and intersect_x > out_co[i][0]) or (intersect_y < out_co[i + 1][1] and intersect_y < out_co[i][1]) or (intersect_y > out_co[i + 1][1] and intersect_y > out_co[i][1]):
                    temp = math.sqrt((in_co[j][0] - out_co[i][0]) ** 2 + (in_co[j][1] - out_co[i][1]) ** 2)
                    temp2 = math.sqrt((in_co[j][0] - out_co[i + 1][0]) ** 2 + (in_co[j][1] - out_co[i + 1][1]) ** 2)
                    if temp > temp2:
                        d = temp2
                    else:
                        d = temp
                else:
                    if m == 1 and flag == -1:
                        d = abs(m * in_co[j][0] - b)
                    else:
                        d = abs(m * in_co[j][0] - in_co[j][1] + b)
                    if d == 0:
                        temp = math.sqrt((in_co[j][0] - out_co[i + 1][0]) ** 2 + (in_co[j][1] - out_co[i + 1][1]) ** 2)
                        temp2 = math.sqrt((in_co[j][0] - out_co[i][0]) ** 2 + (in_co[j][1] - out_co[i][1]) ** 2)
                        if temp > temp2:
                            d = temp2
                        else:
                            d = temp
                if d < min:
                    min = d
    print(min / 2)

in_n = 4
in_co = [(1.0, 1.0), (1.0, 2.0), (2.0, 2.0), (2.0, 1.0)]
out_n = 4
out_co = [(0.0, 0.0), (0.0, 3.0), (3.0, 3.0), (3.0, 0.0)]
main(in_n, in_co, out_n, out_co)
