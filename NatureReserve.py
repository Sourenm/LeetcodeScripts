from math import inf
def main(n, m, l, s, init_s, b, e, c):
    d = {}
    
    for i in range(m):
        if b[i] not in d:
            d[b[i]] = []
        if e[i] not in d:
            d[e[i]] = []
        d[b[i]].append([e[i], c[i]])
        d[e[i]].append([b[i], c[i]])
    total_c = 0
    while len(init_s) != n:
        min_c = inf
        d_ind = 0
        d_inside_ind = 0
        for i in range(len(init_s)):
            if init_s[i] in d:
                for j in range(len(d[init_s[i]])):
                    if d[init_s[i]][j][1] < min_c and d[init_s[i]][j][0] not in init_s:
                        min_c = d[init_s[i]][j][1]
                        d_ind = i
                        d_inside_ind = j
        total_c += min_c + l
        init_s.append(d[init_s[d_ind]][d_inside_ind][0])
    print(total_c)
    
    

main(5, 7, 2, [1, 2, 3], [1], [1, 2, 2, 3, 4, 4, 5], [2, 3, 4, 4, 5, 5, 1], [3, 5, 2, 1, 3, 4, 1])
