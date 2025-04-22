from math import inf
def main(n):
    divs = []
    for i in range(2, n):
        if n % i == 0:
            if [i, int(n / i)] not in divs and [int(n / i), i] not in divs:
                divs.append([i, int(n / i)])
    flag = 0
    result = []
    for i in range(len(divs)):
        if (divs[i][0] + divs[i][1]) % 2 == 0:
            n1 = int((divs[i][0] + divs[i][1]) / 2)
            n2 = max(divs[i][0], divs[i][1]) - n1
            if abs(n1 ** 2 - n2 ** 2) == n:
                flag = 1
                result.append([n1, n2])
    if flag == 0:
        print('impossible')
    else:
        min = inf
        min_ind = -1
        for i in range(len(result)):
            if sum(result[i]) < min:
                min = sum(result[i])
                min_ind = i
        print(result[min_ind])

main(4)