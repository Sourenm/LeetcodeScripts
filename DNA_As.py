def main(n, strand):
    moves = 0
    while strand.count('B') > 0:
        start = 0
        b_ind = 0
        e_ind = len(strand)
        for i in range(len(strand)):
            if strand[i] == 'B' and start == 0:
                start = 1
                b_ind = i
            if strand[i] == 'A' and start == 1:
                if len(strand) > i + 1:
                    if strand[i + 1] != 'B':
                        e_ind = i
                        break
                else:
                    e_ind = i
                    break
        if e_ind - b_ind == 1:
            strand[b_ind] = 'A'
        else:
            for i in range(e_ind):
                if strand[i] == 'B':
                    strand[i] = 'A'
                else:
                    strand[i] = 'B'
        moves += 1
    print(moves)
n = 5
strand = ['B', 'A', 'B', 'A', 'B']
main(n, strand)