def main(w):
    base = int(w ** (1 / 3))
    base_2 = round(w ** (1 / 3))
    base_3 = base - 1
    if base != base_2 and abs(w - (3 ** base_2)) < abs(w - (3 ** base)):
        base = base_2
    if abs(w - (3 ** base_3)) < abs(w - (3 ** base)):
        base = base_3
    table = []
    table.append(base)
    left_w = []
    right_w = []
    if w - (3 ** base) == 0:
        print(f'left pan: {0}')
        print(f'right pan: {w}')
    else:
        right = 3 ** base
        right_w.append(right)
        left = w
        r = left - right
        while r != 0:
            if r > 0:
                if r == 1:
                    right += 1
                    right_w.append(1)
                    r = left - right
                elif int(r ** (1 / 3)) > 0:
                    base = int(r ** (1 / 3))
                    base_2 = round(r ** (1 / 3))
                    if base != base_2 and abs(r - base_2) < abs(r - base):
                        base = base_2
                    if table.count(base) > 0:
                        if table[0] > 0:
                            base = table[0] - 1
                        else:
                            base = table[-1] + 1
                    table.append(base)
                    table.sort()
                    right += int(3 ** base)
                    right_w.append(3 ** base)
                    r = left - right
                else:
                    right += 3
                    right_w.append(3)
                    r = left - right
            else:
                if r == -1:
                    left += 1
                    left_w.append(1)
                    r = left - right
                elif int(abs(r) ** (1 / 3)) > 0:
                    base = int(abs(r) ** (1 / 3))
                    base_2 = round(abs(r) ** (1 / 3))
                    if base != base_2 and abs(abs(r) - base_2) < abs(abs(r) - base):
                        base = base_2
                    if table.count(base) > 0:
                        if table[0] > 0:
                            base = table[0] - 1
                        else:
                            base = table[-1] + 1
                    table.append(base)
                    table.sort()
                    left += 3 ** base
                    left_w.append(3 ** base)
                    r = left - right
                else:
                    left += 3
                    left_w.append(3)
                    r = left - right
        print('right pan: ',end='')
        print(*right_w, sep=' ')
        print('left pan: ',end='')
        print(*left_w, sep=' ')
    
    

main(10)