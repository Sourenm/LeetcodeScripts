import math
def main(n, m, k, plots, circles, squares):
    rad = circles.copy()
    for i in range(len(squares)):
        rad.append(math.sqrt(2 * (squares[i] ** 2)) / 2)
    rad.sort()
    plots.sort()
    count = 0
    done = 0
    index = 0
    ind_rad = 0
    print(rad)
    while ind_rad < len(rad):
        while index < len(plots):
            if rad[ind_rad] < plots[index]:
                print(rad[ind_rad], ' ', plots[index])
                count += 1
                plots.pop(index)
                rad.pop(ind_rad)
                index = -1
                if len(plots) == 0 or len(rad) == 0:
                    done = 1
            if done == 1:
                break
            index += 1
        ind_rad += 1
        if done == 1:
            break
    print(count)

main(
    5,
    4,
    2,
    [3.0, 6.0, 8.0, 12.0, 15.0],
    [2.0, 5.0],
    [4.0, 7.0]
)
