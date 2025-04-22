from random import random
def main(dl, dw, g, l):    
    g /= 100
    l /= 100
    count = 0
    attempts = []
    while count < 5000:
        p = 0
        hands = 0
        while True:
            hands += 1
            check = random()
            if check < l:
                p += dl
                if p > 100:
                    p = 100
            else:
                p += dw
                if p > 100:
                    p = 100
            check2 = random()
            if check2 < p:
                gorilla = random()
                if gorilla < g:
                    attempts.append(hands)
                    break
                else:
                    p = 0
        count += 1
    print(sum(attempts) / len(attempts))

main(1.5, 0.5, 5, 40)
