def main(d, u, temp):
    menu = []
    retired = []
    ind = []
    count = 0
    while count < u:
        for i in range(len(ind)):
            if retired[ind[i]] != d:
                retired[ind[i]] += 1
            if len(temp[i]) > 1:
                ind.append(int(temp[i][1]) - 1)
            if len(temp[i]) == 1:
                if len(retired) > 0:
                    flag = 0
                    ret_index = 0
                    for i in range(len(retired)):
                        if retired[i] == d:
                            menu[i] = temp[i][0]
                            retired[i] = 1
                            ret_index = i
                            ind.pop(i - 1)
                            flag = 1
                            break
                    if flag == 0:
                        menu.append(temp[i][0])
                        retired.append(0)
                        print(len(retired))
                    else:
                        print(ret_index + 1)
                else:
                    menu.append(temp[i][0])
                    retired.append(1)
                    print(retired[-1])
        count += 1
main(3, 5, [[0, 1], [3, 2], [4, 5]])
