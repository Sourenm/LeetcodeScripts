from random import shuffle
def main(n, c, cards):
    counter = 0
    score = []
    while counter < 5000:
        shuffle(cards)
        flag = 0
        if c != 0:
            check = max(cards[0: c])
        else:
            check = 0
        for i in range(c, len(cards)):
            if cards[i] > check:
                score.append(cards[i])
                flag = 1
                break
        if flag == 0:
            score.append(cards[-1])
        counter += 1
    print(sum(score)/len(score))
n = 10
c = 3
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
main(n, c, cards)
