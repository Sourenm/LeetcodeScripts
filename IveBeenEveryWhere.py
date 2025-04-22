def main(n, lines, city):
    for i in range(n):
        d = {}
        for j in range(lines[i]):
            if city[j] not in d:
                d[city[j]] = 1
            else:
                d[city[j]] += 1
        print(len(d.keys()))

n_sample = 2
lines_sample = [5, 3]
city_sample = ["A", "B", "A", "C", "B", "D", "D", "A", "B"]
main(n_sample, lines_sample, city_sample)