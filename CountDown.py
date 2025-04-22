from math import sqrt
def main(coords):
    x = []
    y = []
    for i in range(len(coords)):
        if i % 2 == 0:
            x.append(coords[i])
        else:
            y.append(coords[i])
    if len(x) == 1:
        print(100)
    elif len(x) == 2:
        print(2 * sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2))
    else:
        dropouts = []
        keep_ins = []
        current = 0
        while (len(dropouts) + len(keep_ins)) < len(x):
            distances = []
            for i in range(len(x)):
                distances.append(sqrt(x[i] ** 2 + y[i] ** 2))
            if len(keep_ins) == 0:
                keep_ins.append(distances.index(max(distances)))
                x[keep_ins[-1]] = 0
                y[keep_ins[-1]] = 0
            else:
                current = distances.index(max(distances))
                if current in keep_ins:
                    break
                else:
                    flag = 0
                    for i in range(len(keep_ins)):
                        if coords[(2 * keep_ins[i])] > 0 and coords[(2 * keep_ins[i]) + 1] > 0:
                            if coords[(2 * keep_ins[i])] < x[current] or coords[(2 * keep_ins[i]) + 1] < y[current]:
                                flag = 1
                                break
                        elif coords[(2 * keep_ins[i])] < 0 and coords[(2 * keep_ins[i]) + 1] < 0:
                            if coords[(2 * keep_ins[i])] > x[current] or coords[(2 * keep_ins[i]) + 1] > y[current]:
                                flag = 1
                                break
                        elif coords[(2 * keep_ins[i])] > 0 and coords[(2 * keep_ins[i]) + 1] < 0:
                            if coords[(2 * keep_ins[i])] < x[current] or coords[(2 * keep_ins[i]) + 1] > y[current]:
                                flag = 1
                                break
                        elif coords[(2 * keep_ins[i])] < 0 and coords[(2 * keep_ins[i]) + 1] > 0:
                            if coords[(2 * keep_ins[i])] > x[current] or coords[(2 * keep_ins[i]) + 1] < y[current]:
                                flag = 1
                                break
                    if flag == 0:
                        dropouts.append(current)
                        x[current] = 0
                        y[current] = 0
                    else:
                        keep_ins.append(current)
                        x[current] = 0
                        y[current] = 0
                        to_del = []
                        for i in range(len(keep_ins)):
                            flag = 0
                            for j in range(i + 1, len(keep_ins)):
                                if coords[(2 * keep_ins[j])] >= 0 and coords[(2 * keep_ins[j]) + 1] >= 0:
                                    if coords[(2 * keep_ins[j])] > coords[(2 * keep_ins[i])] and coords[(2 * keep_ins[j]) + 1] > coords[(2 * keep_ins[i]) + 1]:
                                        flag = 1
                                        break
                                elif coords[(2 * keep_ins[j])] < 0 and coords[(2 * keep_ins[j]) + 1] < 0:
                                    if coords[(2 * keep_ins[j])] < coords[(2 * keep_ins[i])] and coords[(2 * keep_ins[j]) + 1] < coords[(2 * keep_ins[i]) + 1]:
                                        flag = 1
                                        break
                                elif coords[(2 * keep_ins[j])] > 0 and coords[(2 * keep_ins[j]) + 1] < 0:
                                    if coords[(2 * keep_ins[j])] > coords[(2 * keep_ins[i])] and coords[(2 * keep_ins[j]) + 1] < coords[(2 * keep_ins[i]) + 1]:
                                        flag = 1
                                        break
                                else:
                                    if coords[(2 * keep_ins[j])] < coords[(2 * keep_ins[i])] and coords[(2 * keep_ins[j]) + 1] > coords[(2 * keep_ins[i]) + 1]:
                                        flag = 1
                                        break
                            if flag == 1:
                                to_del.append(i)
                        if len(to_del) > 0:
                            for i in range(len(to_del)):
                                keep_ins.pop(to_del[i])
                                dropouts.append(to_del[i])
        total_d = 0
        for i in range(1, len(keep_ins)):
            total_d += ((coords[(2 * keep_ins[i - 1])] - coords[(2 * keep_ins[i])]) ** 2 + (coords[(2 * keep_ins[i - 1]) + 1] - coords[(2 * keep_ins[i]) + 1]) ** 2) ** 0.5
            if i == len(keep_ins) - 1:
                total_d += ((coords[(2 * keep_ins[0])] - coords[(2 * keep_ins[i])]) ** 2 + (coords[(2 * keep_ins[0]) + 1] - coords[(2 * keep_ins[i]) + 1]) ** 2) ** 0.5
        print(100 * (len(coords) / 2) / (1 + total_d))
    
        #check to see if the point is inside all other points in 2 places
coords = [10.0, 5.0, -5.0, 8.0, -2.0, -6.0, 3.0, -4.0, 1.0, 2.0]
main(coords)
