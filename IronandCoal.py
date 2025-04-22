def main(n, m, iron, coal, temp):
    d = {}
    flag_iron = 0
    flag_coal = 0
    iron_count = 0
    coal_count = 0
    for i in range(n):
        d[i + 1] = temp[i][1:]
    path = d[1].copy()
    for i in range(len(path)):
        if path[i] in iron:
            iron_count = 1
            flag_iron = 1
        if path[i] in coal:
            coal_count = 1
            flag_coal = 1
    if flag_iron == 1 and flag_coal == 1:
        print(2)
    else:
        while True:
            change_flag = 0
            path_ind = []
            for i in range(len(path)):
                if path[i] in d and path[i] != 1:
                    for j in range(len(d[path[i]])):
                        if d[path[i]][j] != 1:
                            path_ind.append([path[i], j])
            else:
                for i in range(len(path_ind)):
                    if d[path_ind[i][0]][path_ind[i][1]] not in path:
                        path.append(d[path_ind[i][0]][path_ind[i][1]])
                        change_flag = 1
                        if path[-1] in iron and flag_iron == 0:
                            flag_iron = 1
                            check = path[-1]
                            while True:
                                for j in d.keys():
                                    if check in d[j]:
                                        if check not in coal:
                                            iron_count += 1
                                        check = j
                                if check == 1:
                                    break
                        if path[-1] in coal and flag_coal == 0:
                            flag_coal = 1
                            check = path[-1]
                            while True:
                                for j in d.keys():
                                    if check in d[j]:
                                        if check not in iron:
                                            coal_count += 1
                                        check = j
                                        break
                                if check == 1:
                                    break
            if change_flag == 0:
                break
        if flag_iron == 0 or flag_coal == 0:
            print('Impossible')
        else:
            print(coal_count + iron_count)
    

n = 5
m = 5
iron = [3, 4]
coal = [5]
temp = [[1, 2, 3], [1, 4], [3, 5], [2, 4], [4, 5]]
main(n, m, iron, coal, temp)