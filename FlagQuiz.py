def main(q, n, alts):
    max_change = [0 for x in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                check = 0
                if alts[i][0] != alts[j][0]:
                    check += 1
                if alts[i][1] != alts[j][1]:
                    check += 1
                if alts[i][2] != alts[j][2]:
                    check += 1
                if check > max_change[i]:
                    max_change[i] = check
    print(alts[max_change.index(min(max_change))])
q_sample = 2
n_sample = 3
alts_sample = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
main(q_sample, n_sample, alts_sample)
