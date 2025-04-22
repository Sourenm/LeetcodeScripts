def main(n):
    def next_move(c, p):
        if c - 1 == 0:
            return 0
        elif c - (p * 2) == 0:
            return 0
        else:
            if (c - 1) - 1 != 0 and (c - 1) - 2 != 0:
                return c - 1
            elif (c - (p * 2)) - 1 != 0 and (c - (p * 2)) - (p * 4) != 0:
                return c - (p * 2)
            else:
                return c - 1
    out = 1
    turn = 1
    check = n - out
    p = 1
    while out < n:
        if next_move(check, p) == 0:
            if turn == 0:
                print(out)
                break
            else:
                out += 1
                check = n - out
                p = out
        else:
            turn = 1 - turn
            p = check - next_move(check, p)
            check = next_move(check, p)

n_sample = 10
main(n_sample)