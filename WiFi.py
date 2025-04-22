def main(ac, nm, positions):
    mx_pos = 0
    while ac > 0:
        max_ind = -1
        max_val = 0
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                if positions[j] - positions[i] > max_val:
                    max_val = positions[j] - positions[i]
                    max_ind = j
        positions.pop(max_ind)
        ac -= 1
        if ac == 1:
            temp = 0
            max_pos = (max(positions) - min(positions)) / len(positions)
            break
    print(max_pos)
ac = 3
nm = 5
positions = [2, 8, 1, 6, 7]
main(ac, nm, positions)
