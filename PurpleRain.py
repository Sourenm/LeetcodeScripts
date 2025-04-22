def main(n):
    b_ind = -1
    end_ind = -1
    mx = -1
    for i in range(len(n)):
        count_back = i + 1
        while count_back < len(n):
            blues = 0
            reds = 0
            for j in range(i, count_back):
                if n[j] == 'B':
                    blues += 1
                else:
                    reds += 1
            if abs(blues - reds) > mx:
                b_ind = i
                end_ind = count_back - 1
                mx = abs(blues - reds)
            count_back += 1
    print(b_ind + 1, ' ', end_ind + 1)

main(['A', 'B', 'C', 'D'])