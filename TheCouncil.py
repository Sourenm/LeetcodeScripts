def main(n, m, temp, town_values):
    d = {}
    roads_sum = [0 for x in range(n)]
    for i in range(m):
        if temp[i][0] - 1 not in d:
            d[temp[i][0] - 1] = []
        if temp[i][1] - 1 not in d:
            d[temp[i][1] - 1] = []
        d[temp[i][0] - 1].append(temp[i][2])
        d[temp[i][1] - 1].append(temp[i][2])
        roads_sum[temp[i][0] - 1] += temp[i][2]
        roads_sum[temp[i][1] - 1] += temp[i][2]
    heaviest = []
    for i in range(n):
        heaviest.append(town_values[i] * roads_sum[i])
    
    temp = roads_sum.copy()
    one_side = []
    one_side_ind = []
    other_side_ind = [i for i in range(n)]
    one_side.append(temp[heaviest.index(max(heaviest))])
    one_side_ind.append(heaviest.index(max(heaviest)))
    other_side_ind.pop(heaviest.index(max(heaviest)))
    temp.pop(one_side_ind[-1])
    other_side = temp.copy()
    one_side_sum = sum(one_side)
    other_side_sum = sum(other_side)
    while True:
        if one_side_sum == other_side_sum:
            sum2 = sum(heaviest)
            sum1 = 0
            for i in range(len(one_side_ind)):
                sum1 += heaviest[one_side_ind[i]]
            sum2 -= sum1
            print(abs(sum2 - sum1))
            if sum2 > sum1:
                for i in range(n):
                    if one_side_ind.count(i) > 0:
                        print(-1 * one_side[one_side_ind.index(i)], end=' ')
                    else:
                        print(other_side[other_side_ind.index(i)], end=' ')
            else:
                for i in range(n):
                    if one_side_ind.count(i) > 0:
                        print(one_side[one_side_ind.index(i)], end=' ')
                    else:
                        print(-1 * other_side[other_side_ind.index(i)], end=' ')
            print()
            break
        elif one_side_sum > other_side_sum:
            if (one_side_sum - other_side_sum) / 2 == min(one_side):
                other_side.append(min(one_side))
                other_side_ind.append(roads_sum.index(min(one_side)))
                one_side_ind.pop(one_side.index(min(one_side)))
                one_side.pop(min(one_side))
                one_side_sum = sum(one_side)
                other_side_sum = sum(other_side)
        elif one_side_sum < other_side_sum:
            if (other_side_sum - one_side_sum) / 2 == min(other_side):
                one_side.append(min(other_side))
                one_side_ind.append(roads_sum.index(min(other_side)))
                other_side_ind.pop(other_side.index(min(other_side)))
                other_side.pop(other_side.index(min(other_side)))
                one_side_sum = sum(one_side)
                other_side_sum = sum(other_side)
main(2, 1, [(1, 2, 3)], [2, 1])
