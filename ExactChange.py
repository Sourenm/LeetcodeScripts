from itertools import combinations as c
from math import inf
def main(goal, n, coins):
    combos = []
    for i in range(n):
        temp = list(c(coins, i))
        for j in range(len(temp)):
            combos.append(temp[j])
    
    min_dif = inf
    final = []
    for i in range(len(combos)):
        if sum(combos[i]) >= goal:
            if sum(combos[i]) - goal < min_dif:
                min_dif = sum(combos[i]) - goal
                final = combos[i]
    print(sum(final), len(final))
goal_sample = 15
n_sample = 4
coins_sample = [1, 2, 5, 10]
main(goal_sample, n_sample, coins_sample)
