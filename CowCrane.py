def main(in_p, out_p, t):
    timer = 0
    pos = 0
    choice = -1
    pickedup = [0, 0]
    done = [0, 0]
    if abs(pos - in_p[0]) <= abs(pos - in_p[1]):
        choice = 0
    else:
        choice = 1
    while True:
        if (timer > t[0] and done[0] == 0) or (timer > t[1] and done[1] == 0):
            print('IMPOSSIBLE')
            break
        else:
            if sum(done) == 2:
                print('POSSIBLE')
                break
            if pos != in_p[choice] and done[choice] == 0 and pickedup[choice] == 0:
                timer += 1
                if pos > in_p[choice]:
                    pos -= 1
                else:
                    pos += 1
            elif done[choice] == 0 and pickedup[choice] == 1 and pos != out_p[choice]:
                timer += 1
                if pos > out_p[choice]:
                    pos -= 1
                else:
                    pos += 1
            elif pos == in_p[choice] and done[choice] == 0 and pickedup[choice] == 0:
                timer += 1
                pickedup[choice] = 1
                if pos > out_p[choice]:
                    pos -= 1
                else:
                    pos += 1
            elif done[choice] == 0 and pickedup[choice] == 1 and pos == out_p[choice]:
                timer += 1
                done[choice] = 1
                choice = 1 - choice
                if pos > in_p[choice]:
                    pos -= 1
                else:
                    pos += 1

in_p_sample = [3, 7]
out_p_sample = [9, 2]
t_sample = [5, 10]
main(in_p_sample, out_p_sample, t_sample)
