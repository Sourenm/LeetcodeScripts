def main(H, T):
    S = 0
    while H > 0 or T > 0:
        if H >= 2:
            print('2 Heads Removed!')
            H -= 2
            S += 1
        elif T >= 2:
            print('2 Tails Removed!')
            T -= 2
            H += 1
            S += 1
        elif H >= 1:
            print('1 Head Removed!')
            S += 1
        elif T >= 1:
            print('1 Tail Removed!')
            T += 1
            S += 1
        print(H, ' ', T)
    print('The Hydra Was Killed in ', S, ' Moves!')

H_sample = 5
T_sample = 3
main(H_sample, T_sample)
