def main(l):
    flag = 0
    moves = []
    vowels = ('A', 'E', 'I', 'O', 'U')
    und_flag = 0
    index = -1
    if 'L' not in l:
        flag = 1
    for i in range(len(l)):
        if l[i] == '_':
            moves.append(0)
            index += 1
            if i > 0 and i < (len(l) - 1):
                if l[i - 1] in vowels:
                    if l[i + 1] in vowels:
                        moves[index] += 24
                    else:
                        moves[index] += 29
                elif l[i - 1] not in vowels and l[i - 1] != '_':
                    if l[i + 1] not in vowels and l[i + 1] != '_':
                        moves[index] += 5
                    else:
                        moves[index] += 29
                elif l[i - 1] == '_':
                    if moves[index - 1] == 5:
                        if i < (len(l) - 1):
                            if l[i + 1] in vowels:
                                moves[index] += 24
                            else:
                                moves[index] += 29
                        else:
                            moves[index] += 29
                    elif moves[index - 1] == 24:
                        if i < (len(l) - 1):
                            if l[i + 1] not in vowels:
                                moves[index] += 5
                            else:
                                moves[index] += 29
                        else:
                            moves[index] += 29
                    elif moves[index - 1] == 29:
                        if i > 1:
                            if l[i - 2] in vowels:
                                moves[index] += 24
                            else:
                                moves[index] += 5
                        else:
                            moves[index] += 29
            else:
                if i == 0 and len(l) > 2:
                    if l[i + 1] in vowels and l[i + 2] in vowels:
                        moves[index] += 24
                    elif l[i + 1] not in vowels and l[i + 2] not in vowels:
                        moves[index] += 5
                    else:
                        moves[index] += 29
                elif i == 0 and len(l) < 2:
                    moves[index] += 29
                elif i == (len(l) - 1) and len(l) > 2:
                    if l[i - 1] in vowels and l[i - 2] in vowels:
                        moves[index] += 24
                    elif l[i - 1] not in vowels and l[i - 2] not in vowels:
                        moves[index] += 5
                    else:
                        moves[index] += 29
                elif i == (len(l) - 1) and len(l) < 2:
                    moves[index] += 29
    final = 1
    if flag == 0:
        for i in range(len(moves)):
            final *= moves[i]
    else:
        temp = 0
        for i in range(len(moves)):
            final += temp
            temp = 1
            for j in range(len(moves)):
                if j != i:
                    temp *= moves[j]
    print(final)
l_sample = ["HELLO_WORLD"]
main(l_sample)
