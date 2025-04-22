from itertools import permutations as perm
from random import shuffle
def main(n):
    bells = []
    for i in range(n):
        bells.append(i + 1)
    p = list(perm(bells, len(bells)))
    current = []
    current.append(p[0])
    temp = p[1:]
    len_check = 0
    stat = 0
    while len(temp) > 0:
        if len_check == 1:
            if len(temp) == stat:
                current = []
                current.append(p[0])
                temp = p[1:]
                shuffle(temp)
            else:
                len_check = 0
        if len_check == 0:
            stat = len(temp)
            len_check = 1
        for i in range(len(temp)):
            flag = 0
            check = temp[i]
            for j in range(len(check)):
                if j == 0:
                    if check[j] != current[-1][1] and check[j] != current[-1][0]:
                        flag = 1
                        break
                elif j == (len(check) - 1):
                    if check[j] != current[-1][-2] and check[j] != current[-1][-1]:
                        flag = 1
                        break
                else:
                    if check[j] != current[-1][j - 1] and check[j] != current[-1][j + 1] and check[j] != current[-1][j]:
                        flag = 1
                        break
            if flag == 0:
                current.append(check)
                temp.pop(i)
                break
    print(current)

main(10)