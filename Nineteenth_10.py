from math import sqrt
import math
from math import factorial as f
from math import sqrt
from math import pi
from math import e
from math import inf
from random import shuffle

def SpaceMail(n, cords):
    d = {}
    min_d = 0
    for i in range(len(cords) - 1):
        d[i] = []
        for j in range(i + 1, len(cords)):
            d[i].append(sqrt((cords[i][0] - cords[j][0]) ** 2 + (cords[i][1] - cords[j][1]) ** 2 + (cords[i][2] - cords[j][2]) ** 2))
        if min(d[i]) > min_d:
            min_d = min(d[i])
    if int(min_d) != min_d:
        print(int(min_d) + 1)
    else:
        print(min_d)

def SquarePeg(n, m, k, plots, circles, squares):
    rad = circles.copy()
    for i in range(len(squares)):
        rad.append(math.sqrt(2 * (squares[i] ** 2)) / 2)
    rad.sort()
    plots.sort()
    count = 0
    done = 0
    index = 0
    ind_rad = 0
    print(rad)
    while ind_rad < len(rad):
        while index < len(plots):
            if rad[ind_rad] < plots[index]:
                print(rad[ind_rad], ' ', plots[index])
                count += 1
                plots.pop(index)
                rad.pop(ind_rad)
                index = -1
                if len(plots) == 0 or len(rad) == 0:
                    done = 1
            if done == 1:
                break
            index += 1
        ind_rad += 1
        if done == 1:
            break
    print(count)

def SquawkVirus(n, m, s, t, temp):
    d = {}
    for i in range(m):
        if temp[i][0] not in d:
            d[temp[i][0]] = []
        d[temp[i][0]].append(temp[i][1])
        if temp[i][1] not in d:
            d[temp[i][1]] = []
        d[temp[i][1]].append(temp[i][0])
    virus = [0 for x in range(n)]
    virus[s] = 1
    while t > 0:
        next = [0 for x in range(n)]
        for i in range(n):
            if virus[i] > 0:
                if i in d.keys():
                    for v in d[i]:
                        next[v] += virus[i]
        virus = next.copy()
        t -= 1
    print(sum(virus))

def Sretan(n):
    if n > 2:
        digits = n - 2
        it = 2
        while digits > 0:
            digits -= 2**it
            if digits <= 0:
                break
            it += 1
        digits = n
        out = []
        out.append('4')
        for i in range(1, it):
            digits -= 2**i
            out.append('4')
        temp = str(bin(digits - 1)[2:])
        print(temp)
        if len(temp) >= 1:
            for i in range(len(temp)):
                if temp[len(temp) - (i + 1)] == '1':
                    out[len(out) - (i + 1)] = '7'
        print(' '.join(out))
    else:
        if n == 1:
            print('4')
        else:
            print('7')

def StarPuzzle(grids, star):
    valid = 0
    for i in range(10):
        for j in range(1, 10):
            if star[i][j] == '*' and star[i][j - 1] == '*':
                valid = 1
                print('InvalidRow')
    for i in range(1, 10):
        for j in range(10):
            if star[i][j] == '*' and star[i - 1][j] == '*':
                valid = 1
                print('InvalidCol')
    for i in range(9):
        for j in range(9):
            if star[i][j] == '*' and star[i + 1][j + 1] == '*':
                valid = 1
                print('InvalidDiag')
    if valid == 0:
        gcheck = []
        for i in range(10):
            gcheck.append(0)
        valid = 0
        for i in range(10):
            for j in range(10):
                if star[i][j] == '*':
                    gcheck[int(grids[i][j])] += 1
                    if gcheck[int(grids[i][j])] > 2:
                        print('InvalidGrid')
                        valid = 1
                        break
            if valid == 1:
                break
        if valid == 0:
            print('Valid!')

def StirlingApproximation(n):    
    s = sqrt(2 * pi * n) * ((n ** n) / (e ** n))    
    print(f(int(n)) / s)

def StockPrices(n, current):
    bid_pending = []
    sell_pending = []
    bid = -1
    ask = inf
    stock = -1
    for i in range(n):
        if current[i][0] == 'buy':
            bid_pending.append([int(current[i][1]), int(current[i][-1])])
            if int(current[i][-1]) > bid:
                bid = int(current[i][-1])
        if current[i][0] == 'sell':
            sell_pending.append([int(current[i][1]), int(current[i][-1])])
            if int(current[i][-1]) < ask:
                ask = int(current[i][-1])
        ind_b = []
        ind_s = []
        if len(bid_pending) != 0 and len(sell_pending) != 0:
            mx = 1
            temp = bid_pending.copy()
            while mx > 0:
                mx = temp[0][1]
                i = 0
                for k in range(1, len(temp)):
                    if temp[k][1] > mx:
                        mx = temp[k][1]
                        i = k
                if mx == -1:
                    break
                mn = 1
                temp_s = sell_pending.copy()
                while mn > 0:
                    mn = temp_s[0][1]
                    j = 0
                    for k in range(1, len(temp_s)):
                        if temp_s[k][1] < mn:
                            mn = temp_s[k][1]
                            j = k
                    if mn == -1:
                        break
                    if bid_pending[i][1] >= sell_pending[j][1] and sell_pending[j][0] != 0 and bid_pending[i][0] != 0:
                        stock = sell_pending[j][1]
                        if sell_pending[j][0] >= bid_pending[i][0]:
                            sell_pending[j][0] -= bid_pending[i][0]
                            bid_pending[i][0] = 0
                            if sell_pending[j][0] == 0:
                                ind_s.append(j)
                            ind_b.append(i)
                        else:
                            bid_pending[i][0] -= sell_pending[j][0]
                            sell_pending[j][0] = 0
                            ind_s.append(j)
                    temp_s[j][1] = -1
                temp[i][1] = -1
        for i in range(len(ind_b)):
            bid_pending.pop(ind_b[i])
        if len(bid_pending) > 0 and len(ind_b) > 0:
            bid = bid_pending[0][1]
            for i in range(1, len(bid_pending)):
                if bid_pending[i][1] > bid:
                    bid = bid_pending[i][i]
        for i in range(len(ind_s)):
            sell_pending.pop(ind_s[i])
        if len(sell_pending) > 0 and len(ind_s) > 0:
            ask = sell_pending[0][1]
            for i in range(len(sell_pending)):
                if sell_pending[i][1] < ask:
                    ask = sell_pending[i][1]
        if len(sell_pending) == 0:
            ask = inf
        if len(bid_pending) == 0:
            bid = -1
        if bid == -1:
            bid = '-'
        if ask == inf:
            ask = '-'
        if stock == -1:
            stock = '-'
        print(f'{ask} {bid} {stock}')
        if bid == '-':
            bid = -1
        if ask == '-':
            ask = inf
        if stock == '-':
            stock = -1

def StopCard(n, c, cards):
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

def StopCounting(n, cards):
    stop_index = 0
    start_index = 1
    mx = sum(cards) / len(cards)
    while stop_index < len(cards) - 1:
        if stop_index == 0:
            check = sum(cards[start_index:]) / len(cards[start_index:])
        else:
            check = (sum(cards[:stop_index]) + sum(cards[start_index:])) / (len(cards[:stop_index]) + len(cards[start_index:]))
        if check > mx:
            mx = check
        if start_index < len(cards) - 1:
            start_index += 1
        else:
            stop_index += 1
            if stop_index == len(cards) - 1:
                start_index = stop_index
            else:
                start_index = stop_index + 1
    if mx < 0:
        print(0)
    else:
        print(mx)
    
def StringMatching(pat, text):
    positions = []
    for i in range(len(text)):
        if text[i] == pat[0]:
            flag = 0
            for j in range(1, len(pat)):
                if text[i + j] != pat[j]:
                    flag = 1
                    break
            if flag == 0:
                positions.append(i)
    for i in range(len(positions)):
        print(positions[i], end=' ')
    print()


StringMatching(['is', 'a'], ['This', 'is', 'a', 'sample', 'text', 'for', 'testing', 'purposes.'])
StopCounting(5, [1, 2, 3, 4, 5])
n = 10
c = 3
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
StopCard(n, c, cards)
StockPrices(5, [[0, 10, 5], [1, 8, 4], [0, 12, 6], [1, 9, 3], [1, 7, 2]])
StirlingApproximation(4.0)
StarPuzzle(
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
        [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
        [4, 5, 6, 7, 8, 9, 10, 1, 2, 3],
        [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
        [6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
        [7, 8, 9, 10, 1, 2, 3, 4, 5, 6],
        [8, 9, 10, 1, 2, 3, 4, 5, 6, 7],
        [9, 10, 1, 2, 3, 4, 5, 6, 7, 8],
        [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ],
    [
        [' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        [' ', '*', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ']
    ]
)

Sretan(4)
n = 6
m = 5
s = 0
t = 2
temp = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4),
    (3, 5),
]
SquawkVirus(n, m, s, t, temp)
SquarePeg(
    5,
    4,
    2,
    [3.0, 6.0, 8.0, 12.0, 15.0],
    [2.0, 5.0],
    [4.0, 7.0]
)
SpaceMail(3, [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)])
