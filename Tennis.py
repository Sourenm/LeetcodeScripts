def main(player1, player2, n, matches):
    flag = 0
    if player1 == 'federer':
        flag = 1
    elif player2 == 'federer':
        flag = 2
    
    for i in range(len(matches)):
        set = matches[i]
        p1 = 0
        p2 = 0
        for j in range(len(set)):
            game = list(set[j])
            if j != 2:
                if game[0] == '6' or game[0] == '7':
                    if game[0] == '6' and int(game[-1]) < 5:
                        p1 += 1
                    elif game[0] == '7' and int(game[-1]) < 7:
                        p1 += 1
                elif game[-1] == '6' or game[-1] == '7':
                    if game[-1] == '6' and int(game[0]) < 5:
                        p2 += 1
                    elif game[-1] == '7' and int(game[0]) < 7:
                        p2 += 1
            else:
                if (game[0] == '6' or game[0] == '7' or game[0] == '8') and game[-1] != '8':
                    if game[0] == '6' and int(game[-1]) < 5:
                        p1 += 1
                    elif game[0] == '7' and int(game[-1]) < 7:
                        p1 += 1
                    elif game[0] == '8' and int(game[-1]) < 7:
                        p1 += 1
                elif game[-1] == '6' or game[-1] == '7' or game[-1] == '8':
                    if game[-1] == '6' and int(game[0]) < 5:
                        p2 += 1
                    elif game[-1] == '7' and int(game[0]) < 7:
                        p2 += 1
                    elif game[-1] == '8' and int(game[0]) < 7:
                        p2 += 1
        if flag == 1:
            if p1 == 2:
                if p2 == 0:
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')
        elif flag == 2:
            if p2 == 2:
                if p1 == 0:
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')
        else:
            if p1 == 2:
                if p2 != 2:
                    print('YES')
                else:
                    print('NO')
            elif p2 == 2:
                if p1 != 2:
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')
main("nadal", "federer", 3, [["6-2", "6-3", "7-6"], ["6-4", "7-6", "6-3"], ["7-5", "4-6", "6-4"]])
