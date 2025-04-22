def main(n, d, init, people):
    init.pop(0)
    counter = 0
    infected = [0 for x in range(n)]
    for i in range(len(init)):
        infected[init[i] - 1] = 1
    next_day = infected.copy()
    while counter < d:
        for i in range(len(infected)):
            if infected[i] == 1:
                for j in range(len(people)):
                    if (people[j][0] <= people[i][1] and people[j][0] >= people[i][0]) or (people[j][1] <= people[i][1] and people[j][1] >= people[i][0]):
                        next_day[j] = 1
        infected = next_day.copy()
        counter += 1
    for i in range(len(next_day)):
        if next_day[i] == 1:
            print(i + 1, end=' ')
    print()
n = 5
d = 3
init = [2, 4]
people = [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
main(n, d, init, people)
