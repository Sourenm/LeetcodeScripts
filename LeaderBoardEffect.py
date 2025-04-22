from math import inf
from random import random, choice, randint
def main(n, t, problems):
    teams = 100000
    leaderboard = [0 for y in range(n)]
    team_times = [0 for x in range(teams)]
    solved = [[0 for w in range(n)] for z in range(teams)]
    while sum(team_times) / teams < t:
        for i in range(teams):
            if team_times[i] < t:
                if sum(leaderboard) == 0:
                    p_select = randint(0, n - 1)
                else:
                    temp = []
                    for j in range(len(solved[i])):
                        if solved[i][j] == 1:
                            temp.append(0)
                        else:
                            temp.append(leaderboard[j])
                    if sum(temp) == 0:
                        p_select = randint(0, n - 1)
                        while solved[i][p_select] == 1:
                            p_select = randint(0, n - 1)
                    else:
                        s = sum(temp)
                        for j in range(len(temp)):
                            temp[j] = temp[j] / s
                        choose = random()
                        c = max(temp)
                        if choose < c:
                            p_select = temp.index(c)
                        else:
                            temp[temp.index(c)] = 0
                            while True:
                                c = max(temp)
                                if choose < 1 - c:
                                    p_select = temp.index(c)
                                    break
                                else:
                                    temp[temp.index(c)] = 0
                check = random()
                team_times[i] += problems[p_select][0]
                if check < problems[p_select][2]:
                    solved[i][p_select] = 1
                    team_times[i] += problems[p_select][1]
                    leaderboard[p_select] += 1
    for i in range(len(leaderboard)):
        print(leaderboard[i] / teams)

n = 5
t = 10.0
problems = [
    (2.0, 5.0, 0.8),
    (3.0, 6.0, 0.7),
    (1.0, 4.0, 0.9),
    (2.0, 7.0, 0.6),
    (4.0, 8.0, 0.5),
]
main(n, t, problems)