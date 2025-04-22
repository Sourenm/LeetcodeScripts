from math import inf

def main(n, current):
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
main(5, [[0, 10, 5], [1, 8, 4], [0, 12, 6], [1, 9, 3], [1, 7, 2]])
