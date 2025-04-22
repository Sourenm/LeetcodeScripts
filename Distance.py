def main(n, trucks):
    total = 0
    trucks = []
    for i in range(n):
        if len(trucks) > 1:
            for j in range(len(trucks) - 1):
                total += abs(trucks[-1][0] - trucks[j][0]) + abs(trucks[-1][1] - trucks[j][1])
    print(total)
n_sample = 3
trucks_sample = [
    (1, 2),
    (3, 4),
    (5, 6)
]
main(n_sample, trucks_sample)
