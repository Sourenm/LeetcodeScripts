def main(n, k, temp):
    bits = [0 for x in range(n)]
    for i in range(k):
        if temp[i][0] == 'F':
            bits[int(temp[i][1]) - 1] = 1 - bits[int(temp[i][1]) - 1]
        elif temp[i][0] == 'C':
            no = bits[int(temp[i][1]) - 1 : int(temp[i][2])]
            print(sum(no))

main(5, 3, [('F', 1, 0), ('C', 2, 4), ('F', 3, 0)])
