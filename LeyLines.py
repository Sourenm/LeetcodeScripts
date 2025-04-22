def main(n, t, coords):
    mx_count = 0
    for i in range(len(coords)):
        m = 0
        y_c = 0
        x_c = 0
        c = 0
        count = 2
        for j in range(i + 1, len(coords)):
            if coords[i][0] - coords[j][0] == 0:
                x_c = coords[i][0]
            elif coords[i][1] - coords[j][1] == 0:
                y_c = coords[i][1]
            else:
                y_c = coords[i][1] - coords[j][1]
                x_c = coords[i][0] - coords[j][0]
                m = y_c / x_c
                c = coords[i][1] - (m * coords[i][0])
            for k in range(j + 1, len(coords)):
                if coords[k][1] - (m * coords[k][0]) < c + t and coords[k][1] - (m * coords[k][0]) > c - t:
                    count += 1
        if count > mx_count:
            mx_count = count
    print(mx_count)
main(5, 2, [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])
