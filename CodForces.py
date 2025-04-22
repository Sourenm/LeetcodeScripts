def main(n, k, contest):
    division = 1
    start = 0
    count = 0
    while division < k + 1:
        if division in contest[start:]:
            ind = start + contest[start:].index(division)
            count += ind - start
            start = ind
            division += 1
        else:
            count += len(contest) - (start + 1)
            start = 0
    print(count + 1)
n = 10
k = 3
contest = [1, 2, 1, 3, 1, 2, 1, 2, 3, 3]
main(n, k, contest)
