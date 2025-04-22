def main(n, cards):
    d = {}
    d_ind = {}
    d_ind['h'] = []
    d_ind['c'] = []
    d_ind['s'] = []
    d_ind['d'] = []
    d['h'] = []
    d['c'] = []
    d['s'] = []
    d['d'] = []
    total_moves = 0
    for i in range(len(cards)):
        if cards[i][0] == 'T':
            d[cards[i][1]].append(10)
        elif cards[i][0] == 'J':
            d[cards[i][1]].append(11)
        elif cards[i][0] == 'Q':
            d[cards[i][1]].append(12)
        elif cards[i][0] == 'K':
            d[cards[i][1]].append(13)
        else:
            d[cards[i][1]].append(int(cards[i][0]))
        d_ind[cards[i][1]].append(i)
    order = []
    pop_ind = []
    sorted = []
    moves = []
    for i in d.keys():
        ascending = 0
        descending = 0
        if len(d[i]) != 0:
            if len(d[i]) > 1:
                sorted.append(0)
            for j in range(len(d[i])):
                for k in range(j + 1, len(d[i])):
                    if d[i][k] >= d[i][j]:
                        ascending += 1
                    else:
                        descending += 1
            if ascending >= descending:
                moves.append(((len(d[i]) * (len(d[i]) - 1)) / 2) - ascending)
                order.append(1)
            else:
                moves.append(((len(d[i]) * (len(d[i]) - 1)) / 2) - descending)
                order.append(-1)
        elif len(d[i]) == 0:
            pop_ind.append(i)
        elif len(d[i]) == 1:
            sorted.append(0.5)
            moves.append(0)
    for i in pop_ind:
        d.pop(i)
        d_ind.pop(i)
    move_count = 0
    for i in d_ind.keys():
        check = d_ind[i][0]
        for j in range(1, len(d_ind[i])):
            if d_ind[i][j] != check + 1:
                moves[move_count] += 1
                check = d_ind[i][j]
        move_count += 1
    print()

n = 5
cards = [('2', 'h'), ('3', 'h'), ('4', 'h'), ('5', 'c'), ('6', 'c')]
main(n, cards)