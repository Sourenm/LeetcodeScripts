from math import inf
def main(n, temp):
    delegates = []
    federals = []
    constituents = []
    undecided = []
    total_federals = 0
    total_constituents = 0
    done = []
    left_to_decide = 0
    min_to_change = []
    for i in range(n):
        delegates.append(temp[i][0])
        constituents.append(temp[i][1])
        federals.append(temp[i][2])
        undecided.append(temp[i][3])
        if constituents[-1] + undecided[-1] <= federals[-1]:
            total_federals += delegates[-1]
            done.append(1)
            min_to_change.append(inf)
        elif federals[-1] + undecided[-1] <= constituents[-1]:
            total_constituents += delegates[-1]
            done.append(1)
            min_to_change.append(inf)
        else:
            done.append(0)
            left_to_decide += delegates[-1]
            min_to_change.append(int(undecided[-1] / 2) + 1)
    if total_constituents + left_to_decide <= total_federals:
        print('Impossible')
    else:
        d_left = int((sum(delegates) - (total_federals + total_constituents)) / 2) + (total_federals - total_constituents)
        if d_left + total_constituents == sum(delegates) / 2:
            d_left += 1
        total = 0
        while True:
            mx = 0
            mx_ind = 0
            for i in range(len(done)):
                if done[i] != 1:
                    if delegates[i] > mx:
                        mx = delegates[i]
                        mx_ind = i
            done[mx_ind] = 1
            total += min_to_change[mx_ind]
            d_left -= delegates[mx_ind]
            if d_left <= 0:
                print(total)
                break
            min_to_change[mx_ind] = inf
n = 3
temp = [[2, 3, 4, 5], [1, 5, 2, 4], [3, 2, 1, 6]]
main(n, temp)
