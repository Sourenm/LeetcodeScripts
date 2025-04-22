def main(n, points):
    counter = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            if d == 2018:
                counter += 1
    print(counter)
n = 5
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
main(n, points)