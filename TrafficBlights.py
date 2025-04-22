from math import factorial as f
from random import randint
def main(n, temp):
    pos = []
    r_timer = []
    g_timer = []
    for i in range(n):
        pos.append(temp[i][0])
        r_timer.append(temp[i][1])
        g_timer.append(temp[i][2])
    counter = 0
    lights = [0 for y in range(n + 1)]
    while counter < 10:
        passed = 0
        car = randint(0, f(10))
        car_pos = 0
        clock = car + sum(r_timer) + sum(pos)
        timer = r_timer.copy()
        turn = ['r' for x in range(n)]
        for i in range(clock):
            for j in range(len(timer)):
                timer[j] -= 1
                if timer[j] == 0:
                    if turn[j] == 'r':
                        timer[j] = g_timer[j]
                        turn[j] = 'g'
                    else:
                        timer[j] = r_timer[j]
                        turn[j] = 'r'
            if  i > car:
                car_pos += 1
                if car_pos in pos:
                    print(turn)
                    check = pos.index(car_pos)
                    print(pos[check])
                    print(turn[check])
                    if turn[check] == 'r':
                        lights[check] += 1
                        break
                    else:
                        passed += 1
                        if passed == n:
                            lights[-1] += 1
                            break
        counter += 1
    for i in range(len(lights)):
        print(lights[i] / sum(lights))

main(3, [[2, 5, 3], [4, 7, 2], [6, 4, 6]])
