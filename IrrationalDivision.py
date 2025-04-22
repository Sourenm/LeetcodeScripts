def main(p, q):
    chocolate = [[0 for x in range(q)] for y in range(p)]
    for i in range(p):
        for j in range(q):
            if i % 2 == 0:
                if j % 2 == 0:
                    chocolate[i][j] = 1
                else:
                    chocolate[i][j] = 0
            else:
                if j % 2 == 0:
                    chocolate[i][j] = 0
                else:
                    chocolate[i][j] = 1
    my_score = 0
    sisters_score = 0
    turn = 0
    while len(chocolate) > 0:
        if turn == 0:
            if len(chocolate) % 2 != 0:
                if chocolate[0][0] == 1:
                    my_score += 1
                    for i in range(len(chocolate)):
                        chocolate[i].pop(0)
                else:
                    if len(chocolate[0]) > 1:
                        for i in range(len(chocolate)):
                            chocolate[i].pop(0)
                            chocolate[i].pop(0)
                    else:
                        my_score -= 1
                        chocolate = []
            else:
                if len(chocolate[0]) == 2:
                    chocolate = []
                    break
                else:
                    for i in range(len(chocolate)):
                        while len(chocolate[i]) != 2:
                            chocolate[i].pop(0)
            turn = 1
        if turn == 1:
            if len(chocolate[-1]) % 2 != 0:
                if chocolate[-1][0] == 1:
                    sisters_score += 1
                    chocolate.pop(-1)
                else:
                    if len(chocolate) > 1:
                        chocolate.pop(-1)
                        chocolate.pop(-1)
                    else:
                        sisters_score -= 1
                        chocolate = []
            else:
                if len(chocolate) == 2:
                    chocolate = []
                    break
                else:
                    while len(chocolate) != 2:
                        chocolate.pop(-1)
            turn = 0
    print(abs(my_score - sisters_score))

main(4, 5)