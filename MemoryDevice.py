def main(n, q, temp):
    array = [0 for x in range(n)]
    for i in range(q):
        if temp[i][0] == 1:
            ind = 0
            flag = 0
            while True:
                if array[ind:].count(0) > 0:
                    begin = array[ind:].index(0)
                    ind = array[ind:].index(0)
                    count = 1
                    ind += 1
                    if ind >= len(array):
                        if count == temp[i][1]:
                            for i in range(begin, ind):
                                array[i] = 1
                            print(begin)
                            break
                        else:
                            print(-1)
                    else:
                        while array[ind] == 0:
                            count += 1
                            ind += 1
                            if count == temp[i][1]:
                                for i in range(begin, ind):
                                    array[i] = 1
                                print(begin)
                                flag = 1
                                break
                        if flag == 1:
                            break
                else:
                    print(-1)
                    break
        else:
            for i in range(temp[i][1], temp[i][1] + temp[i][2]):
                array[i] = 0
            print(array.count(0))
n = 15
q = 5
temp = [
    (1, 3, 0),
    (2, 3, 6),
    (1, 2, 0),
    (2, 5, 8),
    (1, 4, 0),
]
main(n, q, temp)