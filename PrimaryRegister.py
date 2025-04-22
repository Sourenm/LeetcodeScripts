def main(reg):
    operations = 0
    while reg[len(reg) - 1] < 19:
        if reg[0] == 0:
            reg[0] += 1
            operations += 1
        else:
            reg[0] = 0
            if reg[1] != 2:
                reg[1] += 1
                operations += 1
            else:
                reg[1] = 0
                if reg[2] != 4:
                    reg[2] += 1
                    operations += 1
                else:
                    reg[2] = 0
                    if reg[3] != 6:
                        reg[3] += 1
                        operations += 1
                    else:
                        reg[3] = 0
                        if reg[4] != 10:
                            reg[4] += 1
                            operations += 1
                        else:
                            reg[4] = 0
                            if reg[5] != 12:
                                reg[5] += 1
                                operations += 1
                            else:
                                reg[5] = 0
                                if reg[6] != 16:
                                    reg[6] += 1
                                    operations += 1
                                else:
                                    reg[6] = 0
                                    if reg[7] != 18:
                                        reg[7] += 1
                                        operations += 1
                                    else:
                                        break
    print(operations)

main([0, 0, 0, 0, 0, 0, 0, 0])
