import math
from math import sqrt
def main(goal):
    a = 1
    b = 1
    results = []
    check = 1
    while True:
        br_flag = 0
        init_a = a
        init_b = b
        while True:
            temp = b
            b = a + b
            a = temp
            if b == goal:
                results.append([init_a, init_b])
                br_flag = 1
                break
            elif b > goal:
                break
        if br_flag == 1:
            break
        flag = 0
        if init_b > init_a + 8:
            a = init_a + 1
            b = init_b
        else:
            a = 1
            b = init_b + 1
        if init_b >= goal - 1 or init_a >= goal - 1:
            break
    print(results[0])
    

goal_sample = 13
main(goal_sample)