def main(n):
    disks = [0 for i in range(len(n))]
    for i in range(len(n)):
        if n[i] == 'A':
            disks[i] = 1
        elif n[i] == 'B':
            disks[i] = 2
        elif n[i] == 'C':
            disks[i] = 3
    flag = 0
    for i in range(1, len(disks)):
        if disks[i] != disks[0]:
            flag = 1
            break
    if flag == 0:
        if disks[0] == 2:
            print(0)
        else:
            print(2 ** len(disks) - 1)
    else:
        s = 2 ** len(disks) - 1
        test_disks = [1 for x in range(len(disks))]
        a_ind = 0
        b_ind = -1
        c_ind = -1
        rep_no = 0
        moves = 0
        while test_disks != disks:
            if len(test_disks) % 2 == 0:
                if rep_no == 0:
                    if a_ind < c_ind or c_ind == -1:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 1:
                                c_ind = i
                                test_disks[i] = 3
                                break
                        if test_disks.count(1) == 0:
                            a_ind = -1
                        else:
                            a_ind = test_disks.index(1)
                    else:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 3:
                                a_ind = i
                                test_disks[i] = 1
                                break
                        if test_disks.count(3) == 0:
                            c_ind = -1
                        else:
                            c_ind = test_disks.index(3)
                    rep_no += 1
                elif rep_no == 1:
                    if a_ind < b_ind or b_ind == -1:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 1:
                                b_ind = i
                                test_disks[i] = 2
                                break
                        if test_disks.count(1) == 0:
                            a_ind = -1
                        else:
                            a_ind = test_disks.index(1)
                    else:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 2:
                                a_ind = i
                                test_disks[i] = 1
                                break
                        if test_disks.count(2) == 0:
                            b_ind = -1
                        else:
                            b_ind = test_disks.index(2)
                    rep_no += 1
                elif rep_no == 2:
                    if b_ind < c_ind or c_ind == -1:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 2:
                                c_ind = i
                                test_disks[i] = 3
                                break
                        if test_disks.count(2) == 0:
                            b_ind = -1
                        else:
                            b_ind = test_disks.index(2)
                    else:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 3:
                                b_ind = i
                                test_disks[i] = 2
                                break
                        if test_disks.count(3) == 0:
                            c_ind = -1
                        else:
                            c_ind = test_disks.index(3)
                    rep_no = 0
            else:
                if rep_no == 1:
                    if a_ind < c_ind or c_ind == -1:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 1:
                                c_ind = i
                                test_disks[i] = 3
                                break
                        if test_disks.count(1) == 0:
                            a_ind = -1
                        else:
                            a_ind = test_disks.index(1)
                    else:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 3:
                                a_ind = i
                                test_disks[i] = 1
                                break
                        if test_disks.count(3) == 0:
                            c_ind = -1
                        else:
                            c_ind = test_disks.index(3)
                    rep_no += 1
                elif rep_no == 0:
                    if a_ind < b_ind or b_ind == -1:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 1:
                                b_ind = i
                                test_disks[i] = 2
                                break
                        if test_disks.count(1) == 0:
                            a_ind = -1
                        else:
                            a_ind = test_disks.index(1)
                    else:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 2:
                                a_ind = i
                                test_disks[i] = 1
                                break
                        if test_disks.count(2) == 0:
                            b_ind = -1
                        else:
                            b_ind = test_disks.index(2)
                    rep_no += 1
                elif rep_no == 2:
                    if b_ind < c_ind or c_ind == -1:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 2:
                                c_ind = i
                                test_disks[i] = 3
                                break
                        if test_disks.count(2) == 0:
                            b_ind = -1
                        else:
                            b_ind = test_disks.index(2)
                    else:
                        for i in range(len(test_disks)):
                            if test_disks[i] == 3:
                                b_ind = i
                                test_disks[i] = 2
                                break
                        if test_disks.count(3) == 0:
                            c_ind = -1
                        else:
                            c_ind = test_disks.index(3)
                    rep_no = 0
            moves += 1
        print(s - moves)
n = "AABBB"
main(n)