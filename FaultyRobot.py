from random import random
from math import inf
def main(n, m, temp):
    d = {}
    for i in range(m):
        if temp[i][0] < 0:
            temp[i][1] *= -1
            temp[i][0] *= -1
        if temp[i][0] not in d:
            d[temp[i][0]] = []
        d[temp[i][0]].append(temp[i][1])
    current = 1
    next = inf
    counter = 0
    end_nodes = []
    r_check = 0
    reset = 0
    cycle = []
    while counter < 500:
        if reset == 1:
            reset = 0
            current = 1
            next = -1
            r_check = 0
        if r_check == 0:
            checker = random()
            if checker < 0.5:
                r_check = 1
        if r_check == 1:
            r_check = -1
            next_choice = d[current]
            r_next = 1 / len(next_choice)
            r = random()
            next = d[current][int(r // r_next)]
            if next < 0:
                next *= -1
        else:
            flag = 0
            if current in d:
                for i in range(len(d[current])):
                    if d[current][i] < 0:
                        flag = 1
                        next = d[current][i] * -1
                        break
            if flag == 0:
                next = current
                reset = 1
                if current not in end_nodes:
                    end_nodes.append(current)
        current = next
        next = inf
        counter += 1
        if current not in cycle:
            cycle.append(current)
        else:
            cycle = []
            reset = 1
    print(len(end_nodes))
n = 3
m = 5
temp = [
    [1, 2],
    [1, 3],
    [2, -4],
    [3, 4],
    [4, -2]
]
# Call the main function with the sample input
main(n, m, temp)