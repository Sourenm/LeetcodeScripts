from math import inf
def main(r, c, sum_r, sum_c):
    matrix = [[0 for x in range(c)] for y in range(r)]
    i = 0
    j = 0
    temp_r = sum_r.copy()
    temp_c = sum_c.copy()
    while max(temp_r) != -1:
        i = temp_r.index(max(temp_r))
        value = sum_r[i]
        temp_r[i] = -1
        if value == c:
            matrix[i] = [1 for x in range(c)]
        else:
            count = 0
            ind = []
            check = []
            for k in range(len(temp_c)):
                if temp_c[k] != inf and ind.count(k) == 0:
                    check.append([temp_c[k], k])
            while c - count != value:
                min = inf
                for k in range(len(check)):
                    if check[k][0] < min:
                        min = check[k][0]
                        v = k
                check[v] = [inf, -1]
                ind.append(v)
                count += 1
            for k in range(len(matrix[i])):
                if ind.count(k) == 0:
                    matrix[i][k] = 1
                    temp_c[k] -= 1
                    if temp_c[k] == 0:
                        temp_c[k] = inf
            # for k in range(c):
            #     sum_check_c = 0
            #     for l in range(r):
            #         sum_check_c += matrix[l][k]
            #     if sum_check_c == sum_c[k]:
            #         temp_c[k] = inf
    print(matrix)

main(3, 4, [2, 3, 4], [3, 2, 4, 1])
