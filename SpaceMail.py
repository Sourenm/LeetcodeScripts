from math import sqrt
def main(n, cords):
    d = {}
    min_d = 0
    for i in range(len(cords) - 1):
        d[i] = []
        for j in range(i + 1, len(cords)):
            d[i].append(sqrt((cords[i][0] - cords[j][0]) ** 2 + (cords[i][1] - cords[j][1]) ** 2 + (cords[i][2] - cords[j][2]) ** 2))
        if min(d[i]) > min_d:
            min_d = min(d[i])
    if int(min_d) != min_d:
        print(int(min_d) + 1)
    else:
        print(min_d)
main(3, [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)])
